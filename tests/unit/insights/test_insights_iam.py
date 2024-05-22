import unittest
from datetime import datetime
from unittest.mock import patch

from pyawsopstoolkit import Account, Session
from pyawsopstoolkit.insights import IAM
from pyawsopstoolkit.models import IAMRole, IAMPermissionsBoundary, IAMRoleLastUsed


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
        roles = iam_object.unused_roles()
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
                name='test_role',
                id='ABCDGH',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role',
                max_session_duration=3600,
                permissions_boundary=IAMPermissionsBoundary(
                    type='Policy',
                    arn=f'arn:aws:iam::{self.account.number}:policy/some_boundary'
                ),
                last_used=IAMRoleLastUsed(
                    used_date=datetime.today()
                ),
                created_date=datetime(2022, 3, 15)
            )
        ]

        iam_object = IAM(session)
        roles = iam_object.unused_roles()
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
                id='ABCDGH',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role1',
                max_session_duration=3600,
                permissions_boundary=IAMPermissionsBoundary(
                    type='Policy',
                    arn=f'arn:aws:iam::{self.account.number}:policy/some_boundary'
                ),
                last_used=IAMRoleLastUsed(
                    used_date=datetime.today()
                ),
                created_date=datetime(2022, 3, 15)
            ),
            IAMRole(
                account=self.account,
                name='test_role2',
                id='BCDGHY',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role2',
                max_session_duration=3600,
                last_used=None,
                created_date=datetime.today()
            ),
            IAMRole(
                account=self.account,
                name='test_role3',
                id='BCDGHY',
                path='/service-role/',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role3',
                max_session_duration=3600,
                last_used=None,
                created_date=datetime(2022, 3, 15)
            ),
            IAMRole(
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

        iam_object = IAM(session)
        roles = iam_object.unused_roles()
        self.assertEqual(len(roles), 1)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.advsearch.IAM')
    def test_some_roles_matching_criteria_include_newly_created(self, mock_iam, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        mock_iam.return_value.search_roles.return_value = [
            IAMRole(
                account=self.account,
                name='test_role1',
                id='ABCDGH',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role1',
                max_session_duration=3600,
                permissions_boundary=IAMPermissionsBoundary(
                    type='Policy',
                    arn=f'arn:aws:iam::{self.account.number}:policy/some_boundary'
                ),
                last_used=IAMRoleLastUsed(
                    used_date=datetime.today()
                ),
                created_date=datetime(2022, 3, 15)
            ),
            IAMRole(
                account=self.account,
                name='test_role2',
                id='BCDGHY',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role2',
                max_session_duration=3600,
                last_used=None,
                created_date=datetime.today()
            ),
            IAMRole(
                account=self.account,
                name='test_role3',
                id='BCDGHY',
                path='/service-role/',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role3',
                max_session_duration=3600,
                last_used=None,
                created_date=datetime(2022, 3, 15)
            ),
            IAMRole(
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

        iam_object = IAM(session)
        roles = iam_object.unused_roles(include_newly_created=True)
        self.assertEqual(len(roles), 2)


if __name__ == "__main__":
    unittest.main()
