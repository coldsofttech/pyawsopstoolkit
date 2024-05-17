import unittest
from datetime import datetime

from pyawsopstoolkit import Credentials


class TestCredentials(unittest.TestCase):
    """Unit test cases for Credentials class."""

    def setUp(self) -> None:
        self.access_key = "valid_access_key"
        self.secret_access_key = "valid_secret_access_key"
        self.token = "valid_token"
        self.expiry_none = None
        self.expiry_datetime = datetime.now()
        self.creds_no_expiry = Credentials(self.access_key, self.secret_access_key, self.token)
        self.creds_with_expiry = Credentials(self.access_key, self.secret_access_key, self.token, self.expiry_datetime)

    def test_init_valid(self):
        """Test if init works as expected."""
        creds = Credentials(self.access_key, self.secret_access_key, self.token, self.expiry_datetime)

        self.assertEqual(creds._access_key, self.access_key)
        self.assertEqual(creds._secret_access_key, self.secret_access_key)
        self.assertEqual(creds._token, self.token)
        self.assertEqual(creds._expiry, self.expiry_datetime)

    def test_init_invalid(self):
        """Test if init raises exception as expected."""
        with self.assertRaises(TypeError):
            Credentials(123, self.secret_access_key, self.token, self.expiry_datetime)

    def test_init_expiry_none(self):
        """Test if init works as expected."""
        creds = Credentials(self.access_key, self.secret_access_key, self.token, self.expiry_none)

        self.assertEqual(creds._access_key, self.access_key)
        self.assertEqual(creds._secret_access_key, self.secret_access_key)
        self.assertEqual(creds._token, self.token)
        self.assertIsNone(creds._expiry)

    def test_get_access_key(self):
        """Test if access key works as expected."""
        self.assertEqual(self.creds_no_expiry.access_key, self.access_key)

    def test_set_access_key_valid(self):
        """Test if access key works as expected."""
        new_access_key = "new_access_key"
        self.creds_no_expiry.access_key = new_access_key
        self.assertEqual(self.creds_no_expiry.access_key, new_access_key)

    def test_set_access_key_invalid(self):
        """Test if access key raises exception as expected."""
        with self.assertRaises(TypeError):
            self.creds_no_expiry.access_key = 123

    def test_get_secret_access_key(self):
        """Test if secret access key works as expected."""
        self.assertEqual(self.creds_no_expiry.secret_access_key, self.secret_access_key)

    def test_set_secret_access_key_valid(self):
        """Test if secret access key works as expected."""
        new_secret_access_key = "new_secret_access_key"
        self.creds_no_expiry.secret_access_key = new_secret_access_key
        self.assertEqual(self.creds_no_expiry.secret_access_key, new_secret_access_key)

    def test_set_secret_access_key_invalid(self):
        """Test if secret access key raises exception as expected."""
        with self.assertRaises(TypeError):
            self.creds_no_expiry.secret_access_key = 123

    def test_get_token(self):
        """Test if token works as expected."""
        self.assertEqual(self.creds_no_expiry.token, self.token)

    def test_set_token_valid(self):
        """Test if token works as expected."""
        new_token = "new_token"
        self.creds_no_expiry.token = new_token
        self.assertEqual(self.creds_no_expiry.token, new_token)

    def test_set_token_invalid(self):
        """Test if token raises exception as expected."""
        with self.assertRaises(TypeError):
            self.creds_no_expiry.token = 123

    def test_get_expiry(self):
        """Test if expiry works as expected."""
        self.assertEqual(self.creds_with_expiry.expiry, self.expiry_datetime)

    def test_set_expiry_valid(self):
        """Test if expiry works as expected."""
        new_expiry = datetime.now()
        self.creds_with_expiry.expiry = new_expiry
        self.assertEqual(self.creds_with_expiry.expiry, new_expiry)

    def test_set_expiry_invalid(self):
        """Test if expiry raises exception as expected."""
        with self.assertRaises(TypeError):
            self.creds_with_expiry.expiry = 123

    def test_get_str(self):
        """Test if str works as expected."""
        expected = (
            f'Credentials('
            f'access_key="{self.creds_no_expiry.access_key}",'
            f'secret_access_key="{self.creds_no_expiry.secret_access_key}",'
            f'token="{self.creds_no_expiry.token}",'
            f'expiry={None})'
        )
        self.assertEqual(str(self.creds_no_expiry), expected)

    def test_get_str_with_expiry(self):
        """Test if str works as expected."""
        expected = (
            f'Credentials('
            f'access_key="{self.creds_with_expiry.access_key}",'
            f'secret_access_key="{self.creds_with_expiry.secret_access_key}",'
            f'token="{self.creds_with_expiry.token}",'
            f'expiry={self.creds_with_expiry.expiry.isoformat()})'
        )
        self.assertEqual(str(self.creds_with_expiry), expected)

    def test_get_dict(self):
        """Test if dict works as expected."""
        expected = {
            "access_key": self.creds_no_expiry.access_key,
            "secret_access_key": self.creds_no_expiry.secret_access_key,
            "token": self.creds_no_expiry.token,
            "expiry": None
        }
        self.assertDictEqual(self.creds_no_expiry.__dict__(), expected)

    def test_get_dict_with_expiry(self):
        """Test if dict works as expected."""
        expected = {
            "access_key": self.creds_with_expiry.access_key,
            "secret_access_key": self.creds_with_expiry.secret_access_key,
            "token": self.creds_with_expiry.token,
            "expiry": self.creds_with_expiry.expiry.isoformat()
        }
        self.assertDictEqual(self.creds_with_expiry.__dict__(), expected)


if __name__ == "__main__":
    unittest.main()
