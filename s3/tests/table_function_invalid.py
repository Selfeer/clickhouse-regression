from testflows.core import *

from s3.tests.common import *
from s3.requirements import *


@TestStep(Given)
def insert_to_s3_function_invalid(
    self,
    path,
    table_name,
    columns="d UInt64",
    compression=None,
    file_format="CSVWithNames",
    access_key_id=None,
    secret_access_key=None,
    message=None,
    exitcode=None,
):
    """Write a table to a file in s3. File will be overwritten from an empty table during cleanup."""

    access_key_id = access_key_id or self.context.access_key_id
    secret_access_key = secret_access_key or self.context.secret_access_key
    node = current().context.node

    query = f"INSERT INTO FUNCTION s3('{path}', '{access_key_id}','{secret_access_key}', '{file_format}', '{columns}'"

    if compression:
        query += f", '{compression}'"

    query += f") SELECT * FROM {table_name}"

    node.query(query, message=message, exitcode=exitcode)


@TestScenario
@Requirements(RQ_SRS_015_S3_TableFunction_Path("1.0"))
def empty_path(self):
    """Check that ClickHouse returns an error when the S3 table function path
    parameter is empty.
    """
    name = "table_" + getuid()
    node = current().context.node

    with Given("I create a table"):
        simple_table(node=node, name=name, policy="default")

    with And(f"I store simple data in the table"):
        node.query(f"INSERT INTO {name} VALUES (427)")

    with Then(
        """When I export the data to S3 using the table function with
                empty path parameter it should fail"""
    ):
        insert_to_s3_function_invalid(
            path="", message="DB::Exception: Host is empty in S3 URI", exitcode=36
        )


@TestScenario
@Requirements(RQ_SRS_015_S3_TableFunction_Path("1.0"))
def invalid_path(self):
    """Check that ClickHouse returns an error when the table function path
    parameter is invalid.
    """
    name = "table_" + getuid()
    node = current().context.node
    invalid_path = "https://invalid/path"

    with Given("I create a table"):
        simple_table(node=node, name=name, policy="default")

    with And(f"I store simple data in the table"):
        node.query(f"INSERT INTO {name} VALUES (427)")

    with Then(
        """When I export the data to S3 using the table function with
                invalid path parameter it should fail"""
    ):
        insert_to_s3_function_invalid(
            path=invalid_path,
            message="DB::Exception: Bucket or key name are invalid in S3 URI",
            exitcode=36,
        )


@TestOutline(Scenario)
@Examples(
    "invalid_format",
    [("", Name("empty string")), ("not_a_format", Name("unknown format"))],
)
@Requirements(RQ_SRS_015_S3_TableFunction_Format("1.0"))
def invalid_format(self, invalid_format):
    """Check that ClickHouse returns an error when the table function format
    parameter is invalid.
    """
    name = "table_" + getuid()
    uri = self.context.uri
    node = current().context.node

    with Given("I create a table"):
        simple_table(node=node, name=name, policy="default")

    with And(f"I store simple data in the table"):
        node.query(f"INSERT INTO {name} VALUES (427)")

    with Then(
        """When I export the data to S3 using the table function with
                invalid format parameter it should fail"""
    ):
        insert_to_s3_function_invalid(
            path=f"{uri}invalid.csv",
            file_format=invalid_format,
            message="DB::Exception: Unknown format",
            exitcode=36,
        )


@TestScenario
@Requirements(RQ_SRS_015_S3_TableFunction_Structure("1.0"))
def empty_structure(self):
    """Check that ClickHouse returns an error when the table function structure
    parameter is empty.
    """
    name = "table_" + getuid()
    uri = self.context.uri
    node = current().context.node

    with Given("I create a table"):
        simple_table(node=node, name=name, policy="default")

    with And(f"I store simple data in the table"):
        node.query(f"INSERT INTO {name} VALUES (427)")

    with Then(
        """When I export the data to S3 using the table function with
                empty structure parameter it should fail"""
    ):
        insert_to_s3_function_invalid(
            path=f"{uri}invalid.csv",
            columns="",
            message="DB::Exception: Empty query",
            exitcode=62,
        )


@TestScenario
@Requirements(RQ_SRS_015_S3_TableFunction_Structure("1.0"))
def invalid_structure(self):
    """Check that ClickHouse returns an error when the table function structure
    parameter is invalid.
    """
    name = "table_" + getuid()
    access_key_id = self.context.access_key_id
    secret_access_key = self.context.secret_access_key
    uri = self.context.uri
    node = current().context.node

    with Given("I create a table"):
        simple_table(node=node, name=name, policy="default")

    with And(f"I store simple data in the table"):
        node.query(f"INSERT INTO {name} VALUES (427)")

    with Then(
        """When I export the data to S3 using the table function with
                invalid structure parameter it should fail"""
    ):
        insert_to_s3_function_invalid(
            path=f"{uri}invalid.csv",
            columns="not_a_structure",
            message="DB::Exception: Syntax error",
            exitcode=62,
        )


@TestScenario
@Requirements(RQ_SRS_015_S3_TableFunction_Compression("1.0"))
def invalid_compression(self):
    """Check that ClickHouse returns an error when the table function compression
    parameter is invalid.
    """
    name = "table_" + getuid()
    access_key_id = self.context.access_key_id
    secret_access_key = self.context.secret_access_key
    uri = self.context.uri
    node = current().context.node

    with Given("I create a table"):
        simple_table(node=node, name=name, policy="default")

    with And(f"I store simple data in the table"):
        node.query(f"INSERT INTO {name} VALUES (427)")

    with Then(
        """When I export the data to S3 using the table function with
                invalid compression parameter it should fail"""
    ):
        insert_to_s3_function_invalid(
            path=f"{uri}invalid.csv",
            compression="invalid_compression",
            message="DB::Exception: Unknown compression method",
            exitcode=48,
        )


@TestScenario
@Requirements(RQ_SRS_015_S3_TableFunction_Credentials_Invalid("1.0"))
def invalid_credentials(self):
    """Check that ClickHouse throws an error when invalid bucket credentials
    are provided to the S3 table function.
    """
    name_table1 = "table_" + getuid()
    name_table2 = "table_" + getuid()
    access_key_id = "invalid_id"
    secret_access_key = "invalid_key"
    uri = self.context.uri
    node = current().context.node
    expected = "DB::Exception:"

    with Given("I create a table"):
        simple_table(node=node, name=name_table1, policy="default")

    with And("I create a second table for comparison"):
        simple_table(node=node, name=name_table2, policy="default")

    with And(f"I store simple data in the first table {name_table1}"):
        node.query(f"INSERT INTO {name_table1} VALUES (427)")

    with When(
        """I export the data to S3 using the table function with invalid
               credentials, expecting failure"""
    ):
        insert_to_s3_function_invalid(
            path=f"{uri}invalid.csv",
            access_key_id=access_key_id,
            secret_access_key=secret_access_key,
            message=expected,
            exitcode=243,
        )


@TestOutline(Feature)
@Requirements(RQ_SRS_015_S3_TableFunction("1.0"))
def outline(self):
    """Test S3 and S3 compatible storage through storage disks."""
    for scenario in loads(current_module(), Scenario):
        with allow_s3_truncate(self.context.node):
            scenario()


@TestFeature
@Requirements(RQ_SRS_015_S3_AWS_TableFunction("1.0"))
@Name("invalid table function")
def aws_s3(self, uri, access_key, key_id, node="clickhouse1"):
    self.context.node = self.context.cluster.node(node)
    self.context.storage = "aws_s3"
    self.context.uri = uri
    self.context.access_key_id = key_id
    self.context.secret_access_key = access_key

    outline()


@TestFeature
@Requirements(RQ_SRS_015_S3_GCS_TableFunction("1.0"))
@Name("invalid table function")
def gcs(self, uri, access_key, key_id, node="clickhouse1"):
    self.context.node = self.context.cluster.node(node)
    self.context.storage = "gcs"
    self.context.uri = uri
    self.context.access_key_id = key_id
    self.context.secret_access_key = access_key

    outline()


@TestFeature
@Requirements(RQ_SRS_015_S3_MinIO_TableFunction("1.0"))
@Name("invalid table function")
def minio(self, uri, key, secret, node="clickhouse1"):
    self.context.node = self.context.cluster.node(node)
    self.context.storage = "minio"
    self.context.uri = uri
    self.context.access_key_id = key
    self.context.secret_access_key = secret

    outline()
