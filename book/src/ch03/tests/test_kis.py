"""Clean Code in Python - Chapter 3: General traits of good code

> Keep It Simple
"""
import unittest


from kis import Namespace


class TestKis(unittest.TestCase):
    def test_namespace(self):
        cn = Namespace(
            id_=42, user="root", location="127.0.0.1", extra="excluded"
        )
        self.assertEqual(
            (cn.id_, cn.user, cn.location), (42, "root", "127.0.0.1")
        )
        self.assertFalse(hasattr(cn, "extra"))


if __name__ == "__main__":
    unittest.main()
