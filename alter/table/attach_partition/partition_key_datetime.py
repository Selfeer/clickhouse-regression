from testflows.core import *
from testflows.combinatorics import product

from alter.table.attach_partition.common import *
from alter.table.attach_partition.requirements.requirements import *

from helpers.common import (
    getuid,
)
from helpers.tables import *


def valid_partition_key_pair(source_partition_key, destination_partition_key):
    """Validates if pair source partition key - destination partition key is valid
    for `attach partition from` statement."""

    not_subset = {
        "tuple()": [
            "time",
            "toYYYYMMDD(time)",
            "toYYYYMM(time)",
            "toYear(time)",
            "toDayOfYear(time)",
            "toQuarter(time)",
            "toMonth(time)",
            "toDayOfMonth(time)",
            "toDayOfWeek(time)",
            "toHour(time)",
            "toMinute(time)",
            "toSecond(time)",
        ],
    }

    not_monotonic = {
    #    "toMonth(time)": ["toQuarter(time)"]
    }

    partially_different = {
        "toYYYYMMDD(time)": ["toHour(time)", "toMinute(time)", "toSecond(time)"],
        "toYYYYMM(time)": [
            "toYYYYMMDD(time)",
            "toDayOfYear(time)",
            "toQuarter(time)",
            "toDayOfMonth(time)",
            "toDayOfWeek(time)",
            "toHour(time)",
            "toMinute(time)",
            "toSecond(time)",
        ],
        "toMonth(time)": [
            "toYYYYMM(time)",
            "toYYYYMMDD(time)",
            "toDayOfYear(time)",
            "toDayOfMonth(time)",
            "toDayOfWeek(time)",
            "toHour(time)",
            "toMinute(time)",
            "toSecond(time)",
            "toYear(time)",
        ],
        "toDayOfYear(time)": ["toYYYYMMDD(time)", "toYYYYMM(time)", "toHour(time)", "toMinute(time)", "toSecond(time)", "toYear(time)"],
        "toDayOfMonth(time)": [
            "toYYYYMMDD(time)",
            "toYYYYMM(time)",
            "toYear(time)",
            "toDayOfYear(time)",
            "toQuarter(time)",
            "toMonth(time)",
            "toDayOfWeek(time)",
            "toHour(time)",
            "toMinute(time)",
            "toSecond(time)",
        ],
        "toDayOfWeek(time)": [
            "toYYYYMMDD(time)",
            "toYYYYMM(time)",
            "toYear(time)",
            "toDayOfYear(time)",
            "toQuarter(time)",
            "toMonth(time)",
            "toDayOfMonth(time)",
            "toHour(time)",
            "toMinute(time)",
            "toSecond(time)",
        ],
        "toHour(time)": [
            "toYYYYMMDD(time)",
            "toYYYYMM(time)",
            "toYear(time)",
            "toDayOfYear(time)",
            "toQuarter(time)",
            "toMonth(time)",
            "toDayOfMonth(time)",
            "toDayOfWeek(time)",
            "toMinute(time)",
            "toSecond(time)",
        ],
        "toMinute(time)" : [
            "toYYYYMMDD(time)",
            "toYYYYMM(time)",
            "toYear(time)",
            "toDayOfYear(time)",
            "toQuarter(time)",
            "toMonth(time)",
            "toDayOfMonth(time)",
            "toDayOfWeek(time)",
            "toHour(time)",
            "toSecond(time)",
        ],
        "toSecond(time)" : [
            "toYYYYMMDD(time)",
            "toYYYYMM(time)",
            "toYear(time)",
            "toDayOfYear(time)",
            "toQuarter(time)",
            "toMonth(time)",
            "toDayOfMonth(time)",
            "toDayOfWeek(time)",
            "toHour(time)",
            "toMinute(time)",
        ],
        "toYear(time)" : [
            "toYYYYMMDD(time)",
            "toYYYYMM(time)",
            "toDayOfYear(time)",
            "toQuarter(time)",
            "toMonth(time)",
            "toDayOfMonth(time)",
            "toDayOfWeek(time)",
            "toHour(time)",
            "toMinute(time)",
            "toSecond(time)",
        ],
        "toQuarter(time)": [
            "toYYYYMMDD(time)",
            "toYYYYMM(time)",
            "toYear(time)",     
            "toDayOfYear(time)",
            "toMonth(time)",
            "toDayOfMonth(time)",
            "toDayOfWeek(time)",
            "toHour(time)",
            "toMinute(time)",
            "toSecond(time)",
        ]
    }

    if (
        destination_partition_key in not_monotonic.get(source_partition_key, "")
        and destination_partition_key not in not_subset.get(source_partition_key, "")
        and destination_partition_key
        not in partially_different.get(source_partition_key, "")
    ):
        return False, "not monotonic"

    if (
        destination_partition_key in not_subset.get(source_partition_key, "")
        and destination_partition_key not in not_monotonic.get(source_partition_key, "")
        and destination_partition_key
        not in partially_different.get(source_partition_key, "")
    ):
        return False, "not subset"

    if (
        destination_partition_key in partially_different.get(source_partition_key, "")
        and destination_partition_key not in not_monotonic.get(source_partition_key, "")
        and destination_partition_key not in not_subset.get(source_partition_key, "")
    ):
        return False, "partially different"

    return True, ""


def get_node(self, table):
    """Returns first node for non-replicated tables and returns random node for replicated tables."""
    if table == "source":
        if "Replicated" in self.context.source_engine:
            return random.choice(
                [self.context.node_1, self.context.node_2, self.context.node_3]
            )
        else:
            return self.context.node_1
    elif table == "destination":
        if "Replicated" in self.context.destination_engine:
            return random.choice(
                [self.context.node_1, self.context.node_2, self.context.node_3]
            )
        else:
            return self.context.node_1


def check(
    self,
    partition_ids,
    source_table_name,
    destination_table_name,
    exitcode=None,
    message=None,
    with_id=False,
):
    """Check `attach partition from` statement with or without `id`."""
    for partition_id in partition_ids:
        if with_id:
            query = f"ALTER TABLE {destination_table_name} ATTACH PARTITION ID '{partition_id}' FROM {source_table_name}"
        else:
            query = f"ALTER TABLE {destination_table_name} ATTACH PARTITION {partition_id} FROM {source_table_name}"

        self.context.node_1.query(
            query,
            exitcode=exitcode,
            message=message,
        )


@TestScenario
@Flags(TE)
def check_attach_partition_from(
    self,
    source_partition_key,
    destination_partition_key,
    source_table,
    destination_table,
    with_id=False,
):
    """Check `attach partition from` with different types of source and destination tables."""

    if check_clickhouse_version("<24.2")(self):
        if source_partition_key != destination_partition_key:
            skip("Different partition keys are not supported before 24.1")

    self.context.source_engine = source_table.__name__
    self.context.destination_engine = destination_table.__name__

    source_table_name = "source_" + getuid()
    destination_table_name = "destination_" + getuid()

    with Given(
        "I create two tables with specified engines and partition keys",
        description=f"""
            partition keys:
            source table partition key: {source_partition_key}
            destination table partition key: {destination_partition_key}
            engines:
            source table engine: {source_table.__name__}
            destination table engine: {destination_table.__name__}
            """,
    ):
        source_table(
            table_name=source_table_name,
            partition_by=source_partition_key,
            node=self.context.node_1,
        )
        destination_table(
            table_name=destination_table_name,
            partition_by=destination_partition_key,
            node=self.context.node_1,
        )

    if check_clickhouse_version(">=24.2")(self):
        with And("I add setting to allow alter partition with different key"):
            get_node(self, "source").query(
                f"ALTER TABLE {source_table_name} MODIFY SETTING allow_experimental_alter_partition_with_different_key=1"
            )
            get_node(self, "destination").query(
                f"ALTER TABLE {destination_table_name} MODIFY SETTING allow_experimental_alter_partition_with_different_key=1"
            )

    with And("I get the list of partitions and validate partition keys pair"):
        if with_id:
            partition_list_query = f"SELECT partition_id FROM system.parts WHERE table='{source_table_name}' ORDER BY partition_id"
        else:
            partition_list_query = f"SELECT partition FROM system.parts WHERE table='{source_table_name}' ORDER BY partition_id"

        partition_ids = sorted(
            list(
                set(get_node(self, "source").query(partition_list_query).output.split())
            )
        )
        valid, reason = valid_partition_key_pair(
            source_partition_key, destination_partition_key
        )
        get_node(self, "source").query(f"SELECT time from {source_table_name}")

    with And("I attach partition from source table to the destination table"):
        if valid:
            for partition_id in partition_ids:
                if with_id:
                    query = f"ALTER TABLE {destination_table_name} ATTACH PARTITION ID '{partition_id}' FROM {source_table_name}"
                else:
                    query = f"ALTER TABLE {destination_table_name} ATTACH PARTITION {partition_id} FROM {source_table_name}"

                self.context.node_1.query(query)
                self.context.node_1.query(
                    f"SELECT * FROM {destination_table_name} format PrettyCompactMonoBlock"
                )

        else:
            if reason == "not monotonic":
                exitcode, message = (
                    36,
                    "DB::Exception: Destination table partition expression is not monotonically increasing",
                )
                check(
                    self,
                    partition_ids=partition_ids,
                    source_table_name=source_table_name,
                    destination_table_name=destination_table_name,
                    exitcode=exitcode,
                    message=message,
                    with_id=with_id,
                )
            elif reason == "not subset":
                exitcode, message = (
                    36,
                    "DB::Exception: Destination table partition expression columns must be a subset of source table partition expression columns.",
                )
                check(
                    self,
                    partition_ids=partition_ids,
                    source_table_name=source_table_name,
                    destination_table_name=destination_table_name,
                    exitcode=exitcode,
                    message=message,
                    with_id=with_id,
                )
            elif reason == "partially different":
                exitcode, message = (
                    248,
                    "DB::Exception: Can not create the partition. A partition can not contain values that have different partition ids.",
                )
                for partition_id in partition_ids:
                    if with_id:
                        query = f"ALTER TABLE {destination_table_name} ATTACH PARTITION ID '{partition_id}' FROM {source_table_name}"
                    else:
                        query = f"ALTER TABLE {destination_table_name} ATTACH PARTITION {partition_id} FROM {source_table_name}"
                    try:
                        self.context.node_1.query(
                            query,
                            exitcode=exitcode,
                            message=message,
                        )
                    except:
                        note("Partition can be attached")

    with And(
        "I change engine names to compare replicated results with non-replicated results in snapshots"
    ):
        if "Replicated" in source_table.__name__:
            source_table = source_table.__name__.split("_")[-1]
            source_table = source_table.replace("Replicated", "")
        else:
            source_table = source_table.__name__.split("_")[-1]
        if "Replicated" in destination_table.__name__:
            destination_table = destination_table.__name__.split("_")[-1]
            destination_table = destination_table.replace("Replicated", "")
        else:
            destination_table = destination_table.__name__.split("_")[-1]

    with Then(
        f"I check that partitions were attached when source table partition_id - {source_partition_key}, destination table partition key - {destination_partition_key}, source table engine - {source_table}, destination table engine - {destination_table}:"
    ):
        if valid:
            source_partition_data = get_node(self, "source").query(
                f"SELECT * FROM {source_table_name} ORDER BY time,extra"
            )
            destination_partition_data = get_node(self, "destination").query(
                f"SELECT * FROM {destination_table_name} ORDER BY time,extra"
            )
            for attempt in retries(timeout=30, delay=2):
                with attempt:
                    assert (
                        destination_partition_data.output
                        == source_partition_data.output
                    ), error()

        elif reason == "partially different":
            execute_query(
                f"SELECT time,extra FROM {destination_table_name} ORDER BY time,extra",
                snapshot_name="/alter/table/attach_partition/partition_key_datetime/attach_partition_from/"
                + current().name.split("/")[-1],
                node=get_node(self, "destination"),
            )

    with And(f"I check that all replicas of destination table have same data:"):
        if "Replicated" in self.context.destination_engine:
            destination_partition_data_1 = self.context.node_1.query(
                f"SELECT * FROM {destination_table_name} ORDER BY time,extra"
            )
            destination_partition_data_2 = self.context.node_2.query(
                f"SELECT * FROM {destination_table_name} ORDER BY time,extra"
            )
            destination_partition_data_3 = self.context.node_3.query(
                f"SELECT * FROM {destination_table_name} ORDER BY time,extra"
            )
            for attempt in retries(timeout=30, delay=2):
                with attempt:
                    assert (
                        destination_partition_data_1.output
                        == destination_partition_data_2.output
                        == destination_partition_data_3.output
                    )

    # with And("I check that I can use data in te destination table after detach attach"):
    #     get_node(self, "source").query(
    #         f"DETACH TABLE {destination_table_name}"
    #     )
    #     get_node(self, "source").query(
    #         f"ATTACH TABLE {destination_table_name}"
    #     )
    #     get_node(self, "source").query(
    #         f"SELECT * FROM {destination_table_name} where a=1"
    #     )


@TestScenario
@Flags(TE)
def attach_partition_from(self, with_id=False):
    """Run test check with different partition keys for both source and destination tables to see if `attach partition from` is possible."""

    source_partition_keys = {
        # "tuple()",
        # "toYYYYMMDD(time)",
        # "toYYYYMM(time)",
        # "toYear(time)",
        # "toDayOfYear(time)",
        # "toQuarter(time)",
        "toMonth(time)",
        # "toDayOfMonth(time)",
        # "toDayOfWeek(time)",
        # "toHour(time)",
        # "toMinute(time)",
        # "toSecond(time)",
    }
    destination_partition_keys = {
        # "tuple()",
        # "toYYYYMMDD(time)",
        # "toYYYYMM(time)",
        # "toYear(time)",
        # "toDayOfYear(time)",
        "toQuarter(time)",
        # "toMonth(time)",
        # "toDayOfMonth(time)",
        # "toDayOfWeek(time)",
        # "toHour(time)",
        # "toMinute(time)",
        # "toSecond(time)",
    }

    source_table_types = {create_partitioned_table_with_datetime_data}

    destination_table_types = {create_empty_partitioned_table_with_datetime_data}

    if not self.context.stress:
        source_table_types = {create_partitioned_table_with_datetime_data}
        destination_table_types = {create_empty_partitioned_table_with_datetime_data}

    partition_keys_pairs = product(source_partition_keys, destination_partition_keys)
    table_pairs = product(source_table_types, destination_table_types)
    combinations = product(partition_keys_pairs, table_pairs)

    with Pool(4) as executor:
        for partition_keys, tables in combinations:
            source_partition_key, destination_partition_key = partition_keys
            source_table, destination_table = tables

            Scenario(
                f"combination: partition keys - {source_partition_key}, {destination_partition_key}; tables - {source_table.__name__}, {destination_table.__name__}",
                test=check_attach_partition_from,
                parallel=True,
                executor=executor,
            )(
                source_table=source_table,
                destination_table=destination_table,
                source_partition_key=source_partition_key,
                destination_partition_key=destination_partition_key,
                with_id=with_id,
            )
        join()


@TestFeature
@Requirements(
    RQ_SRS_034_ClickHouse_Alter_Table_AttachPartitionFrom_Conditions_Key_PartitionKey(
        "1.0"
    ),
    RQ_SRS_034_ClickHouse_Alter_Table_AttachPartition_SupportedTableEngines("1.0"),
    RQ_SRS_034_ClickHouse_Alter_Table_AttachPartitionFrom_Replicas("1.0"),
    RQ_SRS_034_ClickHouse_Alter_Table_AttachPartitionFrom("1.0"),
    RQ_SRS_034_ClickHouse_Alter_Table_AttachPartitionFrom_KeepData("1.0"),
)
@Name("partition key")
def feature(self):
    """Check conditions for partition key."""

    self.context.node_1 = self.context.cluster.node("clickhouse1")
    self.context.node_2 = self.context.cluster.node("clickhouse2")
    self.context.node_3 = self.context.cluster.node("clickhouse3")
    self.context.nodes = [
        self.context.cluster.node("clickhouse1"),
        self.context.cluster.node("clickhouse2"),
        self.context.cluster.node("clickhouse3"),
    ]

    # self.context.node_1.query("SET allow_experimental_alter_partition_with_different_key=1")

    with Pool(2) as pool:
        Scenario(
            "attach partition from without id",
            test=attach_partition_from,
            parallel=True,
            executor=pool,
        )(with_id=False)
        # Scenario(
        #     "attach partition from with id",
        #     test=attach_partition_from,
        #     parallel=True,
        #     executor=pool,
        # )(with_id=True)
        join()
