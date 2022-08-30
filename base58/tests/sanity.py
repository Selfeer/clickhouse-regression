from base58.tests.steps import *


@TestScenario
def sanity(self, node=None):
    """Check that clickhouse support using base58."""

    if node is None:
        node = self.context.node

    table_name_random = f"table_{getuid()}_random"
    table_name = f"table_{getuid()}"
    table_name_e64 = f"table_{getuid()}_e64"
    table_name_e58 = f"table_{getuid()}_e58"

    # with Given("I change max_partitions_per_insert_block clickhouse variable"):
    #     node.query("set max_partitions_per_insert_block=10000")

    with When("I create a table with random engine"):
        create_partitioned_table(
            table_name=table_name_random,
            engine="GenerateRandom(1, 5, 3)",
            order="",
            partition="",
        )

    with When("I create a table with MergeTree engine"):
        create_partitioned_table(table_name=table_name, partition="")

    with When("I insert data into the MergeTree table"):
        node.query(
            f"insert into {table_name} select id, x from {table_name_random} limit 100000000"
        )

    with When("I create a table with MergeTree engine"):
        create_partitioned_table(table_name=table_name_e64, partition="")

    with When("I insert data into the table with base64 encoding"):
        node.query(
            f"insert into {table_name_e64} select id, base64Encode(x) from {table_name};"
        )

    with When("I create a table with MergeTree engine"):
        create_partitioned_table(table_name=table_name_e58, partition="")

    with When("I insert data into the table with base58 encoding"):
        node.query(
            f"insert into {table_name_e58} select id, base58Encode(x) from {table_name};"
        )

    with Then("I compare base58 select performance and base64 select performance"):
        execution_times = []
        start_time = time.time()
        node.query(f"select count(*) from (select base64Encode(x) from {table_name})")
        execution_times.append(time.time() - start_time)
        start_time = time.time()
        node.query(f"select count(*) from (select base58Encode(x) from {table_name})")
        execution_times.append(time.time() - start_time)
        start_time = time.time()
        node.query(
            f"select count(*) from (select base64Decode(x) from {table_name_e64})"
        )
        execution_times.append(time.time() - start_time)
        start_time = time.time()
        node.query(
            f"select count(*) from (select base58Decode(x) from {table_name_e58})"
        )
        execution_times.append(time.time() - start_time)
        note(execution_times)
        assert 2 * min(execution_times) > max(execution_times), error()


@TestFeature
# @Requirements(RQ_SRS_023_ClickHouse_LightweightDelete_S3Disks("1.0"))
@Name("sanity")  # todo performance
def feature(self, node="clickhouse1"):
    """Check that clickhouse support using base58"""
    self.context.node = self.context.cluster.node(node)
    self.context.table_engine = "MergeTree"
    for scenario in loads(current_module(), Scenario):
        scenario()
