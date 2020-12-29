import unittest

from coroutines import X, Y, func, coro, func2, coro2


class TestCoroutinesDecorators(unittest.IsolatedAsyncioTestCase):
    def test_function(self):
        self.assertEqual(func(), X + Y)

    async def test_coroutine(self):
        self.assertEqual(await coro(), X + Y)

    def test_timing_function(self):
        result = func2()
        self.assertTrue(result["latency"] >= 0.1)
        self.assertEqual(result["result"], 42)

    async def test_timing_coroutine(self):
        result = await coro2()
        self.assertTrue(result["latency"] >= 0.1)
        self.assertEqual(result["result"], 42)


if __name__ == "__main__":
    unittest.main()
