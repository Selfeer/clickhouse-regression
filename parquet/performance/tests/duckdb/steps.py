import time

from testflows.core import *
from testflows.asserts import snapshot, values, error
from helpers.common import getuid


@TestOutline
def run_query(self, name: str, clickhouse_query: str, duckdb_query: str, database: str):
    """Run the query on clickhouse and duckdb and collect the metrics of execution time for each.
    :param name: name of the query that is being run
    :param clickhouse_query: full query being run in ClickHouse
    :param duckdb_query: full query being run in DuckDB
    """

    clickhouse_node = self.context.clickhouse_node
    duckdb_node = self.context.duckdb_node
    duckdb_database = "db_" + getuid()
    repeats = self.context.run_count
    if database == "clickhouse":
        with By("running the query on clickhouse", description=f"{clickhouse_query}"):
            clickhouse_times = []
            for _ in range(repeats):
                start_time = time.time()
                query = clickhouse_node.query(clickhouse_query)
                clickhouse_run_time = time.time() - start_time
                clickhouse_times.append(clickhouse_run_time)
            metric(name="clickhouse-" + name, value=min(clickhouse_times), units="s")

            with values() as that:
                assert that(
                    snapshot(
                        query.output.strip(),
                        name=name
                        + "clickhouse"
                        + f"from_year_{self.context.from_year}"
                        + f"_to_year_{self.context.to_year}",
                    )
                ), error()

        csv_result = (
            name,
            self.context.clickhouse_version,
            min(clickhouse_times),
            clickhouse_query,
        )

        for i in range(repeats):
            csv_result += (clickhouse_times[i],)

        self.context.query_results.append(csv_result)

    elif database == "duckdb":
        with By("running the query on duckdb", description=f"{duckdb_query}"):
            duckdb_times = []
            for _ in range(repeats):
                start_time = time.time()
                query = duckdb_node.command(
                    f"duckdb {duckdb_database} '{duckdb_query}'", exitcode=0
                )
                duckdb_run_time = time.time() - start_time
                duckdb_times.append(duckdb_run_time)
            metric(name="duckdb-" + name, value=min(duckdb_times), units="s")

            with values() as that:
                assert that(
                    snapshot(
                        query.output.strip(),
                        name=name
                        + "duckdb"
                        + f"from_year_{self.context.from_year}"
                        + f"_to_year_{self.context.to_year}",
                    )
                ), error()

        csv_result = (
            name,
            self.context.duckdb_version,
            min(duckdb_times),
            duckdb_query,
        )

        for i in range(repeats):
            csv_result += (duckdb_times[i],)

        self.context.query_results.append(csv_result)


@TestScenario
def get_row_count(self, filename: str):
    """Calculating and uploading the row count of the parquet file into the CSV."""
    clickhouse_node = self.context.clickhouse_node

    with Given("I select the number of rows from the parquet file"):
        rows = clickhouse_node.query(f"SELECT count() FROM file({filename})")
    self.context.row_count.append(rows.output.strip())


@TestStep
def query_0(self, filename: str, database: str):
    """Calculating the average count of rows per group, where each group is defined by a combination of Year and
    Month values from the table."""

    clickhouse_query = f"SELECT avg(c1) FROM(SELECT Year, Month, count(*) AS c1 FROM file('{filename}') GROUP BY Year, Month ORDER BY Year ASC, Month ASC);"
    duckdb_query = f'SELECT avg(c1) FROM(SELECT Year, Month, count(*) AS c1 FROM "/data1/{filename}" GROUP BY Year, Month ORDER BY Year ASC, Month ASC);'

    run_query(
        clickhouse_query=clickhouse_query,
        duckdb_query=duckdb_query,
        name="query_0",
        database=database,
    )


@TestStep
def query_1(self, filename: str, database: str):
    """Get the number of flights per day from the year 2000 to 2008."""

    clickhouse_query = (
        f"SELECT DayOfWeek, count(*) AS c FROM file('{filename}') WHERE Year>=2000 AND Year<=2008 GROUP BY DayOfWeek ORDER "
        "BY c DESC;"
    )

    duckdb_query = f'SELECT DayOfWeek, count(*) AS c FROM "/data1/{filename}" WHERE Year>=2000 AND Year<=2008 GROUP BY DayOfWeek ORDER BY c DESC;'

    run_query(
        clickhouse_query=clickhouse_query,
        duckdb_query=duckdb_query,
        name="query_1",
        database=database,
    )


@TestStep
def query_2(self, filename: str, database: str):
    """Get the number of flights delayed by more than 10 minutes, grouped by the day of the week, for 2000-2008."""

    clickhouse_query = (
        f"SELECT DayOfWeek, count(*) AS c FROM file('{filename}') "
        f"WHERE Year>=2000 AND Year<=2008 GROUP BY DayOfWeek ORDER BY c DESC;"
    )
    duckdb_query = (
        f'SELECT DayOfWeek, COUNT(*) AS c FROM "/data1/{filename}" '
        f"WHERE Year >= 2000 AND Year <= 2008 GROUP BY DayOfWeek ORDER BY c DESC;"
    )

    run_query(
        clickhouse_query=clickhouse_query,
        duckdb_query=duckdb_query,
        name="query_2",
        database=database,
    )


@TestStep
def query_3(self, filename: str, database: str):
    """Get the number of delays by the airport for 2000-2008."""

    clickhouse_query = (
        f"SELECT Origin, count(*) AS c FROM file('{filename}') "
        f"WHERE DepDelay>10 AND Year>=2000 AND Year<=2008 GROUP BY Origin ORDER BY c DESC LIMIT 10;"
    )
    duckdb_query = (
        f'SELECT Origin, COUNT(*) AS c FROM "/data1/{filename}" '
        f"WHERE DepDelay > 10 AND Year >= 2000 AND Year <= 2008 GROUP BY Origin ORDER BY c DESC LIMIT 10;"
    )

    run_query(
        clickhouse_query=clickhouse_query,
        duckdb_query=duckdb_query,
        name="query_3",
        database=database,
    )


@TestStep
def query_4(self, filename: str, database: str):
    """Get the number of delays by carrier for 2007."""

    clickhouse_query = (
        f"SELECT IATA_CODE_Reporting_Airline AS Carrier, count(*) FROM file('{filename}') "
        f"WHERE DepDelay>10 AND Year=2007 GROUP BY Carrier ORDER BY count(*) DESC;"
    )
    duckdb_query = (
        f'SELECT IATA_CODE_Reporting_Airline AS Carrier, COUNT(*) AS count FROM "/data1/{filename}" '
        f"WHERE DepDelay > 10 AND Year = 2007 GROUP BY Carrier ORDER BY count DESC;"
    )

    run_query(
        clickhouse_query=clickhouse_query,
        duckdb_query=duckdb_query,
        name="query_4",
        database=database,
    )


@TestStep
def query_5(self, filename: str, database: str):
    """Get the percentage of delays by carrier for 2007."""

    clickhouse_query = (
        f"SELECT IATA_CODE_Reporting_Airline AS Carrier, avg(DepDelay>10)*100 AS c3 FROM file('{filename}') WHERE "
        f"Year=2007 GROUP BY Carrier ORDER BY c3 DESC"
    )
    duckdb_query = (
        f"SELECT IATA_CODE_Reporting_Airline AS Carrier, AVG(CAST(DepDelay > 10 AS DECIMAL) * 100) AS c3 "
        f'FROM "/data1/{filename}" WHERE Year = 2007 GROUP BY Carrier ORDER BY c3 DESC;'
    )

    run_query(
        clickhouse_query=clickhouse_query,
        duckdb_query=duckdb_query,
        name="query_5",
        database=database,
    )


@TestStep
def query_6(self, filename: str, database: str):
    """Get the percentage of delays by carrier for a broader range of years, 2000-2008."""

    clickhouse_query = (
        f"SELECT IATA_CODE_Reporting_Airline AS Carrier, avg(DepDelay>10)*100 AS c3 FROM file('{filename}') "
        f"WHERE Year>=2000 AND Year<=2008 GROUP BY Carrier ORDER BY c3 DESC;"
    )

    duckdb_query = (
        f"SELECT IATA_CODE_Reporting_Airline AS Carrier, AVG(CAST(DepDelay > 10 AS DECIMAL) * 100) AS c3 "
        f'FROM "/data1/{filename}" WHERE Year >= 2000 AND Year <= 2008 GROUP BY Carrier ORDER BY c3 DESC;'
    )

    run_query(
        clickhouse_query=clickhouse_query,
        duckdb_query=duckdb_query,
        name="query_6",
        database=database,
    )


@TestStep
def query_7(self, filename: str, database: str):
    """Get the percentage of flights delayed for more than 10 minutes, by year."""

    clickhouse_query = f"SELECT Year, avg(DepDelay>10)*100 FROM file('{filename}') GROUP BY Year ORDER BY Year;"
    duckdb_query = f'SELECT Year, AVG(CAST(DepDelay > 10 AS DECIMAL) * 100) FROM "/data1/{filename}" GROUP BY Year ORDER BY Year;'

    run_query(
        clickhouse_query=clickhouse_query,
        duckdb_query=duckdb_query,
        name="query_7",
        database=database,
    )


@TestStep
def query_8(self, filename: str, database: str):
    """Get the most popular destinations by the number of directly connected cities for various year ranges."""

    clickhouse_query = (
        f"SELECT DestCityName, uniqExact(OriginCityName) AS u FROM file('{filename}') "
        f"WHERE Year >= 2000 and Year <= 2010 GROUP BY DestCityName ORDER BY u DESC, DestCityName ASC LIMIT 10;"
    )
    duckdb_query = (
        f'SELECT DestCityName, COUNT(DISTINCT OriginCityName) AS u FROM "/data1/{filename}" WHERE Year >= '
        f"2000 AND Year <= 2010 GROUP BY DestCityName ORDER BY u DESC, DestCityName ASC LIMIT 10;;"
    )

    run_query(
        clickhouse_query=clickhouse_query,
        duckdb_query=duckdb_query,
        name="query_8",
        database=database,
    )


@TestStep
def query_9(self, filename: str, database: str):
    """Group the data by the Year column, and calculate the count of rows in each year."""
    clickhouse_query = f"SELECT Year, count(*) AS c1 FROM file('{filename}') GROUP BY Year ORDER BY Year ASC;"
    duckdb_query = f'SELECT Year, COUNT(*) AS c1 FROM "/data1/{filename}" GROUP BY Year ORDER BY Year ASC;'

    run_query(
        clickhouse_query=clickhouse_query,
        duckdb_query=duckdb_query,
        name="query_9",
        database=database,
    )


@TestSuite
def clickhouse(self, filename):
    duckdb_node = self.context.duckdb_node
    duckdb_node.stop()

    for step in loads(current_module(), Step):
        step(filename=filename, database="clickhouse")

    duckdb_node.start()


@TestScenario
def duckdb(self, filename):
    clickhouse_node = self.context.clickhouse_node
    clickhouse_node.stop()

    for step in loads(current_module(), Step):
        step(filename=filename, database="duckdb")

    clickhouse_node.start()


@TestScenario
def queries(self, filename):
    """Save number of rows of th parquet file into a CSV file and run the set of queries on ClickHouse and DuckDB."""
    Feature(run=get_row_count(filename=filename))
    Feature(test=clickhouse)(filename=filename)
    Feature(test=duckdb)(filename=filename)
