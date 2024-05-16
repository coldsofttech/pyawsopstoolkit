import unittest

from pyawsopstoolkit.exceptions import ValidationError
from pyawsopstoolkit.validators import Validator


class TestValidator(unittest.TestCase):
    """Unit test cases for Validator class."""

    def test_region_valid(self):
        """Test if region works as expected."""
        regions = {
            "Region1": "us-east-1",
            "Region2": "af-south-1",
            "Region3": "ap-northeast-1"
        }

        for key, value in regions.items():
            self.assertTrue(Validator.region(value, custom_error_message=f'{key} is not valid.'))

    def test_region_invalid(self):
        """Test if region raises exception as expected."""
        regions = {
            "Region1": "usa-east-1",
            "Region2": "usa-east1-1",
            "Region3": "us-eas-1",
            "Region4": "us-east-12"
        }

        for key, value in regions.items():
            with self.assertRaises(Exception) as context:
                Validator.region(value)

                self.assertTrue(isinstance(context.exception, (ValidationError, TypeError)))


if __name__ == "__main__":
    unittest.main()
