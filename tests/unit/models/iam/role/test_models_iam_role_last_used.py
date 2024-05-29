import unittest
from datetime import datetime

from pyawsopstoolkit.models.iam.role import LastUsed


class TestLastUsed(unittest.TestCase):
    """Unit test cases for LastUsed."""

    def setUp(self) -> None:
        self.used_date = datetime(2023, 5, 18)
        self.region = 'eu-west-1'
        self.last_used_empty = LastUsed()
        self.last_used_with_date = LastUsed(used_date=self.used_date)
        self.last_used_with_region = LastUsed(region=self.region)
        self.last_used = LastUsed(self.used_date, self.region)

    def test_initialization_empty(self):
        self.assertIsNone(self.last_used_empty.used_date)
        self.assertIsNone(self.last_used_empty.region)

    def test_initialization_with_date(self):
        self.assertEqual(self.last_used_with_date.used_date, self.used_date)
        self.assertIsNone(self.last_used_with_date.region)

    def test_initialization_with_region(self):
        self.assertIsNone(self.last_used_with_region.used_date)
        self.assertEqual(self.last_used_with_region.region, self.region)

    def test_initialization(self):
        self.assertEqual(self.last_used.used_date, self.used_date)
        self.assertEqual(self.last_used.region, self.region)

    def test_set_used_date(self):
        new_used_date = datetime.today()
        self.last_used.used_date = new_used_date
        self.assertEqual(self.last_used.used_date, new_used_date)

    def test_set_region(self):
        new_region = 'us-east-2'
        self.last_used.region = new_region
        self.assertEqual(self.last_used.region, new_region)

    def test_str(self):
        expected_str = (
            f'LastUsed('
            f'used_date={self.used_date.isoformat()},'
            f'region="{self.region}"'
            f')'
        )
        self.assertEqual(str(self.last_used), expected_str)

    def test_to_dict(self):
        expected_dict = {
            "used_date": self.used_date.isoformat(),
            "region": self.region
        }
        self.assertDictEqual(self.last_used.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
