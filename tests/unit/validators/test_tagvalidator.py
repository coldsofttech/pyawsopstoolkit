import unittest

from pyawsopstoolkit.exceptions import ValidationError
from pyawsopstoolkit.validators import TagValidator


class TestTagValidator(unittest.TestCase):
    """Unit test cases for TagValidator class."""

    def test_tag_valid(self):
        """Test if tag works as expected."""
        tags = {
            "Tags1": {"Key": "test", "Value": "test"},
            "Tags2": {"key-major": "test-1", "value-major": "test_123"},
            "Tags3": {"just:key": "key1"},
            "Tags4": [
                {"Key": "test", "Value": "test"},
                {"key-major": "test-1", "value-major": "test_123"},
                {"just:key": "key1"}
            ]
        }

        for key, value in tags.items():
            self.assertTrue(TagValidator.tag(value, custom_error_message=f'{key} is not valid.'))

    def test_tag_invalid(self):
        """Test if tag raises exception as expected."""
        tags = {
            "Tags1": {1: "test", "2:value": "test"},
            "Tags2": {"key": 1, "value": True},
            "Tags3": "key=key,value=value"
        }

        for key, value in tags.items():
            with self.assertRaises(Exception) as context:
                TagValidator.tag(value, custom_error_message=f'{key} is not valid.')

                self.assertTrue(isinstance(context.exception, (ValidationError, TypeError)))


if __name__ == "__main__":
    unittest.main()
