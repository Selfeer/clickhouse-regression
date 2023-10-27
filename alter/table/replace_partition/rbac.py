from testflows.core import *
from testflows.asserts import *
from alter.table.replace_partition.requirements.requirements import *
from helpers.common import getuid, create_user, replace_partition
from helpers.tables import (
    create_table_partitioned_by_column,
    insert_into_table_random_uint64,
)


@TestStep(Given)
def no_privileges(self, node, name, on):
    """Grant no privileges to a user."""
    with By("Granting the user no privileges"):
        node.query(f"GRANT NONE ON {on} TO {name}")


@TestStep(Given)
def select_privileges(self, node, name, on):
    """Grant only select privileges to a user."""
    with By("Granting the user only select privileges"):
        node.query(f"GRANT SELECT ON {on} TO {name}")


@TestStep(Given)
def insert_privileges(self, node, name, on):
    """Grant only insert privileges to a user."""
    with By("Granting the user only insert privileges"):
        node.query(f"GRANT INSERT ON {on} TO {name}")


@TestStep(Given)
def alter_privileges(self, node, name, on):
    """Grant only alter privileges to a user."""
    with By("Granting the user only alter privileges"):
        node.query(f"GRANT ALTER ON {on} TO {name}")


@TestStep(Given)
def alter_table_privileges(self, node, name, on):
    """Grant only alter table privileges to a user."""
    with By("Granting the user only alter table privileges"):
        node.query(f"GRANT ALTER TABLE ON {on} TO {name}")


@TestStep(When)
def get_privileges_as_list_of_strings(self, privileges: list):
    """The test check takes a list of privileges to assign to a specific table for a user.

    This test step takes the list of test steps that grant privilege and converts it to the list of privilege names as
    strings.
    """
    privilege_names = []
    for privilege in privileges:
        privilege_names.append(privilege.__name__)

    return privilege_names


@TestStep(Check)
def check_if_partition_values_on_destination_changed(
    self, source_table, destination_table, user_name, changed=True
):
    """Assert two possabilities:
    - When we expect that replace partition was successful due to valid privileges.
    - When we expect that replace partition was not successful due to invalid privileges.
    """
    node = self.context.node

    with By(
        "Trying to replace partition on the destination table as a user with set privileges"
    ):
        if changed:
            replace_partition(
                destination_table=destination_table,
                source_table=source_table,
                user_name=user_name,
            )
        else:
            replace_partition(
                destination_table=destination_table,
                source_table=source_table,
                user_name=user_name,
                message=f"Exception: {user_name}: Not enough privileges.",
                exitcode=241,
            )

    with And(
        "Checking if the data on the specific partition was replaced or not",
        description="The data on the destination table should only be replaced if the user has privileges needed"
        " for that action",
    ):
        partition_values_source = node.query(f"SELECT i FROM {source_table} ORDER BY i")
        partition_values_destination = node.query(
            f"SELECT i FROM {destination_table} ORDER BY i"
        )

        if changed:
            assert (
                partition_values_source.output.strip()
                == partition_values_destination.output.strip()
            ), error()
        else:
            assert (
                partition_values_source.output.strip()
                != partition_values_destination.output.strip()
            ), error()


@TestCheck
def user_replace_partition_with_privileges(
    self,
    destination_table_privileges,
    source_table_privileges,
):
    """A test check to grant a user a set of privileges on both destination and source tables to see if replace
    partition is possible with these privileges."""
    node = self.context.node
    user_name = f"user_{getuid()}"
    destination_table = f"destination_{getuid()}"
    source_table = f"source_{getuid()}"

    with Given(
        "I create a destination table and a source table that are partitioned by the same column"
    ):
        create_table_partitioned_by_column(table_name=source_table)
        create_table_partitioned_by_column(table_name=destination_table)

    with And("I insert data into both tables"):
        insert_into_table_random_uint64(
            table_name=destination_table, number_of_values=10
        )
        insert_into_table_random_uint64(table_name=source_table, number_of_values=10)

    with And("I create a user"):
        create_user(node=node, name=user_name)

    with When(
        "I grant specific privileges for destination table and source table to a created user"
    ):
        for grant_privilege in destination_table_privileges:
            grant_privilege(node=node, name=user_name, on=destination_table)

        for grant_privilege in source_table_privileges:
            grant_privilege(node=node, name=user_name, on=source_table)

    with And("I save the list of privileges that I granted on both tables"):
        destination_privileges = get_privileges_as_list_of_strings(
            privileges=destination_table_privileges
        )
        source_privileges = get_privileges_as_list_of_strings(
            privileges=source_table_privileges
        )

    with Then(
        f"I check that replacing partition is possible on the destination table when correct privileges are set",
        description=f"""
            Destination table privileges: {destination_privileges}
            Source table privileges: {source_privileges}
            """,
    ):
        if ("select_privileges" in source_privileges) and (
            (
                "alter_privileges" in destination_privileges
                and "insert_privileges" in destination_privileges
            )
            or (
                "alter_table_privileges" in destination_privileges
                and "insert_privileges" in destination_privileges
            )
        ):
            check_if_partition_values_on_destination_changed(
                destination_table=destination_table,
                source_table=source_table,
                user_name=user_name,
            )
        else:
            check_if_partition_values_on_destination_changed(
                destination_table=destination_table,
                source_table=source_table,
                user_name=user_name,
                changed=False,
            )


@TestSketch(Scenario)
@Flags(TE)
def check_replace_partition_with_privileges(self):
    """Run the test check with different privilege combinations."""
    values = {
        no_privileges,
        select_privileges,
        alter_privileges,
        alter_table_privileges,
        insert_privileges,
    }

    destination_table_privileges = [
        either(*values, i="first_privilege"),
        either(*values, i="second_privileges"),
    ]
    source_table_privileges = [
        either(*values, i="first_privilege"),
        either(*values, i="second_privileges"),
    ]

    user_replace_partition_with_privileges(
        destination_table_privileges=destination_table_privileges,
        source_table_privileges=source_table_privileges,
    )


@TestFeature
@Requirements(RQ_SRS_032_ClickHouse_Alter_Table_ReplacePartition_RBAC("1.0"))
@Name("rbac")
def feature(self, node="clickhouse1"):
    """Check that it is possible to replace partition on a table as a user with given privileges.

    Privileges:
    * None
    * Select
    * Insert
    * Alter
    * Alter Table
    """
    self.context.node = self.context.cluster.node(node)

    Scenario(run=check_replace_partition_with_privileges)