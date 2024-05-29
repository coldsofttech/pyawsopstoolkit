import unittest

from pyawsopstoolkit import Account
from pyawsopstoolkit.models.iam import PermissionsBoundary


class TestPermissionsBoundary(unittest.TestCase):
    """Unit test cases of PermissionsBoundary."""

    def setUp(self) -> None:
        self.account = Account('123456789012')
        self.type = 'Policy'
        self.arn = f'arn:aws:iam::{self.account.number}:policy/ExamplePolicy'
        self.permissions_boundary = PermissionsBoundary(self.type, self.arn)

    def test_initialization(self):
        self.assertEqual(self.permissions_boundary.type, self.type)
        self.assertEqual(self.permissions_boundary.arn, self.arn)

    def test_set_type(self):
        new_type = 'ManagedPolicy'
        self.permissions_boundary.type = new_type
        self.assertEqual(self.permissions_boundary.type, new_type)

    def test_set_arn(self):
        new_arn = f'arn:aws:iam::{self.account.number}:policy/ManagedPolicy'
        self.permissions_boundary.arn = new_arn
        self.assertEqual(self.permissions_boundary.arn, new_arn)

    def test_str(self):
        expected_str = (
            f'PermissionsBoundary('
            f'type="{self.type}",'
            f'arn="{self.arn}"'
            f')'
        )
        self.assertEqual(str(self.permissions_boundary), expected_str)

    def test_to_dict(self):
        expected_dict = {
            "type": self.type,
            "arn": self.arn
        }
        self.assertDictEqual(self.permissions_boundary.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
