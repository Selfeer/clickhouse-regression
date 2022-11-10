from testflows.core import *

from aggregate_functions.requirements import (
    RQ_SRS_031_ClickHouse_AggregateFunctions_Standard_VarSamp,
)

from aggregate_functions.tests.avg import feature as avg_feature


@TestFeature
@Name("varSamp")
@Requirements(RQ_SRS_031_ClickHouse_AggregateFunctions_Standard_VarSamp("1.0"))
def feature(self, func="varSamp({params})", table=None):
    """Check varSamp aggregate function by using the same checks as for avg."""
    self.context.snapshot_id = name.basename(current().name)

    if table is None:
        table = self.context.table

    avg_feature(func=func, table=table, exclude_types=["Decimal128(38)"])
