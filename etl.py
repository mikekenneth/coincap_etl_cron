import psycopg2.extras as psycopg2_extras
from uuid import uuid4
from datetime import datetime
from xlib.db import WarehouseConnection
from xlib.load_config import _get_warehouse_creds
from xlib.utils import get_exchange_data, _get_exchange_insert_query, _get_utc_from_unix_time


def extract():
    return get_exchange_data()


def transform_enrich(data):
    batch_id = str(uuid4())
    batch_datetime = datetime.now()
    # Add batch_id & current date to data before inserting
    for d in data:
        d["batch_id"] = batch_id
        d["batch_datetime"] = batch_datetime
        d["update_dt"] = _get_utc_from_unix_time(d.get("updated"))
    return data


def load(data):
    with WarehouseConnection(db_conn=_get_warehouse_creds()).managed_cursor() as cursor:
        psycopg2_extras.execute_batch(cur=cursor, sql=_get_exchange_insert_query(), argslist=data)
