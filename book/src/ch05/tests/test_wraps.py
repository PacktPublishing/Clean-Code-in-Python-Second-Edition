"""Clean Code in Python - Chapter 5: Decorators

Tests for examples with ``functools.wraps``
"""

import unittest

from decorator_wraps_1 import process_account as process_account_1
from decorator_wraps_2 import process_account as process_account_2


class TestWraps1(unittest.TestCase):
    def test_name_incorrect(self):
        self.assertEqual(
            process_account_1.__qualname__, "trace_decorator.<locals>.wrapped"
        )

    def test_no_docstring(self):
        self.assertIsNone(process_account_1.__doc__)

    def test_no_annotations(self):
        self.assertDictEqual(process_account_1.__annotations__, {})


class TestWraps2(unittest.TestCase):
    def test_name_solved(self):
        self.assertEqual(process_account_2.__qualname__, "process_account")

    def test_docsting_preserved(self):
        self.assertTrue(process_account_2.__doc__.startswith("Process"))

    def test_annotations(self):
        self.assertDictEqual(
            process_account_2.__annotations__, {"account_id": str}
        )


if __name__ == "__main__":
    unittest.main()
