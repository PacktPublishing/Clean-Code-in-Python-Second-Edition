"""Clean Code in Python - Chapter 5: Decorators

> Decorators for coroutines & functions
"""
import inspect
import asyncio
from functools import wraps
import time

X, Y = 1, 2


def decorator(callable):
    """Call <callable> with fixed values"""

    @wraps(callable)
    def wrapped():
        return callable(X, Y)

    return wrapped


@decorator
def func(x, y):
    return x + y


@decorator
async def coro(x, y):
    return x + y


def timing(callable):
    @wraps(callable)
    def wrapped(*args, **kwargs):
        start = time.time()
        result = callable(*args, **kwargs)
        latency = time.time() - start
        return {"latency": latency, "result": result}

    @wraps(callable)
    async def wrapped_coro(*args, **kwargs):
        start = time.time()
        result = await callable(*args, **kwargs)
        latency = time.time() - start
        return {"latency": latency, "result": result}

    if inspect.iscoroutinefunction(callable):
        return wrapped_coro

    return wrapped


@timing
def func2():
    time.sleep(0.1)
    return 42


@timing
async def coro2():
    await asyncio.sleep(0.1)
    return 42
