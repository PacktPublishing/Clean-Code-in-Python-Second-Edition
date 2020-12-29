"""Clean Code in Python - Chapter 7: Generators, Iterators, and Asynchronous Programming

> Asynchronous programming / asynchronous iteration
"""
import asyncio


async def coroutine(index: int) -> int:
    await asyncio.sleep(0.1)
    return index * 1_000


class RecordStreamer:
    def __init__(self, max_rows=100) -> None:
        self._current_row = 0
        self._max_rows = max_rows

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self._current_row < self._max_rows:
            row = (self._current_row, await coroutine(self._current_row))
            self._current_row += 1
            return row
        raise StopAsyncIteration


NOT_SET = object()


async def anext(async_generator_expression, default=NOT_SET):
    try:
        return await async_generator_expression.__anext__()
    except StopAsyncIteration:
        if default is NOT_SET:
            raise
        return default


async def record_streamer(max_rows):
    current_row = 0
    while current_row < max_rows:
        row = (current_row, await coroutine(current_row))
        current_row += 1
        yield row
