"""Clean Code in Python - Chapter 4, The SOLID Principles

Liskov's Substitution Principle (LSP)
Tests
"""
import unittest

from lsp_2 import Event


class TestLSP(unittest.TestCase):
    def test_vaidate_preconditions(self):
        invalid_events = (
            "not a dict",
            {"reason": "doesn't contain key 'before'", "after": {"foo": "1"}},
            {"reason": "doesn't contain key 'after'", "before": {"foo": "1"}},
            {"before": "'before' is not a dict'", "after": {"foo": "1"}},
            {"after": "not a dict", "before": {"foo": "1"}},
        )
        for event in invalid_events:
            with self.subTest(event=event), self.assertRaises(ValueError):
                Event.validate_precondition(event)

    def test_valid_precondition(self):
        self.assertIsNone(
            Event.validate_precondition(
                {"before": {"foo": 42}, "after": {"bar": 42}}
            )
        )


if __name__ == "__main__":
    unittest.main()
