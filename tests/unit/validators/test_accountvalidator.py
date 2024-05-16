import unittest

from pyawsopstoolkit.exceptions import ValidationError
from pyawsopstoolkit.validators import AccountValidator


class TestAccountValidator(unittest.TestCase):
    """Unit test cases for AccountValidator class."""

    def test_number_valid(self):
        """Test if number works as expected."""
        numbers = {
            "Number1": "123456789012"
        }

        for key, value in numbers.items():
            self.assertTrue(AccountValidator.number(value, custom_error_message=f'{key} is not valid.'))

    def test_number_invalid(self):
        """Test if number raises exception as expected."""
        numbers = {
            "Number1": "123",
            "Number2": "01234567890123",
            "Number3": 123456789012
        }

        for key, value in numbers.items():
            with self.assertRaises(Exception) as context:
                AccountValidator.number(value)

            self.assertTrue(isinstance(context.exception, (ValidationError, TypeError)))


if __name__ == "__main__":
    unittest.main()
