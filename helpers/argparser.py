import os


def argparser(parser):
    """Default argument parser for regressions."""
    parser.add_argument(
        "--local",
        action="store_true",
        help="run regression in local mode",
        default=True,
    )

    parser.add_argument(
        "--clickhouse-version",
        type=str,
        dest="clickhouse_version",
        help="clickhouse server version",
        metavar="version",
        default=os.getenv("CLICKHOUSE_TESTS_SERVER_VERSION", None),
    )

    parser.add_argument(
        "--clickhouse-binary-path",
        type=str,
        dest="clickhouse_binary_path",
        help="path to ClickHouse binary, default: /usr/bin/clickhouse",
        metavar="path",
        default=os.getenv("CLICKHOUSE_TESTS_SERVER_BIN_PATH", "/usr/bin/clickhouse"),
    )

    parser.add_argument(
        "--keeper-binary-path",
        type=str,
        dest="keeper_binary_path",
        help="path to ClickHouse Keeper binary",
        default=None,
    )

    parser.add_argument(
        "--zookeeper-version",
        type=str,
        dest="zookeeper_version",
        help="Zookeeper version",
        default=None,
    )
    parser.add_argument(
        "--use-keeper",
        action="store_true",
        default=False,
        dest="use_keeper",
        help="use ClickHouse Keeper instead of ZooKeeper",
    )

    parser.add_argument(
        "--stress",
        action="store_true",
        default=False,
        help="enable stress testing (might take a long time)",
    )

    parser.add_argument(
        "--allow-vfs",
        help="Instruct the tests to enable allow_vfs for all external disks",
        action="store_true",
    )

    parser.add_argument(
        "--collect-service-logs",
        action="store_true",
        default=False,
        help="enable docker log collection. for ci/cd use, does not work locally.",
    )

    parser.add_argument(
        "--with-analyzer",
        action="store_true",
        default=False,
        help="Use experimental analyzer.",
    )


def CaptureClusterArgs(func):
    """
    Collect cluster arguments from argparser into cluster_args.

    Usage:

        @TestModule
        @ArgumentParser(argparser)
        @...  # other decorators
        @CaptureClusterArgs
        def regression(
            self,
            cluster_args,
            clickhouse_version,
            stress=None,
            allow_vfs=False,
            with_analyzer=False,
        ):
            nodes = ...

            with Given("docker-compose cluster"):
                cluster = create_cluster(
                    **cluster_args,
                    nodes=nodes,
                    configs_dir=current_dir(),
                    docker_compose_project_dir=os.path.join(
                        current_dir(), os.path.basename(current_dir()) + "_env"
                    ),
                )

            ...

    """

    def capture_cluster_args(
        self,
        local,
        clickhouse_binary_path,
        keeper_binary_path,
        zookeeper_version,
        use_keeper,
        collect_service_logs,
        **kwargs
    ):
        cluster_args = {
            "local": local,
            "clickhouse_binary_path": clickhouse_binary_path,
            "keeper_binary_path": keeper_binary_path,
            "zookeeper_version": zookeeper_version,
            "use_keeper": use_keeper,
            "collect_service_logs": collect_service_logs,
        }
        return func(self, cluster_args=cluster_args, **kwargs)

    return capture_cluster_args
