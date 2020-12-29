"""Clean Code in Python - Chapter 5: Decorators


Composition over inheritance, tests for examples 1 & 2
"""
import unittest

from composition_1 import Customer as Customer1
from composition_2 import Customer as Customer2


class BaseTestMixin:
    def test_resolver_finds_attributes(self):
        with self.subTest(test_class=self._CLASS_TO_TEST):
            customer = self._CLASS_TO_TEST(1, "foo", "address")

            self.assertEqual(customer.resolve_customer_id, 1)
            self.assertEqual(customer.resolve_name, "foo")
            self.assertEqual(customer.resolve_address, "address")
            self.assertEqual(customer.customer_id, 1)

    def test_resolver_attribute_error(self):
        with self.subTest(test_class=self._CLASS_TO_TEST):
            customer = self._CLASS_TO_TEST(1, "foo", "address")

            self.assertEqual(customer.name, "foo")
            with self.assertRaises(AttributeError):
                customer.resolve_foo


class TestInheritance(BaseTestMixin, unittest.TestCase):
    _CLASS_TO_TEST = Customer1


class TestDecorator(BaseTestMixin, unittest.TestCase):
    _CLASS_TO_TEST = Customer2


if __name__ == "__main__":
    unittest.main()
