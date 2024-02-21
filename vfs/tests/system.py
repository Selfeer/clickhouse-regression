#!/usr/bin/env python3
import random

from testflows.core import *

from vfs.tests.steps import *
from vfs.requirements import *


@TestScenario
@Requirements(
    RQ_SRS_038_DiskObjectStorageVFS_System_AddKeeper("0.0"),
    RQ_SRS_038_DiskObjectStorageVFS_System_RemoveKeeper("0.0"),
)
def pause_keeper(self):
    nodes = self.context.ch_nodes
    insert_rows = 100000
    fault_probability = 0

    with pause_zookeeper(random.choice(self.context.zk_nodes)):
        with Given("a table is created"):
            _, table_name = replicated_table_cluster(
                storage_policy="external_vfs",
            )

    with pause_zookeeper(random.choice(self.context.zk_nodes)):
        with Given("data is inserted"):
            insert_random(
                node=random.choice(nodes),
                table_name=table_name,
                rows=insert_rows,
                settings=f"insert_keeper_fault_injection_probability={fault_probability}",
            )

    with pause_zookeeper(random.choice(self.context.zk_nodes)):
        with Then("I check that tables are consistent"):
            for node in nodes:
                assert_row_count(node=node, table_name=table_name, rows=insert_rows)


@TestScenario
@Requirements(RQ_SRS_038_DiskObjectStorageVFS_System_Delete("1.0"))
def delete(self):
    """
    Check that when a table is dropped, data in S3 is cleaned up.
    """
    bucket_name = self.context.bucket_name
    bucket_path = self.context.bucket_path
    table_name = "vfs_deleting_replicas"
    nodes = self.context.ch_nodes[:2]

    with Given("I get the size of the s3 bucket before adding data"):
        size_empty = get_stable_bucket_size(
            name=bucket_name,
            prefix=bucket_path,
            minio_enabled=self.context.minio_enabled,
            access_key=self.context.secret_access_key,
            key_id=self.context.access_key_id,
        )

    with And("I enable vfs"):
        enable_vfs()

    try:
        with Given("I have a replicated table"):
            for i, node in enumerate(nodes):
                node.query(
                    f"""
                    CREATE TABLE {table_name}  (
                        d UInt64
                    ) ENGINE = ReplicatedMergeTree('/clickhouse/tables/{table_name}', '{i + 1}')
                    ORDER BY d
                    SETTINGS storage_policy='external'
                    """
                )

        with And("I add data to the table on the first node"):
            insert_random(
                node=nodes[0], table_name=table_name, columns="d UInt64", rows=1000000
            )

        with And("I wait for the second node to sync"):
            nodes[1].query(f"SYSTEM SYNC REPLICA {table_name}", timeout=10)

        with And("I check the row count on the second node"):
            assert_row_count(node=nodes[1], table_name=table_name, rows=1000000)

        with When("I check how much data was added to the s3 bucket"):
            size_after_insert = get_bucket_size(
                name=bucket_name,
                prefix=bucket_path,
                minio_enabled=self.context.minio_enabled,
                access_key=self.context.secret_access_key,
                key_id=self.context.access_key_id,
            )
            assert size_after_insert > size_empty, error()

        with When("I drop the table on the second node"):
            nodes[1].query(f"DROP TABLE {table_name} SYNC")

        with Then("The size of the s3 bucket should be the same"):
            check_stable_bucket_size(
                name=bucket_name,
                prefix=bucket_path,
                expected_size=size_after_insert,
                tolerance=500,
                minio_enabled=self.context.minio_enabled,
            )

        with And("I check the row count on the first node"):
            assert_row_count(node=nodes[0], table_name=table_name, rows=1000000)

        with When("I drop the table on the first node"):
            nodes[0].query(f"DROP TABLE {table_name} SYNC")

        with Then(
            "The size of the s3 bucket should be very close to the size before adding any data"
        ):
            check_stable_bucket_size(
                name=bucket_name,
                prefix=bucket_path,
                expected_size=size_empty,
                tolerance=15,
                minio_enabled=self.context.minio_enabled,
            )

    finally:
        with Finally("I drop the table on each node"):
            for node in nodes:
                node.query(f"DROP TABLE IF EXISTS {table_name} SYNC")


@TestScenario
@Requirements(RQ_SRS_038_DiskObjectStorageVFS_System_CompactWideParts("1.0"))
def wide_parts(self):
    """Check that data can be stored in S3 using only wide data parts."""
    name = "table_" + getuid()
    part_types = None
    node = current().context.node
    value = "427"

    try:
        with Given(
            f"""I create table using S3 storage policy external_vfs,
                    min_bytes_for_wide_parts set to 0"""
        ):
            node.query(
                f"""
                CREATE TABLE {name} (
                    d UInt64
                ) ENGINE = MergeTree()
                ORDER BY d
                SETTINGS storage_policy='external_vfs',
                min_bytes_for_wide_part=0
            """
            )

        with When("I store simple data in the table"):
            node.query(f"INSERT INTO {name} VALUES ({value})")

        with And("I get the part types for the data added in this table"):
            part_types = node.query(
                f"SELECT part_type FROM system.parts WHERE table = '{name}'"
            ).output.splitlines()

        with Then("The part type should be Wide"):
            for _type in part_types:
                assert _type == "Wide", error()

    finally:
        with Finally("I drop the table"):
            node.query(f"DROP TABLE IF EXISTS {name} SYNC")


@TestScenario
@Requirements(RQ_SRS_038_DiskObjectStorageVFS_System_CompactWideParts("1.0"))
def compact_parts(self):
    """Check that data can be stored in S3 using only compact data parts."""
    name = "table_" + getuid()
    part_types = None
    node = current().context.node
    value = "427"

    try:
        with Given(
            f"""I create table using S3 storage policy external_vfs,
                    min_bytes_for_wide_parts set to a very large value"""
        ):
            node.query(
                f"""
                CREATE TABLE {name} (
                    d UInt64
                ) ENGINE = MergeTree()
                ORDER BY d
                SETTINGS storage_policy='external_vfs',
                min_bytes_for_wide_part=100000
            """
            )

        with When("I store simple data in the table, stored as compact parts"):
            node.query(f"INSERT INTO {name} VALUES ({value})")

        with And("I get the part types for the data added in this table"):
            part_types = node.query(
                f"SELECT part_type FROM system.parts WHERE table = '{name}'"
            ).output.splitlines()

        with Then("The part type should be Compact"):
            for _type in part_types:
                assert _type == "Compact", error()

    finally:
        with Finally("I drop the table"):
            node.query(f"DROP TABLE IF EXISTS {name} SYNC")


@TestStep
def get_active_part_count(self, node, table_name):
    """Get the number of active parts for a table."""
    r = node.query(f"SELECT sum(active) FROM system.parts where table='{table_name}'")
    return int(r.output)


@TestOutline(Scenario)
@Requirements(RQ_SRS_038_DiskObjectStorageVFS_System_Optimize("0.0"))
@Examples("table_settings", [[None], [WIDE_PART_SETTING], [COMPACT_PART_SETTING]])
def optimize(self, table_settings):
    """Check that OPTIMIZE works as expected on VFS."""

    table_name = "opt_table_" + getuid()
    nodes = self.context.ch_nodes
    n_inserts = 3000
    insert_size = 1000

    with Given("I have a vfs table"):
        replicated_table_cluster(
            table_name=table_name,
            storage_policy="external_vfs",
            settings=table_settings,
        )

    with And("I perform many inserts"):
        for _ in range(n_inserts):
            By(test=insert_random, parallel=True)(
                node=random.choice(nodes), table_name=table_name, rows=insert_size
            )
        join()

    with When("Check the number of active parts"):
        # SELECT count(), sum(active) FROM system.parts where table='opt_table'
        initial_part_count = get_active_part_count(node=nodes[0], table_name=table_name)

    with And("I perform OPTIMIZE"):
        nodes[0].query(f"OPTIMIZE TABLE {table_name}")

    with Then("There should be fewer active parts"):
        optimized_part_count = get_active_part_count(
            node=nodes[0], table_name=table_name
        )
        assert optimized_part_count < initial_part_count, error()

    with When("I perform OPTIMIZE FINAL"):
        nodes[0].query(f"OPTIMIZE TABLE {table_name} FINAL")

    with Then("There should be fewer active parts"):
        for attempt in retries(timeout=15, delay=1):
            with attempt:
                final_part_count = get_active_part_count(
                    node=nodes[0], table_name=table_name
                )
                assert final_part_count < optimized_part_count, error()

    with Then("there should be only one active part"):
        assert final_part_count == 1, error()

    with And("there should still be the same amount og data"):
        assert_row_count(
            node=nodes[0], table_name=table_name, rows=n_inserts * insert_size
        )


@TestScenario
@Requirements(
    RQ_SRS_038_DiskObjectStorageVFS_System_ConnectionInterruption_FaultInjection("0.0")
)
def fault_injection(self):
    """Test that ClickHouse is robust against injected faults."""
    nodes = self.context.ch_nodes
    table_name = "fault_injection"
    rows_per_insert = 5000
    insert_rounds = 5
    fault_probability = 0.3

    with Given("I have a replicated vfs table"):
        replicated_table_cluster(
            table_name=table_name,
            storage_policy="external_vfs",
            columns="d UInt64",
        )

    with When(
        f"I perform inserts with insert_keeper_fault_injection_probability={fault_probability}"
    ):
        for _ in range(insert_rounds):
            for node in nodes:
                with By(f"Inserting {rows_per_insert} rows on {node.name}"):
                    insert_random(
                        node=node,
                        table_name=table_name,
                        columns="d UInt64",
                        rows=rows_per_insert,
                        no_checks=True,
                        settings=f"insert_keeper_fault_injection_probability={fault_probability}",
                    )

    with Then("I check the number of rows in the table"):
        retry(assert_row_count, timeout=5, delay=1)(
            node=nodes[0],
            table_name=table_name,
            rows=(rows_per_insert * insert_rounds * len(nodes)),
        )


@TestFeature
@Name("system")
def feature(self):
    """Test cluster functionality."""

    with Given("I have S3 disks configured"):
        s3_config()

    for scenario in loads(current_module(), Scenario):
        scenario()
