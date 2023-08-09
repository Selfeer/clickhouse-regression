from testflows.core import *
from helpers.common import getuid
import time


@TestOutline
def outline(self, clickhouse_query: str, duckdb_query: str, step_name: str):
    clickhouse_node = self.context.clickhouse_node
    duckdb_node = self.context.duckdb_node
    duckdb_database = "db_" + getuid()

    clickhouse_start_time = time.time()
    clickhouse_node.query(clickhouse_query, use_file=True, file_output="tests")
    clickhouse_run_time = time.time() - clickhouse_start_time
    metric(name="ClickHouse: " + step_name, value=clickhouse_run_time, units="s")

    duckdb_start_time = time.time()
    duckdb_node.command(f"duckdb {duckdb_database} '{duckdb_query}'", exitcode=0)
    duckdb_run_time = time.time() - duckdb_start_time
    metric(name="DuckDB: " + step_name, value=duckdb_run_time, units="s")


@TestStep
def query_0(self, filename: str):
    """Calculating the average count of rows per group, where each group is defined by a combination of Year and
    Month values from the table."""

    r = "SELECT avg(c1) FROM(SELECT Year, Month, count(*) AS c1 FROM {filename} GROUP BY Year, Month);"

    clickhouse_query = r.format(filename=f"file({filename})")
    duckdb_query = r.format(filename=f'"/data1/{filename}"')

    outline(
        clickhouse_query=clickhouse_query,
        duckdb_query=duckdb_query,
        step_name="query_0",
    )


@TestStep
def query_1(self, filename: str):
    """Get the number of flights per day from the year 2000 to 2008."""

    query = "SELECT DayOfWeek, count(*) AS c FROM {filename} WHERE Year>=2000 AND Year<=2008 GROUP BY DayOfWeek ORDER BY c DESC;"

    clickhouse_query = query.format(filename=f"file({filename})")
    duckdb_query = query.format(filename=f'"/data1/{filename}"')

    outline(
        clickhouse_query=clickhouse_query,
        duckdb_query=duckdb_query,
        step_name="query_1",
    )


# @TestStep
# def query_2(self, filename: str, database: str = "clickhouse"):
#     """Get the number of flights delayed by more than 10 minutes, grouped by the day of the week, for 2000-2008."""
#
#     query = f"SELECT DayOfWeek, count(*) AS c FROM {filename} WHERE Year>=2000 AND Year<=2008 GROUP BY DayOfWeek ORDER BY c DESC;"
#     outline(query=query, step_name="query_2")
#
#
# @TestStep
# def query_3(self, filename: str, database: str = "clickhouse"):
#     """Get the number of delays by the airport for 2000-2008."""
#
#     query = f"SELECT Origin, count(*) AS c FROM {filename} WHERE DepDelay>10 AND Year>=2000 AND Year<=2008 GROUP BY Origin ORDER BY c DESC LIMIT 10;"
#     outline(query=query, step_name="query_3")
#
#
# @TestStep
# def query_4(self, filename: str, database: str = "clickhouse"):
#     """Get the number of delays by carrier for 2007."""
#
#     query = f"""SELECT IATA_CODE_Reporting_Airline AS Carrier, count(*) FROM {filename} WHERE DepDelay>10 AND
#     Year=2007 GROUP BY Carrier ORDER BY count(*) DESC;"""
#     outline(query=query, step_name="query_4")


# @TestStep
# def query_5(self, filename: str, database: str = "clickhouse"):
#     """Get the percentage of delays by carrier for 2007."""
#
#     query = (
#         f"SELECT IATA_CODE_Reporting_Airline AS Carrier, avg(DepDelay>10)*100 AS c3 FROM {filename} WHERE "
#         f"Year=2007 GROUP BY Carrier ORDER BY c3 DESC"
#     )
#
#     q = f"SELECT Carrier, c, c2, c*100/c2 as c3 FROM(SELECT IATA_CODE_Reporting_Airline AS Carrier, count(*) AS c FROM {filename} WHERE DepDelay>10 AND Year=2007 GROUP BY Carrier) q JOIN(SELECT IATA_CODE_Reporting_Airline AS Carrier, count(*) AS c2 FROM {filename} WHERE Year=2007 GROUP BY Carrier) qq USING Carrier ORDER BY c3 DESC;"
#     outline(query=q, database=database)
#
#
# @TestStep
# def query_6(self, filename: str, database: str = "clickhouse"):
#     """Get the percentage of delays by carrier for a broader range of years, 2000-2008."""
#
#     query = f"SELECT IATA_CODE_Reporting_Airline AS Carrier, avg(DepDelay>10)*100 AS c3 FROM {filename} WHERE Year>=2000 AND Year<=2008 GROUP BY Carrier ORDER BY c3 DESC;"
#
#     q = f"""SELECT Carrier, c, c2, c*100/c2 as c3 FROM(SELECT IATA_CODE_Reporting_Airline AS Carrier, count(*) AS c FROM {filename} WHERE DepDelay>10 AND Year>=2000 AND Year<=2008 GROUP BY Carrier) q JOIN(SELECT IATA_CODE_Reporting_Airline AS Carrier, count(*) AS c2 FROM {filename} WHERE Year>=2000 AND Year<=2008 GROUP BY Carrier) qq USING Carrier ORDER BY c3 DESC;"""
#
#     outline(query=q, database=database)
#
#
# @TestStep
# def query_7(self, filename: str, database: str = "clickhouse"):
#     """Get the percentage of flights delayed for more than 10 minutes, by year."""
#
#     query = f"SELECT Year, avg(DepDelay>10)*100 FROM {filename} GROUP BY Year ORDER BY Year;"
#     outline(query=query, database=database)
#
#
# @TestStep
# def query_8(self, filename: str, database: str = "clickhouse"):
#     """Get the most popular destinations by the number of directly connected cities for various year ranges."""
#
#     query = (
#         f"SELECT DestCityName, uniqExact(OriginCityName) AS u FROM {filename} "
#         f"WHERE Year >= 2000 and Year <= 2010 GROUP BY DestCityName ORDER BY u DESC LIMIT 10;"
#     )
#     outline(query=query, database=database)


# @TestStep
# def query_9(self, filename: str, database: str = "clickhouse"):
#     query = f"SELECT Year, count(*) AS c1 FROM {filename} GROUP BY Year;"
#     outline(query=query, step_name="query_9")


@TestScenario
def queries(self, filename):
    for step in loads(current_module(), Step):
        step(filename=filename)
