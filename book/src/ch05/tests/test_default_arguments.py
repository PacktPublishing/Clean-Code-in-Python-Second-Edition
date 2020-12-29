"""Clean Code in Python - Chapter 5: Decorators

tests for default_arguments.py
"""

import unittest

from default_arguments import decorator, DEFAULT_X, DEFAULT_Y


class TestDefaultArgumentsDecorator(unittest.TestCase):
    def test_default_callable(self):
        @decorator()
        def my_function(x, y):
            return {"x": x, "y": y}

        obtained = my_function()
        self.assertDictEqual(obtained, {"x": DEFAULT_X, "y": DEFAULT_Y})

    def test_default_no_callable(self):
        @decorator
        def my_function(x, y):
            return {"x": x, "y": y}

        obtained = my_function()
        self.assertDictEqual(obtained, {"x": DEFAULT_X, "y": DEFAULT_Y})

    def test_one_argument(self):
        @decorator(x=2)
        def f1(x, y):
            return x + y

        @decorator(y=3)
        def f2(x, y):
            return x + y

        self.assertEqual(f1(), 2 + DEFAULT_Y)
        self.assertEqual(f2(), DEFAULT_X + 3)

    def test_all_arguments(self):
        @decorator(x=3, y=4)
        def my_function(x, y):
            return x + y

        self.assertEqual(my_function(), 3 + 4)


if __name__ == "__main__":
    unittest.main()
