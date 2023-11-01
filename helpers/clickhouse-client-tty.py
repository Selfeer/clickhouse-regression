#!/usr/bin/env python3

from clickhouse_driver import Client
import sys


def clickhouse_client_tty():
    client = Client("localhost")

    while True:
        query = input("[clickhouse1] :) ")

        if query.lower() in ["exit", "quit"]:
            print("Exiting...")
            sys.exit(0)

        try:
            result = client.execute(query)
            print(query)

            for row in result:
                print(row)
        except Exception as e:
            print(f"Error executing query: {e}")


if __name__ == "__main__":
    clickhouse_client_tty()
