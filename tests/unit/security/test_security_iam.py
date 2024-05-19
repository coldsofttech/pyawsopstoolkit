import unittest
from unittest.mock import patch

from pyawsopstoolkit import Session, Account
from pyawsopstoolkit.models import IAMRole, IAMRolePermissionsBoundary
from pyawsopstoolkit.security import IAM


class TestIAM(unittest.TestCase):
    def setUp(self) -> None:
        self.profile_name = 'temp'
        self.account = Account('123456789012')

    @patch('boto3.Session')
    def test_no_iam_roles_returned(self, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        iam_object = IAM(session)
        roles = iam_object.roles_without_permissions_boundary()
        self.assertEqual(len(roles), 0)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.advsearch.IAM')
    def test_no_roles_matching_criteria(self, mock_iam, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        mock_iam.return_value.search_roles.return_value = [
            IAMRole(
                account=self.account,
                name='test_role1',
                id='ABCHYSF',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role1',
                max_session_duration=3600,
                permissions_boundary=IAMRolePermissionsBoundary(
                    type='Policy',
                    arn=f'arn:aws:iam::{self.account.number}:policy/some_boundary'
                )
            )
        ]

        iam_object = IAM(session)
        roles = iam_object.roles_without_permissions_boundary()
        self.assertEqual(len(roles), 0)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.advsearch.IAM')
    def test_some_roles_matching_criteria(self, mock_iam, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        mock_iam.return_value.search_roles.return_value = [
            IAMRole(
                account=self.account,
                name='test_role1',
                id='ABCHYSF',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role1',
                max_session_duration=3600,
                permissions_boundary=IAMRolePermissionsBoundary(
                    type='Policy',
                    arn=f'arn:aws:iam::{self.account.number}:policy/some_boundary'
                )
            ),
            IAMRole(
                account=self.account,
                name='test_role2',
                id='BHGSFA',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role2',
                max_session_duration=3600
            ),
            IAMRole(
                account=self.account,
                name='test_role3',
                id='HYGDSG',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role3',
                path='/aws-service-role/',
                max_session_duration=3600
            )
        ]

        iam_object = IAM(session)
        roles = iam_object.roles_without_permissions_boundary()
        self.assertEqual(len(roles), 1)
        self.assertTrue(all(role.permissions_boundary is None and role.path != '/aws-service-role/' for role in roles))


if __name__ == "__main__":
    unittest.main()
