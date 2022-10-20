import os
from .db import DBConnection


def _get_warehouse_creds() -> DBConnection:
    return DBConnection(
        user=os.getenv("WAREHOUSE_USER"),
        password=os.getenv("WAREHOUSE_PASSWORD"),
        db=os.getenv("WAREHOUSE_DB"),
        host=os.getenv("WAREHOUSE_HOST"),
        port=int(os.getenv("WAREHOUSE_PORT")),
    )
