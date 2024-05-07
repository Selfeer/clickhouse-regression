#!/usr/bin/env python3
import random
from itertools import chain
import time

from testflows.core import *
from testflows.combinatorics import combinations

from helpers.alter import *
from alter.stress.tests.actions import *
from alter.stress.tests.steps import *


def build_action_list(
    columns=True,
    projections=True,
    indexes=True,
    restarts=False,
    network_restarts=False,
    add_remove_replicas=False,
    fill_disks=False,
):
    actions = [
        delete_random_rows,
        detach_attach_random_partition,
        freeze_unfreeze_random_part,
        drop_random_part,
        replace_random_part,
        modify_random_ttl,
        remove_random_ttl,
        move_random_partition_to_random_disk,
        move_random_partition_to_random_table,
        attach_random_part_from_table,
        fetch_random_part_from_table,
    ]

    if restarts:
        actions += [restart_keeper, restart_clickhouse]

    if network_restarts:
        actions.append(restart_network)

    if add_remove_replicas:
        actions += [delete_replica, add_replica]

    if columns:
        actions += [
            add_random_column,
            rename_random_column,
            clear_random_column,
            delete_random_column,
            update_random_column,
        ]

    if projections:
        actions += [
            add_random_projection,
            clear_random_projection,
            drop_random_projection,
        ]
    else:
        actions += [delete_random_rows_lightweight]

    if indexes:
        actions += [
            add_random_index,
            clear_random_index,
            drop_random_index,
        ]

    if fill_disks:
        actions += [
            fill_clickhouse_disks,
            fill_zookeeper_disks,
        ]

    return actions


def build_action_groups(
    actions: list,
    combination_size=3,
    limit=10,
    shuffle=True,
    with_replacement=True,
):
    with Given(f"I make a list of groups of {combination_size} actions"):
        action_groups = list(
            combinations(actions, combination_size, with_replacement=with_replacement)
        )

    if shuffle:
        with And("I shuffle the list"):
            random.shuffle(action_groups)

    if limit:
        with And(f"I choose {limit} groups of actions"):
            action_groups = action_groups[:limit]

    return action_groups


@TestOutline(Scenario)
def alter_combinations(
    self,
    actions: list,
    limit=10,
    shuffle=True,
    combination_size=3,
    run_groups_in_parallel=True,
    run_optimize_in_parallel=True,
    ignore_failed_part_moves=False,
    sync_replica_timeout=600,
    storage_policy="tiered",
    minimum_replicas=1,
    maximum_replicas=3,
    n_tables=5,
    n_columns=50,
    insert_keeper_fault_injection_probability=0,
    network_impairment=False,
    limit_disk_space=False,
):
    """
    Perform combinations of alter actions, checking that all replicas agree.
    """

    self.context.ignore_failed_part_moves = ignore_failed_part_moves
    self.context.sync_replica_timeout = sync_replica_timeout
    self.context.storage_policy = storage_policy
    self.context.minimum_replicas = minimum_replicas
    self.context.maximum_replicas = maximum_replicas
    self.context.fault_probability = insert_keeper_fault_injection_probability

    assert not (
        restart_network in actions and network_impairment
    ), "network impairment is not compatible with restart_network"

    if fill_clickhouse_disks in actions or fill_zookeeper_disks in actions:
        assert (
            limit_disk_space
        ), "enable limit_disk_space when using fill_disks to avoid unexpected behavior"

    action_groups = build_action_groups(
        actions=actions,
        combination_size=combination_size,
        limit=limit,
        shuffle=shuffle,
    )

    # To test a single combination, uncomment and edit as needed.
    # action_groups = [
    #     [
    #         delete_replica,
    #         add_replica,
    #     ]
    # ]

    background_actions = [
        insert_to_random,
        select_count_random,
        select_sum_random,
        select_max_min_random,
    ]

    if limit_disk_space:
        with Given("Clickhouse is restarted with limited disk space"):
            for node in self.context.ch_nodes:
                limit_clickhouse_disks(node=node)

        with And("Zookeeper is restarted with limited disk space"):
            for node in self.context.zk_nodes:
                limit_zookeeper_disks(node=node)

    try:
        with Given(f"I create {n_tables} tables with {n_columns} columns and data"):
            self.context.table_names = []
            columns = "key DateTime," + ",".join(
                f"value{i} UInt16" for i in range(n_columns)
            )
            for i in range(n_tables):
                table_name = f"table{i}_{self.context.storage_policy}"
                replicated_table_cluster(
                    table_name=table_name,
                    storage_policy=self.context.storage_policy,
                    partition_by="toQuarter(key) - 1",
                    columns=columns,
                    ttl=f"key + INTERVAL {random.randint(1, 10)} YEAR",
                    no_cleanup=True,
                )
                self.context.table_names.append(table_name)
                insert_random(
                    node=self.context.node, table_name=table_name, columns=columns
                )

        with And("I create 10 random projections and indexes if required"):
            for _ in range(10):
                # safe=False because we don't need to waste time on extra checks during setup
                if drop_random_projection in actions:
                    add_random_projection(safe=False)

                if drop_random_index in actions:
                    add_random_index(safe=False)

        t = time.time()
        total_combinations = len(action_groups)
        for i, chosen_actions in enumerate(action_groups):
            title = f"{i+1}/{total_combinations} " + ",".join(
                [f"{f.name}" for f in chosen_actions]
            )

            if network_impairment:
                net_mode = random.choice(network_impairments)
                title += "," + net_mode.name

            with Check(title):
                if network_impairment:
                    with Given("a network impairment"):
                        impaired_network(network_mode=net_mode)

                with When("I perform a group of actions"):
                    for action in chain(background_actions, chosen_actions):
                        By(
                            f"I {action.name}",
                            run=action,
                            parallel=run_groups_in_parallel,
                            flags=TE | ERROR_NOT_COUNTED,
                        )

                    for table in self.context.table_names:
                        By(
                            f"I OPTIMIZE {table}",
                            test=optimize_random,
                            parallel=run_optimize_in_parallel,
                            flags=TE,
                        )(table_name=table_name)

                    join()

                with Then("I check that the replicas are consistent", flags=TE):
                    check_consistency()

            note(f"Average time per test combination {(time.time()-t)/(i+1):.1f}s")

    finally:
        with Finally("I log any pending mutations that might have caused a fail"):
            for node in self.context.ch_nodes:
                r = node.query(
                    "SELECT * FROM system.mutations WHERE is_done=0 FORMAT Vertical",
                    no_checks=True,
                )
                if r.output.strip():
                    note(f"Pending mutations on {node.name}:\n{r.output.strip()}")

        with Finally(
            "I drop each table on each node in case the cluster is in a bad state"
        ):
            for node in self.context.ch_nodes:
                for table_name in self.context.table_names:
                    When(test=delete_one_replica, parallel=True)(
                        node=node, table_name=table_name, timeout=120
                    )
            join()


@TestScenario
def safe(self):
    """
    Perform only actions that are relatively unlikely to cause crashes.
    """

    alter_combinations(
        actions=build_action_list(),
        limit=None if self.context.stress else 20,
    )


@TestScenario
def insert_faults(self):
    """
    Perform actions with keeper fault injection on inserts with VFS PR.
    """

    if not self.context.allow_vfs:
        skip("VFS is not enabled")

    alter_combinations(
        actions=build_action_list(),
        insert_keeper_fault_injection_probability=0.1,
        limit=None if self.context.stress else 20,
    )


@TestScenario
def network_faults(self):
    """
    Perform actions with random network interference.
    """

    alter_combinations(
        actions=build_action_list(),
        limit=None if self.context.stress else 20,
        network_impairment=True,
    )


@TestScenario
def restarts(self):
    """
    Allow restarting nodes randomly. High probability of crashes.
    """

    alter_combinations(
        actions=build_action_list(restarts=True),
        limit=None if self.context.stress else 20,
    )


@TestScenario
def add_remove_replicas(self):
    """
    Allow adding and removing replicas randomly.
    """

    alter_combinations(
        actions=build_action_list(add_remove_replicas=True),
        limit=None if self.context.stress else 20,
    )


@TestScenario
def full_disk(self):
    """
    Allow filling clickhouse and zookeeper disks.
    """

    alter_combinations(
        actions=self.build_action_list(fill_disks=True),
        limit=None if self.context.stress else 20,
        limit_disk_space=True,
    )


@TestFeature
def vfs(self):
    """Run test scenarios with vfs."""

    if check_clickhouse_version("<24.2")(self):
        skip("vfs not supported on ClickHouse < 24.2 and requires --allow-vfs flag")

    with Given("VFS is enabled"):
        enable_vfs(disk_names=["external", "external_tiered"])

    for scenario in loads(current_module(), Scenario):
        Scenario(run=scenario, tags=["long", "combinatoric"])


@TestFeature
def normal(self):
    """Run test scenarios without vfs."""

    for scenario in loads(current_module(), Scenario):
        Scenario(run=scenario, tags=["long", "combinatoric"])


@TestFeature
@Name("alter")
def feature(self):
    """Stress test with many alters."""

    # Workarounds
    # https://github.com/ClickHouse/ClickHouse/issues/62459
    self.context.disallow_move_partition_to_self = True

    with Given("I have S3 disks configured"):
        s3_config()

    if self.context.allow_vfs:
        Feature(run=vfs)
    else:
        Feature(run=normal)
