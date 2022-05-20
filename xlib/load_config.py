from .utils import _get_conf
from .db import DBConnection


# Get Configurations
CONFIG = _get_conf(ini_file=".conf.ini", section="POSTGRES")


def _get_warehouse_creds() -> DBConnection:
    return DBConnection(
        user=CONFIG["user"],
        password=CONFIG["password"],
        db=CONFIG["db"],
        host=CONFIG["host"],
        port=int(CONFIG["port"]),
    )
