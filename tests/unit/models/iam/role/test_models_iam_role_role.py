import unittest
from datetime import datetime

from pyawsopstoolkit import Account
from pyawsopstoolkit.models.iam import PermissionsBoundary
from pyawsopstoolkit.models.iam.role import LastUsed, Role


class TestRole(unittest.TestCase):
    """Unit test cases for Role."""

    def setUp(self) -> None:
        self.account = Account('123456789012')
        self.name = 'test_role'
        self.id = 'AID2MAB8DPLSRHEXAMPLE'
        self.arn = f'arn:aws:iam::{self.account.number}:role/{self.name}'
        self.max_session_duration = 3600
        self.path = '/test/'
        self.created_date = datetime(2023, 5, 18)
        self.policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": f"arn:aws:iam::{self.account.number}:root"
                    },
                    "Action": "sts:AssumeRole",
                    "Resource": "*"
                }
            ]
        }
        self.description = 'role used for testing purposes'
        self.permissions_boundary = PermissionsBoundary(
            type='Policy',
            arn=f'arn:aws:iam::{self.account.number}:policy/ExamplePolicy'
        )
        self.last_used = LastUsed(
            used_date=datetime(2023, 6, 18),
            region='eu-west-1'
        )
        self.tags = [
            {'Key': 'test_key', 'Value': 'test_value'}
        ]
        self.role = Role(
            account=self.account,
            name=self.name,
            id=self.id,
            arn=self.arn,
            max_session_duration=self.max_session_duration,
            path=self.path
        )
        self.role_with_date = Role(
            account=self.account,
            name=self.name,
            id=self.id,
            arn=self.arn,
            max_session_duration=self.max_session_duration,
            path=self.path,
            created_date=self.created_date
        )
        self.role_with_policy = Role(
            account=self.account,
            name=self.name,
            id=self.id,
            arn=self.arn,
            max_session_duration=self.max_session_duration,
            path=self.path,
            assume_role_policy_document=self.policy
        )
        self.role_with_desc = Role(
            account=self.account,
            name=self.name,
            id=self.id,
            arn=self.arn,
            max_session_duration=self.max_session_duration,
            path=self.path,
            description=self.description
        )
        self.role_with_permissions_boundary = Role(
            account=self.account,
            name=self.name,
            id=self.id,
            arn=self.arn,
            max_session_duration=self.max_session_duration,
            path=self.path,
            permissions_boundary=self.permissions_boundary
        )
        self.role_with_last_used = Role(
            account=self.account,
            name=self.name,
            id=self.id,
            arn=self.arn,
            max_session_duration=self.max_session_duration,
            path=self.path,
            last_used=self.last_used
        )
        self.role_with_tags = Role(
            account=self.account,
            name=self.name,
            id=self.id,
            arn=self.arn,
            max_session_duration=self.max_session_duration,
            path=self.path,
            tags=self.tags
        )
        self.role_full = Role(
            account=self.account,
            name=self.name,
            id=self.id,
            arn=self.arn,
            max_session_duration=self.max_session_duration,
            path=self.path,
            created_date=self.created_date,
            assume_role_policy_document=self.policy,
            description=self.description,
            permissions_boundary=self.permissions_boundary,
            last_used=self.last_used,
            tags=self.tags
        )

    def test_initialization(self):
        self.assertEqual(self.role.account, self.account)
        self.assertEqual(self.role.name, self.name)
        self.assertEqual(self.role.id, self.id)
        self.assertEqual(self.role.arn, self.arn)
        self.assertEqual(self.role.max_session_duration, self.max_session_duration)
        self.assertEqual(self.role.path, self.path)
        self.assertIsNone(self.role.created_date)
        self.assertIsNone(self.role.assume_role_policy_document)
        self.assertIsNone(self.role.description)
        self.assertIsNone(self.role.permissions_boundary)
        self.assertIsNone(self.role.last_used)
        self.assertIsNone(self.role.tags)

    def test_initialization_with_date(self):
        self.assertEqual(self.role_with_date.account, self.account)
        self.assertEqual(self.role_with_date.name, self.name)
        self.assertEqual(self.role_with_date.id, self.id)
        self.assertEqual(self.role_with_date.arn, self.arn)
        self.assertEqual(self.role_with_date.max_session_duration, self.max_session_duration)
        self.assertEqual(self.role_with_date.path, self.path)
        self.assertEqual(self.role_with_date.created_date, self.created_date)
        self.assertIsNone(self.role_with_date.assume_role_policy_document)
        self.assertIsNone(self.role_with_date.description)
        self.assertIsNone(self.role_with_date.permissions_boundary)
        self.assertIsNone(self.role_with_date.last_used)
        self.assertIsNone(self.role_with_date.tags)

    def test_initialization_with_policy(self):
        self.assertEqual(self.role_with_policy.account, self.account)
        self.assertEqual(self.role_with_policy.name, self.name)
        self.assertEqual(self.role_with_policy.id, self.id)
        self.assertEqual(self.role_with_policy.arn, self.arn)
        self.assertEqual(self.role_with_policy.max_session_duration, self.max_session_duration)
        self.assertEqual(self.role_with_policy.path, self.path)
        self.assertIsNone(self.role_with_policy.created_date)
        self.assertEqual(self.role_with_policy.assume_role_policy_document, self.policy)
        self.assertIsNone(self.role_with_policy.description)
        self.assertIsNone(self.role_with_policy.permissions_boundary)
        self.assertIsNone(self.role_with_policy.last_used)
        self.assertIsNone(self.role_with_policy.tags)

    def test_initialization_with_desc(self):
        self.assertEqual(self.role_with_desc.account, self.account)
        self.assertEqual(self.role_with_desc.name, self.name)
        self.assertEqual(self.role_with_desc.id, self.id)
        self.assertEqual(self.role_with_desc.arn, self.arn)
        self.assertEqual(self.role_with_desc.max_session_duration, self.max_session_duration)
        self.assertEqual(self.role_with_desc.path, self.path)
        self.assertIsNone(self.role_with_desc.created_date)
        self.assertIsNone(self.role_with_desc.assume_role_policy_document)
        self.assertEqual(self.role_with_desc.description, self.description)
        self.assertIsNone(self.role_with_desc.permissions_boundary)
        self.assertIsNone(self.role_with_desc.last_used)
        self.assertIsNone(self.role_with_desc.tags)

    def test_initialization_with_permissions_boundary(self):
        self.assertEqual(self.role_with_permissions_boundary.account, self.account)
        self.assertEqual(self.role_with_permissions_boundary.name, self.name)
        self.assertEqual(self.role_with_permissions_boundary.id, self.id)
        self.assertEqual(self.role_with_permissions_boundary.arn, self.arn)
        self.assertEqual(self.role_with_permissions_boundary.max_session_duration, self.max_session_duration)
        self.assertEqual(self.role_with_permissions_boundary.path, self.path)
        self.assertIsNone(self.role_with_permissions_boundary.created_date)
        self.assertIsNone(self.role_with_permissions_boundary.assume_role_policy_document)
        self.assertIsNone(self.role_with_permissions_boundary.description)
        self.assertEqual(self.role_with_permissions_boundary.permissions_boundary, self.permissions_boundary)
        self.assertIsNone(self.role_with_permissions_boundary.last_used)
        self.assertIsNone(self.role_with_permissions_boundary.tags)

    def test_initialization_with_last_used(self):
        self.assertEqual(self.role_with_last_used.account, self.account)
        self.assertEqual(self.role_with_last_used.name, self.name)
        self.assertEqual(self.role_with_last_used.id, self.id)
        self.assertEqual(self.role_with_last_used.arn, self.arn)
        self.assertEqual(self.role_with_last_used.max_session_duration, self.max_session_duration)
        self.assertEqual(self.role_with_last_used.path, self.path)
        self.assertIsNone(self.role_with_last_used.created_date)
        self.assertIsNone(self.role_with_last_used.assume_role_policy_document)
        self.assertIsNone(self.role_with_last_used.description)
        self.assertIsNone(self.role_with_last_used.permissions_boundary)
        self.assertEqual(self.role_with_last_used.last_used, self.last_used)
        self.assertIsNone(self.role_with_last_used.tags)

    def test_initialization_with_tags(self):
        self.assertEqual(self.role_with_tags.account, self.account)
        self.assertEqual(self.role_with_tags.name, self.name)
        self.assertEqual(self.role_with_tags.id, self.id)
        self.assertEqual(self.role_with_tags.arn, self.arn)
        self.assertEqual(self.role_with_tags.max_session_duration, self.max_session_duration)
        self.assertEqual(self.role_with_tags.path, self.path)
        self.assertIsNone(self.role_with_tags.created_date)
        self.assertIsNone(self.role_with_tags.assume_role_policy_document)
        self.assertIsNone(self.role_with_tags.description)
        self.assertIsNone(self.role_with_tags.permissions_boundary)
        self.assertIsNone(self.role_with_tags.last_used)
        self.assertEqual(self.role_with_tags.tags, self.tags)

    def test_initialization_full(self):
        self.assertEqual(self.role_full.account, self.account)
        self.assertEqual(self.role_full.name, self.name)
        self.assertEqual(self.role_full.id, self.id)
        self.assertEqual(self.role_full.arn, self.arn)
        self.assertEqual(self.role_full.max_session_duration, self.max_session_duration)
        self.assertEqual(self.role_full.path, self.path)
        self.assertEqual(self.role_full.created_date, self.created_date)
        self.assertEqual(self.role_full.assume_role_policy_document, self.policy)
        self.assertEqual(self.role_full.description, self.description)
        self.assertEqual(self.role_full.permissions_boundary, self.permissions_boundary)
        self.assertEqual(self.role_full.last_used, self.last_used)
        self.assertEqual(self.role_full.tags, self.tags)

    def test_set_account(self):
        new_account = Account('987654321012')
        self.role_full.account = new_account
        self.assertEqual(self.role_full.account, new_account)

    def test_set_name(self):
        new_name = 'test_role1'
        self.role_full.name = new_name
        self.assertEqual(self.role_full.name, new_name)

    def test_set_id(self):
        new_id = 'ABDHJGFY'
        self.role_full.id = new_id
        self.assertEqual(self.role_full.id, new_id)

    def test_set_arn(self):
        new_arn = 'arn:aws:iam::987654321012:test_role1'
        self.role_full.arn = new_arn
        self.assertEqual(self.role_full.arn, new_arn)

    def test_set_max_session_duration(self):
        new_duration = 4800
        self.role_full.max_session_duration = new_duration
        self.assertEqual(self.role_full.max_session_duration, new_duration)

    def test_set_path(self):
        new_path = '/service-role/'
        self.role_full.path = new_path
        self.assertEqual(self.role_full.path, new_path)

    def test_set_created_date(self):
        new_date = datetime.today()
        self.role_full.created_date = new_date
        self.assertEqual(self.role_full.created_date, new_date)

    def test_set_assume_role_policy_document(self):
        new_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": "arn:aws:iam::987654321012:root"
                    },
                    "Action": "sts:AssumeRole",
                    "Resource": "*"
                }
            ]
        }
        self.role_full.assume_role_policy_document = new_policy
        self.assertDictEqual(self.role_full.assume_role_policy_document, new_policy)

    def test_set_description(self):
        new_description = 'test role desc'
        self.role_full.description = new_description
        self.assertEqual(self.role_full.description, new_description)

    def test_set_permissions_boundary(self):
        new_permissions_boundary = PermissionsBoundary(
            type='ManagedPolicy',
            arn='arn:aws:iam::987654321012:policy/ManagedPolicy'
        )
        self.role_full.permissions_boundary = new_permissions_boundary
        self.assertEqual(self.role_full.permissions_boundary, new_permissions_boundary)

    def test_set_last_used(self):
        new_date = LastUsed(
            used_date=datetime.today(),
            region='us-east-1'
        )
        self.role_full.last_used = new_date
        self.assertEqual(self.role_full.last_used, new_date)

    def test_set_tags(self):
        new_tags = [
            {'Key': 'test_key1', 'Value': 'test_value1'}
        ]
        self.role_full.tags = new_tags
        self.assertEqual(self.role_full.tags, new_tags)

    def test_str(self):
        expected_str = (
            f'Role('
            f'account={str(self.account)},'
            f'path="{self.path}",'
            f'name="{self.name}",'
            f'id="{self.id}",'
            f'arn="{self.arn}",'
            f'created_date={self.created_date.isoformat()},'
            f'assume_role_policy_document={self.policy},'
            f'description="{self.description}",'
            f'max_session_duration={self.max_session_duration},'
            f'permissions_boundary={str(self.permissions_boundary)},'
            f'last_used={str(self.last_used)},'
            f'tags={self.tags}'
            f')'
        )
        self.assertEqual(str(self.role_full), expected_str)

    def test_to_dict(self):
        expected_dict = {
            "account": self.account.to_dict(),
            "path": self.path,
            "name": self.name,
            "id": self.id,
            "arn": self.arn,
            "created_date": self.created_date.isoformat(),
            "assume_role_policy_document": self.policy,
            "description": self.description,
            "max_session_duration": self.max_session_duration,
            "permissions_boundary": self.permissions_boundary.to_dict(),
            "last_used": self.last_used.to_dict(),
            "tags": self.tags
        }
        self.assertDictEqual(self.role_full.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
