from configparser import ConfigParser
from typing import Optional, Any
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
