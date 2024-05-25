import unittest

from pyawsopstoolkit.exceptions import ValidationError


class TestValidationError(unittest.TestCase):
    """Unit test cases for ValidationError."""

    def setUp(self) -> None:
        self.message = 'test message'
        self.exception = ValueError('invalid value')
        self.validation_error = ValidationError(self.message)
        self.validation_error_with_exception = ValidationError(self.message, self.exception)

    def test_initialization(self):
        self.assertEqual(self.validation_error.message, f'ERROR: {self.message}.')
        self.assertIsNone(self.validation_error.exception)

    def test_initialization_with_exception(self):
        self.assertEqual(
            self.validation_error_with_exception.message, f'ERROR: {self.message}. {self.exception}.'
        )
        self.assertEqual(self.validation_error_with_exception.exception, self.exception)


if __name__ == "__main__":
    unittest.main()
