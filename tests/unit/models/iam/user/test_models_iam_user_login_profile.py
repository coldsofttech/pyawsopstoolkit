import unittest
from datetime import datetime

from pyawsopstoolkit.models.iam.user import LoginProfile


class TestLoginProfile(unittest.TestCase):
    """Unit test cases for LoginProfile."""

    def setUp(self) -> None:
        self.created_date = datetime(2023, 5, 18)
        self.pwd_reset = True
        self.login_profile_empty = LoginProfile()
        self.login_profile_with_date = LoginProfile(created_date=self.created_date)
        self.login_profile_with_pwd_reset = LoginProfile(password_reset_required=self.pwd_reset)
        self.login_profile = LoginProfile(self.created_date, self.pwd_reset)

    def test_initialization_empty(self):
        self.assertIsNone(self.login_profile_empty.created_date)
        self.assertFalse(self.login_profile_empty.password_reset_required)

    def test_initialization_with_date(self):
        self.assertEqual(self.login_profile_with_date.created_date, self.created_date)
        self.assertFalse(self.login_profile_empty.password_reset_required)

    def test_initialization_with_pwd_reset(self):
        self.assertIsNone(self.login_profile_with_pwd_reset.created_date)
        self.assertTrue(self.login_profile_with_pwd_reset.password_reset_required)

    def test_initialization(self):
        self.assertEqual(self.login_profile.created_date, self.created_date)
        self.assertTrue(self.login_profile.password_reset_required)

    def test_set_created_date(self):
        new_date = datetime.today()
        self.login_profile.created_date = new_date
        self.assertEqual(self.login_profile.created_date, new_date)

    def test_set_password_reset_required(self):
        self.login_profile.password_reset_required = False
        self.assertFalse(self.login_profile.password_reset_required)

    def test_str(self):
        expected_str = (
            f'LoginProfile('
            f'created_date={self.created_date.isoformat()},'
            f'password_reset_required={self.pwd_reset}'
            f')'
        )
        self.assertEqual(str(self.login_profile), expected_str)

    def test_to_dict(self):
        expected_dict = {
            "created_date": self.created_date.isoformat(),
            "password_reset_required": self.pwd_reset
        }
        self.assertDictEqual(self.login_profile.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
