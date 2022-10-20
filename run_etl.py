import psycopg2.extras as psycopg2_extras
from uuid import uuid4
from datetime import datetime
from xlib.db import WarehouseConnection
from xlib.load_config import _get_warehouse_creds
from xlib.utils import get_exchange_data, _get_exchange_insert_query, get_utc_from_unix_time


def extract():
    url = "https://api.coincap.io/v2/exchanges"
    return get_exchange_data(url)


def transform_enrich(data):
    batchId = str(uuid4())
    batchDatetime = datetime.now()
    # Add batch_id & current date to data before inserting
    for d in data:
        d["batchId"] = batchId
        d["batchDatetime"] = batchDatetime
        d["updatedUTC"] = get_utc_from_unix_time(d.get("updated"))
    return data


def load(data):
    with WarehouseConnection(db_conn=_get_warehouse_creds()).managed_cursor() as cursor:
        psycopg2_extras.execute_batch(cur=cursor, sql=_get_exchange_insert_query(), argslist=data)


if __name__ == "__main__":
    # db_setup()
    data = extract()
    data_enriched = transform_enrich(data)
    load(data_enriched)
    print("Loaded data in database!!!")
