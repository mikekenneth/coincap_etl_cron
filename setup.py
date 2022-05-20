from xlib.db import WarehouseConnection
from xlib.load_config import _get_warehouse_creds


if __name__ == "__main__":
    with WarehouseConnection(db_conn=_get_warehouse_creds()).managed_cursor() as cursor, open(
        "assets/db_setup.sql"
    ) as sqlfile:
        cursor.execute(sqlfile.read())
        if cursor.statusmessage == "CREATE TABLE":  # Check if table was successfuly created
            print("Successfully Setup coinCap Exchange Database !")
        else:
            print("Failed to Setup coinCap Exchange Database !")
