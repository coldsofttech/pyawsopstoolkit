import unittest
from unittest.mock import patch

from pyawsopstoolkit import Account, Session
from pyawsopstoolkit.security.iam import Role


class TestRole(unittest.TestCase):
    """Unit test cases for Role."""

    def setUp(self) -> None:
        self.profile_name = 'temp'
        self.account = Account('123456789012')
        self.session = Session(profile_name=self.profile_name)
        self.role = Role(session=self.session)

    def test_initialization(self):
        self.assertEqual(self.role.session, self.session)

    def test_setters(self):
        new_session = Session(profile_name='sample')
        self.role.session = new_session
        self.assertEqual(self.role.session, new_session)

    def test_invalid_types(self):
        invalid_session = 123

        with self.assertRaises(TypeError):
            Role(session=invalid_session)
        with self.assertRaises(TypeError):
            self.role.session = invalid_session

    @patch('boto3.Session')
    def test_roles_without_permissions_boundary_no_iam_roles_returned(self, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        self.assertEqual(len(self.role.roles_without_permissions_boundary()), 0)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.advsearch.iam.Role')
    def test_roles_without_permissions_boundary_no_roles_matching_criteria(self, mock_iam, mock_session):
        from pyawsopstoolkit.models.iam.role import Role
        from pyawsopstoolkit.models.iam import PermissionsBoundary

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        mock_iam.return_value.search_roles.return_value = [
            Role(
                account=self.account,
                name='test_role1',
                id='ABCHYSF',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role1',
                max_session_duration=3600,
                permissions_boundary=PermissionsBoundary(
                    type='Policy',
                    arn=f'arn:aws:iam::{self.account.number}:policy/some_boundary'
                )
            )
        ]

        self.assertEqual(len(self.role.roles_without_permissions_boundary()), 0)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.advsearch.iam.Role')
    def test_roles_without_permissions_boundary_some_roles_matching_criteria(self, mock_iam, mock_session):
        from pyawsopstoolkit.models.iam.role import Role
        from pyawsopstoolkit.models.iam import PermissionsBoundary

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        mock_iam.return_value.search_roles.return_value = [
            Role(
                account=self.account,
                name='test_role1',
                id='ABCHYSF',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role1',
                max_session_duration=3600,
                permissions_boundary=PermissionsBoundary(
                    type='Policy',
                    arn=f'arn:aws:iam::{self.account.number}:policy/some_boundary'
                )
            ),
            Role(
                account=self.account,
                name='test_role2',
                id='BHGSFA',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role2',
                max_session_duration=3600
            ),
            Role(
                account=self.account,
                name='test_role3',
                id='HYGDSG',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role3',
                path='/aws-service-role/',
                max_session_duration=3600
            )
        ]

        roles = self.role.roles_without_permissions_boundary()

        self.assertEqual(len(roles), 1)
        self.assertTrue(all(role.permissions_boundary is None and role.path != '/aws-service-role/' for role in roles))


if __name__ == "__main__":
    unittest.main()
