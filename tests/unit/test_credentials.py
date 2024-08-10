import unittest
from datetime import datetime

from pyawsopstoolkit.credentials import Credentials


class TestCredentials(unittest.TestCase):
    def setUp(self) -> None:
        self.maxDiff = None
        self.params = {
            'access_key': 'valid_access_key',
            'secret_access_key': 'valid_secret_access_key',
            'token': 'valid_token',
            'expiry': datetime(2023, 5, 18)
        }
        self.creds = self.create_credentials()
        self.creds_with_token = self.create_credentials(token=self.params['token'])
        self.creds_with_expiry = self.create_credentials(expiry=self.params['expiry'])
        self.creds_full = self.create_credentials(token=self.params['token'], expiry=self.params['expiry'])

    def create_credentials(self, **kwargs):
        return Credentials(
            access_key=self.params['access_key'],
            secret_access_key=self.params['secret_access_key'],
            **kwargs
        )

    def test_initialization(self):
        self.assertEqual(self.creds.access_key, self.params['access_key'])
        self.assertEqual(self.creds.secret_access_key, self.params['secret_access_key'])
        self.assertIsNone(self.creds.token)
        self.assertIsNone(self.creds.expiry)

    def test_initialization_with_optional_params(self):
        test_cases = [
            (self.creds_with_token, self.params['token'], None),
            (self.creds_with_expiry, None, self.params['expiry']),
            (self.creds_full, self.params['token'], self.params['expiry'])
        ]
        for creds, token, expiry in test_cases:
            with self.subTest(creds=creds):
                self.assertEqual(creds.access_key, self.params['access_key'])
                self.assertEqual(creds.secret_access_key, self.params['secret_access_key'])
                self.assertEqual(creds.token, token)
                self.assertEqual(creds.expiry, expiry)

    def test_setters(self):
        new_params = {
            'access_key': 'access_key',
            'secret_access_key': 'secret_access_key',
            'token': 'token',
            'expiry': datetime.today()
        }

        self.creds_full.access_key = new_params['access_key']
        self.creds_full.secret_access_key = new_params['secret_access_key']
        self.creds_full.token = new_params['token']
        self.creds_full.expiry = new_params['expiry']

        self.assertEqual(self.creds_full.access_key, new_params['access_key'])
        self.assertEqual(self.creds_full.secret_access_key, new_params['secret_access_key'])
        self.assertEqual(self.creds_full.token, new_params['token'])
        self.assertEqual(self.creds_full.expiry, new_params['expiry'])

    def test_invalid_types(self):
        invalid_params = {
            'access_key': 123,
            'secret_access_key': 123,
            'token': 123,
            'expiry': '2024-05-06'
        }

        with self.assertRaises(TypeError):
            Credentials(
                access_key=invalid_params['access_key'],
                secret_access_key=self.params['secret_access_key']
            )
        with self.assertRaises(TypeError):
            Credentials(
                access_key=self.params['access_key'],
                secret_access_key=invalid_params['secret_access_key']
            )
        with self.assertRaises(TypeError):
            self.create_credentials(token=invalid_params['token'])
        with self.assertRaises(TypeError):
            self.create_credentials(expiry=invalid_params['expiry'])

        with self.assertRaises(TypeError):
            self.creds_full.access_key = invalid_params['access_key']
        with self.assertRaises(TypeError):
            self.creds_full.secret_access_key = invalid_params['secret_access_key']
        with self.assertRaises(TypeError):
            self.creds_full.token = invalid_params['token']
        with self.assertRaises(TypeError):
            self.creds_full.expiry = invalid_params['expiry']

    def test_to_dict(self):
        expected_dict = {
            "access_key": self.params['access_key'],
            "secret_access_key": self.params['secret_access_key'],
            "token": self.params['token'],
            "expiry": self.params['expiry'].isoformat()
        }
        self.assertDictEqual(self.creds_full.to_dict(), expected_dict)

    def test_to_dict_with_missing_fields(self):
        expected_dict = {
            "access_key": self.params['access_key'],
            "secret_access_key": self.params['secret_access_key'],
            "token": None,
            "expiry": None
        }
        self.assertDictEqual(self.creds.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
