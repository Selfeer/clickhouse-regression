#!/usr/bin/env python3
import time, datetime

from testflows.core import *
from testflows.combinatorics import permutations

from object_storage_vfs.tests.steps import *
from object_storage_vfs.requirements import *


@TestScenario
@Requirements(RQ_SRS_038_DiskObjectStorageVFS_Integrity_Delete("1.0"))
def delete(self):
    """
    Check that when a table is dropped, data in S3 is cleaned up.
    """
    bucket_name = self.context.bucket_name
    bucket_path = self.context.bucket_path
    table_name = "vfs_deleting_replicas"
    nodes = self.context.ch_nodes[:2]

    with Given("I get the size of the s3 bucket before adding data"):
        size_empty = get_bucket_size(
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
            retry(check_bucket_size, timeout=60, delay=1)(
                name=bucket_name,
                prefix=bucket_path,
                expected_size=size_after_insert,
                tolerance=0,
                minio_enabled=self.context.minio_enabled,
            )

        with And("I check the row count on the first node"):
            assert_row_count(node=nodes[0], table_name=table_name, rows=1000000)

        with When("I drop the table on the first node"):
            nodes[0].query(f"DROP TABLE {table_name} SYNC")

        with Then(
            "The size of the s3 bucket should be very close to the size before adding any data"
        ):
            retry(check_bucket_size, timeout=180, delay=1)(
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
@Requirements(RQ_SRS_038_DiskObjectStorageVFS_Integrity_VFSToggled("1.0"))
def disable_vfs_with_vfs_table(self):
    """
    Check that removing global allow_vfs=1 when a vfs table exists does not cause data to become inaccessible.
    """
    nodes = current().context.ch_nodes
    table_name = "my_replicated_vfs_table"

    with Check("create a table with VFS enabled"):
        with Given("I enable allow_vfs"):
            enable_vfs()

        with Given("I have a table with vfs"):
            replicated_table_cluster(
                table_name=table_name,
                storage_policy="external",
                columns="d UInt64",
            )

        with And("I insert some data"):
            nodes[1].query(
                f"INSERT INTO {table_name} VALUES {','.join(f'({x})' for x in range(100))}"
            )

        with Then("the data is accesssible"):
            assert_row_count(node=nodes[1], table_name=table_name, rows=100)
            retry(assert_row_count, timeout=10, delay=1)(
                node=nodes[0], table_name=table_name, rows=100
            )

    with Check("access the table without VFS"):
        with When("VFS is no longer enabled"):
            check_vfs_state(node=nodes[0], enabled=False)

        with Then("the data remains accessible"):
            assert_row_count(node=nodes[0], table_name=table_name, rows=100)

        with When("I delete some data"):
            nodes[2].query(f"DELETE FROM {table_name} WHERE d=40")

        with Then("Not all data is deleted"):
            retry(assert_row_count, timeout=5, delay=1)(
                node=nodes[1], table_name=table_name, rows=99
            )


@TestScenario
@Requirements(RQ_SRS_038_DiskObjectStorageVFS_Integrity_VFSToggled("1.0"))
def enable_vfs_with_non_vfs_table(self):
    """
    Check that globally enabling allow_vfs when a non-vfs table exists does not cause data to become inaccessible.
    """

    node = current().context.node

    with Given("VFS is not enabled"):
        check_vfs_state(enabled=False)

    with And("I have a table without vfs"):
        replicated_table_cluster(
            table_name="my_non_vfs_table",
            columns="d UInt64",
        )

    with And("I insert some data"):
        node.query(
            f"INSERT INTO my_non_vfs_table SELECT * FROM generateRandom('d UInt64') LIMIT 1000000"
        )
        assert_row_count(node=node, table_name="my_non_vfs_table", rows=1000000)

    with And("I enable allow_object_storage_vfs"):
        enable_vfs()

    with Then("the data remains accessible"):
        assert_row_count(node=node, table_name="my_non_vfs_table", rows=1000000)


@TestScenario
@Requirements(RQ_SRS_038_DiskObjectStorageVFS_Integrity_Detach("1.0"))
def bad_detached_part(self):
    """
    Test that a bad detached part on one replica does not affect the other replica.
    """

    table_name = "detach_table"

    with Given("I have a pair of clickhouse nodes"):
        nodes = self.context.ch_nodes[:2]

    with And("I enable allow_object_storage_vfs"):
        enable_vfs()

    try:
        with When("I create a replicated table on each node"):
            for i, node in enumerate(nodes):
                node.restart()
                node.query(
                    f"""
                    CREATE TABLE {table_name} (
                        d UInt64,
                    ) ENGINE = ReplicatedMergeTree('/clickhouse/tables/{table_name}', '{i + 1}')
                    ORDER BY d
                    SETTINGS storage_policy='external', min_bytes_for_wide_part=0
                """
                )

        with And("I insert data on the second node"):
            nodes[1].query(f"INSERT INTO {table_name} VALUES (123)")

        with And("I sync the first node"):
            nodes[0].query(f"SYSTEM SYNC REPLICA {table_name}")

        with And("I get the path for the part"):
            r = nodes[1].query(
                f"SELECT path FROM system.parts where table='{table_name}' and name='all_0_0_0'"
            )
            part_path = r.output
            assert part_path.startswith("/"), error("Expected absolute path!")

        with And("I delete the part's count.txt"):
            nodes[1].command(f"rm {part_path}/count.txt")

        with And("I detach the table on the second node"):
            nodes[1].query(f"DETACH TABLE {table_name} SYNC")

        with And("I reattach the table on the second node"):
            nodes[1].query(f"ATTACH TABLE {table_name}")

        with And("I check detached parts on the second node"):
            r = nodes[1].query(
                f"SELECT reason, name FROM system.detached_parts where table='{table_name}'"
            )
            assert r.output == "broken-on-start	broken-on-start_all_0_0_0", error()

        with And("I drop the table on the second node"):
            nodes[1].query(f"DROP TABLE {table_name} SYNC")

        with Then("The first node should still have the data"):
            r = nodes[0].query(f"SELECT * FROM {table_name}")
            assert r.output == "123", error()

    finally:
        with Finally("I drop the table on each node"):
            for node in nodes:
                node.query(f"DROP TABLE IF EXISTS {table_name} SYNC")


@TestStep(When)
def insert_data_time(self, node, table_name, days_ago, rows):
    t = time.mktime(
        (datetime.date.today() - datetime.timedelta(days=days_ago)).timetuple()
    )
    values = ",".join(f"({x},{t})" for x in range(rows))
    node.query(f"INSERT INTO {table_name} VALUES {values}")


@TestScenario
@Requirements(RQ_SRS_038_DiskObjectStorageVFS_Integrity_TTLDelete("1.0"))
def ttl_delete(self):
    """Check that TTL delete works properly when <allow_vfs> parameter is set to 1."""
    nodes = self.context.ch_nodes
    table_name = "ttl_delete"

    with Given("I enable vfs"):
        enable_vfs()

    with And("I have a replicated table"):
        replicated_table_cluster(
            table_name=table_name,
            storage_policy="tiered",
            columns="d UInt64, d1 DateTime",
            ttl="d1 + interval 2 day",
        )

    with When("I add data to the table"):
        with By("first inserting 200k rows"):
            insert_data_time(
                node=nodes[0], table_name=table_name, days_ago=7, rows=200000
            )

        with And("another insert of 400k rows"):
            insert_data_time(
                node=nodes[1], table_name=table_name, days_ago=3, rows=400000
            )

        with And("a large insert of 800k rows"):
            insert_data_time(
                node=nodes[2], table_name=table_name, days_ago=0, rows=800000
            )

    with Then("I check the row count"):
        retry(assert_row_count, timeout=5, delay=1)(
            node=nodes[0], table_name=table_name, rows=800000
        )


@TestScenario
@Requirements(RQ_SRS_038_DiskObjectStorageVFS_Integrity_TTLMove("1.0"))
def ttl_move(self):
    """Check that TTL moves work properly when <allow_vfs> parameter is set to 1."""
    nodes = self.context.ch_nodes
    table_name = "ttl_move"

    with Given("I enable vfs"):
        enable_vfs()

    with And("I have a replicated table"):
        replicated_table_cluster(
            table_name=table_name,
            storage_policy="tiered",
            columns="d UInt64, d1 DateTime",
            ttl="d1 + interval 2 day to volume 'external'",
        )

    with When("I add data to the table"):
        with By("first inserting 200k rows"):
            insert_data_time(
                node=nodes[0], table_name=table_name, days_ago=7, rows=200000
            )

        with And("another insert of 400k rows"):
            insert_data_time(
                node=nodes[1], table_name=table_name, days_ago=3, rows=400000
            )

        with And("a large insert of 800k rows"):
            insert_data_time(
                node=nodes[2], table_name=table_name, days_ago=0, rows=800000
            )

    with Then("I check the row count"):
        retry(assert_row_count, timeout=5, delay=1)(
            node=nodes[0], table_name=table_name, rows=1400000
        )


@TestOutline(Scenario)
@Requirements(RQ_SRS_038_DiskObjectStorageVFS_Integrity_Migration("1.0"))
@Examples("source destination", permutations(["replicated", "zero-copy", "vfs"], 2))
def migration(self, source, destination):
    node = self.context.node

    with Given("I have a replicated table"):
        _, replicated_table_name = replicated_table_cluster(
            storage_policy="external_no_vfs"
        )

    with And("I have a zero-copy table"):
        _, zero_copy_table_name = replicated_table_cluster(
            storage_policy="external_no_vfs", allow_zero_copy=True
        )

    with And("I have a vfs table"):
        _, vfs_table_name = replicated_table_cluster(storage_policy="external_vfs")

    table_names = {
        "replicated": replicated_table_name,
        "zero-copy": zero_copy_table_name,
        "vfs": vfs_table_name,
    }

    with And(f"I select {source} as the source table"):
        source_table_name = table_names[source]

    with And(f"I select {destination} as the destination table"):
        dest_table_name = table_names[destination]

    with And("I insert data to the source table"):
        insert_random(node=node, table_name=source_table_name, rows=1000000)

    with When("I copy the source table to the destination table"):
        node.query(f"INSERT INTO {dest_table_name} SELECT * from {source_table_name}")

    with And("I delete the source table"):
        node.query(f"DROP TABLE {source_table_name}")

    with Then("the data should be in the destination table"):
        assert_row_count(node=node, table_name=dest_table_name, rows=1000000)


@TestScenario
@Requirements(
    RQ_SRS_038_DiskObjectStorageVFS_Integrity_ConnectionInterruption_FaultInjection(
        "0.0"
    )
)
def fault_injection(self):
    """Test that ClickHouse is robust against injected faults"""
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
                    node.query(
                        f"""INSERT INTO {table_name} 
                        SELECT * FROM generateRandom('d UInt64') 
                        LIMIT {rows_per_insert} 
                        SETTINGS insert_keeper_fault_injection_probability={fault_probability}
                        """,
                        no_checks=True,
                    )

    with Then("I check the number of rows in the table"):
        retry(assert_row_count, timeout=5, delay=1)(
            node=nodes[0],
            table_name=table_name,
            rows=(rows_per_insert * insert_rounds * len(nodes)),
        )


# RQ_SRS_038_DiskObjectStorageVFS_Integrity_ConnectionInterruption


@TestFeature
@Name("integrity")
def feature(self):
    with Given("I have S3 disks configured"):
        s3_config()

    for scenario in loads(current_module(), Scenario):
        scenario()
