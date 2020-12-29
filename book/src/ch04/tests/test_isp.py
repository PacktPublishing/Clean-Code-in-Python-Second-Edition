import unittest

from isp import EventParser


class TestEventParser(unittest.TestCase):
    def test_parse_from_xml(self):
        self.assertIsInstance(EventParser(), EventParser)


if __name__ == "__main__":
    unittest.main()
