import sys
import requests
import logging
import psycopg2.extras as psycopg2_extras

from typing import List, Dict, Any, AnyStr
from xlib.db import WarehouseConnection
from xlib.utils import _get_utc_from_unix_time
from xlib.load_config import _get_warehouse_creds


def get_exchange_data() -> List[Dict[str, Any]]:
    url = "https://api.coincap.io/v2/exchanges"

    try:
        response = requests.get(url=url)
    except requests.ConnectionError as e:
        logging.error(f"The was an error with the request, {e}")
        sys.exit(1)
    return response.json().get("data", [])  # Get "data" object else return an empty list


def _get_exchange_insert_query():
    return """
    INSERT INTO bitcoin.exchange (
        id,
        name,
        rank,
        percenttotalvolume,
        volumeusd,
        tradingpairs,
        socket,
        exchangeurl,
        updated_unix_millis,
        updated_utc
    )
    VALUES (
        %(exchangeId)s,
        %(name)s,
        %(rank)s,
        %(percentTotalVolume)s,
        %(volumeUsd)s,
        %(tradingPairs)s,
        %(socket)s,
        %(exchangeUrl)s,
        %(updated)s,
        %(update_dt)s
    );"""


def run() -> None:
    data = get_exchange_data()
    # Add current date to data before inserting
    for d in data:
        d["update_dt"] = _get_utc_from_unix_time(d.get("updated"))
    with WarehouseConnection(db_conn=_get_warehouse_creds()).managed_cursor() as cursor:
        psycopg2_extras.execute_batch(cur=cursor, sql=_get_exchange_insert_query(), argslist=data)


if __name__ == "__main__":
    run()
