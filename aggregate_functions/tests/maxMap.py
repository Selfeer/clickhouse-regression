from testflows.core import *

from aggregate_functions.requirements import (
    RQ_SRS_031_ClickHouse_AggregateFunctions_Specific_MaxMap,
)

from aggregate_functions.tests.steps import get_snapshot_id
from aggregate_functions.tests.sumMap import scenario as checks


@TestScenario
@Name("maxMap")
@Requirements(RQ_SRS_031_ClickHouse_AggregateFunctions_Specific_MaxMap("1.0"))
def scenario(self, func="maxMap({params})", table=None, snapshot_id=None):
    """Check maxMap aggregate function by using the same tests as for sumMap."""
    self.context.snapshot_id = get_snapshot_id(snapshot_id=snapshot_id)

    if "Merge" in self.name:
        return self.context.snapshot_id, func.replace("({params})", "")

    if table is None:
        table = self.context.table

    checks(func=func, table=table, snapshot_id=self.context.snapshot_id)
