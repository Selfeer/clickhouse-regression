import sys

from testflows.core import *
from engines.requirements import *
from engines.tests.steps import *
from helpers.common import check_clickhouse_version


append_path(sys.path, "..")

insert_values = (
    " ('data1', 1, 0),"
    " ('data1', 2, 0),"
    " ('data1', 3, 0),"
    " ('data1', 3, 0),"
    " ('data1', 1, 1),"
    " ('data1', 2, 1),"
    " ('data2', 1, 0),"
    " ('data2', 2, 0),"
    " ('data2', 3, 0),"
    " ('data2', 3, 1),"
    " ('data2', 1, 1),"
    " ('data2', 2, 1),"
    " ('data3', 1, 0),"
    " ('data3', 2, 0),"
    " ('data3', 3, 0),"
    " ('data3', 3, 1),"
    " ('data3', 1, 1),"
    " ('data3', 2, 1)"
)


@TestScenario
def final(self, node=None):
    """Test to check 'FINAL' clause behaviour
    https://kb.altinity.com/engines/mergetree-table-engine-family/replacingmergetree/"""
    if node is None:
        node = self.context.cluster.node("clickhouse1")

    name = f"repl_tbl_part_{getuid()}"

    try:
        with Given("I create table with ReplacingMergeTree engine"):
            node.query(
                f"CREATE TABLE {name} (key UInt32, value UInt32, part_key UInt32) ENGINE = ReplacingMergeTree"
                f" PARTITION BY part_key ORDER BY key;"
            )

        with When("I insert data in this table"):
            node.query(
                f"INSERT INTO {name} SELECT 1 AS key, number AS value, number % 2 AS part_key FROM numbers(4)"
                f" SETTINGS optimize_on_insert = 0;"
            )

        with Then("I select all data from the table"):
            node.query(f"SELECT count(*) FROM {name};", message="4")

        with And("I select all data from the table with --final"):
            node.query(
                f"SELECT count(*) FROM {name};", message="1", settings=[("final", 1)]
            )

        with And(
            "I select all data from the table with --final and --do_not_merge_across_partitions_select_final"
        ):
            node.query(
                f"SELECT count(*) FROM {name};",
                message="2",
                settings=[
                    ("final", 1),
                    ("do_not_merge_across_partitions_select_final", 1),
                ],
            )

        with And("I optimize table"):
            node.query(
                f"OPTIMIZE TABLE {name} FINAL;",
            )

        with Then("I select again all data from the table"):
            node.query(f"SELECT count(*) FROM {name};", message="2")

    finally:
        with Finally("I drop table"):
            node.query(f"DROP TABLE IF EXISTS {name}")


@TestScenario
def without_is_deleted(self, node=None):
    """Check the behaviour without the is_deleted column"""
    if node is None:
        node = self.context.cluster.node("clickhouse1")

    name = f"without_is_deleted_{getuid()}"

    try:
        with Given("I create table without is_deleted column"):
            node.query(
                f"CREATE TABLE IF NOT EXISTS {name} (id String, version UInt32, is_deleted UInt8)"
                f" ENGINE = ReplacingMergeTree(version) ORDER BY id"
            )

        with When("I insert data in this table"):
            node.query(
                f"INSERT INTO {name} VALUES {insert_values}",
                settings=[("optimize_on_insert", 0)],
            )

        with Then("I select all data from the table"):
            node.query(f"SELECT count(*) FROM {name};", message="18")

        with And("I select all data from the table with --final"):
            node.query(
                f"SELECT count(*) FROM {name};", message="3", settings=[("final", 1)]
            )

        with And("I optimize table"):
            node.query(
                f"OPTIMIZE TABLE {name} FINAL;",
            )

        with Then("I select again all data from the table"):
            node.query(f"SELECT count(*) FROM {name};", message="3")

    finally:
        with Finally("I drop table"):
            node.query(f"DROP TABLE IF EXISTS {name}")


@TestScenario
def clean_deleted_rows_without_is_deleted(self, node=None):
    """Check the behaviour without the is_deleted column and with clean_deleted_rows='Always'"""
    if node is None:
        node = self.context.cluster.node("clickhouse1")

    name = f"clean_deleted_rows_without_is_deleted_{getuid()}"

    try:
        with Given("I create table without is_deleted column and with clean_deleted_rows='Always'"):
            node.query(
                f"CREATE TABLE IF NOT EXISTS {name} (id String, version UInt32, is_deleted UInt8)"
                f" ENGINE = ReplacingMergeTree(version) ORDER BY id SETTINGS clean_deleted_rows='Always'"
            )

        with When("I insert data in this table"):
            node.query(
                f"INSERT INTO {name} VALUES {insert_values}",
                settings=[("optimize_on_insert", 0)],
            )

        with Then("I select all data from the table"):
            node.query(f"SELECT count(*) FROM {name};", message="18")

        with And("I select all data from the table with --final"):
            node.query(
                f"SELECT count(*) FROM {name};", message="3", settings=[("final", 1)]
            )

        with And("I optimize table"):
            node.query(
                f"OPTIMIZE TABLE {name} FINAL;",
            )

        with Then("I select again all data from the table"):
            node.query(f"SELECT count(*) FROM {name};", message="3")

    finally:
        with Finally("I drop table"):
            node.query(f"DROP TABLE IF EXISTS {name}")


@TestScenario
def with_is_deleted(self, node=None):
    """Check the behaviour with the is_deleted column"""
    if node is None:
        node = self.context.cluster.node("clickhouse1")

    name = f"clean_deleted_rows_with_is_deleted_{getuid()}"

    try:
        with Given("I create table with is_deleted column"):
            node.query(
                f"CREATE TABLE IF NOT EXISTS {name} (id String, version UInt32, is_deleted UInt8)"
                f" ENGINE = ReplacingMergeTree(version, is_deleted) ORDER BY id"
            )

        with When("I insert data in this table"):
            node.query(
                f"INSERT INTO {name} VALUES {insert_values}",
                settings=[("optimize_on_insert", 0)],
            )

        with Then("I select all data from the table"):
            node.query(f"SELECT count(*) FROM {name};", message="18")

        with And("I select all data from the table with --final"):
            node.query(
                f"SELECT count(*) FROM {name};", message="1", settings=[("final", 1)]
            )

        with And("I optimize table"):
            node.query(
                f"OPTIMIZE TABLE {name} FINAL;",
            )

        with Then("I select again all data from the table"):
            node.query(f"SELECT count(*) FROM {name};", message="3")

    finally:
        with Finally("I drop table"):
            node.query(f"DROP TABLE IF EXISTS {name}")


@TestScenario
def clean_deleted_rows_with_is_deleted(self, node=None):
    """Check the behaviour with the is_deleted column and with clean_deleted_rows='Always'"""
    if node is None:
        node = self.context.cluster.node("clickhouse1")

    name = f"clean_deleted_rows_with_is_deleted_{getuid()}"

    try:
        with Given(
            "I create table with is_deleted column and clean_deleted_rows='Always'"
        ):
            node.query(
                f"CREATE TABLE IF NOT EXISTS {name} (id String, version UInt32, is_deleted UInt8)"
                f" ENGINE = ReplacingMergeTree(version, is_deleted) ORDER BY id SETTINGS clean_deleted_rows='Always'"
            )

        with When("I insert data in this table"):
            node.query(
                f"INSERT INTO {name} VALUES {insert_values}",
                settings=[("optimize_on_insert", 0)],
            )

        with Then("I select all data from the table"):
            node.query(f"SELECT count(*) FROM {name};", message="18")

        with And("I select all data from the table with --final"):
            node.query(
                f"SELECT count(*) FROM {name};", message="1", settings=[("final", 1)]
            )

        with And("I optimize table"):
            node.query(
                f"OPTIMIZE TABLE {name} FINAL;",
            )

        with Then("I select again all data from the table"):
            node.query(f"SELECT count(*) FROM {name};", message="1")

    finally:
        with Finally("I drop table"):
            node.query(f"DROP TABLE IF EXISTS {name}")


@TestModule
@Name("general")
def feature(self):
    """Check new ReplacingMergeTree engine."""
    if check_clickhouse_version("<23.2")(self):
        skip(
            reason="--final query setting is only supported on ClickHouse version >= 23.2"
        )

    with Pool(1) as executor:
        try:
            for scenario in loads(current_module(), Scenario):
                Feature(test=scenario, parallel=True, executor=executor)()
        finally:
            join()