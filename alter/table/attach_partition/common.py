import platform

from testflows.asserts import values, error, snapshot
from testflows.core import *

from helpers.tables import *


def current_cpu():
    """Return current cpu architecture."""
    arch = platform.processor()
    if arch not in ("x86_64", "aarch64"):
        raise TypeError(f"unsupported CPU architecture {arch}")
    return arch


@TestStep(Given)
def create_partitioned_table_with_data(
    self,
    table_name,
    engine="MergeTree",
    partition_by="tuple()",
    primary_key=None,
    columns=None,
    query_settings=None,
    order_by="tuple()",
    node=None,
    number_of_partitions=3,
    config="graphite_rollup_example",
    sign="sign",
    version="a",
    bias=0,
):
    """Create a table that is partitioned by specified columns."""

    if node is None:
        node = self.context.node

    if columns is None:
        columns = [
            Column(name="a", datatype=UInt16()),
            Column(name="b", datatype=UInt16()),
            Column(name="c", datatype=UInt16()),
            Column(name="extra", datatype=UInt64()),
            Column(name="Path", datatype=String()),
            Column(name="Time", datatype=DateTime()),
            Column(name="Value", datatype=Float64()),
            Column(name="Timestamp", datatype=Int64()),
            Column(name="sign", datatype=Int8()),
        ]

    if engine == "GraphiteMergeTree":
        engine = f"GraphiteMergeTree('{config}')"
    elif engine == "VersionedCollapsingMergeTree":
        engine = f"VersionedCollapsingMergeTree({sign},{version})"
    elif engine == "CollapsingMergeTree":
        engine = f"CollapsingMergeTree({sign})"

    with By(f"creating a table that is partitioned by '{partition_by}'"):
        create_table(
            name=table_name,
            engine=engine,
            partition_by=partition_by,
            primary_key=primary_key,
            order_by=order_by,
            columns=columns,
            query_settings=query_settings,
            if_not_exists=True,
            node=node,
        )

    with And(f"inserting data that will create multiple partitions"):
        for i in range(1, number_of_partitions + 1):
            node.query(
                f"INSERT INTO {table_name} (a, b, c, extra, sign) SELECT {i+bias}, {i+4+bias}, {i+8+bias}, number+1000, 1 FROM numbers({4})"
            )


@TestStep(Given)
def create_partitioned_replicated_table_with_data(
    self,
    table_name: str,
    columns: list[dict] = None,
    if_not_exists: bool = False,
    db: str = None,
    comment: str = None,
    primary_key=None,
    order_by: str = "tuple()",
    partition_by: str = None,
    engine="ReplicatedMergeTree",
    query_settings=None,
    nodes=None,
    number_of_partitions=3,
    config="graphite_rollup_example",
    sign="sign",
    version="a",
    bias=0,
):
    """Create a table with the specified engine."""
    if columns is None:
        columns = [
            Column(name="a", datatype=UInt16()),
            Column(name="b", datatype=UInt16()),
            Column(name="c", datatype=UInt16()),
            Column(name="extra", datatype=UInt64()),
            Column(name="Path", datatype=String()),
            Column(name="Time", datatype=DateTime()),
            Column(name="Value", datatype=Float64()),
            Column(name="Timestamp", datatype=Int64()),
            Column(name="sign", datatype=Int8()),
        ]

    if "GraphiteMergeTree" in engine:
        engine = f"GraphiteMergeTree('{config}')"
    elif "VersionedCollapsingMergeTree" in engine:
        engine = f"VersionedCollapsingMergeTree({sign},{version})"
    elif "CollapsingMergeTree" in engine:
        engine = f"CollapsingMergeTree({sign})"

    with By(f"creating a table that is partitioned by '{partition_by}'"):
        for node in nodes:
            create_table(
                name=table_name,
                columns=columns,
                engine=f"{engine}('/clickhouse/tables/"
                + "{shard}"
                + f"/{table_name}', "
                + "'{replica}')",
                order_by=order_by,
                primary_key=primary_key,
                comment=comment,
                partition_by=partition_by,
                cluster="replicated_cluster_secure",
                node=node,
                if_not_exists=True,
            )

    node = random.choice(nodes)
    with And(f"inserting data that will create multiple partitions"):
        for i in range(1, number_of_partitions + 1):
            node.query(
                f"INSERT INTO {table_name} (a, b, c, extra, sign) SELECT {i+bias}, {i+4+bias}, {i+8+bias}, number+1000, 1 FROM numbers({4})"
            )


@TestStep(Given)
def create_empty_partitioned_replicated_table(
    self,
    table_name: str,
    columns: list[dict] = None,
    if_not_exists: bool = False,
    db: str = None,
    comment: str = None,
    primary_key=None,
    order_by: str = "tuple()",
    partition_by: str = None,
    engine="ReplicatedMergeTree",
    query_settings=None,
    nodes=None,
    number_of_partitions=2,
    config="graphite_rollup_example",
    sign="sign",
    version="a",
    bias=0,
):
    """Create a table with the specified engine."""
    if columns is None:
        columns = [
            Column(name="a", datatype=UInt16()),
            Column(name="b", datatype=UInt16()),
            Column(name="c", datatype=UInt16()),
            Column(name="extra", datatype=UInt64()),
            Column(name="Path", datatype=String()),
            Column(name="Time", datatype=DateTime()),
            Column(name="Value", datatype=Float64()),
            Column(name="Timestamp", datatype=Int64()),
            Column(name="sign", datatype=Int8()),
        ]

    if engine == "GraphiteMergeTree":
        engine = f"GraphiteMergeTree('{config}')"
    elif engine == "VersionedCollapsingMergeTree":
        engine = f"VersionedCollapsingMergeTree({sign},{version})"
    elif engine == "CollapsingMergeTree":
        engine = f"CollapsingMergeTree({sign})"

    with By(f"creating a table that is partitioned by '{partition_by}'"):
        for node in nodes:
            create_table(
                name=table_name,
                columns=columns,
                engine=f"{engine}('/clickhouse/tables/"
                + "{shard}"
                + f"/{table_name}', "
                + "'{replica}')",
                order_by=order_by,
                primary_key=primary_key,
                comment=comment,
                partition_by=partition_by,
                cluster="replicated_cluster_secure",
                node=node,
                if_not_exists=True,
            )


@TestStep(Given)
def create_empty_partitioned_table(
    self,
    table_name,
    engine="MergeTree",
    partition_by="tuple()",
    primary_key=None,
    columns=None,
    query_settings=None,
    order_by="tuple()",
    node=None,
    config="graphite_rollup_example",
    sign="sign",
    version="a",
):
    """Create a table that is partitioned by specified columns."""

    if node is None:
        node = self.context.node

    if columns is None:
        columns = [
            Column(name="a", datatype=UInt16()),
            Column(name="b", datatype=UInt16()),
            Column(name="c", datatype=UInt16()),
            Column(name="extra", datatype=UInt64()),
            Column(name="Path", datatype=String()),
            Column(name="Time", datatype=DateTime()),
            Column(name="Value", datatype=Float64()),
            Column(name="Timestamp", datatype=Int64()),
            Column(name="sign", datatype=Int8()),
        ]

    if engine == "GraphiteMergeTree":
        engine = f"GraphiteMergeTree('{config}')"
    elif engine == "VersionedCollapsingMergeTree":
        engine = f"VersionedCollapsingMergeTree({sign},{version})"
    elif engine == "CollapsingMergeTree":
        engine = f"CollapsingMergeTree({sign})"

    with By(f"creating a table that is partitioned by '{partition_by}'"):
        create_table(
            name=table_name,
            engine=engine,
            partition_by=partition_by,
            primary_key=primary_key,
            order_by=order_by,
            columns=columns,
            query_settings=query_settings,
            if_not_exists=True,
            node=node,
        )


@TestStep(Then)
def check_partition_was_attached(
    self,
    table,
    node=None,
    sort_column="p",
    partition=1,
    column="i",
    list=False,
):
    """Check that the partition was attached on the table."""
    if node is None:
        node = self.context.node

    with By("I check that there is no partition in detached folder"):
        partition_values = node.query(
            f"SELECT partition_id FROM system.detached_parts WHERE table = '{table}' and partition_id = '{partition}' ORDER BY tuple(*)"
        ).output

        assert len(partition_values) == 0

    with And("I check that data from the partition is on the table"):
        data = node.query(
            f"SELECT partition FROM system.parts WHERE partition = '{partition}' and table = '{table}'"
        ).output

        assert len(data) > 0


@TestStep(Then)
def check_partition_was_attached_from(
    self,
    source_table,
    destination_table,
    node=None,
    partition=1,
):
    """Check that the partition was attached on the table."""
    if node is None:
        node = self.context.node

    with By(
        "I check that data in attached partition is the same in both the source and destination tables"
    ):
        source_data = node.query(
            f"SELECT * FROM {source_table} WHERE p = {partition} ORDER BY p"
        ).output
        destination_data = node.query(
            f"SELECT * FROM {destination_table} WHERE p = {partition} ORDER BY p"
        ).output

        assert source_data == destination_data


@TestStep(Then)
def check_partition_was_detached(
    self,
    table,
    node=None,
    sort_column="p",
    partition=1,
    column="i",
    list=False,
):
    """Check that the partition was detached from the table."""
    if node is None:
        node = self.context.node

    with By("selecting data from the table"):
        partition_values = node.query(
            f"SELECT partition_id FROM system.detached_parts WHERE table = '{table}' and partition_id = '{partition}' ORDER BY tuple(*)"
        ).output

        assert len(partition_values) > 0


@TestStep(Given)
def insert_data(
    self,
    table_name,
    number_of_values=3,
    number_of_partitions=5,
    number_of_parts=1,
    node=None,
    bias=0,
):
    """Insert random UInt64 values into a column and create multiple partitions based on the value of number_of_partitions."""
    if node is None:
        node = self.context.node

    with By("Inserting random values into a column with uint64 datatype"):
        for i in range(1, number_of_partitions + 1):
            for _ in range(1, number_of_parts + 1):
                node.query(
                    f"INSERT INTO {table_name} (a, b, i) SELECT {i%4+bias}, {i}, rand64() FROM numbers({number_of_values})"
                )


@TestStep(Given)
def insert_date_data(
    self,
    table_name,
    number_of_partitions=5,
    node=None,
    bias=0,
):
    """Insert Date data into table."""
    if node is None:
        node = self.context.node

    with By("Inserting values into a column with Date datatype"):
        for i in range(1, number_of_partitions + 1):
            node.query(
                f"INSERT INTO {table_name} (timestamp) VALUES (toDate('2023-12-20')+{i}+{bias})"
            )


@TestStep(Given)
def create_partitions_with_random_uint64(
    self,
    table_name,
    number_of_values=3,
    number_of_partitions=5,
    number_of_parts=1,
    node=None,
    bias=0,
):
    """Insert random UInt64 values into a column and create multiple partitions based on the value of number_of_partitions."""
    if node is None:
        node = self.context.node

    with By("Inserting random values into a column with uint64 datatype"):
        for i in range(1, number_of_partitions + 1):
            for _ in range(1, number_of_parts + 1):
                node.query(
                    f"INSERT INTO {table_name} (p, i) SELECT {i+bias}, rand64() FROM numbers({number_of_values})"
                )


def execute_query(
    sql,
    expected=None,
    exitcode=None,
    message=None,
    no_checks=False,
    snapshot_name=None,
    format="TabSeparatedWithNames",
    node=None,
):
    """Execute SQL query and compare the output to the snapshot."""
    if snapshot_name is None:
        snapshot_name = "/alter/table/attach_partition" + current().name

    if node is None:
        node = current().context.node

    with When("I execute query", description=sql):
        r = node.query(
            sql + " FORMAT " + format,
            exitcode=exitcode,
            message=message,
            no_checks=no_checks,
        )
        if no_checks:
            return r

    if message is None:
        if expected is not None:
            with Then("I check output against expected"):
                assert r.output.strip() == expected, error()
        else:
            with Then("I check output against snapshot"):
                with values() as that:
                    for attempt in retries(timeout=30, delay=5):
                        with attempt:
                            assert that(
                                snapshot(
                                    "\n" + r.output.strip() + "\n",
                                    "tests." + current_cpu(),
                                    name=snapshot_name,
                                    encoder=str,
                                    mode=snapshot.CHECK,
                                )
                            ), error()
