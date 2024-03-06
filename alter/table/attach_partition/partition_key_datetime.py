from testflows.core import *
from testflows.combinatorics import product, CoveringArray

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

    partially_monotonic = {
        "toMonth(time)": ["toQuarter(time)"],
        "toDayOfYear(time)": [
            "toMonth(time)",
            "toDayOfWeek(time)",
            "toDayOfMonth(time)",
            "toQuarter(time)",
        ],
    }

    partially_different = {
        "toYYYYMMDD(time)": ["toHour(time)", "toMinute(time)", "toSecond(time)"],
        "toYYYYMM(time)": [
            "toYYYYMMDD(time)",
            "toDayOfYear(time)",
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
        "toDayOfYear(time)": [
            "toYYYYMMDD(time)",
            "toYYYYMM(time)",
            "toHour(time)",
            "toMinute(time)",
            "toSecond(time)",
            "toYear(time)",
        ],
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
        "toMinute(time)": [
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
        "toSecond(time)": [
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
        "toYear(time)": [
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
        ],
    }

    if (
        destination_partition_key in not_subset.get(source_partition_key, "")
        and destination_partition_key
        not in partially_different.get(source_partition_key, "")
        and destination_partition_key
        not in partially_monotonic.get(source_partition_key, "")
    ):
        return False, "not subset"

    if (
        destination_partition_key in partially_different.get(source_partition_key, "")
        and destination_partition_key not in not_subset.get(source_partition_key, "")
        and destination_partition_key
        not in partially_monotonic.get(source_partition_key, "")
    ):
        return False, "partially different"

    if (
        destination_partition_key in partially_different.get(source_partition_key, "")
        and destination_partition_key not in not_subset.get(source_partition_key, "")
        and destination_partition_key
        not in partially_monotonic.get(source_partition_key, "")
    ):
        return False, "partially different"

    if destination_partition_key in partially_monotonic.get(source_partition_key, ""):
        return False, "partially monotonic"

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
):
    """Check `attach partition from` statement."""
    for partition_id in partition_ids:
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
):
    """Check `attach partition from` with different types of source and destination tables."""

    if (
        check_clickhouse_version("<24.3")(self)
        and source_partition_key != destination_partition_key
    ):
        skip(
            "`attach partition from` with tables that have different partition keys are not supported before 24.3"
        )

    self.context.source_engine = source_table.__name__.split("_")[-1]
    self.context.destination_engine = destination_table.__name__.split("_")[-1]

    source_table_name = "source_" + getuid()
    destination_table_name = "destination_" + getuid()

    with Given(
        "I create two tables with specified engines and partition keys",
        description=f"""
            partition keys:
            source table partition key: {source_partition_key}
            destination table partition key: {destination_partition_key}
            engines:
            source table engine: {self.context.source_engine}
            destination table engine: {self.context.destination_engine}
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

    if check_clickhouse_version(">=24.3")(self):
        with And(
            "I add setting to allow alter partition with different partition keys"
        ):
            if "Replicated" in self.context.destination_engine:
                for node in self.context.nodes:
                    node.query(
                        f"ALTER TABLE {destination_table_name} MODIFY SETTING allow_experimental_alter_partition_with_different_key=1"
                    )
            else:
                get_node(self, "destination").query(
                    f"ALTER TABLE {destination_table_name} MODIFY SETTING allow_experimental_alter_partition_with_different_key=1"
                )

    with And("I get the list of partitions"):
        partition_list_query = f"SELECT partition FROM system.parts WHERE table='{source_table_name}' ORDER BY partition"
        partition_ids = sorted(
            list(
                set(get_node(self, "source").query(partition_list_query).output.split())
            )
        )

    with And("I validate partition keys pair"):
        valid, reason = valid_partition_key_pair(
            source_partition_key, destination_partition_key
        )

    with And("I attach partition from source table to the destination table"):
        if valid:
            for partition_id in partition_ids:
                query = f"ALTER TABLE {destination_table_name} ATTACH PARTITION {partition_id} FROM {source_table_name}"
                self.context.node_1.query(query)
                self.context.node_1.query(
                    f"SELECT * FROM {destination_table_name} format PrettyCompactMonoBlock"
                )
        else:
            if reason == "not subset":
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
                )

            elif reason == "partially different":
                exitcode, message = (
                    248,
                    "DB::Exception: Can not create the partition. A partition can not contain values that have different partition ids.",
                )
                for partition_id in partition_ids:
                    query = f"ALTER TABLE {destination_table_name} ATTACH PARTITION {partition_id} FROM {source_table_name}"
                    try:
                        self.context.node_1.query(
                            query,
                            exitcode=exitcode,
                            message=message,
                        )
                    except:
                        note("Partition can be attached")

            elif reason == "partially monotonic":
                exitcode, message = (
                    36,
                    "DB::Exception: Destination table partition expression is not monotonically increasing",
                )
                for partition_id in partition_ids:
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
        if "Replicated" in self.context.source_engine:
            source_engine = self.context.source_engine.replace("Replicated", "")
        else:
            source_engine = self.context.source_engine

        if "Replicated" in self.context.destination_engine:
            destination_engine = self.context.destination_engine.replace(
                "Replicated", ""
            )
        else:
            destination_engine = self.context.destination_engine

    with Then(
        f"""
        I check that partitions were attached when 
        source table partition_id - {source_partition_key}, 
        destination table partition key - {destination_partition_key}, 
        source table engine - {source_engine}, 
        destination table engine - {destination_engine}:
        """
    ):
        if valid:
            source_partition_data = get_node(self, "source").query(
                f"SELECT * FROM {source_table_name} ORDER BY time,date,extra"
            )
            destination_partition_data = get_node(self, "destination").query(
                f"SELECT * FROM {destination_table_name} ORDER BY time,date,extra"
            )
            for attempt in retries(timeout=30, delay=2):
                with attempt:
                    assert (
                        destination_partition_data.output.strip()
                        == source_partition_data.output.strip()
                    ), error()

        elif reason == "partially different":
            execute_query(
                f"SELECT time,extra FROM {destination_table_name} ORDER BY time,date,extra",
                snapshot_name="/alter/table/attach_partition/partition_key_datetime/attach_partition_from/"
                + current().name.split("/")[-1],
                node=get_node(self, "destination"),
            )

            source_partition_data = get_node(self, "source").query(
                f"SELECT * FROM {source_table_name} ORDER BY time,date,extra"
            )
            destination_partition_data = get_node(self, "destination").query(
                f"SELECT * FROM {destination_table_name} ORDER BY time,date,extra"
            )
            for attempt in retries(timeout=30, delay=2):
                with attempt:
                    assert (
                        destination_partition_data.output
                        != source_partition_data.output
                    ), "not partially different"

        elif reason == "partially monotonic":
            execute_query(
                f"SELECT time,extra FROM {destination_table_name} ORDER BY time,date,extra",
                snapshot_name="/alter/table/attach_partition/partition_key_datetime/attach_partition_from/"
                + current().name.split("/")[-1],
                node=get_node(self, "destination"),
            )
            source_partition_data = get_node(self, "source").query(
                f"SELECT * FROM {source_table_name} ORDER BY time,date,extra"
            )
            destination_partition_data = get_node(self, "destination").query(
                f"SELECT * FROM {destination_table_name} ORDER BY time,date,extra"
            )
            for attempt in retries(timeout=30, delay=2):
                with attempt:
                    assert (
                        destination_partition_data.output
                        != source_partition_data.output
                    ), "not partially monotonic"

    with And(f"I check that all replicas of destination table have same data:"):
        if "Replicated" in self.context.destination_engine:
            destination_partition_data_1 = self.context.node_1.query(
                f"SELECT * FROM {destination_table_name} ORDER BY time,date,extra"
            )
            destination_partition_data_2 = self.context.node_2.query(
                f"SELECT * FROM {destination_table_name} ORDER BY time,date,extra"
            )
            destination_partition_data_3 = self.context.node_3.query(
                f"SELECT * FROM {destination_table_name} ORDER BY time,date,extra"
            )
            for attempt in retries(timeout=30, delay=2):
                with attempt:
                    assert (
                        destination_partition_data_1.output
                        == destination_partition_data_2.output
                        == destination_partition_data_3.output
                    ), error()

    with And(
        "I check that I can use data in the destination table after detach attach"
    ):
        data_before = self.context.node_1.query(
            f"SELECT * FROM {destination_table_name} WHERE time > '2000-05-10' ORDER BY time,date,extra"
        ).output
        self.context.node_1.query(f"DETACH TABLE {destination_table_name}")
        self.context.node_1.query(f"ATTACH TABLE {destination_table_name}")
        data_after = self.context.node_1.query(
            f"SELECT * FROM {destination_table_name} WHERE time > '2000-05-10' ORDER BY time,date,extra"
        )
        for attempt in retries(timeout=30, delay=2):
            with attempt:
                assert data_after.output == data_before, error()


@TestScenario
@Flags(TE)
def attach_partition_from(self):
    """
    Run test check with different partition keys for both source and destination
    tables to see if `attach partition from` is possible.
    """

    source_partition_keys = {
        "tuple()",
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
    }

    destination_partition_keys = {
        "tuple()",
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
    }

    source_table_types = {
        partitioned_datetime_MergeTree,
        partitioned_datetime_ReplicatedMergeTree,
        partitioned_datetime_ReplacingMergeTree,
        partitioned_datetime_ReplicatedReplacingMergeTree,
        partitioned_datetime_AggregatingMergeTree,
        partitioned_datetime_ReplicatedAggregatingMergeTree,
        partitioned_datetime_SummingMergeTree,
        partitioned_datetime_ReplicatedSummingMergeTree,
        partitioned_datetime_CollapsingMergeTree,
        partitioned_datetime_ReplicatedCollapsingMergeTree,
        partitioned_datetime_VersionedCollapsingMergeTree,
        partitioned_datetime_ReplicatedVersionedCollapsingMergeTree,
        partitioned_datetime_GraphiteMergeTree,
        partitioned_datetime_ReplicatedGraphiteMergeTree,
    }

    destination_table_types = {
        empty_partitioned_datetime_MergeTree,
        empty_partitioned_datetime_ReplicatedMergeTree,
        empty_partitioned_datetime_ReplacingMergeTree,
        empty_partitioned_datetime_ReplicatedReplacingMergeTree,
        empty_partitioned_datetime_AggregatingMergeTree,
        empty_partitioned_datetime_ReplicatedAggregatingMergeTree,
        empty_partitioned_datetime_SummingMergeTree,
        empty_partitioned_datetime_ReplicatedSummingMergeTree,
        empty_partitioned_datetime_CollapsingMergeTree,
        empty_partitioned_datetime_ReplicatedCollapsingMergeTree,
        empty_partitioned_datetime_VersionedCollapsingMergeTree,
        empty_partitioned_datetime_ReplicatedVersionedCollapsingMergeTree,
        empty_partitioned_datetime_GraphiteMergeTree,
        empty_partitioned_datetime_ReplicatedGraphiteMergeTree,
    }

    if not self.context.stress:
        source_table_types = {
            partitioned_datetime_MergeTree,
            partitioned_datetime_ReplicatedMergeTree,
        }
        destination_table_types = {
            empty_partitioned_datetime_MergeTree,
            empty_partitioned_datetime_ReplicatedMergeTree,
        }
        partition_keys_pairs = product(
            source_partition_keys, destination_partition_keys
        )
        table_pairs = product(source_table_types, destination_table_types)
        combinations = product(partition_keys_pairs, table_pairs)
    else:
        combinations_dict = {
            "source_table": source_table_types,
            "destination_table": destination_table_types,
            "source_key": source_partition_keys,
            "destination_key": destination_partition_keys,
        }
        covering_array = CoveringArray(combinations_dict, strength=3)
        combinations = [
            (
                (item["source_key"], item["destination_key"]),
                (item["source_table"], item["destination_table"]),
            )
            for item in covering_array
        ]

    with Pool(4) as executor:
        for partition_keys, tables in combinations:
            source_partition_key, destination_partition_key = partition_keys
            source_table, destination_table = tables

            Scenario(
                f"combination partition keys {source_partition_key} {destination_partition_key} tables {source_table.__name__} {destination_table.__name__}",
                test=check_attach_partition_from,
                parallel=True,
                executor=executor,
            )(
                source_table=source_table,
                destination_table=destination_table,
                source_partition_key=source_partition_key,
                destination_partition_key=destination_partition_key,
            )
        join()


@TestFeature
@Requirements(
    RQ_SRS_034_ClickHouse_Alter_Table_AttachPartitionFrom("1.0"),
    RQ_SRS_034_ClickHouse_Alter_Table_AttachPartitionFrom_Conditions_Key_PartitionKey(
        "1.0"
    ),
    RQ_SRS_034_ClickHouse_Alter_Table_AttachPartitionFrom_Replicas("1.0"),
)
@Name("partition key datetime")
def feature(self):
    """Check conditions for partition key when using `attach partition from` statement
    with different partition keys and datetime data."""

    self.context.node_1 = self.context.cluster.node("clickhouse1")
    self.context.node_2 = self.context.cluster.node("clickhouse2")
    self.context.node_3 = self.context.cluster.node("clickhouse3")
    self.context.nodes = [
        self.context.node_1,
        self.context.node_2,
        self.context.node_3,
    ]

    Scenario(run=attach_partition_from)
