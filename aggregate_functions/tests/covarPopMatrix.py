from testflows.core import *

from aggregate_functions.requirements import (
    RQ_SRS_031_ClickHouse_AggregateFunctions_Specific_CovarPopMatrix,
)

from aggregate_functions.tests.steps import get_snapshot_id, current_cpu
from aggregate_functions.tests.corrMatrix import scenario as checks


@TestScenario
@Name("covarPopMatrix")
@Requirements(RQ_SRS_031_ClickHouse_AggregateFunctions_Specific_CovarPopMatrix("1.0"))
def scenario(self, func="covarPopMatrix({params})", table=None, snapshot_id=None):
    """Check covarPopMatrix aggregate function by using the same checks as for corrMatrix."""
    self.context.snapshot_id = get_snapshot_id(snapshot_id=snapshot_id)

    if current_cpu() == "aarch64":
        self.context.snapshot_id = get_snapshot_id(
            snapshot_id=snapshot_id, clickhouse_version=">=24.3"
        )

    if "Merge" in self.name:
        return self.context.snapshot_id, func.replace("({params})", "")

    if table is None:
        table = self.context.table

    checks(func=func, table=table, snapshot_id=self.context.snapshot_id)
