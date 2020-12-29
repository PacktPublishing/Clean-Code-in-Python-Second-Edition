import unittest

from packing_1 import (
    User,
    bad_users_from_rows,
    users_from_rows,
    users_from_rows2,
    USERS,
)


class TestPacking(unittest.TestCase):
    def test_users_list(self):
        for function in bad_users_from_rows, users_from_rows, users_from_rows2:
            with self.subTest(function=function):
                users = function(USERS)
                self.assertTrue(all(isinstance(u, User) for u in users))


if __name__ == "__main__":
    unittest.main()
