import unittest
from datetime import datetime

from pyawsopstoolkit.models.iam.user import LoginProfile


class TestLoginProfile(unittest.TestCase):
    """Unit test cases for LoginProfile."""

    def setUp(self) -> None:
        self.maxDiff = None
        self.params = {
            'created_date': datetime(2023, 5, 18),
            'pwd_reset': True
        }
        self.login_profile_empty = self.create_login_profile()
        self.login_profile_with_date = self.create_login_profile(created_date=self.params['created_date'])
        self.login_profile_with_pwd_reset = self.create_login_profile(password_reset_required=self.params['pwd_reset'])
        self.login_profile = self.create_login_profile(
            created_date=self.params['created_date'],
            password_reset_required=self.params['pwd_reset']
        )

    @staticmethod
    def create_login_profile(**kwargs):
        return LoginProfile(**kwargs)

    def test_initialization(self):
        self.assertIsNone(self.login_profile_empty.created_date)
        self.assertFalse(self.login_profile_empty.password_reset_required)

    def test_initialization_with_optional_params(self):
        test_cases = [
            (self.login_profile_with_date, self.params['created_date'], False),
            (self.login_profile_with_pwd_reset, None, self.params['pwd_reset']),
            (self.login_profile, self.params['created_date'], self.params['pwd_reset'])
        ]
        for login_profile, created_date, pwd_reset in test_cases:
            with self.subTest(login_profile=login_profile):
                self.assertEqual(login_profile.created_date, created_date)
                self.assertEqual(login_profile.password_reset_required, pwd_reset)

    def test_setters(self):
        new_params = {
            'created_date': datetime.today(),
            'pwd_reset': False
        }

        self.login_profile.created_date = new_params['created_date']
        self.login_profile.password_reset_required = new_params['pwd_reset']

        self.assertEqual(self.login_profile.created_date, new_params['created_date'])
        self.assertEqual(self.login_profile.password_reset_required, new_params['pwd_reset'])

    def test_invalid_types(self):
        invalid_params = {
            'created_date': '2024-05-06',
            'pwd_reset': 1
        }

        with self.assertRaises(TypeError):
            LoginProfile(created_date=invalid_params['created_date'])
        with self.assertRaises(TypeError):
            LoginProfile(password_reset_required=invalid_params['pwd_reset'])

        with self.assertRaises(TypeError):
            self.login_profile.created_date = invalid_params['created_date']
        with self.assertRaises(TypeError):
            self.login_profile.password_reset_required = invalid_params['pwd_reset']

    def test_to_dict(self):
        expected_dict = {
            "created_date": self.params['created_date'].isoformat(),
            "password_reset_required": self.params['pwd_reset']
        }
        self.assertDictEqual(self.login_profile.to_dict(), expected_dict)

    def test_to_dict_with_missing_fields(self):
        expected_dict = {
            "created_date": None,
            "password_reset_required": False
        }
        self.assertDictEqual(self.login_profile_empty.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
