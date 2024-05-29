import unittest
from datetime import datetime
from unittest.mock import patch

import pyawsopstoolkit
from pyawsopstoolkit import Account, Session
from pyawsopstoolkit.insights import IAM


class TestIAM(unittest.TestCase):
    def setUp(self) -> None:
        self.profile_name = 'temp'
        self.account = Account('123456789012')

    @patch('boto3.Session')
    def test_unused_roles_no_iam_roles_returned(self, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        iam_object = IAM(session)
        roles = iam_object.unused_roles()
        self.assertEqual(len(roles), 0)

    @patch('boto3.Session')
    def test_unused_users_no_iam_users_returned(self, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        iam_object = IAM(session)
        users = iam_object.unused_users()
        self.assertEqual(len(users), 0)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.advsearch.IAM')
    def test_unused_roles_no_roles_matching_criteria(self, mock_iam, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        mock_iam.return_value.search_roles.return_value = [
            pyawsopstoolkit.models.iam.role.Role(
                account=self.account,
                name='test_role',
                id='ABCDGH',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role',
                max_session_duration=3600,
                permissions_boundary=pyawsopstoolkit.models.iam.PermissionsBoundary(
                    type='Policy',
                    arn=f'arn:aws:iam::{self.account.number}:policy/some_boundary'
                ),
                last_used=pyawsopstoolkit.models.iam.role.LastUsed(
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
    def test_unused_users_no_users_matching_criteria1(self, mock_iam, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        mock_iam.return_value.search_users.return_value = [
            pyawsopstoolkit.models.iam.user.User(
                account=self.account,
                name='test_user',
                id='ABCDGJH',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user',
                created_date=datetime(2022, 5, 18),
                password_last_used_date=datetime.today()
            )
        ]

        iam_object = IAM(session)
        users = iam_object.unused_users()
        self.assertEqual(len(users), 0)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.advsearch.IAM')
    def test_unused_users_no_users_matching_criteria2(self, mock_iam, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        mock_iam.return_value.search_users.return_value = [
            pyawsopstoolkit.models.iam.user.User(
                account=self.account,
                name='test_user',
                id='ABCDGJH',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user',
                created_date=datetime(2022, 5, 18),
                login_profile=pyawsopstoolkit.models.iam.user.LoginProfile(
                    created_date=datetime.today()
                )
            )
        ]

        iam_object = IAM(session)
        users = iam_object.unused_users()
        self.assertEqual(len(users), 0)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.advsearch.IAM')
    def test_unused_users_no_users_matching_criteria3(self, mock_iam, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        mock_iam.return_value.search_users.return_value = [
            pyawsopstoolkit.models.iam.user.User(
                account=self.account,
                name='test_user',
                id='ABCDGJH',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user',
                created_date=datetime(2022, 5, 18),
                password_last_used_date=datetime.today()
            )
        ]

        iam_object = IAM(session)
        users = iam_object.unused_users()
        self.assertEqual(len(users), 0)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.advsearch.IAM')
    def test_unused_users_no_users_matching_criteria4(self, mock_iam, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        mock_iam.return_value.search_users.return_value = [
            pyawsopstoolkit.models.iam.user.User(
                account=self.account,
                name='test_user',
                id='ABCDGJH',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user',
                created_date=datetime(2022, 5, 18),
                access_keys=[
                    pyawsopstoolkit.models.iam.user.AccessKey(
                        id='ACCESS_KEY1',
                        status='Active',
                        created_date=datetime(2022, 6, 18),
                        last_used_date=datetime.today()
                    )
                ]
            )
        ]

        iam_object = IAM(session)
        users = iam_object.unused_users()
        self.assertEqual(len(users), 0)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.advsearch.IAM')
    def test_unused_roles_some_roles_matching_criteria(self, mock_iam, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        mock_iam.return_value.search_roles.return_value = [
            pyawsopstoolkit.models.iam.role.Role(
                account=self.account,
                name='test_role1',
                id='ABCDGH',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role1',
                max_session_duration=3600,
                permissions_boundary=pyawsopstoolkit.models.iam.PermissionsBoundary(
                    type='Policy',
                    arn=f'arn:aws:iam::{self.account.number}:policy/some_boundary'
                ),
                last_used=pyawsopstoolkit.models.iam.role.LastUsed(
                    used_date=datetime.today()
                ),
                created_date=datetime(2022, 3, 15)
            ),
            pyawsopstoolkit.models.iam.role.Role(
                account=self.account,
                name='test_role2',
                id='BCDGHY',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role2',
                max_session_duration=3600,
                last_used=None,
                created_date=datetime.today()
            ),
            pyawsopstoolkit.models.iam.role.Role(
                account=self.account,
                name='test_role3',
                id='BCDGHY',
                path='/service-role/',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role3',
                max_session_duration=3600,
                last_used=None,
                created_date=datetime(2022, 3, 15)
            ),
            pyawsopstoolkit.models.iam.role.Role(
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
    def test_unused_users_some_roles_matching_criteria(self, mock_iam, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        mock_iam.return_value.search_users.return_value = [
            pyawsopstoolkit.models.iam.user.User(
                account=self.account,
                name='test_user1',
                id='ABDCGHY',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user1',
                created_date=datetime(2022, 5, 18),
                login_profile=pyawsopstoolkit.models.iam.user.LoginProfile(
                    created_date=datetime.today()
                )
            ),
            pyawsopstoolkit.models.iam.user.User(
                account=self.account,
                name='test_user2',
                id='SHJYG',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user2',
                created_date=datetime(2022, 5, 18),
                password_last_used_date=datetime.today()
            ),
            pyawsopstoolkit.models.iam.user.User(
                account=self.account,
                name='test_user3',
                id='SHJYG',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user3',
                created_date=datetime(2022, 5, 18),
                access_keys=[
                    pyawsopstoolkit.models.iam.user.AccessKey(
                        id='ACCESS_KEY1',
                        status='Active',
                        created_date=datetime(2022, 6, 18),
                        last_used_date=datetime.today()
                    )
                ]
            ),
            pyawsopstoolkit.models.iam.user.User(
                account=self.account,
                name='test_user4',
                id='SHJYG',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user4',
                created_date=datetime(2022, 5, 18),
                password_last_used_date=datetime(2022, 5, 20)
            ),
            pyawsopstoolkit.models.iam.user.User(
                account=self.account,
                name='test_user5',
                id='SHJYG',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user5',
                created_date=datetime(2022, 5, 18)
            ),
            pyawsopstoolkit.models.iam.user.User(
                account=self.account,
                name='test_user5',
                id='SHJYG',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user5',
                created_date=datetime.today()
            )
        ]

        iam_object = IAM(session)
        users = iam_object.unused_users()
        self.assertEqual(len(users), 2)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.advsearch.IAM')
    def test_unused_roles_some_roles_matching_criteria_include_newly_created(self, mock_iam, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        mock_iam.return_value.search_roles.return_value = [
            pyawsopstoolkit.models.iam.role.Role(
                account=self.account,
                name='test_role1',
                id='ABCDGH',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role1',
                max_session_duration=3600,
                permissions_boundary=pyawsopstoolkit.models.iam.PermissionsBoundary(
                    type='Policy',
                    arn=f'arn:aws:iam::{self.account.number}:policy/some_boundary'
                ),
                last_used=pyawsopstoolkit.models.iam.role.LastUsed(
                    used_date=datetime.today()
                ),
                created_date=datetime(2022, 3, 15)
            ),
            pyawsopstoolkit.models.iam.role.Role(
                account=self.account,
                name='test_role2',
                id='BCDGHY',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role2',
                max_session_duration=3600,
                last_used=None,
                created_date=datetime.today()
            ),
            pyawsopstoolkit.models.iam.role.Role(
                account=self.account,
                name='test_role3',
                id='BCDGHY',
                path='/service-role/',
                arn=f'arn:aws:iam::{self.account.number}:role/test_role3',
                max_session_duration=3600,
                last_used=None,
                created_date=datetime(2022, 3, 15)
            ),
            pyawsopstoolkit.models.iam.role.Role(
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

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.advsearch.IAM')
    def test_unused_users_some_roles_matching_criteria_include_newly_created(self, mock_iam, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        mock_iam.return_value.search_users.return_value = [
            pyawsopstoolkit.models.iam.user.User(
                account=self.account,
                name='test_user1',
                id='ABDCGHY',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user1',
                created_date=datetime(2022, 5, 18),
                login_profile=pyawsopstoolkit.models.iam.user.LoginProfile(
                    created_date=datetime.today()
                )
            ),
            pyawsopstoolkit.models.iam.user.User(
                account=self.account,
                name='test_user2',
                id='SHJYG',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user2',
                created_date=datetime(2022, 5, 18),
                password_last_used_date=datetime.today()
            ),
            pyawsopstoolkit.models.iam.user.User(
                account=self.account,
                name='test_user3',
                id='SHJYG',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user3',
                created_date=datetime(2022, 5, 18),
                access_keys=[
                    pyawsopstoolkit.models.iam.user.AccessKey(
                        id='ACCESS_KEY1',
                        status='Active',
                        created_date=datetime(2022, 6, 18),
                        last_used_date=datetime.today()
                    )
                ]
            ),
            pyawsopstoolkit.models.iam.user.User(
                account=self.account,
                name='test_user4',
                id='SHJYG',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user4',
                created_date=datetime(2022, 5, 18),
                password_last_used_date=datetime(2022, 5, 20)
            ),
            pyawsopstoolkit.models.iam.user.User(
                account=self.account,
                name='test_user5',
                id='SHJYG',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user5',
                created_date=datetime(2022, 5, 18)
            ),
            pyawsopstoolkit.models.iam.user.User(
                account=self.account,
                name='test_user5',
                id='SHJYG',
                arn=f'arn:aws:iam::{self.account.number}:user/test_user5',
                created_date=datetime.today()
            )
        ]

        iam_object = IAM(session)
        users = iam_object.unused_users(include_newly_created=True)
        self.assertEqual(len(users), 3)


if __name__ == "__main__":
    unittest.main()
