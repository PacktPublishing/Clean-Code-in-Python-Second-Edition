import unittest
from properties import Coordinate


class TestProperties(unittest.TestCase):
    def test_invalid_coordinates(self):
        for lat, long in (
            (-91, 0),
            (91, 0),
            (90.0001, 0),
            (-90.0001, 0),
            (0, -181),
            (0, -180.0001),
            (0, -200),
            (0, 180.0001),
            (0, 200),
            (0, -180.0001),
            (0, -200),
            (-90.001, -180.001),
            (90.001, 180.001),
        ):
            with self.subTest(case="invalid", lat=lat, long=long), self.assertRaises(ValueError):
                Coordinate(lat, long)

    def test_valid_coordinates(self):
        for lat, long in (
            (0, 0),
            (90, 0),
            (-90, 0),
            (90, 180),
            (90, -180),
            (-90, 180),
            (-90, -180),
            (0, 180),
            (0, -180),
            (41, 2),
            (41.5, 2.1),
        ):
            with self.subTest(case="valid", lat=lat, long=long):
                coord = Coordinate(lat, long)

                self.assertEqual(coord.latitude, lat)
                self.assertEqual(coord.longitude, long)


if __name__ == "__main__":
    unittest.main()
