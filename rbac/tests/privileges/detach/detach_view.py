from rbac.requirements import *
from rbac.helper.common import *
import rbac.helper.errors as errors


@TestSuite
def privilege_granted_directly_or_via_role(self, node=None):
    """Check that user is only able to execute DETACH VIEW when they have required privilege, either directly or via role."""
    role_name = f"role_{getuid()}"
    user_name = f"user_{getuid()}"

    if node is None:
        node = self.context.node

    with Suite("user with direct privilege"):
        with user(node, user_name):
            with When(
                f"I run checks that {user_name} is only able to execute DETACH VIEW with required privileges"
            ):
                privilege_check(
                    grant_target_name=user_name, user_name=user_name, node=node
                )

    with Suite("user with privilege via role"):
        with user(node, user_name), role(node, role_name):
            with When("I grant the role to the user"):
                node.query(f"GRANT {role_name} TO {user_name}")

            with And(
                f"I run checks that {user_name} with {role_name} is only able to execute DETACH VIEW with required privileges"
            ):
                privilege_check(
                    grant_target_name=role_name, user_name=user_name, node=node
                )


def privilege_check(grant_target_name, user_name, node=None):
    """Run scenarios to check the user's access with different privileges."""
    exitcode, message = errors.not_enough_privileges(name=f"{user_name}")

    with Scenario("user without privilege"):
        view_name = f"view_{getuid()}"

        try:
            with Given("I have a view"):
                node.query(f"CREATE VIEW {view_name} AS SELECT 1")

            with When("I grant the user NONE privilege"):
                node.query(f"GRANT NONE TO {grant_target_name}")

            with And("I grant the user USAGE privilege"):
                node.query(f"GRANT USAGE ON *.* TO {grant_target_name}")

            with When("I attempt to drop a view without privilege"):
                node.query(
                    f"DETACH VIEW {view_name}",
                    settings=[("user", user_name)],
                    exitcode=exitcode,
                    message=message,
                )

        finally:
            with Finally("I reattach the view as a table", flags=TE):
                node.query(f"ATTACH VIEW IF NOT EXISTS {view_name} AS SELECT 1")
            with And("I drop the view", flags=TE):
                node.query(f"DROP VIEW IF EXISTS {view_name}")

    with Scenario("user with privilege"):
        view_name = f"view_{getuid()}"

        try:
            with Given("I have a view"):
                node.query(f"CREATE VIEW {view_name} AS SELECT 1")

            with When("I grant drop view privilege"):
                node.query(f"GRANT DROP VIEW ON {view_name} TO {grant_target_name}")

            with Then("I attempt to drop a view"):
                node.query(f"DETACH VIEW {view_name}", settings=[("user", user_name)])

        finally:
            with Finally("I reattach the view as a table", flags=TE):
                node.query(f"ATTACH VIEW IF NOT EXISTS {view_name} AS SELECT 1")
            with And("I drop the table", flags=TE):
                node.query(f"DROP VIEW IF EXISTS {view_name}")

    with Scenario("user with revoked privilege"):
        view_name = f"view_{getuid()}"

        try:
            with Given("I have a view"):
                node.query(f"CREATE VIEW {view_name} AS SELECT 1")

            with When("I grant the drop view privilege"):
                node.query(f"GRANT DROP VIEW ON {view_name} TO {grant_target_name}")

            with And("I revoke the drop view privilege"):
                node.query(f"REVOKE DROP VIEW ON {view_name} FROM {grant_target_name}")

            with Then("I attempt to drop a  view"):
                node.query(
                    f"DETACH VIEW {view_name}",
                    settings=[("user", user_name)],
                    exitcode=exitcode,
                    message=message,
                )

        finally:
            with Finally("I reattach the view as a table", flags=TE):
                node.query(f"ATTACH VIEW IF NOT EXISTS {view_name} AS SELECT 1")
            with And("I drop the view", flags=TE):
                node.query(f"DROP VIEW IF EXISTS {view_name}")

    with Scenario("user with revoked ALL privilege"):
        view_name = f"view_{getuid()}"

        try:
            with Given("I have a view"):
                node.query(f"CREATE VIEW {view_name} AS SELECT 1")

            with When("I grant the drop view privilege"):
                node.query(f"GRANT DROP VIEW ON {view_name} TO {grant_target_name}")

            with And("I revoke ALL privilege"):
                node.query(f"REVOKE ALL ON *.* FROM {grant_target_name}")

            with Then("I attempt to drop a  view"):
                node.query(
                    f"DETACH VIEW {view_name}",
                    settings=[("user", user_name)],
                    exitcode=exitcode,
                    message=message,
                )

        finally:
            with Finally("I reattach the view as a table", flags=TE):
                node.query(f"ATTACH VIEW IF NOT EXISTS {view_name} AS SELECT 1")
            with And("I drop the view", flags=TE):
                node.query(f"DROP VIEW IF EXISTS {view_name}")

    with Scenario("user with ALL privilege"):
        view_name = f"view_{getuid()}"

        try:
            with Given("I have a view"):
                node.query(f"CREATE VIEW {view_name} AS SELECT 1")

            with When("I grant ALL privilege"):
                node.query(f"GRANT ALL ON *.* TO {grant_target_name}")

            with Then("I attempt to drop a view"):
                node.query(f"DETACH VIEW {view_name}", settings=[("user", user_name)])

        finally:
            with Finally("I reattach the view as a table", flags=TE):
                node.query(f"ATTACH VIEW IF NOT EXISTS {view_name} AS SELECT 1")
            with And("I drop the table", flags=TE):
                node.query(f"DROP VIEW IF EXISTS {view_name}")


@TestFeature
@Requirements(
    RQ_SRS_006_RBAC_Privileges_DetachView("1.0"),
    RQ_SRS_006_RBAC_Privileges_All("1.0"),
    RQ_SRS_006_RBAC_Privileges_None("1.0"),
)
@Name("detach view")
def feature(self, node="clickhouse1", stress=None, parallel=None):
    """Check the RBAC functionality of DETACH VIEW."""
    self.context.node = self.context.cluster.node(node)

    if parallel is not None:
        self.context.parallel = parallel
    if stress is not None:
        self.context.stress = stress

    with Suite(
        test=privilege_granted_directly_or_via_role,
        setup=instrument_clickhouse_server_log,
    ):
        privilege_granted_directly_or_via_role()
