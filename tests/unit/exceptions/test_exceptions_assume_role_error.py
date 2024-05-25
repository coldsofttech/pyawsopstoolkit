import unittest

from pyawsopstoolkit import Account
from pyawsopstoolkit.exceptions import AssumeRoleError


class TestAssumeRoleError(unittest.TestCase):
    """Unit test cases for AssumeRoleError."""

    def setUp(self) -> None:
        self.account = Account('123456789012')
        self.role_arn = f'arn:aws:iam::{self.account.number}:role/test_role'
        self.exception = ValueError('invalid value')
        self.message = f'ERROR: Unable to assume role "{self.role_arn}".'
        self.message_with_exception = f'ERROR: Unable to assume role "{self.role_arn}". {self.exception}.'
        self.assume_role_error = AssumeRoleError(self.role_arn)
        self.assume_role_error_with_exception = AssumeRoleError(self.role_arn, self.exception)

    def test_initialization(self):
        self.assertEqual(self.assume_role_error.role_arn, self.role_arn)
        self.assertEqual(self.assume_role_error.message, self.message)
        self.assertIsNone(self.assume_role_error.exception)

    def test_initialization_with_exception(self):
        self.assertEqual(self.assume_role_error_with_exception.role_arn, self.role_arn)
        self.assertEqual(self.assume_role_error_with_exception.message, self.message_with_exception)
        self.assertEqual(self.assume_role_error_with_exception.exception, self.exception)


if __name__ == "__main__":
    unittest.main()
