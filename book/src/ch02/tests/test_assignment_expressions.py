import unittest


from assignment_expressions import (
    collect_account_ids_from_arns,
    collect_account_ids_from_arns2,
    collect_account_ids_from_arns3,
)


class TestCollectIds(unittest.TestCase):
    data = (
        "arn:aws:iam::123456789012:user/Development/product_1234/*",
        "arn:aws:iam::123456789012:user",
        "arn:aws:s3:::my_corporate_bucket/*",
        "arn:aws:iam::999999999999:user/Development/product_1234/*",
    )
    expected = {"123456789012", "999999999999"}
    test_cases = (
        collect_account_ids_from_arns,
        collect_account_ids_from_arns2,
        collect_account_ids_from_arns3,
    )

    def test(self):
        for case in self.test_cases:
            with self.subTest(testing=case):
                self.assertSetEqual(self.expected, obtained := case(self.data), obtained)


if __name__ == "__main__":
    unittest.main()
