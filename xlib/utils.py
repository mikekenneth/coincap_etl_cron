import sys
import requests
import logging
from configparser import ConfigParser
from typing import Optional, List, Dict, Any
from datetime import datetime


def _get_conf(ini_file: str, section: str = None) -> dict:
    """Get section configurations from ini file
    Args:
        ini_file (str): Configuration file that will be parsed
        section (str, optional): Specify the section to be return
    """
    config = ConfigParser()
    config.read(ini_file)
    if section is not None:
        return dict(config[section])
    return {i: dict(config[i]) for i in config.sections()}


def _get_utc_from_unix_time(unix_ts: Optional[Any], second: int = 1000) -> Optional[datetime]:
    return datetime.utcfromtimestamp(int(unix_ts) / second) if unix_ts else None


def _get_exchange_insert_query() -> str:
    return """
    INSERT INTO crypto.exchange (
        batchId,
        batchDatetime,
        id,
        name,
        rank,
        percentTotalVolume,
        volumeUsd,
        tradingPairs,
        socket,
        exchangeUrl,
        updated,
        updatedUTC
    )
    VALUES (
        %(batchId)s,
        %(batchDatetime)s,
        %(exchangeId)s,
        %(name)s,
        %(rank)s,
        %(percentTotalVolume)s,
        %(volumeUsd)s,
        %(tradingPairs)s,
        %(socket)s,
        %(exchangeUrl)s,
        %(updated)s,
        %(updatedUTC)s
    );"""


def get_exchange_data(url) -> List[Dict[str, Any]]:
    try:
        response = requests.get(url=url)
    except requests.ConnectionError as e:
        logging.error(f"The was an error with the request, {e}")
        sys.exit(1)
    return response.json().get("data", [])  # Get "data" object else return an empty list
