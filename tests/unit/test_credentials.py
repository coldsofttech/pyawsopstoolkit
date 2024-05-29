import unittest
from datetime import datetime

from pyawsopstoolkit import Credentials


class TestCredentials(unittest.TestCase):
    """Unit test cases for Credentials."""

    def setUp(self) -> None:
        self.access_key = "valid_access_key"
        self.secret_access_key = "valid_secret_access_key"
        self.token = "valid_token"
        self.expiry = datetime(2023, 5, 18)
        self.creds = Credentials(self.access_key, self.secret_access_key)
        self.creds_with_token = Credentials(self.access_key, self.secret_access_key, self.token)
        self.creds_with_expiry = Credentials(self.access_key, self.secret_access_key, expiry=self.expiry)
        self.creds_full = Credentials(self.access_key, self.secret_access_key, self.token, self.expiry)

    def test_initialization(self):
        self.assertEqual(self.creds.access_key, self.access_key)
        self.assertEqual(self.creds.secret_access_key, self.secret_access_key)
        self.assertIsNone(self.creds.token)
        self.assertIsNone(self.creds.expiry)

    def test_initialization_with_token(self):
        self.assertEqual(self.creds_with_token.access_key, self.access_key)
        self.assertEqual(self.creds_with_token.secret_access_key, self.secret_access_key)
        self.assertEqual(self.creds_with_token.token, self.token)
        self.assertIsNone(self.creds_with_token.expiry)

    def test_initialization_with_expiry(self):
        self.assertEqual(self.creds_with_expiry.access_key, self.access_key)
        self.assertEqual(self.creds_with_expiry.secret_access_key, self.secret_access_key)
        self.assertIsNone(self.creds_with_expiry.token)
        self.assertEqual(self.creds_with_expiry.expiry, self.expiry)

    def test_initialization_full(self):
        self.assertEqual(self.creds_full.access_key, self.access_key)
        self.assertEqual(self.creds_full.secret_access_key, self.secret_access_key)
        self.assertEqual(self.creds_full.token, self.token)
        self.assertEqual(self.creds_full.expiry, self.expiry)

    def test_set_access_key(self):
        new_access_key = 'new_access_key'
        self.creds_full.access_key = new_access_key
        self.assertEqual(self.creds_full.access_key, new_access_key)

    def test_set_secret_access_key(self):
        new_secret_access_key = 'new_secret_access_key'
        self.creds_full.secret_access_key = new_secret_access_key
        self.assertEqual(self.creds_full.secret_access_key, new_secret_access_key)

    def test_set_token(self):
        new_token = 'new_token'
        self.creds_full.token = new_token
        self.assertEqual(self.creds_full.token, new_token)

    def test_set_expiry(self):
        new_expiry = datetime.today()
        self.creds_full.expiry = new_expiry
        self.assertEqual(self.creds_full.expiry, new_expiry)

    def test_str(self):
        expected_str = (
            f'Credentials('
            f'access_key="{self.access_key}",'
            f'secret_access_key="{self.secret_access_key}",'
            f'token="{self.token}",'
            f'expiry={self.expiry.isoformat()}'
            f')'
        )
        self.assertEqual(str(self.creds_full), expected_str)

    def test_to_dict(self):
        expected_dict = {
            "access_key": self.access_key,
            "secret_access_key": self.secret_access_key,
            "token": self.token,
            "expiry": self.expiry.isoformat()
        }
        self.assertDictEqual(self.creds_full.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
