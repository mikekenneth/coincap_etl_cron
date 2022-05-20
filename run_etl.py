import sys
import requests
import logging
import psycopg2.extras as psycopg2_extras

from datetime import datetime
from uuid import uuid4
from typing import List, Dict, Any
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


def _get_exchange_insert_query() -> str:
    return """
    INSERT INTO crypto.exchange (
        batch_id,
        batch_datetime,
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
        %(batch_id)s,
        %(batch_datetime)s,
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
    batch_id = str(uuid4())
    batch_datetime = datetime.now()
    # Add batch_id & current date to data before inserting
    for d in data:
        d["batch_id"] = batch_id
        d["batch_datetime"] = batch_datetime
        d["update_dt"] = _get_utc_from_unix_time(d.get("updated"))
    with WarehouseConnection(db_conn=_get_warehouse_creds()).managed_cursor() as cursor:
        psycopg2_extras.execute_batch(cur=cursor, sql=_get_exchange_insert_query(), argslist=data)


if __name__ == "__main__":
    run()
