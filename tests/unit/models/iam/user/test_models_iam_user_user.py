import unittest
from datetime import datetime

from pyawsopstoolkit import Account
from pyawsopstoolkit.models.iam import PermissionsBoundary
from pyawsopstoolkit.models.iam.user import LoginProfile, AccessKey, User


class TestUser(unittest.TestCase):
    """Unit test cases for User."""

    def setUp(self) -> None:
        self.maxDiff = None
        self.account = Account('123456789012')
        self.name = 'test_user'
        self.id = 'AID2MAB8DPLSRHEXAMPLE'
        self.arn = f'arn:aws:iam::{self.account.number}:user/{self.name}'
        self.path = '/test/'
        self.created_date = datetime(2023, 5, 18)
        self.pwd_used_date = datetime(2023, 6, 18)
        self.permissions_boundary = PermissionsBoundary(
            type='Policy',
            arn=f'arn:aws:iam::{self.account.number}:policy/ExamplePolicy'
        )
        self.login_profile = LoginProfile(
            created_date=datetime(2023, 5, 18)
        )
        self.access_keys = [
            AccessKey('ID', 'Active')
        ]
        self.tags = [
            {'Key': 'test_key', 'Value': 'test_value'}
        ]
        self.user = User(self.account, self.name, self.id, self.arn, self.path)
        self.user_with_date = User(
            self.account, self.name, self.id, self.arn, self.path, created_date=self.created_date
        )
        self.user_with_pwd_date = User(
            self.account, self.name, self.id, self.arn, self.path, password_last_used_date=self.pwd_used_date
        )
        self.user_with_permissions_boundary = User(
            self.account, self.name, self.id, self.arn, self.path, permissions_boundary=self.permissions_boundary
        )
        self.user_with_login_profile = User(
            self.account, self.name, self.id, self.arn, self.path, login_profile=self.login_profile
        )
        self.user_with_access_keys = User(
            self.account, self.name, self.id, self.arn, self.path, access_keys=self.access_keys
        )
        self.user_with_tags = User(
            self.account, self.name, self.id, self.arn, self.path, tags=self.tags
        )
        self.user_full = User(
            self.account, self.name, self.id, self.arn, self.path, self.created_date, self.pwd_used_date,
            self.permissions_boundary, self.login_profile, self.access_keys, self.tags
        )

    def test_initialization(self):
        self.assertEqual(self.user.account, self.account)
        self.assertEqual(self.user.name, self.name)
        self.assertEqual(self.user.id, self.id)
        self.assertEqual(self.user.arn, self.arn)
        self.assertEqual(self.user.path, self.path)
        self.assertIsNone(self.user.created_date)
        self.assertIsNone(self.user.password_last_used_date)
        self.assertIsNone(self.user.permissions_boundary)
        self.assertIsNone(self.user.login_profile)
        self.assertIsNone(self.user.access_keys)
        self.assertIsNone(self.user.tags)

    def test_initialization_with_date(self):
        self.assertEqual(self.user_with_date.account, self.account)
        self.assertEqual(self.user_with_date.name, self.name)
        self.assertEqual(self.user_with_date.id, self.id)
        self.assertEqual(self.user_with_date.arn, self.arn)
        self.assertEqual(self.user_with_date.path, self.path)
        self.assertEqual(self.user_with_date.created_date, self.created_date)
        self.assertIsNone(self.user_with_date.password_last_used_date)
        self.assertIsNone(self.user_with_date.permissions_boundary)
        self.assertIsNone(self.user_with_date.login_profile)
        self.assertIsNone(self.user_with_date.access_keys)
        self.assertIsNone(self.user_with_date.tags)

    def test_initialization_with_pwd_date(self):
        self.assertEqual(self.user_with_pwd_date.account, self.account)
        self.assertEqual(self.user_with_pwd_date.name, self.name)
        self.assertEqual(self.user_with_pwd_date.id, self.id)
        self.assertEqual(self.user_with_pwd_date.arn, self.arn)
        self.assertEqual(self.user_with_pwd_date.path, self.path)
        self.assertIsNone(self.user_with_pwd_date.created_date)
        self.assertEqual(self.user_with_pwd_date.password_last_used_date, self.pwd_used_date)
        self.assertIsNone(self.user_with_pwd_date.permissions_boundary)
        self.assertIsNone(self.user_with_pwd_date.login_profile)
        self.assertIsNone(self.user_with_pwd_date.access_keys)
        self.assertIsNone(self.user_with_pwd_date.tags)

    def test_initialization_with_permissions_boundary(self):
        self.assertEqual(self.user_with_permissions_boundary.account, self.account)
        self.assertEqual(self.user_with_permissions_boundary.name, self.name)
        self.assertEqual(self.user_with_permissions_boundary.id, self.id)
        self.assertEqual(self.user_with_permissions_boundary.arn, self.arn)
        self.assertEqual(self.user_with_permissions_boundary.path, self.path)
        self.assertIsNone(self.user_with_permissions_boundary.created_date)
        self.assertIsNone(self.user_with_permissions_boundary.password_last_used_date)
        self.assertEqual(self.user_with_permissions_boundary.permissions_boundary, self.permissions_boundary)
        self.assertIsNone(self.user_with_permissions_boundary.login_profile)
        self.assertIsNone(self.user_with_permissions_boundary.access_keys)
        self.assertIsNone(self.user_with_permissions_boundary.tags)

    def test_initialization_with_login_profile(self):
        self.assertEqual(self.user_with_login_profile.account, self.account)
        self.assertEqual(self.user_with_login_profile.name, self.name)
        self.assertEqual(self.user_with_login_profile.id, self.id)
        self.assertEqual(self.user_with_login_profile.arn, self.arn)
        self.assertEqual(self.user_with_login_profile.path, self.path)
        self.assertIsNone(self.user_with_login_profile.created_date)
        self.assertIsNone(self.user_with_login_profile.password_last_used_date)
        self.assertIsNone(self.user_with_login_profile.permissions_boundary)
        self.assertEqual(self.user_with_login_profile.login_profile, self.login_profile)
        self.assertIsNone(self.user_with_login_profile.access_keys)
        self.assertIsNone(self.user_with_login_profile.tags)

    def test_initialization_with_access_keys(self):
        self.assertEqual(self.user_with_access_keys.account, self.account)
        self.assertEqual(self.user_with_access_keys.name, self.name)
        self.assertEqual(self.user_with_access_keys.id, self.id)
        self.assertEqual(self.user_with_access_keys.arn, self.arn)
        self.assertEqual(self.user_with_access_keys.path, self.path)
        self.assertIsNone(self.user_with_access_keys.created_date)
        self.assertIsNone(self.user_with_access_keys.password_last_used_date)
        self.assertIsNone(self.user_with_access_keys.permissions_boundary)
        self.assertIsNone(self.user_with_access_keys.login_profile)
        self.assertEqual(self.user_with_access_keys.access_keys, self.access_keys)
        self.assertIsNone(self.user_with_access_keys.tags)

    def test_initialization_with_tags(self):
        self.assertEqual(self.user_with_tags.account, self.account)
        self.assertEqual(self.user_with_tags.name, self.name)
        self.assertEqual(self.user_with_tags.id, self.id)
        self.assertEqual(self.user_with_tags.arn, self.arn)
        self.assertEqual(self.user_with_tags.path, self.path)
        self.assertIsNone(self.user_with_tags.created_date)
        self.assertIsNone(self.user_with_tags.password_last_used_date)
        self.assertIsNone(self.user_with_tags.permissions_boundary)
        self.assertIsNone(self.user_with_tags.login_profile)
        self.assertIsNone(self.user_with_tags.access_keys)
        self.assertEqual(self.user_with_tags.tags, self.tags)

    def test_initialization_full(self):
        self.assertEqual(self.user_full.account, self.account)
        self.assertEqual(self.user_full.name, self.name)
        self.assertEqual(self.user_full.id, self.id)
        self.assertEqual(self.user_full.arn, self.arn)
        self.assertEqual(self.user_full.path, self.path)
        self.assertEqual(self.user_full.created_date, self.created_date)
        self.assertEqual(self.user_full.password_last_used_date, self.pwd_used_date)
        self.assertEqual(self.user_full.permissions_boundary, self.permissions_boundary)
        self.assertEqual(self.user_full.login_profile, self.login_profile)
        self.assertEqual(self.user_full.access_keys, self.access_keys)
        self.assertEqual(self.user_full.tags, self.tags)

    def test_set_account(self):
        new_account = Account('987654321012')
        self.user_full.account = new_account
        self.assertEqual(self.user_full.account, new_account)

    def test_set_name(self):
        new_name = 'test_user2'
        self.user_full.name = new_name
        self.assertEqual(self.user_full.name, new_name)

    def test_set_id(self):
        new_id = 'NEW_ID'
        self.user_full.id = new_id
        self.assertEqual(self.user_full.id, new_id)

    def test_set_arn(self):
        new_arn = 'arn:aws:iam::987654321012:user/test_user2'
        self.user_full.arn = new_arn
        self.assertEqual(self.user_full.arn, new_arn)

    def test_set_path(self):
        new_path = '/test1/'
        self.user_full.path = new_path
        self.assertEqual(self.user_full.path, new_path)

    def test_set_created_date(self):
        new_date = datetime.today()
        self.user_full.created_date = new_date
        self.assertEqual(self.user_full.created_date, new_date)

    def test_set_password_last_used_date(self):
        new_date = datetime.today()
        self.user_full.password_last_used_date = new_date
        self.assertEqual(self.user_full.password_last_used_date, new_date)

    def test_set_permissions_boundary(self):
        new_permissions_boundary = PermissionsBoundary(
            type='ManagedPolicy',
            arn='arn:aws:iam::987654321012:policy/ManagedPolicy'
        )
        self.user_full.permissions_boundary = new_permissions_boundary
        self.assertEqual(self.user_full.permissions_boundary, new_permissions_boundary)

    def test_set_login_profile(self):
        new_login_profile = LoginProfile(
            created_date=datetime.today()
        )
        self.user_full.login_profile = new_login_profile
        self.assertEqual(self.user_full.login_profile, new_login_profile)

    def test_set_access_keys(self):
        new_access_keys = [
            AccessKey('ID1', 'Active'),
            AccessKey('ID2', 'Inactive')
        ]
        self.user_full.access_keys = new_access_keys
        self.assertEqual(self.user_full.access_keys, new_access_keys)

    def test_set_tags(self):
        new_tags = [
            {'Key': 'test_key1', 'Value': 'test_value1'}
        ]
        self.user_full.tags = new_tags
        self.assertEqual(self.user_full.tags, new_tags)

    def test_str(self):
        expected_str = (
            f'User('
            f'account={self.account},'
            f'path="{self.path}",'
            f'name="{self.name}",'
            f'id="{self.id}",'
            f'arn="{self.arn}",'
            f'created_date={self.created_date.isoformat()},'
            f'password_last_used_date={self.pwd_used_date.isoformat()},'
            f'permissions_boundary={self.permissions_boundary},'
            f'login_profile={self.login_profile},'
            f'access_keys={self.access_keys},'
            f'tags={self.tags}'
            f')'
        )
        self.assertEqual(str(self.user_full), expected_str)

    def test_to_dict(self):
        expected_dict = {
            "account": self.account.to_dict(),
            "path": self.path,
            "name": self.name,
            "id": self.id,
            "arn": self.arn,
            "created_date": self.created_date.isoformat(),
            "password_last_used_date": self.pwd_used_date.isoformat(),
            "permissions_boundary": self.permissions_boundary.to_dict(),
            "login_profile": self.login_profile.to_dict(),
            "access_keys": self.access_keys,
            "tags": self.tags
        }
        self.assertDictEqual(self.user_full.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
