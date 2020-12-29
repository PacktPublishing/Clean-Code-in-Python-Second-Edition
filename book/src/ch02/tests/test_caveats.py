import unittest
from caveats import BadList, GoodList


class TestCaveats(unittest.TestCase):
    def test_bad_list(self):
        bl = BadList((0, 1, 2, 3, 4, 5))
        self.assertEqual(bl[0], "[even] 0")
        self.assertEqual(bl[3], "[odd] 3")
        self.assertRaises(TypeError, str.join, bl)

    def test_good_list(self):
        gl = GoodList((0, 1, 2))
        self.assertEqual(gl[0], "[even] 0")
        self.assertEqual(gl[1], "[odd] 1")

        expected = "[even] 0; [odd] 1; [even] 2"
        self.assertEqual("; ".join(gl), expected)


if __name__ == "__main__":
    unittest.main()
