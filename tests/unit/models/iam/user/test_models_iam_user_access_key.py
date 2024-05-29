import unittest
from datetime import datetime

from pyawsopstoolkit.models.iam.user import AccessKey


class TestAccessKey(unittest.TestCase):
    """Unit test cases for AccessKey."""

    def setUp(self) -> None:
        self.id = 'ID'
        self.status = 'Active'
        self.created_date = datetime(2023, 5, 18)
        self.last_date = datetime(2023, 6, 18)
        self.last_service = 'ec2.amazonaws.com'
        self.last_region = 'eu-west-1'
        self.access_key = AccessKey(self.id, self.status)
        self.access_key_with_date = AccessKey(self.id, self.status, created_date=self.created_date)
        self.access_key_with_last_date = AccessKey(self.id, self.status, last_used_date=self.last_date)
        self.access_key_with_last_service = AccessKey(self.id, self.status, last_used_service=self.last_service)
        self.access_key_with_last_region = AccessKey(self.id, self.status, last_used_region=self.last_region)
        self.access_key_full = AccessKey(
            self.id, self.status, self.created_date, self.last_date, self.last_service, self.last_region
        )

    def test_initialization(self):
        self.assertEqual(self.access_key.id, self.id)
        self.assertEqual(self.access_key.status, self.status)
        self.assertIsNone(self.access_key.created_date)
        self.assertIsNone(self.access_key.last_used_date)
        self.assertIsNone(self.access_key.last_used_service)
        self.assertIsNone(self.access_key.last_used_region)

    def test_initialization_with_date(self):
        self.assertEqual(self.access_key_with_date.id, self.id)
        self.assertEqual(self.access_key_with_date.status, self.status)
        self.assertEqual(self.access_key_with_date.created_date, self.created_date)
        self.assertIsNone(self.access_key_with_date.last_used_date)
        self.assertIsNone(self.access_key_with_date.last_used_service)
        self.assertIsNone(self.access_key_with_date.last_used_region)

    def test_initialization_with_last_date(self):
        self.assertEqual(self.access_key_with_last_date.id, self.id)
        self.assertEqual(self.access_key_with_last_date.status, self.status)
        self.assertIsNone(self.access_key_with_last_date.created_date)
        self.assertEqual(self.access_key_with_last_date.last_used_date, self.last_date)
        self.assertIsNone(self.access_key_with_last_date.last_used_service)
        self.assertIsNone(self.access_key_with_last_date.last_used_region)

    def test_initialization_with_last_service(self):
        self.assertEqual(self.access_key_with_last_service.id, self.id)
        self.assertEqual(self.access_key_with_last_service.status, self.status)
        self.assertIsNone(self.access_key_with_last_service.created_date)
        self.assertIsNone(self.access_key_with_last_service.last_used_date)
        self.assertEqual(self.access_key_with_last_service.last_used_service, self.last_service)
        self.assertIsNone(self.access_key_with_last_service.last_used_region)

    def test_initialization_with_last_region(self):
        self.assertEqual(self.access_key_with_last_region.id, self.id)
        self.assertEqual(self.access_key_with_last_region.status, self.status)
        self.assertIsNone(self.access_key_with_last_region.created_date)
        self.assertIsNone(self.access_key_with_last_region.last_used_date)
        self.assertIsNone(self.access_key_with_last_region.last_used_service)
        self.assertEqual(self.access_key_with_last_region.last_used_region, self.last_region)

    def test_initialization_full(self):
        self.assertEqual(self.access_key_full.id, self.id)
        self.assertEqual(self.access_key_full.status, self.status)
        self.assertEqual(self.access_key_full.created_date, self.created_date)
        self.assertEqual(self.access_key_full.last_used_date, self.last_date)
        self.assertEqual(self.access_key_full.last_used_service, self.last_service)
        self.assertEqual(self.access_key_full.last_used_region, self.last_region)

    def test_set_id(self):
        new_id = 'NEW_ID'
        self.access_key_full.id = new_id
        self.assertEqual(self.access_key_full.id, new_id)

    def test_set_status(self):
        new_status = 'Inactive'
        self.access_key_full.status = new_status
        self.assertEqual(self.access_key_full.status, new_status)

    def test_set_created_date(self):
        new_date = datetime.today()
        self.access_key_full.created_date = new_date
        self.assertEqual(self.access_key_full.created_date, new_date)

    def test_set_last_used_date(self):
        new_date = datetime.today()
        self.access_key_full.last_used_date = new_date
        self.assertEqual(self.access_key_full.last_used_date, new_date)

    def test_set_last_used_service(self):
        new_service = 'ssm.amazonaws.com'
        self.access_key_full.last_used_service = new_service
        self.assertEqual(self.access_key_full.last_used_service, new_service)

    def test_set_last_used_region(self):
        new_region = 'eu-central-1'
        self.access_key_full.last_used_region = new_region
        self.assertEqual(self.access_key_full.last_used_region, new_region)

    def test_str(self):
        expected_str = (
            f'AccessKey('
            f'id="{self.id}",'
            f'status="{self.status}",'
            f'created_date={self.created_date.isoformat()},'
            f'last_used_date={self.last_date.isoformat()},'
            f'last_used_service="{self.last_service}",'
            f'last_used_region="{self.last_region}"'
            f')'
        )
        self.assertEqual(str(self.access_key_full), expected_str)

    def test_to_dict(self):
        expected_dict = {
            "id": self.id,
            "status": self.status,
            "created_date": self.created_date.isoformat(),
            "last_used_date": self.last_date.isoformat(),
            "last_used_service": self.last_service,
            "last_used_region": self.last_region
        }
        self.assertDictEqual(self.access_key_full.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
