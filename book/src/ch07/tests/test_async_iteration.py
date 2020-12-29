"""Tests for asynchronous iteration"""

import unittest
import pytest
from unittest.mock import ANY, patch

from async_iteration import (
    RecordStreamer,
    anext,
    record_streamer,
)


@pytest.fixture(autouse=True)
def no_sleep():
    with patch("asyncio.sleep"):
        yield


class TestAsyncIteration(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.streamer = RecordStreamer(10)

    async def test_record_streamer(self):
        collected_rows = [row_id async for row_id, _ in self.streamer]
        self.assertEqual(len(collected_rows), 10)

    async def test_async_stop_iteration(self):
        streamer = RecordStreamer(1)
        self.assertEqual(await streamer.__anext__(), (0, ANY))
        with self.assertRaises(StopAsyncIteration):
            await streamer.__anext__()

    async def test_anext_finds_first_value(self):
        first_value = await anext(
            value async for _, value in self.streamer if value > 7500
        )
        self.assertTrue(first_value > 7500)

    async def test_anext_with_default(self):
        for default_set in (-1, None):
            streamer = RecordStreamer(10)
            not_found_with_default = await anext(
                (
                    (rid, value)
                    async for rid, value in streamer
                    if value > 10_000
                ),
                default_set,
            )
            with self.subTest(case="default-value", default=default_set):
                self.assertEqual(not_found_with_default, default_set)

    async def test_default_not_used_when_found(self):
        streamer = RecordStreamer(10)
        first = await anext((row async for row in streamer), None)
        self.assertIsNotNone(first)

    async def test_anext_fails(self):
        with self.assertRaises(StopAsyncIteration):
            await anext(
                (rid, value)
                async for rid, value in self.streamer
                if value > 10000
            )


class TestAsyncGenerator(unittest.IsolatedAsyncioTestCase):
    async def test_record_streamer(self):
        streamer = record_streamer(1)
        first = await anext(streamer)
        self.assertEqual(first[0], 0)

        row_ids = [rowid async for rowid, _ in record_streamer(10)]
        self.assertListEqual(row_ids, list(range(10)))


if __name__ == "__main__":
    unittest.main()
