"""Configuration file for the DB Client
Modify this file according to your environment.
"""
import os


def _extract_from_env(variable, *, default=None):
    try:
        return os.environ[variable]

    except KeyError as e:
        if default is not None:
            return default

        raise RuntimeError(f"Environment variable {variable} not set") from e


DB_CONFIG = {
    "user": _extract_from_env("DBUSER"),
    "password": _extract_from_env("DBPASSWORD"),
    "database": _extract_from_env("DBNAME"),
    "host": "db",
    "port": 5432,
}
