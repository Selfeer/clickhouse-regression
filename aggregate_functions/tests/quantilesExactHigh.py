from testflows.core import *

from aggregate_functions.requirements import (
    RQ_SRS_031_ClickHouse_AggregateFunctions_Specific_QuantilesExactHigh,
)

from aggregate_functions.tests.steps import get_snapshot_id
from aggregate_functions.tests.quantileExactHigh import feature as checks


@TestFeature
@Name("quantilesExactHigh")
@Requirements(
    RQ_SRS_031_ClickHouse_AggregateFunctions_Specific_QuantilesExactHigh("1.0")
)
def feature(self, func="quantilesExactHigh({params})", table=None):
    """Check quantilesExactHigh aggregate function by using the same tests as for quantileExactHigh."""
    self.context.snapshot_id = get_snapshot_id()

    if table is None:
        table = self.context.table

    _func = func.replace(
        "({params})", f"(0.25, 0.5, 0.75, 0.9, 0.95, 0.99, 0.999)({{params}})"
    )
    checks(func=_func)
