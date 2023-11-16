from testflows.core import *

from aggregate_functions.requirements import (
    RQ_SRS_031_ClickHouse_AggregateFunctions_Standard_VarPop,
)

from aggregate_functions.tests.steps import get_snapshot_id
from aggregate_functions.tests.varPop import scenario as checks


@TestScenario
@Name("varPopStable")
@Requirements(RQ_SRS_031_ClickHouse_AggregateFunctions_Standard_VarPop("1.0"))
def scenario(self, func="varPopStable({params})", table=None, snapshot_id=None):
    """Check varPopStable aggregate function by using the same checks as for varPop."""
    self.context.snapshot_id = get_snapshot_id(snapshot_id=snapshot_id)

    if 'Merge' in self.name:
        return self.context.snapshot_id, func.replace("({params})", "")

    if table is None:
        table = self.context.table

    checks(func=func, table=table, snapshot_id=self.context.snapshot_id)
