"""Clean Code in Python - Second edition - Chapter 7

> Generators / Asynchronous context managers
"""
import contextlib
import asyncio


async def stop_database():
    await asyncio.sleep(0.1)
    print("systemctl stop postgresql.service")


async def start_database():
    await asyncio.sleep(0.2)
    print("systemctp start postgresql.service")


@contextlib.asynccontextmanager
async def db_management():
    try:
        await stop_database()
        yield
    finally:
        await start_database()


async def create_metrics_logger():
    await asyncio.sleep(0.01)
    return "metrics-logger"


@contextlib.asynccontextmanager
async def metrics_logger():
    yield await create_metrics_logger()


async def run_db_backup():
    async with db_management(), metrics_logger():
        print("Performing DB backup...")
