import os
from testflows import *
from testflows.core import *
from testflows.asserts import snapshot, values
from parquet.requirements import *
from helpers.common import *


@TestOutline
def import_export(self, snapshot_name, import_file):
    node = self.context.node
    table_name = "table_" + getuid()
    path_to_export = f"/var/lib/clickhouse/user_files/{table_name}.parquet"

    with And("I save file structure"):
        import_column_structure = node.query(f"DESCRIBE TABLE file('{import_file}')")

    with Check("import"):
        with When(f"I try to import the Parquet file into the table"):
            node.query(
                f"""
                CREATE TABLE {table_name}
                ENGINE = MergeTree
                ORDER BY tuple() AS SELECT * FROM file('{import_file}', Parquet)
                """
            )

        with And("I read the contents of the created table"):
            import_read = node.query(f"SELECT * FROM {table_name}")

        with Then("I check the output is correct"):
            with values() as that:
                assert that(
                    snapshot(
                        import_column_structure.output.strip(),
                        name=snapshot_name,
                    )
                ), error()

    with Check("export"):
        with When("I export the table back into a new parquet file"):
            node.query(
                f"SELECT * FROM {table_name} INTO OUTFILE '{path_to_export}' COMPRESSION 'none' FORMAT Parquet"
            )

        with And("I check the exported Parquet file's contents"):
            read = node.query(f"SELECT * FROM file('{path_to_export}', Parquet)")

        with Then("output must match the snapshot"):
            assert read.output.strip() == import_read.output.strip(), error()

        with And("I check that table structure matches ..."):
            export_columns_structure = node.query(
                f"DESCRIBE TABLE file('{path_to_export}')"
            )
            assert (
                import_column_structure.output.strip()
                == export_columns_structure.output.strip()
            ), error()


@TestScenario
@XFailed("Issue with datetime. Different number of on import and export")
@Requirements(
    RQ_SRS_032_ClickHouse_Parquet_Import_Encoding_Dictionary("1.0"),
    RQ_SRS_032_ClickHouse_Parquet_Export_Encoding_Dictionary("1.0"),
)
def dictionary(self):
    with Given("I have a Parquet file with the Dictionary encoding"):
        import_file = os.path.join("arrow", "alltypes_dictionary.parquet")

    import_export(snapshot_name="dictionary_structure", import_file=import_file)


@TestScenario
@XFailed("Issue with datetime. Different number of on import and export")
@Requirements(
    RQ_SRS_032_ClickHouse_Parquet_Import_Encoding_Plain("1.0"),
    RQ_SRS_032_ClickHouse_Parquet_Export_Encoding_Plain("1.0"),
)
def plain(self):
    with Given("I have a Parquet file with the Plain encoding"):
        import_file = os.path.join("arrow", "alltypes_plain.parquet")

    import_export(snapshot_name="plain_structure", import_file=import_file)


@TestFeature
@Name("encoding")
def feature(self, node="clickhouse1"):
    """Check importing and exporting Dictionary encoded parquet files."""
    self.context.node = self.context.cluster.node(node)

    for scenario in loads(current_module(), Scenario):
        scenario()
