"""Clean Code in Python - Chapter 6: Descriptors

> How Python uses descriptors internally.

"""

import io
import re
from contextlib import redirect_stdout
from unittest import TestCase, main

from descriptors_cpython_1 import Method, MyClass1, MyClass2, NewMethod
from descriptors_cpython_2 import Coordinate2D
from descriptors_cpython_3 import MyClass, TableEvent


class TestDescriptorsCPython1(TestCase):
    def setUp(self):
        self.pattern = re.compile(
            r"(External|Internal) call: .* called with \S+ and \S+",
            re.DOTALL | re.MULTILINE,
        )

    def test_method_unbound_fails(self):
        instance = MyClass1()

        capture = io.StringIO()
        with redirect_stdout(capture):
            Method("External call")(instance, "first", "second")

        result = capture.getvalue()

        self.assertIsNotNone(self.pattern.match(result), repr(result))

        with self.assertRaises(TypeError):
            instance.method("first", "second")

    def test_working_example(self):
        instance = MyClass2()
        capture = io.StringIO()

        with redirect_stdout(capture):
            NewMethod("External call")(instance, "first", "second")

        external = capture.getvalue()
        self.assertIsNotNone(self.pattern.match(external), repr(external))

        capture = io.StringIO()
        with redirect_stdout(capture):
            instance.method("first", "second")

        internal = capture.getvalue()
        self.assertIsNotNone(self.pattern.match(internal), repr(internal))


class TestDescriptorSlots(TestCase):
    def test_slots(self):
        coord = Coordinate2D(1, 2)
        self.assertEqual(repr(coord), "Coordinate2D(1, 2)")
        self.assertEqual(coord.lat, 1)
        self.assertEqual(coord.long, 2)
        with self.assertRaises(AttributeError):
            coord.new = "something not allowed"

        with self.assertRaises(TypeError):
            vars(coord)


class TestClassMethod(TestCase):
    def test_class_method(self):
        self.assertEqual(
            MyClass().class_method("first", "second"),
            "MyClass called with arguments: first, and second",
        )
        self.assertEqual(
            MyClass.class_method("one", "two"),
            "MyClass called with arguments: one, and two",
        )
        self.assertEqual(
            MyClass().method(),
            "MyClass called with arguments: self, and from method",
            "A regular method call should work",
        )

    def test_class_property(self):
        self.assertEqual(
            TableEvent.topic,
            "public.user",
            "The property obtained from the class, works as attribute",
        )
        self.assertEqual(
            TableEvent().topic,
            "public.user",
            "Also works on regular objects",
        )


if __name__ == "__main__":
    main()
