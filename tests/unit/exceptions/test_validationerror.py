import unittest

from pyawsopstoolkit.exceptions import ValidationError


class TestValidationError(unittest.TestCase):
    """Unit test cases for ValidationError class."""

    def test_valid(self):
        exception = ValueError('Invalid value')
        error = ValidationError('sample message', exception)

        self.assertIsInstance(error.message, str)
        self.assertEqual(exception, error.exception)

    def test_invalid_message(self):
        with self.assertRaises(Exception) as context:
            ValidationError(100)

            self.assertEqual(context.exception, TypeError)

    def test_invalid_exception(self):
        with self.assertRaises(Exception) as context:
            ValidationError('sample message', 'exception')

            self.assertEqual(context.exception, TypeError)


if __name__ == "__main__":
    unittest.main()
