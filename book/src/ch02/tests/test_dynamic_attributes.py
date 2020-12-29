import unittest
from dynamic import DynamicAttributes


class TestDynamic(unittest.TestCase):
    def test_dynamic_attributes(self):
        dyn = DynamicAttributes("value")

        self.assertEqual(dyn.attribute, "value")
        self.assertEqual(dyn.fallback_test, "[fallback resolved] test")
        self.assertEqual(getattr(dyn, "something", "default"), "default")
        with self.assertRaisesRegex(AttributeError, ".* has no attribute \S+"):
            dyn.something_not_found


if __name__ == "__main__":
    unittest.main()
