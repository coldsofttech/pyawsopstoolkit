import unittest
from datetime import datetime
from unittest.mock import patch

from pyawsopstoolkit import Account, Session
from pyawsopstoolkit.insights.iam import Role


class TestRole(unittest.TestCase):
    """Unit test cases for Role."""

    def setUp(self) -> None:
        self.profile_name = 'temp'
        self.account = Account('123456789012')
        self.session = Session(profile_name=self.profile_name)
        self.role = Role(session=self.session)

    def test_initialization(self):
        self.assertEqual(self.role.session, self.session)

    def test_set_session(self):
        new_session = Session(profile_name='sample')
        self.role.session = new_session
        self.assertEqual(self.role.session, new_session)

    @patch('boto3.Session')
    def test_unused_roles_no_iam_roles_returned(self, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        self.assertEqual(len(self.role.unused_roles()), 0)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.advsearch.iam.Role')
    def test_unused_roles_no_roles_matching_criteria(self, mock_iam, mock_session):
        from pyawsopstoolkit.models.iam.role import Role, LastUsed
        from pyawsopstoolkit.models.iam import PermissionsBoundary

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        mock_iam.return_value.search_roles.return_value = [
            Role(
                account=self.account,
                name='test_role',
                id='ABCDGH',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role',
                max_session_duration=3600,
                permissions_boundary=PermissionsBoundary(
                    type='Policy',
                    arn=f'arn:aws:iam::{self.account.number}:policy/some_boundary'
                ),
                last_used=LastUsed(
                    used_date=datetime.today()
                ),
                created_date=datetime(2022, 3, 15)
            )
        ]

        self.assertEqual(len(self.role.unused_roles()), 0)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.advsearch.iam.Role')
    def test_unused_roles_some_roles_matching_criteria(self, mock_iam, mock_session):
        from pyawsopstoolkit.models.iam.role import Role, LastUsed
        from pyawsopstoolkit.models.iam import PermissionsBoundary

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        mock_iam.return_value.search_roles.return_value = [
            Role(
                account=self.account,
                name='test_role1',
                id='ABCDGH',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role1',
                max_session_duration=3600,
                permissions_boundary=PermissionsBoundary(
                    type='Policy',
                    arn=f'arn:aws:iam::{self.account.number}:policy/some_boundary'
                ),
                last_used=LastUsed(
                    used_date=datetime.today()
                ),
                created_date=datetime(2022, 3, 15)
            ),
            Role(
                account=self.account,
                name='test_role2',
                id='BCDGHY',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role2',
                max_session_duration=3600,
                last_used=None,
                created_date=datetime.today()
            ),
            Role(
                account=self.account,
                name='test_role3',
                id='BCDGHY',
                path='/service-role/',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role3',
                max_session_duration=3600,
                last_used=None,
                created_date=datetime(2022, 3, 15)
            ),
            Role(
                account=self.account,
                name='test_role2',
                id='BCDGHY',
                path='/aws-service-role/',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role2',
                max_session_duration=3600,
                last_used=None,
                created_date=datetime(2022, 3, 15)
            )
        ]

        self.assertEqual(len(self.role.unused_roles()), 1)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.advsearch.iam.Role')
    def test_unused_roles_some_roles_matching_criteria_include_newly_created(self, mock_iam, mock_session):
        from pyawsopstoolkit.models.iam.role import Role, LastUsed
        from pyawsopstoolkit.models.iam import PermissionsBoundary

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        mock_iam.return_value.search_roles.return_value = [
            Role(
                account=self.account,
                name='test_role1',
                id='ABCDGH',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role1',
                max_session_duration=3600,
                permissions_boundary=PermissionsBoundary(
                    type='Policy',
                    arn=f'arn:aws:iam::{self.account.number}:policy/some_boundary'
                ),
                last_used=LastUsed(
                    used_date=datetime.today()
                ),
                created_date=datetime(2022, 3, 15)
            ),
            Role(
                account=self.account,
                name='test_role2',
                id='BCDGHY',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role2',
                max_session_duration=3600,
                last_used=None,
                created_date=datetime.today()
            ),
            Role(
                account=self.account,
                name='test_role3',
                id='BCDGHY',
                path='/service-role/',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role3',
                max_session_duration=3600,
                last_used=None,
                created_date=datetime(2022, 3, 15)
            ),
            Role(
                account=self.account,
                name='test_role2',
                id='BCDGHY',
                path='/aws-service-role/',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role2',
                max_session_duration=3600,
                last_used=None,
                created_date=datetime(2022, 3, 15)
            )
        ]

        self.assertEqual(len(self.role.unused_roles(include_newly_created=True)), 2)


if __name__ == "__main__":
    unittest.main()
