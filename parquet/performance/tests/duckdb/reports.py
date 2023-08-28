import csv
import pandas as pd


def write_to_csv(filename, data, row_count, test_machine):
    """Generating a CSV file with performance results from the test run."""
    with open(filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)

        csv_writer.writerow(
            ["Number of rows:", row_count, "Test Environment:", test_machine]
        )
        csv_writer.writerow(
            [
                "Query",
                "ClickHouse version",
                "DuckDB version",
                "ClickHouse Query Runtime",
                "DuckDB Query Runtime",
                "ClickHouse Query Description",
                "DuckDB Query Description",
                "ClickHouse samples",
                "DuckDB samples",
            ]
        )

        for row in data:
            csv_writer.writerow(row)


def convert_to_markdown(csv_file, markdown_name, query):
    """Converting the CSV report of a Parquet performance test program into a markdown file."""
    data = pd.read_csv(csv_file, skiprows=1)

    with open(markdown_name, "w") as f:
        f.write("# ClickHouse vs DuckDB (Runtime in Seconds)\n\n")
        for index, row in data.iterrows():
            clickhouse_runtime = row["ClickHouse Query Runtime"]
            duckdb_runtime = row["DuckDB Query Runtime"]
            query_number = row["Query"]
            f.write(f"# {query_number}\n")
            f.write(f"```sql\n {query}\n```\n")
            f.write(
                f"""
```mermaid
     pie showData
         "ClickHouse" : {clickhouse_runtime}
         "DuckDB" : {duckdb_runtime}
```\n"""
            )
