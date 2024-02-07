#!/usr/bin/env python3
import random
from itertools import combinations, chain

from testflows.core import *

from vfs.tests.steps import *
from vfs.requirements import *
from vfs.tests.stress_alter import optimize, check_consistency


@TestScenario
@Requirements(
    RQ_SRS_038_DiskObjectStorageVFS_Settings_ZeroCopyIncompatible("1.0"),
    RQ_SRS_038_DiskObjectStorageVFS_Settings_Shared_TTL("1.0"),
)
def incompatible_with_zero_copy(self):
    """
    Check that using zero copy replication when vfs is enabled is not allowed.
    """
    with Given("VFS is globally enabled"):
        enable_vfs()

    with When("I create a replicated table with both vfs and 0-copy enabled"):
        r, _ = replicated_table_cluster(
            table_name="vfs_zero_copy_replication",
            allow_zero_copy=True,
            exitcode=None,
        )

    with Then("I expect it to fail"):
        assert r.exitcode != 0, error()


@TestStep(When)
def create_insert_measure_replicated_table(self, storage_policy="external"):
    nodes = self.context.ch_nodes
    n_rows = 100_000
    columns = "d UInt64, m UInt64"

    with Given("an s3 bucket with a known amount of data"):
        size_before = get_bucket_size(
            name=self.context.bucket_name,
            prefix=self.context.bucket_path,
            minio_enabled=self.context.minio_enabled,
            access_key=self.context.secret_access_key,
            key_id=self.context.access_key_id,
        )

    with When("a replicated table is created successfully"):
        _, table_name = replicated_table_cluster(
            columns=columns, exitcode=0, storage_policy=storage_policy
        )

    with And("I add data to the table"):
        insert_random(
            node=nodes[0],
            table_name=table_name,
            columns=columns,
            rows=n_rows,
        )

    with And("I wait for the replicas to sync", flags=TE):
        # nodes[1].query(f"SYSTEM SYNC REPLICA {table_name}", timeout=300)
        # nodes[2].query(f"SYSTEM SYNC REPLICA {table_name}", timeout=300)
        retry(assert_row_count, timeout=120, delay=1)(
            node=nodes[0], table_name=table_name, rows=n_rows
        )
        retry(assert_row_count, timeout=120, delay=1)(
            node=nodes[1], table_name=table_name, rows=n_rows
        )
        retry(assert_row_count, timeout=120, delay=1)(
            node=nodes[2], table_name=table_name, rows=n_rows
        )

    with And("I get the size of the data added to s3"):
        size_after = get_bucket_size(
            name=self.context.bucket_name,
            prefix=self.context.bucket_path,
            minio_enabled=self.context.minio_enabled,
            access_key=self.context.secret_access_key,
            key_id=self.context.access_key_id,
        )
        size = size_after - size_before

    return size


@TestScenario
@Requirements(
    RQ_SRS_038_DiskObjectStorageVFS_Settings_Disk("1.0"),
    RQ_SRS_038_DiskObjectStorageVFS_Settings_Shared_TTL("1.0"),
)
def disk_setting(self):
    """
    Check that allow_vfs can be enabled per disk.
    """
    with When("I measure the disk usage after create and insert without vfs"):
        size_no_vfs = create_insert_measure_replicated_table(
            storage_policy="external_no_vfs"
        )
        assert size_no_vfs > 0, error()

    with When(
        "I measure the disk usage after create and insert with vfs config in one file"
    ):
        size_vfs = create_insert_measure_replicated_table(storage_policy="external_vfs")

    with Then("Data usage should be less than half compared to no vfs"):
        assert size_vfs <= size_no_vfs // 2, error()

    with Given("VFS is enabled for 'external' disk"):
        enable_vfs(disk_names=["external"])

    with When(
        "I measure the disk usage after create and insert with vfs config in a separate file"
    ):
        size_vfs = create_insert_measure_replicated_table(storage_policy="external")

    with Then("Data usage should be less than half compared to no vfs"):
        assert size_vfs <= size_no_vfs // 2, error()


@TestScenario
@Requirements(RQ_SRS_038_DiskObjectStorageVFS_Settings_VFSToggled("1.0"))
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

        with Then("the data is accessible"):
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
@Requirements(RQ_SRS_038_DiskObjectStorageVFS_Settings_VFSToggled("1.0"))
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


@TestStep
@Retry(timeout=10, delay=1)
def insert(self, table_name, settings):
    node = random.choice(self.context.ch_nodes)
    with By(f"inserting rows to {table_name} on {node.name} with settings {settings}"):
        insert_random(node=node, table_name=table_name, settings=settings, rows=5000000)


@TestStep
@Retry(timeout=10, delay=1)
def select(self, table_name, settings=None):
    node = random.choice(self.context.ch_nodes)
    if settings:
        settings = "SETTINGS " + settings
    for _ in range(random.randint(3, 10)):
        with By(f"count rows in {table_name} on {node.name}"):
            node.query(f"SELECT count() FROM {table_name} {settings}")


def combinations_all_lengths(items):
    return chain(*[combinations(items, i + 1) for i in range(len(items))])


@TestSketch(Scenario)
@Requirements(
    RQ_SRS_038_DiskObjectStorageVFS_Settings_Shared("0.0"),
    RQ_SRS_038_DiskObjectStorageVFS_Settings_Shared_S3("1.0"),
    RQ_SRS_038_DiskObjectStorageVFS_Settings_Shared_ReadBackoff("1.0"),
    RQ_SRS_038_DiskObjectStorageVFS_Settings_Shared_ConcurrentRead("1.0"),
)
def combination(self):
    """Perform concurrent inserts and selects with a combination of settings"""

    table_setting = either(
        None,
        "remote_fs_execute_merges_on_single_replica_time_threshold=0",
        "zero_copy_merge_mutation_min_parts_size_sleep_before_lock=0",
    )

    select_setting = either(
        None,
        "merge_tree_min_rows_for_concurrent_read_for_remote_filesystem=0",
        "merge_tree_min_bytes_for_concurrent_read_for_remote_filesystem=0",
    )

    insert_setting_choices = [
        "s3_truncate_on_insert=1",
        "s3_create_new_file_on_insert=1",
        "s3_skip_empty_files=1",
        f"s3_max_single_part_upload_size={int(32*1024)}",
    ]

    insert_setting = either(
        None,
        *[",".join(c) for c in combinations_all_lengths(insert_setting_choices)],
    )

    storage_setting = either(
        None,
        "remote_fs_read_backoff_threshold=0",
        "remote_fs_read_backoff_max_tries=0",
    )

    with Check(
        f"Settings: table:{table_setting}, insert:{insert_setting}, select:{select_setting}, disk:{storage_setting}"
    ):
        if storage_setting is not None:
            with Given(f"storage with settings {storage_setting}"):
                storage_setting = storage_setting.split("=")
                disks = {
                    "external": {
                        storage_setting[0]: storage_setting[1],
                    }
                }
                storage_config(disks=disks, restart=True)

        with Given("a replicated table"):
            _, table_name = replicated_table_cluster(
                storage_policy="external_vfs",
                exitcode=0,
                settings=table_setting,
            )

        with And("some inserted data"):
            insert(table_name=table_name, settings=insert_setting)

        When(
            f"I INSERT in parallel",
            test=insert,
            parallel=True,
            flags=TE,
        )(table_name=table_name, settings=insert_setting)
        When(
            f"I SELECT in parallel",
            test=select,
            parallel=True,
            flags=TE,
        )(table_name=table_name, settings=select_setting)
        When(
            f"I OPTIMIZE {table_name}",
            test=optimize,
            parallel=True,
            flags=TE,
        )(table_name=table_name)

        join()

        with Then("I check that the replicas are consistent", flags=TE):
            check_consistency(tables=[table_name])


@TestFeature
@Name("settings")
@Requirements(RQ_SRS_038_DiskObjectStorageVFS_Providers_Configuration("1.0"))
def feature(self):
    with Given("I have S3 disks configured"):
        s3_config()

    for scenario in loads(current_module(), Scenario):
        scenario()
