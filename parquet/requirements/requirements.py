# These requirements were auto generated
# from software requirements specification (SRS)
# document by TestFlows v1.9.230315.1003122.
# Do not edit by hand but re-generate instead
# using 'tfs requirements generate' command.
from testflows.core import Specification
from testflows.core import Requirement

Heading = Specification.Heading

RQ_SRS_032_ClickHouse_SupportedDatatypes = Requirement(
    name="RQ.SRS-032.ClickHouse.SupportedDatatypes",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support all the following datatypes:\n"
        "\n"
        "| name                              | case_insensitive | alias_to data type |\n"
        "|-----------------------------------|------------------|--------------------|\n"
        "| `JSON`                            | 1                |                    |\n"
        "| `Polygon`                         | 0                |                    |\n"
        "| `Ring`                            | 0                |                    |\n"
        "| `Point`                           | 0                |                    |\n"
        "| `SimpleAggregateFunction`         | 0                |                    |\n"
        "| `IntervalQuarter`                 | 0                |                    |\n"
        "| `IntervalMonth`                   | 0                |                    |\n"
        "| `Int64`                           | 0                |                    |\n"
        "| `IntervalDay`                     | 0                |                    |\n"
        "| `IntervalHour`                    | 0                |                    |\n"
        "| `IPv4`                            | 0                |                    |\n"
        "| `IntervalSecond`                  | 0                |                    |\n"
        "| `LowCardinality`                  | 0                |                    |\n"
        "| `Int16`                           | 0                |                    |\n"
        "| `UInt256`                         | 0                |                    |\n"
        "| `AggregateFunction`               | 0                |                    |\n"
        "| `MultiPolygon`                    | 0                |                    |\n"
        "| `IPv6`                            | 0                |                    |\n"
        "| `Nothing`                         | 0                |                    |\n"
        "| `Decimal256`                      | 1                |                    |\n"
        "| `Tuple`                           | 0                |                    |\n"
        "| `Array`                           | 0                |                    |\n"
        "| `IntervalMicrosecond`             | 0                |                    |\n"
        "| `Bool`                            | 1                |                    |\n"
        "| `Enum16`                          | 0                |                    |\n"
        "| `IntervalMinute`                  | 0                |                    |\n"
        "| `FixedString`                     | 0                |                    |\n"
        "| `String`                          | 0                |                    |\n"
        "| `DateTime`                        | 1                |                    |\n"
        "| `Object`                          | 0                |                    |\n"
        "| `Map`                             | 0                |                    |\n"
        "| `UUID`                            | 0                |                    |\n"
        "| `Decimal64`                       | 1                |                    |\n"
        "| `Nullable`                        | 0                |                    |\n"
        "| `Enum`                            | 1                |                    |\n"
        "| `Int32`                           | 0                |                    |\n"
        "| `UInt8`                           | 0                |                    |\n"
        "| `Date`                            | 1                |                    |\n"
        "| `Decimal32`                       | 1                |                    |\n"
        "| `UInt128`                         | 0                |                    |\n"
        "| `Float64`                         | 0                |                    |\n"
        "| `Nested`                          | 0                |                    |\n"
        "| `UInt16`                          | 0                |                    |\n"
        "| `IntervalMillisecond`             | 0                |                    |\n"
        "| `Int128`                          | 0                |                    |\n"
        "| `Decimal128`                      | 1                |                    |\n"
        "| `Int8`                            | 0                |                    |\n"
        "| `Decimal`                         | 1                |                    |\n"
        "| `Int256`                          | 0                |                    |\n"
        "| `DateTime64`                      | 1                |                    |\n"
        "| `Enum8`                           | 0                |                    |\n"
        "| `DateTime32`                      | 1                |                    |\n"
        "| `Date32`                          | 1                |                    |\n"
        "| `IntervalWeek`                    | 0                |                    |\n"
        "| `UInt64`                          | 0                |                    |\n"
        "| `IntervalNanosecond`              | 0                |                    |\n"
        "| `IntervalYear`                    | 0                |                    |\n"
        "| `UInt32`                          | 0                |                    |\n"
        "| `Float32`                         | 0                |                    |\n"
        "| `bool`                            | 1                | `Bool`             |\n"
        "| `INET6`                           | 1                | `IPv6`             |\n"
        "| `INET4`                           | 1                | `IPv4`             |\n"
        "| `ENUM`                            | 1                | `Enum`             |\n"
        "| `BINARY`                          | 1                | `FixedString`      |\n"
        "| `GEOMETRY`                        | 1                | `String`           |\n"
        "| `NATIONAL CHAR VARYING`           | 1                | `String`           |\n"
        "| `BINARY VARYING`                  | 1                | `String`           |\n"
        "| `NCHAR LARGE OBJECT`              | 1                | `String`           |\n"
        "| `NATIONAL CHARACTER VARYING`      | 1                | `String`           |\n"
        "| `boolean`                         | 1                | `Bool`             |\n"
        "| `NATIONAL CHARACTER LARGE OBJECT` | 1                | `String`           |\n"
        "| `NATIONAL CHARACTER`              | 1                | `String`           |\n"
        "| `NATIONAL CHAR`                   | 1                | `String`           |\n"
        "| `CHARACTER VARYING`               | 1                | `String`           |\n"
        "| `LONGBLOB`                        | 1                | `String`           |\n"
        "| `TINYBLOB`                        | 1                | `String`           |\n"
        "| `MEDIUMTEXT`                      | 1                | `String`           |\n"
        "| `TEXT`                            | 1                | `String`           |\n"
        "| `VARCHAR2`                        | 1                | `String`           |\n"
        "| `CHARACTER LARGE OBJECT`          | 1                | `String`           |\n"
        "| `DOUBLE PRECISION`                | 1                | `Float64`          |\n"
        "| `LONGTEXT`                        | 1                | `String`           |\n"
        "| `NVARCHAR`                        | 1                | `String`           |\n"
        "| `INT1 UNSIGNED`                   | 1                | `UInt8`            |\n"
        "| `VARCHAR`                         | 1                | `String`           |\n"
        "| `CHAR VARYING`                    | 1                | `String`           |\n"
        "| `MEDIUMBLOB`                      | 1                | `String`           |\n"
        "| `NCHAR`                           | 1                | `String`           |\n"
        "| `VARBINARY`                       | 1                | `String`           |\n"
        "| `CHAR`                            | 1                | `String`           |\n"
        "| `SMALLINT UNSIGNED`               | 1                | `UInt16`           |\n"
        "| `TIMESTAMP`                       | 1                | `DateTime`         |\n"
        "| `FIXED`                           | 1                | `Decimal`          |\n"
        "| `TINYTEXT`                        | 1                | `String`           |\n"
        "| `NUMERIC`                         | 1                | `Decimal`          |\n"
        "| `DEC`                             | 1                | `Decimal`          |\n"
        "| `TIME`                            | 1                | `Int64`            |\n"
        "| `FLOAT`                           | 1                | `Float32`          |\n"
        "| `SET`                             | 1                | `UInt64`           |\n"
        "| `TINYINT UNSIGNED`                | 1                | `UInt8`            |\n"
        "| `INTEGER UNSIGNED`                | 1                | `UInt32`           |\n"
        "| `INT UNSIGNED`                    | 1                | `UInt32`           |\n"
        "| `CLOB`                            | 1                | `String`           |\n"
        "| `MEDIUMINT UNSIGNED`              | 1                | `UInt32`           |\n"
        "| `BLOB`                            | 1                | `String`           |\n"
        "| `REAL`                            | 1                | `Float32`          |\n"
        "| `SMALLINT`                        | 1                | `Int16`            |\n"
        "| `INTEGER SIGNED`                  | 1                | `Int32`            |\n"
        "| `NCHAR VARYING`                   | 1                | `String`           |\n"
        "| `INT SIGNED`                      | 1                | `Int32`            |\n"
        "| `TINYINT SIGNED`                  | 1                | `Int8`             |\n"
        "| `BIGINT SIGNED`                   | 1                | `Int64`            |\n"
        "| `BINARY LARGE OBJECT`             | 1                | `String`           |\n"
        "| `SMALLINT SIGNED`                 | 1                | `Int16`            |\n"
        "| `YEAR`                            | 1                | `UInt16`           |\n"
        "| `MEDIUMINT`                       | 1                | `Int32`            |\n"
        "| `INTEGER`                         | 1                | `Int32`            |\n"
        "| `INT1 SIGNED`                     | 1                | `Int8`             |\n"
        "| `BIT`                             | 1                | `UInt64`           |\n"
        "| `BIGINT UNSIGNED`                 | 1                | `UInt64`           |\n"
        "| `BYTEA`                           | 1                | `String`           |\n"
        "| `INT`                             | 1                | `Int32`            |\n"
        "| `SINGLE`                          | 1                | `Float32`          |\n"
        "| `MEDIUMINT SIGNED`                | 1                | `Int32`            |\n"
        "| `DOUBLE`                          | 1                | `Float64`          |\n"
        "| `INT1`                            | 1                | `Int8`             |\n"
        "| `CHAR LARGE OBJECT`               | 1                | `String`           |\n"
        "| `TINYINT`                         | 1                | `Int8`             |\n"
        "| `BIGINT`                          | 1                | `Int64`            |\n"
        "| `CHARACTER`                       | 1                | `String`           |\n"
        "| `BYTE`                            | 1                | `Int8`             |\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.1.1",
)

RQ_SRS_032_ClickHouse_Parquet = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=("[ClickHouse] SHALL support `Parquet` data format.\n" "\n"),
    link=None,
    level=3,
    num="4.1.2",
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
    level=3,
    num="4.1.3",
)

RQ_SRS_032_ClickHouse_Parquet_Encryption = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Encryption",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] MAY not support reading or writing encrypted Parquet files.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.1.4",
)

RQ_SRS_032_ClickHouse_Parquet_Chunks = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Chunks",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=("[ClickHouse] SHALL support chunked `Parquet` files.\n" "\n"),
    link=None,
    level=3,
    num="4.1.5",
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
    level=3,
    num="4.1.6",
)

RQ_SRS_032_ClickHouse_Parquet_ReadChunkedColumns = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.ReadChunkedColumns",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support reading chunked columns from the Parquet files.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.1.7",
)

RQ_SRS_032_ClickHouse_Parquet_WriteChunkedColumns = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.WriteChunkedColumns",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support writing chunked columns into the Parquet files.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.1.8",
)

RQ_SRS_032_ClickHouse_Parquet_SupportedVersions = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.SupportedVersions",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support reading the following Parquet file versions: `1.0.0`, `2.0.0`, `2.1.0`, `2.2.0`, `2.4.0`, `2.6.0`, `2.7.0`, `2.8.0`, `2.9.0`.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.1.9",
)

RQ_SRS_032_ClickHouse_Parquet_Compression_None = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Compression.None",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support reading or writing uncompressed Parquet files.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.2.1",
)

RQ_SRS_032_ClickHouse_Parquet_Compression_Gzip = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Compression.Gzip",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support reading or writing Parquet files compressed using gzip.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.2.2",
)

RQ_SRS_032_ClickHouse_Parquet_Compression_Brotli = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Compression.Brotli",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support reading or writing Parquet files compressed using brotli.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.2.3",
)

RQ_SRS_032_ClickHouse_Parquet_Compression_Lz4 = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Compression.Lz4",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support reading or writing Parquet files compressed using lz4.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.2.4",
)

RQ_SRS_032_ClickHouse_Parquet_Compression_Lz4Raw = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Compression.Lz4Raw",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support reading or writing Parquet files compressed using lz4_raw.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.2.5",
)

RQ_SRS_032_ClickHouse_Parquet_UnsupportedCompression_Snappy = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.UnsupportedCompression.Snappy",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] MAY not support reading or writing Parquet files compressed using snapy.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.3.1",
)

RQ_SRS_032_ClickHouse_Parquet_UnsupportedCompression_Lzo = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.UnsupportedCompression.Lzo",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] MAY not support reading or writing Parquet files compressed using lzo.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.3.2",
)

RQ_SRS_032_ClickHouse_Parquet_UnsupportedCompression_Zstd = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.UnsupportedCompression.Zstd",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] MAY not support reading or writing Parquet files compressed using zstd.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.3.3",
)

RQ_SRS_032_ClickHouse_Parquet_DataTypes_Read = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.Read",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support reading the following Parquet data types:\n"
        "Parquet Decimal is currently not tested.\n"
        "\n"
        "| Parquet data type (INSERT)                    | ClickHouse data type                  |\n"
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
        "\n"
    ),
    link=None,
    level=3,
    num="4.4.1",
)

RQ_SRS_032_ClickHouse_Parquet_DataTypes_DateUTCAdjusted = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.DateUTCAdjusted",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support reading `DATE` Parquet datatype with `isAdjustedToUTC = true`.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.4.2",
)

RQ_SRS_032_ClickHouse_Parquet_DataTypes_TimestampUTCAdjusted = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.TimestampUTCAdjusted",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support reading `TIMESTAMP` Parquet datatype with `isAdjustedToUTC = true`.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.4.3",
)

RQ_SRS_032_ClickHouse_Parquet_DataTypes_TimeUTCAdjusted = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.TimeUTCAdjusted",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support reading `TIME` Parquet datatype with `isAdjustedToUTC = true`.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.4.4",
)

RQ_SRS_032_ClickHouse_Parquet_DataTypes_ReadNested = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.ReadNested",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support reading nested: `Array`, `Tuple` and `Map` datatypes in Parquet files.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.4.5",
)

RQ_SRS_032_ClickHouse_Parquet_DataTypes_NullValues = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.NullValues",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support reading columns that have `Null` values in Parquet files. If the target [ClickHouse] column is not `Nullable` then the `Null` value should be converted to the default values for the target column datatype.\n"
        "\n"
        "For example, if the target column has `Int32`, then the `Null` value will be replaced with `0`.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.4.6",
)

RQ_SRS_032_ClickHouse_Parquet_DataTypes_ReadInto_Nullable = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.ReadInto.Nullable",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support reading Parquet files into target table's `Nullable` datatype columns.\n"
        "\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.4.7",
)

RQ_SRS_032_ClickHouse_Parquet_DataTypes_ReadInto_LowCardinality = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.ReadInto.LowCardinality",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support reading Parquet files into target table's `LowCardinality` datatype columns.\n"
        "\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.4.8",
)

RQ_SRS_032_ClickHouse_Parquet_DataTypes_ReadInto_Nested = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.ReadInto.Nested",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support reading Parquet files into target table's `Nested` datatype columns.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.4.9",
)

RQ_SRS_032_ClickHouse_Parquet_DataTypes_ReadInto_Unknown = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.ReadInto.Unknown",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support reading Parquet files with `UNKNOWN` logical type.\n"
        "\n"
        "The example as to why the Parquet might have an `UNKNOWN` types is as follows,\n"
        "\n"
        "> Sometimes, when discovering the schema of existing data, values are always null and there's no type information. \n"
        "> The UNKNOWN type can be used to annotate a column that is always null. (Similar to Null type in Avro and Arrow)\n"
        "\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.4.10",
)

RQ_SRS_032_ClickHouse_Parquet_DataTypes_Write = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.Write",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support writing the following datatypes to Parquet:\n"
        "\n"
        "| Parquet data type (SELECT) | ClickHouse data type                  |\n"
        "|----------------------------|---------------------------------------|\n"
        "| `BOOL`                     | `Bool`                                |\n"
        "| `UINT8`                    | `UInt8`                               |\n"
        "| `INT8`                     | `Int8`/`Enum8`                        |\n"
        "| `UINT16`                   | `UInt16`                              |\n"
        "| `INT16`                    | `Int16`/`Enum16`                      |\n"
        "| `UINT32`                   | `UInt32`                              |\n"
        "| `INT32`                    | `Int32`                               |\n"
        "| `UINT64`                   | `UInt64`                              |\n"
        "| `INT64`                    | `Int64`                               |\n"
        "| `FLOAT`                    | `Float32`                             |\n"
        "| `DOUBLE`                   | `Float64`                             |\n"
        "| `DATE`                     | `Date32`                              |\n"
        "| `UINT32`                   | `DateTime`                            |\n"
        "| `TIMESTAMP`                | `DateTime64`                          |\n"
        "| `BINARY`                   | `String`                              |\n"
        "| `FIXED_LENGTH_BYTE_ARRAY`  | `FixedString`                         |\n"
        "| `DECIMAL`                  | `Decimal`                             |\n"
        "| `LIST`                     | `Array`                               |\n"
        "| `STRUCT`                   | `Tuple`                               |\n"
        "| `MAP`                      | `Map`                                 |\n"
        "| `UINT32`                   | `IPv4`                                |\n"
        "| `FIXED_LENGTH_BYTE_ARRAY`  | `IPv6`                                |\n"
        "| `FIXED_LENGTH_BYTE_ARRAY`  | `Int128`/`UInt128`/`Int256`/`UInt256` |\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.4.11",
)

RQ_SRS_032_ClickHouse_Parquet_DataTypes_WriteNested = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.WriteNested",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support writing nested: `Array`, `Tuple` and `Map` datatypes in Parquet files.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.4.12",
)

RQ_SRS_032_ClickHouse_Parquet_DataTypes_WriteNullable = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.WriteNullable",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support writing `Nullable` datatypes in Parquet files and `Nullable` datatypes that consist only of `Null`.\n"
        "\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.4.13",
)

RQ_SRS_032_ClickHouse_Parquet_DataTypes_TypeConversionFunction = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.TypeConversionFunction",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support using type conversion functions when reading Parquet files.\n"
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
        "The conversion MAY not be possible between some datatypes.\n"
        "\n"
        "For example,\n"
        "\n"
        "`Bool` -> `IPv6`\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.4.14",
)

RQ_SRS_032_ClickHouse_Parquet_UnsupportedParquetTypes = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.UnsupportedParquetTypes",
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
        "\n"
    ),
    link=None,
    level=3,
    num="4.5.1",
)

RQ_SRS_032_ClickHouse_Parquet_UnsupportedParquetTypes_ChunkedArray = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.UnsupportedParquetTypes.ChunkedArray",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=("[ClickHouse] MAY not support Parquet chunked arrays.\n" "\n"),
    link=None,
    level=3,
    num="4.5.2",
)

RQ_SRS_032_ClickHouse_Parquet_Insert = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Insert",
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
    level=3,
    num="4.6.1",
)

RQ_SRS_032_ClickHouse_Parquet_Insert_AutoDetectParquetFileFormat = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Insert.AutoDetectParquetFileFormat",
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
    num="4.6.2",
)

RQ_SRS_032_ClickHouse_Parquet_Insert_Projections = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Insert.Projections",
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
    num="4.6.3",
)

RQ_SRS_032_ClickHouse_Parquet_Insert_SkipColumns = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Insert.SkipColumns",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support skipping unexistent columns when reading from Parquet files.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.6.4",
)

RQ_SRS_032_ClickHouse_Parquet_Insert_SkipValues = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Insert.SkipValues",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support skipping unsupported values when reading from Parquet files. When the values are being skipped, the inserted values SHALL be the default value for the corresponding column's datatype.\n"
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
    num="4.6.5",
)

RQ_SRS_032_ClickHouse_Parquet_Insert_AutoTypecast = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Insert.AutoTypecast",
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
    num="4.6.6",
)

RQ_SRS_032_ClickHouse_Parquet_Insert_RowGroupSize = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Insert.RowGroupSize",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support reading Parquet files with different Row Group Sizes.\n"
        "\n"
        "As described in https://parquet.apache.org/docs/file-format/configurations/#row-group-size,\n"
        "\n"
        "> We recommend large row groups (512MB - 1GB). Since an entire row group might need to be read, \n"
        "> we want it to completely fit on one HDFS block.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.6.7",
)

RQ_SRS_032_ClickHouse_Parquet_Insert_DataPageSize = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Insert.DataPageSize",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support reading Parquet files with different Data Page Sizes.\n"
        "\n"
        "As described in https://parquet.apache.org/docs/file-format/configurations/#data-page--size,\n"
        "\n"
        "> Note: for sequential scans, it is not expected to read a page at a time; this is not the IO chunk. We recommend 8KB for page sizes.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.6.8",
)

RQ_SRS_032_ClickHouse_Parquet_Insert_Settings_ImportNested = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Insert.Settings.ImportNested",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support specifying `input_format_parquet_import_nested` to allow inserting arrays of\n"
        "nested structs into Nested tables. The default value SHALL be `0`.\n"
        "\n"
        "- `0` — Data can not be inserted into Nested columns as an array of structs.\n"
        "- `1` — Data can be inserted into Nested columns as an array of structs.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.6.9.1",
)

RQ_SRS_032_ClickHouse_Parquet_Insert_Settings_CaseInsensitiveColumnMatching = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Insert.Settings.CaseInsensitiveColumnMatching",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support specifying `input_format_parquet_case_insensitive_column_matching` to ignore matching\n"
        "Parquet and ClickHouse columns. The default value SHALL be `0`.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.6.9.2",
)

RQ_SRS_032_ClickHouse_Parquet_Insert_Settings_AllowMissingColumns = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Insert.Settings.AllowMissingColumns",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support specifying `input_format_parquet_allow_missing_columns` to allow missing columns.\n"
        "The default value SHALL be `0`.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.6.9.3",
)

RQ_SRS_032_ClickHouse_Parquet_Insert_Settings_SkipColumnsWithUnsupportedTypesInSchemaInference = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Insert.Settings.SkipColumnsWithUnsupportedTypesInSchemaInference",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support specifying `input_format_parquet_skip_columns_with_unsupported_types_in_schema_inference`\n"
        "to allow skipping unsupported types. The default value SHALL be `0`.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.6.9.4",
)

RQ_SRS_032_ClickHouse_Parquet_Nested_ArrayIntoNested_ReadNested = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Nested.ArrayIntoNested.ReadNested",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support reading nested columns from the Parquet file.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.7.1",
)

RQ_SRS_032_ClickHouse_Parquet_Nested_ArrayIntoNested_ImportNested = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Nested.ArrayIntoNested.ImportNested",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support inserting arrays of nested structs from Parquet files into [ClickHouse] Nested columns when `input_format_parquet_import_nested` setting is set to `1`.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.7.2",
)

RQ_SRS_032_ClickHouse_Parquet_Nested_ArrayIntoNested_NotImportNested = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Nested.ArrayIntoNested.NotImportNested",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL return an error when trying to insert arrays of nested structs from Parquet files into [ClickHouse] Nested columns when\n"
        "`input_format_parquet_import_nested` setting is set to `0`.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.7.3",
)

RQ_SRS_032_ClickHouse_Parquet_Nested_ArrayIntoNotNested = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Nested.ArrayIntoNotNested",
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
    num="4.7.4",
)

RQ_SRS_032_ClickHouse_Parquet_Nested_NonArrayIntoNested = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Nested.NonArrayIntoNested",
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
    num="4.7.5",
)

RQ_SRS_032_ClickHouse_Parquet_Nested_ArrayIntoNested_WriteNested = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Nested.ArrayIntoNested.WriteNested",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support writing nested columns to the Parquet file.\n" "\n"
    ),
    link=None,
    level=3,
    num="4.7.6",
)

RQ_SRS_032_ClickHouse_Parquet_Select = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Select",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support using `SELECT` query with either the `INTO OUTFILE {file_name}` or just `FORMAT Parquet` clauses to write Parquet files. \n"
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
    num="4.8.1",
)

RQ_SRS_032_ClickHouse_Parquet_Select_Outfile_AutoDetectParquetFileFormat = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Select.Outfile.AutoDetectParquetFileFormat",
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
    level=3,
    num="4.8.2",
)

RQ_SRS_032_ClickHouse_Parquet_Select_Join = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Select.Join",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support writing output of `SELECT` query with a `JOIN` clause into a Parquet file.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.8.3",
)

RQ_SRS_032_ClickHouse_Parquet_Select_Union = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Select.Union",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support writing output of `SELECT` query with a `UNION` clause into a Parquet file.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.8.4",
)

RQ_SRS_032_ClickHouse_Parquet_Select_View = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Select.View",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support writing output of `SELECT * FROM {view_name}` query into a Parquet file.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.8.5",
)

RQ_SRS_032_ClickHouse_Parquet_Select_MaterializedView = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Select.MaterializedView",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support writing output of `SELECT * FROM {mat_view_name}` query into a Parquet file.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.8.6",
)

RQ_SRS_032_ClickHouse_Parquet_Select_Settings_RowGroupSize = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Select.Settings.RowGroupSize",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support specifying `output_format_parquet_row_group_size` row group size by row count.\n"
        "The default value SHALL be `1000000`.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.8.7.1",
)

RQ_SRS_032_ClickHouse_Parquet_Select_Settings_StringAsString = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Select.Settings.StringAsString",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support specifying `output_format_parquet_string_as_string` to use Parquet String type instead of Binary.\n"
        "The default value SHALL be `0`.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.8.7.2",
)

RQ_SRS_032_ClickHouse_Parquet_Select_Settings_StringAsFixedByteArray = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Select.Settings.StringAsFixedByteArray",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support specifying `output_format_parquet_fixed_string_as_fixed_byte_array` to use Parquet FIXED_LENGTH_BYTE_ARRAY type instead of Binary/String for FixedString columns. The default value SHALL be `1`.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.8.7.3",
)

RQ_SRS_032_ClickHouse_Parquet_Select_Settings_ParquetVersion = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Select.Settings.ParquetVersion",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support specifying `output_format_parquet_version` to set the version of Parquet used in the output file.\n"
        "The default value SHALL be `2.latest`.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.8.7.4",
)

RQ_SRS_032_ClickHouse_Parquet_Select_Settings_CompressionMethod = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Select.Settings.CompressionMethod",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support specifying `output_format_parquet_compression_method` to set the compression method used in the Parquet file.\n"
        "The default value SHALL be `lz4`.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.8.7.5",
)

RQ_SRS_032_ClickHouse_Parquet_Create_NewTable = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Create.NewTable",
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
    level=4,
    num="4.9.7.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableFunctions_URL = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.URL",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `url` table function reading and writing Parquet format.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.10.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableFunctions_File = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.File",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `file` table function reading and writing Parquet format.\n"
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
    num="4.10.2",
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
    level=4,
    num="4.10.2.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableFunctions_S3 = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.S3",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `s3` table function for reading and writing Parquet format.\n"
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
    num="4.10.3",
)

RQ_SRS_032_ClickHouse_Parquet_TableFunctions_JDBC = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.JDBC",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `jdbc` table function for reading and writing Parquet format.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.10.4",
)

RQ_SRS_032_ClickHouse_Parquet_TableFunctions_ODBC = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.ODBC",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `odbc` table function for reading and writing Parquet format.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.10.5",
)

RQ_SRS_032_ClickHouse_Parquet_TableFunctions_HDFS = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.HDFS",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `hdfs` table function for reading and writing Parquet format.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.10.6",
)

RQ_SRS_032_ClickHouse_Parquet_TableFunctions_Remote = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.Remote",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `remote` table function for reading and writing Parquet format.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.10.7",
)

RQ_SRS_032_ClickHouse_Parquet_TableFunctions_MySQL = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.MySQL",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `mysql` table function for reading and writing Parquet format.\n"
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
        "> We can write to a Parquet file format with:\n"
        "> \n"
        "> ```sql\n"
        "> SELECT * FROM mysql_table1 INTO OUTFILE testTable.parquet FORMAT Parquet\n"
        "> ```\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.10.8",
)

RQ_SRS_032_ClickHouse_Parquet_TableFunctions_PostgreSQL = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.PostgreSQL",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `postgresql` table function reading and writing Parquet format.\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.10.9",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_MergeTree_MergeTree = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.MergeTree",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being writen into and read from a `MergeTree` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.11.1.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_MergeTree_ReplicatedMergeTree = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.ReplicatedMergeTree",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being writen into and read from a `ReplicatedMergeTree` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.11.1.2",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_MergeTree_ReplacingMergeTree = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.ReplacingMergeTree",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being writen into and read from a `ReplacingMergeTree` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.11.1.3",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_MergeTree_SummingMergeTree = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.SummingMergeTree",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being writen into and read from a `SummingMergeTree` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.11.1.4",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_MergeTree_AggregatingMergeTree = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.AggregatingMergeTree",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being writen into and read from a `AggregatingMergeTree` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.11.1.5",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_MergeTree_CollapsingMergeTree = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.CollapsingMergeTree",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being writen into and read from a `CollapsingMergeTree` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.11.1.6",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_MergeTree_VersionedCollapsingMergeTree = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.VersionedCollapsingMergeTree",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being writen into and read from a `VersionedCollapsingMergeTree` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.11.1.7",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_MergeTree_GraphiteMergeTree = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.GraphiteMergeTree",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being writen into and read from a `GraphiteMergeTree` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.11.1.8",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_ODBC = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.ODBC",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being writen into and read from an `ODBC` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.11.2.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_JDBC = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.JDBC",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being writen into and read from a `JDBC` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.11.2.2",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_MySQL = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.MySQL",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being writen into and read from a `MySQL` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.11.2.3",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_MongoDB = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.MongoDB",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being writen into and read from a `MongoDB` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.11.2.4",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_HDFS = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.HDFS",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being writen into and read from a `HDFS` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.11.2.5",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_S3 = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.S3",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being writen into and read from an `S3` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.11.2.6",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_Kafka = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.Kafka",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being writen into and read from a `Kafka` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.11.2.7",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_EmbeddedRocksDB = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.EmbeddedRocksDB",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being writen into and read from an `EmbeddedRocksDB` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.11.2.8",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Integration_PostgreSQL = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.PostgreSQL",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being writen into and read from a `PostgreSQL` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.11.2.9",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Special_Memory = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.Memory",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being writen into and read from a `Memory` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.11.3.1",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Special_Distributed = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.Distributed",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being writen into and read from a `Distributed` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.11.3.2",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Special_Dictionary = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.Dictionary",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being writen into and read from a `Dictionary` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.11.3.3",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Special_File = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.File",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being writen into and read from a `File` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.11.3.4",
)

RQ_SRS_032_ClickHouse_Parquet_TableEngines_Special_URL = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.URL",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support Parquet format being writen into and read from a `URL` table engine.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.11.3.5",
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
    level=4,
    num="4.12.1.1",
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
    level=4,
    num="4.12.1.2",
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
    level=4,
    num="4.12.1.3",
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
    level=4,
    num="4.12.1.4",
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
    level=4,
    num="4.12.2.1",
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
    level=4,
    num="4.12.2.2",
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
    level=4,
    num="4.12.2.3",
)

RQ_SRS_032_ClickHouse_Parquet_Metadata_ErrorRecovery_MissingMagicNumber = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.MissingMagicNumber",
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
        "then when we try to read that Parquet file in [ClickHouse] we SHALL get an exception:\n"
        "\n"
        "```\n"
        "exception. Code: 1001, type: parquet::ParquetInvalidOrCorruptedFileException,\n"
        "e.what() = Invalid: Parquet magic bytes not found in footer.\n"
        "Either the file is corrupted or this is not a Parquet file.\n"
        "```\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.13.1",
)

RQ_SRS_032_ClickHouse_Parquet_Metadata_ErrorRecovery_CorruptFile = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.CorruptFile",
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
    level=3,
    num="4.13.2",
)

RQ_SRS_032_ClickHouse_Parquet_Metadata_ErrorRecovery_CorruptColumn = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.CorruptColumn",
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
    level=3,
    num="4.13.3",
)

RQ_SRS_032_ClickHouse_Parquet_Metadata_ErrorRecovery_CorruptPageHeader = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.CorruptPageHeader",
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
    level=3,
    num="4.13.4",
)

RQ_SRS_032_ClickHouse_Parquet_Metadata_ErrorRecovery_CorruptPageData = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.CorruptPageData",
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
    level=3,
    num="4.13.5",
)

RQ_SRS_032_ClickHouse_Parquet_Metadata_ErrorRecovery_CorruptColumnValues = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.CorruptColumnValues",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL output an error when trying to access the corrupt column values.\n"
        "\n"
        "\n"
    ),
    link=None,
    level=3,
    num="4.13.6",
)

RQ_SRS_032_ClickHouse_Parquet_Metadata_ErrorRecovery_CorruptChecksum = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.CorruptChecksum",
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
    level=3,
    num="4.13.7",
)

RQ_SRS_032_ClickHouse_Parquet_Encoding_Plain = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Encoding.Plain",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=("[ClickHouse] SHALL support `Plain` encoded Parquet files.\n" "\n"),
    link=None,
    level=4,
    num="4.14.7.1",
)

RQ_SRS_032_ClickHouse_Parquet_Encoding_RunLength = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Encoding.RunLength",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `Run Length Encoding / Bit-Packing Hybrid` encoded Parquet files.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.14.7.2",
)

RQ_SRS_032_ClickHouse_Parquet_Encoding_Delta = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Encoding.Delta",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `Delta Encoding` encoded Parquet files.\n" "\n" "\n"
    ),
    link=None,
    level=4,
    num="4.14.7.3",
)

RQ_SRS_032_ClickHouse_Parquet_Encoding_DeltaLengthByteArray = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Encoding.DeltaLengthByteArray",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `Delta-length byte array` encoded Parquet files.\n"
        "\n"
    ),
    link=None,
    level=4,
    num="4.14.7.4",
)

RQ_SRS_032_ClickHouse_Parquet_Encoding_DeltaStrings = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Encoding.DeltaStrings",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `Delta Strings` encoded Parquet files.\n" "\n"
    ),
    link=None,
    level=4,
    num="4.14.7.5",
)

RQ_SRS_032_ClickHouse_Parquet_Encoding_ByteStreamSplit = Requirement(
    name="RQ.SRS-032.ClickHouse.Parquet.Encoding.ByteStreamSplit",
    version="1.0",
    priority=None,
    group=None,
    type=None,
    uid=None,
    description=(
        "[ClickHouse] SHALL support `Byte Stream Split` encoded Parquet files.\n"
        "\n"
        "[ClickHouse]: https://clickhouse.com\n"
        "[GitHub Repository]: https://github.com/Altinity/clickhouse-regression/blob/main/parquet/requirements/requirements.md\n"
        "[Revision History]: https://github.com/Altinity/clickhouse-regression/commits/main/parquet/requirements/requirements.md\n"
        "[Git]: https://git-scm.com/\n"
        "[GitHub]: https://github.com\n"
    ),
    link=None,
    level=4,
    num="4.14.7.6",
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
        Heading(name="Requirements", level=1, num="4"),
        Heading(name="General", level=2, num="4.1"),
        Heading(name="RQ.SRS-032.ClickHouse.SupportedDatatypes", level=3, num="4.1.1"),
        Heading(name="RQ.SRS-032.ClickHouse.Parquet", level=3, num="4.1.2"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ClickHouseLocal", level=3, num="4.1.3"
        ),
        Heading(name="RQ.SRS-032.ClickHouse.Parquet.Encryption", level=3, num="4.1.4"),
        Heading(name="RQ.SRS-032.ClickHouse.Parquet.Chunks", level=3, num="4.1.5"),
        Heading(name="RQ.SRS-032.ClickHouse.Parquet.Structure", level=3, num="4.1.6"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.ReadChunkedColumns",
            level=3,
            num="4.1.7",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.WriteChunkedColumns",
            level=3,
            num="4.1.8",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.SupportedVersions", level=3, num="4.1.9"
        ),
        Heading(name="Compression", level=2, num="4.2"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Compression.None", level=3, num="4.2.1"
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Compression.Gzip", level=3, num="4.2.2"
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Compression.Brotli",
            level=3,
            num="4.2.3",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Compression.Lz4", level=3, num="4.2.4"
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Compression.Lz4Raw",
            level=3,
            num="4.2.5",
        ),
        Heading(name="Unsupported Compression", level=2, num="4.3"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.UnsupportedCompression.Snappy",
            level=3,
            num="4.3.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.UnsupportedCompression.Lzo",
            level=3,
            num="4.3.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.UnsupportedCompression.Zstd",
            level=3,
            num="4.3.3",
        ),
        Heading(name="Data Types", level=2, num="4.4"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.Read", level=3, num="4.4.1"
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.DateUTCAdjusted",
            level=3,
            num="4.4.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.TimestampUTCAdjusted",
            level=3,
            num="4.4.3",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.TimeUTCAdjusted",
            level=3,
            num="4.4.4",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.ReadNested",
            level=3,
            num="4.4.5",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.NullValues",
            level=3,
            num="4.4.6",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.ReadInto.Nullable",
            level=3,
            num="4.4.7",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.ReadInto.LowCardinality",
            level=3,
            num="4.4.8",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.ReadInto.Nested",
            level=3,
            num="4.4.9",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.ReadInto.Unknown",
            level=3,
            num="4.4.10",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.Write", level=3, num="4.4.11"
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.WriteNested",
            level=3,
            num="4.4.12",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.WriteNullable",
            level=3,
            num="4.4.13",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.DataTypes.TypeConversionFunction",
            level=3,
            num="4.4.14",
        ),
        Heading(name="Unsupported Parquet Types", level=2, num="4.5"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.UnsupportedParquetTypes",
            level=3,
            num="4.5.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.UnsupportedParquetTypes.ChunkedArray",
            level=3,
            num="4.5.2",
        ),
        Heading(name="INSERT", level=2, num="4.6"),
        Heading(name="RQ.SRS-032.ClickHouse.Parquet.Insert", level=3, num="4.6.1"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Insert.AutoDetectParquetFileFormat",
            level=3,
            num="4.6.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Insert.Projections",
            level=3,
            num="4.6.3",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Insert.SkipColumns",
            level=3,
            num="4.6.4",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Insert.SkipValues", level=3, num="4.6.5"
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Insert.AutoTypecast",
            level=3,
            num="4.6.6",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Insert.RowGroupSize",
            level=3,
            num="4.6.7",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Insert.DataPageSize",
            level=3,
            num="4.6.8",
        ),
        Heading(name="INSERT Settings", level=3, num="4.6.9"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Insert.Settings.ImportNested",
            level=4,
            num="4.6.9.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Insert.Settings.CaseInsensitiveColumnMatching",
            level=4,
            num="4.6.9.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Insert.Settings.AllowMissingColumns",
            level=4,
            num="4.6.9.3",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Insert.Settings.SkipColumnsWithUnsupportedTypesInSchemaInference",
            level=4,
            num="4.6.9.4",
        ),
        Heading(name="Working With Nested Types", level=2, num="4.7"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Nested.ArrayIntoNested.ReadNested",
            level=3,
            num="4.7.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Nested.ArrayIntoNested.ImportNested",
            level=3,
            num="4.7.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Nested.ArrayIntoNested.NotImportNested",
            level=3,
            num="4.7.3",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Nested.ArrayIntoNotNested",
            level=3,
            num="4.7.4",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Nested.NonArrayIntoNested",
            level=3,
            num="4.7.5",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Nested.ArrayIntoNested.WriteNested",
            level=3,
            num="4.7.6",
        ),
        Heading(name="SELECT", level=2, num="4.8"),
        Heading(name="RQ.SRS-032.ClickHouse.Parquet.Select", level=3, num="4.8.1"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Select.Outfile.AutoDetectParquetFileFormat",
            level=3,
            num="4.8.2",
        ),
        Heading(name="RQ.SRS-032.ClickHouse.Parquet.Select.Join", level=3, num="4.8.3"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Select.Union", level=3, num="4.8.4"
        ),
        Heading(name="RQ.SRS-032.ClickHouse.Parquet.Select.View", level=3, num="4.8.5"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Select.MaterializedView",
            level=3,
            num="4.8.6",
        ),
        Heading(name="SELECT Settings", level=3, num="4.8.7"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Select.Settings.RowGroupSize",
            level=4,
            num="4.8.7.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Select.Settings.StringAsString",
            level=4,
            num="4.8.7.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Select.Settings.StringAsFixedByteArray",
            level=4,
            num="4.8.7.3",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Select.Settings.ParquetVersion",
            level=4,
            num="4.8.7.4",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Select.Settings.CompressionMethod",
            level=4,
            num="4.8.7.5",
        ),
        Heading(name="CREATE", level=2, num="4.9"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Create.NewTable", level=4, num="4.9.7.1"
        ),
        Heading(name="Table Functions", level=2, num="4.10"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.URL",
            level=3,
            num="4.10.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.File",
            level=3,
            num="4.10.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.File.AutoDetectParquetFileFormat",
            level=4,
            num="4.10.2.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.S3",
            level=3,
            num="4.10.3",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.JDBC",
            level=3,
            num="4.10.4",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.ODBC",
            level=3,
            num="4.10.5",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.HDFS",
            level=3,
            num="4.10.6",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.Remote",
            level=3,
            num="4.10.7",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.MySQL",
            level=3,
            num="4.10.8",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableFunctions.PostgreSQL",
            level=3,
            num="4.10.9",
        ),
        Heading(name="Table Engines", level=2, num="4.11"),
        Heading(name="MergeTree", level=3, num="4.11.1"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.MergeTree",
            level=4,
            num="4.11.1.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.ReplicatedMergeTree",
            level=4,
            num="4.11.1.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.ReplacingMergeTree",
            level=4,
            num="4.11.1.3",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.SummingMergeTree",
            level=4,
            num="4.11.1.4",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.AggregatingMergeTree",
            level=4,
            num="4.11.1.5",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.CollapsingMergeTree",
            level=4,
            num="4.11.1.6",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.VersionedCollapsingMergeTree",
            level=4,
            num="4.11.1.7",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.GraphiteMergeTree",
            level=4,
            num="4.11.1.8",
        ),
        Heading(name="Integration Engines", level=3, num="4.11.2"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.ODBC",
            level=4,
            num="4.11.2.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.JDBC",
            level=4,
            num="4.11.2.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.MySQL",
            level=4,
            num="4.11.2.3",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.MongoDB",
            level=4,
            num="4.11.2.4",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.HDFS",
            level=4,
            num="4.11.2.5",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.S3",
            level=4,
            num="4.11.2.6",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.Kafka",
            level=4,
            num="4.11.2.7",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.EmbeddedRocksDB",
            level=4,
            num="4.11.2.8",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.PostgreSQL",
            level=4,
            num="4.11.2.9",
        ),
        Heading(name="Special Engines", level=3, num="4.11.3"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.Memory",
            level=4,
            num="4.11.3.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.Distributed",
            level=4,
            num="4.11.3.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.Dictionary",
            level=4,
            num="4.11.3.3",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.File",
            level=4,
            num="4.11.3.4",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.URL",
            level=4,
            num="4.11.3.5",
        ),
        Heading(name="Metadata", level=2, num="4.12"),
        Heading(name="ParquetFormat", level=3, num="4.12.1"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadataFormat",
            level=4,
            num="4.12.1.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadataFormat.Output",
            level=4,
            num="4.12.1.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadata.Content",
            level=4,
            num="4.12.1.3",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadata.MinMax",
            level=4,
            num="4.12.1.4",
        ),
        Heading(name="Metadata Types", level=3, num="4.12.2"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Metadata.File", level=4, num="4.12.2.1"
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Metadata.Column",
            level=4,
            num="4.12.2.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Metadata.Header",
            level=4,
            num="4.12.2.3",
        ),
        Heading(name="Error Recovery", level=2, num="4.13"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.MissingMagicNumber",
            level=3,
            num="4.13.1",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.CorruptFile",
            level=3,
            num="4.13.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.CorruptColumn",
            level=3,
            num="4.13.3",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.CorruptPageHeader",
            level=3,
            num="4.13.4",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.CorruptPageData",
            level=3,
            num="4.13.5",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.CorruptColumnValues",
            level=3,
            num="4.13.6",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.CorruptChecksum",
            level=3,
            num="4.13.7",
        ),
        Heading(name="Encoding", level=2, num="4.14"),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Encoding.Plain", level=4, num="4.14.7.1"
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Encoding.RunLength",
            level=4,
            num="4.14.7.2",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Encoding.Delta", level=4, num="4.14.7.3"
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Encoding.DeltaLengthByteArray",
            level=4,
            num="4.14.7.4",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Encoding.DeltaStrings",
            level=4,
            num="4.14.7.5",
        ),
        Heading(
            name="RQ.SRS-032.ClickHouse.Parquet.Encoding.ByteStreamSplit",
            level=4,
            num="4.14.7.6",
        ),
    ),
    requirements=(
        RQ_SRS_032_ClickHouse_SupportedDatatypes,
        RQ_SRS_032_ClickHouse_Parquet,
        RQ_SRS_032_ClickHouse_Parquet_ClickHouseLocal,
        RQ_SRS_032_ClickHouse_Parquet_Encryption,
        RQ_SRS_032_ClickHouse_Parquet_Chunks,
        RQ_SRS_032_ClickHouse_Parquet_Structure,
        RQ_SRS_032_ClickHouse_Parquet_ReadChunkedColumns,
        RQ_SRS_032_ClickHouse_Parquet_WriteChunkedColumns,
        RQ_SRS_032_ClickHouse_Parquet_SupportedVersions,
        RQ_SRS_032_ClickHouse_Parquet_Compression_None,
        RQ_SRS_032_ClickHouse_Parquet_Compression_Gzip,
        RQ_SRS_032_ClickHouse_Parquet_Compression_Brotli,
        RQ_SRS_032_ClickHouse_Parquet_Compression_Lz4,
        RQ_SRS_032_ClickHouse_Parquet_Compression_Lz4Raw,
        RQ_SRS_032_ClickHouse_Parquet_UnsupportedCompression_Snappy,
        RQ_SRS_032_ClickHouse_Parquet_UnsupportedCompression_Lzo,
        RQ_SRS_032_ClickHouse_Parquet_UnsupportedCompression_Zstd,
        RQ_SRS_032_ClickHouse_Parquet_DataTypes_Read,
        RQ_SRS_032_ClickHouse_Parquet_DataTypes_DateUTCAdjusted,
        RQ_SRS_032_ClickHouse_Parquet_DataTypes_TimestampUTCAdjusted,
        RQ_SRS_032_ClickHouse_Parquet_DataTypes_TimeUTCAdjusted,
        RQ_SRS_032_ClickHouse_Parquet_DataTypes_ReadNested,
        RQ_SRS_032_ClickHouse_Parquet_DataTypes_NullValues,
        RQ_SRS_032_ClickHouse_Parquet_DataTypes_ReadInto_Nullable,
        RQ_SRS_032_ClickHouse_Parquet_DataTypes_ReadInto_LowCardinality,
        RQ_SRS_032_ClickHouse_Parquet_DataTypes_ReadInto_Nested,
        RQ_SRS_032_ClickHouse_Parquet_DataTypes_ReadInto_Unknown,
        RQ_SRS_032_ClickHouse_Parquet_DataTypes_Write,
        RQ_SRS_032_ClickHouse_Parquet_DataTypes_WriteNested,
        RQ_SRS_032_ClickHouse_Parquet_DataTypes_WriteNullable,
        RQ_SRS_032_ClickHouse_Parquet_DataTypes_TypeConversionFunction,
        RQ_SRS_032_ClickHouse_Parquet_UnsupportedParquetTypes,
        RQ_SRS_032_ClickHouse_Parquet_UnsupportedParquetTypes_ChunkedArray,
        RQ_SRS_032_ClickHouse_Parquet_Insert,
        RQ_SRS_032_ClickHouse_Parquet_Insert_AutoDetectParquetFileFormat,
        RQ_SRS_032_ClickHouse_Parquet_Insert_Projections,
        RQ_SRS_032_ClickHouse_Parquet_Insert_SkipColumns,
        RQ_SRS_032_ClickHouse_Parquet_Insert_SkipValues,
        RQ_SRS_032_ClickHouse_Parquet_Insert_AutoTypecast,
        RQ_SRS_032_ClickHouse_Parquet_Insert_RowGroupSize,
        RQ_SRS_032_ClickHouse_Parquet_Insert_DataPageSize,
        RQ_SRS_032_ClickHouse_Parquet_Insert_Settings_ImportNested,
        RQ_SRS_032_ClickHouse_Parquet_Insert_Settings_CaseInsensitiveColumnMatching,
        RQ_SRS_032_ClickHouse_Parquet_Insert_Settings_AllowMissingColumns,
        RQ_SRS_032_ClickHouse_Parquet_Insert_Settings_SkipColumnsWithUnsupportedTypesInSchemaInference,
        RQ_SRS_032_ClickHouse_Parquet_Nested_ArrayIntoNested_ReadNested,
        RQ_SRS_032_ClickHouse_Parquet_Nested_ArrayIntoNested_ImportNested,
        RQ_SRS_032_ClickHouse_Parquet_Nested_ArrayIntoNested_NotImportNested,
        RQ_SRS_032_ClickHouse_Parquet_Nested_ArrayIntoNotNested,
        RQ_SRS_032_ClickHouse_Parquet_Nested_NonArrayIntoNested,
        RQ_SRS_032_ClickHouse_Parquet_Nested_ArrayIntoNested_WriteNested,
        RQ_SRS_032_ClickHouse_Parquet_Select,
        RQ_SRS_032_ClickHouse_Parquet_Select_Outfile_AutoDetectParquetFileFormat,
        RQ_SRS_032_ClickHouse_Parquet_Select_Join,
        RQ_SRS_032_ClickHouse_Parquet_Select_Union,
        RQ_SRS_032_ClickHouse_Parquet_Select_View,
        RQ_SRS_032_ClickHouse_Parquet_Select_MaterializedView,
        RQ_SRS_032_ClickHouse_Parquet_Select_Settings_RowGroupSize,
        RQ_SRS_032_ClickHouse_Parquet_Select_Settings_StringAsString,
        RQ_SRS_032_ClickHouse_Parquet_Select_Settings_StringAsFixedByteArray,
        RQ_SRS_032_ClickHouse_Parquet_Select_Settings_ParquetVersion,
        RQ_SRS_032_ClickHouse_Parquet_Select_Settings_CompressionMethod,
        RQ_SRS_032_ClickHouse_Parquet_Create_NewTable,
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
        RQ_SRS_032_ClickHouse_Parquet_Metadata_ParquetMetadataFormat,
        RQ_SRS_032_ClickHouse_Parquet_Metadata_ParquetMetadataFormat_Output,
        RQ_SRS_032_ClickHouse_Parquet_Metadata_ParquetMetadata_Content,
        RQ_SRS_032_ClickHouse_Parquet_Metadata_ParquetMetadata_MinMax,
        RQ_SRS_032_ClickHouse_Parquet_Metadata_File,
        RQ_SRS_032_ClickHouse_Parquet_Metadata_Column,
        RQ_SRS_032_ClickHouse_Parquet_Metadata_Header,
        RQ_SRS_032_ClickHouse_Parquet_Metadata_ErrorRecovery_MissingMagicNumber,
        RQ_SRS_032_ClickHouse_Parquet_Metadata_ErrorRecovery_CorruptFile,
        RQ_SRS_032_ClickHouse_Parquet_Metadata_ErrorRecovery_CorruptColumn,
        RQ_SRS_032_ClickHouse_Parquet_Metadata_ErrorRecovery_CorruptPageHeader,
        RQ_SRS_032_ClickHouse_Parquet_Metadata_ErrorRecovery_CorruptPageData,
        RQ_SRS_032_ClickHouse_Parquet_Metadata_ErrorRecovery_CorruptColumnValues,
        RQ_SRS_032_ClickHouse_Parquet_Metadata_ErrorRecovery_CorruptChecksum,
        RQ_SRS_032_ClickHouse_Parquet_Encoding_Plain,
        RQ_SRS_032_ClickHouse_Parquet_Encoding_RunLength,
        RQ_SRS_032_ClickHouse_Parquet_Encoding_Delta,
        RQ_SRS_032_ClickHouse_Parquet_Encoding_DeltaLengthByteArray,
        RQ_SRS_032_ClickHouse_Parquet_Encoding_DeltaStrings,
        RQ_SRS_032_ClickHouse_Parquet_Encoding_ByteStreamSplit,
    ),
    content="""
# SRS032 ClickHouse Parquet Data Format
# Software Requirements Specification

## Table of Contents

* 1 [Revision History](#revision-history)
* 2 [Introduction](#introduction)
* 3 [Feature Diagram](#feature-diagram)
* 4 [Requirements](#requirements)
  * 4.1 [General](#general)
    * 4.1.1 [RQ.SRS-032.ClickHouse.SupportedDatatypes](#rqsrs-032clickhousesupporteddatatypes)
    * 4.1.2 [RQ.SRS-032.ClickHouse.Parquet](#rqsrs-032clickhouseparquet)
    * 4.1.3 [RQ.SRS-032.ClickHouse.Parquet.ClickHouseLocal](#rqsrs-032clickhouseparquetclickhouselocal)
    * 4.1.4 [RQ.SRS-032.ClickHouse.Parquet.Encryption](#rqsrs-032clickhouseparquetencryption)
    * 4.1.5 [RQ.SRS-032.ClickHouse.Parquet.Chunks](#rqsrs-032clickhouseparquetchunks)
    * 4.1.6 [RQ.SRS-032.ClickHouse.Parquet.Structure](#rqsrs-032clickhouseparquetstructure)
    * 4.1.7 [RQ.SRS-032.ClickHouse.Parquet.ReadChunkedColumns](#rqsrs-032clickhouseparquetreadchunkedcolumns)
    * 4.1.8 [RQ.SRS-032.ClickHouse.Parquet.WriteChunkedColumns](#rqsrs-032clickhouseparquetwritechunkedcolumns)
    * 4.1.9 [RQ.SRS-032.ClickHouse.Parquet.SupportedVersions](#rqsrs-032clickhouseparquetsupportedversions)
  * 4.2 [Compression](#compression)
    * 4.2.1 [RQ.SRS-032.ClickHouse.Parquet.Compression.None](#rqsrs-032clickhouseparquetcompressionnone)
    * 4.2.2 [RQ.SRS-032.ClickHouse.Parquet.Compression.Gzip](#rqsrs-032clickhouseparquetcompressiongzip)
    * 4.2.3 [RQ.SRS-032.ClickHouse.Parquet.Compression.Brotli](#rqsrs-032clickhouseparquetcompressionbrotli)
    * 4.2.4 [RQ.SRS-032.ClickHouse.Parquet.Compression.Lz4](#rqsrs-032clickhouseparquetcompressionlz4)
    * 4.2.5 [RQ.SRS-032.ClickHouse.Parquet.Compression.Lz4Raw](#rqsrs-032clickhouseparquetcompressionlz4raw)
  * 4.3 [Unsupported Compression](#unsupported-compression)
    * 4.3.1 [RQ.SRS-032.ClickHouse.Parquet.UnsupportedCompression.Snappy](#rqsrs-032clickhouseparquetunsupportedcompressionsnappy)
    * 4.3.2 [RQ.SRS-032.ClickHouse.Parquet.UnsupportedCompression.Lzo](#rqsrs-032clickhouseparquetunsupportedcompressionlzo)
    * 4.3.3 [RQ.SRS-032.ClickHouse.Parquet.UnsupportedCompression.Zstd](#rqsrs-032clickhouseparquetunsupportedcompressionzstd)
  * 4.4 [Data Types](#data-types)
    * 4.4.1 [RQ.SRS-032.ClickHouse.Parquet.DataTypes.Read](#rqsrs-032clickhouseparquetdatatypesread)
    * 4.4.2 [RQ.SRS-032.ClickHouse.Parquet.DataTypes.DateUTCAdjusted](#rqsrs-032clickhouseparquetdatatypesdateutcadjusted)
    * 4.4.3 [RQ.SRS-032.ClickHouse.Parquet.DataTypes.TimestampUTCAdjusted](#rqsrs-032clickhouseparquetdatatypestimestamputcadjusted)
    * 4.4.4 [RQ.SRS-032.ClickHouse.Parquet.DataTypes.TimeUTCAdjusted](#rqsrs-032clickhouseparquetdatatypestimeutcadjusted)
    * 4.4.5 [RQ.SRS-032.ClickHouse.Parquet.DataTypes.ReadNested](#rqsrs-032clickhouseparquetdatatypesreadnested)
    * 4.4.6 [RQ.SRS-032.ClickHouse.Parquet.DataTypes.NullValues](#rqsrs-032clickhouseparquetdatatypesnullvalues)
    * 4.4.7 [RQ.SRS-032.ClickHouse.Parquet.DataTypes.ReadInto.Nullable](#rqsrs-032clickhouseparquetdatatypesreadintonullable)
    * 4.4.8 [RQ.SRS-032.ClickHouse.Parquet.DataTypes.ReadInto.LowCardinality](#rqsrs-032clickhouseparquetdatatypesreadintolowcardinality)
    * 4.4.9 [RQ.SRS-032.ClickHouse.Parquet.DataTypes.ReadInto.Nested](#rqsrs-032clickhouseparquetdatatypesreadintonested)
    * 4.4.10 [RQ.SRS-032.ClickHouse.Parquet.DataTypes.ReadInto.Unknown](#rqsrs-032clickhouseparquetdatatypesreadintounknown)
    * 4.4.11 [RQ.SRS-032.ClickHouse.Parquet.DataTypes.Write](#rqsrs-032clickhouseparquetdatatypeswrite)
    * 4.4.12 [RQ.SRS-032.ClickHouse.Parquet.DataTypes.WriteNested](#rqsrs-032clickhouseparquetdatatypeswritenested)
    * 4.4.13 [RQ.SRS-032.ClickHouse.Parquet.DataTypes.WriteNullable](#rqsrs-032clickhouseparquetdatatypeswritenullable)
    * 4.4.14 [RQ.SRS-032.ClickHouse.Parquet.DataTypes.TypeConversionFunction](#rqsrs-032clickhouseparquetdatatypestypeconversionfunction)
  * 4.5 [Unsupported Parquet Types](#unsupported-parquet-types)
    * 4.5.1 [RQ.SRS-032.ClickHouse.Parquet.UnsupportedParquetTypes](#rqsrs-032clickhouseparquetunsupportedparquettypes)
    * 4.5.2 [RQ.SRS-032.ClickHouse.Parquet.UnsupportedParquetTypes.ChunkedArray](#rqsrs-032clickhouseparquetunsupportedparquettypeschunkedarray)
  * 4.6 [INSERT](#insert)
    * 4.6.1 [RQ.SRS-032.ClickHouse.Parquet.Insert](#rqsrs-032clickhouseparquetinsert)
    * 4.6.2 [RQ.SRS-032.ClickHouse.Parquet.Insert.AutoDetectParquetFileFormat](#rqsrs-032clickhouseparquetinsertautodetectparquetfileformat)
    * 4.6.3 [RQ.SRS-032.ClickHouse.Parquet.Insert.Projections](#rqsrs-032clickhouseparquetinsertprojections)
    * 4.6.4 [RQ.SRS-032.ClickHouse.Parquet.Insert.SkipColumns](#rqsrs-032clickhouseparquetinsertskipcolumns)
    * 4.6.5 [RQ.SRS-032.ClickHouse.Parquet.Insert.SkipValues](#rqsrs-032clickhouseparquetinsertskipvalues)
    * 4.6.6 [RQ.SRS-032.ClickHouse.Parquet.Insert.AutoTypecast](#rqsrs-032clickhouseparquetinsertautotypecast)
    * 4.6.7 [RQ.SRS-032.ClickHouse.Parquet.Insert.RowGroupSize](#rqsrs-032clickhouseparquetinsertrowgroupsize)
    * 4.6.8 [RQ.SRS-032.ClickHouse.Parquet.Insert.DataPageSize](#rqsrs-032clickhouseparquetinsertdatapagesize)
    * 4.6.9 [INSERT Settings](#insert-settings)
      * 4.6.9.1 [RQ.SRS-032.ClickHouse.Parquet.Insert.Settings.ImportNested](#rqsrs-032clickhouseparquetinsertsettingsimportnested)
      * 4.6.9.2 [RQ.SRS-032.ClickHouse.Parquet.Insert.Settings.CaseInsensitiveColumnMatching](#rqsrs-032clickhouseparquetinsertsettingscaseinsensitivecolumnmatching)
      * 4.6.9.3 [RQ.SRS-032.ClickHouse.Parquet.Insert.Settings.AllowMissingColumns](#rqsrs-032clickhouseparquetinsertsettingsallowmissingcolumns)
      * 4.6.9.4 [RQ.SRS-032.ClickHouse.Parquet.Insert.Settings.SkipColumnsWithUnsupportedTypesInSchemaInference](#rqsrs-032clickhouseparquetinsertsettingsskipcolumnswithunsupportedtypesinschemainference)
  * 4.7 [Working With Nested Types](#working-with-nested-types)
    * 4.7.1 [RQ.SRS-032.ClickHouse.Parquet.Nested.ArrayIntoNested.ReadNested](#rqsrs-032clickhouseparquetnestedarrayintonestedreadnested)
    * 4.7.2 [RQ.SRS-032.ClickHouse.Parquet.Nested.ArrayIntoNested.ImportNested](#rqsrs-032clickhouseparquetnestedarrayintonestedimportnested)
    * 4.7.3 [RQ.SRS-032.ClickHouse.Parquet.Nested.ArrayIntoNested.NotImportNested](#rqsrs-032clickhouseparquetnestedarrayintonestednotimportnested)
    * 4.7.4 [RQ.SRS-032.ClickHouse.Parquet.Nested.ArrayIntoNotNested](#rqsrs-032clickhouseparquetnestedarrayintonotnested)
    * 4.7.5 [RQ.SRS-032.ClickHouse.Parquet.Nested.NonArrayIntoNested](#rqsrs-032clickhouseparquetnestednonarrayintonested)
    * 4.7.6 [RQ.SRS-032.ClickHouse.Parquet.Nested.ArrayIntoNested.WriteNested](#rqsrs-032clickhouseparquetnestedarrayintonestedwritenested)
  * 4.8 [SELECT](#select)
    * 4.8.1 [RQ.SRS-032.ClickHouse.Parquet.Select](#rqsrs-032clickhouseparquetselect)
    * 4.8.2 [RQ.SRS-032.ClickHouse.Parquet.Select.Outfile.AutoDetectParquetFileFormat](#rqsrs-032clickhouseparquetselectoutfileautodetectparquetfileformat)
    * 4.8.3 [RQ.SRS-032.ClickHouse.Parquet.Select.Join](#rqsrs-032clickhouseparquetselectjoin)
    * 4.8.4 [RQ.SRS-032.ClickHouse.Parquet.Select.Union](#rqsrs-032clickhouseparquetselectunion)
    * 4.8.5 [RQ.SRS-032.ClickHouse.Parquet.Select.View](#rqsrs-032clickhouseparquetselectview)
    * 4.8.6 [RQ.SRS-032.ClickHouse.Parquet.Select.MaterializedView](#rqsrs-032clickhouseparquetselectmaterializedview)
    * 4.8.7 [SELECT Settings](#select-settings)
      * 4.8.7.1 [RQ.SRS-032.ClickHouse.Parquet.Select.Settings.RowGroupSize](#rqsrs-032clickhouseparquetselectsettingsrowgroupsize)
      * 4.8.7.2 [RQ.SRS-032.ClickHouse.Parquet.Select.Settings.StringAsString](#rqsrs-032clickhouseparquetselectsettingsstringasstring)
      * 4.8.7.3 [RQ.SRS-032.ClickHouse.Parquet.Select.Settings.StringAsFixedByteArray](#rqsrs-032clickhouseparquetselectsettingsstringasfixedbytearray)
      * 4.8.7.4 [RQ.SRS-032.ClickHouse.Parquet.Select.Settings.ParquetVersion](#rqsrs-032clickhouseparquetselectsettingsparquetversion)
      * 4.8.7.5 [RQ.SRS-032.ClickHouse.Parquet.Select.Settings.CompressionMethod](#rqsrs-032clickhouseparquetselectsettingscompressionmethod)
  * 4.9 [CREATE](#create)
      * 4.9.7.1 [RQ.SRS-032.ClickHouse.Parquet.Create.NewTable](#rqsrs-032clickhouseparquetcreatenewtable)
  * 4.10 [Table Functions](#table-functions)
    * 4.10.1 [RQ.SRS-032.ClickHouse.Parquet.TableFunctions.URL](#rqsrs-032clickhouseparquettablefunctionsurl)
    * 4.10.2 [RQ.SRS-032.ClickHouse.Parquet.TableFunctions.File](#rqsrs-032clickhouseparquettablefunctionsfile)
      * 4.10.2.1 [RQ.SRS-032.ClickHouse.Parquet.TableFunctions.File.AutoDetectParquetFileFormat](#rqsrs-032clickhouseparquettablefunctionsfileautodetectparquetfileformat)
    * 4.10.3 [RQ.SRS-032.ClickHouse.Parquet.TableFunctions.S3](#rqsrs-032clickhouseparquettablefunctionss3)
    * 4.10.4 [RQ.SRS-032.ClickHouse.Parquet.TableFunctions.JDBC](#rqsrs-032clickhouseparquettablefunctionsjdbc)
    * 4.10.5 [RQ.SRS-032.ClickHouse.Parquet.TableFunctions.ODBC](#rqsrs-032clickhouseparquettablefunctionsodbc)
    * 4.10.6 [RQ.SRS-032.ClickHouse.Parquet.TableFunctions.HDFS](#rqsrs-032clickhouseparquettablefunctionshdfs)
    * 4.10.7 [RQ.SRS-032.ClickHouse.Parquet.TableFunctions.Remote](#rqsrs-032clickhouseparquettablefunctionsremote)
    * 4.10.8 [RQ.SRS-032.ClickHouse.Parquet.TableFunctions.MySQL](#rqsrs-032clickhouseparquettablefunctionsmysql)
    * 4.10.9 [RQ.SRS-032.ClickHouse.Parquet.TableFunctions.PostgreSQL](#rqsrs-032clickhouseparquettablefunctionspostgresql)
  * 4.11 [Table Engines](#table-engines)
    * 4.11.1 [MergeTree](#mergetree)
      * 4.11.1.1 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.MergeTree](#rqsrs-032clickhouseparquettableenginesmergetreemergetree)
      * 4.11.1.2 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.ReplicatedMergeTree](#rqsrs-032clickhouseparquettableenginesmergetreereplicatedmergetree)
      * 4.11.1.3 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.ReplacingMergeTree](#rqsrs-032clickhouseparquettableenginesmergetreereplacingmergetree)
      * 4.11.1.4 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.SummingMergeTree](#rqsrs-032clickhouseparquettableenginesmergetreesummingmergetree)
      * 4.11.1.5 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.AggregatingMergeTree](#rqsrs-032clickhouseparquettableenginesmergetreeaggregatingmergetree)
      * 4.11.1.6 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.CollapsingMergeTree](#rqsrs-032clickhouseparquettableenginesmergetreecollapsingmergetree)
      * 4.11.1.7 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.VersionedCollapsingMergeTree](#rqsrs-032clickhouseparquettableenginesmergetreeversionedcollapsingmergetree)
      * 4.11.1.8 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.GraphiteMergeTree](#rqsrs-032clickhouseparquettableenginesmergetreegraphitemergetree)
    * 4.11.2 [Integration Engines](#integration-engines)
      * 4.11.2.1 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.ODBC](#rqsrs-032clickhouseparquettableenginesintegrationodbc)
      * 4.11.2.2 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.JDBC](#rqsrs-032clickhouseparquettableenginesintegrationjdbc)
      * 4.11.2.3 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.MySQL](#rqsrs-032clickhouseparquettableenginesintegrationmysql)
      * 4.11.2.4 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.MongoDB](#rqsrs-032clickhouseparquettableenginesintegrationmongodb)
      * 4.11.2.5 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.HDFS](#rqsrs-032clickhouseparquettableenginesintegrationhdfs)
      * 4.11.2.6 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.S3](#rqsrs-032clickhouseparquettableenginesintegrations3)
      * 4.11.2.7 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.Kafka](#rqsrs-032clickhouseparquettableenginesintegrationkafka)
      * 4.11.2.8 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.EmbeddedRocksDB](#rqsrs-032clickhouseparquettableenginesintegrationembeddedrocksdb)
      * 4.11.2.9 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.PostgreSQL](#rqsrs-032clickhouseparquettableenginesintegrationpostgresql)
    * 4.11.3 [Special Engines](#special-engines)
      * 4.11.3.1 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.Memory](#rqsrs-032clickhouseparquettableenginesspecialmemory)
      * 4.11.3.2 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.Distributed](#rqsrs-032clickhouseparquettableenginesspecialdistributed)
      * 4.11.3.3 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.Dictionary](#rqsrs-032clickhouseparquettableenginesspecialdictionary)
      * 4.11.3.4 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.File](#rqsrs-032clickhouseparquettableenginesspecialfile)
      * 4.11.3.5 [RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.URL](#rqsrs-032clickhouseparquettableenginesspecialurl)
  * 4.12 [Metadata](#metadata)
    * 4.12.1 [ParquetFormat](#parquetformat)
      * 4.12.1.1 [RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadataFormat](#rqsrs-032clickhouseparquetmetadataparquetmetadataformat)
      * 4.12.1.2 [RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadataFormat.Output](#rqsrs-032clickhouseparquetmetadataparquetmetadataformatoutput)
      * 4.12.1.3 [RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadata.Content](#rqsrs-032clickhouseparquetmetadataparquetmetadatacontent)
      * 4.12.1.4 [RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadata.MinMax](#rqsrs-032clickhouseparquetmetadataparquetmetadataminmax)
    * 4.12.2 [Metadata Types](#metadata-types)
      * 4.12.2.1 [RQ.SRS-032.ClickHouse.Parquet.Metadata.File](#rqsrs-032clickhouseparquetmetadatafile)
      * 4.12.2.2 [RQ.SRS-032.ClickHouse.Parquet.Metadata.Column](#rqsrs-032clickhouseparquetmetadatacolumn)
      * 4.12.2.3 [RQ.SRS-032.ClickHouse.Parquet.Metadata.Header](#rqsrs-032clickhouseparquetmetadataheader)
  * 4.13 [Error Recovery](#error-recovery)
    * 4.13.1 [RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.MissingMagicNumber](#rqsrs-032clickhouseparquetmetadataerrorrecoverymissingmagicnumber)
    * 4.13.2 [RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.CorruptFile](#rqsrs-032clickhouseparquetmetadataerrorrecoverycorruptfile)
    * 4.13.3 [RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.CorruptColumn](#rqsrs-032clickhouseparquetmetadataerrorrecoverycorruptcolumn)
    * 4.13.4 [RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.CorruptPageHeader](#rqsrs-032clickhouseparquetmetadataerrorrecoverycorruptpageheader)
    * 4.13.5 [RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.CorruptPageData](#rqsrs-032clickhouseparquetmetadataerrorrecoverycorruptpagedata)
    * 4.13.6 [RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.CorruptColumnValues](#rqsrs-032clickhouseparquetmetadataerrorrecoverycorruptcolumnvalues)
    * 4.13.7 [RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.CorruptChecksum](#rqsrs-032clickhouseparquetmetadataerrorrecoverycorruptchecksum)
  * 4.14 [Encoding](#encoding)
      * 4.14.7.1 [RQ.SRS-032.ClickHouse.Parquet.Encoding.Plain](#rqsrs-032clickhouseparquetencodingplain)
      * 4.14.7.2 [RQ.SRS-032.ClickHouse.Parquet.Encoding.RunLength](#rqsrs-032clickhouseparquetencodingrunlength)
      * 4.14.7.3 [RQ.SRS-032.ClickHouse.Parquet.Encoding.Delta](#rqsrs-032clickhouseparquetencodingdelta)
      * 4.14.7.4 [RQ.SRS-032.ClickHouse.Parquet.Encoding.DeltaLengthByteArray](#rqsrs-032clickhouseparquetencodingdeltalengthbytearray)
      * 4.14.7.5 [RQ.SRS-032.ClickHouse.Parquet.Encoding.DeltaStrings](#rqsrs-032clickhouseparquetencodingdeltastrings)
      * 4.14.7.6 [RQ.SRS-032.ClickHouse.Parquet.Encoding.ByteStreamSplit](#rqsrs-032clickhouseparquetencodingbytestreamsplit)


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

Sources --> Compression --> Encryption --> Parquet_File_in --Insert into ClickHouse--> Input_settings --> ClickHouse -- Read From ClickHouse --> Output_settings --> Parquet_File_out

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

## Requirements

### General

#### RQ.SRS-032.ClickHouse.SupportedDatatypes
version: 1.0

[ClickHouse] SHALL support all the following datatypes:

| name                              | case_insensitive | alias_to data type |
|-----------------------------------|------------------|--------------------|
| `JSON`                            | 1                |                    |
| `Polygon`                         | 0                |                    |
| `Ring`                            | 0                |                    |
| `Point`                           | 0                |                    |
| `SimpleAggregateFunction`         | 0                |                    |
| `IntervalQuarter`                 | 0                |                    |
| `IntervalMonth`                   | 0                |                    |
| `Int64`                           | 0                |                    |
| `IntervalDay`                     | 0                |                    |
| `IntervalHour`                    | 0                |                    |
| `IPv4`                            | 0                |                    |
| `IntervalSecond`                  | 0                |                    |
| `LowCardinality`                  | 0                |                    |
| `Int16`                           | 0                |                    |
| `UInt256`                         | 0                |                    |
| `AggregateFunction`               | 0                |                    |
| `MultiPolygon`                    | 0                |                    |
| `IPv6`                            | 0                |                    |
| `Nothing`                         | 0                |                    |
| `Decimal256`                      | 1                |                    |
| `Tuple`                           | 0                |                    |
| `Array`                           | 0                |                    |
| `IntervalMicrosecond`             | 0                |                    |
| `Bool`                            | 1                |                    |
| `Enum16`                          | 0                |                    |
| `IntervalMinute`                  | 0                |                    |
| `FixedString`                     | 0                |                    |
| `String`                          | 0                |                    |
| `DateTime`                        | 1                |                    |
| `Object`                          | 0                |                    |
| `Map`                             | 0                |                    |
| `UUID`                            | 0                |                    |
| `Decimal64`                       | 1                |                    |
| `Nullable`                        | 0                |                    |
| `Enum`                            | 1                |                    |
| `Int32`                           | 0                |                    |
| `UInt8`                           | 0                |                    |
| `Date`                            | 1                |                    |
| `Decimal32`                       | 1                |                    |
| `UInt128`                         | 0                |                    |
| `Float64`                         | 0                |                    |
| `Nested`                          | 0                |                    |
| `UInt16`                          | 0                |                    |
| `IntervalMillisecond`             | 0                |                    |
| `Int128`                          | 0                |                    |
| `Decimal128`                      | 1                |                    |
| `Int8`                            | 0                |                    |
| `Decimal`                         | 1                |                    |
| `Int256`                          | 0                |                    |
| `DateTime64`                      | 1                |                    |
| `Enum8`                           | 0                |                    |
| `DateTime32`                      | 1                |                    |
| `Date32`                          | 1                |                    |
| `IntervalWeek`                    | 0                |                    |
| `UInt64`                          | 0                |                    |
| `IntervalNanosecond`              | 0                |                    |
| `IntervalYear`                    | 0                |                    |
| `UInt32`                          | 0                |                    |
| `Float32`                         | 0                |                    |
| `bool`                            | 1                | `Bool`             |
| `INET6`                           | 1                | `IPv6`             |
| `INET4`                           | 1                | `IPv4`             |
| `ENUM`                            | 1                | `Enum`             |
| `BINARY`                          | 1                | `FixedString`      |
| `GEOMETRY`                        | 1                | `String`           |
| `NATIONAL CHAR VARYING`           | 1                | `String`           |
| `BINARY VARYING`                  | 1                | `String`           |
| `NCHAR LARGE OBJECT`              | 1                | `String`           |
| `NATIONAL CHARACTER VARYING`      | 1                | `String`           |
| `boolean`                         | 1                | `Bool`             |
| `NATIONAL CHARACTER LARGE OBJECT` | 1                | `String`           |
| `NATIONAL CHARACTER`              | 1                | `String`           |
| `NATIONAL CHAR`                   | 1                | `String`           |
| `CHARACTER VARYING`               | 1                | `String`           |
| `LONGBLOB`                        | 1                | `String`           |
| `TINYBLOB`                        | 1                | `String`           |
| `MEDIUMTEXT`                      | 1                | `String`           |
| `TEXT`                            | 1                | `String`           |
| `VARCHAR2`                        | 1                | `String`           |
| `CHARACTER LARGE OBJECT`          | 1                | `String`           |
| `DOUBLE PRECISION`                | 1                | `Float64`          |
| `LONGTEXT`                        | 1                | `String`           |
| `NVARCHAR`                        | 1                | `String`           |
| `INT1 UNSIGNED`                   | 1                | `UInt8`            |
| `VARCHAR`                         | 1                | `String`           |
| `CHAR VARYING`                    | 1                | `String`           |
| `MEDIUMBLOB`                      | 1                | `String`           |
| `NCHAR`                           | 1                | `String`           |
| `VARBINARY`                       | 1                | `String`           |
| `CHAR`                            | 1                | `String`           |
| `SMALLINT UNSIGNED`               | 1                | `UInt16`           |
| `TIMESTAMP`                       | 1                | `DateTime`         |
| `FIXED`                           | 1                | `Decimal`          |
| `TINYTEXT`                        | 1                | `String`           |
| `NUMERIC`                         | 1                | `Decimal`          |
| `DEC`                             | 1                | `Decimal`          |
| `TIME`                            | 1                | `Int64`            |
| `FLOAT`                           | 1                | `Float32`          |
| `SET`                             | 1                | `UInt64`           |
| `TINYINT UNSIGNED`                | 1                | `UInt8`            |
| `INTEGER UNSIGNED`                | 1                | `UInt32`           |
| `INT UNSIGNED`                    | 1                | `UInt32`           |
| `CLOB`                            | 1                | `String`           |
| `MEDIUMINT UNSIGNED`              | 1                | `UInt32`           |
| `BLOB`                            | 1                | `String`           |
| `REAL`                            | 1                | `Float32`          |
| `SMALLINT`                        | 1                | `Int16`            |
| `INTEGER SIGNED`                  | 1                | `Int32`            |
| `NCHAR VARYING`                   | 1                | `String`           |
| `INT SIGNED`                      | 1                | `Int32`            |
| `TINYINT SIGNED`                  | 1                | `Int8`             |
| `BIGINT SIGNED`                   | 1                | `Int64`            |
| `BINARY LARGE OBJECT`             | 1                | `String`           |
| `SMALLINT SIGNED`                 | 1                | `Int16`            |
| `YEAR`                            | 1                | `UInt16`           |
| `MEDIUMINT`                       | 1                | `Int32`            |
| `INTEGER`                         | 1                | `Int32`            |
| `INT1 SIGNED`                     | 1                | `Int8`             |
| `BIT`                             | 1                | `UInt64`           |
| `BIGINT UNSIGNED`                 | 1                | `UInt64`           |
| `BYTEA`                           | 1                | `String`           |
| `INT`                             | 1                | `Int32`            |
| `SINGLE`                          | 1                | `Float32`          |
| `MEDIUMINT SIGNED`                | 1                | `Int32`            |
| `DOUBLE`                          | 1                | `Float64`          |
| `INT1`                            | 1                | `Int8`             |
| `CHAR LARGE OBJECT`               | 1                | `String`           |
| `TINYINT`                         | 1                | `Int8`             |
| `BIGINT`                          | 1                | `Int64`            |
| `CHARACTER`                       | 1                | `String`           |
| `BYTE`                            | 1                | `Int8`             |

#### RQ.SRS-032.ClickHouse.Parquet
version: 1.0

[ClickHouse] SHALL support `Parquet` data format.

#### RQ.SRS-032.ClickHouse.Parquet.ClickHouseLocal
version: 1.0

[ClickHouse] SHALL support the usage of `clickhouse-local` with `Parquet` data format.

#### RQ.SRS-032.ClickHouse.Parquet.Encryption
version: 1.0

[ClickHouse] MAY not support reading or writing encrypted Parquet files.

#### RQ.SRS-032.ClickHouse.Parquet.Chunks
version: 1.0

[ClickHouse] SHALL support chunked `Parquet` files.

#### RQ.SRS-032.ClickHouse.Parquet.Structure
version: 1.0

[ClickHouse] SHALL support using `DESCRIBE TABLE` statement on the Parquet to read the file structure.

For example,

```sql
DESCRIBE TABLE file('data.parquet', Parquet)
```

#### RQ.SRS-032.ClickHouse.Parquet.ReadChunkedColumns
version: 1.0

[ClickHouse] SHALL support reading chunked columns from the Parquet files.

#### RQ.SRS-032.ClickHouse.Parquet.WriteChunkedColumns
version: 1.0

[ClickHouse] SHALL support writing chunked columns into the Parquet files.

#### RQ.SRS-032.ClickHouse.Parquet.SupportedVersions
version: 1.0

[ClickHouse] SHALL support reading the following Parquet file versions: `1.0.0`, `2.0.0`, `2.1.0`, `2.2.0`, `2.4.0`, `2.6.0`, `2.7.0`, `2.8.0`, `2.9.0`.

### Compression

#### RQ.SRS-032.ClickHouse.Parquet.Compression.None
version: 1.0

[ClickHouse] SHALL support reading or writing uncompressed Parquet files.

#### RQ.SRS-032.ClickHouse.Parquet.Compression.Gzip
version: 1.0

[ClickHouse] SHALL support reading or writing Parquet files compressed using gzip.

#### RQ.SRS-032.ClickHouse.Parquet.Compression.Brotli
version: 1.0

[ClickHouse] SHALL support reading or writing Parquet files compressed using brotli.

#### RQ.SRS-032.ClickHouse.Parquet.Compression.Lz4
version: 1.0

[ClickHouse] SHALL support reading or writing Parquet files compressed using lz4.

#### RQ.SRS-032.ClickHouse.Parquet.Compression.Lz4Raw
version: 1.0

[ClickHouse] SHALL support reading or writing Parquet files compressed using lz4_raw.

### Unsupported Compression

#### RQ.SRS-032.ClickHouse.Parquet.UnsupportedCompression.Snappy
version: 1.0

[ClickHouse] MAY not support reading or writing Parquet files compressed using snapy.

#### RQ.SRS-032.ClickHouse.Parquet.UnsupportedCompression.Lzo
version: 1.0

[ClickHouse] MAY not support reading or writing Parquet files compressed using lzo.

#### RQ.SRS-032.ClickHouse.Parquet.UnsupportedCompression.Zstd
version: 1.0

[ClickHouse] MAY not support reading or writing Parquet files compressed using zstd.

### Data Types

#### RQ.SRS-032.ClickHouse.Parquet.DataTypes.Read
version:1.0

[ClickHouse] SHALL support reading the following Parquet data types:
Parquet Decimal is currently not tested.

| Parquet data type (INSERT)                    | ClickHouse data type                  |
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


#### RQ.SRS-032.ClickHouse.Parquet.DataTypes.DateUTCAdjusted
version:1.0

[ClickHouse] SHALL support reading `DATE` Parquet datatype with `isAdjustedToUTC = true`.

#### RQ.SRS-032.ClickHouse.Parquet.DataTypes.TimestampUTCAdjusted
version:1.0

[ClickHouse] SHALL support reading `TIMESTAMP` Parquet datatype with `isAdjustedToUTC = true`.

#### RQ.SRS-032.ClickHouse.Parquet.DataTypes.TimeUTCAdjusted
version:1.0

[ClickHouse] SHALL support reading `TIME` Parquet datatype with `isAdjustedToUTC = true`.

#### RQ.SRS-032.ClickHouse.Parquet.DataTypes.ReadNested
version:1.0

[ClickHouse] SHALL support reading nested: `Array`, `Tuple` and `Map` datatypes in Parquet files.

#### RQ.SRS-032.ClickHouse.Parquet.DataTypes.NullValues
version:1.0

[ClickHouse] SHALL support reading columns that have `Null` values in Parquet files. If the target [ClickHouse] column is not `Nullable` then the `Null` value should be converted to the default values for the target column datatype.

For example, if the target column has `Int32`, then the `Null` value will be replaced with `0`.

#### RQ.SRS-032.ClickHouse.Parquet.DataTypes.ReadInto.Nullable
version:1.0

[ClickHouse] SHALL support reading Parquet files into target table's `Nullable` datatype columns.


#### RQ.SRS-032.ClickHouse.Parquet.DataTypes.ReadInto.LowCardinality
version:1.0

[ClickHouse] SHALL support reading Parquet files into target table's `LowCardinality` datatype columns.


#### RQ.SRS-032.ClickHouse.Parquet.DataTypes.ReadInto.Nested
version:1.0

[ClickHouse] SHALL support reading Parquet files into target table's `Nested` datatype columns.

#### RQ.SRS-032.ClickHouse.Parquet.DataTypes.ReadInto.Unknown
version:1.0

[ClickHouse] SHALL support reading Parquet files with `UNKNOWN` logical type.

The example as to why the Parquet might have an `UNKNOWN` types is as follows,

> Sometimes, when discovering the schema of existing data, values are always null and there's no type information. 
> The UNKNOWN type can be used to annotate a column that is always null. (Similar to Null type in Avro and Arrow)


#### RQ.SRS-032.ClickHouse.Parquet.DataTypes.Write
version:1.0

[ClickHouse] SHALL support writing the following datatypes to Parquet:

| Parquet data type (SELECT) | ClickHouse data type                  |
|----------------------------|---------------------------------------|
| `BOOL`                     | `Bool`                                |
| `UINT8`                    | `UInt8`                               |
| `INT8`                     | `Int8`/`Enum8`                        |
| `UINT16`                   | `UInt16`                              |
| `INT16`                    | `Int16`/`Enum16`                      |
| `UINT32`                   | `UInt32`                              |
| `INT32`                    | `Int32`                               |
| `UINT64`                   | `UInt64`                              |
| `INT64`                    | `Int64`                               |
| `FLOAT`                    | `Float32`                             |
| `DOUBLE`                   | `Float64`                             |
| `DATE`                     | `Date32`                              |
| `UINT32`                   | `DateTime`                            |
| `TIMESTAMP`                | `DateTime64`                          |
| `BINARY`                   | `String`                              |
| `FIXED_LENGTH_BYTE_ARRAY`  | `FixedString`                         |
| `DECIMAL`                  | `Decimal`                             |
| `LIST`                     | `Array`                               |
| `STRUCT`                   | `Tuple`                               |
| `MAP`                      | `Map`                                 |
| `UINT32`                   | `IPv4`                                |
| `FIXED_LENGTH_BYTE_ARRAY`  | `IPv6`                                |
| `FIXED_LENGTH_BYTE_ARRAY`  | `Int128`/`UInt128`/`Int256`/`UInt256` |

#### RQ.SRS-032.ClickHouse.Parquet.DataTypes.WriteNested
version:1.0

[ClickHouse] SHALL support writing nested: `Array`, `Tuple` and `Map` datatypes in Parquet files.

#### RQ.SRS-032.ClickHouse.Parquet.DataTypes.WriteNullable
version:1.0

[ClickHouse] SHALL support writing `Nullable` datatypes in Parquet files and `Nullable` datatypes that consist only of `Null`.


#### RQ.SRS-032.ClickHouse.Parquet.DataTypes.TypeConversionFunction
version:1.0

[ClickHouse] SHALL support using type conversion functions when reading Parquet files.

For example,

```sql
SELECT
    n,
    toDateTime(time)
FROM file('time.parquet', Parquet);
```

The conversion MAY not be possible between some datatypes.

For example,

`Bool` -> `IPv6`

### Unsupported Parquet Types

#### RQ.SRS-032.ClickHouse.Parquet.UnsupportedParquetTypes
version:1.0

[ClickHouse] MAY not support the following Parquet types:

- `Time32`
- `Fixed_Size_Binary`
- `JSON`
- `UUID`
- `ENUM`

#### RQ.SRS-032.ClickHouse.Parquet.UnsupportedParquetTypes.ChunkedArray
version:1.0

[ClickHouse] MAY not support Parquet chunked arrays.

### INSERT

#### RQ.SRS-032.ClickHouse.Parquet.Insert
version: 1.0

[ClickHouse] SHALL support using `INSERT` query with `FROM INFILE {file_name}` and `FORMAT Parquet` clauses to
read data from Parquet files and insert data into tables or table functions.

```sql
INSERT INTO sometable
FROM INFILE 'data.parquet' FORMAT Parquet;
```

#### RQ.SRS-032.ClickHouse.Parquet.Insert.AutoDetectParquetFileFormat
version: 1.0

[ClickHouse] SHALL support automatically detecting Parquet file format based on 
when using INFILE clause without explicitly specifying the format setting.

```sql
INSERT INTO sometable
FROM INFILE 'data.parquet';
```

#### RQ.SRS-032.ClickHouse.Parquet.Insert.Projections
version: 1.0

[ClickHouse] SHALL support inserting parquet data into a table that has a projection on it.

#### RQ.SRS-032.ClickHouse.Parquet.Insert.SkipColumns
version: 1.0

[ClickHouse] SHALL support skipping unexistent columns when reading from Parquet files.

#### RQ.SRS-032.ClickHouse.Parquet.Insert.SkipValues
version: 1.0

[ClickHouse] SHALL support skipping unsupported values when reading from Parquet files. When the values are being skipped, the inserted values SHALL be the default value for the corresponding column's datatype.

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

#### RQ.SRS-032.ClickHouse.Parquet.Insert.AutoTypecast
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

#### RQ.SRS-032.ClickHouse.Parquet.Insert.RowGroupSize
version: 1.0

[ClickHouse] SHALL support reading Parquet files with different Row Group Sizes.

As described in https://parquet.apache.org/docs/file-format/configurations/#row-group-size,

> We recommend large row groups (512MB - 1GB). Since an entire row group might need to be read, 
> we want it to completely fit on one HDFS block.

#### RQ.SRS-032.ClickHouse.Parquet.Insert.DataPageSize
version: 1.0

[ClickHouse] SHALL support reading Parquet files with different Data Page Sizes.

As described in https://parquet.apache.org/docs/file-format/configurations/#data-page--size,

> Note: for sequential scans, it is not expected to read a page at a time; this is not the IO chunk. We recommend 8KB for page sizes.

#### INSERT Settings

##### RQ.SRS-032.ClickHouse.Parquet.Insert.Settings.ImportNested
version: 1.0

[ClickHouse] SHALL support specifying `input_format_parquet_import_nested` to allow inserting arrays of
nested structs into Nested tables. The default value SHALL be `0`.

- `0` — Data can not be inserted into Nested columns as an array of structs.
- `1` — Data can be inserted into Nested columns as an array of structs.

##### RQ.SRS-032.ClickHouse.Parquet.Insert.Settings.CaseInsensitiveColumnMatching
version: 1.0

[ClickHouse] SHALL support specifying `input_format_parquet_case_insensitive_column_matching` to ignore matching
Parquet and ClickHouse columns. The default value SHALL be `0`.

##### RQ.SRS-032.ClickHouse.Parquet.Insert.Settings.AllowMissingColumns
version: 1.0

[ClickHouse] SHALL support specifying `input_format_parquet_allow_missing_columns` to allow missing columns.
The default value SHALL be `0`.

##### RQ.SRS-032.ClickHouse.Parquet.Insert.Settings.SkipColumnsWithUnsupportedTypesInSchemaInference
version: 1.0

[ClickHouse] SHALL support specifying `input_format_parquet_skip_columns_with_unsupported_types_in_schema_inference`
to allow skipping unsupported types. The default value SHALL be `0`.

### Working With Nested Types

#### RQ.SRS-032.ClickHouse.Parquet.Nested.ArrayIntoNested.ReadNested
version: 1.0

[ClickHouse] SHALL support reading nested columns from the Parquet file.

#### RQ.SRS-032.ClickHouse.Parquet.Nested.ArrayIntoNested.ImportNested
version: 1.0

[ClickHouse] SHALL support inserting arrays of nested structs from Parquet files into [ClickHouse] Nested columns when `input_format_parquet_import_nested` setting is set to `1`.

#### RQ.SRS-032.ClickHouse.Parquet.Nested.ArrayIntoNested.NotImportNested
version: 1.0

[ClickHouse] SHALL return an error when trying to insert arrays of nested structs from Parquet files into [ClickHouse] Nested columns when
`input_format_parquet_import_nested` setting is set to `0`.

#### RQ.SRS-032.ClickHouse.Parquet.Nested.ArrayIntoNotNested
version: 1.0

[ClickHouse] SHALL return an error when trying to insert arrays of nested structs from Parquet files into [ClickHouse] not Nested columns.

#### RQ.SRS-032.ClickHouse.Parquet.Nested.NonArrayIntoNested
version: 1.0

[ClickHouse] SHALL return an error when trying to insert datatypes other than arrays of nested structs from Parquet files into [ClickHouse] Nested columns.

#### RQ.SRS-032.ClickHouse.Parquet.Nested.ArrayIntoNested.WriteNested
version: 1.0

[ClickHouse] SHALL support writing nested columns to the Parquet file.

### SELECT

#### RQ.SRS-032.ClickHouse.Parquet.Select
version: 1.0

[ClickHouse] SHALL support using `SELECT` query with either the `INTO OUTFILE {file_name}` or just `FORMAT Parquet` clauses to write Parquet files. 

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

#### RQ.SRS-032.ClickHouse.Parquet.Select.Outfile.AutoDetectParquetFileFormat
version: 1.0


[ClickHouse] SHALL support automatically detecting Parquet file format based on file extension when using OUTFILE clause without explicitly specifying the format setting.

```sql
SELECT *
FROM sometable
INTO OUTFILE 'export.parquet'
```

#### RQ.SRS-032.ClickHouse.Parquet.Select.Join
version: 1.0

[ClickHouse] SHALL support writing output of `SELECT` query with a `JOIN` clause into a Parquet file.

#### RQ.SRS-032.ClickHouse.Parquet.Select.Union
version: 1.0

[ClickHouse] SHALL support writing output of `SELECT` query with a `UNION` clause into a Parquet file.

#### RQ.SRS-032.ClickHouse.Parquet.Select.View
version: 1.0

[ClickHouse] SHALL support writing output of `SELECT * FROM {view_name}` query into a Parquet file.

#### RQ.SRS-032.ClickHouse.Parquet.Select.MaterializedView
version: 1.0

[ClickHouse] SHALL support writing output of `SELECT * FROM {mat_view_name}` query into a Parquet file.

#### SELECT Settings

##### RQ.SRS-032.ClickHouse.Parquet.Select.Settings.RowGroupSize
version: 1.0

[ClickHouse] SHALL support specifying `output_format_parquet_row_group_size` row group size by row count.
The default value SHALL be `1000000`.

##### RQ.SRS-032.ClickHouse.Parquet.Select.Settings.StringAsString
version: 1.0

[ClickHouse] SHALL support specifying `output_format_parquet_string_as_string` to use Parquet String type instead of Binary.
The default value SHALL be `0`.

##### RQ.SRS-032.ClickHouse.Parquet.Select.Settings.StringAsFixedByteArray
version: 1.0

[ClickHouse] SHALL support specifying `output_format_parquet_fixed_string_as_fixed_byte_array` to use Parquet FIXED_LENGTH_BYTE_ARRAY type instead of Binary/String for FixedString columns. The default value SHALL be `1`.

##### RQ.SRS-032.ClickHouse.Parquet.Select.Settings.ParquetVersion
version: 1.0

[ClickHouse] SHALL support specifying `output_format_parquet_version` to set the version of Parquet used in the output file.
The default value SHALL be `2.latest`.

##### RQ.SRS-032.ClickHouse.Parquet.Select.Settings.CompressionMethod
version: 1.0

[ClickHouse] SHALL support specifying `output_format_parquet_compression_method` to set the compression method used in the Parquet file.
The default value SHALL be `lz4`.

### CREATE

##### RQ.SRS-032.ClickHouse.Parquet.Create.NewTable
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

### Table Functions

#### RQ.SRS-032.ClickHouse.Parquet.TableFunctions.URL
version: 1.0

[ClickHouse] SHALL support `url` table function reading and writing Parquet format.

#### RQ.SRS-032.ClickHouse.Parquet.TableFunctions.File
version: 1.0

[ClickHouse] SHALL support `file` table function reading and writing Parquet format.

For example,

```sql
SELECT * FROM file('data.parquet', Parquet)
```

##### RQ.SRS-032.ClickHouse.Parquet.TableFunctions.File.AutoDetectParquetFileFormat
version: 1.0

[ClickHouse] SHALL support automatically detecting Parquet file format based on file extension when using `file()` function without explicitly specifying the format setting.

```sql
SELECT * FROM file('data.parquet')
```

#### RQ.SRS-032.ClickHouse.Parquet.TableFunctions.S3
version: 1.0

[ClickHouse] SHALL support `s3` table function for reading and writing Parquet format.

For example,

```sql
SELECT *
FROM gcs('https://storage.googleapis.com/my-test-bucket-768/data.parquet', Parquet)
```

#### RQ.SRS-032.ClickHouse.Parquet.TableFunctions.JDBC
version: 1.0

[ClickHouse] SHALL support `jdbc` table function for reading and writing Parquet format.

#### RQ.SRS-032.ClickHouse.Parquet.TableFunctions.ODBC
version: 1.0

[ClickHouse] SHALL support `odbc` table function for reading and writing Parquet format.

#### RQ.SRS-032.ClickHouse.Parquet.TableFunctions.HDFS
version: 1.0

[ClickHouse] SHALL support `hdfs` table function for reading and writing Parquet format.

#### RQ.SRS-032.ClickHouse.Parquet.TableFunctions.Remote
version: 1.0

[ClickHouse] SHALL support `remote` table function for reading and writing Parquet format.

#### RQ.SRS-032.ClickHouse.Parquet.TableFunctions.MySQL
version: 1.0

[ClickHouse] SHALL support `mysql` table function for reading and writing Parquet format.

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
> We can write to a Parquet file format with:
> 
> ```sql
> SELECT * FROM mysql_table1 INTO OUTFILE testTable.parquet FORMAT Parquet
> ```

#### RQ.SRS-032.ClickHouse.Parquet.TableFunctions.PostgreSQL
version: 1.0

[ClickHouse] SHALL support `postgresql` table function reading and writing Parquet format.

### Table Engines

#### MergeTree

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.MergeTree
version: 1.0

[ClickHouse] SHALL support Parquet format being writen into and read from a `MergeTree` table engine.

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.ReplicatedMergeTree
version: 1.0

[ClickHouse] SHALL support Parquet format being writen into and read from a `ReplicatedMergeTree` table engine.

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.ReplacingMergeTree
version: 1.0

[ClickHouse] SHALL support Parquet format being writen into and read from a `ReplacingMergeTree` table engine.

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.SummingMergeTree
version: 1.0

[ClickHouse] SHALL support Parquet format being writen into and read from a `SummingMergeTree` table engine.

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.AggregatingMergeTree
version: 1.0

[ClickHouse] SHALL support Parquet format being writen into and read from a `AggregatingMergeTree` table engine.

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.CollapsingMergeTree
version: 1.0

[ClickHouse] SHALL support Parquet format being writen into and read from a `CollapsingMergeTree` table engine.

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.VersionedCollapsingMergeTree
version: 1.0

[ClickHouse] SHALL support Parquet format being writen into and read from a `VersionedCollapsingMergeTree` table engine.

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.MergeTree.GraphiteMergeTree
version: 1.0

[ClickHouse] SHALL support Parquet format being writen into and read from a `GraphiteMergeTree` table engine.

#### Integration Engines

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.ODBC
version: 1.0

[ClickHouse] SHALL support Parquet format being writen into and read from an `ODBC` table engine.

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.JDBC
version: 1.0

[ClickHouse] SHALL support Parquet format being writen into and read from a `JDBC` table engine.

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.MySQL
version: 1.0

[ClickHouse] SHALL support Parquet format being writen into and read from a `MySQL` table engine.

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.MongoDB
version: 1.0

[ClickHouse] SHALL support Parquet format being writen into and read from a `MongoDB` table engine.

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.HDFS
version: 1.0

[ClickHouse] SHALL support Parquet format being writen into and read from a `HDFS` table engine.

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.S3
version: 1.0

[ClickHouse] SHALL support Parquet format being writen into and read from an `S3` table engine.

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.Kafka
version: 1.0

[ClickHouse] SHALL support Parquet format being writen into and read from a `Kafka` table engine.

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.EmbeddedRocksDB
version: 1.0

[ClickHouse] SHALL support Parquet format being writen into and read from an `EmbeddedRocksDB` table engine.

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Integration.PostgreSQL
version: 1.0

[ClickHouse] SHALL support Parquet format being writen into and read from a `PostgreSQL` table engine.

#### Special Engines

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.Memory
version: 1.0

[ClickHouse] SHALL support Parquet format being writen into and read from a `Memory` table engine.

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.Distributed
version: 1.0

[ClickHouse] SHALL support Parquet format being writen into and read from a `Distributed` table engine.

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.Dictionary
version: 1.0

[ClickHouse] SHALL support Parquet format being writen into and read from a `Dictionary` table engine.

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.File
version: 1.0

[ClickHouse] SHALL support Parquet format being writen into and read from a `File` table engine.

##### RQ.SRS-032.ClickHouse.Parquet.TableEngines.Special.URL
version: 1.0

[ClickHouse] SHALL support Parquet format being writen into and read from a `URL` table engine.

### Metadata

Parquet files have three types of metadata

- file metadata
- column (chunk) metadata
- page header metadata

as described in https://parquet.apache.org/docs/file-format/metadata/.

#### ParquetFormat

##### RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadataFormat
version: 1.0

[ClickHouse] SHALL support `ParquetMetadata` format to read metadata from Parquet files.

For example,

```sql
SELECT * FROM file(data.parquet, ParquetMetadata) format PrettyJSONEachRow
```

##### RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadataFormat.Output
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

##### RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadata.Content
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

##### RQ.SRS-032.ClickHouse.Parquet.Metadata.ParquetMetadata.MinMax
version: 1.0

[ClickHouse] SHALL support Parquet files that have Min/Max values in the metadata and the files that are missing Min/Max values.

#### Metadata Types

##### RQ.SRS-032.ClickHouse.Parquet.Metadata.File
version: 1.0

[ClickHouse] SHALL support accessing `File Metadata` in Parquet files.

##### RQ.SRS-032.ClickHouse.Parquet.Metadata.Column
version: 1.0

[ClickHouse] SHALL support accessing `Column (Chunk) Metadata` in Parquet files.

##### RQ.SRS-032.ClickHouse.Parquet.Metadata.Header
version: 1.0

[ClickHouse] SHALL support accessing `Page Header Metadata` in Parquet files.

### Error Recovery

#### RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.MissingMagicNumber
version: 1.0

[ClickHouse] SHALL output an error if the 4-byte magic number "PAR1" is missing from the Parquet metadata.

For example,

When using hexeditor on the Parquet file we alter the values of "PAR1" and change it to "PARQ".
then when we try to read that Parquet file in [ClickHouse] we SHALL get an exception:

```
exception. Code: 1001, type: parquet::ParquetInvalidOrCorruptedFileException,
e.what() = Invalid: Parquet magic bytes not found in footer.
Either the file is corrupted or this is not a Parquet file.
```

#### RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.CorruptFile
version: 1.0

[ClickHouse] SHALL output an error when trying to access the corrupt `file` metadata.
In this case the file metadata is corrupt, the file is lost.

#### RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.CorruptColumn
version: 1.0

[ClickHouse] SHALL output an error when trying to access the corrupt `column` metadata.
In this case that column chunk MAY be lost but column chunks for this column in other row groups SHALL be okay.

#### RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.CorruptPageHeader
version: 1.0

[ClickHouse] SHALL output an error when trying to access the corrupt `Page Header`.
In this case the remaining pages in that chunk SHALL be lost.

#### RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.CorruptPageData
version: 1.0

[ClickHouse] SHALL output an error when trying to access the corrupt `Page Data`.
In this case that page SHALL be lost.

#### RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.CorruptColumnValues
version: 1.0

[ClickHouse] SHALL output an error when trying to access the corrupt column values.


#### RQ.SRS-032.ClickHouse.Parquet.Metadata.ErrorRecovery.CorruptChecksum
version: 1.0

[ClickHouse] SHALL output an error if the Parquet file's checksum is corrupted.

### Encoding

##### RQ.SRS-032.ClickHouse.Parquet.Encoding.Plain
version: 1.0

[ClickHouse] SHALL support `Plain` encoded Parquet files.

##### RQ.SRS-032.ClickHouse.Parquet.Encoding.RunLength
version: 1.0

[ClickHouse] SHALL support `Run Length Encoding / Bit-Packing Hybrid` encoded Parquet files.

##### RQ.SRS-032.ClickHouse.Parquet.Encoding.Delta
version: 1.0

[ClickHouse] SHALL support `Delta Encoding` encoded Parquet files.


##### RQ.SRS-032.ClickHouse.Parquet.Encoding.DeltaLengthByteArray
version: 1.0

[ClickHouse] SHALL support `Delta-length byte array` encoded Parquet files.

##### RQ.SRS-032.ClickHouse.Parquet.Encoding.DeltaStrings
version: 1.0

[ClickHouse] SHALL support `Delta Strings` encoded Parquet files.

##### RQ.SRS-032.ClickHouse.Parquet.Encoding.ByteStreamSplit
version: 1.0

[ClickHouse] SHALL support `Byte Stream Split` encoded Parquet files.

[ClickHouse]: https://clickhouse.com
[GitHub Repository]: https://github.com/Altinity/clickhouse-regression/blob/main/parquet/requirements/requirements.md
[Revision History]: https://github.com/Altinity/clickhouse-regression/commits/main/parquet/requirements/requirements.md
[Git]: https://git-scm.com/
[GitHub]: https://github.com
""",
)
