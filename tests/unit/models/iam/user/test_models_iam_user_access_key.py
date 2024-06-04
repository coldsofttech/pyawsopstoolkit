import unittest
from datetime import datetime

from pyawsopstoolkit.exceptions import ValidationError
from pyawsopstoolkit.models.iam.user import AccessKey


class TestAccessKey(unittest.TestCase):
    """Unit test cases for AccessKey."""

    def setUp(self) -> None:
        self.maxDiff = None
        self.params = {
            'id': 'ID',
            'status': 'Active',
            'created_date': datetime(2023, 5, 18),
            'last_date': datetime(2023, 6, 18),
            'last_service': 'ec2.amazonaws.com',
            'last_region': 'eu-west-1'
        }
        self.access_key = self.create_access_key()
        self.access_key_with_date = self.create_access_key(created_date=self.params['created_date'])
        self.access_key_with_last_date = self.create_access_key(last_used_date=self.params['last_date'])
        self.access_key_with_last_service = self.create_access_key(last_used_service=self.params['last_service'])
        self.access_key_with_last_region = self.create_access_key(last_used_region=self.params['last_region'])
        self.access_key_full = self.create_access_key(
            created_date=self.params['created_date'],
            last_used_date=self.params['last_date'],
            last_used_service=self.params['last_service'],
            last_used_region=self.params['last_region']
        )

    def create_access_key(self, **kwargs):
        return AccessKey(self.params['id'], self.params['status'], **kwargs)

    def test_initialization(self):
        self.assertEqual(self.access_key.id, self.params['id'])
        self.assertEqual(self.access_key.status, self.params['status'])
        self.assertIsNone(self.access_key.created_date)
        self.assertIsNone(self.access_key.last_used_date)
        self.assertIsNone(self.access_key.last_used_service)
        self.assertIsNone(self.access_key.last_used_region)

    def test_initialization_empty(self):
        with self.assertRaises(TypeError):
            AccessKey()

    def test_initialization_with_optional_params(self):
        test_cases = [
            (self.access_key_with_date, self.params['created_date'], None, None, None),
            (self.access_key_with_last_date, None, self.params['last_date'], None, None),
            (self.access_key_with_last_service, None, None, self.params['last_service'], None),
            (self.access_key_with_last_region, None, None, None, self.params['last_region']),
            (
                self.access_key_full, self.params['created_date'], self.params['last_date'],
                self.params['last_service'], self.params['last_region']
            )
        ]
        for access_key, created_date, last_date, last_service, last_region in test_cases:
            with self.subTest(access_key=access_key):
                self.assertEqual(access_key.id, self.params['id'])
                self.assertEqual(access_key.status, self.params['status'])
                self.assertEqual(access_key.created_date, created_date)
                self.assertEqual(access_key.last_used_date, last_date)
                self.assertEqual(access_key.last_used_service, last_service)
                self.assertEqual(access_key.last_used_region, last_region)

    def test_setters(self):
        new_params = {
            'id': 'ID1',
            'status': 'Inactive',
            'created_date': datetime.today(),
            'last_date': datetime.today(),
            'last_service': 'ssm.amazonaws.com',
            'last_region': 'us-east-2'
        }

        self.access_key_full.id = new_params['id']
        self.access_key_full.status = new_params['status']
        self.access_key_full.created_date = new_params['created_date']
        self.access_key_full.last_used_date = new_params['last_date']
        self.access_key_full.last_used_service = new_params['last_service']
        self.access_key_full.last_used_region = new_params['last_region']

        self.assertEqual(self.access_key_full.id, new_params['id'])
        self.assertEqual(self.access_key_full.status, new_params['status'])
        self.assertEqual(self.access_key_full.created_date, new_params['created_date'])
        self.assertEqual(self.access_key_full.last_used_date, new_params['last_date'])
        self.assertEqual(self.access_key_full.last_used_service, new_params['last_service'])
        self.assertEqual(self.access_key_full.last_used_region, new_params['last_region'])

    def test_invalid_types(self):
        invalid_params = {
            'id': 123,
            'status': 123,
            'created_date': '2023-02-06',
            'last_date': '2023-04-05',
            'last_service': 123,
            'last_region': 'Ohio'
        }

        with self.assertRaises(TypeError):
            AccessKey(invalid_params['id'], self.params['status'])
        with self.assertRaises(TypeError):
            AccessKey(self.params['id'], invalid_params['status'])
        with self.assertRaises(TypeError):
            self.create_access_key(created_date=invalid_params['created_date'])
        with self.assertRaises(TypeError):
            self.create_access_key(last_used_date=invalid_params['last_date'])
        with self.assertRaises(TypeError):
            self.create_access_key(last_used_service=invalid_params['last_service'])
        with self.assertRaises(ValidationError):
            self.create_access_key(last_used_region=invalid_params['last_region'])

        with self.assertRaises(TypeError):
            self.access_key_full.id = invalid_params['id']
        with self.assertRaises(TypeError):
            self.access_key_full.status = invalid_params['status']
        with self.assertRaises(TypeError):
            self.access_key_full.created_date = invalid_params['created_date']
        with self.assertRaises(TypeError):
            self.access_key_full.last_used_date = invalid_params['last_date']
        with self.assertRaises(TypeError):
            self.access_key_full.last_used_service = invalid_params['last_service']
        with self.assertRaises(ValidationError):
            self.access_key_full.last_used_region = invalid_params['last_region']

    def test_to_dict(self):
        expected_dict = {
            "id": self.params['id'],
            "status": self.params['status'],
            "created_date": self.params['created_date'].isoformat(),
            "last_used_date": self.params['last_date'].isoformat(),
            "last_used_service": self.params['last_service'],
            "last_used_region": self.params['last_region']
        }
        self.assertDictEqual(self.access_key_full.to_dict(), expected_dict)

    def test_to_dict_with_missing_fields(self):
        expected_dict = {
            "id": self.params['id'],
            "status": self.params['status'],
            "created_date": None,
            "last_used_date": None,
            "last_used_service": None,
            "last_used_region": None
        }
        self.assertDictEqual(self.access_key.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
