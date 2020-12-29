"""Clean code in Python - Second edition
Chapter 04, the SOLID principles

Tests for the Open/Closed Principle (OCP) examples 1 through 3
"""
import unittest

from openclosed_1 import SystemMonitor as SystemMonitor1
from openclosed_2 import SystemMonitor as SystemMonitor2
from openclosed_3 import SystemMonitor as SystemMonitor3


class TestBaseMixin:
    def test_identify_event(self):
        for event_data, expected_event_name in self.test_cases:
            monitor = self.class_under_test(event_data)
            identified_event = monitor.identify_event()
            with self.subTest(data=event_data, expected=expected_event_name):
                self.assertEqual(
                    identified_event.__class__.__name__, expected_event_name
                )


class BaseTestOCP(unittest.TestCase):
    test_cases = (
        ({"before": {"session": 0}, "after": {"session": 1}}, "LoginEvent"),
        ({"before": {"session": 1}, "after": {"session": 0}}, "LogoutEvent"),
        ({"before": {"session": 1}, "after": {"session": 1}}, "UnknownEvent"),
    )


class TestOCP1(TestBaseMixin, BaseTestOCP):
    class_under_test = SystemMonitor1


class TestOCP2(TestBaseMixin, BaseTestOCP):
    class_under_test = SystemMonitor2


class TestOCP3(TestBaseMixin, BaseTestOCP):
    class_under_test = SystemMonitor3
    test_cases = (
        *BaseTestOCP.test_cases,
        ({"after": {"transaction": "Tx001"}}, "TransactionEvent"),
        ({"after": {"not-a-transaction": "Tx001"}}, "UnknownEvent"),
    )


if __name__ == "__main__":
    unittest.main()
