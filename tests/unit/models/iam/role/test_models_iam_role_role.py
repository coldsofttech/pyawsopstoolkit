import unittest
from datetime import datetime

from pyawsopstoolkit import Account
from pyawsopstoolkit.exceptions import ValidationError
from pyawsopstoolkit.models.iam import PermissionsBoundary
from pyawsopstoolkit.models.iam.role import LastUsed, Role


class TestRole(unittest.TestCase):
    """Unit test cases for Role."""

    def setUp(self) -> None:
        self.maxDiff = None
        self.params = {
            'account': Account('123456789012'),
            'name': 'test_role',
            'id': 'AID2MAB8DPLSRHEXAMPLE',
            'arn': 'arn:aws:iam::123456789012:role/test_role',
            'max_session_duration': 3600,
            'path': '/test/',
            'created_date': datetime(2023, 5, 18),
            'policy': {
                'Version': '2012-10-17',
                'Statement': {
                    'Effect': 'Allow',
                    'Principal': {'AWS': 'arn:aws:iam::123456789012:root'},
                    'Action': 'sts:AssumeRole',
                    'Resource': '*'
                }
            },
            'description': 'Role used for testing purposes',
            'permissions_boundary': PermissionsBoundary('Policy', 'arn:aws:iam::123456789012:policy/ExamplePolicy'),
            'last_used': LastUsed(datetime(2023, 6, 18), 'eu-west-1'),
            'tags': [{'Key': 'test_key', 'Value': 'test_value'}]
        }
        self.role = self.create_role()
        self.role_with_path = self.create_role(path=self.params['path'])
        self.role_with_date = self.create_role(created_date=self.params['created_date'])
        self.role_with_policy = self.create_role(assume_role_policy_document=self.params['policy'])
        self.role_with_desc = self.create_role(description=self.params['description'])
        self.role_with_permissions_boundary = self.create_role(permissions_boundary=self.params['permissions_boundary'])
        self.role_with_last_used = self.create_role(last_used=self.params['last_used'])
        self.role_with_tags = self.create_role(tags=self.params['tags'])
        self.role_full = self.create_role(
            path=self.params['path'],
            created_date=self.params['created_date'],
            assume_role_policy_document=self.params['policy'],
            description=self.params['description'],
            permissions_boundary=self.params['permissions_boundary'],
            last_used=self.params['last_used'],
            tags=self.params['tags']
        )

    def create_role(self, **kwargs):
        return Role(
            account=self.params['account'],
            name=self.params['name'],
            id=self.params['id'],
            arn=self.params['arn'],
            max_session_duration=self.params['max_session_duration'],
            **kwargs
        )

    def test_initialization(self):
        self.assertEqual(self.role.account, self.params['account'])
        self.assertEqual(self.role.name, self.params['name'])
        self.assertEqual(self.role.id, self.params['id'])
        self.assertEqual(self.role.arn, self.params['arn'])
        self.assertEqual(self.role.max_session_duration, self.params['max_session_duration'])
        self.assertEqual(self.role.path, '/')
        self.assertIsNone(self.role.created_date)
        self.assertIsNone(self.role.assume_role_policy_document)
        self.assertIsNone(self.role.description)
        self.assertIsNone(self.role.permissions_boundary)
        self.assertIsNone(self.role.last_used)
        self.assertIsNone(self.role.tags)

    def test_initialization_with_optional_params(self):
        test_cases = [
            (self.role_with_path, self.params['path'], None, None, None, None, None, None),
            (self.role_with_date, '/', self.params['created_date'], None, None, None, None, None),
            (self.role_with_policy, '/', None, self.params['policy'], None, None, None, None),
            (self.role_with_desc, '/', None, None, self.params['description'], None, None, None),
            (
                self.role_with_permissions_boundary,
                '/', None, None, None, self.params['permissions_boundary'], None, None
            ),
            (self.role_with_last_used, '/', None, None, None, None, self.params['last_used'], None),
            (self.role_with_tags, '/', None, None, None, None, None, self.params['tags']),
            (
                self.role_full,
                self.params['path'],
                self.params['created_date'],
                self.params['policy'],
                self.params['description'],
                self.params['permissions_boundary'],
                self.params['last_used'],
                self.params['tags']
            )
        ]
        for role, path, created_date, policy, description, boundary, last_used, tags in test_cases:
            with self.subTest(role=role):
                self.assertEqual(role.account, self.params['account'])
                self.assertEqual(role.name, self.params['name'])
                self.assertEqual(role.id, self.params['id'])
                self.assertEqual(role.arn, self.params['arn'])
                self.assertEqual(role.max_session_duration, self.params['max_session_duration'])
                self.assertEqual(role.path, path)
                self.assertEqual(role.created_date, created_date)
                self.assertEqual(role.assume_role_policy_document, policy)
                self.assertEqual(role.description, description)
                self.assertEqual(role.permissions_boundary, boundary)
                self.assertEqual(role.last_used, last_used)
                self.assertEqual(role.tags, tags)

    def test_setters(self):
        new_params = {
            'account': Account('987654321012'),
            'name': 'test_role1',
            'id': 'AID2MAB8DPLSRHEXAMPL1',
            'arn': 'arn:aws:iam::987654321012:role/test_role1',
            'max_session_duration': 4800,
            'path': '/test_app/',
            'created_date': datetime(2024, 5, 18),
            'policy': {
                'Version': '2012-10-17',
                'Statement': {
                    'Effect': 'Allow',
                    'Principal': {'AWS': 'arn:aws:iam::987654321012:root'},
                    'Action': 'sts:AssumeRole',
                    'Resource': '*'
                }
            },
            'description': 'Role used for test purposes',
            'permissions_boundary': PermissionsBoundary(
                'ManagedPolicy', 'arn:aws:iam::987654321012:policy/ExamplePolicy'
            ),
            'last_used': LastUsed(datetime(2024, 6, 18), 'us-east-2'),
            'tags': [{'Key': 'test_key1', 'Value': 'test_value1'}]
        }

        self.role_full.account = new_params['account']
        self.role_full.name = new_params['name']
        self.role_full.id = new_params['id']
        self.role_full.arn = new_params['arn']
        self.role_full.max_session_duration = new_params['max_session_duration']
        self.role_full.path = new_params['path']
        self.role_full.created_date = new_params['created_date']
        self.role_full.assume_role_policy_document = new_params['policy']
        self.role_full.description = new_params['description']
        self.role_full.permissions_boundary = new_params['permissions_boundary']
        self.role_full.last_used = new_params['last_used']
        self.role_full.tags = new_params['tags']

        self.assertEqual(self.role_full.account, new_params['account'])
        self.assertEqual(self.role_full.name, new_params['name'])
        self.assertEqual(self.role_full.id, new_params['id'])
        self.assertEqual(self.role_full.arn, new_params['arn'])
        self.assertEqual(self.role_full.max_session_duration, new_params['max_session_duration'])
        self.assertEqual(self.role_full.path, new_params['path'])
        self.assertEqual(self.role_full.created_date, new_params['created_date'])
        self.assertEqual(self.role_full.assume_role_policy_document, new_params['policy'])
        self.assertEqual(self.role_full.description, new_params['description'])
        self.assertEqual(self.role_full.permissions_boundary, new_params['permissions_boundary'])
        self.assertEqual(self.role_full.last_used, new_params['last_used'])
        self.assertEqual(self.role_full.tags, new_params['tags'])

    def test_invalid_types(self):
        invalid_params = {
            'account': '123456789012',
            'name': 123,
            'id': 123,
            'arn': 'invalid-arn',
            'max_session_duration': '6hours',
            'path': 123,
            'created_date': '2024-05-06',
            'policy': '*',
            'description': 123,
            'permissions_boundary': 'arn:aws:iam::987654321012:policy/ExamplePolicy',
            'last_used': '2024-05-06',
            'tags': 'tag_key=tag_value'
        }

        with self.assertRaises(TypeError):
            Role(
                account=invalid_params['account'],
                name=self.params['name'],
                id=self.params['id'],
                arn=self.params['arn'],
                max_session_duration=self.params['max_session_duration']
            )
        with self.assertRaises(TypeError):
            Role(
                account=self.params['account'],
                name=invalid_params['name'],
                id=self.params['id'],
                arn=self.params['arn'],
                max_session_duration=self.params['max_session_duration']
            )
        with self.assertRaises(TypeError):
            Role(
                account=self.params['account'],
                name=self.params['name'],
                id=invalid_params['id'],
                arn=self.params['arn'],
                max_session_duration=self.params['max_session_duration']
            )
        with self.assertRaises(ValidationError):
            Role(
                account=self.params['account'],
                name=self.params['name'],
                id=self.params['id'],
                arn=invalid_params['arn'],
                max_session_duration=self.params['max_session_duration']
            )
        with self.assertRaises(TypeError):
            Role(
                account=self.params['account'],
                name=self.params['name'],
                id=self.params['id'],
                arn=self.params['arn'],
                max_session_duration=invalid_params['max_session_duration']
            )
        with self.assertRaises(TypeError):
            Role(
                account=self.params['account'],
                name=self.params['name'],
                id=self.params['id'],
                arn=self.params['arn'],
                max_session_duration=self.params['max_session_duration'],
                path=invalid_params['path']
            )
        with self.assertRaises(TypeError):
            Role(
                account=self.params['account'],
                name=self.params['name'],
                id=self.params['id'],
                arn=self.params['arn'],
                max_session_duration=self.params['max_session_duration'],
                created_date=invalid_params['created_date']
            )
        with self.assertRaises(TypeError):
            Role(
                account=self.params['account'],
                name=self.params['name'],
                id=self.params['id'],
                arn=self.params['arn'],
                max_session_duration=self.params['max_session_duration'],
                assume_role_policy_document=invalid_params['policy']
            )
        with self.assertRaises(TypeError):
            Role(
                account=self.params['account'],
                name=self.params['name'],
                id=self.params['id'],
                arn=self.params['arn'],
                max_session_duration=self.params['max_session_duration'],
                description=invalid_params['description']
            )
        with self.assertRaises(TypeError):
            Role(
                account=self.params['account'],
                name=self.params['name'],
                id=self.params['id'],
                arn=self.params['arn'],
                max_session_duration=self.params['max_session_duration'],
                permissions_boundary=invalid_params['permissions_boundary']
            )
        with self.assertRaises(TypeError):
            Role(
                account=self.params['account'],
                name=self.params['name'],
                id=self.params['id'],
                arn=self.params['arn'],
                max_session_duration=self.params['max_session_duration'],
                last_used=invalid_params['last_used']
            )
        with self.assertRaises(TypeError):
            Role(
                account=self.params['account'],
                name=self.params['name'],
                id=self.params['id'],
                arn=self.params['arn'],
                max_session_duration=self.params['max_session_duration'],
                tags=invalid_params['tags']
            )

        with self.assertRaises(TypeError):
            self.role_full.account = invalid_params['account']
        with self.assertRaises(TypeError):
            self.role_full.name = invalid_params['name']
        with self.assertRaises(TypeError):
            self.role_full.id = invalid_params['id']
        with self.assertRaises(ValidationError):
            self.role_full.arn = invalid_params['arn']
        with self.assertRaises(TypeError):
            self.role_full.max_session_duration = invalid_params['max_session_duration']
        with self.assertRaises(TypeError):
            self.role_full.path = invalid_params['path']
        with self.assertRaises(TypeError):
            self.role_full.created_date = invalid_params['created_date']
        with self.assertRaises(TypeError):
            self.role_full.assume_role_policy_document = invalid_params['policy']
        with self.assertRaises(TypeError):
            self.role_full.description = invalid_params['description']
        with self.assertRaises(TypeError):
            self.role_full.permissions_boundary = invalid_params['permissions_boundary']
        with self.assertRaises(TypeError):
            self.role_full.last_used = invalid_params['last_used']
        with self.assertRaises(TypeError):
            self.role_full.tags = invalid_params['tags']

    def test_to_dict(self):
        expected_dict = {
            "account": self.params['account'].to_dict(),
            "path": self.params['path'],
            "name": self.params['name'],
            "id": self.params['id'],
            "arn": self.params['arn'],
            "created_date": self.params['created_date'].isoformat(),
            "assume_role_policy_document": self.params['policy'],
            "description": self.params['description'],
            "max_session_duration": self.params['max_session_duration'],
            "permissions_boundary": self.params['permissions_boundary'].to_dict(),
            "last_used": self.params['last_used'].to_dict(),
            "tags": self.params['tags']
        }
        self.assertDictEqual(self.role_full.to_dict(), expected_dict)

    def test_to_dict_with_missing_fields(self):
        expected_dict = {
            "account": self.params['account'].to_dict(),
            "path": "/",
            "name": self.params['name'],
            "id": self.params['id'],
            "arn": self.params['arn'],
            "created_date": None,
            "assume_role_policy_document": None,
            "description": None,
            "max_session_duration": self.params['max_session_duration'],
            "permissions_boundary": None,
            "last_used": None,
            "tags": None
        }
        self.assertDictEqual(self.role.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
