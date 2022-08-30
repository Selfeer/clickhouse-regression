#  Copyright 2020, Altinity LTD. All Rights Reserved.
#
#  All information contained herein is, and remains the property
#  of Altinity LTD. Any dissemination of this information or
#  reproduction of this material is strictly forbidden unless
#  prior written permission is obtained from Altinity LTD.
#
import time

from tiered_storage.tests.common import get_random_string
from tiered_storage.tests.common import get_used_disks_for_table
from testflows.core import TestScenario, Name, Requirements
from testflows.core import Given, When, And, Then, By, Finally, current
from testflows.asserts import error

from tiered_storage.requirements import *


@TestScenario
@Name("download appropriate disk advanced")
@Requirements(RQ_SRS_004_StoragePolicy_ReplicatedTable_DownloadedPartPlacement("1.0"))
def scenario(self, cluster, nodes=None):
    """Check that when parts are downloaded from a replica
    they are placed according to the storage policy specified for the table.
    We check that when placing the part each replica evaluates storage policy
    from bottom to the top and the same part on each replica can reside
    on different disks.

    The test uses cluster of 3 nodes. Trying to force the final merged part
    to be placed on each node as follows:

        * node0 - slow disk ( because fast and medium disks are filled up)
        * node1 - medium disk ( because fast disk is filled up)
        * node3 - fast disk
    """
    name = "replicated_table_download_appropriate_disk_advanced"

    if nodes is None:
        nodes = cluster.nodes["clickhouse"][:3]

    with Given(f"cluster nodes {nodes}"):
        nodes = [cluster.node(name) for name in nodes]

    try:
        with When("I create replicated table on each node"):
            for i, node in enumerate(nodes):
                node.query(
                    f"""
                    CREATE TABLE {name} (
                        EventDate Date,
                        number UInt64
                    ) ENGINE = ReplicatedMergeTree('/clickhouse/{name}', '{i + 1}')
                    ORDER BY tuple()
                    PARTITION BY toYYYYMM(EventDate)
                    SETTINGS storage_policy='fast_med_and_slow', old_parts_lifetime=1, cleanup_delay_period=1, cleanup_delay_period_random_add=2
                """
                )

        with And("I stop moves and merges on each node"):
            for node in nodes:
                node.query(f"SYSTEM STOP MOVES {name}")
                node.query(f"SYSTEM STOP MERGES {name}")

        def fill_up_disk(node, name, policy, size):
            with When(f"I fill up fast disk on the {node.name}"):
                with By(
                    "Creating a temporary table",
                    description="with storage policy that includes only the first disk",
                ):
                    node.query(
                        f"""
                        CREATE TABLE {name} (
                            s1 String
                        ) ENGINE = MergeTree()
                        ORDER BY tuple()
                        SETTINGS storage_policy='{policy}'
                    """
                    )

                with And("filling up temporary table to the max"):
                    data = []
                    for i in range(size):
                        data.append(get_random_string(cluster, 1024 * 1024))
                    values = ",".join(["('" + x + "')" for x in data])
                    node.query(f"INSERT INTO {name} VALUES {values}")

        def check_used_disks(node, name, expected):
            disks = get_used_disks_for_table(node, name)

            with Then(f"used disks should be {expected}", format_name=False):
                assert set(disks) == expected, error()

        with When(f"I fill up fast and medium disk on the first node"):
            fill_up_disk(
                nodes[0], name=name + "_temp", policy="one_small_disk", size=38
            )
            fill_up_disk(nodes[0], name=name + "_temp2", policy="only_jbod2", size=28)

        with And(f"I fill up fast disk on the second node"):
            fill_up_disk(
                nodes[1], name=name + "_temp", policy="one_small_disk", size=38
            )

        with When("I insert 6 values into first node"):
            node = nodes[0]
            node.query(f"INSERT INTO {name} VALUES(toDate('2019-03-15'), 65)")
            node.query(f"INSERT INTO {name} VALUES(toDate('2019-03-16'), 66)")
            node.query(f"INSERT INTO {name} VALUES(toDate('2019-03-17'), 42)")
            node.query(f"INSERT INTO {name} VALUES(toDate('2019-03-18'), 43)")
            node.query(f"INSERT INTO {name} VALUES(toDate('2019-03-19'), 32)")
            node.query(f"INSERT INTO {name} VALUES(toDate('2019-03-20'), 33)")

        with And("I restart moves and merges on each node"):
            for node in nodes:
                node.query(f"SYSTEM START MOVES {name}")
                node.query(f"SYSTEM START MERGES {name}")

        with And("I do system sync replica on each node"):
            for node in nodes:
                node.query(f"SYSTEM SYNC REPLICA {name}")

        with And("wait for replication and moves to complete"):
            time.sleep(3)

        with When("I check used disks on first node"):
            check_used_disks(nodes[0], name, {"external"})

        with And("I check used disks on second node"):
            check_used_disks(nodes[1], name, {"jbod2"})

        with And("I check used disks on third node"):
            check_used_disks(nodes[2], name, {"jbod1"})

        with When("I query replicated table on each node"):
            for node in nodes:
                with When(f"on node {node.name}"):
                    r = node.query(f"SELECT sum(number) FROM {name}").output.strip()
                    with Then("the result should match"):
                        assert r == "281", error()
    finally:
        with Finally("I drop all the tables on each node"):
            nodes[0].query(f"DROP TABLE IF EXISTS {name}_temp SYNC")
            nodes[0].query(f"DROP TABLE IF EXISTS {name}_temp2 SYNC")
            nodes[1].query(f"DROP TABLE IF EXISTS {name}_temp SYNC")

            for node in nodes:
                node.query(f"DROP TABLE IF EXISTS {name} SYNC")
