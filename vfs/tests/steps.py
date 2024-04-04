#!/usr/bin/env python3
import json
import time
from threading import Event

from testflows.core import *
from testflows.asserts import error
from testflows.combinatorics import combinations

from helpers.common import getuid, check_clickhouse_version
from helpers.queries import *

from s3.tests.common import s3_storage, check_bucket_size, get_bucket_size, get_stable_bucket_size, check_stable_bucket_size

DEFAULT_COLUMNS = "key UInt32, value1 String, value2 String, value3 String"
WIDE_PART_SETTING = "min_bytes_for_wide_part=0"
COMPACT_PART_SETTING = "min_bytes_for_wide_part=100000"


@TestStep(Given)
def s3_config(self):
    """Set up disks and policies for vfs tests."""
    with Given("I have two S3 disks configured"):
        disks = {
            "external": {
                "type": "s3",
                "endpoint": f"{self.context.uri}object-storage/storage/",
                "access_key_id": f"{self.context.access_key_id}",
                "secret_access_key": f"{self.context.secret_access_key}",
            },
            "external_vfs": {
                "type": "s3",
                "endpoint": f"{self.context.uri}object-storage/vfs/",
                "access_key_id": f"{self.context.access_key_id}",
                "secret_access_key": f"{self.context.secret_access_key}",
                "allow_vfs": "1",
            },
            "external_vfs_2": {
                "type": "s3",
                "endpoint": f"{self.context.uri}object-storage/vfs-2/",
                "access_key_id": f"{self.context.access_key_id}",
                "secret_access_key": f"{self.context.secret_access_key}",
                "allow_vfs": "1",
            },
            "external_no_vfs": {
                "type": "s3",
                "endpoint": f"{self.context.uri}object-storage/no-vfs/",
                "access_key_id": f"{self.context.access_key_id}",
                "secret_access_key": f"{self.context.secret_access_key}",
            },
            "external_tiered": {
                "type": "s3",
                "endpoint": f"{self.context.uri}object-storage/tiered/",
                "access_key_id": f"{self.context.access_key_id}",
                "secret_access_key": f"{self.context.secret_access_key}",
            },
        }

    with And("""I have a storage policy configured to use the S3 disk"""):
        policies = {
            "external": {"volumes": {"external": {"disk": "external"}}},
            "external_vfs": {"volumes": {"external": {"disk": "external_vfs"}}},
            "external_no_vfs": {"volumes": {"external": {"disk": "external_no_vfs"}}},
            "tiered": {
                "volumes": {
                    "default": {"disk": "external"},
                    "external": {"disk": "external_tiered"},
                }
            },
        }

    return s3_storage(
        disks=disks,
        policies=policies,
        restart=True,
        timeout=30,
        config_file="vfs_storage.xml",
    )


@TestStep(Given)
def check_vfs_state(
    self, node=None, enabled: bool = True, config_file="enable_vfs.xml"
):
    """Assert that vfs is enabled on at least one or on no disks in a config file."""
    if node is None:
        node = current().context.node

    c = f'grep "<allow_vfs>1" /etc/clickhouse-server/config.d/{config_file}'

    if enabled:
        node.command(c, exitcode=0)
    else:
        r = node.command(c, exitcode=None)
        assert r.exitcode in [1, 2], error()


@TestStep(Then)
def assert_row_count(self, node, table_name: str, rows: int = 1000000):
    """Assert that the number of rows in a table is as expected."""
    if node is None:
        node = current().context.node

    actual_count = get_row_count(node=node, table_name=table_name)
    assert rows == actual_count, error()


@TestStep(Given)
def replicated_table_cluster(
    self,
    table_name: str = None,
    storage_policy: str = "external",
    cluster_name: str = "replicated_cluster",
    columns: str = None,
    order_by: str = None,
    partition_by: str = None,
    primary_key: str = None,
    ttl: str = None,
    settings: str = None,
    allow_zero_copy: bool = None,
    exitcode: int = 0,
    no_cleanup=False,
):
    """Create a replicated table with the ON CLUSTER clause."""
    node = current().context.node

    if table_name is None:
        table_name = "table_" + getuid()

    if columns is None:
        columns = DEFAULT_COLUMNS

    if order_by is None:
        order_by = columns.split()[0]

    if settings is None:
        settings = []
    else:
        settings = [settings]

    settings.append(f"storage_policy='{storage_policy}'")

    if allow_zero_copy is not None:
        settings.append(f"allow_remote_fs_zero_copy_replication={int(allow_zero_copy)}")

    if partition_by is not None:
        partition_by = f"PARTITION BY ({partition_by})"
    else:
        partition_by = ""

    if primary_key is not None:
        primary_key = f"PRIMARY KEY {primary_key}"
    else:
        primary_key = ""

    if ttl is not None:
        ttl = "TTL " + ttl
    else:
        ttl = ""

    try:
        with Given("I have a table"):
            r = node.query(
                f"""
                CREATE TABLE IF NOT EXISTS {table_name} 
                ON CLUSTER '{cluster_name}' ({columns}) 
                ENGINE=ReplicatedMergeTree('/clickhouse/tables/{table_name}', '{{replica}}')
                ORDER BY {order_by} {partition_by} {primary_key} {ttl}
                SETTINGS {', '.join(settings)}
                """,
                settings=[("distributed_ddl_task_timeout ", 360)],
                exitcode=exitcode,
            )

        yield r, table_name

    finally:
        if not no_cleanup:
            with Finally(f"I drop the table"):
                for attempt in retries(timeout=120, delay=5):
                    with attempt:
                        node.query(
                            f"DROP TABLE IF EXISTS {table_name} ON CLUSTER '{cluster_name}' SYNC",
                            timeout=60,
                        )


@TestStep(Given)
def insert_random(
    self,
    node,
    table_name,
    columns: str = None,
    rows: int = 1000000,
    settings: str = None,
    **kwargs,
):
    """Insert random data to a table."""
    if columns is None:
        columns = DEFAULT_COLUMNS

    if settings:
        settings = "SETTINGS " + settings
    else:
        settings = ""

    return node.query(
        f"INSERT INTO {table_name} SELECT * FROM generateRandom('{columns}') LIMIT {rows} {settings}",
        exitcode=0,
        **kwargs,
    )


@TestStep(Given)
def create_one_replica(
    self,
    node,
    table_name,
    columns="d UInt64",
    order_by="d",
    partition_by=None,
    replica_path_suffix=None,
    replica_name="{replica}",
    no_checks=False,
    storage_policy="external",
):
    """
    Create a simple replicated table on the given node.
    Call multiple times with the same table name and different nodes
    to create multiple replicas.
    """
    if replica_path_suffix is None:
        replica_path_suffix = table_name

    if partition_by is not None:
        partition_by = f"PARTITION BY ({partition_by})"
    else:
        partition_by = ""

    r = node.query(
        f"""
        CREATE TABLE IF NOT EXISTS {table_name} ({columns}) 
        ENGINE=ReplicatedMergeTree('/clickhouse/tables/{replica_path_suffix}', '{replica_name}')
        ORDER BY ({order_by}) {partition_by}
        SETTINGS storage_policy='{storage_policy}'
        """,
        no_checks=no_checks,
        exitcode=0,
    )
    return r


@TestStep(Given)
def delete_one_replica(self, node, table_name, timeout=30):
    """Delete the local copy of a replicated table."""
    r = node.query(
        f"DROP TABLE IF EXISTS {table_name} SYNC", exitcode=0, timeout=timeout
    )
    return r


@TestStep(Given)
def enable_vfs(
    self,
    nodes=None,
    config_file="enable_vfs.xml",
    timeout=30,
    disk_names: list = None,
    vfs_gc_sleep_ms=2000,
):
    """
    Add the config file for object storage vfs for the disks in `disk_names`.
    Default disk names are ["external"].
    """
    if check_clickhouse_version("<24.2")(self):
        skip("vfs not supported on ClickHouse < 24.2 and requires --allow-vfs flag")

    if disk_names is None:
        disk_names = ["external"]

    disks = {
        n: {
            "allow_vfs": "1",
            "vfs_gc_sleep_ms": f"{vfs_gc_sleep_ms}",
        }
        for n in disk_names
    }

    policies = {}

    return s3_storage(
        disks=disks,
        policies=policies,
        nodes=nodes,
        restart=True,
        timeout=timeout,
        config_file=config_file,
    )


@TestStep(Then)
def check_consistency(self, nodes, table_name, sync_timeout=10):
    """SYNC the given nodes and check that they agree about the given table"""

    with When("I make sure all nodes are synced"):
        for node in nodes:
            sync_replica(
                node=node, table_name=table_name, timeout=sync_timeout, no_checks=True
            )

    with When("I query all nodes for their row counts"):
        row_counts = {}
        for node in nodes:
            row_counts[node.name] = get_row_count(node=node, table_name=table_name)

    with Then("All replicas should have the same state"):
        for n1, n2 in combinations(nodes, 2):
            assert row_counts[n1.name] == row_counts[n2.name], error()


@TestStep(When)
def repeat_until_stop(self, stop_event: Event, func, delay=0.5):
    """
    Call the given function with no arguments until stop_event is set.
    Use with parallel=True.
    """
    while not stop_event.is_set():
        func()
        time.sleep(delay)
