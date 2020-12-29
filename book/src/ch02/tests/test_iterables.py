import unittest
from datetime import datetime, timedelta

from iterables import (
    DateRangeContainerIterable,
    DateRangeIterable,
    DateRangeSequence,
)


class TestIterables(unittest.TestCase):
    def setUp(self):
        self.start_date = datetime(2016, 7, 17)
        self.end_date = datetime(2016, 7, 24)
        self.expected = [datetime(2016, 7, i) for i in range(17, 24)]

    def _base_test_date_range(self, range_cls):
        date_range = range_cls(self.start_date, self.end_date)
        self.assertListEqual(list(date_range), self.expected)
        self.assertEqual(date_range.start_date, self.start_date)
        self.assertEqual(date_range.end_date, self.end_date)

    def test_date_range(self):
        for range_cls in (
            DateRangeIterable,
            DateRangeContainerIterable,
            DateRangeSequence,
        ):
            with self.subTest(type_=range_cls.__name__):
                self._base_test_date_range(range_cls)

    def test_date_range_sequence(self):
        date_range = DateRangeSequence(self.start_date, self.end_date)

        self.assertEqual(date_range[0], self.start_date)
        self.assertEqual(date_range[-1], self.end_date - timedelta(days=1))
        self.assertEqual(len(date_range), len(self.expected))


if __name__ == "__main__":
    unittest.main()
