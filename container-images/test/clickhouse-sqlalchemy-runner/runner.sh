#!/bin/bash
set -xe

# install clickhouse, make sure binaries for common and client in /clickhouse folder

clickhouse server --daemon
sleep 10
clickhouse-client -q "SELECT 1"

apt update

apt install git -y

git clone --branch "${RELEASE}" --depth 1 --single-branch "https://github.com/xzkostyan/clickhouse-sqlalchemy.git"
cd clickhouse-sqlalchemy
git apply /sqlalchemy.patch

apt install python3-pip -y

pip install --upgrade pip
pip install asynch
python3 testsrequire.py && python3 setup.py develop
pytest -v
