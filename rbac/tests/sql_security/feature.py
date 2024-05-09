from testflows.core import *
from rbac.helper.common import *


@TestFeature
@Name("SQL security")
def feature(self):
    """Check SQL security feature."""
    Feature(run=load("rbac.tests.sql_security.materialized_view", "feature"))
    Feature(run=load("rbac.tests.sql_security.view", "feature"))
    #Feature(run=load("rbac.tests.sql_security.cluster", "feature"))
 

