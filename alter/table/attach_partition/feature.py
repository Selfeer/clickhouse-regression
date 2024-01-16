from testflows.core import *

from alter.table.attach_partition.requirements.requirements import (
    SRS034_ClickHouse_Alter_Table_Attach_Partition,
)


@TestFeature
@Specifications(SRS034_ClickHouse_Alter_Table_Attach_Partition)
@Name("attach partition")
def feature(self):
    """Run features from the attach partition suite."""
    with Pool(2) as pool:
        Feature(
            run=load("alter.table.attach_partition.partition_types", "feature"),
            parallel=True,
            executor=pool,
        )
        Feature(
            run=load("alter.table.attach_partition.partition_key", "feature"),
            parallel=True,
            executor=pool,
        )
        Feature(
            run=load("alter.table.attach_partition.simple_test", "feature"),
            parallel=True,
            executor=pool,
        )
        Feature(
            run=load(
                "alter.table.attach_partition.corrupted_partitions",
                "feature",
            ),
            parallel=True,
            executor=pool,
        )
        Feature(
            run=load("alter.table.attach_partition.rbac", "feature"),
            parallel=True,
            executor=pool,
        )
        Feature(
            run=load("alter.table.attach_partition.conditions", "feature"),
            parallel=True,
            executor=pool,
        )
        Feature(
            run=load("alter.table.attach_partition.replicated_engines", "feature"),
            parallel=True,
            executor=pool,
        )
        Feature(
            run=load(
                "alter.table.attach_partition.miscellaneous",
                "feature",
            ),
            parallel=True,
            executor=pool,
        )
        join()
