import random

from testflows.core import *

from s3.tests.common import *
from s3.requirements import *


@TestFeature
@Name("setup")
def s3_create_many_files(self):
    """Create a folder with many folders and files in S3."""

    num_folders = 50_000
    start_offset = 0
    folder_size_mb = 0.5 if self.context.storage == "minio" else 4
    num_files_per_folder = 5

    node = current().context.node
    access_key_id = self.context.access_key_id
    secret_access_key = self.context.secret_access_key
    table_name = "table_" + getuid()
    random.seed("many_files")

    @TestStep(When)
    def insert_files(self, folder_id, iteration):
        node.query(
            f"""INSERT INTO TABLE FUNCTION 
            s3('{self.context.many_files_uri}id={folder_id}/file_{{_partition_id}}.csv','{access_key_id}','{secret_access_key}','CSV','d UInt64') 
            PARTITION BY (d % {num_files_per_folder}) SELECT * FROM {table_name} 
            -- {iteration}/{num_folders}"""
        )

    with Given("I have a table with data"):
        simple_table(node=node, name=table_name, policy="default")
        insert_data(node=node, number_of_mb=folder_size_mb, name=table_name)

    with Given("I have many folders with files in S3"):
        executor = Pool(100, thread_name_prefix="s3_insert")
        for j in range(num_folders):
            i = random.randint(100_000, 999_999)

            # skip ahead through random number generation
            if j < start_offset:
                continue

            By(test=insert_files, parallel=True, executor=executor)(
                folder_id=i, iteration=j
            )

        join()


@TestOutline(Scenario)
@Examples(
    "wildcard expected_time",
    [
        ("522029", 20, Name("one folder")),
        ("{759040,547776,167687,283359}", 60, Name("nums")),
        ("{759040,547776,167687,abc,283359}", 60, Name("nums one invalid")),
        ("1500*", 20, Name("star")),
        ("2500%3F%3F", 20, Name("question encoded")),
        ("3500??", 20, Name("question")),
        ("{45000..45099}", 120, Name("range")),
        ("{abc,efg,hij}", 10, Name("nums no match")),
        ("abc*", 1, Name("star no match")),
        ("abc??", 1, Name("question no match")),
        ("{0..10000}", 120, Name("range no match")),
    ],
)
@Requirements(RQ_SRS_015_S3_Performance_Glob("1.0"))
def wildcard(self, wildcard, expected_time):
    """Check the performance of using wildcards in s3 paths."""

    node = current().context.node
    access_key_id = self.context.access_key_id
    secret_access_key = self.context.secret_access_key

    for i in range(1, 3):
        with Then(f"""I query S3 using the wildcard '{wildcard}'"""):
            t_start = time.time()
            r = node.query(
                f"""SELECT median(d) FROM s3('{self.context.many_files_uri}id={wildcard}/*', '{access_key_id}','{secret_access_key}', 'CSV', 'd UInt64') FORMAT TabSeparated""",
                timeout=expected_time,
            )
            t_elapsed = time.time() - t_start
            metric(f"wildcard pattern='{wildcard}', i={i}", t_elapsed, "s")
            assert r.output.strip() != "", error()
            assert t_elapsed < expected_time, error()


@TestOutline(Feature)
@Requirements(RQ_SRS_015_S3_TableFunction("1.0"))
def outline(self):
    """Test S3 and S3 compatible storage through storage disks."""

    for scenario in loads(current_module(), Scenario):
        with allow_s3_truncate(self.context.node):
            scenario()


@TestFeature
@Requirements(RQ_SRS_015_S3_AWS_TableFunction("1.0"))
@Name("table function performance")
def aws_s3(self, uri, access_key, key_id, node="clickhouse1"):
    self.context.node = self.context.cluster.node(node)
    self.context.storage = "aws_s3"
    self.context.uri = uri
    self.context.access_key_id = key_id
    self.context.secret_access_key = access_key
    self.context.many_files_uri = self.context.uri + "many_files_benchmark/"

    # Scenario(run=s3_create_many_files)

    outline()


@TestFeature
@Requirements(RQ_SRS_015_S3_GCS_TableFunction("1.0"))
@Name("table function performance")
def gcs(self, uri, access_key, key_id, node="clickhouse1"):
    self.context.node = self.context.cluster.node(node)
    self.context.storage = "gcs"
    self.context.uri = uri
    self.context.access_key_id = key_id
    self.context.secret_access_key = access_key
    self.context.many_files_uri = self.context.uri + "many_files_benchmark/"

    # Scenario(run=s3_create_many_files)

    outline()


@TestFeature
@Requirements(RQ_SRS_015_S3_MinIO_TableFunction("1.0"))
@Name("table function performance")
def minio(self, uri, key, secret, node="clickhouse1"):
    self.context.node = self.context.cluster.node(node)
    self.context.storage = "minio"
    self.context.uri = uri
    self.context.access_key_id = key
    self.context.secret_access_key = secret
    self.context.many_files_uri = self.context.uri + "many_files_benchmark/"

    Scenario(run=s3_create_many_files)

    outline()
