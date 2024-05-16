import unittest

from pyawsopstoolkit.exceptions import AssumeRoleError


class TestAssumeRoleError(unittest.TestCase):
    """Unit test cases for AssumeRoleError class."""

    def test_valid(self):
        exception = ValueError('Invalid value')
        error = AssumeRoleError('sample role', exception)

        self.assertEqual('sample role', error.role_arn)
        self.assertEqual(exception, error.exception)
        self.assertIsInstance(error.message, str)

    def test_invalid_role_arn(self):
        with self.assertRaises(Exception) as context:
            AssumeRoleError(100)

            self.assertEqual(context.exception, TypeError)

    def test_invalid_exception(self):
        with self.assertRaises(Exception) as context:
            AssumeRoleError('sample role', 'exception')

            self.assertEqual(context.exception, TypeError)


if __name__ == "__main__":
    unittest.main()
