from testflows.core import *
from testflows.asserts import error

import rbac.helper.errors as errors
from rbac.requirements import *
from rbac.tests.sql_security.common import *
from helpers.common import getuid, get_settings_value


@TestScenario
@Requirements(
    RQ_SRS_006_RBAC_SQLSecurity_ModifySQLSecurity("1.0"),
)
def modify_sql_security(self):
    """Check that SQL security could be modified for an existing materialized views."""

    node = self.context.node

    default_default_view_definer = get_settings_value(
        setting_name="default_view_definer"
    )
    default_ignore_empty_sql_security_in_create_view_query = get_settings_value(
        setting_name="ignore_empty_sql_security_in_create_view_query",
        table="system.server_settings",
    )

    try:
        with Given(
            "I create view's source and target tables and populate target table"
        ):
            source_table_name = create_simple_MergeTree_table(column_name="x")
            target_table_name = create_simple_MergeTree_table(column_name="x")
            insert_data_from_numbers(table_name=target_table_name)

        with And(
            "I create user that will be set as default_view_definer and grant him SELECT privilege on mv's source and target tables"
        ):
            new_default_user_name = "new_default_view_definer_" + getuid()
            create_user(user_name=new_default_user_name)
            grant_privileges_directly(
                privileges=["SELECT"],
                user=new_default_user_name,
                object=source_table_name,
            )
            grant_privileges_directly(
                privileges=["SELECT"],
                user=new_default_user_name,
                object=target_table_name,
            )

        with And(
            f"I change default_view_definer setting to {new_default_user_name} for default user"
        ):
            entries = {
                "profiles": {
                    "default": {
                        "default_view_definer": f"{new_default_user_name}",
                    }
                }
            }
            change_core_settings(restart=True, entries=entries)

        with And(
            "I change ignore_empty_sql_security_in_create_view_query to 0 so defaults will be used"
        ):
            if default_ignore_empty_sql_security_in_create_view_query == "1":
                entries = {"ignore_empty_sql_security_in_create_view_query": "0"}
                change_core_settings(
                    restart=True,
                    entries=entries,
                    config_d_dir="/etc/clickhouse-server/config.d",
                    preprocessed_name="config.xml",
                )

        with And("I check that settings were changed"):
            assert (
                get_settings_value(setting_name="default_view_definer")
                == f"{new_default_user_name}"
            ), error()

            assert (
                get_settings_value(
                    setting_name="ignore_empty_sql_security_in_create_view_query",
                    table="system.server_settings",
                )
                == "0"
            ), error()

        with And("I create materialized view without specifying SQL security options"):
            mv_name = create_materialized_view(
                source_table_name=source_table_name,
                target_table_name=target_table_name,
            )

        with When("I create user and grant select privilege for mv"):
            user_name = "user_" + getuid()
            create_user(user_name=user_name)
            grant_privileges_directly(
                user=user_name,
                object=mv_name,
                privileges=["SELECT"],
            )

        with And("I check that user can select from mv"):
            output = self.context.node.query(
                f"SELECT sum(x) FROM {mv_name} FORMAT TabSeparated"
            ).output
            assert output == "45", error()

        with And("I create new definer user without any privileges"):
            new_definer_name = "new_definer_" + getuid()
            create_user(user_name=new_definer_name)

        with And("I modify SQL security to DEFINER for mv"):
            node.query(f"ALTER TABLE {mv_name} MODIFY DEFINER {new_definer_name}")

        with Then("I check that user can not select from mv"):
            exitcode, message = errors.not_enough_privileges(name=new_definer_name)
            node.query(
                f"SELECT * FROM {mv_name}",
                settings=[("user", user_name)],
                exitcode=exitcode,
                message=message,
            )

        with And("I try to set SQL security to INVOKER for materialized view"):
            node.query(
                f"ALTER TABLE {mv_name} MODIFY SQL SECURITY INVOKER",
                exitcode=141,
                message="B::Exception: SQL SECURITY INVOKER can't be specified for MATERIALIZED VIEW.",
            )

        with Then("I check create table query for mv"):
            create_table_query = node.query(f"SHOW CREATE TABLE {mv_name}").output
            assert (
                f"DEFINER = {new_definer_name} SQL SECURITY DEFINER"
                in create_table_query
            ), error()

    finally:
        with Finally("I restore default_default_view_definer setting"):
            entries = {
                "profiles": {
                    "default": {
                        "default_view_definer": f"{default_default_view_definer}",
                    }
                }
            }
            change_core_settings(restart=True, entries=entries)

        with And("I restore ignore_empty_sql_security_in_create_view_query setting"):
            changed = get_settings_value(
                setting_name="ignore_empty_sql_security_in_create_view_query",
                table="system.server_settings",
                column="changed",
            )

            if changed:
                entries = {
                    "ignore_empty_sql_security_in_create_view_query": f"{default_ignore_empty_sql_security_in_create_view_query}"
                }
                change_core_settings(
                    restart=True,
                    entries=entries,
                    config_d_dir="/etc/clickhouse-server/config.d",
                    preprocessed_name="config.xml",
                )

        with And("I check that settings were restored"):
            assert (
                get_settings_value(setting_name="default_view_definer")
                == f"{default_default_view_definer}"
            ), error()
            assert (
                get_settings_value(
                    setting_name="ignore_empty_sql_security_in_create_view_query",
                    table="system.server_settings",
                )
                == f"{default_ignore_empty_sql_security_in_create_view_query}"
            ), error()


@TestFeature
@Name("modify materialized view SQL security")
def feature(self):
    """Check SQL security functionality for materialized views."""
    self.context.node = self.context.cluster.node("clickhouse1")
    self.context.node_2 = self.context.cluster.node("clickhouse2")
    self.context.node_3 = self.context.cluster.node("clickhouse3")
    self.context.nodes = [self.context.node, self.context.node_2, self.context.node_3]

    Scenario(run=modify_sql_security)