import psycopg2
from contextlib import contextmanager
from dataclasses import dataclass


@dataclass
class DBConnection:
    db: str
    user: str
    password: str
    host: str
    port: int = 5432


class WarehouseConnection:
    def __init__(self, db_conn=DBConnection):
        self.connection_url = (
            f"postgresql://{db_conn.user}:{db_conn.password}@{db_conn.host}:{db_conn.port}/{db_conn.db}"
        )

    @contextmanager
    def managed_cursor(self, cursor_factory=None):
        self.connection = psycopg2.connect(self.connection_url)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor(cursor_factory=cursor_factory)
        try:
            yield self.cursor
        finally:
            self.cursor.close()
            self.connection.close()
