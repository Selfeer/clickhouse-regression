#!/usr/bin/env python3
import os
import sys

from testflows.core import *

append_path(sys.path, "..")

from helpers.cluster import create_cluster
from base_58.requirements.requirements import *
from helpers.argparser import argparser as argparser
from helpers.common import check_clickhouse_version
from s3.tests.common import enable_vfs

xfails = {"alias input/alias instead of table and column": [(Fail, "not implemented")]}

xflags = {}

ffails = {}


@TestModule
@ArgumentParser(argparser)
@XFails(xfails)
@XFlags(xflags)
@FFails(ffails)
@Name("base58")
@Specifications(SRS_ClickHouse_Base58_Encoding_and_Decoding)
@Requirements(RQ_ClickHouse_Base58_Encode("1.0"), RQ_ClickHouse_Base58_Decode("1.0"))
def regression(
    self,
    local,
    clickhouse_binary_path,
    clickhouse_version,
    collect_service_logs,
    stress=None,
    parallel=None,
    allow_vfs=False,
):
    """Base58 regression."""
    nodes = {"clickhouse": ("clickhouse1", "clickhouse2", "clickhouse3")}

    self.context.clickhouse_version = clickhouse_version

    with Given("docker-compose cluster"):
        cluster = create_cluster(
            local=local,
            clickhouse_binary_path=clickhouse_binary_path,
            collect_service_logs=collect_service_logs,
            nodes=nodes,
            configs_dir=current_dir(),
        )
        self.context.cluster = cluster
        self.context.stress = stress

    if parallel is not None:
        self.context.parallel = parallel

    if check_clickhouse_version("<22.7")(self):
        skip(reason="only supported on ClickHouse version >= 22.7")

    if allow_vfs:
        with Given("I enable allow_object_storage_vfs"):
            enable_vfs()

    Feature(run=load("base_58.tests.consistency", "feature"))
    Feature(run=load("base_58.tests.null", "feature"))
    Feature(run=load("base_58.tests.alias_input", "feature"))
    Feature(run=load("base_58.tests.function_input", "feature"))
    Feature(run=load("base_58.tests.compatibility", "feature"))
    Feature(run=load("base_58.tests.memory_usage", "feature"))
    Feature(run=load("base_58.tests.performance", "feature"))
    Feature(run=load("base_58.tests.supported_types_constant", "feature"))
    Feature(run=load("base_58.tests.supported_types_column", "feature"))
    Feature(run=load("base_58.tests.unsupported_types_constant", "feature"))
    Feature(run=load("base_58.tests.unsupported_types_column", "feature"))


if main():
    regression()
