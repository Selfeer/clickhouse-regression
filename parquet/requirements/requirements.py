# These requirements were auto generated
# from software requirements specification (SRS)
# document by TestFlows v2.0.240111.1210833.
# Do not edit by hand but re-generate instead
# using 'tfs requirements generate' command.
from testflows.core import Specification
from testflows.core import Requirement

Heading = Specification.Heading

RQ_SRS_032_ClickHouse_Parquet = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=("[ClickHouse] SHALL support `Parquet` data format.\n" "\n"),
    link=None,
    level=2,
    num="4.1",
)

RQ_SRS_032_ClickHouse_Parquet_SupportedVersions = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.SupportedVersions",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing Parquet files with the following versions: `1.0.0`, `2.0.0`, `2.1.0`, `2.2.0`, `2.4.0`, `2.6.0`, `2.7.0`, `2.8.0`, `2.9.0`.\n"
        "\n"
    ),
    link=None,
    level=2,
    num="5.1",
)

RQ_SRS_032_ClickHouse_Parquet_ClickHouseLocal = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ClickHouseLocal",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support the usage of `clickhouse-local` with `Parquet` data format.\n"
        "\n"
    ),
    link=None,
    level=2,
    num="5.2",
)

RQ_SRS_032_ClickHouse_Parquet_Offsets = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Offsets",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing and exporting parquet files with offsets.\n"
        "\n"
    ),
    link=None,
    level=2,
    num="6.1",
)

RQ_SRS_032_ClickHouse_Parquet_Offsets_MonotonicallyIncreasing = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Offsets.MonotonicallyIncreasing",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing and exporting parquet files with monotonically increasing offsets.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="6.1.1",
)

RQ_SRS_032_ClickHouse_Parquet_Query_Cache = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Query.Cache",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support using the query cache functionality when working with the Parquet files.\n"
        "\n"
    ),
    link=None,
    level=2,
    num="7.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support using `INSERT` query with `FROM INFILE {file_name}` and `FORMAT Parquet` clauses to\n"
        "read data from Parquet files and insert data into tables or table functions.\n"
        "\n"
        "```sql\n"
        "INSERT INTO sometable\n"
        "FROM INFILE 'data.parquet' FORMAT Parquet;\n"
        "```\n"
        "\n"
    ),
    link=None,
    level=2,
    num="8.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_AutoDetectParquetFileFormat = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.AutoDetectParquetFileFormat",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support automatically detecting Parquet file format based on \n"
        "when using INFILE clause without explicitly specifying the format setting.\n"
        "\n"
        "```sql\n"
        "INSERT INTO sometable\n"
        "FROM INFILE 'data.parquet';\n"
        "```\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.2.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_Glob = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.Glob",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support using glob patterns in file paths to import multiple Parquet files.\n"
        "\n"
        "> Multiple path components can have globs. For being processed file must exist and match to the whole path pattern (not only suffix or prefix).\n"
        ">\n"
        ">   - `*` — Substitutes any number of any characters except / including empty string.\n"
        ">   - `?` — Substitutes any single character.\n"
        ">   - `{some_string,another_string,yet_another_one}` — Substitutes any of strings 'some_string', 'another_string', 'yet_another_one'.\n"
        ">   - `{N..M}` — Substitutes any number in range from N to M including both borders.\n"
        ">   - `**` - Fetches all files inside the folder recursively.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.3.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_Glob_MultiDirectory = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.Glob.MultiDirectory",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support using `{str1, ...}` globs across different directories when importing from the Parquet files. \n"
        "\n"
        "For example,\n"
        "\n"
        "> The following query will import both from a/1.parquet and b/2.parquet\n"
        "> \n"
        "> ```sql\n"
        "> SELECT\n"
        ">     *,\n"
        ">     _path,\n"
        ">     _file\n"
        "> FROM file('{a/1,b/2}.parquet', Parquet)\n"
        "> ```\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.3.2",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Conversion = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Conversion",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing the Parquet files with the following datatypes and converting them into corresponding ClickHouse columns as described in the table.\n"
        "\n"
        "The conversion MAY not be possible between some datatypes.\n"
        ">\n"
        "> For example,\n"
        ">\n"
        "> `Bool` -> `IPv6`\n"
        "\n"
        "| Parquet to ClickHouse supported Datatypes     | ClickHouse Datatype Family        | alias_to Datatype | case_insensitive |\n"
        "|-----------------------------------------------|-----------------------------------|-------------------|------------------|\n"
        "|                                               | `JSON`                            |                   | 1                |\n"
        "|                                               | `Polygon`                         |                   | 0                |\n"
        "|                                               | `Ring`                            |                   | 0                |\n"
        "|                                               | `Point`                           |                   | 0                |\n"
        "|                                               | `SimpleAggregateFunction`         |                   | 0                |\n"
        "|                                               | `IntervalQuarter`                 |                   | 0                |\n"
        "|                                               | `IntervalMonth`                   |                   | 0                |\n"
        "| `INT64`                                       | `Int64`                           |                   | 0                |\n"
        "|                                               | `IntervalDay`                     |                   | 0                |\n"
        "|                                               | `IntervalHour`                    |                   | 0                |\n"
        "| `UINT32`                                      | `IPv4`                            |                   | 0                |\n"
        "|                                               | `IntervalSecond`                  |                   | 0                |\n"
        "|                                               | `LowCardinality`                  |                   | 0                |\n"
        "| `INT16`                                       | `Int16`                           |                   | 0                |\n"
        "| `FIXED_LENGTH_BYTE_ARRAY`, `BINARY`           | `UInt256`                         |                   | 0                |\n"
        "|                                               | `AggregateFunction`               |                   | 0                |\n"
        "|                                               | `MultiPolygon`                    |                   | 0                |\n"
        "| `FIXED_LENGTH_BYTE_ARRAY`, `BINARY`           | `IPv6`                            |                   | 0                |\n"
        "|                                               | `Nothing`                         |                   | 0                |\n"
        "|                                               | `Decimal256`                      |                   | 1                |\n"
        "| `STRUCT`                                      | `Tuple`                           |                   | 0                |\n"
        "| `LIST`                                        | `Array`                           |                   | 0                |\n"
        "|                                               | `IntervalMicrosecond`             |                   | 0                |\n"
        "|                                               | `Bool`                            |                   | 1                |\n"
        "| `INT16`                                       | `Enum16`                          |                   | 0                |\n"
        "|                                               | `IntervalMinute`                  |                   | 0                |\n"
        "|                                               | `FixedString`                     |                   | 0                |\n"
        "| `STRING`, `BINARY`                            | `String`                          |                   | 0                |\n"
        "| `TIME (ms)`                                   | `DateTime`                        |                   | 1                |\n"
        "|                                               | `Object`                          |                   | 0                |\n"
        "| `MAP`                                         | `Map`                             |                   | 0                |\n"
        "|                                               | `UUID`                            |                   | 0                |\n"
        "|                                               | `Decimal64`                       |                   | 1                |\n"
        "|                                               | `Nullable`                        |                   | 0                |\n"
        "|                                               | `Enum`                            |                   | 1                |\n"
        "| `INT32`                                       | `Int32`                           |                   | 0                |\n"
        "| `UINT8`, `BOOL`                               | `UInt8`                           |                   | 0                |\n"
        "|                                               | `Date`                            |                   | 1                |\n"
        "|                                               | `Decimal32`                       |                   | 1                |\n"
        "| `FIXED_LENGTH_BYTE_ARRAY`, `BINARY`           | `UInt128`                         |                   | 0                |\n"
        "| `DOUBLE`                                      | `Float64`                         |                   | 0                |\n"
        "|                                               | `Nested`                          |                   | 0                |\n"
        "| `UINT16`                                      | `UInt16`                          |                   | 0                |\n"
        "|                                               | `IntervalMillisecond`             |                   | 0                |\n"
        "| `FIXED_LENGTH_BYTE_ARRAY`, `BINARY`           | `Int128`                          |                   | 0                |\n"
        "|                                               | `Decimal128`                      |                   | 1                |\n"
        "| `INT8`                                        | `Int8`                            |                   | 0                |\n"
        "| `DECIMAL`                                     | `Decimal`                         |                   | 1                |\n"
        "| `FIXED_LENGTH_BYTE_ARRAY`, `BINARY`           | `Int256`                          |                   | 0                |\n"
        "| `TIMESTAMP (ms, ns, us)`, `TIME (us, ns)`     | `DateTime64`                      |                   | 1                |\n"
        "| `INT8`                                        | `Enum8`                           |                   | 0                |\n"
        "|                                               | `DateTime32`                      |                   | 1                |\n"
        "| `DATE (ms, ns, us)`                           | `Date32`                          |                   | 1                |\n"
        "|                                               | `IntervalWeek`                    |                   | 0                |\n"
        "| `UINT64`                                      | `UInt64`                          |                   | 0                |\n"
        "|                                               | `IntervalNanosecond`              |                   | 0                |\n"
        "|                                               | `IntervalYear`                    |                   | 0                |\n"
        "| `UINT32`                                      | `UInt32`                          |                   | 0                |\n"
        "| `FLOAT`                                       | `Float32`                         |                   | 0                |\n"
        "| `BOOL`                                        | `bool`                            | `Bool`            | 1                |\n"
        "| `FIXED_LENGTH_BYTE_ARRAY`, `BINARY`           | `INET6`                           | `IPv6`            | 1                |\n"
        "| `UINT32`                                      | `INET4`                           | `IPv4`            | 1                |\n"
        "|                                               | `ENUM`                            | `Enum`            | 1                |\n"
        "| `STRING`, `BINARY`, `FIXED_LENGTH_BYTE_ARRAY` | `BINARY`                          | `FixedString`     | 1                |\n"
        "| `STRING`, `BINARY`                            | `GEOMETRY`                        | `String`          | 1                |\n"
        "| `STRING`, `BINARY`                            | `NATIONAL CHAR VARYING`           | `String`          | 1                |\n"
        "| `STRING`, `BINARY`                            | `BINARY VARYING`                  | `String`          | 1                |\n"
        "| `STRING`, `BINARY`                            | `NCHAR LARGE OBJECT`              | `String`          | 1                |\n"
        "| `STRING`, `BINARY`                            | `NATIONAL CHARACTER VARYING`      | `String`          | 1                |\n"
        "|                                               | `boolean`                         | `Bool`            | 1                |\n"
        "| `STRING`, `BINARY`                            | `NATIONAL CHARACTER LARGE OBJECT` | `String`          | 1                |\n"
        "| `STRING`, `BINARY`                            | `NATIONAL CHARACTER`              | `String`          | 1                |\n"
        "| `STRING`, `BINARY`                            | `NATIONAL CHAR`                   | `String`          | 1                |\n"
        "| `STRING`, `BINARY`                            | `CHARACTER VARYING`               | `String`          | 1                |\n"
        "| `STRING`, `BINARY`                            | `LONGBLOB`                        | `String`          | 1                |\n"
        "| `STRING`, `BINARY`                            | `TINYBLOB`                        | `String`          | 1                |\n"
        "| `STRING`, `BINARY`                            | `MEDIUMTEXT`                      | `String`          | 1                |\n"
        "| `STRING`, `BINARY`                            | `TEXT`                            | `String`          | 1                |\n"
        "| `STRING`, `BINARY`                            | `VARCHAR2`                        | `String`          | 1                |\n"
        "| `STRING`, `BINARY`                            | `CHARACTER LARGE OBJECT`          | `String`          | 1                |\n"
        "| `DOUBLE`                                      | `DOUBLE PRECISION`                | `Float64`         | 1                |\n"
        "| `STRING`, `BINARY`                            | `LONGTEXT`                        | `String`          | 1                |\n"
        "| `STRING`, `BINARY`                            | `NVARCHAR`                        | `String`          | 1                |\n"
        "|                                               | `INT1 UNSIGNED`                   | `UInt8`           | 1                |\n"
        "| `STRING`, `BINARY`                            | `VARCHAR`                         | `String`          | 1                |\n"
        "| `STRING`, `BINARY`                            | `CHAR VARYING`                    | `String`          | 1                |\n"
        "| `STRING`, `BINARY`                            | `MEDIUMBLOB`                      | `String`          | 1                |\n"
        "| `STRING`, `BINARY`                            | `NCHAR`                           | `String`          | 1                |\n"
        "| `STRING`, `BINARY`                            | `VARBINARY`                       | `String`          | 1                |\n"
        "| `STRING`, `BINARY`                            | `CHAR`                            | `String`          | 1                |\n"
        "| `UINT16`                                      | `SMALLINT UNSIGNED`               | `UInt16`          | 1                |\n"
        "| `TIME (ms)`                                   | `TIMESTAMP`                       | `DateTime`        | 1                |\n"
        "| `DECIMAL`                                     | `FIXED`                           | `Decimal`         | 1                |\n"
        "| `STRING`, `BINARY`                            | `TINYTEXT`                        | `String`          | 1                |\n"
        "| `DECIMAL`                                     | `NUMERIC`                         | `Decimal`         | 1                |\n"
        "| `DECIMAL`                                     | `DEC`                             | `Decimal`         | 1                |\n"
        "| `INT64`                                       | `TIME`                            | `Int64`           | 1                |\n"
        "| `FLOAT`                                       | `FLOAT`                           | `Float32`         | 1                |\n"
        "| `UINT64`                                      | `SET`                             | `UInt64`          | 1                |\n"
        "|                                               | `TINYINT UNSIGNED`                | `UInt8`           | 1                |\n"
        "| `UINT32`                                      | `INTEGER UNSIGNED`                | `UInt32`          | 1                |\n"
        "| `UINT32`                                      | `INT UNSIGNED`                    | `UInt32`          | 1                |\n"
        "| `STRING`, `BINARY`                            | `CLOB`                            | `String`          | 1                |\n"
        "| `UINT32`                                      | `MEDIUMINT UNSIGNED`              | `UInt32`          | 1                |\n"
        "| `STRING`, `BINARY`                            | `BLOB`                            | `String`          | 1                |\n"
        "| `FLOAT`                                       | `REAL`                            | `Float32`         | 1                |\n"
        "|                                               | `SMALLINT`                        | `Int16`           | 1                |\n"
        "| `INT32`                                       | `INTEGER SIGNED`                  | `Int32`           | 1                |\n"
        "| `STRING`, `BINARY`                            | `NCHAR VARYING`                   | `String`          | 1                |\n"
        "| `INT32`                                       | `INT SIGNED`                      | `Int32`           | 1                |\n"
        "|                                               | `TINYINT SIGNED`                  | `Int8`            | 1                |\n"
        "| `INT64`                                       | `BIGINT SIGNED`                   | `Int64`           | 1                |\n"
        "| `STRING`, `BINARY`                            | `BINARY LARGE OBJECT`             | `String`          | 1                |\n"
        "|                                               | `SMALLINT SIGNED`                 | `Int16`           | 1                |\n"
        "|                                               | `YEAR`                            | `UInt16`          | 1                |\n"
        "| `INT32`                                       | `MEDIUMINT`                       | `Int32`           | 1                |\n"
        "| `INT32`                                       | `INTEGER`                         | `Int32`           | 1                |\n"
        "|                                               | `INT1 SIGNED`                     | `Int8`            | 1                |\n"
        "| `UINT64`                                      | `BIT`                             | `UInt64`          | 1                |\n"
        "| `UINT64`                                      | `BIGINT UNSIGNED`                 | `UInt64`          | 1                |\n"
        "| `STRING`, `BINARY`                            | `BYTEA`                           | `String`          | 1                |\n"
        "| `INT32`                                       | `INT`                             | `Int32`           | 1                |\n"
        "| `FLOAT`                                       | `SINGLE`                          | `Float32`         | 1                |\n"
        "| `INT32`                                       | `MEDIUMINT SIGNED`                | `Int32`           | 1                |\n"
        "| `DOUBLE`                                      | `DOUBLE`                          | `Float64`         | 1                |\n"
        "|                                               | `INT1`                            | `Int8`            | 1                |\n"
        "| `STRING`, `BINARY`                            | `CHAR LARGE OBJECT`               | `String`          | 1                |\n"
        "|                                               | `TINYINT`                         | `Int8`            | 1                |\n"
        "| `INT64`                                       | `BIGINT`                          | `Int64`           | 1                |\n"
        "| `STRING`, `BINARY`                            | `CHARACTER`                       | `String`          | 1                |\n"
        "|                                               | `BYTE`                            | `Int8`            | 1                |\n"
        "\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.4.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing the following Parquet data types:\n"
        "\n"
        "| Parquet data type                             | ClickHouse data type                  |\n"
        "|-----------------------------------------------|---------------------------------------|\n"
        "| `BOOL`                                        | `Bool`                                |\n"
        "| `UINT8`, `BOOL`                               | `UInt8`                               |\n"
        "| `INT8`                                        | `Int8`/`Enum8`                        |\n"
        "| `UINT16`                                      | `UInt16`                              |\n"
        "| `INT16`                                       | `Int16`/`Enum16`                      |\n"
        "| `UINT32`                                      | `UInt32`                              |\n"
        "| `INT32`                                       | `Int32`                               |\n"
        "| `UINT64`                                      | `UInt64`                              |\n"
        "| `INT64`                                       | `Int64`                               |\n"
        "| `FLOAT`                                       | `Float32`                             |\n"
        "| `DOUBLE`                                      | `Float64`                             |\n"
        "| `DATE (ms, ns, us)`                           | `Date32`                              |\n"
        "| `TIME (ms)`                                   | `DateTime`                            |\n"
        "| `TIMESTAMP (ms, ns, us)`, `TIME (us, ns)`     | `DateTime64`                          |\n"
        "| `STRING`, `BINARY`                            | `String`                              |\n"
        "| `STRING`, `BINARY`, `FIXED_LENGTH_BYTE_ARRAY` | `FixedString`                         |\n"
        "| `DECIMAL`                                     | `Decimal`                             |\n"
        "| `LIST`                                        | `Array`                               |\n"
        "| `STRUCT`                                      | `Tuple`                               |\n"
        "| `MAP`                                         | `Map`                                 |\n"
        "| `UINT32`                                      | `IPv4`                                |\n"
        "| `FIXED_LENGTH_BYTE_ARRAY`, `BINARY`           | `IPv6`                                |\n"
        "| `FIXED_LENGTH_BYTE_ARRAY`, `BINARY`           | `Int128`/`UInt128`/`Int256`/`UInt256` |\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.4.2",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_BLOB = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.BLOB",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing parquet files with `BLOB` content.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.3",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_BOOL = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.BOOL",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `BOOL` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.4",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_UINT8 = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.UINT8",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `UINT8` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.5",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_INT8 = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.INT8",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `INT8` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.6",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_UINT16 = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.UINT16",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `UINT16` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.7",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_INT16 = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.INT16",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `INT16` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.8",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_UINT32 = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.UINT32",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `UINT32` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.9",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_INT32 = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.INT32",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `INT32` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.10",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_UINT64 = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.UINT64",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `UINT64` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.11",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_INT64 = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.INT64",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `INT64` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.12",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_FLOAT = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.FLOAT",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `FLOAT` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.13",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_DOUBLE = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DOUBLE",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `DOUBLE` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.14",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_DATE = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DATE",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `DATE` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.15",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_DATE_ms = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DATE.ms",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `DATE (ms)` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.16",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_DATE_ns = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DATE.ns",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `DATE (ns)` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.17",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_DATE_us = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DATE.us",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `DATE (us)` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.18",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_TIME_ms = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.TIME.ms",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `TIME (ms)` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.19",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_TIMESTAMP_ms = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.TIMESTAMP.ms",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `TIMESTAMP (ms)` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.20",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_TIMESTAMP_ns = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.TIMESTAMP.ns",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `TIMESTAMP (ns)` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.21",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_TIMESTAMP_us = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.TIMESTAMP.us",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `TIMESTAMP (us)` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.22",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_STRING = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.STRING",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `STRING` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.23",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_BINARY = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.BINARY",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `BINARY` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.24",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_FixedLengthByteArray = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.FixedLengthByteArray",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `FIXED_LENGTH_BYTE_ARRAY` Parquet datatype.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.4.25",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_DECIMAL = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DECIMAL",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `DECIMAL` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.26",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_DECIMAL_Filter = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DECIMAL.Filter",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `DECIMAL` Parquet datatype with specified filters.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.4.27",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_LIST = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.LIST",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `LIST` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.28",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_ARRAY = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.ARRAY",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `ARRAY` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.29",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_STRUCT = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.STRUCT",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `STRUCT` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="8.4.30",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_MAP = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.MAP",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=("[ClickHouse] SHALL support importing `MAP` Parquet datatype.\n" "\n"),
    link=None,
    level=3,
    num="8.4.31",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_DateUTCAdjusted = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.DateUTCAdjusted",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `DATE` Parquet datatype with `isAdjustedToUTC = true`.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="8.4.32.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_TimestampUTCAdjusted = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.TimestampUTCAdjusted",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `TIMESTAMP` Parquet datatype with `isAdjustedToUTC = true`.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="8.4.32.2",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_TimeUTCAdjusted = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.TimeUTCAdjusted",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `TIME` Parquet datatype with `isAdjustedToUTC = true`.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="8.4.32.3",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_NullValues = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.NullValues",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing columns that have `Null` values in Parquet files. If the target [ClickHouse] column is not `Nullable` then the `Null` value should be converted to the default values for the target column datatype.\n"
        "\n"
        "For example, if the target column has `Int32`, then the `Null` value will be replaced with `0`.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="8.4.33.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_ImportInto_Nullable = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.ImportInto.Nullable",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing Parquet files into target table's `Nullable` datatype columns.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="8.4.33.2",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_ImportInto_LowCardinality = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.ImportInto.LowCardinality",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing Parquet files into target table's `LowCardinality` datatype columns.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="8.4.34.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_ImportInto_Nested = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.ImportInto.Nested",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing Parquet files into target table's `Nested` datatype columns.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="8.4.35.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_ImportInto_Unknown = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.ImportInto.Unknown",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing Parquet files with `UNKNOWN` logical type.\n"
        "\n"
        "The example as to why the Parquet might have an `UNKNOWN` types is as follows,\n"
        "\n"
        "> Sometimes, when discovering the schema of existing data, values are always null and there's no type information. \n"
        "> The UNKNOWN type can be used to annotate a column that is always null. (Similar to Null type in Avro and Arrow)\n"
        "\n"
    ),
    link=None,
    level=4,
    num="8.4.36.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Unsupported = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Unsupported",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] MAY not support the following Parquet types:\n"
        "\n"
        "- `Time32`\n"
        "- `Fixed_Size_Binary`\n"
        "- `JSON`\n"
        "- `UUID`\n"
        "- `ENUM`\n"
        "- `Null`\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.5.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Unsupported_ChunkedArray = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Unsupported.ChunkedArray",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=("[ClickHouse] MAY not support Parquet chunked arrays.\n" "\n"),
    link=None,
    level=3,
    num="8.5.2",
)

RQ_SRS_032_ClickHouse_Parquet_Import_FilterPushdown = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.FilterPushdown",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] MAY support filter pushdown functionality when importing from the Parquet files.\n"
        "\n"
        "> The functionality should behave similar to https://drill.apache.org/docs/parquet-filter-pushdown/\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.6.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_Projections = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.Projections",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support inserting parquet data into a table that has a projection on it.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.7.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_SkipColumns = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.SkipColumns",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support skipping unexistent columns when importing from Parquet files.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.8.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_SkipValues = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.SkipValues",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support skipping unsupported values when import from Parquet files. When the values are being skipped, the inserted values SHALL be the default value for the corresponding column's datatype.\n"
        "\n"
        "For example, trying to insert `Null` values into the non-`Nullable` column.\n"
        "\n"
        "```sql\n"
        "CREATE TABLE TestTable\n"
        "(\n"
        "    `path` String,\n"
        "    `date` Date,\n"
        "    `hits` UInt32\n"
        ")\n"
        "ENGINE = MergeTree\n"
        "ORDER BY (date, path);\n"
        "\n"
        "SELECT *\n"
        "FROM file(output.parquet);\n"
        "\n"
        "┌─path───┬─date───────┬─hits─┐\n"
        "│ /path1 │ 2021-06-01 │   10 │\n"
        "│ /path2 │ 2021-06-02 │    5 │\n"
        "│ ᴺᵁᴸᴸ   │ 2021-06-03 │    8 │\n"
        "└────────┴────────────┴──────┘\n"
        "\n"
        "INSERT INTO TestTable\n"
        "FROM INFILE 'output.parquet' FORMAT Parquet;\n"
        "\n"
        "SELECT *\n"
        "FROM TestTable;\n"
        "\n"
        "┌─path───┬───────date─┬─hits─┐\n"
        "│ /path1 │ 2021-06-01 │   10 │\n"
        "│ /path2 │ 2021-06-02 │    5 │\n"
        "│        │ 2021-06-03 │    8 │\n"
        "└────────┴────────────┴──────┘\n"
        "```\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.9.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_AutoTypecast = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.AutoTypecast",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL automatically typecast parquet datatype based on the types in the target table.\n"
        "\n"
        "For example,\n"
        "\n"
        "> When we take the following Parquet file:\n"
        "> \n"
        "> ```\n"
        "> ┌─path────────────────────────────────────────────────────────────┬─date───────┬──hits─┐\n"
        "> │ Akiba_Hebrew_Academy                                            │ 2017-08-01 │   241 │\n"
        "> │ 1980_Rugby_League_State_of_Origin_match                         │ 2017-07-01 │     2 │\n"
        "> │ Column_of_Santa_Felicita,_Florence                              │ 2017-06-01 │    14 │\n"
        "> └─────────────────────────────────────────────────────────────────┴────────────┴───────┘\n"
        "> ```\n"
        "> \n"
        "> ```\n"
        "> ┌─name─┬─type─────────────┬─default_type─┬─default_expression─┬─comment─┬─codec_expression─┬─ttl_expression─┐\n"
        "> │ path │ Nullable(String) │              │                    │         │                  │                │\n"
        "> │ date │ Nullable(String) │              │                    │         │                  │                │\n"
        "> │ hits │ Nullable(Int64)  │              │                    │         │                  │                │\n"
        "> └──────┴──────────────────┴──────────────┴────────────────────┴─────────┴──────────────────┴────────────────┘\n"
        "> ```\n"
        "> \n"
        "> \n"
        "> Then create a table to import parquet data to:\n"
        "> ```sql\n"
        "> CREATE TABLE sometable\n"
        "> (\n"
        ">     `path` String,\n"
        ">     `date` Date,\n"
        ">     `hits` UInt32\n"
        "> )\n"
        "> ENGINE = MergeTree\n"
        "> ORDER BY (date, path)\n"
        "> ```\n"
        "> \n"
        "> Then import data using a FROM INFILE clause:\n"
        "> \n"
        "> \n"
        "> ```sql\n"
        "> INSERT INTO sometable\n"
        "> FROM INFILE 'data.parquet' FORMAT Parquet;\n"
        "> ```\n"
        "> \n"
        "> As a result ClickHouse automatically converted parquet `strings` (in the `date` column) to the `Date` type.\n"
        "> \n"
        "> \n"
        "> ```sql\n"
        "> DESCRIBE TABLE sometable\n"
        "> ```\n"
        "> \n"
        "> ```\n"
        "> ┌─name─┬─type───┬─default_type─┬─default_expression─┬─comment─┬─codec_expression─┬─ttl_expression─┐\n"
        "> │ path │ String │              │                    │         │                  │                │\n"
        "> │ date │ Date   │              │                    │         │                  │                │\n"
        "> │ hits │ UInt32 │              │                    │         │                  │                │\n"
        "> └──────┴────────┴──────────────┴────────────────────┴─────────┴──────────────────┴────────────────┘\n"
        "> ```\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.10.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_RowGroupSize = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.RowGroupSize",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing Parquet files with different Row Group Sizes.\n"
        "\n"
        "As described in https://parquet.apache.org/docs/file-format/configurations/#row-group-size,\n"
        "\n"
        "> We recommend large row groups (512MB - 1GB). Since an entire row group might need to be read, \n"
        "> we want it to completely fit on one HDFS block.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.11.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_DataPageSize = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.DataPageSize",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing Parquet files with different Data Page Sizes.\n"
        "\n"
        "As described in https://parquet.apache.org/docs/file-format/configurations/#data-page--size,\n"
        "\n"
        "> Note: for sequential scans, it is not expected to read a page at a time; this is not the IO chunk. We recommend 8KB for page sizes.\n"
        "\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.12.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_NewTable = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.NewTable",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support creating and populating tables directly from the Parquet files with table schema being auto-detected\n"
        "from file's structure.\n"
        "\n"
        "For example,\n"
        "\n"
        "> Since ClickHouse reads parquet file schema, we can create tables on the fly:\n"
        "> \n"
        "> ```sql\n"
        "> CREATE TABLE imported_from_parquet\n"
        "> ENGINE = MergeTree\n"
        "> ORDER BY tuple() AS\n"
        "> SELECT *\n"
        "> FROM file('data.parquet', Parquet)\n"
        "> ```\n"
        "> \n"
        "> This will automatically create and populate a table from a given parquet file:\n"
        "> \n"
        "> ```sql\n"
        "> DESCRIBE TABLE imported_from_parquet;\n"
        "> ```\n"
        "> ```\n"
        "> ┌─name─┬─type─────────────┬─default_type─┬─default_expression─┬─comment─┬─codec_expression─┬─ttl_expression─┐\n"
        "> │ path │ Nullable(String) │              │                    │         │                  │                │\n"
        "> │ date │ Nullable(String) │              │                    │         │                  │                │\n"
        "> │ hits │ Nullable(Int64)  │              │                    │         │                  │                │\n"
        "> └──────┴──────────────────┴──────────────┴────────────────────┴─────────┴──────────────────┴────────────────┘\n"
        "> ```\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.13.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_Performance_CountFromMetadata = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.Performance.CountFromMetadata",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] MAY support importing the information about the number of rows from Parquet file directly from the metadata instead of going through the whole file.\n"
        "\n"
        "For example,\n"
        "\n"
        "> When running this query,\n"
        "> \n"
        "> ```sql\n"
        "> SELECT count(*)\n"
        "> FROM file('*.parquet', 'Parquet');\n"
        ">\n"
        "> ┌───count()─┐\n"
        "> │ 110000000 │\n"
        "> └───────────┘\n"
        "> \n"
        "> Elapsed: 1.365 sec.\n"
        "> ```\n"
        "> \n"
        "> The runtime should be around ~16ms instead of 1.365 sec.\n"
        ">\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.14.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_Performance_ParallelProcessing = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.Performance.ParallelProcessing",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support process parallelization when importing from the parquet files.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.14.2",
)

RQ_SRS_032_ClickHouse_Parquet_Import_Nested_ArrayIntoNested = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.Nested.ArrayIntoNested",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing nested columns from the Parquet file.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.15.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_Nested_Complex = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.Nested.Complex",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing nested: `Array`, `Tuple` and `Map` datatypes from Parquet files.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.15.2",
)

RQ_SRS_032_ClickHouse_Parquet_Import_Nested_ArrayIntoNested_ImportNested = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.Nested.ArrayIntoNested.ImportNested",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support inserting arrays of nested structs from Parquet files into [ClickHouse] Nested columns when the `input_format_parquet_import_nested` setting is set to `1`.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.15.3",
)

RQ_SRS_032_ClickHouse_Parquet_Import_Nested_ArrayIntoNested_NotImportNested = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.Nested.ArrayIntoNested.NotImportNested",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error when trying to insert arrays of nested structs from Parquet files into [ClickHouse] Nested columns when the\n"
        "`input_format_parquet_import_nested` setting is set to `0`.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.15.4",
)

RQ_SRS_032_ClickHouse_Parquet_Import_Nested_ArrayIntoNotNested = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.Nested.ArrayIntoNotNested",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error when trying to insert arrays of nested structs from Parquet files into [ClickHouse] not Nested columns.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.15.5",
)

RQ_SRS_032_ClickHouse_Parquet_Import_Nested_NonArrayIntoNested = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.Nested.NonArrayIntoNested",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error when trying to insert datatypes other than arrays of nested structs from Parquet files into [ClickHouse] Nested columns.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.15.6",
)

RQ_SRS_032_ClickHouse_Parquet_Import_ChunkedColumns = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.ChunkedColumns",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing Parquet files with chunked columns.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.16.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_Encoding_Plain = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.Plain",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `Plain` encoded Parquet files.\n" "\n"
    ),
    link=None,
    level=4,
    num="8.17.1.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_Encoding_Dictionary = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.Dictionary",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `Dictionary` encoded Parquet files.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="8.17.2.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_Encoding_RunLength = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.RunLength",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `Run Length Encoding / Bit-Packing Hybrid` encoded Parquet files.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="8.17.3.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_Encoding_Delta = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.Delta",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `Delta Encoding` encoded Parquet files.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="8.17.4.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_Encoding_DeltaLengthByteArray = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.DeltaLengthByteArray",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `Delta-length byte array` encoded Parquet files.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="8.17.5.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_Encoding_DeltaStrings = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.DeltaStrings",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `Delta Strings` encoded Parquet files.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="8.17.6.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_Encoding_ByteStreamSplit = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.ByteStreamSplit",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing `Byte Stream Split` encoded Parquet files.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="8.17.7.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_Settings_ImportNested = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.Settings.ImportNested",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support specifying the `input_format_parquet_import_nested` setting to allow inserting arrays of\n"
        "nested structs into Nested column type. The default value SHALL be `0`.\n"
        "\n"
        "- `0` — Data can not be inserted into Nested columns as an array of structs.\n"
        "- `1` — Data can be inserted into Nested columns as an array of structs.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.18.1",
)

RQ_SRS_032_ClickHouse_Parquet_Import_Settings_CaseInsensitiveColumnMatching = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.Settings.CaseInsensitiveColumnMatching",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support specifying the `input_format_parquet_case_insensitive_column_matching` setting to ignore matching\n"
        "Parquet and ClickHouse columns. The default value SHALL be `0`.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.18.2",
)

RQ_SRS_032_ClickHouse_Parquet_Import_Settings_AllowMissingColumns = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.Settings.AllowMissingColumns",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support specifying the `input_format_parquet_allow_missing_columns` setting to allow missing columns.\n"
        "The default value SHALL be `0`.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.18.3",
)

RQ_SRS_032_ClickHouse_Parquet_Import_Settings_SkipColumnsWithUnsupportedTypesInSchemaInference = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Import.Settings.SkipColumnsWithUnsupportedTypesInSchemaInference",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support specifying the `input_format_parquet_skip_columns_with_unsupported_types_in_schema_inference` \n"
        "setting to allow skipping unsupported types. The default value SHALL be `0`.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.18.4",
)

RQ_SRS_032_ClickHouse_Parquet_Libraries = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Libraries",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing from Parquet files generated using various libraries.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="8.19.1",
)

RQ_SRS_032_ClickHouse_Parquet_Libraries_Pyarrow = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Libraries.Pyarrow",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing from Parquet files generated using `Pyarrow`.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="8.19.2.1",
)

RQ_SRS_032_ClickHouse_Parquet_Libraries_PySpark = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Libraries.PySpark",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing from Parquet files generated using `PySpark`.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="8.19.3.1",
)

RQ_SRS_032_ClickHouse_Parquet_Libraries_Pandas = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Libraries.Pandas",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing from Parquet files generated using `Pandas`.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="8.19.4.1",
)

RQ_SRS_032_ClickHouse_Parquet_Libraries_ParquetGO = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Libraries.ParquetGO",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing from Parquet files generated using `parquet-go`.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="8.19.5.1",
)

RQ_SRS_032_ClickHouse_Parquet_Libraries_H2OAI = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Libraries.H2OAI",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing from Parquet files generated using `H2OAI`.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="8.19.6.1",
)

RQ_SRS_032_ClickHouse_Parquet_Export = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support using `SELECT` query with either the `INTO OUTFILE {file_name}` or just `FORMAT Parquet` clauses to Export Parquet files. \n"
        "\n"
        "For example,\n"
        "\n"
        "```sql\n"
        "SELECT *\n"
        "FROM sometable\n"
        "INTO OUTFILE 'export.parquet'\n"
        "FORMAT Parquet\n"
        "```\n"
        "\n"
        "or\n"
        "\n"
        "```sql\n"
        "SELECT *\n"
        "FROM sometable\n"
        "FORMAT Parquet\n"
        "```\n"
        "\n"
    ),
    link=None,
    level=3,
    num="9.19.1",
)

RQ_SRS_032_ClickHouse_Parquet_Export_Outfile_AutoDetectParquetFileFormat = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.Outfile.AutoDetectParquetFileFormat",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support automatically detecting Parquet file format based on file extension when using OUTFILE clause without explicitly specifying the format setting.\n"
        "\n"
        "```sql\n"
        "SELECT *\n"
        "FROM sometable\n"
        "INTO OUTFILE 'export.parquet'\n"
        "```\n"
        "\n"
    ),
    link=None,
    level=4,
    num="9.19.2.1",
)

RQ_SRS_032_ClickHouse_Parquet_Export_Datatypes_Supported = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.Datatypes.Supported",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting the following datatypes to Parquet:\n"
        "\n"
        "| ClickHouse data type                  | Parquet data type         |\n"
        "|---------------------------------------|---------------------------|\n"
        "| `Bool`                                | `BOOL`                    |\n"
        "| `UInt8`                               | `UINT8`                   |\n"
        "| `Int8`/`Enum8`                        | `INT8`                    |\n"
        "| `UInt16`                              | `UINT16`                  |\n"
        "| `Int16`/`Enum16`                      | `INT16`                   |\n"
        "| `UInt32`                              | `UINT32`                  |\n"
        "| `Int32`                               | `INT32`                   |\n"
        "| `UInt64`                              | `UINT64`                  |\n"
        "| `Int64`                               | `INT64`                   |\n"
        "| `Float32`                             | `FLOAT`                   |\n"
        "| `Float64`                             | `DOUBLE`                  |\n"
        "| `Date32`                              | `DATE`                    |\n"
        "| `DateTime`                            | `UINT32`                  |\n"
        "| `DateTime64`                          | `TIMESTAMP`               |\n"
        "| `String`                              | `BINARY`                  |\n"
        "| `FixedString`                         | `FIXED_LENGTH_BYTE_ARRAY` |\n"
        "| `Decimal`                             | `DECIMAL`                 |\n"
        "| `Array`                               | `LIST`                    |\n"
        "| `Tuple`                               | `STRUCT`                  |\n"
        "| `Map`                                 | `MAP`                     |\n"
        "| `IPv4`                                | `UINT32`                  |\n"
        "| `IPv6`                                | `FIXED_LENGTH_BYTE_ARRAY` |\n"
        "| `Int128`/`UInt128`/`Int256`/`UInt256` | `FIXED_LENGTH_BYTE_ARRAY` |\n"
        "\n"
    ),
    link=None,
    level=3,
    num="9.20.1",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_BLOB = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.BLOB",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting parquet files with `BLOB` content.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.2",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_BOOL = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.BOOL",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `BOOL` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.3",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_UINT8 = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.UINT8",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `UINT8` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.4",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_INT8 = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.INT8",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `INT8` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.5",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_UINT16 = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.UINT16",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `UINT16` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.6",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_INT16 = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.INT16",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `INT16` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.7",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_UINT32 = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.UINT32",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `UINT32` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.8",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_INT32 = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.INT32",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `INT32` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.9",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_UINT64 = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.UINT64",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `UINT64` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.10",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_INT64 = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.INT64",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `INT64` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.11",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_FLOAT = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.FLOAT",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `FLOAT` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.12",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_DOUBLE = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DOUBLE",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `DOUBLE` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.13",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_DATE = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DATE",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `DATE` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.14",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_DATE_ms = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DATE.ms",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `DATE (ms)` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.15",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_DATE_ns = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DATE.ns",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `DATE (ns)` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.16",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_DATE_us = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DATE.us",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `DATE (us)` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.17",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_TIME_ms = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.TIME.ms",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `TIME (ms)` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.18",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_TIMESTAMP_ms = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.TIMESTAMP.ms",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `TIMESTAMP (ms)` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.19",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_TIMESTAMP_ns = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.TIMESTAMP.ns",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `TIMESTAMP (ns)` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.20",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_TIMESTAMP_us = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.TIMESTAMP.us",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `TIMESTAMP (us)` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.21",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_STRING = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.STRING",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `STRING` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.22",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_BINARY = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.BINARY",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `BINARY` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.23",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_FixedLengthByteArray = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.FixedLengthByteArray",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `FIXED_LENGTH_BYTE_ARRAY` Parquet datatype.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="9.20.24",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_DECIMAL = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DECIMAL",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `DECIMAL` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.25",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_DECIMAL_Filter = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DECIMAL.Filter",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `DECIMAL` Parquet datatype with specified filters.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="9.20.26",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_LIST = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.LIST",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `LIST` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.27",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_ARRAY = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.ARRAY",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `ARRAY` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.28",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_STRUCT = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.STRUCT",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `STRUCT` Parquet datatype.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.20.29",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_MAP = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.MAP",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=("[ClickHouse] SHALL support exporting `MAP` Parquet datatype.\n" "\n"),
    link=None,
    level=3,
    num="9.20.30",
)

RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Nullable = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Nullable",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `Nullable` datatypes to Parquet files and `Nullable` datatypes that consist only of `Null`.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="9.20.31",
)

RQ_SRS_032_ClickHouse_Parquet_Export_Nested = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.Nested",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting nested columns to the Parquet file.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="9.21.1",
)

RQ_SRS_032_ClickHouse_Parquet_Export_Nested_Complex = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.Nested.Complex",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting nested: `Array`, `Tuple` and `Map` datatypes to Parquet files.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="9.21.2",
)

RQ_SRS_032_ClickHouse_Parquet_Export_ChunkedColumns = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.ChunkedColumns",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting chunked columns to Parquet files.\n" "\n"
    ),
    link=None,
    level=3,
    num="9.22.1",
)

RQ_SRS_032_ClickHouse_Export_Parquet_Join = Requirement(
    name="RQ.SRS-032.ClickHouse.Export.Parquet.Join",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting output of `SELECT` query with a `JOIN` clause into a Parquet file.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="9.23.1.1",
)

RQ_SRS_032_ClickHouse_Parquet_Export_Union = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.Union",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting output of `SELECT` query with a `UNION` clause into a Parquet file.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="9.23.2.1",
)

RQ_SRS_032_ClickHouse_Parquet_Export_Union_Multiple = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.Union.Multiple",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting output of `SELECT` query with multiple `UNION` clauses used on the Parquet file.\n"
        "\n"
        "For example,\n"
        "\n"
        "```sql\n"
        "SELECT * FROM (SELECT * FROM file('file0001.parquet')\n"
        "UNION ALL SELECT * FROM file('file0001.parquet')\n"
        "UNION ALL SELECT * FROM file('file0001.parquet')\n"
        "UNION ALL SELECT * FROM file('file0001.parquet')\n"
        "UNION ALL SELECT * FROM file('file0001.parquet')\n"
        "...\n"
        "UNION ALL SELECT * FROM file('file0001.parquet')) LIMIT 10;\n"
        "```\n"
        "\n"
    ),
    link=None,
    level=4,
    num="9.23.2.2",
)

RQ_SRS_032_ClickHouse_Parquet_Export_View = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.View",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting output of `SELECT * FROM {view_name}` query into a Parquet file.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="9.23.3",
)

RQ_SRS_032_ClickHouse_Parquet_Export_Select_MaterializedView = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.Select.MaterializedView",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting output of `SELECT * FROM {mat_view_name}` query into a Parquet file.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="9.23.4",
)

RQ_SRS_032_ClickHouse_Parquet_Export_Encoding_Plain = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.Plain",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `Plain` encoded Parquet files.\n" "\n"
    ),
    link=None,
    level=4,
    num="9.24.1.1",
)

RQ_SRS_032_ClickHouse_Parquet_Export_Encoding_Dictionary = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.Dictionary",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `Dictionary` encoded Parquet files.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="9.24.2.1",
)

RQ_SRS_032_ClickHouse_Parquet_Export_Encoding_RunLength = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.RunLength",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `Run Length Encoding / Bit-Packing Hybrid` encoded Parquet files.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="9.24.3.1",
)

RQ_SRS_032_ClickHouse_Parquet_Export_Encoding_Delta = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.Delta",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `Delta Encoding` encoded Parquet files.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="9.24.4.1",
)

RQ_SRS_032_ClickHouse_Parquet_Export_Encoding_DeltaLengthByteArray = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.DeltaLengthByteArray",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `Delta-length byte array` encoded Parquet files.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="9.24.5.1",
)

RQ_SRS_032_ClickHouse_Parquet_Export_Encoding_DeltaStrings = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.DeltaStrings",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `Delta Strings` encoded Parquet files.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="9.24.6.1",
)

RQ_SRS_032_ClickHouse_Parquet_Export_Encoding_ByteStreamSplit = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.ByteStreamSplit",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support exporting `Byte Stream Split` encoded Parquet files.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="9.24.7.1",
)

RQ_SRS_032_ClickHouse_Parquet_Export_Settings_RowGroupSize = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.Settings.RowGroupSize",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support specifying the `output_format_parquet_row_group_size` setting to specify row group size in rows.\n"
        "The default value SHALL be `1000000`.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="9.25.1",
)

RQ_SRS_032_ClickHouse_Parquet_Export_Settings_StringAsString = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.Settings.StringAsString",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support specifying the `output_format_parquet_string_as_string` setting to use Parquet String type instead of Binary.\n"
        "The default value SHALL be `0`.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="9.25.2",
)

RQ_SRS_032_ClickHouse_Parquet_Export_Settings_StringAsFixedByteArray = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.Settings.StringAsFixedByteArray",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support specifying the `output_format_parquet_fixed_string_as_fixed_byte_array` setting to use Parquet FIXED_LENGTH_BYTE_ARRAY type instead of Binary/String for FixedString columns. The default value SHALL be `1`.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="9.25.3",
)

RQ_SRS_032_ClickHouse_Parquet_Export_Settings_ParquetVersion = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.Settings.ParquetVersion",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support specifying the `output_format_parquet_version` setting to set the version of Parquet used in the output file.\n"
        "The default value SHALL be `2.latest`.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="9.25.4",
)

RQ_SRS_032_ClickHouse_Parquet_Export_Settings_CompressionMethod = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Export.Settings.CompressionMethod",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support specifying the `output_format_parquet_compression_method` setting to set the compression method used in the Parquet file.\n"
        "The default value SHALL be `lz4`.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="9.25.5",
)

RQ_SRS_032_ClickHouse_Parquet_DataTypes_TypeConversionFunction = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.TypeConversionFunction",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support using type conversion functions when importing Parquet files.\n"
        "\n"
        "For example,\n"
        "\n"
        "```sql\n"
        "SELECT\n"
        "    n,\n"
        "    toDateTime(time)\n"
        "FROM file('time.parquet', Parquet);\n"
        "```\n"
        "\n"
    ),
    link=None,
    level=3,
    num="9.26.1",
)

RQ_SRS_032_ClickHouse_Parquet_Hive = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Hive",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] MAY not support importing or exporting hive partitioned Parquet files.\n"
        "\n"
    ),
    link=None,
    level=2,
    num="10.1",
)

RQ_SRS_032_ClickHouse_Parquet_Encryption_File = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Encryption.File",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] MAY support importing or exporting encrypted Parquet files.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="11.1.1",
)

RQ_SRS_032_ClickHouse_Parquet_Encryption_Column_Modular = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Encryption.Column.Modular",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] MAY support importing or exporting Parquet files with specific encrypted columns.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="11.2.1",
)

RQ_SRS_032_ClickHouse_Parquet_Encryption_Column_Keys = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Encryption.Column.Keys",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] MAY support importing or exporting Parquet files when different columns are encrypted with different keys.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="11.2.2",
)

RQ_SRS_032_ClickHouse_Parquet_Encryption_Algorithms_AESGCM = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Encryption.Algorithms.AESGCM",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] MAY support importing or exporting Parquet files with `AES-GCM` encryption algorithm.\n"
        "\n"
        "> The default algorithm AES-GCM provides full protection against tampering with data and metadata parts in Parquet files.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="11.3.1",
)

RQ_SRS_032_ClickHouse_Parquet_Encryption_Algorithms_AESGCMCTR = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Encryption.Algorithms.AESGCMCTR",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] MAY support importing or exporting Parquet files with `AES-GCM-CTR`  encryption algorithm.\n"
        "\n"
        "> The alternative algorithm AES-GCM-CTR supports partial integrity protection of Parquet files. \n"
        "> Only metadata parts are protected against tampering, not data parts. \n"
        "> An advantage of this algorithm is that it has a lower throughput overhead compared to the AES-GCM algorithm.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="11.3.2",
)

RQ_SRS_032_ClickHouse_Parquet_Encryption_Parameters = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Encryption.Parameters",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] MAY support importing or exporting Parquet files with different parameters.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="11.4.1",
)

RQ_SRS_032_ClickHouse_Parquet_Encryption_Parameters_Algorythm = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Encryption.Parameters.Algorythm",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] MAY support importing or exporting Parquet files with `encryption.algorithm` parameter specified.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="11.4.1.1",
)

RQ_SRS_032_ClickHouse_Parquet_Encryption_Parameters_Plaintext_Footer = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Encryption.Parameters.Plaintext.Footer",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] MAY support importing or exporting Parquet files with `encryption.plaintext.footer` parameter specified.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="11.4.1.2",
)

RQ_SRS_032_ClickHouse_Parquet_Structure = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Structure",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support using `DESCRIBE TABLE` statement on the Parquet to read the file structure.\n"
        "\n"
        "For example,\n"
        "\n"
        "```sql\n"
        "DESCRIBE TABLE file('data.parquet', Parquet)\n"
        "```\n"
        "\n"
    ),
    link=None,
    level=2,
    num="12.1",
)

RQ_SRS_032_ClickHouse_Parquet_Compression_None = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Compression.None",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing or exporting uncompressed Parquet files.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="13.1.1",
)

RQ_SRS_032_ClickHouse_Parquet_Compression_Gzip = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Compression.Gzip",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing or exporting Parquet files compressed using gzip.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="13.2.1",
)

RQ_SRS_032_ClickHouse_Parquet_Compression_Brotli = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Compression.Brotli",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing or exporting Parquet files compressed using brotli.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="13.3.1",
)

RQ_SRS_032_ClickHouse_Parquet_Compression_Lz4 = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Compression.Lz4",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing or exporting Parquet files compressed using lz4.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="13.4.1",
)

RQ_SRS_032_ClickHouse_Parquet_Compression_Lz4Raw = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Compression.Lz4Raw",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing or exporting Parquet files compressed using lz4_raw.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="13.5.1",
)

RQ_SRS_032_ClickHouse_Parquet_Compression_Lz4Hadoop = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Compression.Lz4Hadoop",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing or exporting Parquet files compressed using LZ4_HADOOP.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="13.6.1",
)

RQ_SRS_032_ClickHouse_Parquet_Compression_Snappy = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Compression.Snappy",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing or exporting Parquet files compressed using Snappy.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="13.7.1",
)

RQ_SRS_032_ClickHouse_Parquet_Compression_Zstd = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Compression.Zstd",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing or exporting Parquet files compressed using Zstd.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="13.8.1",
)

RQ_SRS_032_ClickHouse_Parquet_UnsupportedCompression_Lzo = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.UnsupportedCompression.Lzo",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] MAY not support importing or exporting Parquet files compressed using lzo.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="13.9.1.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableFunctions_URL = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.URL",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `url` table function importing and exporting Parquet format.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="14.1.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableFunctions_File = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.File",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `file` table function importing and exporting Parquet format.\n"
        "\n"
        "For example,\n"
        "\n"
        "```sql\n"
        "SELECT * FROM file('data.parquet', Parquet)\n"
        "```\n"
        "\n"
    ),
    link=None,
    level=3,
    num="14.2.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableFunctions_File_AutoDetectParquetFileFormat = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.File.AutoDetectParquetFileFormat",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support automatically detecting Parquet file format based on file extension when using `file()` function without explicitly specifying the format setting.\n"
        "\n"
        "```sql\n"
        "SELECT * FROM file('data.parquet')\n"
        "```\n"
        "\n"
    ),
    link=None,
    level=3,
    num="14.2.2",
)

RQ_SRS_032_ClickHouse_Parquet_TableFunctions_S3 = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.S3",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `s3` table function for import and exporting Parquet format.\n"
        "\n"
        "For example,\n"
        "\n"
        "```sql\n"
        "SELECT *\n"
        "FROM gcs('https://storage.googleapis.com/my-test-bucket-768/data.parquet', Parquet)\n"
        "```\n"
        "\n"
    ),
    link=None,
    level=3,
    num="14.3.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableFunctions_JDBC = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.JDBC",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `jdbc` table function for import and exporting Parquet format.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="14.4.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableFunctions_ODBC = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.ODBC",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `odbc` table function for importing and exporting Parquet format.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="14.5.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableFunctions_HDFS = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.HDFS",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `hdfs` table function for importing and exporting Parquet format.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="14.6.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableFunctions_Remote = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.Remote",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `remote` table function for importing and exporting Parquet format.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="14.7.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableFunctions_MySQL = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.MySQL",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `mysql` table function for import and exporting Parquet format.\n"
        "\n"
        "For example,\n"
        "\n"
        "> Given we have a table with a `mysql` engine:\n"
        "> \n"
        "> ```sql\n"
        "> CREATE TABLE mysql_table1 (\n"
        ">   id UInt64,\n"
        ">   column1 String\n"
        "> )\n"
        "> ENGINE = MySQL('mysql-host.domain.com','db1','table1','mysql_clickhouse','Password123!')\n"
        "> ```\n"
        "> \n"
        "> We can Export from a Parquet file format with:\n"
        "> \n"
        "> ```sql\n"
        "> SELECT * FROM mysql_table1 INTO OUTFILE testTable.parquet FORMAT Parquet\n"
        "> ```\n"
        "\n"
    ),
    link=None,
    level=3,
    num="14.8.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableFunctions_PostgreSQL = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.PostgreSQL",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `postgresql` table function importing and exporting Parquet format.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="14.9.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_ReadableExternalTable = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.ReadableExternalTable",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] MAY support Parquet format being exported from and imported into all table engines using `READABLE EXTERNAL TABLE`.\n"
        "\n"
        "For example,\n"
        "\n"
        "> ```sql\n"
        "> CREATE READABLE EXTERNAL TABLE table_name (\n"
        ">     key UInt32,\n"
        ">     value UInt32\n"
        "> ) LOCATION ('file://file_localtion/*.parquet')\n"
        "> ```\n"
        "\n"
    ),
    link=None,
    level=3,
    num="15.1.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_MergeTree_MergeTree = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.MergeTree",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being exported from and imported into a `MergeTree` table engine.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="15.2.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_MergeTree_ReplicatedMergeTree = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.ReplicatedMergeTree",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being exported from and imported into a `ReplicatedMergeTree` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="15.2.2.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_MergeTree_ReplacingMergeTree = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.ReplacingMergeTree",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being exported from and imported into a `ReplacingMergeTree` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="15.2.3.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_MergeTree_SummingMergeTree = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.SummingMergeTree",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being exported from and imported into a `SummingMergeTree` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="15.2.4.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_MergeTree_AggregatingMergeTree = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.AggregatingMergeTree",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being exported from and imported into a `AggregatingMergeTree` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="15.2.5.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_MergeTree_CollapsingMergeTree = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.CollapsingMergeTree",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being exported from and imported into a `CollapsingMergeTree` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="15.2.6.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_MergeTree_VersionedCollapsingMergeTree = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.VersionedCollapsingMergeTree",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being exported from and imported into a `VersionedCollapsingMergeTree` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="15.2.7.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_MergeTree_GraphiteMergeTree = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.GraphiteMergeTree",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being exported from and imported into a `GraphiteMergeTree` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="15.2.8.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_ODBC = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.ODBC",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being exported from and imported into an `ODBC` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="15.3.1.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_JDBC = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.JDBC",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being exported from and imported into a `JDBC` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="15.3.2.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_MySQL = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.MySQL",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being exported from and imported into a `MySQL` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="15.3.3.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_MongoDB = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.MongoDB",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being exported from and imported into a `MongoDB` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="15.3.4.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_HDFS = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.HDFS",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being exported from and imported into a `HDFS` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="15.3.5.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_S3 = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.S3",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being exported from and imported into an `S3` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="15.3.6.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_Kafka = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.Kafka",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being exported from and imported into a `Kafka` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="15.3.7.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_EmbeddedRocksDB = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.EmbeddedRocksDB",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being exported from and imported into an `EmbeddedRocksDB` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="15.3.8.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_PostgreSQL = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.PostgreSQL",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being exported from and imported into a `PostgreSQL` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="15.3.9.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Special_Memory = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.Memory",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being exported from and imported into a `Memory` table engine.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="15.4.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Special_Distributed = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.Distributed",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being exported from and imported into a `Distributed` table engine.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="15.4.2",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Special_Dictionary = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.Dictionary",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being exported from and imported into a `Dictionary` table engine.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="15.4.3",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Special_File = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.File",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being exported from and imported into a `File` table engine.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="15.4.4",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Special_URL = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.URL",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being exported from and imported into a `URL` table engine.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="15.4.5",
)

RQ_SRS_032_ClickHouse_Parquet_Indexes = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Indexes",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing from Parquet files that utilize indexes.\n"
        "\n"
    ),
    link=None,
    level=2,
    num="16.1",
)

RQ_SRS_032_ClickHouse_Parquet_Indexes_Page = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Indexes.Page",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support utilizing 'Page Index' of a parquet file in order to read data from the file more efficiently.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="16.2.1",
)

RQ_SRS_032_ClickHouse_Parquet_Indexes_BloomFilter = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Indexes.BloomFilter",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support utilizing 'Bloom Filter' of a parquet file in order to read data from the file more efficiently.\n"
        "\n"
        "> A Bloom filter is a compact data structure that overapproximates a set. It can respond to membership \n"
        "> queries with either “definitely no” or “probably yes”, where the probability of false positives is configured when the filter is initialized. Bloom filters do not have false negatives.\n"
        "> \n"
        "> Because Bloom filters are small compared to dictionaries, they can be used for predicate pushdown even in columns with high cardinality and when space is at a premium.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="16.3.1",
)

RQ_SRS_032_ClickHouse_Parquet_Indexes_Dictionary = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Indexes.Dictionary",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support utilizing 'Dictionary' of a parquet file in order to read data from the file more efficiently.\n"
        "\n"
        "\n"
    ),
    link=None,
    level=3,
    num="16.4.1",
)

RQ_SRS_032_ClickHouse_Parquet_Metadata_ParquetMetadataFormat = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadataFormat",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `ParquetMetadata` format to read metadata from Parquet files.\n"
        "\n"
        "For example,\n"
        "\n"
        "```sql\n"
        "SELECT * FROM file(data.parquet, ParquetMetadata) format PrettyJSONEachRow\n"
        "```\n"
        "\n"
    ),
    link=None,
    level=3,
    num="17.1.1",
)

RQ_SRS_032_ClickHouse_Parquet_Metadata_ParquetMetadataFormat_Output = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadataFormat.Output",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL not support `ParquetMetadata` format as an output format and the `FORMAT_IS_NOT_SUITABLE_FOR_OUTPUT` \n"
        "error SHALL be returned.\n"
        "\n"
        "For example,\n"
        "\n"
        "```sql\n"
        "SELECT *\n"
        "FROM file('writing_nullable_int8.parquet', 'ParquetMetadata')\n"
        "FORMAT ParquetMetadata\n"
        "\n"
        "Exception on client:\n"
        "Code: 399. DB::Exception: Code: 399. DB::Exception: Format ParquetMetadata is not suitable for output. (FORMAT_IS_NOT_SUITABLE_FOR_OUTPUT) (version 23.5.1.2890 (official build)). (FORMAT_IS_NOT_SUITABLE_FOR_OUTPUT)\n"
        "```\n"
        "\n"
    ),
    link=None,
    level=3,
    num="17.1.2",
)

RQ_SRS_032_ClickHouse_Parquet_Metadata_ParquetMetadata_Content = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadata.Content",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse]'s ParquetMetadata format SHALL output the Parquet metadata in the following structure:\n"
        "\n"
        "> - num_columns - the number of columns\n"
        "> - num_rows - the total number of rows\n"
        "> - num_row_groups - the total number of row groups\n"
        "> - format_version - parquet format version, always 1.0 or 2.6\n"
        "> - total_uncompressed_size - total uncompressed bytes size of the data, calculated as the sum of total_byte_size from all row groups\n"
        "> - total_compressed_size - total compressed bytes size of the data, calculated as the sum of total_compressed_size from all row groups\n"
        "> - columns - the list of columns metadata with the next structure:\n"
        ">     - name - column name\n"
        ">     - path - column path (differs from name for nested column)\n"
        ">     - max_definition_level - maximum definition level\n"
        ">     - max_repetition_level - maximum repetition level\n"
        ">     - physical_type - column physical type\n"
        ">     - logical_type - column logical type\n"
        ">     - compression - compression used for this column\n"
        ">     - total_uncompressed_size - total uncompressed bytes size of the column, calculated as the sum of total_uncompressed_size of the column from all row groups\n"
        ">     - total_compressed_size - total compressed bytes size of the column, calculated as the sum of total_compressed_size of the column from all row groups\n"
        ">     - space_saved - percent of space saved by compression, calculated as (1 - total_compressed_size/total_uncompressed_size).\n"
        ">     - encodings - the list of encodings used for this column\n"
        "> - row_groups - the list of row groups metadata with the next structure:\n"
        ">     - num_columns - the number of columns in the row group\n"
        ">     - num_rows - the number of rows in the row group\n"
        ">     - total_uncompressed_size - total uncompressed bytes size of the row group\n"
        ">     - total_compressed_size - total compressed bytes size of the row group\n"
        ">     - columns - the list of column chunks metadata with the next structure:\n"
        ">        - name - column name\n"
        ">        - path - column path\n"
        ">        - total_compressed_size - total compressed bytes size of the column\n"
        ">        - total_uncompressed_size - total uncompressed bytes size of the row group\n"
        ">        - have_statistics - boolean flag that indicates if column chunk metadata contains column statistics\n"
        ">        - statistics - column chunk statistics (all fields are NULL if have_statistics = false) with the next structure:\n"
        ">            - num_values - the number of non-null values in the column chunk\n"
        ">            - null_count - the number of NULL values in the column chunk\n"
        ">            - distinct_count - the number of distinct values in the column chunk\n"
        ">            - min - the minimum value of the column chunk\n"
        ">            - max - the maximum column of the column chunk\n"
        "\n"
        "For example,\n"
        "\n"
        "> ```json\n"
        "> {\n"
        '>     "num_columns": "2",\n'
        '>     "num_rows": "100000",\n'
        '>     "num_row_groups": "2",\n'
        '>     "format_version": "2.6",\n'
        '>     "metadata_size": "577",\n'
        '>     "total_uncompressed_size": "282436",\n'
        '>     "total_compressed_size": "26633",\n'
        '>     "columns": [\n'
        ">         {\n"
        '>             "name": "number",\n'
        '>             "path": "number",\n'
        '>             "max_definition_level": "0",\n'
        '>             "max_repetition_level": "0",\n'
        '>             "physical_type": "INT32",\n'
        '>             "logical_type": "Int(bitWidth=16, isSigned=false)",\n'
        '>             "compression": "LZ4",\n'
        '>             "total_uncompressed_size": "133321",\n'
        '>             "total_compressed_size": "13293",\n'
        '>             "space_saved": "90.03%",\n'
        '>             "encodings": [\n'
        '>                 "RLE_DICTIONARY",\n'
        '>                 "PLAIN",\n'
        '>                 "RLE"\n'
        ">             ]\n"
        ">         },\n"
        ">         {\n"
        '>             "name": "concat(\'Hello\', toString(modulo(number, 1000)))",\n'
        '>             "path": "concat(\'Hello\', toString(modulo(number, 1000)))",\n'
        '>             "max_definition_level": "0",\n'
        '>             "max_repetition_level": "0",\n'
        '>             "physical_type": "BYTE_ARRAY",\n'
        '>             "logical_type": "None",\n'
        '>             "compression": "LZ4",\n'
        '>             "total_uncompressed_size": "149115",\n'
        '>             "total_compressed_size": "13340",\n'
        '>             "space_saved": "91.05%",\n'
        '>             "encodings": [\n'
        '>                 "RLE_DICTIONARY",\n'
        '>                 "PLAIN",\n'
        '>                 "RLE"\n'
        ">             ]\n"
        ">         }\n"
        ">     ],\n"
        '>     "row_groups": [\n'
        ">         {\n"
        '>             "num_columns": "2",\n'
        '>             "num_rows": "65409",\n'
        '>             "total_uncompressed_size": "179809",\n'
        '>             "total_compressed_size": "14163",\n'
        '>             "columns": [\n'
        ">                 {\n"
        '>                     "name": "number",\n'
        '>                     "path": "number",\n'
        '>                     "total_compressed_size": "7070",\n'
        '>                     "total_uncompressed_size": "85956",\n'
        '>                     "have_statistics": true,\n'
        '>                     "statistics": {\n'
        '>                         "num_values": "65409",\n'
        '>                         "null_count": "0",\n'
        '>                         "distinct_count": null,\n'
        '>                         "min": "0",\n'
        '>                         "max": "999"\n'
        ">                     }\n"
        ">                 },\n"
        ">                 {\n"
        '>                     "name": "concat(\'Hello\', toString(modulo(number, 1000)))",\n'
        '>                     "path": "concat(\'Hello\', toString(modulo(number, 1000)))",\n'
        '>                     "total_compressed_size": "7093",\n'
        '>                     "total_uncompressed_size": "93853",\n'
        '>                     "have_statistics": true,\n'
        '>                     "statistics": {\n'
        '>                         "num_values": "65409",\n'
        '>                         "null_count": "0",\n'
        '>                         "distinct_count": null,\n'
        '>                         "min": "Hello0",\n'
        '>                         "max": "Hello999"\n'
        ">                     }\n"
        ">                 }\n"
        ">             ]\n"
        ">         }\n"
        "> \n"
        ">     ]\n"
        "> }\n"
        "> ```\n"
        "\n"
    ),
    link=None,
    level=3,
    num="17.1.3",
)

RQ_SRS_032_ClickHouse_Parquet_Metadata_ParquetMetadata_MinMax = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadata.MinMax",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet files that have Min/Max values in the metadata and the files that are missing Min/Max values.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="17.1.4",
)

RQ_SRS_032_ClickHouse_Parquet_Metadata_File = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Metadata.File",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support accessing `File Metadata` in Parquet files.\n" "\n"
    ),
    link=None,
    level=3,
    num="17.2.1",
)

RQ_SRS_032_ClickHouse_Parquet_Metadata_Column = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Metadata.Column",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support accessing `Column (Chunk) Metadata` in Parquet files.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="17.2.2",
)

RQ_SRS_032_ClickHouse_Parquet_Metadata_Header = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Metadata.Header",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support accessing `Page Header Metadata` in Parquet files.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="17.2.3",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Metadata_MagicNumber = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Metadata.MagicNumber",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        '[ClickHouse] SHALL output an error if the 4-byte magic number "PAR1" is missing from the Parquet metadata.\n'
        "\n"
        "For example,\n"
        "\n"
        'When using hexeditor on the Parquet file we alter the values of "PAR1" and change it to "PARQ".\n'
        "then when we try to import that Parquet file to [ClickHouse] we SHALL get an exception:\n"
        "\n"
        "```\n"
        "exception. Code: 1001, type: parquet::ParquetInvalidOrCorruptedFileException,\n"
        "e.what() = Invalid: Parquet magic bytes not found in footer.\n"
        "Either the file is corrupted or this is not a Parquet file.\n"
        "```\n"
        "\n"
    ),
    link=None,
    level=2,
    num="18.1",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Metadata_File = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Metadata.File",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to access the corrupt `file` metadata.\n"
        "In this case the file metadata is corrupt, the file is lost.\n"
        "\n"
    ),
    link=None,
    level=2,
    num="18.2",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Metadata_Column = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Metadata.Column",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to access the corrupt `column` metadata.\n"
        "In this case that column chunk MAY be lost but column chunks for this column in other row groups SHALL be okay.\n"
        "\n"
    ),
    link=None,
    level=2,
    num="18.3",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Metadata_PageHeader = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Metadata.PageHeader",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to access the corrupt `Page Header`.\n"
        "In this case the remaining pages in that chunk SHALL be lost.\n"
        "\n"
    ),
    link=None,
    level=2,
    num="18.4",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Metadata_PageData = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Metadata.PageData",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to access the corrupt `Page Data`.\n"
        "In this case that page SHALL be lost.\n"
        "\n"
    ),
    link=None,
    level=2,
    num="18.5",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Metadata_Checksum = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Metadata.Checksum",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error if the Parquet file's checksum is corrupted.\n"
        "\n"
    ),
    link=None,
    level=2,
    num="18.6",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to access the corrupt column values.\n"
        "\n"
        "Error message example,\n"
        "\n"
        "> DB::Exception: Cannot extract table structure from Parquet format file.\n"
        "\n"
        "\n"
    ),
    link=None,
    level=2,
    num="18.7",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_Date = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Date",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `date` values.\n"
        "\n"
        "\n"
    ),
    link=None,
    level=3,
    num="18.7.1",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_Int = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Int",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `Int` values.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="18.7.2",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_BigInt = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.BigInt",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `BigInt` values.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="18.7.3",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_SmallInt = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.SmallInt",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `SmallInt` values.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="18.7.4",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_TinyInt = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.TinyInt",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `TinyInt` values.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="18.7.5",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_UInt = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.UInt",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `UInt` values.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="18.7.6",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_UBigInt = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.UBigInt",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `UBigInt` values.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="18.7.7",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_USmallInt = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.USmallInt",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `USmallInt` values.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="18.7.8",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_UTinyInt = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.UTinyInt",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `UTinyInt` values.\n"
        "\n"
        "\n"
    ),
    link=None,
    level=3,
    num="18.7.9",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_TimestampUS = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.TimestampUS",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `Timestamp (us)` values.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="18.7.10",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_TimestampMS = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.TimestampMS",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `Timestamp (ms)` values.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="18.7.11",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_Bool = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Bool",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `BOOL` values.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="18.7.12",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_Float = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Float",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `FLOAT` values.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="18.7.13",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_Double = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Double",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `DOUBLE` values.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="18.7.14",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_TimeMS = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.TimeMS",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `TIME (ms)` values.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="18.7.15",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_TimeUS = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.TimeUS",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `TIME (us)` values.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="18.7.16",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_TimeNS = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.TimeNS",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `TIME (ns)` values.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="18.7.17",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_String = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.String",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `STRING` values.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="18.7.18",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_Binary = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Binary",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `BINARY` values.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="18.7.19",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_FixedLengthByteArray = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.FixedLengthByteArray",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `FIXED_LENGTH_BYTE_ARRAY` values.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="18.7.20",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_Decimal = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Decimal",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `DECIMAL` values.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="18.7.21",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_List = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.List",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `LIST` values.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="18.7.22",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_Struct = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Struct",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `STRUCT` values.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="18.7.23",
)

RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_Map = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Map",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `MAP` values.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="18.7.24",
)

RQ_SRS_032_ClickHouse_Parquet_Interoperability_From_x86_To_ARM = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Interoperability.From.x86.To.ARM",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing and exporting parquet files on `ARM` machine that were generated on `x86` machine.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="19.1.1",
)

RQ_SRS_032_ClickHouse_Parquet_Interoperability_From_ARM_To_x86 = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Interoperability.From.ARM.To.x86",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support importing and exporting parquet files on `x86` machine that were generated on `ARM` machine.\n"
        "\n"
        "[ClickHouse]: https://clickhouse.com\n"
        "[GitHub Repository]: https://github.com/Altinity/clickhouse-regression/blob/main/parquet/requirements/requirements.md\n"
        "[Revision History]: https://github.com/Altinity/clickhouse-regression/commits/main/parquet/requirements/requirements.md\n"
        "[Git]: https://git-scm.com/\n"
        "[GitHub]: https://github.com\n"
    ),
    link=None,
    level=3,
    num="19.2.1",
)

SRS032_ClickHouse_Parquet_Data_Format = Specification(
    name="SRS032 ClickHouse Parquet Data Format",
    description=None,
    author=None,
    date=None,
    status=None,
    approved_by=None,
    approved_date=None,
    approved_version=None,
    version=None,
    group=None,
    type=None,
    link=None,
    uid=None,
    parent=None,
    children=None,
    headings=(
        Heading(name="Revision History", level=1, num="1"),
        Heading(name="Introduction", level=1, num="2"),
        Heading(name="Feature Diagram", level=1, num="3"),
        Heading(name="Working With Parquet", level=1, num="4"),
        Heading(name="RQ.SRS-032.ClickHouse.Parquet", level=2, num="4.1"),
        Heading(name="Supported Parquet Versions", level=1, num="5"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.SupportedVersions", level=2, num="5.1"
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ClickHouseLocal", level=2, num="5.2"
        ),
        Heading(name="Offsets", level=1, num="6"),
        Heading(name="RQ.SRS-032.ClickHouse.Parquet.Offsets", level=2, num="6.1"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Offsets.MonotonicallyIncreasing",
            level=3,
            num="6.1.1",
        ),
        Heading(name="Query Cache", level=1, num="7"),
        Heading(name="RQ.SRS-032.ClickHouse.Parquet.Query.Cache", level=2, num="7.1"),
        Heading(name="Import from Parquet Files", level=1, num="8"),
        Heading(name="RQ.SRS-032.ClickHouse.Parquet.Import", level=2, num="8.1"),
        Heading(name="Auto Detect Parquet File When Importing", level=2, num="8.2"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.AutoDetectParquetFileFormat",
            level=3,
            num="8.2.1",
        ),
        Heading(name="Glob Patterns", level=2, num="8.3"),
        Heading(name="RQ.SRS-032.ClickHouse.Parquet.Import.Glob", level=3, num="8.3.1"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.Glob.MultiDirectory",
            level=3,
            num="8.3.2",
        ),
        Heading(name="Supported Datatypes", level=2, num="8.4"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Conversion",
            level=3,
            num="8.4.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported",
            level=3,
            num="8.4.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.BLOB",
            level=3,
            num="8.4.3",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.BOOL",
            level=3,
            num="8.4.4",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.UINT8",
            level=3,
            num="8.4.5",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.INT8",
            level=3,
            num="8.4.6",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.UINT16",
            level=3,
            num="8.4.7",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.INT16",
            level=3,
            num="8.4.8",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.UINT32",
            level=3,
            num="8.4.9",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.INT32",
            level=3,
            num="8.4.10",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.UINT64",
            level=3,
            num="8.4.11",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.INT64",
            level=3,
            num="8.4.12",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.FLOAT",
            level=3,
            num="8.4.13",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DOUBLE",
            level=3,
            num="8.4.14",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DATE",
            level=3,
            num="8.4.15",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DATE.ms",
            level=3,
            num="8.4.16",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DATE.ns",
            level=3,
            num="8.4.17",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DATE.us",
            level=3,
            num="8.4.18",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.TIME.ms",
            level=3,
            num="8.4.19",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.TIMESTAMP.ms",
            level=3,
            num="8.4.20",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.TIMESTAMP.ns",
            level=3,
            num="8.4.21",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.TIMESTAMP.us",
            level=3,
            num="8.4.22",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.STRING",
            level=3,
            num="8.4.23",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.BINARY",
            level=3,
            num="8.4.24",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.FixedLengthByteArray",
            level=3,
            num="8.4.25",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DECIMAL",
            level=3,
            num="8.4.26",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DECIMAL.Filter",
            level=3,
            num="8.4.27",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.LIST",
            level=3,
            num="8.4.28",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.ARRAY",
            level=3,
            num="8.4.29",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.STRUCT",
            level=3,
            num="8.4.30",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.MAP",
            level=3,
            num="8.4.31",
        ),
        Heading(name="UTCAdjusted", level=3, num="8.4.32"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.DateUTCAdjusted",
            level=4,
            num="8.4.32.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.TimestampUTCAdjusted",
            level=4,
            num="8.4.32.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.TimeUTCAdjusted",
            level=4,
            num="8.4.32.3",
        ),
        Heading(name="Nullable", level=3, num="8.4.33"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.NullValues",
            level=4,
            num="8.4.33.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.ImportInto.Nullable",
            level=4,
            num="8.4.33.2",
        ),
        Heading(name="LowCardinality", level=3, num="8.4.34"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.ImportInto.LowCardinality",
            level=4,
            num="8.4.34.1",
        ),
        Heading(name="Nested", level=3, num="8.4.35"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.ImportInto.Nested",
            level=4,
            num="8.4.35.1",
        ),
        Heading(name="UNKNOWN", level=3, num="8.4.36"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.ImportInto.Unknown",
            level=4,
            num="8.4.36.1",
        ),
        Heading(name="Unsupported Datatypes", level=2, num="8.5"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Unsupported",
            level=3,
            num="8.5.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Unsupported.ChunkedArray",
            level=3,
            num="8.5.2",
        ),
        Heading(name="Filter Pushdown", level=2, num="8.6"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.FilterPushdown",
            level=3,
            num="8.6.1",
        ),
        Heading(name="Projections", level=2, num="8.7"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.Projections",
            level=3,
            num="8.7.1",
        ),
        Heading(name="Skip Columns", level=2, num="8.8"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.SkipColumns",
            level=3,
            num="8.8.1",
        ),
        Heading(name="Skip Values", level=2, num="8.9"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.SkipValues", level=3, num="8.9.1"
        ),
        Heading(name="Auto Typecast", level=2, num="8.10"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.AutoTypecast",
            level=3,
            num="8.10.1",
        ),
        Heading(name="Row Group Size", level=2, num="8.11"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.RowGroupSize",
            level=3,
            num="8.11.1",
        ),
        Heading(name="Data Page Size", level=2, num="8.12"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.DataPageSize",
            level=3,
            num="8.12.1",
        ),
        Heading(name="Import Into New Table", level=2, num="8.13"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.NewTable", level=3, num="8.13.1"
        ),
        Heading(name="Performance", level=2, num="8.14"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.Performance.CountFromMetadata",
            level=3,
            num="8.14.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.Performance.ParallelProcessing",
            level=3,
            num="8.14.2",
        ),
        Heading(name="Import Nested Types", level=2, num="8.15"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.Nested.ArrayIntoNested",
            level=3,
            num="8.15.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.Nested.Complex",
            level=3,
            num="8.15.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.Nested.ArrayIntoNested.ImportNested",
            level=3,
            num="8.15.3",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.Nested.ArrayIntoNested.NotImportNested",
            level=3,
            num="8.15.4",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.Nested.ArrayIntoNotNested",
            level=3,
            num="8.15.5",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.Nested.NonArrayIntoNested",
            level=3,
            num="8.15.6",
        ),
        Heading(name="Import Chunked Columns", level=2, num="8.16"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.ChunkedColumns",
            level=3,
            num="8.16.1",
        ),
        Heading(name="Import Encoded", level=2, num="8.17"),
        Heading(name="Plain (Import)", level=3, num="8.17.1"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.Plain",
            level=4,
            num="8.17.1.1",
        ),
        Heading(name="Dictionary (Import)", level=3, num="8.17.2"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.Dictionary",
            level=4,
            num="8.17.2.1",
        ),
        Heading(name="Run Length Encoding (Import)", level=3, num="8.17.3"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.RunLength",
            level=4,
            num="8.17.3.1",
        ),
        Heading(name="Delta (Import)", level=3, num="8.17.4"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.Delta",
            level=4,
            num="8.17.4.1",
        ),
        Heading(name="Delta-length byte array (Import)", level=3, num="8.17.5"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.DeltaLengthByteArray",
            level=4,
            num="8.17.5.1",
        ),
        Heading(name="Delta Strings (Import)", level=3, num="8.17.6"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.DeltaStrings",
            level=4,
            num="8.17.6.1",
        ),
        Heading(name="Byte Stream Split (Import)", level=3, num="8.17.7"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.ByteStreamSplit",
            level=4,
            num="8.17.7.1",
        ),
        Heading(name="Import Settings", level=2, num="8.18"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.Settings.ImportNested",
            level=3,
            num="8.18.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.Settings.CaseInsensitiveColumnMatching",
            level=3,
            num="8.18.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.Settings.AllowMissingColumns",
            level=3,
            num="8.18.3",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Import.Settings.SkipColumnsWithUnsupportedTypesInSchemaInference",
            level=3,
            num="8.18.4",
        ),
        Heading(name="Libraries", level=2, num="8.19"),
        Heading(name="RQ.SRS-032.ClickHouse.Parquet.Libraries", level=3, num="8.19.1"),
        Heading(name="Pyarrow", level=3, num="8.19.2"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Libraries.Pyarrow",
            level=4,
            num="8.19.2.1",
        ),
        Heading(name="PySpark", level=3, num="8.19.3"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Libraries.PySpark",
            level=4,
            num="8.19.3.1",
        ),
        Heading(name="Pandas", level=3, num="8.19.4"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Libraries.Pandas",
            level=4,
            num="8.19.4.1",
        ),
        Heading(name="parquet-go", level=3, num="8.19.5"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Libraries.ParquetGO",
            level=4,
            num="8.19.5.1",
        ),
        Heading(name="H2OAI", level=3, num="8.19.6"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Libraries.H2OAI",
            level=4,
            num="8.19.6.1",
        ),
        Heading(name="Export from Parquet Files", level=1, num="9"),
        Heading(name="RQ.SRS-032.ClickHouse.Parquet.Export", level=3, num="9.19.1"),
        Heading(name="Auto Detect Parquet File When Exporting", level=3, num="9.19.2"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.Outfile.AutoDetectParquetFileFormat",
            level=4,
            num="9.19.2.1",
        ),
        Heading(name="Supported Data types", level=2, num="9.20"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.Datatypes.Supported",
            level=3,
            num="9.20.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.BLOB",
            level=3,
            num="9.20.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.BOOL",
            level=3,
            num="9.20.3",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.UINT8",
            level=3,
            num="9.20.4",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.INT8",
            level=3,
            num="9.20.5",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.UINT16",
            level=3,
            num="9.20.6",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.INT16",
            level=3,
            num="9.20.7",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.UINT32",
            level=3,
            num="9.20.8",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.INT32",
            level=3,
            num="9.20.9",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.UINT64",
            level=3,
            num="9.20.10",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.INT64",
            level=3,
            num="9.20.11",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.FLOAT",
            level=3,
            num="9.20.12",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DOUBLE",
            level=3,
            num="9.20.13",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DATE",
            level=3,
            num="9.20.14",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DATE.ms",
            level=3,
            num="9.20.15",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DATE.ns",
            level=3,
            num="9.20.16",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DATE.us",
            level=3,
            num="9.20.17",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.TIME.ms",
            level=3,
            num="9.20.18",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.TIMESTAMP.ms",
            level=3,
            num="9.20.19",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.TIMESTAMP.ns",
            level=3,
            num="9.20.20",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.TIMESTAMP.us",
            level=3,
            num="9.20.21",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.STRING",
            level=3,
            num="9.20.22",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.BINARY",
            level=3,
            num="9.20.23",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.FixedLengthByteArray",
            level=3,
            num="9.20.24",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DECIMAL",
            level=3,
            num="9.20.25",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DECIMAL.Filter",
            level=3,
            num="9.20.26",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.LIST",
            level=3,
            num="9.20.27",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.ARRAY",
            level=3,
            num="9.20.28",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.STRUCT",
            level=3,
            num="9.20.29",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.MAP",
            level=3,
            num="9.20.30",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Nullable",
            level=3,
            num="9.20.31",
        ),
        Heading(name="Working With Nested Types Export", level=2, num="9.21"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.Nested", level=3, num="9.21.1"
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.Nested.Complex",
            level=3,
            num="9.21.2",
        ),
        Heading(name="Exporting Chunked Columns", level=2, num="9.22"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.ChunkedColumns",
            level=3,
            num="9.22.1",
        ),
        Heading(name="Query Types", level=2, num="9.23"),
        Heading(name="JOIN", level=3, num="9.23.1"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Export.Parquet.Join", level=4, num="9.23.1.1"
        ),
        Heading(name="UNION", level=3, num="9.23.2"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.Union", level=4, num="9.23.2.1"
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.Union.Multiple",
            level=4,
            num="9.23.2.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.View", level=3, num="9.23.3"
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.Select.MaterializedView",
            level=3,
            num="9.23.4",
        ),
        Heading(name="Export Encoded", level=2, num="9.24"),
        Heading(name="Plain (Export)", level=3, num="9.24.1"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.Plain",
            level=4,
            num="9.24.1.1",
        ),
        Heading(name="Dictionary (Export)", level=3, num="9.24.2"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.Dictionary",
            level=4,
            num="9.24.2.1",
        ),
        Heading(name="Run Length Encoding (Export)", level=3, num="9.24.3"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.RunLength",
            level=4,
            num="9.24.3.1",
        ),
        Heading(name="Delta (Export)", level=3, num="9.24.4"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.Delta",
            level=4,
            num="9.24.4.1",
        ),
        Heading(name="Delta-length byte array (Export)", level=3, num="9.24.5"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.DeltaLengthByteArray",
            level=4,
            num="9.24.5.1",
        ),
        Heading(name="Delta Strings (Export)", level=3, num="9.24.6"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.DeltaStrings",
            level=4,
            num="9.24.6.1",
        ),
        Heading(name="Byte Stream Split (Export)", level=3, num="9.24.7"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.ByteStreamSplit",
            level=4,
            num="9.24.7.1",
        ),
        Heading(name="Export Settings", level=2, num="9.25"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.Settings.RowGroupSize",
            level=3,
            num="9.25.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.Settings.StringAsString",
            level=3,
            num="9.25.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.Settings.StringAsFixedByteArray",
            level=3,
            num="9.25.3",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.Settings.ParquetVersion",
            level=3,
            num="9.25.4",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Export.Settings.CompressionMethod",
            level=3,
            num="9.25.5",
        ),
        Heading(name="Type Conversion", level=2, num="9.26"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.TypeConversionFunction",
            level=3,
            num="9.26.1",
        ),
        Heading(name="Hive Partitioning", level=1, num="10"),
        Heading(name="RQ.SRS-032.ClickHouse.Parquet.Hive", level=2, num="10.1"),
        Heading(name="Parquet Encryption", level=1, num="11"),
        Heading(name="File Encryption", level=2, num="11.1"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Encryption.File", level=3, num="11.1.1"
        ),
        Heading(name="Column Encryption", level=2, num="11.2"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Encryption.Column.Modular",
            level=3,
            num="11.2.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Encryption.Column.Keys",
            level=3,
            num="11.2.2",
        ),
        Heading(name="Encryption Algorithms", level=2, num="11.3"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Encryption.Algorithms.AESGCM",
            level=3,
            num="11.3.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Encryption.Algorithms.AESGCMCTR",
            level=3,
            num="11.3.2",
        ),
        Heading(name="EncryptionParameters", level=2, num="11.4"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Encryption.Parameters",
            level=3,
            num="11.4.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Encryption.Parameters.Algorythm",
            level=4,
            num="11.4.1.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Encryption.Parameters.Plaintext.Footer",
            level=4,
            num="11.4.1.2",
        ),
        Heading(name="DESCRIBE Parquet", level=1, num="12"),
        Heading(name="RQ.SRS-032.ClickHouse.Parquet.Structure", level=2, num="12.1"),
        Heading(name="Compression", level=1, num="13"),
        Heading(name="None", level=2, num="13.1"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Compression.None", level=3, num="13.1.1"
        ),
        Heading(name="Gzip", level=2, num="13.2"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Compression.Gzip", level=3, num="13.2.1"
        ),
        Heading(name="Brotli", level=2, num="13.3"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Compression.Brotli",
            level=3,
            num="13.3.1",
        ),
        Heading(name="Lz4", level=2, num="13.4"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Compression.Lz4", level=3, num="13.4.1"
        ),
        Heading(name="Lz4Raw", level=2, num="13.5"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Compression.Lz4Raw",
            level=3,
            num="13.5.1",
        ),
        Heading(name="Lz4Hadoop", level=2, num="13.6"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Compression.Lz4Hadoop",
            level=3,
            num="13.6.1",
        ),
        Heading(name="Snappy", level=2, num="13.7"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Compression.Snappy",
            level=3,
            num="13.7.1",
        ),
        Heading(name="Zstd", level=2, num="13.8"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Compression.Zstd", level=3, num="13.8.1"
        ),
        Heading(name="Unsupported Compression", level=2, num="13.9"),
        Heading(name="Lzo", level=3, num="13.9.1"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.UnsupportedCompression.Lzo",
            level=4,
            num="13.9.1.1",
        ),
        Heading(name="Table Functions", level=1, num="14"),
        Heading(name="URL", level=2, num="14.1"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.URL",
            level=3,
            num="14.1.1",
        ),
        Heading(name="File", level=2, num="14.2"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.File",
            level=3,
            num="14.2.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.File.AutoDetectParquetFileFormat",
            level=3,
            num="14.2.2",
        ),
        Heading(name="S3", level=2, num="14.3"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.S3",
            level=3,
            num="14.3.1",
        ),
        Heading(name="JDBC", level=2, num="14.4"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.JDBC",
            level=3,
            num="14.4.1",
        ),
        Heading(name="ODBC", level=2, num="14.5"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.ODBC",
            level=3,
            num="14.5.1",
        ),
        Heading(name="HDFS", level=2, num="14.6"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.HDFS",
            level=3,
            num="14.6.1",
        ),
        Heading(name="Remote", level=2, num="14.7"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.Remote",
            level=3,
            num="14.7.1",
        ),
        Heading(name="MySQL", level=2, num="14.8"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.MySQL",
            level=3,
            num="14.8.1",
        ),
        Heading(name="PostgreSQL", level=2, num="14.9"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.PostgreSQL",
            level=3,
            num="14.9.1",
        ),
        Heading(name="Table Engines", level=1, num="15"),
        Heading(name="Readable External Table", level=2, num="15.1"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.ReadableExternalTable",
            level=3,
            num="15.1.1",
        ),
        Heading(name="MergeTree", level=2, num="15.2"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.MergeTree",
            level=3,
            num="15.2.1",
        ),
        Heading(name="ReplicatedMergeTree", level=3, num="15.2.2"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.ReplicatedMergeTree",
            level=4,
            num="15.2.2.1",
        ),
        Heading(name="ReplacingMergeTree", level=3, num="15.2.3"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.ReplacingMergeTree",
            level=4,
            num="15.2.3.1",
        ),
        Heading(name="SummingMergeTree", level=3, num="15.2.4"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.SummingMergeTree",
            level=4,
            num="15.2.4.1",
        ),
        Heading(name="AggregatingMergeTree", level=3, num="15.2.5"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.AggregatingMergeTree",
            level=4,
            num="15.2.5.1",
        ),
        Heading(name="CollapsingMergeTree", level=3, num="15.2.6"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.CollapsingMergeTree",
            level=4,
            num="15.2.6.1",
        ),
        Heading(name="VersionedCollapsingMergeTree", level=3, num="15.2.7"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.VersionedCollapsingMergeTree",
            level=4,
            num="15.2.7.1",
        ),
        Heading(name="GraphiteMergeTree", level=3, num="15.2.8"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.GraphiteMergeTree",
            level=4,
            num="15.2.8.1",
        ),
        Heading(name="Integration Engines", level=2, num="15.3"),
        Heading(name="ODBC Engine", level=3, num="15.3.1"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.ODBC",
            level=4,
            num="15.3.1.1",
        ),
        Heading(name="JDBC Engine", level=3, num="15.3.2"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.JDBC",
            level=4,
            num="15.3.2.1",
        ),
        Heading(name="MySQL Engine", level=3, num="15.3.3"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.MySQL",
            level=4,
            num="15.3.3.1",
        ),
        Heading(name="MongoDB Engine", level=3, num="15.3.4"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.MongoDB",
            level=4,
            num="15.3.4.1",
        ),
        Heading(name="HDFS Engine", level=3, num="15.3.5"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.HDFS",
            level=4,
            num="15.3.5.1",
        ),
        Heading(name="S3 Engine", level=3, num="15.3.6"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.S3",
            level=4,
            num="15.3.6.1",
        ),
        Heading(name="Kafka Engine", level=3, num="15.3.7"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.Kafka",
            level=4,
            num="15.3.7.1",
        ),
        Heading(name="EmbeddedRocksDB Engine", level=3, num="15.3.8"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.EmbeddedRocksDB",
            level=4,
            num="15.3.8.1",
        ),
        Heading(name="PostgreSQL Engine", level=3, num="15.3.9"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.PostgreSQL",
            level=4,
            num="15.3.9.1",
        ),
        Heading(name="Special Engines", level=2, num="15.4"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.Memory",
            level=3,
            num="15.4.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.Distributed",
            level=3,
            num="15.4.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.Dictionary",
            level=3,
            num="15.4.3",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.File",
            level=3,
            num="15.4.4",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.URL",
            level=3,
            num="15.4.5",
        ),
        Heading(name="Indexes", level=1, num="16"),
        Heading(name="RQ.SRS-032.ClickHouse.Parquet.Indexes", level=2, num="16.1"),
        Heading(name="Page", level=2, num="16.2"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Indexes.Page", level=3, num="16.2.1"
        ),
        Heading(name="Bloom Filter", level=2, num="16.3"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Indexes.BloomFilter",
            level=3,
            num="16.3.1",
        ),
        Heading(name="Dictionary", level=2, num="16.4"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Indexes.Dictionary",
            level=3,
            num="16.4.1",
        ),
        Heading(name="Metadata", level=1, num="17"),
        Heading(name="ParquetFormat", level=2, num="17.1"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadataFormat",
            level=3,
            num="17.1.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadataFormat.Output",
            level=3,
            num="17.1.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadata.Content",
            level=3,
            num="17.1.3",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadata.MinMax",
            level=3,
            num="17.1.4",
        ),
        Heading(name="Metadata Types", level=2, num="17.2"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Metadata.File", level=3, num="17.2.1"
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Metadata.Column", level=3, num="17.2.2"
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Metadata.Header", level=3, num="17.2.3"
        ),
        Heading(name="Error Recovery", level=1, num="18"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Metadata.MagicNumber",
            level=2,
            num="18.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Metadata.File",
            level=2,
            num="18.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Metadata.Column",
            level=2,
            num="18.3",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Metadata.PageHeader",
            level=2,
            num="18.4",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Metadata.PageData",
            level=2,
            num="18.5",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Metadata.Checksum",
            level=2,
            num="18.6",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values",
            level=2,
            num="18.7",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Date",
            level=3,
            num="18.7.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Int",
            level=3,
            num="18.7.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.BigInt",
            level=3,
            num="18.7.3",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.SmallInt",
            level=3,
            num="18.7.4",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.TinyInt",
            level=3,
            num="18.7.5",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.UInt",
            level=3,
            num="18.7.6",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.UBigInt",
            level=3,
            num="18.7.7",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.USmallInt",
            level=3,
            num="18.7.8",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.UTinyInt",
            level=3,
            num="18.7.9",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.TimestampUS",
            level=3,
            num="18.7.10",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.TimestampMS",
            level=3,
            num="18.7.11",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Bool",
            level=3,
            num="18.7.12",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Float",
            level=3,
            num="18.7.13",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Double",
            level=3,
            num="18.7.14",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.TimeMS",
            level=3,
            num="18.7.15",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.TimeUS",
            level=3,
            num="18.7.16",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.TimeNS",
            level=3,
            num="18.7.17",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.String",
            level=3,
            num="18.7.18",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Binary",
            level=3,
            num="18.7.19",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.FixedLengthByteArray",
            level=3,
            num="18.7.20",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Decimal",
            level=3,
            num="18.7.21",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.List",
            level=3,
            num="18.7.22",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Struct",
            level=3,
            num="18.7.23",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Map",
            level=3,
            num="18.7.24",
        ),
        Heading(name="Interoperability Between ARM and x86", level=1, num="19"),
        Heading(
            name="Importing and Exporting Parquet Files On ARM That Were Generated On x86 Machine",
            level=2,
            num="19.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Interoperability.From.x86.To.ARM",
            level=3,
            num="19.1.1",
        ),
        Heading(
            name="Importing and Exporting Parquet Files On x86 That Were Generated On ARM Machine",
            level=2,
            num="19.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Interoperability.From.ARM.To.x86",
            level=3,
            num="19.2.1",
        ),
    ),
    requirements=(
        RQ_SRS_032_ClickHouse_Parquet,
        RQ_SRS_032_ClickHouse_Parquet_SupportedVersions,
        RQ_SRS_032_ClickHouse_Parquet_ClickHouseLocal,
        RQ_SRS_032_ClickHouse_Parquet_Offsets,
        RQ_SRS_032_ClickHouse_Parquet_Offsets_MonotonicallyIncreasing,
        RQ_SRS_032_ClickHouse_Parquet_Query_Cache,
        RQ_SRS_032_ClickHouse_Parquet_Import,
        RQ_SRS_032_ClickHouse_Parquet_Import_AutoDetectParquetFileFormat,
        RQ_SRS_032_ClickHouse_Parquet_Import_Glob,
        RQ_SRS_032_ClickHouse_Parquet_Import_Glob_MultiDirectory,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Conversion,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_BLOB,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_BOOL,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_UINT8,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_INT8,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_UINT16,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_INT16,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_UINT32,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_INT32,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_UINT64,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_INT64,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_FLOAT,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_DOUBLE,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_DATE,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_DATE_ms,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_DATE_ns,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_DATE_us,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_TIME_ms,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_TIMESTAMP_ms,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_TIMESTAMP_ns,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_TIMESTAMP_us,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_STRING,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_BINARY,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_FixedLengthByteArray,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_DECIMAL,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_DECIMAL_Filter,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_LIST,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_ARRAY,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_STRUCT,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Supported_MAP,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_DateUTCAdjusted,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_TimestampUTCAdjusted,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_TimeUTCAdjusted,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_NullValues,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_ImportInto_Nullable,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_ImportInto_LowCardinality,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_ImportInto_Nested,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_ImportInto_Unknown,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Unsupported,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataTypes_Unsupported_ChunkedArray,
        RQ_SRS_032_ClickHouse_Parquet_Import_FilterPushdown,
        RQ_SRS_032_ClickHouse_Parquet_Import_Projections,
        RQ_SRS_032_ClickHouse_Parquet_Import_SkipColumns,
        RQ_SRS_032_ClickHouse_Parquet_Import_SkipValues,
        RQ_SRS_032_ClickHouse_Parquet_Import_AutoTypecast,
        RQ_SRS_032_ClickHouse_Parquet_Import_RowGroupSize,
        RQ_SRS_032_ClickHouse_Parquet_Import_DataPageSize,
        RQ_SRS_032_ClickHouse_Parquet_Import_NewTable,
        RQ_SRS_032_ClickHouse_Parquet_Import_Performance_CountFromMetadata,
        RQ_SRS_032_ClickHouse_Parquet_Import_Performance_ParallelProcessing,
        RQ_SRS_032_ClickHouse_Parquet_Import_Nested_ArrayIntoNested,
        RQ_SRS_032_ClickHouse_Parquet_Import_Nested_Complex,
        RQ_SRS_032_ClickHouse_Parquet_Import_Nested_ArrayIntoNested_ImportNested,
        RQ_SRS_032_ClickHouse_Parquet_Import_Nested_ArrayIntoNested_NotImportNested,
        RQ_SRS_032_ClickHouse_Parquet_Import_Nested_ArrayIntoNotNested,
        RQ_SRS_032_ClickHouse_Parquet_Import_Nested_NonArrayIntoNested,
        RQ_SRS_032_ClickHouse_Parquet_Import_ChunkedColumns,
        RQ_SRS_032_ClickHouse_Parquet_Import_Encoding_Plain,
        RQ_SRS_032_ClickHouse_Parquet_Import_Encoding_Dictionary,
        RQ_SRS_032_ClickHouse_Parquet_Import_Encoding_RunLength,
        RQ_SRS_032_ClickHouse_Parquet_Import_Encoding_Delta,
        RQ_SRS_032_ClickHouse_Parquet_Import_Encoding_DeltaLengthByteArray,
        RQ_SRS_032_ClickHouse_Parquet_Import_Encoding_DeltaStrings,
        RQ_SRS_032_ClickHouse_Parquet_Import_Encoding_ByteStreamSplit,
        RQ_SRS_032_ClickHouse_Parquet_Import_Settings_ImportNested,
        RQ_SRS_032_ClickHouse_Parquet_Import_Settings_CaseInsensitiveColumnMatching,
        RQ_SRS_032_ClickHouse_Parquet_Import_Settings_AllowMissingColumns,
        RQ_SRS_032_ClickHouse_Parquet_Import_Settings_SkipColumnsWithUnsupportedTypesInSchemaInference,
        RQ_SRS_032_ClickHouse_Parquet_Libraries,
        RQ_SRS_032_ClickHouse_Parquet_Libraries_Pyarrow,
        RQ_SRS_032_ClickHouse_Parquet_Libraries_PySpark,
        RQ_SRS_032_ClickHouse_Parquet_Libraries_Pandas,
        RQ_SRS_032_ClickHouse_Parquet_Libraries_ParquetGO,
        RQ_SRS_032_ClickHouse_Parquet_Libraries_H2OAI,
        RQ_SRS_032_ClickHouse_Parquet_Export,
        RQ_SRS_032_ClickHouse_Parquet_Export_Outfile_AutoDetectParquetFileFormat,
        RQ_SRS_032_ClickHouse_Parquet_Export_Datatypes_Supported,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_BLOB,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_BOOL,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_UINT8,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_INT8,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_UINT16,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_INT16,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_UINT32,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_INT32,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_UINT64,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_INT64,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_FLOAT,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_DOUBLE,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_DATE,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_DATE_ms,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_DATE_ns,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_DATE_us,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_TIME_ms,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_TIMESTAMP_ms,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_TIMESTAMP_ns,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_TIMESTAMP_us,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_STRING,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_BINARY,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_FixedLengthByteArray,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_DECIMAL,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_DECIMAL_Filter,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_LIST,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_ARRAY,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_STRUCT,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Supported_MAP,
        RQ_SRS_032_ClickHouse_Parquet_Export_DataTypes_Nullable,
        RQ_SRS_032_ClickHouse_Parquet_Export_Nested,
        RQ_SRS_032_ClickHouse_Parquet_Export_Nested_Complex,
        RQ_SRS_032_ClickHouse_Parquet_Export_ChunkedColumns,
        RQ_SRS_032_ClickHouse_Export_Parquet_Join,
        RQ_SRS_032_ClickHouse_Parquet_Export_Union,
        RQ_SRS_032_ClickHouse_Parquet_Export_Union_Multiple,
        RQ_SRS_032_ClickHouse_Parquet_Export_View,
        RQ_SRS_032_ClickHouse_Parquet_Export_Select_MaterializedView,
        RQ_SRS_032_ClickHouse_Parquet_Export_Encoding_Plain,
        RQ_SRS_032_ClickHouse_Parquet_Export_Encoding_Dictionary,
        RQ_SRS_032_ClickHouse_Parquet_Export_Encoding_RunLength,
        RQ_SRS_032_ClickHouse_Parquet_Export_Encoding_Delta,
        RQ_SRS_032_ClickHouse_Parquet_Export_Encoding_DeltaLengthByteArray,
        RQ_SRS_032_ClickHouse_Parquet_Export_Encoding_DeltaStrings,
        RQ_SRS_032_ClickHouse_Parquet_Export_Encoding_ByteStreamSplit,
        RQ_SRS_032_ClickHouse_Parquet_Export_Settings_RowGroupSize,
        RQ_SRS_032_ClickHouse_Parquet_Export_Settings_StringAsString,
        RQ_SRS_032_ClickHouse_Parquet_Export_Settings_StringAsFixedByteArray,
        RQ_SRS_032_ClickHouse_Parquet_Export_Settings_ParquetVersion,
        RQ_SRS_032_ClickHouse_Parquet_Export_Settings_CompressionMethod,
        RQ_SRS_032_ClickHouse_Parquet_DataTypes_TypeConversionFunction,
        RQ_SRS_032_ClickHouse_Parquet_Hive,
        RQ_SRS_032_ClickHouse_Parquet_Encryption_File,
        RQ_SRS_032_ClickHouse_Parquet_Encryption_Column_Modular,
        RQ_SRS_032_ClickHouse_Parquet_Encryption_Column_Keys,
        RQ_SRS_032_ClickHouse_Parquet_Encryption_Algorithms_AESGCM,
        RQ_SRS_032_ClickHouse_Parquet_Encryption_Algorithms_AESGCMCTR,
        RQ_SRS_032_ClickHouse_Parquet_Encryption_Parameters,
        RQ_SRS_032_ClickHouse_Parquet_Encryption_Parameters_Algorythm,
        RQ_SRS_032_ClickHouse_Parquet_Encryption_Parameters_Plaintext_Footer,
        RQ_SRS_032_ClickHouse_Parquet_Structure,
        RQ_SRS_032_ClickHouse_Parquet_Compression_None,
        RQ_SRS_032_ClickHouse_Parquet_Compression_Gzip,
        RQ_SRS_032_ClickHouse_Parquet_Compression_Brotli,
        RQ_SRS_032_ClickHouse_Parquet_Compression_Lz4,
        RQ_SRS_032_ClickHouse_Parquet_Compression_Lz4Raw,
        RQ_SRS_032_ClickHouse_Parquet_Compression_Lz4Hadoop,
        RQ_SRS_032_ClickHouse_Parquet_Compression_Snappy,
        RQ_SRS_032_ClickHouse_Parquet_Compression_Zstd,
        RQ_SRS_032_ClickHouse_Parquet_UnsupportedCompression_Lzo,
        RQ_SRS_032_ClickHouse_Parquet_TableFunctions_URL,
        RQ_SRS_032_ClickHouse_Parquet_TableFunctions_File,
        RQ_SRS_032_ClickHouse_Parquet_TableFunctions_File_AutoDetectParquetFileFormat,
        RQ_SRS_032_ClickHouse_Parquet_TableFunctions_S3,
        RQ_SRS_032_ClickHouse_Parquet_TableFunctions_JDBC,
        RQ_SRS_032_ClickHouse_Parquet_TableFunctions_ODBC,
        RQ_SRS_032_ClickHouse_Parquet_TableFunctions_HDFS,
        RQ_SRS_032_ClickHouse_Parquet_TableFunctions_Remote,
        RQ_SRS_032_ClickHouse_Parquet_TableFunctions_MySQL,
        RQ_SRS_032_ClickHouse_Parquet_TableFunctions_PostgreSQL,
        RQ_SRS_032_ClickHouse_Parquet_TableEngines_ReadableExternalTable,
        RQ_SRS_032_ClickHouse_Parquet_TableEngines_MergeTree_MergeTree,
        RQ_SRS_032_ClickHouse_Parquet_TableEngines_MergeTree_ReplicatedMergeTree,
        RQ_SRS_032_ClickHouse_Parquet_TableEngines_MergeTree_ReplacingMergeTree,
        RQ_SRS_032_ClickHouse_Parquet_TableEngines_MergeTree_SummingMergeTree,
        RQ_SRS_032_ClickHouse_Parquet_TableEngines_MergeTree_AggregatingMergeTree,
        RQ_SRS_032_ClickHouse_Parquet_TableEngines_MergeTree_CollapsingMergeTree,
        RQ_SRS_032_ClickHouse_Parquet_TableEngines_MergeTree_VersionedCollapsingMergeTree,
        RQ_SRS_032_ClickHouse_Parquet_TableEngines_MergeTree_GraphiteMergeTree,
        RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_ODBC,
        RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_JDBC,
        RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_MySQL,
        RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_MongoDB,
        RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_HDFS,
        RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_S3,
        RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_Kafka,
        RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_EmbeddedRocksDB,
        RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_PostgreSQL,
        RQ_SRS_032_ClickHouse_Parquet_TableEngines_Special_Memory,
        RQ_SRS_032_ClickHouse_Parquet_TableEngines_Special_Distributed,
        RQ_SRS_032_ClickHouse_Parquet_TableEngines_Special_Dictionary,
        RQ_SRS_032_ClickHouse_Parquet_TableEngines_Special_File,
        RQ_SRS_032_ClickHouse_Parquet_TableEngines_Special_URL,
        RQ_SRS_032_ClickHouse_Parquet_Indexes,
        RQ_SRS_032_ClickHouse_Parquet_Indexes_Page,
        RQ_SRS_032_ClickHouse_Parquet_Indexes_BloomFilter,
        RQ_SRS_032_ClickHouse_Parquet_Indexes_Dictionary,
        RQ_SRS_032_ClickHouse_Parquet_Metadata_ParquetMetadataFormat,
        RQ_SRS_032_ClickHouse_Parquet_Metadata_ParquetMetadataFormat_Output,
        RQ_SRS_032_ClickHouse_Parquet_Metadata_ParquetMetadata_Content,
        RQ_SRS_032_ClickHouse_Parquet_Metadata_ParquetMetadata_MinMax,
        RQ_SRS_032_ClickHouse_Parquet_Metadata_File,
        RQ_SRS_032_ClickHouse_Parquet_Metadata_Column,
        RQ_SRS_032_ClickHouse_Parquet_Metadata_Header,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Metadata_MagicNumber,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Metadata_File,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Metadata_Column,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Metadata_PageHeader,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Metadata_PageData,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Metadata_Checksum,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_Date,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_Int,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_BigInt,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_SmallInt,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_TinyInt,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_UInt,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_UBigInt,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_USmallInt,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_UTinyInt,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_TimestampUS,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_TimestampMS,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_Bool,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_Float,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_Double,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_TimeMS,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_TimeUS,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_TimeNS,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_String,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_Binary,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_FixedLengthByteArray,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_Decimal,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_List,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_Struct,
        RQ_SRS_032_ClickHouse_Parquet_ErrorRecovery_Corrupt_Values_Map,
        RQ_SRS_032_ClickHouse_Parquet_Interoperability_From_x86_To_ARM,
        RQ_SRS_032_ClickHouse_Parquet_Interoperability_From_ARM_To_x86,
    ),
    content="""
# SRS032 ClickHouse Parquet Data Format
# Software Requirements Specification

## Table of Contents

* 1 [Revision History](#revision-history)
* 2 [Introduction](#introduction)
* 3 [Feature Diagram](#feature-diagram)
* 4 [Working With Parquet](#working-with-parquet)
    * 4.1 [RQ.SRS-032.ClickHouse.Parquet](#rqsrs-032clickhouseparquet)
* 5 [Supported Parquet Versions](#supported-parquet-versions)
    * 5.1 [RQ.SRS-032.ClickHouse.Parquet.SupportedVersions](#rqsrs-032clickhouseparquetsupportedversions)
    * 5.2 [RQ.SRS-032.ClickHouse.Parquet.ClickHouseLocal](#rqsrs-032clickhouseparquetclickhouselocal)
* 6 [Offsets](#offsets)
    * 6.1 [RQ.SRS-032.ClickHouse.Parquet.Offsets](#rqsrs-032clickhouseparquetoffsets)
        * 6.1.1 [RQ.SRS-032.ClickHouse.Parquet.Offsets.MonotonicallyIncreasing](#rqsrs-032clickhouseparquetoffsetsmonotonicallyincreasing)
* 7 [Query Cache](#query-cache)
    * 7.1 [RQ.SRS-032.ClickHouse.Parquet.Query.Cache](#rqsrs-032clickhouseparquetquerycache)
* 8 [Import from Parquet Files](#import-from-parquet-files)
    * 8.1 [RQ.SRS-032.ClickHouse.Parquet.Import](#rqsrs-032clickhouseparquetimport)
    * 8.2 [Auto Detect Parquet File When Importing](#auto-detect-parquet-file-when-importing)
        * 8.2.1 [RQ.SRS-032.ClickHouse.Parquet.Import.AutoDetectParquetFileFormat](#rqsrs-032clickhouseparquetimportautodetectparquetfileformat)
    * 8.3 [Glob Patterns](#glob-patterns)
        * 8.3.1 [RQ.SRS-032.ClickHouse.Parquet.Import.Glob](#rqsrs-032clickhouseparquetimportglob)
        * 8.3.2 [RQ.SRS-032.ClickHouse.Parquet.Import.Glob.MultiDirectory](#rqsrs-032clickhouseparquetimportglobmultidirectory)
    * 8.4 [Supported Datatypes](#supported-datatypes)
        * 8.4.1 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Conversion](#rqsrs-032clickhouseparquetimportdatatypesconversion)
        * 8.4.2 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported](#rqsrs-032clickhouseparquetimportdatatypessupported)
        * 8.4.3 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.BLOB](#rqsrs-032clickhouseparquetimportdatatypessupportedblob)
        * 8.4.4 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.BOOL](#rqsrs-032clickhouseparquetimportdatatypessupportedbool)
        * 8.4.5 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.UINT8](#rqsrs-032clickhouseparquetimportdatatypessupporteduint8)
        * 8.4.6 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.INT8](#rqsrs-032clickhouseparquetimportdatatypessupportedint8)
        * 8.4.7 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.UINT16](#rqsrs-032clickhouseparquetimportdatatypessupporteduint16)
        * 8.4.8 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.INT16](#rqsrs-032clickhouseparquetimportdatatypessupportedint16)
        * 8.4.9 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.UINT32](#rqsrs-032clickhouseparquetimportdatatypessupporteduint32)
        * 8.4.10 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.INT32](#rqsrs-032clickhouseparquetimportdatatypessupportedint32)
        * 8.4.11 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.UINT64](#rqsrs-032clickhouseparquetimportdatatypessupporteduint64)
        * 8.4.12 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.INT64](#rqsrs-032clickhouseparquetimportdatatypessupportedint64)
        * 8.4.13 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.FLOAT](#rqsrs-032clickhouseparquetimportdatatypessupportedfloat)
        * 8.4.14 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DOUBLE](#rqsrs-032clickhouseparquetimportdatatypessupporteddouble)
        * 8.4.15 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DATE](#rqsrs-032clickhouseparquetimportdatatypessupporteddate)
        * 8.4.16 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DATE.ms](#rqsrs-032clickhouseparquetimportdatatypessupporteddatems)
        * 8.4.17 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DATE.ns](#rqsrs-032clickhouseparquetimportdatatypessupporteddatens)
        * 8.4.18 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DATE.us](#rqsrs-032clickhouseparquetimportdatatypessupporteddateus)
        * 8.4.19 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.TIME.ms](#rqsrs-032clickhouseparquetimportdatatypessupportedtimems)
        * 8.4.20 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.TIMESTAMP.ms](#rqsrs-032clickhouseparquetimportdatatypessupportedtimestampms)
        * 8.4.21 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.TIMESTAMP.ns](#rqsrs-032clickhouseparquetimportdatatypessupportedtimestampns)
        * 8.4.22 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.TIMESTAMP.us](#rqsrs-032clickhouseparquetimportdatatypessupportedtimestampus)
        * 8.4.23 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.STRING](#rqsrs-032clickhouseparquetimportdatatypessupportedstring)
        * 8.4.24 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.BINARY](#rqsrs-032clickhouseparquetimportdatatypessupportedbinary)
        * 8.4.25 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.FixedLengthByteArray](#rqsrs-032clickhouseparquetimportdatatypessupportedfixedlengthbytearray)
        * 8.4.26 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DECIMAL](#rqsrs-032clickhouseparquetimportdatatypessupporteddecimal)
        * 8.4.27 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DECIMAL.Filter](#rqsrs-032clickhouseparquetimportdatatypessupporteddecimalfilter)
        * 8.4.28 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.LIST](#rqsrs-032clickhouseparquetimportdatatypessupportedlist)
        * 8.4.29 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.ARRAY](#rqsrs-032clickhouseparquetimportdatatypessupportedarray)
        * 8.4.30 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.STRUCT](#rqsrs-032clickhouseparquetimportdatatypessupportedstruct)
        * 8.4.31 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.MAP](#rqsrs-032clickhouseparquetimportdatatypessupportedmap)
        * 8.4.32 [UTCAdjusted](#utcadjusted)
            * 8.4.32.1 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.DateUTCAdjusted](#rqsrs-032clickhouseparquetimportdatatypesdateutcadjusted)
            * 8.4.32.2 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.TimestampUTCAdjusted](#rqsrs-032clickhouseparquetimportdatatypestimestamputcadjusted)
            * 8.4.32.3 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.TimeUTCAdjusted](#rqsrs-032clickhouseparquetimportdatatypestimeutcadjusted)
        * 8.4.33 [Nullable](#nullable)
            * 8.4.33.1 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.NullValues](#rqsrs-032clickhouseparquetimportdatatypesnullvalues)
            * 8.4.33.2 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.ImportInto.Nullable](#rqsrs-032clickhouseparquetimportdatatypesimportintonullable)
        * 8.4.34 [LowCardinality](#lowcardinality)
            * 8.4.34.1 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.ImportInto.LowCardinality](#rqsrs-032clickhouseparquetimportdatatypesimportintolowcardinality)
        * 8.4.35 [Nested](#nested)
            * 8.4.35.1 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.ImportInto.Nested](#rqsrs-032clickhouseparquetimportdatatypesimportintonested)
        * 8.4.36 [UNKNOWN](#unknown)
            * 8.4.36.1 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.ImportInto.Unknown](#rqsrs-032clickhouseparquetimportdatatypesimportintounknown)
    * 8.5 [Unsupported Datatypes](#unsupported-datatypes)
        * 8.5.1 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Unsupported](#rqsrs-032clickhouseparquetimportdatatypesunsupported)
        * 8.5.2 [RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Unsupported.ChunkedArray](#rqsrs-032clickhouseparquetimportdatatypesunsupportedchunkedarray)
    * 8.6 [Filter Pushdown](#filter-pushdown)
        * 8.6.1 [RQ.SRS-032.ClickHouse.Parquet.Import.FilterPushdown](#rqsrs-032clickhouseparquetimportfilterpushdown)
    * 8.7 [Projections](#projections)
        * 8.7.1 [RQ.SRS-032.ClickHouse.Parquet.Import.Projections](#rqsrs-032clickhouseparquetimportprojections)
    * 8.8 [Skip Columns](#skip-columns)
        * 8.8.1 [RQ.SRS-032.ClickHouse.Parquet.Import.SkipColumns](#rqsrs-032clickhouseparquetimportskipcolumns)
    * 8.9 [Skip Values](#skip-values)
        * 8.9.1 [RQ.SRS-032.ClickHouse.Parquet.Import.SkipValues](#rqsrs-032clickhouseparquetimportskipvalues)
    * 8.10 [Auto Typecast](#auto-typecast)
        * 8.10.1 [RQ.SRS-032.ClickHouse.Parquet.Import.AutoTypecast](#rqsrs-032clickhouseparquetimportautotypecast)
    * 8.11 [Row Group Size](#row-group-size)
        * 8.11.1 [RQ.SRS-032.ClickHouse.Parquet.Import.RowGroupSize](#rqsrs-032clickhouseparquetimportrowgroupsize)
    * 8.12 [Data Page Size](#data-page-size)
        * 8.12.1 [RQ.SRS-032.ClickHouse.Parquet.Import.DataPageSize](#rqsrs-032clickhouseparquetimportdatapagesize)
    * 8.13 [Import Into New Table](#import-into-new-table)
        * 8.13.1 [RQ.SRS-032.ClickHouse.Parquet.Import.NewTable](#rqsrs-032clickhouseparquetimportnewtable)
    * 8.14 [Performance](#performance)
        * 8.14.1 [RQ.SRS-032.ClickHouse.Parquet.Import.Performance.CountFromMetadata](#rqsrs-032clickhouseparquetimportperformancecountfrommetadata)
        * 8.14.2 [RQ.SRS-032.ClickHouse.Parquet.Import.Performance.ParallelProcessing](#rqsrs-032clickhouseparquetimportperformanceparallelprocessing)
    * 8.15 [Import Nested Types](#import-nested-types)
        * 8.15.1 [RQ.SRS-032.ClickHouse.Parquet.Import.Nested.ArrayIntoNested](#rqsrs-032clickhouseparquetimportnestedarrayintonested)
        * 8.15.2 [RQ.SRS-032.ClickHouse.Parquet.Import.Nested.Complex](#rqsrs-032clickhouseparquetimportnestedcomplex)
        * 8.15.3 [RQ.SRS-032.ClickHouse.Parquet.Import.Nested.ArrayIntoNested.ImportNested](#rqsrs-032clickhouseparquetimportnestedarrayintonestedimportnested)
        * 8.15.4 [RQ.SRS-032.ClickHouse.Parquet.Import.Nested.ArrayIntoNested.NotImportNested](#rqsrs-032clickhouseparquetimportnestedarrayintonestednotimportnested)
        * 8.15.5 [RQ.SRS-032.ClickHouse.Parquet.Import.Nested.ArrayIntoNotNested](#rqsrs-032clickhouseparquetimportnestedarrayintonotnested)
        * 8.15.6 [RQ.SRS-032.ClickHouse.Parquet.Import.Nested.NonArrayIntoNested](#rqsrs-032clickhouseparquetimportnestednonarrayintonested)
    * 8.16 [Import Chunked Columns](#import-chunked-columns)
        * 8.16.1 [RQ.SRS-032.ClickHouse.Parquet.Import.ChunkedColumns](#rqsrs-032clickhouseparquetimportchunkedcolumns)
    * 8.17 [Import Encoded](#import-encoded)
        * 8.17.1 [Plain (Import)](#plain-import)
            * 8.17.1.1 [RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.Plain](#rqsrs-032clickhouseparquetimportencodingplain)
        * 8.17.2 [Dictionary (Import)](#dictionary-import)
            * 8.17.2.1 [RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.Dictionary](#rqsrs-032clickhouseparquetimportencodingdictionary)
        * 8.17.3 [Run Length Encoding (Import)](#run-length-encoding-import)
            * 8.17.3.1 [RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.RunLength](#rqsrs-032clickhouseparquetimportencodingrunlength)
        * 8.17.4 [Delta (Import)](#delta-import)
            * 8.17.4.1 [RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.Delta](#rqsrs-032clickhouseparquetimportencodingdelta)
        * 8.17.5 [Delta-length byte array (Import)](#delta-length-byte-array-import)
            * 8.17.5.1 [RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.DeltaLengthByteArray](#rqsrs-032clickhouseparquetimportencodingdeltalengthbytearray)
        * 8.17.6 [Delta Strings (Import)](#delta-strings-import)
            * 8.17.6.1 [RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.DeltaStrings](#rqsrs-032clickhouseparquetimportencodingdeltastrings)
        * 8.17.7 [Byte Stream Split (Import)](#byte-stream-split-import)
            * 8.17.7.1 [RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.ByteStreamSplit](#rqsrs-032clickhouseparquetimportencodingbytestreamsplit)
    * 8.18 [Import Settings](#import-settings)
        * 8.18.1 [RQ.SRS-032.ClickHouse.Parquet.Import.Settings.ImportNested](#rqsrs-032clickhouseparquetimportsettingsimportnested)
        * 8.18.2 [RQ.SRS-032.ClickHouse.Parquet.Import.Settings.CaseInsensitiveColumnMatching](#rqsrs-032clickhouseparquetimportsettingscaseinsensitivecolumnmatching)
        * 8.18.3 [RQ.SRS-032.ClickHouse.Parquet.Import.Settings.AllowMissingColumns](#rqsrs-032clickhouseparquetimportsettingsallowmissingcolumns)
        * 8.18.4 [RQ.SRS-032.ClickHouse.Parquet.Import.Settings.SkipColumnsWithUnsupportedTypesInSchemaInference](#rqsrs-032clickhouseparquetimportsettingsskipcolumnswithunsupportedtypesinschemainference)
    * 8.19 [Libraries](#libraries)
        * 8.19.1 [RQ.SRS-032.ClickHouse.Parquet.Libraries](#rqsrs-032clickhouseparquetlibraries)
        * 8.19.2 [Pyarrow](#pyarrow)
            * 8.19.2.1 [RQ.SRS-032.ClickHouse.Parquet.Libraries.Pyarrow](#rqsrs-032clickhouseparquetlibrariespyarrow)
        * 8.19.3 [PySpark](#pyspark)
            * 8.19.3.1 [RQ.SRS-032.ClickHouse.Parquet.Libraries.PySpark](#rqsrs-032clickhouseparquetlibrariespyspark)
        * 8.19.4 [Pandas](#pandas)
            * 8.19.4.1 [RQ.SRS-032.ClickHouse.Parquet.Libraries.Pandas](#rqsrs-032clickhouseparquetlibrariespandas)
        * 8.19.5 [parquet-go](#parquet-go)
            * 8.19.5.1 [RQ.SRS-032.ClickHouse.Parquet.Libraries.ParquetGO](#rqsrs-032clickhouseparquetlibrariesparquetgo)
        * 8.19.6 [H2OAI](#h2oai)
            * 8.19.6.1 [RQ.SRS-032.ClickHouse.Parquet.Libraries.H2OAI](#rqsrs-032clickhouseparquetlibrariesh2oai)
* 9 [Export from Parquet Files](#export-from-parquet-files)
        * 9.19.1 [RQ.SRS-032.ClickHouse.Parquet.Export](#rqsrs-032clickhouseparquetexport)
        * 9.19.2 [Auto Detect Parquet File When Exporting](#auto-detect-parquet-file-when-exporting)
            * 9.19.2.1 [RQ.SRS-032.ClickHouse.Parquet.Export.Outfile.AutoDetectParquetFileFormat](#rqsrs-032clickhouseparquetexportoutfileautodetectparquetfileformat)
    * 9.20 [Supported Data types](#supported-data-types)
        * 9.20.1 [RQ.SRS-032.ClickHouse.Parquet.Export.Datatypes.Supported](#rqsrs-032clickhouseparquetexportdatatypessupported)
        * 9.20.2 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.BLOB](#rqsrs-032clickhouseparquetexportdatatypessupportedblob)
        * 9.20.3 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.BOOL](#rqsrs-032clickhouseparquetexportdatatypessupportedbool)
        * 9.20.4 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.UINT8](#rqsrs-032clickhouseparquetexportdatatypessupporteduint8)
        * 9.20.5 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.INT8](#rqsrs-032clickhouseparquetexportdatatypessupportedint8)
        * 9.20.6 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.UINT16](#rqsrs-032clickhouseparquetexportdatatypessupporteduint16)
        * 9.20.7 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.INT16](#rqsrs-032clickhouseparquetexportdatatypessupportedint16)
        * 9.20.8 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.UINT32](#rqsrs-032clickhouseparquetexportdatatypessupporteduint32)
        * 9.20.9 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.INT32](#rqsrs-032clickhouseparquetexportdatatypessupportedint32)
        * 9.20.10 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.UINT64](#rqsrs-032clickhouseparquetexportdatatypessupporteduint64)
        * 9.20.11 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.INT64](#rqsrs-032clickhouseparquetexportdatatypessupportedint64)
        * 9.20.12 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.FLOAT](#rqsrs-032clickhouseparquetexportdatatypessupportedfloat)
        * 9.20.13 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DOUBLE](#rqsrs-032clickhouseparquetexportdatatypessupporteddouble)
        * 9.20.14 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DATE](#rqsrs-032clickhouseparquetexportdatatypessupporteddate)
        * 9.20.15 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DATE.ms](#rqsrs-032clickhouseparquetexportdatatypessupporteddatems)
        * 9.20.16 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DATE.ns](#rqsrs-032clickhouseparquetexportdatatypessupporteddatens)
        * 9.20.17 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DATE.us](#rqsrs-032clickhouseparquetexportdatatypessupporteddateus)
        * 9.20.18 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.TIME.ms](#rqsrs-032clickhouseparquetexportdatatypessupportedtimems)
        * 9.20.19 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.TIMESTAMP.ms](#rqsrs-032clickhouseparquetexportdatatypessupportedtimestampms)
        * 9.20.20 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.TIMESTAMP.ns](#rqsrs-032clickhouseparquetexportdatatypessupportedtimestampns)
        * 9.20.21 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.TIMESTAMP.us](#rqsrs-032clickhouseparquetexportdatatypessupportedtimestampus)
        * 9.20.22 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.STRING](#rqsrs-032clickhouseparquetexportdatatypessupportedstring)
        * 9.20.23 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.BINARY](#rqsrs-032clickhouseparquetexportdatatypessupportedbinary)
        * 9.20.24 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.FixedLengthByteArray](#rqsrs-032clickhouseparquetexportdatatypessupportedfixedlengthbytearray)
        * 9.20.25 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DECIMAL](#rqsrs-032clickhouseparquetexportdatatypessupporteddecimal)
        * 9.20.26 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DECIMAL.Filter](#rqsrs-032clickhouseparquetexportdatatypessupporteddecimalfilter)
        * 9.20.27 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.LIST](#rqsrs-032clickhouseparquetexportdatatypessupportedlist)
        * 9.20.28 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.ARRAY](#rqsrs-032clickhouseparquetexportdatatypessupportedarray)
        * 9.20.29 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.STRUCT](#rqsrs-032clickhouseparquetexportdatatypessupportedstruct)
        * 9.20.30 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.MAP](#rqsrs-032clickhouseparquetexportdatatypessupportedmap)
        * 9.20.31 [RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Nullable](#rqsrs-032clickhouseparquetexportdatatypesnullable)
    * 9.21 [Working With Nested Types Export](#working-with-nested-types-export)
        * 9.21.1 [RQ.SRS-032.ClickHouse.Parquet.Export.Nested](#rqsrs-032clickhouseparquetexportnested)
        * 9.21.2 [RQ.SRS-032.ClickHouse.Parquet.Export.Nested.Complex](#rqsrs-032clickhouseparquetexportnestedcomplex)
    * 9.22 [Exporting Chunked Columns](#exporting-chunked-columns)
        * 9.22.1 [RQ.SRS-032.ClickHouse.Parquet.Export.ChunkedColumns](#rqsrs-032clickhouseparquetexportchunkedcolumns)
    * 9.23 [Query Types](#query-types)
        * 9.23.1 [JOIN](#join)
            * 9.23.1.1 [RQ.SRS-032.ClickHouse.Export.Parquet.Join](#rqsrs-032clickhouseexportparquetjoin)
        * 9.23.2 [UNION](#union)
            * 9.23.2.1 [RQ.SRS-032.ClickHouse.Parquet.Export.Union](#rqsrs-032clickhouseparquetexportunion)
            * 9.23.2.2 [RQ.SRS-032.ClickHouse.Parquet.Export.Union.Multiple](#rqsrs-032clickhouseparquetexportunionmultiple)
        * 9.23.3 [RQ.SRS-032.ClickHouse.Parquet.Export.View](#rqsrs-032clickhouseparquetexportview)
        * 9.23.4 [RQ.SRS-032.ClickHouse.Parquet.Export.Select.MaterializedView](#rqsrs-032clickhouseparquetexportselectmaterializedview)
    * 9.24 [Export Encoded](#export-encoded)
        * 9.24.1 [Plain (Export)](#plain-export)
            * 9.24.1.1 [RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.Plain](#rqsrs-032clickhouseparquetexportencodingplain)
        * 9.24.2 [Dictionary (Export)](#dictionary-export)
            * 9.24.2.1 [RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.Dictionary](#rqsrs-032clickhouseparquetexportencodingdictionary)
        * 9.24.3 [Run Length Encoding (Export)](#run-length-encoding-export)
            * 9.24.3.1 [RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.RunLength](#rqsrs-032clickhouseparquetexportencodingrunlength)
        * 9.24.4 [Delta (Export)](#delta-export)
            * 9.24.4.1 [RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.Delta](#rqsrs-032clickhouseparquetexportencodingdelta)
        * 9.24.5 [Delta-length byte array (Export)](#delta-length-byte-array-export)
            * 9.24.5.1 [RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.DeltaLengthByteArray](#rqsrs-032clickhouseparquetexportencodingdeltalengthbytearray)
        * 9.24.6 [Delta Strings (Export)](#delta-strings-export)
            * 9.24.6.1 [RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.DeltaStrings](#rqsrs-032clickhouseparquetexportencodingdeltastrings)
        * 9.24.7 [Byte Stream Split (Export)](#byte-stream-split-export)
            * 9.24.7.1 [RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.ByteStreamSplit](#rqsrs-032clickhouseparquetexportencodingbytestreamsplit)
    * 9.25 [Export Settings](#export-settings)
        * 9.25.1 [RQ.SRS-032.ClickHouse.Parquet.Export.Settings.RowGroupSize](#rqsrs-032clickhouseparquetexportsettingsrowgroupsize)
        * 9.25.2 [RQ.SRS-032.ClickHouse.Parquet.Export.Settings.StringAsString](#rqsrs-032clickhouseparquetexportsettingsstringasstring)
        * 9.25.3 [RQ.SRS-032.ClickHouse.Parquet.Export.Settings.StringAsFixedByteArray](#rqsrs-032clickhouseparquetexportsettingsstringasfixedbytearray)
        * 9.25.4 [RQ.SRS-032.ClickHouse.Parquet.Export.Settings.ParquetVersion](#rqsrs-032clickhouseparquetexportsettingsparquetversion)
        * 9.25.5 [RQ.SRS-032.ClickHouse.Parquet.Export.Settings.CompressionMethod](#rqsrs-032clickhouseparquetexportsettingscompressionmethod)
    * 9.26 [Type Conversion](#type-conversion)
        * 9.26.1 [RQ.SRS-032.ClickHouse.Parquet.DataTypes.TypeConversionFunction](#rqsrs-032clickhouseparquetdatatypestypeconversionfunction)
* 10 [Hive Partitioning](#hive-partitioning)
    * 10.1 [RQ.SRS-032.ClickHouse.Parquet.Hive](#rqsrs-032clickhouseparquethive)
* 11 [Parquet Encryption](#parquet-encryption)
    * 11.1 [File Encryption](#file-encryption)
        * 11.1.1 [RQ.SRS-032.ClickHouse.Parquet.Encryption.File](#rqsrs-032clickhouseparquetencryptionfile)
    * 11.2 [Column Encryption](#column-encryption)
        * 11.2.1 [RQ.SRS-032.ClickHouse.Parquet.Encryption.Column.Modular](#rqsrs-032clickhouseparquetencryptioncolumnmodular)
        * 11.2.2 [RQ.SRS-032.ClickHouse.Parquet.Encryption.Column.Keys](#rqsrs-032clickhouseparquetencryptioncolumnkeys)
    * 11.3 [Encryption Algorithms](#encryption-algorithms)
        * 11.3.1 [RQ.SRS-032.ClickHouse.Parquet.Encryption.Algorithms.AESGCM](#rqsrs-032clickhouseparquetencryptionalgorithmsaesgcm)
        * 11.3.2 [RQ.SRS-032.ClickHouse.Parquet.Encryption.Algorithms.AESGCMCTR](#rqsrs-032clickhouseparquetencryptionalgorithmsaesgcmctr)
    * 11.4 [EncryptionParameters](#encryptionparameters)
        * 11.4.1 [RQ.SRS-032.ClickHouse.Parquet.Encryption.Parameters](#rqsrs-032clickhouseparquetencryptionparameters)
            * 11.4.1.1 [RQ.SRS-032.ClickHouse.Parquet.Encryption.Parameters.Algorythm](#rqsrs-032clickhouseparquetencryptionparametersalgorythm)
            * 11.4.1.2 [RQ.SRS-032.ClickHouse.Parquet.Encryption.Parameters.Plaintext.Footer](#rqsrs-032clickhouseparquetencryptionparametersplaintextfooter)
* 12 [DESCRIBE Parquet](#describe-parquet)
    * 12.1 [RQ.SRS-032.ClickHouse.Parquet.Structure](#rqsrs-032clickhouseparquetstructure)
* 13 [Compression](#compression)
    * 13.1 [None](#none)
        * 13.1.1 [RQ.SRS-032.ClickHouse.Parquet.Compression.None](#rqsrs-032clickhouseparquetcompressionnone)
    * 13.2 [Gzip](#gzip)
        * 13.2.1 [RQ.SRS-032.ClickHouse.Parquet.Compression.Gzip](#rqsrs-032clickhouseparquetcompressiongzip)
    * 13.3 [Brotli](#brotli)
        * 13.3.1 [RQ.SRS-032.ClickHouse.Parquet.Compression.Brotli](#rqsrs-032clickhouseparquetcompressionbrotli)
    * 13.4 [Lz4](#lz4)
        * 13.4.1 [RQ.SRS-032.ClickHouse.Parquet.Compression.Lz4](#rqsrs-032clickhouseparquetcompressionlz4)
    * 13.5 [Lz4Raw](#lz4raw)
        * 13.5.1 [RQ.SRS-032.ClickHouse.Parquet.Compression.Lz4Raw](#rqsrs-032clickhouseparquetcompressionlz4raw)
    * 13.6 [Lz4Hadoop](#lz4hadoop)
        * 13.6.1 [RQ.SRS-032.ClickHouse.Parquet.Compression.Lz4Hadoop](#rqsrs-032clickhouseparquetcompressionlz4hadoop)
    * 13.7 [Snappy](#snappy)
        * 13.7.1 [RQ.SRS-032.ClickHouse.Parquet.Compression.Snappy](#rqsrs-032clickhouseparquetcompressionsnappy)
    * 13.8 [Zstd](#zstd)
        * 13.8.1 [RQ.SRS-032.ClickHouse.Parquet.Compression.Zstd](#rqsrs-032clickhouseparquetcompressionzstd)
    * 13.9 [Unsupported Compression](#unsupported-compression)
        * 13.9.1 [Lzo](#lzo)
            * 13.9.1.1 [RQ.SRS-032.ClickHouse.Parquet.UnsupportedCompression.Lzo](#rqsrs-032clickhouseparquetunsupportedcompressionlzo)
* 14 [Table Functions](#table-functions)
    * 14.1 [URL](#url)
        * 14.1.1 [RQ.SRS-032.ClickHouse.Parquet.TableFunctions.URL](#rqsrs-032clickhouseparquettablefunctionsurl)
    * 14.2 [File](#file)
        * 14.2.1 [RQ.SRS-032.ClickHouse.Parquet.TableFunctions.File](#rqsrs-032clickhouseparquettablefunctionsfile)
        * 14.2.2 [RQ.SRS-032.ClickHouse.Parquet.TableFunctions.File.AutoDetectParquetFileFormat](#rqsrs-032clickhouseparquettablefunctionsfileautodetectparquetfileformat)
    * 14.3 [S3](#s3)
        * 14.3.1 [RQ.SRS-032.ClickHouse.Parquet.TableFunctions.S3](#rqsrs-032clickhouseparquettablefunctionss3)
    * 14.4 [JDBC](#jdbc)
        * 14.4.1 [RQ.SRS-032.ClickHouse.Parquet.TableFunctions.JDBC](#rqsrs-032clickhouseparquettablefunctionsjdbc)
    * 14.5 [ODBC](#odbc)
        * 14.5.1 [RQ.SRS-032.ClickHouse.Parquet.TableFunctions.ODBC](#rqsrs-032clickhouseparquettablefunctionsodbc)
    * 14.6 [HDFS](#hdfs)
        * 14.6.1 [RQ.SRS-032.ClickHouse.Parquet.TableFunctions.HDFS](#rqsrs-032clickhouseparquettablefunctionshdfs)
    * 14.7 [Remote](#remote)
        * 14.7.1 [RQ.SRS-032.ClickHouse.Parquet.TableFunctions.Remote](#rqsrs-032clickhouseparquettablefunctionsremote)
    * 14.8 [MySQL](#mysql)
        * 14.8.1 [RQ.SRS-032.ClickHouse.Parquet.TableFunctions.MySQL](#rqsrs-032clickhouseparquettablefunctionsmysql)
    * 14.9 [PostgreSQL](#postgresql)
        * 14.9.1 [RQ.SRS-032.ClickHouse.Parquet.TableFunctions.PostgreSQL](#rqsrs-032clickhouseparquettablefunctionspostgresql)
* 15 [Table Engines](#table-engines)
    * 15.1 [Readable External Table](#readable-external-table)
        * 15.1.1 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.ReadableExternalTable](#rqsrs-032clickhouseparquettableenginesreadableexternaltable)
    * 15.2 [MergeTree](#mergetree)
        * 15.2.1 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.MergeTree](#rqsrs-032clickhouseparquettableenginesmergetreemergetree)
        * 15.2.2 [ReplicatedMergeTree](#replicatedmergetree)
            * 15.2.2.1 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.ReplicatedMergeTree](#rqsrs-032clickhouseparquettableenginesmergetreereplicatedmergetree)
        * 15.2.3 [ReplacingMergeTree](#replacingmergetree)
            * 15.2.3.1 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.ReplacingMergeTree](#rqsrs-032clickhouseparquettableenginesmergetreereplacingmergetree)
        * 15.2.4 [SummingMergeTree](#summingmergetree)
            * 15.2.4.1 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.SummingMergeTree](#rqsrs-032clickhouseparquettableenginesmergetreesummingmergetree)
        * 15.2.5 [AggregatingMergeTree](#aggregatingmergetree)
            * 15.2.5.1 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.AggregatingMergeTree](#rqsrs-032clickhouseparquettableenginesmergetreeaggregatingmergetree)
        * 15.2.6 [CollapsingMergeTree](#collapsingmergetree)
            * 15.2.6.1 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.CollapsingMergeTree](#rqsrs-032clickhouseparquettableenginesmergetreecollapsingmergetree)
        * 15.2.7 [VersionedCollapsingMergeTree](#versionedcollapsingmergetree)
            * 15.2.7.1 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.VersionedCollapsingMergeTree](#rqsrs-032clickhouseparquettableenginesmergetreeversionedcollapsingmergetree)
        * 15.2.8 [GraphiteMergeTree](#graphitemergetree)
            * 15.2.8.1 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.GraphiteMergeTree](#rqsrs-032clickhouseparquettableenginesmergetreegraphitemergetree)
    * 15.3 [Integration Engines](#integration-engines)
        * 15.3.1 [ODBC Engine](#odbc-engine)
            * 15.3.1.1 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.ODBC](#rqsrs-032clickhouseparquettableenginesintegrationodbc)
        * 15.3.2 [JDBC Engine](#jdbc-engine)
            * 15.3.2.1 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.JDBC](#rqsrs-032clickhouseparquettableenginesintegrationjdbc)
        * 15.3.3 [MySQL Engine](#mysql-engine)
            * 15.3.3.1 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.MySQL](#rqsrs-032clickhouseparquettableenginesintegrationmysql)
        * 15.3.4 [MongoDB Engine](#mongodb-engine)
            * 15.3.4.1 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.MongoDB](#rqsrs-032clickhouseparquettableenginesintegrationmongodb)
        * 15.3.5 [HDFS Engine](#hdfs-engine)
            * 15.3.5.1 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.HDFS](#rqsrs-032clickhouseparquettableenginesintegrationhdfs)
        * 15.3.6 [S3 Engine](#s3-engine)
            * 15.3.6.1 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.S3](#rqsrs-032clickhouseparquettableenginesintegrations3)
        * 15.3.7 [Kafka Engine](#kafka-engine)
            * 15.3.7.1 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.Kafka](#rqsrs-032clickhouseparquettableenginesintegrationkafka)
        * 15.3.8 [EmbeddedRocksDB Engine](#embeddedrocksdb-engine)
            * 15.3.8.1 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.EmbeddedRocksDB](#rqsrs-032clickhouseparquettableenginesintegrationembeddedrocksdb)
        * 15.3.9 [PostgreSQL Engine](#postgresql-engine)
            * 15.3.9.1 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.PostgreSQL](#rqsrs-032clickhouseparquettableenginesintegrationpostgresql)
    * 15.4 [Special Engines](#special-engines)
        * 15.4.1 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.Memory](#rqsrs-032clickhouseparquettableenginesspecialmemory)
        * 15.4.2 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.Distributed](#rqsrs-032clickhouseparquettableenginesspecialdistributed)
        * 15.4.3 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.Dictionary](#rqsrs-032clickhouseparquettableenginesspecialdictionary)
        * 15.4.4 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.File](#rqsrs-032clickhouseparquettableenginesspecialfile)
        * 15.4.5 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.URL](#rqsrs-032clickhouseparquettableenginesspecialurl)
* 16 [Indexes](#indexes)
    * 16.1 [RQ.SRS-032.ClickHouse.Parquet.Indexes](#rqsrs-032clickhouseparquetindexes)
    * 16.2 [Page](#page)
        * 16.2.1 [RQ.SRS-032.ClickHouse.Parquet.Indexes.Page](#rqsrs-032clickhouseparquetindexespage)
    * 16.3 [Bloom Filter](#bloom-filter)
        * 16.3.1 [RQ.SRS-032.ClickHouse.Parquet.Indexes.BloomFilter](#rqsrs-032clickhouseparquetindexesbloomfilter)
    * 16.4 [Dictionary](#dictionary)
        * 16.4.1 [RQ.SRS-032.ClickHouse.Parquet.Indexes.Dictionary](#rqsrs-032clickhouseparquetindexesdictionary)
* 17 [Metadata](#metadata)
    * 17.1 [ParquetFormat](#parquetformat)
        * 17.1.1 [RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadataFormat](#rqsrs-032clickhouseparquetmetadataparquetmetadataformat)
        * 17.1.2 [RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadataFormat.Output](#rqsrs-032clickhouseparquetmetadataparquetmetadataformatoutput)
        * 17.1.3 [RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadata.Content](#rqsrs-032clickhouseparquetmetadataparquetmetadatacontent)
        * 17.1.4 [RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadata.MinMax](#rqsrs-032clickhouseparquetmetadataparquetmetadataminmax)
    * 17.2 [Metadata Types](#metadata-types)
        * 17.2.1 [RQ.SRS-032.ClickHouse.Parquet.Metadata.File](#rqsrs-032clickhouseparquetmetadatafile)
        * 17.2.2 [RQ.SRS-032.ClickHouse.Parquet.Metadata.Column](#rqsrs-032clickhouseparquetmetadatacolumn)
        * 17.2.3 [RQ.SRS-032.ClickHouse.Parquet.Metadata.Header](#rqsrs-032clickhouseparquetmetadataheader)
* 18 [Error Recovery](#error-recovery)
    * 18.1 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Metadata.MagicNumber](#rqsrs-032clickhouseparqueterrorrecoverycorruptmetadatamagicnumber)
    * 18.2 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Metadata.File](#rqsrs-032clickhouseparqueterrorrecoverycorruptmetadatafile)
    * 18.3 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Metadata.Column](#rqsrs-032clickhouseparqueterrorrecoverycorruptmetadatacolumn)
    * 18.4 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Metadata.PageHeader](#rqsrs-032clickhouseparqueterrorrecoverycorruptmetadatapageheader)
    * 18.5 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Metadata.PageData](#rqsrs-032clickhouseparqueterrorrecoverycorruptmetadatapagedata)
    * 18.6 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Metadata.Checksum](#rqsrs-032clickhouseparqueterrorrecoverycorruptmetadatachecksum)
    * 18.7 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values](#rqsrs-032clickhouseparqueterrorrecoverycorruptvalues)
        * 18.7.1 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Date](#rqsrs-032clickhouseparqueterrorrecoverycorruptvaluesdate)
        * 18.7.2 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Int](#rqsrs-032clickhouseparqueterrorrecoverycorruptvaluesint)
        * 18.7.3 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.BigInt](#rqsrs-032clickhouseparqueterrorrecoverycorruptvaluesbigint)
        * 18.7.4 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.SmallInt](#rqsrs-032clickhouseparqueterrorrecoverycorruptvaluessmallint)
        * 18.7.5 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.TinyInt](#rqsrs-032clickhouseparqueterrorrecoverycorruptvaluestinyint)
        * 18.7.6 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.UInt](#rqsrs-032clickhouseparqueterrorrecoverycorruptvaluesuint)
        * 18.7.7 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.UBigInt](#rqsrs-032clickhouseparqueterrorrecoverycorruptvaluesubigint)
        * 18.7.8 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.USmallInt](#rqsrs-032clickhouseparqueterrorrecoverycorruptvaluesusmallint)
        * 18.7.9 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.UTinyInt](#rqsrs-032clickhouseparqueterrorrecoverycorruptvaluesutinyint)
        * 18.7.10 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.TimestampUS](#rqsrs-032clickhouseparqueterrorrecoverycorruptvaluestimestampus)
        * 18.7.11 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.TimestampMS](#rqsrs-032clickhouseparqueterrorrecoverycorruptvaluestimestampms)
        * 18.7.12 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Bool](#rqsrs-032clickhouseparqueterrorrecoverycorruptvaluesbool)
        * 18.7.13 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Float](#rqsrs-032clickhouseparqueterrorrecoverycorruptvaluesfloat)
        * 18.7.14 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Double](#rqsrs-032clickhouseparqueterrorrecoverycorruptvaluesdouble)
        * 18.7.15 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.TimeMS](#rqsrs-032clickhouseparqueterrorrecoverycorruptvaluestimems)
        * 18.7.16 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.TimeUS](#rqsrs-032clickhouseparqueterrorrecoverycorruptvaluestimeus)
        * 18.7.17 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.TimeNS](#rqsrs-032clickhouseparqueterrorrecoverycorruptvaluestimens)
        * 18.7.18 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.String](#rqsrs-032clickhouseparqueterrorrecoverycorruptvaluesstring)
        * 18.7.19 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Binary](#rqsrs-032clickhouseparqueterrorrecoverycorruptvaluesbinary)
        * 18.7.20 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.FixedLengthByteArray](#rqsrs-032clickhouseparqueterrorrecoverycorruptvaluesfixedlengthbytearray)
        * 18.7.21 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Decimal](#rqsrs-032clickhouseparqueterrorrecoverycorruptvaluesdecimal)
        * 18.7.22 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.List](#rqsrs-032clickhouseparqueterrorrecoverycorruptvalueslist)
        * 18.7.23 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Struct](#rqsrs-032clickhouseparqueterrorrecoverycorruptvaluesstruct)
        * 18.7.24 [RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Map](#rqsrs-032clickhouseparqueterrorrecoverycorruptvaluesmap)
* 19 [Interoperability Between ARM and x86](#interoperability-between-arm-and-x86)
    * 19.1 [Importing and Exporting Parquet Files On ARM That Were Generated On x86 Machine](#importing-and-exporting-parquet-files-on-arm-that-were-generated-on-x86-machine)
        * 19.1.1 [RQ.SRS-032.ClickHouse.Parquet.Interoperability.From.x86.To.ARM](#rqsrs-032clickhouseparquetinteroperabilityfromx86toarm)
    * 19.2 [Importing and Exporting Parquet Files On x86 That Were Generated On ARM Machine](#importing-and-exporting-parquet-files-on-x86-that-were-generated-on-arm-machine)
        * 19.2.1 [RQ.SRS-032.ClickHouse.Parquet.Interoperability.From.ARM.To.x86](#rqsrs-032clickhouseparquetinteroperabilityfromarmtox86)


## Revision History

This document is stored in an electronic form using [Git] source control management software
hosted in a [GitHub Repository].
All the updates are tracked using the [Revision History].

## Introduction

This software requirements specification covers requirements for `Parquet` data format in [ClickHouse].

The documentation used:
- https://clickhouse.com/docs/en/operations/settings/formats#parquet-format-settings
- https://clickhouse.com/docs/en/interfaces/formats#data-format-parquet
- https://clickhouse.com/docs/en/integrations/data-formats/parquet#importing-from-parquet
- https://parquet.apache.org/docs/

## Feature Diagram

```mermaid
flowchart TB;
    subgraph Overhead[Parquet]
        direction TB;
        subgraph Sources[Source of data]
            direction TB;   
            MySQL
            DuckDB

            subgraph Libraries[Parquet Libraries]
                direction LR;
                parquet-tools
                pyarrow
                parquet-cpp
                parquet-mr
                fastparquet
                pyspark
            end

            subgraph ClickHouse_source[ClickHouse]
                style ClickHouse_source fill:#fcbb30
                direction TB;   
                subgraph Select_query[SELECT]
                    style Select_query fill:#d9ead3
                    direction LR;
                    subgraph Select_sources[Sources]
                        direction TB;
                        subgraph Funcs_sel[Functions]
                            direction LR;
                            URL_func_sel[URL]
                            File_func_sel[FILE]
                            Query_func_sel[Query]
                            S3_func_sel[S3]
                            jdbc_func_sel[JDBC]
                            odbc_func_sel[ODBC]
                            hdfs_func_sel[HDFS]
                            remote_func_sel[Remote]
                            mysql_func_sel[MySQL]
                            postgresql_func_sel[PostgreSQL]
                        end

                        subgraph Integration_Engines_sel[Integration Engines]
                            direction LR;
                            ODBC_eng_sel[ODBC]
                            jdbc_eng_sel[JDBC]
                            mysql_eng_sel[MySQL]
                            mongodb_eng_sel[MongoDB]
                            hdfs_eng_sel[HDFS]
                            s3_eng_sel[S3]
                            kafka_eng_sel[Kafka]
                            embeddedrocksDB_eng_sel[EmbeddedRocksDB]
                            RabbitMQ_eng_sel[RabbitMQ]
                            PostgreSQL_eng_sel[PostgreSQL]
                        end

                        subgraph Special_Engines_sel[Special Engines]
                            direction LR;
                            distributed_eng_sel[Distributed]
                            dictionary_eng_sel[Dictionary]
                            file_eng_sel[File]
                            url_eng_sel[URL]
                            mat_view_sel[Materialized View]
                            merge_sel[Merge]
                            join_sel[Join]
                            view_sel[View]
                            memory_sel[Memory]
                            buffer_sel[Buffer]
                        end
                    end

                    subgraph Select_opt[Clauses]
                        JOIN_clause[JOIN]
                        Union_clause[UNION]
                    end
                end

                subgraph ClickHouse_write_direct[Writing into file directly]
                    direction LR;
                    s3_tb_write[S3 table function]
                    s3_en_write[S3 engine]
                    file_tb_write[File table function]
                    file_en_write[File engine]
                    hdfs_tb_write[HDFS table function]
                    hdfs_en_write[HDFS engine]
                    url_tb_write[URL table function]
                    url_en_write[URL engine]
                end
            end
        end

        subgraph Input_settings[Input settings]
            direction LR
            input_format_parquet_import_nested
            input_format_parquet_case_insensitive_column_matching
            input_format_parquet_allow_missing_columns
            input_format_parquet_skip_columns_with_unsupported_types_in_schema_inference 
        end

        subgraph Output_settings[Output settings]
            direction LR
            output_format_parquet_row_group_size
            output_format_parquet_string_as_string
            output_format_parquet_fixed_string_as_fixed_byte_array
            output_format_parquet_version
            output_format_parquet_compression_method
        end

        subgraph Compression
            direction TB
            Uncompressed
            Snappy
            Gzip
            LZO
            Brotli
            LZ4
            ZSTD
            LZ4_RAW
        end

        subgraph Encryption
            direction LR
            AesGcmV1
            AesGcmCtrV1
        end

        subgraph Corrupted
            direction LR
            CorruptedYes[Yes]
            CorruptedNo[No]
        end

        subgraph Possible_Corruptions[Possible Corruptions]
            direction LR
            CorruptFile[Corrupt File]
            CorruptColumn[Corrupted Column]
            CorruptPageHeader[Corrupt Page Header]
            CorruptPageData[Corrupted Page Data]
            CorruptColumnValues[Corrupted Column Values]
        end

        subgraph Error
            direction LR
            Error_message[File is not inserted into ClickHouse. Error Message Is Shown.]
        end

        subgraph ClickHouse[ClickHouse]
            style ClickHouse fill:#fcbb30
            direction TB;
            subgraph Insert_query[INSERT Targets]
                style Insert_query fill:#ffb5b5
                direction TB;
                subgraph Funcs[Functions]
                    URL_func_in[URL]
                    File_func_in[FILE]
                    Query_func_in[Query]
                    S3_func_in[S3]
                    jdbc_func_in[JDBC]
                    odbc_func_in[ODBC]
                    hdfs_func_in[HDFS]
                    remote_func_in[Remote]
                    mysql_func_in[MySQL]
                    postgresql_func_in[PostgreSQL]
                end

                subgraph Integration_Engines[Integration Engines]
                    ODBC_eng[ODBC]
                    jdbc_eng[JDBC]
                    mysql_eng[MySQL]
                    mongodb_eng[MongoDB]
                    hdfs_eng[HDFS]
                    s3_eng[S3]
                    kafka_eng[Kafka]
                    embeddedrocksDB_eng[EmbeddedRocksDB]
                    RabbitMQ_eng[RabbitMQ]
                    PostgreSQL_eng[PostgreSQL]
                end

                subgraph Special_Engines[Special Engines]
                    distributed_eng[Distributed]
                    dictionary_eng[Dictionary]
                    file_eng[File]
                    url_eng[URL]
                    merge[Merge]
                    join[Join]
                    memory[Memory]
                    buffer[Buffer]
                end

            end
            subgraph ClickHouse_read_direct[Reading from file directly]
                s3_tb_read[S3 table function]
                s3_en_read[S3 engine]
                file_tb_read[File table function]
                file_en_read[File engine]
                hdfs_tb_read[HDFS table function]
                hdfs_en_read[HDFS engine]
                url_tb_read[URL table function]
                url_en_read[URL engine]
            end
        end

    Parquet_File_in[Parquet File]
    Parquet_File_out[Parquet File]

        subgraph PossibleCorruptions[Possible Corrupted Parquet Datatypes]
            direction LR;
                UInt8in[UInt8]
                Boolin[Bool]
                Int8in[Int8]
                UInt16in[UInt16]
                Int16in[Int16]
                UInt32in[UInt32]
                Int32in[Int32]
                UInt64in[UInt64]
                Int64in[Int64]
                Floatin[Float]
                HalfFloatin[Half Float]
                Doublein[Double]
                Date32in[Date32]
                Date64in[Date62]
                Timestampin[Timestamp]
                Stringin[String]
                Binaryin[Binary]
                Decimalin[Decimal]
                Listin[List]
                Structin[Struct]
                Mapin[Map]
            end

        subgraph TypeConversion[Parquet type > ClickHouse type > Parquet type]
            direction LR;
            subgraph Insert_types[Parquet]
                UInt8_in[UInt8]
                Bool_in[Bool]
                Int8_in[Int8]
                UInt16_in[UInt16]
                Int16_in[Int16]
                UInt32_in[UInt32]
                Int32_in[Int32]
                UInt64_in[UInt64]
                Int64_in[Int64]
                Float_in[Float]
                Half_Float_in[Half Float]
                Double_in[Double]
                Date32_in[Date32]
                Date64_in[Date62]
                Timestamp_in[Timestamp]
                String_in[String]
                Binary_in[Binary]
                Decimal_in[Decimal]
                List_in[List]
                Struct_in[Struct]
                Map_in[Map]
            end

            subgraph CH_types[ClickHouse]
                UInt8_ch[UInt8]
                Int8_ch[Int8]
                UInt16_ch[UInt16]
                Int16_ch[Int16]
                UInt32_ch[UInt32]
                Int32_ch[Int32]
                UInt64_ch[UInt64]
                Int64_ch[Int64]
                Float32_ch[Float32]
                Float64_ch[Float64]
                Date_ch[Date]
                DateTime_ch[DateTime]
                String_ch[String]
                FixedString_ch[FixedString]
                Decimal128_ch[Decimal128]
                Array_ch[Array]
                Tuple_ch[Tuple]
                Map_ch[Map]
            end

            subgraph Select_types[Parquet]
                UInt8_out[UInt8]
                Int8_out[Int8]
                UInt16_out[UInt16]
                Int16_out[Int16]
                UInt32_out[UInt32]
                Int32_out[Int32]
                UInt64_out[UInt64]
                Int64_out[Int64]
                Float_out[Float]
                Double_out[Double]
                Binary_out[Binary]
                Decimal_out[Decimal]
                List_out[List]
                Struct_out[Struct]
                Map_out[Map]
            end

            subgraph AutoConversions[Type Auto Conversion Based On The Target Table]
                direction LR
                Parquet_type[Parquet Datatype]
                ClickHouse_type[ClickHouse Datatype]
            end

            subgraph Modifiers[Supported Modifiers]
                direction LR
                Nullable
                LowCardinality
            end
        end
        subgraph Not_supported_by_ch[Parquet Types not supported by ClickHouse]
            direction LR
            Time32
            FIXED_SIZE_BINARY
            JSON
            UUID
            ENUM
            Chunked_arr[Chunked Array]
        end
    end


Sources --> Compression --> Encryption --> Parquet_File_in 
Parquet_File_in --> CorruptedYes
CorruptedYes --> Possible_Corruptions --> Error
Parquet_File_in --> CorruptedNo --Insert Into ClickHouse --> Input_settings --> ClickHouse -- Read From ClickHouse --> Output_settings --> Parquet_File_out
CorruptColumnValues --> PossibleCorruptions
ClickHouse_type --> Parquet_type --> ClickHouse_type


UInt8_in --> UInt8_ch --> UInt8_out
Bool_in --> UInt8_ch
Int8_in --> Int8_ch --> Int8_out
UInt16_in --> UInt16_ch --> UInt16_out
UInt32_in --> UInt32_ch --> UInt32_out
UInt64_in --> UInt64_ch --> UInt64_out
Int16_in --> Int16_ch --> Int16_out
Int32_in --> Int32_ch --> Int32_out
Int64_in --> Int64_ch --> Int64_out
Float_in --> Float32_ch --> Float_out
Half_Float_in --> Float32_ch
Double_in --> Float64_ch --> Double_out
Date32_in --> Date_ch --> UInt16_out
Date64_in --> DateTime_ch --> UInt32_out
Timestamp_in --> DateTime_ch
String_in --> String_ch --> Binary_out
Binary_in --> String_ch
Decimal_in --> Decimal128_ch --> Decimal_out
List_in --> Array_ch --> List_out
Struct_in --> Tuple_ch --> Struct_out
Map_in --> Map_ch --> Map_out
FixedString_ch --> Binary_out
```

## Working With Parquet

### RQ.SRS-032.ClickHouse.Parquet
version: 1.0

[ClickHouse] SHALL support `Parquet` data format.

## Supported Parquet Versions

### RQ.SRS-032.ClickHouse.Parquet.SupportedVersions
version: 1.0

[ClickHouse] SHALL support importing Parquet files with the following versions: `1.0.0`, `2.0.0`, `2.1.0`, `2.2.0`, `2.4.0`, `2.6.0`, `2.7.0`, `2.8.0`, `2.9.0`.

### RQ.SRS-032.ClickHouse.Parquet.ClickHouseLocal
version: 1.0

[ClickHouse] SHALL support the usage of `clickhouse-local` with `Parquet` data format.

## Offsets

### RQ.SRS-032.ClickHouse.Parquet.Offsets
version: 1.0

[ClickHouse] SHALL support importing and exporting parquet files with offsets.

#### RQ.SRS-032.ClickHouse.Parquet.Offsets.MonotonicallyIncreasing
version: 1.0

[ClickHouse] SHALL support importing and exporting parquet files with monotonically increasing offsets.

## Query Cache

### RQ.SRS-032.ClickHouse.Parquet.Query.Cache
version: 1.0

[ClickHouse] SHALL support using the query cache functionality when working with the Parquet files.

## Import from Parquet Files

### RQ.SRS-032.ClickHouse.Parquet.Import
version: 1.0

[ClickHouse] SHALL support using `INSERT` query with `FROM INFILE {file_name}` and `FORMAT Parquet` clauses to
read data from Parquet files and insert data into tables or table functions.

```sql
INSERT INTO sometable
FROM INFILE 'data.parquet' FORMAT Parquet;
```

### Auto Detect Parquet File When Importing

#### RQ.SRS-032.ClickHouse.Parquet.Import.AutoDetectParquetFileFormat
version: 1.0

[ClickHouse] SHALL support automatically detecting Parquet file format based on 
when using INFILE clause without explicitly specifying the format setting.

```sql
INSERT INTO sometable
FROM INFILE 'data.parquet';
```

### Glob Patterns

#### RQ.SRS-032.ClickHouse.Parquet.Import.Glob
version: 1.0

[ClickHouse] SHALL support using glob patterns in file paths to import multiple Parquet files.

> Multiple path components can have globs. For being processed file must exist and match to the whole path pattern (not only suffix or prefix).
>
>   - `*` — Substitutes any number of any characters except / including empty string.
>   - `?` — Substitutes any single character.
>   - `{some_string,another_string,yet_another_one}` — Substitutes any of strings 'some_string', 'another_string', 'yet_another_one'.
>   - `{N..M}` — Substitutes any number in range from N to M including both borders.
>   - `**` - Fetches all files inside the folder recursively.

#### RQ.SRS-032.ClickHouse.Parquet.Import.Glob.MultiDirectory
version: 1.0

[ClickHouse] SHALL support using `{str1, ...}` globs across different directories when importing from the Parquet files. 

For example,

> The following query will import both from a/1.parquet and b/2.parquet
> 
> ```sql
> SELECT
>     *,
>     _path,
>     _file
> FROM file('{a/1,b/2}.parquet', Parquet)
> ```

### Supported Datatypes

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Conversion
version: 1.0

[ClickHouse] SHALL support importing the Parquet files with the following datatypes and converting them into corresponding ClickHouse columns as described in the table.

The conversion MAY not be possible between some datatypes.
>
> For example,
>
> `Bool` -> `IPv6`

| Parquet to ClickHouse supported Datatypes     | ClickHouse Datatype Family        | alias_to Datatype | case_insensitive |
|-----------------------------------------------|-----------------------------------|-------------------|------------------|
|                                               | `JSON`                            |                   | 1                |
|                                               | `Polygon`                         |                   | 0                |
|                                               | `Ring`                            |                   | 0                |
|                                               | `Point`                           |                   | 0                |
|                                               | `SimpleAggregateFunction`         |                   | 0                |
|                                               | `IntervalQuarter`                 |                   | 0                |
|                                               | `IntervalMonth`                   |                   | 0                |
| `INT64`                                       | `Int64`                           |                   | 0                |
|                                               | `IntervalDay`                     |                   | 0                |
|                                               | `IntervalHour`                    |                   | 0                |
| `UINT32`                                      | `IPv4`                            |                   | 0                |
|                                               | `IntervalSecond`                  |                   | 0                |
|                                               | `LowCardinality`                  |                   | 0                |
| `INT16`                                       | `Int16`                           |                   | 0                |
| `FIXED_LENGTH_BYTE_ARRAY`, `BINARY`           | `UInt256`                         |                   | 0                |
|                                               | `AggregateFunction`               |                   | 0                |
|                                               | `MultiPolygon`                    |                   | 0                |
| `FIXED_LENGTH_BYTE_ARRAY`, `BINARY`           | `IPv6`                            |                   | 0                |
|                                               | `Nothing`                         |                   | 0                |
|                                               | `Decimal256`                      |                   | 1                |
| `STRUCT`                                      | `Tuple`                           |                   | 0                |
| `LIST`                                        | `Array`                           |                   | 0                |
|                                               | `IntervalMicrosecond`             |                   | 0                |
|                                               | `Bool`                            |                   | 1                |
| `INT16`                                       | `Enum16`                          |                   | 0                |
|                                               | `IntervalMinute`                  |                   | 0                |
|                                               | `FixedString`                     |                   | 0                |
| `STRING`, `BINARY`                            | `String`                          |                   | 0                |
| `TIME (ms)`                                   | `DateTime`                        |                   | 1                |
|                                               | `Object`                          |                   | 0                |
| `MAP`                                         | `Map`                             |                   | 0                |
|                                               | `UUID`                            |                   | 0                |
|                                               | `Decimal64`                       |                   | 1                |
|                                               | `Nullable`                        |                   | 0                |
|                                               | `Enum`                            |                   | 1                |
| `INT32`                                       | `Int32`                           |                   | 0                |
| `UINT8`, `BOOL`                               | `UInt8`                           |                   | 0                |
|                                               | `Date`                            |                   | 1                |
|                                               | `Decimal32`                       |                   | 1                |
| `FIXED_LENGTH_BYTE_ARRAY`, `BINARY`           | `UInt128`                         |                   | 0                |
| `DOUBLE`                                      | `Float64`                         |                   | 0                |
|                                               | `Nested`                          |                   | 0                |
| `UINT16`                                      | `UInt16`                          |                   | 0                |
|                                               | `IntervalMillisecond`             |                   | 0                |
| `FIXED_LENGTH_BYTE_ARRAY`, `BINARY`           | `Int128`                          |                   | 0                |
|                                               | `Decimal128`                      |                   | 1                |
| `INT8`                                        | `Int8`                            |                   | 0                |
| `DECIMAL`                                     | `Decimal`                         |                   | 1                |
| `FIXED_LENGTH_BYTE_ARRAY`, `BINARY`           | `Int256`                          |                   | 0                |
| `TIMESTAMP (ms, ns, us)`, `TIME (us, ns)`     | `DateTime64`                      |                   | 1                |
| `INT8`                                        | `Enum8`                           |                   | 0                |
|                                               | `DateTime32`                      |                   | 1                |
| `DATE (ms, ns, us)`                           | `Date32`                          |                   | 1                |
|                                               | `IntervalWeek`                    |                   | 0                |
| `UINT64`                                      | `UInt64`                          |                   | 0                |
|                                               | `IntervalNanosecond`              |                   | 0                |
|                                               | `IntervalYear`                    |                   | 0                |
| `UINT32`                                      | `UInt32`                          |                   | 0                |
| `FLOAT`                                       | `Float32`                         |                   | 0                |
| `BOOL`                                        | `bool`                            | `Bool`            | 1                |
| `FIXED_LENGTH_BYTE_ARRAY`, `BINARY`           | `INET6`                           | `IPv6`            | 1                |
| `UINT32`                                      | `INET4`                           | `IPv4`            | 1                |
|                                               | `ENUM`                            | `Enum`            | 1                |
| `STRING`, `BINARY`, `FIXED_LENGTH_BYTE_ARRAY` | `BINARY`                          | `FixedString`     | 1                |
| `STRING`, `BINARY`                            | `GEOMETRY`                        | `String`          | 1                |
| `STRING`, `BINARY`                            | `NATIONAL CHAR VARYING`           | `String`          | 1                |
| `STRING`, `BINARY`                            | `BINARY VARYING`                  | `String`          | 1                |
| `STRING`, `BINARY`                            | `NCHAR LARGE OBJECT`              | `String`          | 1                |
| `STRING`, `BINARY`                            | `NATIONAL CHARACTER VARYING`      | `String`          | 1                |
|                                               | `boolean`                         | `Bool`            | 1                |
| `STRING`, `BINARY`                            | `NATIONAL CHARACTER LARGE OBJECT` | `String`          | 1                |
| `STRING`, `BINARY`                            | `NATIONAL CHARACTER`              | `String`          | 1                |
| `STRING`, `BINARY`                            | `NATIONAL CHAR`                   | `String`          | 1                |
| `STRING`, `BINARY`                            | `CHARACTER VARYING`               | `String`          | 1                |
| `STRING`, `BINARY`                            | `LONGBLOB`                        | `String`          | 1                |
| `STRING`, `BINARY`                            | `TINYBLOB`                        | `String`          | 1                |
| `STRING`, `BINARY`                            | `MEDIUMTEXT`                      | `String`          | 1                |
| `STRING`, `BINARY`                            | `TEXT`                            | `String`          | 1                |
| `STRING`, `BINARY`                            | `VARCHAR2`                        | `String`          | 1                |
| `STRING`, `BINARY`                            | `CHARACTER LARGE OBJECT`          | `String`          | 1                |
| `DOUBLE`                                      | `DOUBLE PRECISION`                | `Float64`         | 1                |
| `STRING`, `BINARY`                            | `LONGTEXT`                        | `String`          | 1                |
| `STRING`, `BINARY`                            | `NVARCHAR`                        | `String`          | 1                |
|                                               | `INT1 UNSIGNED`                   | `UInt8`           | 1                |
| `STRING`, `BINARY`                            | `VARCHAR`                         | `String`          | 1                |
| `STRING`, `BINARY`                            | `CHAR VARYING`                    | `String`          | 1                |
| `STRING`, `BINARY`                            | `MEDIUMBLOB`                      | `String`          | 1                |
| `STRING`, `BINARY`                            | `NCHAR`                           | `String`          | 1                |
| `STRING`, `BINARY`                            | `VARBINARY`                       | `String`          | 1                |
| `STRING`, `BINARY`                            | `CHAR`                            | `String`          | 1                |
| `UINT16`                                      | `SMALLINT UNSIGNED`               | `UInt16`          | 1                |
| `TIME (ms)`                                   | `TIMESTAMP`                       | `DateTime`        | 1                |
| `DECIMAL`                                     | `FIXED`                           | `Decimal`         | 1                |
| `STRING`, `BINARY`                            | `TINYTEXT`                        | `String`          | 1                |
| `DECIMAL`                                     | `NUMERIC`                         | `Decimal`         | 1                |
| `DECIMAL`                                     | `DEC`                             | `Decimal`         | 1                |
| `INT64`                                       | `TIME`                            | `Int64`           | 1                |
| `FLOAT`                                       | `FLOAT`                           | `Float32`         | 1                |
| `UINT64`                                      | `SET`                             | `UInt64`          | 1                |
|                                               | `TINYINT UNSIGNED`                | `UInt8`           | 1                |
| `UINT32`                                      | `INTEGER UNSIGNED`                | `UInt32`          | 1                |
| `UINT32`                                      | `INT UNSIGNED`                    | `UInt32`          | 1                |
| `STRING`, `BINARY`                            | `CLOB`                            | `String`          | 1                |
| `UINT32`                                      | `MEDIUMINT UNSIGNED`              | `UInt32`          | 1                |
| `STRING`, `BINARY`                            | `BLOB`                            | `String`          | 1                |
| `FLOAT`                                       | `REAL`                            | `Float32`         | 1                |
|                                               | `SMALLINT`                        | `Int16`           | 1                |
| `INT32`                                       | `INTEGER SIGNED`                  | `Int32`           | 1                |
| `STRING`, `BINARY`                            | `NCHAR VARYING`                   | `String`          | 1                |
| `INT32`                                       | `INT SIGNED`                      | `Int32`           | 1                |
|                                               | `TINYINT SIGNED`                  | `Int8`            | 1                |
| `INT64`                                       | `BIGINT SIGNED`                   | `Int64`           | 1                |
| `STRING`, `BINARY`                            | `BINARY LARGE OBJECT`             | `String`          | 1                |
|                                               | `SMALLINT SIGNED`                 | `Int16`           | 1                |
|                                               | `YEAR`                            | `UInt16`          | 1                |
| `INT32`                                       | `MEDIUMINT`                       | `Int32`           | 1                |
| `INT32`                                       | `INTEGER`                         | `Int32`           | 1                |
|                                               | `INT1 SIGNED`                     | `Int8`            | 1                |
| `UINT64`                                      | `BIT`                             | `UInt64`          | 1                |
| `UINT64`                                      | `BIGINT UNSIGNED`                 | `UInt64`          | 1                |
| `STRING`, `BINARY`                            | `BYTEA`                           | `String`          | 1                |
| `INT32`                                       | `INT`                             | `Int32`           | 1                |
| `FLOAT`                                       | `SINGLE`                          | `Float32`         | 1                |
| `INT32`                                       | `MEDIUMINT SIGNED`                | `Int32`           | 1                |
| `DOUBLE`                                      | `DOUBLE`                          | `Float64`         | 1                |
|                                               | `INT1`                            | `Int8`            | 1                |
| `STRING`, `BINARY`                            | `CHAR LARGE OBJECT`               | `String`          | 1                |
|                                               | `TINYINT`                         | `Int8`            | 1                |
| `INT64`                                       | `BIGINT`                          | `Int64`           | 1                |
| `STRING`, `BINARY`                            | `CHARACTER`                       | `String`          | 1                |
|                                               | `BYTE`                            | `Int8`            | 1                |


#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported
version:1.0

[ClickHouse] SHALL support importing the following Parquet data types:

| Parquet data type                             | ClickHouse data type                  |
|-----------------------------------------------|---------------------------------------|
| `BOOL`                                        | `Bool`                                |
| `UINT8`, `BOOL`                               | `UInt8`                               |
| `INT8`                                        | `Int8`/`Enum8`                        |
| `UINT16`                                      | `UInt16`                              |
| `INT16`                                       | `Int16`/`Enum16`                      |
| `UINT32`                                      | `UInt32`                              |
| `INT32`                                       | `Int32`                               |
| `UINT64`                                      | `UInt64`                              |
| `INT64`                                       | `Int64`                               |
| `FLOAT`                                       | `Float32`                             |
| `DOUBLE`                                      | `Float64`                             |
| `DATE (ms, ns, us)`                           | `Date32`                              |
| `TIME (ms)`                                   | `DateTime`                            |
| `TIMESTAMP (ms, ns, us)`, `TIME (us, ns)`     | `DateTime64`                          |
| `STRING`, `BINARY`                            | `String`                              |
| `STRING`, `BINARY`, `FIXED_LENGTH_BYTE_ARRAY` | `FixedString`                         |
| `DECIMAL`                                     | `Decimal`                             |
| `LIST`                                        | `Array`                               |
| `STRUCT`                                      | `Tuple`                               |
| `MAP`                                         | `Map`                                 |
| `UINT32`                                      | `IPv4`                                |
| `FIXED_LENGTH_BYTE_ARRAY`, `BINARY`           | `IPv6`                                |
| `FIXED_LENGTH_BYTE_ARRAY`, `BINARY`           | `Int128`/`UInt128`/`Int256`/`UInt256` |

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.BLOB
version:1.0

[ClickHouse] SHALL support importing parquet files with `BLOB` content.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.BOOL
version:1.0

[ClickHouse] SHALL support importing `BOOL` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.UINT8
version:1.0

[ClickHouse] SHALL support importing `UINT8` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.INT8
version:1.0

[ClickHouse] SHALL support importing `INT8` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.UINT16
version:1.0

[ClickHouse] SHALL support importing `UINT16` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.INT16
version:1.0

[ClickHouse] SHALL support importing `INT16` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.UINT32
version:1.0

[ClickHouse] SHALL support importing `UINT32` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.INT32
version:1.0

[ClickHouse] SHALL support importing `INT32` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.UINT64
version:1.0

[ClickHouse] SHALL support importing `UINT64` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.INT64
version:1.0

[ClickHouse] SHALL support importing `INT64` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.FLOAT
version:1.0

[ClickHouse] SHALL support importing `FLOAT` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DOUBLE
version:1.0

[ClickHouse] SHALL support importing `DOUBLE` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DATE
version:1.0

[ClickHouse] SHALL support importing `DATE` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DATE.ms
version:1.0

[ClickHouse] SHALL support importing `DATE (ms)` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DATE.ns
version:1.0

[ClickHouse] SHALL support importing `DATE (ns)` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DATE.us
version:1.0

[ClickHouse] SHALL support importing `DATE (us)` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.TIME.ms
version:1.0

[ClickHouse] SHALL support importing `TIME (ms)` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.TIMESTAMP.ms
version:1.0

[ClickHouse] SHALL support importing `TIMESTAMP (ms)` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.TIMESTAMP.ns
version:1.0

[ClickHouse] SHALL support importing `TIMESTAMP (ns)` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.TIMESTAMP.us
version:1.0

[ClickHouse] SHALL support importing `TIMESTAMP (us)` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.STRING
version:1.0

[ClickHouse] SHALL support importing `STRING` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.BINARY
version:1.0

[ClickHouse] SHALL support importing `BINARY` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.FixedLengthByteArray
version:1.0

[ClickHouse] SHALL support importing `FIXED_LENGTH_BYTE_ARRAY` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DECIMAL
version:1.0

[ClickHouse] SHALL support importing `DECIMAL` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.DECIMAL.Filter
version:1.0

[ClickHouse] SHALL support importing `DECIMAL` Parquet datatype with specified filters.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.LIST
version:1.0

[ClickHouse] SHALL support importing `LIST` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.ARRAY
version:1.0

[ClickHouse] SHALL support importing `ARRAY` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.STRUCT
version:1.0

[ClickHouse] SHALL support importing `STRUCT` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Supported.MAP
version:1.0

[ClickHouse] SHALL support importing `MAP` Parquet datatype.

#### UTCAdjusted

##### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.DateUTCAdjusted
version:1.0

[ClickHouse] SHALL support importing `DATE` Parquet datatype with `isAdjustedToUTC = true`.

##### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.TimestampUTCAdjusted
version:1.0

[ClickHouse] SHALL support importing `TIMESTAMP` Parquet datatype with `isAdjustedToUTC = true`.

##### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.TimeUTCAdjusted
version:1.0

[ClickHouse] SHALL support importing `TIME` Parquet datatype with `isAdjustedToUTC = true`.

#### Nullable

##### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.NullValues
version:1.0

[ClickHouse] SHALL support importing columns that have `Null` values in Parquet files. If the target [ClickHouse] column is not `Nullable` then the `Null` value should be converted to the default values for the target column datatype.

For example, if the target column has `Int32`, then the `Null` value will be replaced with `0`.

##### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.ImportInto.Nullable
version:1.0

[ClickHouse] SHALL support importing Parquet files into target table's `Nullable` datatype columns.

#### LowCardinality

##### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.ImportInto.LowCardinality
version:1.0

[ClickHouse] SHALL support importing Parquet files into target table's `LowCardinality` datatype columns.

#### Nested

##### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.ImportInto.Nested
version:1.0

[ClickHouse] SHALL support importing Parquet files into target table's `Nested` datatype columns.

#### UNKNOWN

##### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.ImportInto.Unknown
version:1.0

[ClickHouse] SHALL support importing Parquet files with `UNKNOWN` logical type.

The example as to why the Parquet might have an `UNKNOWN` types is as follows,

> Sometimes, when discovering the schema of existing data, values are always null and there's no type information. 
> The UNKNOWN type can be used to annotate a column that is always null. (Similar to Null type in Avro and Arrow)

### Unsupported Datatypes

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Unsupported
version:1.0

[ClickHouse] MAY not support the following Parquet types:

- `Time32`
- `Fixed_Size_Binary`
- `JSON`
- `UUID`
- `ENUM`
- `Null`

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataTypes.Unsupported.ChunkedArray
version:1.0

[ClickHouse] MAY not support Parquet chunked arrays.

### Filter Pushdown

#### RQ.SRS-032.ClickHouse.Parquet.Import.FilterPushdown
version:1.0

[ClickHouse] MAY support filter pushdown functionality when importing from the Parquet files.

> The functionality should behave similar to https://drill.apache.org/docs/parquet-filter-pushdown/

### Projections

#### RQ.SRS-032.ClickHouse.Parquet.Import.Projections
version: 1.0

[ClickHouse] SHALL support inserting parquet data into a table that has a projection on it.

### Skip Columns

#### RQ.SRS-032.ClickHouse.Parquet.Import.SkipColumns
version: 1.0

[ClickHouse] SHALL support skipping unexistent columns when importing from Parquet files.

### Skip Values

#### RQ.SRS-032.ClickHouse.Parquet.Import.SkipValues
version: 1.0

[ClickHouse] SHALL support skipping unsupported values when import from Parquet files. When the values are being skipped, the inserted values SHALL be the default value for the corresponding column's datatype.

For example, trying to insert `Null` values into the non-`Nullable` column.

```sql
CREATE TABLE TestTable
(
    `path` String,
    `date` Date,
    `hits` UInt32
)
ENGINE = MergeTree
ORDER BY (date, path);

SELECT *
FROM file(output.parquet);

┌─path───┬─date───────┬─hits─┐
│ /path1 │ 2021-06-01 │   10 │
│ /path2 │ 2021-06-02 │    5 │
│ ᴺᵁᴸᴸ   │ 2021-06-03 │    8 │
└────────┴────────────┴──────┘

INSERT INTO TestTable
FROM INFILE 'output.parquet' FORMAT Parquet;

SELECT *
FROM TestTable;

┌─path───┬───────date─┬─hits─┐
│ /path1 │ 2021-06-01 │   10 │
│ /path2 │ 2021-06-02 │    5 │
│        │ 2021-06-03 │    8 │
└────────┴────────────┴──────┘
```

### Auto Typecast

#### RQ.SRS-032.ClickHouse.Parquet.Import.AutoTypecast
version: 1.0

[ClickHouse] SHALL automatically typecast parquet datatype based on the types in the target table.

For example,

> When we take the following Parquet file:
> 
> ```
> ┌─path────────────────────────────────────────────────────────────┬─date───────┬──hits─┐
> │ Akiba_Hebrew_Academy                                            │ 2017-08-01 │   241 │
> │ 1980_Rugby_League_State_of_Origin_match                         │ 2017-07-01 │     2 │
> │ Column_of_Santa_Felicita,_Florence                              │ 2017-06-01 │    14 │
> └─────────────────────────────────────────────────────────────────┴────────────┴───────┘
> ```
> 
> ```
> ┌─name─┬─type─────────────┬─default_type─┬─default_expression─┬─comment─┬─codec_expression─┬─ttl_expression─┐
> │ path │ Nullable(String) │              │                    │         │                  │                │
> │ date │ Nullable(String) │              │                    │         │                  │                │
> │ hits │ Nullable(Int64)  │              │                    │         │                  │                │
> └──────┴──────────────────┴──────────────┴────────────────────┴─────────┴──────────────────┴────────────────┘
> ```
> 
> 
> Then create a table to import parquet data to:
> ```sql
> CREATE TABLE sometable
> (
>     `path` String,
>     `date` Date,
>     `hits` UInt32
> )
> ENGINE = MergeTree
> ORDER BY (date, path)
> ```
> 
> Then import data using a FROM INFILE clause:
> 
> 
> ```sql
> INSERT INTO sometable
> FROM INFILE 'data.parquet' FORMAT Parquet;
> ```
> 
> As a result ClickHouse automatically converted parquet `strings` (in the `date` column) to the `Date` type.
> 
> 
> ```sql
> DESCRIBE TABLE sometable
> ```
> 
> ```
> ┌─name─┬─type───┬─default_type─┬─default_expression─┬─comment─┬─codec_expression─┬─ttl_expression─┐
> │ path │ String │              │                    │         │                  │                │
> │ date │ Date   │              │                    │         │                  │                │
> │ hits │ UInt32 │              │                    │         │                  │                │
> └──────┴────────┴──────────────┴────────────────────┴─────────┴──────────────────┴────────────────┘
> ```

### Row Group Size

#### RQ.SRS-032.ClickHouse.Parquet.Import.RowGroupSize
version: 1.0

[ClickHouse] SHALL support importing Parquet files with different Row Group Sizes.

As described in https://parquet.apache.org/docs/file-format/configurations/#row-group-size,

> We recommend large row groups (512MB - 1GB). Since an entire row group might need to be read, 
> we want it to completely fit on one HDFS block.

### Data Page Size

#### RQ.SRS-032.ClickHouse.Parquet.Import.DataPageSize
version: 1.0

[ClickHouse] SHALL support importing Parquet files with different Data Page Sizes.

As described in https://parquet.apache.org/docs/file-format/configurations/#data-page--size,

> Note: for sequential scans, it is not expected to read a page at a time; this is not the IO chunk. We recommend 8KB for page sizes.


### Import Into New Table

#### RQ.SRS-032.ClickHouse.Parquet.Import.NewTable
version: 1.0

[ClickHouse] SHALL support creating and populating tables directly from the Parquet files with table schema being auto-detected
from file's structure.

For example,

> Since ClickHouse reads parquet file schema, we can create tables on the fly:
> 
> ```sql
> CREATE TABLE imported_from_parquet
> ENGINE = MergeTree
> ORDER BY tuple() AS
> SELECT *
> FROM file('data.parquet', Parquet)
> ```
> 
> This will automatically create and populate a table from a given parquet file:
> 
> ```sql
> DESCRIBE TABLE imported_from_parquet;
> ```
> ```
> ┌─name─┬─type─────────────┬─default_type─┬─default_expression─┬─comment─┬─codec_expression─┬─ttl_expression─┐
> │ path │ Nullable(String) │              │                    │         │                  │                │
> │ date │ Nullable(String) │              │                    │         │                  │                │
> │ hits │ Nullable(Int64)  │              │                    │         │                  │                │
> └──────┴──────────────────┴──────────────┴────────────────────┴─────────┴──────────────────┴────────────────┘
> ```

### Performance

#### RQ.SRS-032.ClickHouse.Parquet.Import.Performance.CountFromMetadata
version: 1.0

[ClickHouse] MAY support importing the information about the number of rows from Parquet file directly from the metadata instead of going through the whole file.

For example,

> When running this query,
> 
> ```sql
> SELECT count(*)
> FROM file('*.parquet', 'Parquet');
>
> ┌───count()─┐
> │ 110000000 │
> └───────────┘
> 
> Elapsed: 1.365 sec.
> ```
> 
> The runtime should be around ~16ms instead of 1.365 sec.
>

#### RQ.SRS-032.ClickHouse.Parquet.Import.Performance.ParallelProcessing
version: 1.0

[ClickHouse] SHALL support process parallelization when importing from the parquet files.

### Import Nested Types

#### RQ.SRS-032.ClickHouse.Parquet.Import.Nested.ArrayIntoNested
version: 1.0

[ClickHouse] SHALL support importing nested columns from the Parquet file.

#### RQ.SRS-032.ClickHouse.Parquet.Import.Nested.Complex
version:1.0

[ClickHouse] SHALL support importing nested: `Array`, `Tuple` and `Map` datatypes from Parquet files.

#### RQ.SRS-032.ClickHouse.Parquet.Import.Nested.ArrayIntoNested.ImportNested
version: 1.0

[ClickHouse] SHALL support inserting arrays of nested structs from Parquet files into [ClickHouse] Nested columns when the `input_format_parquet_import_nested` setting is set to `1`.

#### RQ.SRS-032.ClickHouse.Parquet.Import.Nested.ArrayIntoNested.NotImportNested
version: 1.0

[ClickHouse] SHALL return an error when trying to insert arrays of nested structs from Parquet files into [ClickHouse] Nested columns when the
`input_format_parquet_import_nested` setting is set to `0`.

#### RQ.SRS-032.ClickHouse.Parquet.Import.Nested.ArrayIntoNotNested
version: 1.0

[ClickHouse] SHALL return an error when trying to insert arrays of nested structs from Parquet files into [ClickHouse] not Nested columns.

#### RQ.SRS-032.ClickHouse.Parquet.Import.Nested.NonArrayIntoNested
version: 1.0

[ClickHouse] SHALL return an error when trying to insert datatypes other than arrays of nested structs from Parquet files into [ClickHouse] Nested columns.

### Import Chunked Columns

#### RQ.SRS-032.ClickHouse.Parquet.Import.ChunkedColumns
version: 1.0

[ClickHouse] SHALL support importing Parquet files with chunked columns.

### Import Encoded

#### Plain (Import)

##### RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.Plain
version: 1.0

[ClickHouse] SHALL support importing `Plain` encoded Parquet files.

#### Dictionary (Import)

##### RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.Dictionary
version: 1.0

[ClickHouse] SHALL support importing `Dictionary` encoded Parquet files.

#### Run Length Encoding (Import)

##### RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.RunLength
version: 1.0

[ClickHouse] SHALL support importing `Run Length Encoding / Bit-Packing Hybrid` encoded Parquet files.

#### Delta (Import)

##### RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.Delta
version: 1.0

[ClickHouse] SHALL support importing `Delta Encoding` encoded Parquet files.

#### Delta-length byte array (Import)

##### RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.DeltaLengthByteArray
version: 1.0

[ClickHouse] SHALL support importing `Delta-length byte array` encoded Parquet files.

#### Delta Strings (Import)

##### RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.DeltaStrings
version: 1.0

[ClickHouse] SHALL support importing `Delta Strings` encoded Parquet files.

#### Byte Stream Split (Import)

##### RQ.SRS-032.ClickHouse.Parquet.Import.Encoding.ByteStreamSplit
version: 1.0

[ClickHouse] SHALL support importing `Byte Stream Split` encoded Parquet files.

### Import Settings

#### RQ.SRS-032.ClickHouse.Parquet.Import.Settings.ImportNested
version: 1.0

[ClickHouse] SHALL support specifying the `input_format_parquet_import_nested` setting to allow inserting arrays of
nested structs into Nested column type. The default value SHALL be `0`.

- `0` — Data can not be inserted into Nested columns as an array of structs.
- `1` — Data can be inserted into Nested columns as an array of structs.

#### RQ.SRS-032.ClickHouse.Parquet.Import.Settings.CaseInsensitiveColumnMatching
version: 1.0

[ClickHouse] SHALL support specifying the `input_format_parquet_case_insensitive_column_matching` setting to ignore matching
Parquet and ClickHouse columns. The default value SHALL be `0`.

#### RQ.SRS-032.ClickHouse.Parquet.Import.Settings.AllowMissingColumns
version: 1.0

[ClickHouse] SHALL support specifying the `input_format_parquet_allow_missing_columns` setting to allow missing columns.
The default value SHALL be `0`.

#### RQ.SRS-032.ClickHouse.Parquet.Import.Settings.SkipColumnsWithUnsupportedTypesInSchemaInference
version: 1.0

[ClickHouse] SHALL support specifying the `input_format_parquet_skip_columns_with_unsupported_types_in_schema_inference` 
setting to allow skipping unsupported types. The default value SHALL be `0`.

### Libraries

#### RQ.SRS-032.ClickHouse.Parquet.Libraries
version: 1.0

[ClickHouse] SHALL support importing from Parquet files generated using various libraries.

#### Pyarrow

##### RQ.SRS-032.ClickHouse.Parquet.Libraries.Pyarrow
version: 1.0

[ClickHouse] SHALL support importing from Parquet files generated using `Pyarrow`.

#### PySpark

##### RQ.SRS-032.ClickHouse.Parquet.Libraries.PySpark
version: 1.0

[ClickHouse] SHALL support importing from Parquet files generated using `PySpark`.

#### Pandas

##### RQ.SRS-032.ClickHouse.Parquet.Libraries.Pandas
version: 1.0

[ClickHouse] SHALL support importing from Parquet files generated using `Pandas`.

#### parquet-go

##### RQ.SRS-032.ClickHouse.Parquet.Libraries.ParquetGO
version: 1.0

[ClickHouse] SHALL support importing from Parquet files generated using `parquet-go`.

#### H2OAI

##### RQ.SRS-032.ClickHouse.Parquet.Libraries.H2OAI
version: 1.0

[ClickHouse] SHALL support importing from Parquet files generated using `H2OAI`.

## Export from Parquet Files

#### RQ.SRS-032.ClickHouse.Parquet.Export
version: 1.0

[ClickHouse] SHALL support using `SELECT` query with either the `INTO OUTFILE {file_name}` or just `FORMAT Parquet` clauses to Export Parquet files. 

For example,

```sql
SELECT *
FROM sometable
INTO OUTFILE 'export.parquet'
FORMAT Parquet
```

or

```sql
SELECT *
FROM sometable
FORMAT Parquet
```

#### Auto Detect Parquet File When Exporting

##### RQ.SRS-032.ClickHouse.Parquet.Export.Outfile.AutoDetectParquetFileFormat
version: 1.0


[ClickHouse] SHALL support automatically detecting Parquet file format based on file extension when using OUTFILE clause without explicitly specifying the format setting.

```sql
SELECT *
FROM sometable
INTO OUTFILE 'export.parquet'
```

### Supported Data types

#### RQ.SRS-032.ClickHouse.Parquet.Export.Datatypes.Supported
version:1.0

[ClickHouse] SHALL support exporting the following datatypes to Parquet:

| ClickHouse data type                  | Parquet data type         |
|---------------------------------------|---------------------------|
| `Bool`                                | `BOOL`                    |
| `UInt8`                               | `UINT8`                   |
| `Int8`/`Enum8`                        | `INT8`                    |
| `UInt16`                              | `UINT16`                  |
| `Int16`/`Enum16`                      | `INT16`                   |
| `UInt32`                              | `UINT32`                  |
| `Int32`                               | `INT32`                   |
| `UInt64`                              | `UINT64`                  |
| `Int64`                               | `INT64`                   |
| `Float32`                             | `FLOAT`                   |
| `Float64`                             | `DOUBLE`                  |
| `Date32`                              | `DATE`                    |
| `DateTime`                            | `UINT32`                  |
| `DateTime64`                          | `TIMESTAMP`               |
| `String`                              | `BINARY`                  |
| `FixedString`                         | `FIXED_LENGTH_BYTE_ARRAY` |
| `Decimal`                             | `DECIMAL`                 |
| `Array`                               | `LIST`                    |
| `Tuple`                               | `STRUCT`                  |
| `Map`                                 | `MAP`                     |
| `IPv4`                                | `UINT32`                  |
| `IPv6`                                | `FIXED_LENGTH_BYTE_ARRAY` |
| `Int128`/`UInt128`/`Int256`/`UInt256` | `FIXED_LENGTH_BYTE_ARRAY` |

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.BLOB
version:1.0

[ClickHouse] SHALL support exporting parquet files with `BLOB` content.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.BOOL
version:1.0

[ClickHouse] SHALL support exporting `BOOL` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.UINT8
version:1.0

[ClickHouse] SHALL support exporting `UINT8` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.INT8
version:1.0

[ClickHouse] SHALL support exporting `INT8` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.UINT16
version:1.0

[ClickHouse] SHALL support exporting `UINT16` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.INT16
version:1.0

[ClickHouse] SHALL support exporting `INT16` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.UINT32
version:1.0

[ClickHouse] SHALL support exporting `UINT32` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.INT32
version:1.0

[ClickHouse] SHALL support exporting `INT32` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.UINT64
version:1.0

[ClickHouse] SHALL support exporting `UINT64` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.INT64
version:1.0

[ClickHouse] SHALL support exporting `INT64` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.FLOAT
version:1.0

[ClickHouse] SHALL support exporting `FLOAT` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DOUBLE
version:1.0

[ClickHouse] SHALL support exporting `DOUBLE` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DATE
version:1.0

[ClickHouse] SHALL support exporting `DATE` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DATE.ms
version:1.0

[ClickHouse] SHALL support exporting `DATE (ms)` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DATE.ns
version:1.0

[ClickHouse] SHALL support exporting `DATE (ns)` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DATE.us
version:1.0

[ClickHouse] SHALL support exporting `DATE (us)` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.TIME.ms
version:1.0

[ClickHouse] SHALL support exporting `TIME (ms)` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.TIMESTAMP.ms
version:1.0

[ClickHouse] SHALL support exporting `TIMESTAMP (ms)` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.TIMESTAMP.ns
version:1.0

[ClickHouse] SHALL support exporting `TIMESTAMP (ns)` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.TIMESTAMP.us
version:1.0

[ClickHouse] SHALL support exporting `TIMESTAMP (us)` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.STRING
version:1.0

[ClickHouse] SHALL support exporting `STRING` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.BINARY
version:1.0

[ClickHouse] SHALL support exporting `BINARY` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.FixedLengthByteArray
version:1.0

[ClickHouse] SHALL support exporting `FIXED_LENGTH_BYTE_ARRAY` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DECIMAL
version:1.0

[ClickHouse] SHALL support exporting `DECIMAL` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.DECIMAL.Filter
version:1.0

[ClickHouse] SHALL support exporting `DECIMAL` Parquet datatype with specified filters.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.LIST
version:1.0

[ClickHouse] SHALL support exporting `LIST` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.ARRAY
version:1.0

[ClickHouse] SHALL support exporting `ARRAY` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.STRUCT
version:1.0

[ClickHouse] SHALL support exporting `STRUCT` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Supported.MAP
version:1.0

[ClickHouse] SHALL support exporting `MAP` Parquet datatype.

#### RQ.SRS-032.ClickHouse.Parquet.Export.DataTypes.Nullable
version:1.0

[ClickHouse] SHALL support exporting `Nullable` datatypes to Parquet files and `Nullable` datatypes that consist only of `Null`.

### Working With Nested Types Export

#### RQ.SRS-032.ClickHouse.Parquet.Export.Nested
version: 1.0

[ClickHouse] SHALL support exporting nested columns to the Parquet file.

#### RQ.SRS-032.ClickHouse.Parquet.Export.Nested.Complex
version:1.0

[ClickHouse] SHALL support exporting nested: `Array`, `Tuple` and `Map` datatypes to Parquet files.

### Exporting Chunked Columns

#### RQ.SRS-032.ClickHouse.Parquet.Export.ChunkedColumns
version: 1.0

[ClickHouse] SHALL support exporting chunked columns to Parquet files.

### Query Types

#### JOIN

##### RQ.SRS-032.ClickHouse.Export.Parquet.Join
version: 1.0

[ClickHouse] SHALL support exporting output of `SELECT` query with a `JOIN` clause into a Parquet file.

#### UNION

##### RQ.SRS-032.ClickHouse.Parquet.Export.Union
version: 1.0

[ClickHouse] SHALL support exporting output of `SELECT` query with a `UNION` clause into a Parquet file.

##### RQ.SRS-032.ClickHouse.Parquet.Export.Union.Multiple
version: 1.0

[ClickHouse] SHALL support exporting output of `SELECT` query with multiple `UNION` clauses used on the Parquet file.

For example,

```sql
SELECT * FROM (SELECT * FROM file('file0001.parquet')
UNION ALL SELECT * FROM file('file0001.parquet')
UNION ALL SELECT * FROM file('file0001.parquet')
UNION ALL SELECT * FROM file('file0001.parquet')
UNION ALL SELECT * FROM file('file0001.parquet')
...
UNION ALL SELECT * FROM file('file0001.parquet')) LIMIT 10;
```

#### RQ.SRS-032.ClickHouse.Parquet.Export.View
version: 1.0

[ClickHouse] SHALL support exporting output of `SELECT * FROM {view_name}` query into a Parquet file.

#### RQ.SRS-032.ClickHouse.Parquet.Export.Select.MaterializedView
version: 1.0

[ClickHouse] SHALL support exporting output of `SELECT * FROM {mat_view_name}` query into a Parquet file.

### Export Encoded

#### Plain (Export)

##### RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.Plain
version: 1.0

[ClickHouse] SHALL support exporting `Plain` encoded Parquet files.

#### Dictionary (Export)

##### RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.Dictionary
version: 1.0

[ClickHouse] SHALL support exporting `Dictionary` encoded Parquet files.

#### Run Length Encoding (Export)

##### RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.RunLength
version: 1.0

[ClickHouse] SHALL support exporting `Run Length Encoding / Bit-Packing Hybrid` encoded Parquet files.

#### Delta (Export)

##### RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.Delta
version: 1.0

[ClickHouse] SHALL support exporting `Delta Encoding` encoded Parquet files.

#### Delta-length byte array (Export)

##### RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.DeltaLengthByteArray
version: 1.0

[ClickHouse] SHALL support exporting `Delta-length byte array` encoded Parquet files.

#### Delta Strings (Export)

##### RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.DeltaStrings
version: 1.0

[ClickHouse] SHALL support exporting `Delta Strings` encoded Parquet files.

#### Byte Stream Split (Export)

##### RQ.SRS-032.ClickHouse.Parquet.Export.Encoding.ByteStreamSplit
version: 1.0

[ClickHouse] SHALL support exporting `Byte Stream Split` encoded Parquet files.

### Export Settings

#### RQ.SRS-032.ClickHouse.Parquet.Export.Settings.RowGroupSize
version: 1.0

[ClickHouse] SHALL support specifying the `output_format_parquet_row_group_size` setting to specify row group size in rows.
The default value SHALL be `1000000`.

#### RQ.SRS-032.ClickHouse.Parquet.Export.Settings.StringAsString
version: 1.0

[ClickHouse] SHALL support specifying the `output_format_parquet_string_as_string` setting to use Parquet String type instead of Binary.
The default value SHALL be `0`.

#### RQ.SRS-032.ClickHouse.Parquet.Export.Settings.StringAsFixedByteArray
version: 1.0

[ClickHouse] SHALL support specifying the `output_format_parquet_fixed_string_as_fixed_byte_array` setting to use Parquet FIXED_LENGTH_BYTE_ARRAY type instead of Binary/String for FixedString columns. The default value SHALL be `1`.

#### RQ.SRS-032.ClickHouse.Parquet.Export.Settings.ParquetVersion
version: 1.0

[ClickHouse] SHALL support specifying the `output_format_parquet_version` setting to set the version of Parquet used in the output file.
The default value SHALL be `2.latest`.

#### RQ.SRS-032.ClickHouse.Parquet.Export.Settings.CompressionMethod
version: 1.0

[ClickHouse] SHALL support specifying the `output_format_parquet_compression_method` setting to set the compression method used in the Parquet file.
The default value SHALL be `lz4`.

### Type Conversion

#### RQ.SRS-032.ClickHouse.Parquet.DataTypes.TypeConversionFunction
version:1.0

[ClickHouse] SHALL support using type conversion functions when importing Parquet files.

For example,

```sql
SELECT
    n,
    toDateTime(time)
FROM file('time.parquet', Parquet);
```

## Hive Partitioning

### RQ.SRS-032.ClickHouse.Parquet.Hive
version: 1.0

[ClickHouse] MAY not support importing or exporting hive partitioned Parquet files.

## Parquet Encryption

### File Encryption

#### RQ.SRS-032.ClickHouse.Parquet.Encryption.File
version: 1.0

[ClickHouse] MAY support importing or exporting encrypted Parquet files.

### Column Encryption

#### RQ.SRS-032.ClickHouse.Parquet.Encryption.Column.Modular
version: 1.0

[ClickHouse] MAY support importing or exporting Parquet files with specific encrypted columns.

#### RQ.SRS-032.ClickHouse.Parquet.Encryption.Column.Keys
version: 1.0

[ClickHouse] MAY support importing or exporting Parquet files when different columns are encrypted with different keys.

### Encryption Algorithms

#### RQ.SRS-032.ClickHouse.Parquet.Encryption.Algorithms.AESGCM
version: 1.0

[ClickHouse] MAY support importing or exporting Parquet files with `AES-GCM` encryption algorithm.

> The default algorithm AES-GCM provides full protection against tampering with data and metadata parts in Parquet files.

#### RQ.SRS-032.ClickHouse.Parquet.Encryption.Algorithms.AESGCMCTR
version: 1.0

[ClickHouse] MAY support importing or exporting Parquet files with `AES-GCM-CTR`  encryption algorithm.

> The alternative algorithm AES-GCM-CTR supports partial integrity protection of Parquet files. 
> Only metadata parts are protected against tampering, not data parts. 
> An advantage of this algorithm is that it has a lower throughput overhead compared to the AES-GCM algorithm.

### EncryptionParameters

#### RQ.SRS-032.ClickHouse.Parquet.Encryption.Parameters
version: 1.0

[ClickHouse] MAY support importing or exporting Parquet files with different parameters.

##### RQ.SRS-032.ClickHouse.Parquet.Encryption.Parameters.Algorythm
version: 1.0

[ClickHouse] MAY support importing or exporting Parquet files with `encryption.algorithm` parameter specified.

##### RQ.SRS-032.ClickHouse.Parquet.Encryption.Parameters.Plaintext.Footer
version: 1.0

[ClickHouse] MAY support importing or exporting Parquet files with `encryption.plaintext.footer` parameter specified.

## DESCRIBE Parquet

### RQ.SRS-032.ClickHouse.Parquet.Structure
version: 1.0

[ClickHouse] SHALL support using `DESCRIBE TABLE` statement on the Parquet to read the file structure.

For example,

```sql
DESCRIBE TABLE file('data.parquet', Parquet)
```

## Compression

### None

#### RQ.SRS-032.ClickHouse.Parquet.Compression.None
version: 1.0

[ClickHouse] SHALL support importing or exporting uncompressed Parquet files.

### Gzip

#### RQ.SRS-032.ClickHouse.Parquet.Compression.Gzip
version: 1.0

[ClickHouse] SHALL support importing or exporting Parquet files compressed using gzip.

### Brotli

#### RQ.SRS-032.ClickHouse.Parquet.Compression.Brotli
version: 1.0

[ClickHouse] SHALL support importing or exporting Parquet files compressed using brotli.

### Lz4

#### RQ.SRS-032.ClickHouse.Parquet.Compression.Lz4
version: 1.0

[ClickHouse] SHALL support importing or exporting Parquet files compressed using lz4.

### Lz4Raw

#### RQ.SRS-032.ClickHouse.Parquet.Compression.Lz4Raw
version: 1.0

[ClickHouse] SHALL support importing or exporting Parquet files compressed using lz4_raw.

### Lz4Hadoop

#### RQ.SRS-032.ClickHouse.Parquet.Compression.Lz4Hadoop
version: 1.0

[ClickHouse] SHALL support importing or exporting Parquet files compressed using LZ4_HADOOP.

### Snappy

#### RQ.SRS-032.ClickHouse.Parquet.Compression.Snappy
version: 1.0

[ClickHouse] SHALL support importing or exporting Parquet files compressed using Snappy.

### Zstd

#### RQ.SRS-032.ClickHouse.Parquet.Compression.Zstd
version: 1.0

[ClickHouse] SHALL support importing or exporting Parquet files compressed using Zstd.

### Unsupported Compression

#### Lzo

##### RQ.SRS-032.ClickHouse.Parquet.UnsupportedCompression.Lzo
version: 1.0

[ClickHouse] MAY not support importing or exporting Parquet files compressed using lzo.

## Table Functions

### URL

#### RQ.SRS-032.ClickHouse.Parquet.TableFunctions.URL
version: 1.0

[ClickHouse] SHALL support `url` table function importing and exporting Parquet format.

### File

#### RQ.SRS-032.ClickHouse.Parquet.TableFunctions.File
version: 1.0

[ClickHouse] SHALL support `file` table function importing and exporting Parquet format.

For example,

```sql
SELECT * FROM file('data.parquet', Parquet)
```

#### RQ.SRS-032.ClickHouse.Parquet.TableFunctions.File.AutoDetectParquetFileFormat
version: 1.0

[ClickHouse] SHALL support automatically detecting Parquet file format based on file extension when using `file()` function without explicitly specifying the format setting.

```sql
SELECT * FROM file('data.parquet')
```

### S3

#### RQ.SRS-032.ClickHouse.Parquet.TableFunctions.S3
version: 1.0

[ClickHouse] SHALL support `s3` table function for import and exporting Parquet format.

For example,

```sql
SELECT *
FROM gcs('https://storage.googleapis.com/my-test-bucket-768/data.parquet', Parquet)
```

### JDBC

#### RQ.SRS-032.ClickHouse.Parquet.TableFunctions.JDBC
version: 1.0

[ClickHouse] SHALL support `jdbc` table function for import and exporting Parquet format.

### ODBC

#### RQ.SRS-032.ClickHouse.Parquet.TableFunctions.ODBC
version: 1.0

[ClickHouse] SHALL support `odbc` table function for importing and exporting Parquet format.

### HDFS

#### RQ.SRS-032.ClickHouse.Parquet.TableFunctions.HDFS
version: 1.0

[ClickHouse] SHALL support `hdfs` table function for importing and exporting Parquet format.

### Remote

#### RQ.SRS-032.ClickHouse.Parquet.TableFunctions.Remote
version: 1.0

[ClickHouse] SHALL support `remote` table function for importing and exporting Parquet format.

### MySQL

#### RQ.SRS-032.ClickHouse.Parquet.TableFunctions.MySQL
version: 1.0

[ClickHouse] SHALL support `mysql` table function for import and exporting Parquet format.

For example,

> Given we have a table with a `mysql` engine:
> 
> ```sql
> CREATE TABLE mysql_table1 (
>   id UInt64,
>   column1 String
> )
> ENGINE = MySQL('mysql-host.domain.com','db1','table1','mysql_clickhouse','Password123!')
> ```
> 
> We can Export from a Parquet file format with:
> 
> ```sql
> SELECT * FROM mysql_table1 INTO OUTFILE testTable.parquet FORMAT Parquet
> ```

### PostgreSQL

#### RQ.SRS-032.ClickHouse.Parquet.TableFunctions.PostgreSQL
version: 1.0

[ClickHouse] SHALL support `postgresql` table function importing and exporting Parquet format.

## Table Engines

### Readable External Table

#### RQ.SRS-032.ClickHouse.Parquet.TableEngines.ReadableExternalTable
version: 1.0

[ClickHouse] MAY support Parquet format being exported from and imported into all table engines using `READABLE EXTERNAL TABLE`.

For example,

> ```sql
> CREATE READABLE EXTERNAL TABLE table_name (
>     key UInt32,
>     value UInt32
> ) LOCATION ('file://file_localtion/*.parquet')
> ```

### MergeTree

#### RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.MergeTree
version: 1.0

[ClickHouse] SHALL support Parquet format being exported from and imported into a `MergeTree` table engine.

#### ReplicatedMergeTree

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.ReplicatedMergeTree
version: 1.0

[ClickHouse] SHALL support Parquet format being exported from and imported into a `ReplicatedMergeTree` table engine.

#### ReplacingMergeTree

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.ReplacingMergeTree
version: 1.0

[ClickHouse] SHALL support Parquet format being exported from and imported into a `ReplacingMergeTree` table engine.

#### SummingMergeTree

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.SummingMergeTree
version: 1.0

[ClickHouse] SHALL support Parquet format being exported from and imported into a `SummingMergeTree` table engine.

#### AggregatingMergeTree

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.AggregatingMergeTree
version: 1.0

[ClickHouse] SHALL support Parquet format being exported from and imported into a `AggregatingMergeTree` table engine.

#### CollapsingMergeTree

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.CollapsingMergeTree
version: 1.0

[ClickHouse] SHALL support Parquet format being exported from and imported into a `CollapsingMergeTree` table engine.

#### VersionedCollapsingMergeTree

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.VersionedCollapsingMergeTree
version: 1.0

[ClickHouse] SHALL support Parquet format being exported from and imported into a `VersionedCollapsingMergeTree` table engine.

#### GraphiteMergeTree

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.GraphiteMergeTree
version: 1.0

[ClickHouse] SHALL support Parquet format being exported from and imported into a `GraphiteMergeTree` table engine.

### Integration Engines

#### ODBC Engine

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.ODBC
version: 1.0

[ClickHouse] SHALL support Parquet format being exported from and imported into an `ODBC` table engine.

#### JDBC Engine

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.JDBC
version: 1.0

[ClickHouse] SHALL support Parquet format being exported from and imported into a `JDBC` table engine.

#### MySQL Engine

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.MySQL
version: 1.0

[ClickHouse] SHALL support Parquet format being exported from and imported into a `MySQL` table engine.

#### MongoDB Engine

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.MongoDB
version: 1.0

[ClickHouse] SHALL support Parquet format being exported from and imported into a `MongoDB` table engine.

#### HDFS Engine

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.HDFS
version: 1.0

[ClickHouse] SHALL support Parquet format being exported from and imported into a `HDFS` table engine.

#### S3 Engine

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.S3
version: 1.0

[ClickHouse] SHALL support Parquet format being exported from and imported into an `S3` table engine.

#### Kafka Engine

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.Kafka
version: 1.0

[ClickHouse] SHALL support Parquet format being exported from and imported into a `Kafka` table engine.

#### EmbeddedRocksDB Engine

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.EmbeddedRocksDB
version: 1.0

[ClickHouse] SHALL support Parquet format being exported from and imported into an `EmbeddedRocksDB` table engine.

#### PostgreSQL Engine

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.PostgreSQL
version: 1.0

[ClickHouse] SHALL support Parquet format being exported from and imported into a `PostgreSQL` table engine.

### Special Engines

#### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.Memory
version: 1.0

[ClickHouse] SHALL support Parquet format being exported from and imported into a `Memory` table engine.

#### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.Distributed
version: 1.0

[ClickHouse] SHALL support Parquet format being exported from and imported into a `Distributed` table engine.

#### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.Dictionary
version: 1.0

[ClickHouse] SHALL support Parquet format being exported from and imported into a `Dictionary` table engine.

#### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.File
version: 1.0

[ClickHouse] SHALL support Parquet format being exported from and imported into a `File` table engine.

#### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.URL
version: 1.0

[ClickHouse] SHALL support Parquet format being exported from and imported into a `URL` table engine.

## Indexes

### RQ.SRS-032.ClickHouse.Parquet.Indexes
version: 1.0

[ClickHouse] SHALL support importing from Parquet files that utilize indexes.

### Page

#### RQ.SRS-032.ClickHouse.Parquet.Indexes.Page
version: 1.0

[ClickHouse] SHALL support utilizing 'Page Index' of a parquet file in order to read data from the file more efficiently.

### Bloom Filter

#### RQ.SRS-032.ClickHouse.Parquet.Indexes.BloomFilter
version: 1.0

[ClickHouse] SHALL support utilizing 'Bloom Filter' of a parquet file in order to read data from the file more efficiently.

> A Bloom filter is a compact data structure that overapproximates a set. It can respond to membership 
> queries with either “definitely no” or “probably yes”, where the probability of false positives is configured when the filter is initialized. Bloom filters do not have false negatives.
> 
> Because Bloom filters are small compared to dictionaries, they can be used for predicate pushdown even in columns with high cardinality and when space is at a premium.

### Dictionary

#### RQ.SRS-032.ClickHouse.Parquet.Indexes.Dictionary
version: 1.0

[ClickHouse] SHALL support utilizing 'Dictionary' of a parquet file in order to read data from the file more efficiently.


## Metadata

Parquet files have three types of metadata

- file metadata
- column (chunk) metadata
- page header metadata

as described in https://parquet.apache.org/docs/file-format/metadata/.

### ParquetFormat

#### RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadataFormat
version: 1.0

[ClickHouse] SHALL support `ParquetMetadata` format to read metadata from Parquet files.

For example,

```sql
SELECT * FROM file(data.parquet, ParquetMetadata) format PrettyJSONEachRow
```

#### RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadataFormat.Output
version: 1.0

[ClickHouse] SHALL not support `ParquetMetadata` format as an output format and the `FORMAT_IS_NOT_SUITABLE_FOR_OUTPUT` 
error SHALL be returned.

For example,

```sql
SELECT *
FROM file('writing_nullable_int8.parquet', 'ParquetMetadata')
FORMAT ParquetMetadata

Exception on client:
Code: 399. DB::Exception: Code: 399. DB::Exception: Format ParquetMetadata is not suitable for output. (FORMAT_IS_NOT_SUITABLE_FOR_OUTPUT) (version 23.5.1.2890 (official build)). (FORMAT_IS_NOT_SUITABLE_FOR_OUTPUT)
```

#### RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadata.Content
version: 1.0

[ClickHouse]'s ParquetMetadata format SHALL output the Parquet metadata in the following structure:

> - num_columns - the number of columns
> - num_rows - the total number of rows
> - num_row_groups - the total number of row groups
> - format_version - parquet format version, always 1.0 or 2.6
> - total_uncompressed_size - total uncompressed bytes size of the data, calculated as the sum of total_byte_size from all row groups
> - total_compressed_size - total compressed bytes size of the data, calculated as the sum of total_compressed_size from all row groups
> - columns - the list of columns metadata with the next structure:
>     - name - column name
>     - path - column path (differs from name for nested column)
>     - max_definition_level - maximum definition level
>     - max_repetition_level - maximum repetition level
>     - physical_type - column physical type
>     - logical_type - column logical type
>     - compression - compression used for this column
>     - total_uncompressed_size - total uncompressed bytes size of the column, calculated as the sum of total_uncompressed_size of the column from all row groups
>     - total_compressed_size - total compressed bytes size of the column, calculated as the sum of total_compressed_size of the column from all row groups
>     - space_saved - percent of space saved by compression, calculated as (1 - total_compressed_size/total_uncompressed_size).
>     - encodings - the list of encodings used for this column
> - row_groups - the list of row groups metadata with the next structure:
>     - num_columns - the number of columns in the row group
>     - num_rows - the number of rows in the row group
>     - total_uncompressed_size - total uncompressed bytes size of the row group
>     - total_compressed_size - total compressed bytes size of the row group
>     - columns - the list of column chunks metadata with the next structure:
>        - name - column name
>        - path - column path
>        - total_compressed_size - total compressed bytes size of the column
>        - total_uncompressed_size - total uncompressed bytes size of the row group
>        - have_statistics - boolean flag that indicates if column chunk metadata contains column statistics
>        - statistics - column chunk statistics (all fields are NULL if have_statistics = false) with the next structure:
>            - num_values - the number of non-null values in the column chunk
>            - null_count - the number of NULL values in the column chunk
>            - distinct_count - the number of distinct values in the column chunk
>            - min - the minimum value of the column chunk
>            - max - the maximum column of the column chunk

For example,

> ```json
> {
>     "num_columns": "2",
>     "num_rows": "100000",
>     "num_row_groups": "2",
>     "format_version": "2.6",
>     "metadata_size": "577",
>     "total_uncompressed_size": "282436",
>     "total_compressed_size": "26633",
>     "columns": [
>         {
>             "name": "number",
>             "path": "number",
>             "max_definition_level": "0",
>             "max_repetition_level": "0",
>             "physical_type": "INT32",
>             "logical_type": "Int(bitWidth=16, isSigned=false)",
>             "compression": "LZ4",
>             "total_uncompressed_size": "133321",
>             "total_compressed_size": "13293",
>             "space_saved": "90.03%",
>             "encodings": [
>                 "RLE_DICTIONARY",
>                 "PLAIN",
>                 "RLE"
>             ]
>         },
>         {
>             "name": "concat('Hello', toString(modulo(number, 1000)))",
>             "path": "concat('Hello', toString(modulo(number, 1000)))",
>             "max_definition_level": "0",
>             "max_repetition_level": "0",
>             "physical_type": "BYTE_ARRAY",
>             "logical_type": "None",
>             "compression": "LZ4",
>             "total_uncompressed_size": "149115",
>             "total_compressed_size": "13340",
>             "space_saved": "91.05%",
>             "encodings": [
>                 "RLE_DICTIONARY",
>                 "PLAIN",
>                 "RLE"
>             ]
>         }
>     ],
>     "row_groups": [
>         {
>             "num_columns": "2",
>             "num_rows": "65409",
>             "total_uncompressed_size": "179809",
>             "total_compressed_size": "14163",
>             "columns": [
>                 {
>                     "name": "number",
>                     "path": "number",
>                     "total_compressed_size": "7070",
>                     "total_uncompressed_size": "85956",
>                     "have_statistics": true,
>                     "statistics": {
>                         "num_values": "65409",
>                         "null_count": "0",
>                         "distinct_count": null,
>                         "min": "0",
>                         "max": "999"
>                     }
>                 },
>                 {
>                     "name": "concat('Hello', toString(modulo(number, 1000)))",
>                     "path": "concat('Hello', toString(modulo(number, 1000)))",
>                     "total_compressed_size": "7093",
>                     "total_uncompressed_size": "93853",
>                     "have_statistics": true,
>                     "statistics": {
>                         "num_values": "65409",
>                         "null_count": "0",
>                         "distinct_count": null,
>                         "min": "Hello0",
>                         "max": "Hello999"
>                     }
>                 }
>             ]
>         }
> 
>     ]
> }
> ```

#### RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadata.MinMax
version: 1.0

[ClickHouse] SHALL support Parquet files that have Min/Max values in the metadata and the files that are missing Min/Max values.

### Metadata Types

#### RQ.SRS-032.ClickHouse.Parquet.Metadata.File
version: 1.0

[ClickHouse] SHALL support accessing `File Metadata` in Parquet files.

#### RQ.SRS-032.ClickHouse.Parquet.Metadata.Column
version: 1.0

[ClickHouse] SHALL support accessing `Column (Chunk) Metadata` in Parquet files.

#### RQ.SRS-032.ClickHouse.Parquet.Metadata.Header
version: 1.0

[ClickHouse] SHALL support accessing `Page Header Metadata` in Parquet files.

## Error Recovery

### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Metadata.MagicNumber
version: 1.0

[ClickHouse] SHALL output an error if the 4-byte magic number "PAR1" is missing from the Parquet metadata.

For example,

When using hexeditor on the Parquet file we alter the values of "PAR1" and change it to "PARQ".
then when we try to import that Parquet file to [ClickHouse] we SHALL get an exception:

```
exception. Code: 1001, type: parquet::ParquetInvalidOrCorruptedFileException,
e.what() = Invalid: Parquet magic bytes not found in footer.
Either the file is corrupted or this is not a Parquet file.
```

### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Metadata.File
version: 1.0

[ClickHouse] SHALL output an error when trying to access the corrupt `file` metadata.
In this case the file metadata is corrupt, the file is lost.

### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Metadata.Column
version: 1.0

[ClickHouse] SHALL output an error when trying to access the corrupt `column` metadata.
In this case that column chunk MAY be lost but column chunks for this column in other row groups SHALL be okay.

### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Metadata.PageHeader
version: 1.0

[ClickHouse] SHALL output an error when trying to access the corrupt `Page Header`.
In this case the remaining pages in that chunk SHALL be lost.

### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Metadata.PageData
version: 1.0

[ClickHouse] SHALL output an error when trying to access the corrupt `Page Data`.
In this case that page SHALL be lost.

### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Metadata.Checksum
version: 1.0

[ClickHouse] SHALL output an error if the Parquet file's checksum is corrupted.

### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values
version: 1.0

[ClickHouse] SHALL output an error when trying to access the corrupt column values.

Error message example,

> DB::Exception: Cannot extract table structure from Parquet format file.


#### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Date
version: 1.0

[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `date` values.


#### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Int
version: 1.0

[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `Int` values.

#### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.BigInt
version: 1.0

[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `BigInt` values.

#### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.SmallInt
version: 1.0

[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `SmallInt` values.

#### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.TinyInt
version: 1.0

[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `TinyInt` values.

#### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.UInt
version: 1.0

[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `UInt` values.

#### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.UBigInt
version: 1.0

[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `UBigInt` values.

#### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.USmallInt
version: 1.0

[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `USmallInt` values.

#### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.UTinyInt
version: 1.0

[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `UTinyInt` values.


#### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.TimestampUS
version: 1.0

[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `Timestamp (us)` values.

#### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.TimestampMS
version: 1.0

[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `Timestamp (ms)` values.

#### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Bool
version: 1.0

[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `BOOL` values.

#### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Float
version: 1.0

[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `FLOAT` values.

#### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Double
version: 1.0

[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `DOUBLE` values.

#### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.TimeMS
version: 1.0

[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `TIME (ms)` values.

#### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.TimeUS
version: 1.0

[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `TIME (us)` values.

#### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.TimeNS
version: 1.0

[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `TIME (ns)` values.

#### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.String
version: 1.0

[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `STRING` values.

#### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Binary
version: 1.0

[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `BINARY` values.

#### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.FixedLengthByteArray
version: 1.0

[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `FIXED_LENGTH_BYTE_ARRAY` values.

#### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Decimal
version: 1.0

[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `DECIMAL` values.

#### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.List
version: 1.0

[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `LIST` values.

#### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Struct
version: 1.0

[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `STRUCT` values.

#### RQ.SRS-032.ClickHouse.Parquet.ErrorRecovery.Corrupt.Values.Map
version: 1.0

[ClickHouse] SHALL output an error when trying to import the Parquet files with corrupt `MAP` values.

## Interoperability Between ARM and x86

### Importing and Exporting Parquet Files On ARM That Were Generated On x86 Machine

#### RQ.SRS-032.ClickHouse.Parquet.Interoperability.From.x86.To.ARM
version: 1.0

[ClickHouse] SHALL support importing and exporting parquet files on `ARM` machine that were generated on `x86` machine.

### Importing and Exporting Parquet Files On x86 That Were Generated On ARM Machine

#### RQ.SRS-032.ClickHouse.Parquet.Interoperability.From.ARM.To.x86
version: 1.0

[ClickHouse] SHALL support importing and exporting parquet files on `x86` machine that were generated on `ARM` machine.

[ClickHouse]: https://clickhouse.com
[GitHub Repository]: https://github.com/Altinity/clickhouse-regression/blob/main/parquet/requirements/requirements.md
[Revision History]: https://github.com/Altinity/clickhouse-regression/commits/main/parquet/requirements/requirements.md
[Git]: https://git-scm.com/
[GitHub]: https://github.com
""",
)
