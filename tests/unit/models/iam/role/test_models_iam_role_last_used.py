import unittest
from datetime import datetime

from pyawsopstoolkit.exceptions import ValidationError
from pyawsopstoolkit.models.iam.role import LastUsed


class TestLastUsed(unittest.TestCase):
    """Unit test cases for LastUsed."""

    def setUp(self) -> None:
        self.maxDiff = None
        self.params = {
            'used_date': datetime(2023, 5, 18),
            'region': 'eu-west-1'
        }
        self.last_used_empty = self.create_last_used()
        self.last_used_with_date = self.create_last_used(used_date=self.params['used_date'])
        self.last_used_with_region = self.create_last_used(region=self.params['region'])
        self.last_used = self.create_last_used(
            used_date=self.params['used_date'],
            region=self.params['region']
        )

    @staticmethod
    def create_last_used(**kwargs):
        return LastUsed(**kwargs)

    def test_initialization(self):
        self.assertIsNone(self.last_used_empty.used_date)
        self.assertIsNone(self.last_used_empty.region)

    def test_initialization_with_optional_params(self):
        test_cases = [
            (self.last_used_with_date, self.params['used_date'], None),
            (self.last_used_with_region, None, self.params['region']),
            (self.last_used, self.params['used_date'], self.params['region'])
        ]
        for last_used, used_date, region in test_cases:
            with self.subTest(last_used=last_used):
                self.assertEqual(last_used.used_date, used_date)
                self.assertEqual(last_used.region, region)

    def test_setters(self):
        new_params = {
            'used_date': datetime.today(),
            'region': 'us-east-2'
        }

        self.last_used.used_date = new_params['used_date']
        self.last_used.region = new_params['region']

        self.assertEqual(self.last_used.used_date, new_params['used_date'])
        self.assertEqual(self.last_used.region, new_params['region'])

    def test_invalid_types(self):
        invalid_params = {
            'used_date': '2024-02-06',
            'region': 'Ohio'
        }

        with self.assertRaises(TypeError):
            self.create_last_used(used_date=invalid_params['used_date'])
        with self.assertRaises(ValidationError):
            self.create_last_used(region=invalid_params['region'])

        with self.assertRaises(TypeError):
            self.last_used.used_date = invalid_params['used_date']
        with self.assertRaises(ValidationError):
            self.last_used.region = invalid_params['region']

    def test_to_dict(self):
        expected_dict = {
            "used_date": self.params['used_date'].isoformat(),
            "region": self.params['region']
        }
        self.assertDictEqual(self.last_used.to_dict(), expected_dict)

    def test_to_dict_with_missing_fields(self):
        expected_dict = {
            "used_date": None,
            "region": None
        }
        self.assertDictEqual(self.last_used_empty.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
