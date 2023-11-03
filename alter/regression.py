#!/usr/bin/env python3
import os
import sys
import boto3

from testflows.core import *

append_path(sys.path, "..")

from helpers.cluster import Cluster
from s3.regression import argparser
from alter.table.replace_partition.requirements.requirements import *
from helpers.datatypes import *

xfails = {
    "/alter/replace partition/concurrent actions/alter modify ttl": [
        (
            Fail,
            "modify ttl expression `+ INTERVAL 1 YEAR` deletes all data when date is empty",
        )
    ],
    "/alter/replace partition/concurrent merges and mutations/mutations on unrelated partition": [
        (
            Fail,
            "The pr is not done yet: https://github.com/ClickHouse/ClickHouse/pull/54272",
        )
    ],
    "/alter/replace partition/concurrent merges and mutations/merges on unrelated partition": [
        (
            Fail,
            "The pr is not done yet: https://github.com/ClickHouse/ClickHouse/pull/54272",
        )
    ],
}

xflags = {}

ffails = {
    "/alter/replace partition/temporary table": (
        Skip,
        "Not implemented before 23.5",
        check_clickhouse_version("<23.5"),
    ),
}


@TestModule
@ArgumentParser(argparser)
@XFails(xfails)
@XFlags(xflags)
@FFails(ffails)
@Requirements(RQ_SRS_032_ClickHouse_Alter_Table_ReplacePartition("1.0"))
@Name("alter")
def regression(
    self,
    local,
    clickhouse_version,
    clickhouse_binary_path,
    collect_service_logs,
    storages,
    stress,
    minio_uri,
    gcs_uri,
    aws_s3_region,
    aws_s3_bucket,
    minio_root_user,
    minio_root_password,
    aws_s3_access_key,
    aws_s3_key_id,
    gcs_key_secret,
    gcs_key_id,
    node="clickhouse1",
):
    """Alter regression."""
    nodes = {"clickhouse": ("clickhouse1", "clickhouse2", "clickhouse3")}

    self.context.clickhouse_version = clickhouse_version

    with Cluster(
        local,
        clickhouse_binary_path,
        collect_service_logs=collect_service_logs,
        nodes=nodes,
    ) as cluster:
        self.context.cluster = cluster

        Feature(run=load("alter.table.replace_partition.feature", "feature"))


if main():
    regression()
