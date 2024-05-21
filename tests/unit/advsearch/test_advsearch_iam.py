import unittest
from datetime import datetime
from unittest import mock
from unittest.mock import patch, MagicMock

from pyawsopstoolkit import Session, Account
from pyawsopstoolkit.advsearch import IAM, OR
from pyawsopstoolkit.exceptions import SearchAttributeError
from pyawsopstoolkit.models import IAMRole, IAMPermissionsBoundary, IAMRoleLastUsed, IAMUser


class TestIAM(unittest.TestCase):
    def setUp(self) -> None:
        self.profile_name = 'temp'

    @patch('boto3.Session')
    def test_search_roles_empty_kwargs(self, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        iam_object = IAM(session)
        roles = iam_object.search_roles()
        self.assertEqual(len(roles), 0)

    @patch('boto3.Session')
    def test_search_users_empty_kwargs(self, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        iam_object = IAM(session)
        users = iam_object.search_users()
        self.assertEqual(len(users), 0)

    @patch('boto3.Session')
    def test_search_roles_all_none(self, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        iam_object = IAM(session)
        roles = iam_object.search_roles(condition=OR, name=None, id=None, arn=None)
        self.assertEqual(len(roles), 0)

    @patch('boto3.Session')
    def test_search_users_all_none(self, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        iam_object = IAM(session)
        users = iam_object.search_users(condition=OR, name=None, id=None, arn=None)
        self.assertEqual(len(users), 0)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.Session.get_session')
    @patch('pyawsopstoolkit.advsearch.IAM._list_roles', return_value=[{
        'RoleName': 'test_role',
        'Path': '/',
        'RoleId': 'AID2MAB8DPLSRHEXAMPLE',
        'Arn': 'arn:aws:iam::123456789012:role/test_role',
        'Description': 'Test role',
        'MaxSessionDuration': 3600,
        'CreateDate': datetime(2022, 5, 18)
    }])
    @patch('pyawsopstoolkit.__validations__.Validation.validate_type', return_value=None)
    @patch('pyawsopstoolkit.validators.ArnValidator.arn', return_value=True)
    @patch('pyawsopstoolkit.validators.Validator.region', return_value=True)
    def test_search_roles_basic(
            self, mock_region, mock_arn, mock_validation, mock_list_roles, mock_get_session, mock_session
    ):
        mock_client = MagicMock()
        mock_caller_identity = MagicMock()

        mock_caller_identity.get.return_value = '123456789012'
        mock_client.get_caller_identity.return_value = mock_caller_identity
        mock_get_session.return_value.client.return_value = mock_client

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        iam_object = IAM(session)
        roles_data = mock_list_roles.return_value
        roles = [IAMRole(
            account=Account('123456789012'),
            name=role_data['RoleName'],
            id=role_data['RoleId'],
            arn=role_data['Arn'],
            max_session_duration=role_data['MaxSessionDuration'],
            path=role_data.get('Path', '/'),
            created_date=role_data.get('CreateDate'),
            assume_role_policy_document=None,
            description=role_data.get('Description'),
            permissions_boundary=None,
            last_used=None,
            tags=None
        ) for role_data in roles_data]
        iam_object.search_roles = mock.Mock(return_value=roles)
        result = iam_object.search_roles(condition=OR, name='test_role', id='AID2MAB8DPLSRHEXAMPLE')
        self.assertEqual(result[0].name, 'test_role')
        self.assertIsNone(result[0].permissions_boundary)
        self.assertIsNone(result[0].last_used)
        self.assertIsNone(result[0].tags)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.Session.get_session')
    @patch('pyawsopstoolkit.advsearch.IAM._list_users', return_value=[{
        'Path': '/',
        'UserName': 'test_user',
        'UserId': 'AID2MAB8DPLSRHEXAMPLE',
        'Arn': 'arn:aws:iam::123456789012:user/test_user',
        'CreateDate': datetime(2022, 5, 18)
    }])
    @patch('pyawsopstoolkit.__validations__.Validation.validate_type', return_value=None)
    @patch('pyawsopstoolkit.validators.ArnValidator.arn', return_value=True)
    @patch('pyawsopstoolkit.validators.Validator.region', return_value=True)
    def test_search_users_basic(
            self, mock_region, mock_arn, mock_validation, mock_list_users, mock_get_session, mock_session
    ):
        mock_client = MagicMock()
        mock_caller_identity = MagicMock()

        mock_caller_identity.get.return_value = '123456789012'
        mock_client.get_caller_identity.return_value = mock_caller_identity
        mock_get_session.return_value.client.return_value = mock_client

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        iam_object = IAM(session)
        users_data = mock_list_users.return_value
        users = [IAMUser(
            account=Account('123456789012'),
            name=user_data['UserName'],
            id=user_data['UserId'],
            arn=user_data['Arn'],
            path=user_data['Path'],
            created_date=user_data.get('CreateDate'),
            password_last_used_date=None,
            permissions_boundary=None,
            tags=None
        ) for user_data in users_data]
        iam_object.search_users = mock.Mock(return_value=users)
        result = iam_object.search_users(condition=OR, name='test_user', id='AID2MAB8DPLSRHEXAMPLE')
        self.assertEqual(result[0].name, 'test_user')
        self.assertIsNone(result[0].permissions_boundary)
        self.assertIsNone(result[0].password_last_used_date)
        self.assertIsNone(result[0].tags)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.Session.get_session')
    @patch('pyawsopstoolkit.advsearch.IAM._list_roles', return_value=[{
        'RoleName': 'test_role',
        'Path': '/',
        'RoleId': 'AID2MAB8DPLSRHEXAMPLE',
        'Arn': 'arn:aws:iam::123456789012:role/test_role',
        'Description': 'Test role',
        'MaxSessionDuration': 3600,
        'CreateDate': datetime(2022, 5, 18)
    }])
    @patch('pyawsopstoolkit.advsearch.IAM._get_role', return_value={
        'RoleName': 'test_role',
        'Path': '/',
        'RoleId': 'AID2MAB8DPLSRHEXAMPLE',
        'Arn': 'arn:aws:iam::123456789012:role/test_role',
        'Description': 'Test role',
        'PermissionsBoundary': {
            'PermissionsBoundaryType': 'Managed',
            'PermissionsBoundaryArn': 'arn:aws:iam::123456789012:policy/ManagedPolicy'
        },
        'MaxSessionDuration': 3600,
        'CreateDate': datetime(2022, 5, 18),
    })
    @patch('pyawsopstoolkit.__validations__.Validation.validate_type', return_value=None)
    @patch('pyawsopstoolkit.validators.ArnValidator.arn', return_value=True)
    @patch('pyawsopstoolkit.validators.Validator.region', return_value=True)
    def test_search_roles_with_permissions_boundary(
            self, mock_region, mock_arn, mock_validation, mock_get_role, mock_list_roles, mock_get_session, mock_session
    ):
        mock_client = MagicMock()
        mock_caller_identity = MagicMock()

        mock_caller_identity.get.return_value = '123456789012'
        mock_client.get_caller_identity.return_value = mock_caller_identity
        mock_get_session.return_value.client.return_value = mock_client

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        iam_object = IAM(session)
        roles_data = mock_get_role.return_value
        roles = [IAMRole(
            account=Account('123456789012'),
            name=role_data['RoleName'],
            id=role_data['RoleId'],
            arn=role_data['Arn'],
            max_session_duration=role_data['MaxSessionDuration'],
            path=role_data.get('Path', '/'),
            created_date=role_data.get('CreateDate'),
            assume_role_policy_document=None,
            description=role_data.get('Description'),
            permissions_boundary=IAMPermissionsBoundary(
                type=role_data['PermissionsBoundary']['PermissionsBoundaryType'],
                arn=role_data['PermissionsBoundary']['PermissionsBoundaryArn']
            ),
            last_used=None,
            tags=role_data.get('Tags')
        ) for role_data in [roles_data]]
        iam_object.search_roles = mock.Mock(return_value=roles)
        result = iam_object.search_roles(
            condition=OR,
            include_details=True,
            name='test_role',
            id='AID2MAB8DPLSRHEXAMPLE',
            permissions_boundary_arn='arn:aws:iam::123456789012:policy/ManagedPolicy'
        )
        self.assertEqual(result[0].name, 'test_role')
        self.assertEqual(result[0].permissions_boundary.arn, 'arn:aws:iam::123456789012:policy/ManagedPolicy')

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.Session.get_session')
    @patch('pyawsopstoolkit.advsearch.IAM._list_users', return_value=[{
        'Path': '/',
        'UserName': 'test_user',
        'UserId': 'AID2MAB8DPLSRHEXAMPLE',
        'Arn': 'arn:aws:iam::123456789012:user/test_user',
        'CreateDate': datetime(2022, 5, 18)
    }])
    @patch('pyawsopstoolkit.advsearch.IAM._get_user', return_value={
        'Path': '/',
        'UserName': 'test_user',
        'UserId': 'AID2MAB8DPLSRHEXAMPLE',
        'Arn': 'arn:aws:iam::123456789012:user/test_user',
        'CreateDate': datetime(2022, 5, 18),
        'PermissionsBoundary': {
            'PermissionsBoundaryType': 'Managed',
            'PermissionsBoundaryArn': 'arn:aws:iam::123456789012:policy/ManagedPolicy'
        }
    })
    @patch('pyawsopstoolkit.__validations__.Validation.validate_type', return_value=None)
    @patch('pyawsopstoolkit.validators.ArnValidator.arn', return_value=True)
    @patch('pyawsopstoolkit.validators.Validator.region', return_value=True)
    def test_search_users_with_permissions_boundary(
            self, mock_region, mock_arn, mock_validation, mock_get_user, mock_list_users, mock_get_session, mock_session
    ):
        mock_client = MagicMock()
        mock_caller_identity = MagicMock()

        mock_caller_identity.get.return_value = '123456789012'
        mock_client.get_caller_identity.return_value = mock_caller_identity
        mock_get_session.return_value.client.return_value = mock_client

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        iam_object = IAM(session)
        users_data = mock_get_user.return_value
        users = [IAMUser(
            account=Account('123456789012'),
            name=user_data['UserName'],
            id=user_data['UserId'],
            arn=user_data['Arn'],
            path=user_data['Path'],
            created_date=user_data.get('CreateDate'),
            password_last_used_date=None,
            permissions_boundary=IAMPermissionsBoundary(
                type=user_data['PermissionsBoundary']['PermissionsBoundaryType'],
                arn=user_data['PermissionsBoundary']['PermissionsBoundaryArn']
            ),
            tags=None
        ) for user_data in [users_data]]
        iam_object.search_users = mock.Mock(return_value=users)
        result = iam_object.search_users(
            condition=OR,
            include_details=True,
            name='test_user',
            id='AID2MAB8DPLSRHEXAMPLE',
            permissions_boundary_arn='arn:aws:iam::123456789012:policy/ManagedPolicy'
        )
        self.assertEqual(result[0].name, 'test_user')
        self.assertEqual(result[0].permissions_boundary.arn, 'arn:aws:iam::123456789012:policy/ManagedPolicy')

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.Session.get_session')
    def test_search_roles_with_permissions_boundary_without_details(self, mock_get_session, mock_session):
        mock_client = MagicMock()
        mock_caller_identity = MagicMock()

        mock_caller_identity.get.return_value = '123456789012'
        mock_client.get_caller_identity.return_value = mock_caller_identity
        mock_get_session.return_value.client.return_value = mock_client

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        iam_object = IAM(session)
        with self.assertRaises(SearchAttributeError):
            iam_object.search_roles(
                condition=OR,
                name='test_role',
                id='AID2MAB8DPLSRHEXAMPLE',
                permissions_boundary_arn='arn:aws:iam::123456789012:policy/ManagedPolicy'
            )

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.Session.get_session')
    def test_search_users_with_permissions_boundary_without_details(self, mock_get_session, mock_session):
        mock_client = MagicMock()
        mock_caller_identity = MagicMock()

        mock_caller_identity.get.return_value = '123456789012'
        mock_client.get_caller_identity.return_value = mock_caller_identity
        mock_get_session.return_value.client.return_value = mock_client

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        iam_object = IAM(session)
        with self.assertRaises(SearchAttributeError):
            iam_object.search_users(
                condition=OR,
                name='test_user',
                id='AID2MAB8DPLSRHEXAMPLE',
                permissions_boundary_arn='arn:aws:iam::123456789012:policy/ManagedPolicy'
            )

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.Session.get_session')
    @patch('pyawsopstoolkit.advsearch.IAM._list_roles', return_value=[{
        'RoleName': 'test_role',
        'Path': '/',
        'RoleId': 'AID2MAB8DPLSRHEXAMPLE',
        'Arn': 'arn:aws:iam::123456789012:role/test_role',
        'Description': 'Test role',
        'MaxSessionDuration': 3600,
        'CreateDate': datetime(2022, 5, 18)
    }])
    @patch('pyawsopstoolkit.advsearch.IAM._get_role', return_value={
        'RoleName': 'test_role',
        'Path': '/',
        'RoleId': 'AID2MAB8DPLSRHEXAMPLE',
        'Arn': 'arn:aws:iam::123456789012:role/test_role',
        'Description': 'Test role',
        'PermissionsBoundary': {
            'PermissionsBoundaryType': 'Managed',
            'PermissionsBoundaryArn': 'arn:aws:iam::123456789012:policy/ManagedPolicy'
        },
        'MaxSessionDuration': 3600,
        'CreateDate': datetime(2022, 5, 18),
        'RoleLastUsed': {
            'LastUsedDate': datetime(2024, 5, 18),
            'Region': 'us-west-2'
        },
    })
    @patch('pyawsopstoolkit.__validations__.Validation.validate_type', return_value=None)
    @patch('pyawsopstoolkit.validators.ArnValidator.arn', return_value=True)
    @patch('pyawsopstoolkit.validators.Validator.region', return_value=True)
    def test_search_roles_with_last_used(
            self, mock_region, mock_arn, mock_validation, mock_get_role, mock_list_roles, mock_get_session, mock_session
    ):
        mock_client = MagicMock()
        mock_caller_identity = MagicMock()

        mock_caller_identity.get.return_value = '123456789012'
        mock_client.get_caller_identity.return_value = mock_caller_identity
        mock_get_session.return_value.client.return_value = mock_client

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        iam_object = IAM(session)
        roles_data = mock_get_role.return_value
        roles = [IAMRole(
            account=Account('123456789012'),
            name=role_data['RoleName'],
            id=role_data['RoleId'],
            arn=role_data['Arn'],
            max_session_duration=role_data['MaxSessionDuration'],
            path=role_data.get('Path', '/'),
            created_date=role_data.get('CreateDate'),
            assume_role_policy_document=None,
            description=role_data.get('Description'),
            permissions_boundary=IAMPermissionsBoundary(
                type=role_data['PermissionsBoundary']['PermissionsBoundaryType'],
                arn=role_data['PermissionsBoundary']['PermissionsBoundaryArn']
            ),
            last_used=IAMRoleLastUsed(
                used_date=role_data['RoleLastUsed']['LastUsedDate'],
                region=role_data['RoleLastUsed']['Region']
            ),
            tags=role_data.get('Tags')
        ) for role_data in [roles_data]]
        iam_object.search_roles = mock.Mock(return_value=roles)
        result = iam_object.search_roles(
            condition=OR,
            include_details=True,
            name='test_role',
            id='AID2MAB8DPLSRHEXAMPLE',
            last_used_region='us-west-2'
        )
        self.assertEqual(result[0].name, 'test_role')
        self.assertEqual(result[0].last_used.region, 'us-west-2')

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.Session.get_session')
    def test_search_roles_with_last_used_without_include(self, mock_get_session, mock_session):
        mock_client = MagicMock()
        mock_caller_identity = MagicMock()

        mock_caller_identity.get.return_value = '123456789012'
        mock_client.get_caller_identity.return_value = mock_caller_identity
        mock_get_session.return_value.client.return_value = mock_client

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        iam_object = IAM(session)
        with self.assertRaises(SearchAttributeError):
            iam_object.search_roles(
                condition=OR,
                name='test_role',
                id='AID2MAB8DPLSRHEXAMPLE',
                last_used_region='us-west-2'
            )

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.Session.get_session')
    @patch('pyawsopstoolkit.advsearch.IAM._list_roles', return_value=[{
        'RoleName': 'test_role',
        'Path': '/',
        'RoleId': 'AID2MAB8DPLSRHEXAMPLE',
        'Arn': 'arn:aws:iam::123456789012:role/test_role',
        'Description': 'Test role',
        'MaxSessionDuration': 3600,
        'CreateDate': datetime(2022, 5, 18)
    }])
    @patch('pyawsopstoolkit.advsearch.IAM._get_role', return_value={
        'RoleName': 'test_role',
        'Path': '/',
        'RoleId': 'AID2MAB8DPLSRHEXAMPLE',
        'Arn': 'arn:aws:iam::123456789012:role/test_role',
        'Description': 'Test role',
        'PermissionsBoundary': {
            'PermissionsBoundaryType': 'Managed',
            'PermissionsBoundaryArn': 'arn:aws:iam::123456789012:policy/ManagedPolicy'
        },
        'MaxSessionDuration': 3600,
        'CreateDate': datetime(2022, 5, 18),
        'RoleLastUsed': {
            'LastUsedDate': datetime(2024, 5, 18),
            'Region': 'us-west-2'
        },
        'Tags': [{'Key': 'test_key', 'Value': 'test_value'}]
    })
    @patch('pyawsopstoolkit.__validations__.Validation.validate_type', return_value=None)
    @patch('pyawsopstoolkit.validators.ArnValidator.arn', return_value=True)
    @patch('pyawsopstoolkit.validators.Validator.region', return_value=True)
    def test_search_roles_with_tags(
            self, mock_region, mock_arn, mock_validation, mock_get_role, mock_list_roles, mock_get_session, mock_session
    ):
        mock_client = MagicMock()
        mock_caller_identity = MagicMock()

        mock_caller_identity.get.return_value = '123456789012'
        mock_client.get_caller_identity.return_value = mock_caller_identity
        mock_get_session.return_value.client.return_value = mock_client

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        iam_object = IAM(session)
        roles_data = mock_get_role.return_value
        roles = [IAMRole(
            account=Account('123456789012'),
            name=role_data['RoleName'],
            id=role_data['RoleId'],
            arn=role_data['Arn'],
            max_session_duration=role_data['MaxSessionDuration'],
            path=role_data.get('Path', '/'),
            created_date=role_data.get('CreateDate'),
            assume_role_policy_document=None,
            description=role_data.get('Description'),
            permissions_boundary=IAMPermissionsBoundary(
                type=role_data['PermissionsBoundary']['PermissionsBoundaryType'],
                arn=role_data['PermissionsBoundary']['PermissionsBoundaryArn']
            ),
            last_used=IAMRoleLastUsed(
                used_date=role_data['RoleLastUsed']['LastUsedDate'],
                region=role_data['RoleLastUsed']['Region']
            ),
            tags=role_data.get('Tags')
        ) for role_data in [roles_data]]
        iam_object.search_roles = mock.Mock(return_value=roles)
        result = iam_object.search_roles(
            condition=OR, include_details=True, name='test_role', id='AID2MAB8DPLSRHEXAMPLE', tag_key='test_key'
        )
        self.assertEqual(result[0].name, 'test_role')
        self.assertEqual(result[0].tags[0].get('Key'), 'test_key')

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.Session.get_session')
    @patch('pyawsopstoolkit.advsearch.IAM._list_users', return_value=[{
        'Path': '/',
        'UserName': 'test_user',
        'UserId': 'AID2MAB8DPLSRHEXAMPLE',
        'Arn': 'arn:aws:iam::123456789012:user/test_user',
        'CreateDate': datetime(2022, 5, 18)
    }])
    @patch('pyawsopstoolkit.advsearch.IAM._get_user', return_value={
        'Path': '/',
        'UserName': 'test_user',
        'UserId': 'AID2MAB8DPLSRHEXAMPLE',
        'Arn': 'arn:aws:iam::123456789012:user/test_user',
        'CreateDate': datetime(2022, 5, 18),
        'PermissionsBoundary': {
            'PermissionsBoundaryType': 'Managed',
            'PermissionsBoundaryArn': 'arn:aws:iam::123456789012:policy/ManagedPolicy'
        },
        'Tags': [{'Key': 'test_key', 'Value': 'test_value'}]
    })
    @patch('pyawsopstoolkit.__validations__.Validation.validate_type', return_value=None)
    @patch('pyawsopstoolkit.validators.ArnValidator.arn', return_value=True)
    @patch('pyawsopstoolkit.validators.Validator.region', return_value=True)
    def test_search_users_with_tags(
            self, mock_region, mock_arn, mock_validation, mock_get_user, mock_list_users, mock_get_session, mock_session
    ):
        mock_client = MagicMock()
        mock_caller_identity = MagicMock()

        mock_caller_identity.get.return_value = '123456789012'
        mock_client.get_caller_identity.return_value = mock_caller_identity
        mock_get_session.return_value.client.return_value = mock_client

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        iam_object = IAM(session)
        users_data = mock_get_user.return_value
        users = [IAMUser(
            account=Account('123456789012'),
            name=user_data['UserName'],
            id=user_data['UserId'],
            arn=user_data['Arn'],
            path=user_data['Path'],
            created_date=user_data.get('CreateDate'),
            password_last_used_date=None,
            permissions_boundary=IAMPermissionsBoundary(
                type=user_data['PermissionsBoundary']['PermissionsBoundaryType'],
                arn=user_data['PermissionsBoundary']['PermissionsBoundaryArn']
            ),
            tags=user_data.get('Tags')
        ) for user_data in [users_data]]
        iam_object.search_users = mock.Mock(return_value=users)
        result = iam_object.search_users(
            condition=OR, include_details=True, name='test_user', id='AID2MAB8DPLSRHEXAMPLE', tag_key='test_key'
        )
        self.assertEqual(result[0].name, 'test_user')
        self.assertEqual(result[0].tags[0].get('Key'), 'test_key')

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.Session.get_session')
    def test_search_roles_with_tags_without_include(self, mock_get_session, mock_session):
        mock_client = MagicMock()
        mock_caller_identity = MagicMock()

        mock_caller_identity.get.return_value = '123456789012'
        mock_client.get_caller_identity.return_value = mock_caller_identity
        mock_get_session.return_value.client.return_value = mock_client

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        iam_object = IAM(session)
        with self.assertRaises(SearchAttributeError):
            iam_object.search_roles(condition=OR, name='test_role', id='AID2MAB8DPLSRHEXAMPLE', tag_key='test_key')

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.Session.get_session')
    def test_search_users_with_tags_without_include(self, mock_get_session, mock_session):
        mock_client = MagicMock()
        mock_caller_identity = MagicMock()

        mock_caller_identity.get.return_value = '123456789012'
        mock_client.get_caller_identity.return_value = mock_caller_identity
        mock_get_session.return_value.client.return_value = mock_client

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        iam_object = IAM(session)
        with self.assertRaises(SearchAttributeError):
            iam_object.search_users(condition=OR, name='test_user', id='AID2MAB8DPLSRHEXAMPLE', tag_key='test_key')


if __name__ == "__main__":
    unittest.main()
