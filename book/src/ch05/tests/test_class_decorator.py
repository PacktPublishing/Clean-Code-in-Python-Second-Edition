"""Clean Code in Python - Chapter 5: Decorators
Unit tests for class decorators
"""
import unittest
from datetime import datetime
from decorator_class_1 import LoginEvent as LoginEvent1
from decorator_class_2 import LoginEvent as LoginEvent2


class TestLoginEventSerialized(unittest.TestCase):
    classes_under_test = (LoginEvent1, LoginEvent2)

    def test_serializetion(self):
        for class_ in self.classes_under_test:
            with self.subTest(case=class_):
                event = class_(
                    "username",
                    "password",
                    "127.0.0.1",
                    datetime(2016, 7, 20, 15, 45),
                )
                expected = {
                    "username": "username",
                    "password": "**redacted**",
                    "ip": "127.0.0.1",
                    "timestamp": "2016-07-20 15:45",
                }
                self.assertEqual(event.serialize(), expected)


if __name__ == "__main__":
    unittest.main()
