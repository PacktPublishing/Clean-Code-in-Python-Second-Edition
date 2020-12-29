"""Abstraction to the database.

Provide a client to connect to the database and expose a custom API, at the
convenience of the application.

"""
import asyncpg

from .config import DB_CONFIG


async def DBClient():
    return await asyncpg.connect(**DB_CONFIG)
