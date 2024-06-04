import unittest
from datetime import datetime

from pyawsopstoolkit import Account
from pyawsopstoolkit.exceptions import ValidationError
from pyawsopstoolkit.models.iam import PermissionsBoundary
from pyawsopstoolkit.models.iam.user import LoginProfile, AccessKey, User


class TestUser(unittest.TestCase):
    """Unit test cases for User."""

    def setUp(self) -> None:
        self.maxDiff = None
        self.params = {
            'account': Account('123456789012'),
            'name': 'test_user',
            'id': 'AID2MAB8DPLSRHEXAMPLE',
            'arn': 'arn:aws:iam::123456789012:user/test_user',
            'path': '/test/',
            'created_date': datetime(2023, 5, 18),
            'pwd_used_date': datetime(2023, 6, 18),
            'permissions_boundary': PermissionsBoundary('Policy', 'arn:aws:iam::123456789012:policy/ExamplePolicy'),
            'login_profile': LoginProfile(datetime(2023, 5, 18)),
            'access_keys': [AccessKey('ID', 'Active')],
            'tags': [{'Key': 'test_key', 'Value': 'test_value'}]
        }
        self.user = self.create_user()
        self.user_with_path = self.create_user(path=self.params['path'])
        self.user_with_date = self.create_user(created_date=self.params['created_date'])
        self.user_with_pwd_date = self.create_user(password_last_used_date=self.params['pwd_used_date'])
        self.user_with_permissions_boundary = self.create_user(permissions_boundary=self.params['permissions_boundary'])
        self.user_with_login_profile = self.create_user(login_profile=self.params['login_profile'])
        self.user_with_access_keys = self.create_user(access_keys=self.params['access_keys'])
        self.user_with_tags = self.create_user(tags=self.params['tags'])
        self.user_full = self.create_user(
            path=self.params['path'],
            created_date=self.params['created_date'],
            password_last_used_date=self.params['pwd_used_date'],
            permissions_boundary=self.params['permissions_boundary'],
            login_profile=self.params['login_profile'],
            access_keys=self.params['access_keys'],
            tags=self.params['tags']
        )

    def create_user(self, **kwargs):
        return User(
            account=self.params['account'],
            name=self.params['name'],
            id=self.params['id'],
            arn=self.params['arn'],
            **kwargs
        )

    def test_initialization(self):
        self.assertEqual(self.user.account, self.params['account'])
        self.assertEqual(self.user.name, self.params['name'])
        self.assertEqual(self.user.id, self.params['id'])
        self.assertEqual(self.user.arn, self.params['arn'])
        self.assertEqual(self.user.path, '/')
        self.assertIsNone(self.user.created_date)
        self.assertIsNone(self.user.password_last_used_date)
        self.assertIsNone(self.user.permissions_boundary)
        self.assertIsNone(self.user.login_profile)
        self.assertIsNone(self.user.access_keys)
        self.assertIsNone(self.user.tags)

    def test_initialization_with_optional_params(self):
        test_cases = [
            (self.user_with_path, self.params['path'], None, None, None, None, None, None),
            (self.user_with_date, '/', self.params['created_date'], None, None, None, None, None),
            (self.user_with_pwd_date, '/', None, self.params['pwd_used_date'], None, None, None, None),
            (
                self.user_with_permissions_boundary,
                '/', None, None, self.params['permissions_boundary'], None, None, None
            ),
            (self.user_with_login_profile, '/', None, None, None, self.params['login_profile'], None, None),
            (self.user_with_access_keys, '/', None, None, None, None, self.params['access_keys'], None),
            (self.user_with_tags, '/', None, None, None, None, None, self.params['tags']),
            (
                self.user_full,
                self.params['path'],
                self.params['created_date'],
                self.params['pwd_used_date'],
                self.params['permissions_boundary'],
                self.params['login_profile'],
                self.params['access_keys'],
                self.params['tags']
            )
        ]
        for user, path, created_date, pwd_used_date, boundary, login_profile, access_keys, tags in test_cases:
            with self.subTest(user=user):
                self.assertEqual(user.account, self.params['account'])
                self.assertEqual(user.name, self.params['name'])
                self.assertEqual(user.id, self.params['id'])
                self.assertEqual(user.arn, self.params['arn'])
                self.assertEqual(user.path, path)
                self.assertEqual(user.created_date, created_date)
                self.assertEqual(user.password_last_used_date, pwd_used_date)
                self.assertEqual(user.permissions_boundary, boundary)
                self.assertEqual(user.login_profile, login_profile)
                self.assertEqual(user.access_keys, access_keys)
                self.assertEqual(user.tags, tags)

    def test_setters(self):
        new_params = {
            'account': Account('987654321012'),
            'name': 'test_user2',
            'id': 'AID2MAB8DPLSRHEXAMPL1',
            'arn': 'arn:aws:iam::987654321012:user/test_user2',
            'path': '/test_app/',
            'created_date': datetime(2024, 5, 18),
            'pwd_used_date': datetime(2024, 6, 18),
            'permissions_boundary': PermissionsBoundary(
                'ManagedPolicy', 'arn:aws:iam::987654321012:policy/ExamplePolicy'
            ),
            'login_profile': LoginProfile(datetime(2024, 5, 18)),
            'access_keys': [AccessKey('ID1', 'Inactive')],
            'tags': [{'Key': 'test_key1', 'Value': 'test_value1'}]
        }

        self.user_full.account = new_params['account']
        self.user_full.name = new_params['name']
        self.user_full.id = new_params['id']
        self.user_full.arn = new_params['arn']
        self.user_full.path = new_params['path']
        self.user_full.created_date = new_params['created_date']
        self.user_full.password_last_used_date = new_params['pwd_used_date']
        self.user_full.permissions_boundary = new_params['permissions_boundary']
        self.user_full.login_profile = new_params['login_profile']
        self.user_full.access_keys = new_params['access_keys']
        self.user_full.tags = new_params['tags']

        self.assertEqual(self.user_full.account, new_params['account'])
        self.assertEqual(self.user_full.name, new_params['name'])
        self.assertEqual(self.user_full.id, new_params['id'])
        self.assertEqual(self.user_full.arn, new_params['arn'])
        self.assertEqual(self.user_full.path, new_params['path'])
        self.assertEqual(self.user_full.created_date, new_params['created_date'])
        self.assertEqual(self.user_full.password_last_used_date, new_params['pwd_used_date'])
        self.assertEqual(self.user_full.permissions_boundary, new_params['permissions_boundary'])
        self.assertEqual(self.user_full.login_profile, new_params['login_profile'])
        self.assertEqual(self.user_full.access_keys, new_params['access_keys'])
        self.assertEqual(self.user_full.tags, new_params['tags'])

    def test_invalid_types(self):
        invalid_params = {
            'account': '123456789012',
            'name': 123,
            'id': 123,
            'arn': 'ivnalid-arn',
            'path': 123,
            'created_date': '2024-05-06',
            'pwd_used_date': '2024-05-06',
            'permissions_boundary': 'arn:aws:iam::123456789012:policy/ExamplePolicy',
            'login_profile': 'login_profile',
            'access_keys': [123],
            'tags': 'tag_key=tag_value'
        }

        with self.assertRaises(TypeError):
            User(
                account=invalid_params['account'],
                name=self.params['name'],
                id=self.params['id'],
                arn=self.params['arn']
            )
        with self.assertRaises(TypeError):
            User(
                account=self.params['account'],
                name=invalid_params['name'],
                id=self.params['id'],
                arn=self.params['arn']
            )
        with self.assertRaises(TypeError):
            User(
                account=self.params['account'],
                name=self.params['name'],
                id=invalid_params['id'],
                arn=self.params['arn']
            )
        with self.assertRaises(ValidationError):
            User(
                account=self.params['account'],
                name=self.params['name'],
                id=self.params['id'],
                arn=invalid_params['arn']
            )
        with self.assertRaises(TypeError):
            User(
                account=self.params['account'],
                name=self.params['name'],
                id=self.params['id'],
                arn=self.params['arn'],
                path=invalid_params['path']
            )
        with self.assertRaises(TypeError):
            User(
                account=self.params['account'],
                name=self.params['name'],
                id=self.params['id'],
                arn=self.params['arn'],
                created_date=invalid_params['created_date']
            )
        with self.assertRaises(TypeError):
            User(
                account=self.params['account'],
                name=self.params['name'],
                id=self.params['id'],
                arn=self.params['arn'],
                password_last_used_date=invalid_params['pwd_used_date']
            )
        with self.assertRaises(TypeError):
            User(
                account=self.params['account'],
                name=self.params['name'],
                id=self.params['id'],
                arn=self.params['arn'],
                permissions_boundary=invalid_params['permissions_boundary']
            )
        with self.assertRaises(TypeError):
            User(
                account=self.params['account'],
                name=self.params['name'],
                id=self.params['id'],
                arn=self.params['arn'],
                login_profile=invalid_params['login_profile']
            )
        with self.assertRaises(TypeError):
            User(
                account=self.params['account'],
                name=self.params['name'],
                id=self.params['id'],
                arn=self.params['arn'],
                access_keys=invalid_params['access_keys']
            )
        with self.assertRaises(TypeError):
            User(
                account=self.params['account'],
                name=self.params['name'],
                id=self.params['id'],
                arn=self.params['arn'],
                tags=invalid_params['tags']
            )

        with self.assertRaises(TypeError):
            self.user_full.account = invalid_params['account']
        with self.assertRaises(TypeError):
            self.user_full.name = invalid_params['name']
        with self.assertRaises(TypeError):
            self.user_full.id = invalid_params['id']
        with self.assertRaises(ValidationError):
            self.user_full.arn = invalid_params['arn']
        with self.assertRaises(TypeError):
            self.user_full.path = invalid_params['path']
        with self.assertRaises(TypeError):
            self.user_full.created_date = invalid_params['created_date']
        with self.assertRaises(TypeError):
            self.user_full.password_last_used_date = invalid_params['pwd_used_date']
        with self.assertRaises(TypeError):
            self.user_full.permissions_boundary = invalid_params['permissions_boundary']
        with self.assertRaises(TypeError):
            self.user_full.login_profile = invalid_params['login_profile']
        with self.assertRaises(TypeError):
            self.user_full.access_keys = invalid_params['access_keys']
        with self.assertRaises(TypeError):
            self.user_full.tags = invalid_params['tags']

    def test_to_dict(self):
        expected_dict = {
            "account": self.params['account'].to_dict(),
            "path": self.params['path'],
            "name": self.params['name'],
            "id": self.params['id'],
            "arn": self.params['arn'],
            "created_date": self.params['created_date'].isoformat(),
            "password_last_used_date": self.params['pwd_used_date'].isoformat(),
            "permissions_boundary": self.params['permissions_boundary'].to_dict(),
            "login_profile": self.params['login_profile'].to_dict(),
            "access_keys": [key.to_dict() for key in self.params['access_keys']],
            "tags": self.params['tags']
        }
        self.assertDictEqual(self.user_full.to_dict(), expected_dict)

    def test_to_dict_with_missing_fields(self):
        expected_dict = {
            "account": self.params['account'].to_dict(),
            "path": "/",
            "name": self.params['name'],
            "id": self.params['id'],
            "arn": self.params['arn'],
            "created_date": None,
            "password_last_used_date": None,
            "permissions_boundary": None,
            "login_profile": None,
            "access_keys": None,
            "tags": None
        }
        self.assertDictEqual(self.user.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
