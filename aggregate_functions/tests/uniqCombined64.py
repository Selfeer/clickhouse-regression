from testflows.core import *

from aggregate_functions.requirements import (
    RQ_SRS_031_ClickHouse_AggregateFunctions_Specific_UniqCombined64,
)

from aggregate_functions.tests.steps import get_snapshot_id, check_clickhouse_version
from aggregate_functions.tests.uniq import scenario as checks


@TestScenario
@Name("uniqCombined64")
@Requirements(RQ_SRS_031_ClickHouse_AggregateFunctions_Specific_UniqCombined64("1.0"))
def scenario(self, func="uniqCombined64({params})", table=None, snapshot_id=None):
    """Check uniqCombined64 aggregate function by using the same tests as for uniq."""

    clickhouse_version = (
        ">=23.2" if check_clickhouse_version("<23.12")(self) else ">=23.12"
    )
    self.context.snapshot_id = get_snapshot_id(
        snapshot_id=snapshot_id, clickhouse_version=clickhouse_version
    )

    if "Merge" in self.name:
        return self.context.snapshot_id, func.replace("({params})", "")

    if table is None:
        table = self.context.table

    checks(func=func, table=table, snapshot_id=self.context.snapshot_id)
