from testflows.core import *
from selects.requirements import *
from selects.tests.steps import *


@TestScenario
def select_count(self, node=None):
    """Check select count() with `FINAL` clause equal to force_select_final select."""
    if node is None:
        node = current().context.node
    
    for table in self.context.tables:
        with Then(
            "I check that select with force_select_final equal 'SELECT...FINAL'"
        ):
            assert (
                # final modifier controls if FINAL is appended
                node.query(f"SELECT count() FROM {table_name} FINAL FORMAT JSONEachRow;").output.strip()
                == node.query(
                    f"SELECT count() FROM {table_name};",
                    settings=[("force_select_final", 1)],
                ).output.strip()
            )


@TestScenario
def select(self, node=None):
    """Check select all data with `FINAL` clause equal to force_select_final select."""
    if node is None:
        node = current().context.node

    for table in self.context.tables:
        with Then(
            "I check that select with force_select_final equal 'SELECT...FINAL'"
        ):
            # FIXME: FINAL must be conditional on final modifier being supported by the table
            assert (
                node.query(f"SELECT * FROM {table_name} FINAL;").output.strip()
                == node.query(
                    f"SELECT * FROM {table_name};", settings=[("force_select_final", 1)]
                ).output.strip()
            )


@TestFeature
@Name("final")
def feature(self):
    """Check FINAL modifier."""
    self.context.tables = []

    with Given("I have set of popualed tables"):
        create_and_populate_tables()

    for scenario in loads(current_module(), Scenario):
        scenario()
