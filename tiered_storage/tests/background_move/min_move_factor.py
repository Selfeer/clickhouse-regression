#  Copyright 2019, Altinity LTD. All Rights Reserved.
#
#  All information contained herein is, and remains the property
#  of Altinity LTD. Any dissemination of this information or
#  reproduction of this material is strictly forbidden unless
#  prior written permission is obtained from Altinity LTD.
#
import time
from tiered_storage.tests.common import get_used_disks_for_table, get_random_string
from testflows.core import *
from testflows.asserts import error


@TestScenario
@Name("min move factor")
@Examples(
    "name engine",
    [
        ("moving_min_move_factor_mt", "MergeTree()"),
        (
            "moving_min_move_factor_replicated_mt",
            "ReplicatedMergeTree('/clickhouse/moving_replicated_mt', '1')",
        ),
    ],
)
def scenario(self, cluster, node="clickhouse1"):
    """Check that with the minimum value of **move_factor** of 0
    in the background no parts are moved to the external volume.
    """
    with Given("cluster"):
        node = cluster.node(node)
        for example in self.examples:
            name, engine = example
            with When(f"for example table name='{name}', engine='{engine}'"):
                with When("I create table"):
                    node.query(
                        f"""
                        CREATE TABLE {name} (
                            s1 String
                        ) ENGINE = {engine}
                        ORDER BY tuple()
                        SETTINGS storage_policy='moving_min_jbod_with_external'
                    """
                    )

                with And("I get table's uuid"):
                    table_uuid = node.query(
                        f"SELECT uuid FROM system.tables WHERE name = '{name}'"
                    ).output.strip()
                    table_uuid_prefix = table_uuid[:3]

                try:
                    with And("I stop merges to avoid conflicts"):
                        node.query(f"SYSTEM STOP MERGES {name}")

                    with And(
                        "I fill up first disk above 97%%",
                        description="small jbod size is 40MB",
                    ):
                        with By("first inserting 4MB of data with 4 rows 1MB each"):
                            data = []
                            for i in range(4):
                                data.append(
                                    get_random_string(cluster, 1024 * 1024, steps=False)
                                )
                            values = ",".join(["('" + x + "')" for x in data])
                            node.query(f"INSERT INTO {name} VALUES {values}")

                        with And(
                            "then inserting 7 times 5MB of data with 5 rows 1MB each"
                        ):
                            for i in range(7):
                                data = []
                                for i in range(5):
                                    data.append(
                                        get_random_string(
                                            cluster, 1024 * 1024, steps=False
                                        )
                                    )
                                values = ",".join(["('" + x + "')" for x in data])
                                node.query(f"INSERT INTO {name} VALUES {values}")

                    with When(
                        "poll maximum 20 times to check used disks for the table"
                    ):
                        used_disks = get_used_disks_for_table(node, name)
                        retry = 20
                        i = 0
                        while not used_disks.count("jbod1") < 8 and i < retry:
                            with And("sleep 0.5 sec"):
                                time.sleep(0.5)
                            used_disks = get_used_disks_for_table(node, name)
                            i += 1

                    with Then("check that jbod1 disk is used for all the parts"):
                        assert used_disks.count("jbod1") == 8, error()

                    with When("I read path_on_disk from system.part_log"):
                        path = (
                            node.query(
                                f"SELECT path_on_disk FROM system.part_log WHERE table = '{name}'"
                                " AND event_type='MovePart' ORDER BY event_time"
                            )
                            .output.strip()
                            .splitlines()
                        )

                    with And(
                        "path_on_disk for all parts should have path to the jbod1"
                    ):
                        for p in path:
                            assert p.startswith("/jbod1"), error()

                    with When("I check if parts were deleted from jbod1"):
                        entries = (
                            node.command(
                                f"find /jbod1/store/{table_uuid_prefix}/{table_uuid}/ -name 'all_*'",
                                exitcode=0,
                            )
                            .output.strip()
                            .splitlines()
                        )

                    with Then("number of parts left on jbod1 should be 8"):
                        assert len(entries) == 8, error()

                finally:
                    with Finally("I drop the table"):
                        node.query(f"DROP TABLE IF EXISTS {name} SYNC")
