from testflows.core import *

from aggregate_functions.requirements import (
    RQ_SRS_031_ClickHouse_AggregateFunctions_Standard_StddevPop,
)

from aggregate_functions.tests.steps import get_snapshot_id
from aggregate_functions.tests.avg import scenario as checks


@TestScenario
@Name("stddevPop")
@Requirements(RQ_SRS_031_ClickHouse_AggregateFunctions_Standard_StddevPop("1.0"))
def scenario(self, func="stddevPop({params})", table=None):
    """Check stddevPop aggregate function by using the same checks as for avg."""
    self.context.snapshot_id = get_snapshot_id()

    if table is None:
        table = self.context.table

    checks(func=func, table=table, decimal=False)
