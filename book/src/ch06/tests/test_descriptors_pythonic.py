"""Clean Code in Python - Chapter 6: Descriptors

> A Pythonic Implementation

Tests for src/descriptors_pythonic_{1,2}.py
"""
import unittest

from descriptors_pythonic_1 import Traveler as TravelerNaiveImplementation
from descriptors_pythonic_2 import Traveler as TravelerWithDescriptor


class TestDescriptorTraceability(unittest.TestCase):
    def _test_case(self, traveller_cls):
        alice = traveller_cls("Alice", "Barcelona")
        alice.current_city = "Paris"
        alice.current_city = "Brussels"
        alice.current_city = "Amsterdam"

        self.assertListEqual(
            alice.cities_visited,
            ["Barcelona", "Paris", "Brussels", "Amsterdam"],
        )
        self.assertEqual(alice.current_city, "Amsterdam")

        alice.current_city = "Amsterdam"
        self.assertListEqual(
            alice.cities_visited,
            ["Barcelona", "Paris", "Brussels", "Amsterdam"],
        )

        bob = traveller_cls("Bob", "Rotterdam")
        bob.current_city = "Amsterdam"

        self.assertEqual(bob.current_city, "Amsterdam")
        self.assertListEqual(bob.cities_visited, ["Rotterdam", "Amsterdam"])

    def test_trace_attribute(self):
        for test_cls in (
            TravelerNaiveImplementation,
            TravelerWithDescriptor,
        ):
            with self.subTest(case=test_cls):
                self._test_case(test_cls)


if __name__ == "__main__":
    unittest.main()
