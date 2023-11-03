from testflows.core import *
from testflows.asserts import *
from alter.table.replace_partition.requirements.requirements import *
from helpers.common import getuid, replace_partition
from alter.table.replace_partition.common import (
    check_partition_was_replaced,
    create_two_tables_partitioned_by_column_with_data,
    create_partitions_with_random_uint64,
    create_table_partitioned_by_column_with_data,
)
from helpers.alter import *
from helpers.datatypes import UInt64, UInt8, DateTime
from helpers.tables import Column
from helpers.create import (
    partitioned_replicated_merge_tree_table,
)


@TestScenario
@Requirements(
    RQ_SRS_032_ClickHouse_Alter_Table_ReplacePartition_Concurrent_Merges("1.0")
)
def merges_on_unrelated_partition(self):
    """Check that replace partition is not stopped when concurrent merges happen on another partition."""
    destination_table = "destination_" + getuid()
    source_table = "source_" + getuid()
    node = self.context.node

    with Given("I have a table partitioned by a column"):
        create_table_partitioned_by_column_with_data(table_name=destination_table)

    with When("I stop merges on the destination table"):
        node.query(f"SYSTEM STOP MERGES {destination_table}")

    with And("I insert data into the destination table to create new parts"):
        node.query(
            f"insert into {destination_table} (p, i) select 1, number from numbers(100);"
        )
        node.query(
            f"ALTER TABLE {destination_table} ADD COLUMN make_merge_slower UInt8 DEFAULT sleepEachRow(0.03);"
        )

    with And(
        "I create a source table with the same structure as the destination table"
    ):
        node.query(f"CREATE TABLE {source_table} AS {destination_table}")

    with And("I populate both tables with more data to create partitions"):
        create_partitions_with_random_uint64(table_name=destination_table)
        create_partitions_with_random_uint64(table_name=source_table)

    with Then(
        "I start merges on the destination table and execute optimize deduplicate to initiate merges on the destination table"
    ):
        node.query(f"SYSTEM START MERGES {destination_table}")
        node.query(
            f"OPTIMIZE TABLE {destination_table} PARTITION id '1' DEDUPLICATE BY p;"
        )

    with And(
        "I replace partition on the destination table from the source table's partition on which no merges are happening"
    ):
        replace_partition(
            destination_table=destination_table, source_table=source_table, partition=2
        )

    with Check("I check that partition on the destination table was replaced"):
        check_partition_was_replaced(
            destination_table=destination_table, source_table=source_table, partition=2
        )

    with Check("that the merge was finished"):
        node.query(
            f"SELECT is_mutation, partition_id FROM system.merges WHERE database==currentDatabase() AND table=='{destination_table}';"
        )

        fail()


@TestScenario
@Requirements(
    RQ_SRS_032_ClickHouse_Alter_Table_ReplacePartition_Concurrent_Mutations("1.0")
)
def mutations_on_unrelated_partition(self):
    """Check that replace partition is not stopped when concurrent mutations happen on another partition."""
    destination_table = "destination_" + getuid()
    source_table = "source_" + getuid()
    node = self.context.node

    with Given(
        "I have two tables with the same structure that are partitioned by the same column"
    ):
        create_two_tables_partitioned_by_column_with_data(
            destination_table=destination_table, source_table=source_table
        )

    with When(
        "I update the destination table with arbitrary sleep so that mutation takes long enough time"
    ):
        old_data = node.query(
            f"SELECT i FROM {destination_table} WHERE p == 1 ORDER BY tuple(*)"
        )

        alter_table_update_column(
            table_name=destination_table,
            column_name="i",
            expression="if(sleep(1), 0, 9000) IN PARTITION id '1'",
            condition="p == 1",
        )

    with And("I check that the mutation was started"):
        node.query(
            f"SELECT is_done, latest_fail_reason, parts_to_do FROM system.mutations WHERE database==currentDatabase() "
            f"AND table=='{destination_table}';"
        )

        fail()

    with And(
        "I replace partition on the destination table from the source table's partition on which no mutations are "
        "happening"
    ):
        replace_partition(
            destination_table=destination_table, source_table=source_table, partition=2
        )

    with Check("I check that partition on the destination table was replaced"):
        check_partition_was_replaced(
            destination_table=destination_table, source_table=source_table, partition=2
        )

    with Check(
        "that the mutation is still running as the replace partition stopped it"
    ):
        with By(
            "confirming that the the i column, which mutation should've changed still has the old data"
        ):
            new_data = node.query(
                f"SELECT i FROM {destination_table} WHERE p == 1 ORDER BY tuple(*)"
            )

            assert old_data.output.strip() != new_data.output.strip(), error()


@TestFeature
@Requirements(RQ_SRS_032_ClickHouse_Alter_Table_ReplacePartition_Concurrent("1.0"))
@Name("concurrent merges and mutations")
def feature(self, node="clickhouse1"):
    """Check that replace partition does not wait for the ongoing merges and mutations that are not happening on the
    source table."""
    self.context.node = self.context.cluster.node(node)

    for scenario in loads(current_module(), Scenario):
        scenario()