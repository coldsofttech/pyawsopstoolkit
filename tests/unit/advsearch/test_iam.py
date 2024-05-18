import unittest
from datetime import datetime
from unittest import mock
from unittest.mock import patch, MagicMock

from pyawsopstoolkit import Session, Account
from pyawsopstoolkit.advsearch import IAM, OR
from pyawsopstoolkit.models import IAMRole, IAMRolePermissionsBoundary, IAMRoleLastUsed


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
    def test_search_roles_all_none(self, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        iam_object = IAM(session)
        roles = iam_object.search_roles(condition=OR, name=None, id=None, arn=None)
        self.assertEqual(len(roles), 0)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.Session.get_session')
    @patch('pyawsopstoolkit.advsearch.IAM._list_roles', return_value=[{
        'RoleName': 'test_role',
        'Path': '/',
        'RoleId': '123456789012',
        'Arn': 'arn:aws:iam::123456789012:role/test_role',
        'Description': 'Test role',
        'MaxSessionDuration': 3600,
        'CreateDate': datetime(2022, 5, 18)
    }])
    @patch('pyawsopstoolkit.__validations__.Validation.validate_type', return_value=None)
    @patch('pyawsopstoolkit.validators.ArnValidator.arn', return_value=True)
    @patch('pyawsopstoolkit.validators.Validator.region', return_value=True)
    def test_search_roles_basic(self, mock_region, mock_arn, mock_validation, mock_list_roles, mock_get_session,
                                mock_session):
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
            tags=role_data.get('Tags')
        ) for role_data in roles_data]
        iam_object.search_roles = mock.Mock(return_value=roles)
        result = iam_object.search_roles(condition='OR', name='test_role', id='123456789012')
        self.assertEqual(result[0].name, 'test_role')

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.Session.get_session')
    @patch('pyawsopstoolkit.advsearch.IAM._list_roles', return_value=[{
        'RoleName': 'test_role',
        'Path': '/',
        'RoleId': '123456789012',
        'Arn': 'arn:aws:iam::123456789012:role/test_role',
        'Description': 'Test role',
        'MaxSessionDuration': 3600,
        'CreateDate': datetime(2022, 5, 18)
    }])
    @patch('pyawsopstoolkit.advsearch.IAM._get_role', return_value={
        'RoleName': 'test_role',
        'Path': '/',
        'RoleId': '123456789012',
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
    def test_search_roles_with_permissions_boundary(self, mock_region, mock_arn, mock_validation, mock_get_role,
                                                    mock_list_roles, mock_get_session, mock_session):
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
            permissions_boundary=IAMRolePermissionsBoundary(
                type=role_data['PermissionsBoundary']['PermissionsBoundaryType'],
                arn=role_data['PermissionsBoundary']['PermissionsBoundaryArn']
            ),
            last_used=None,
            tags=role_data.get('Tags')
        ) for role_data in [roles_data]]
        iam_object.search_roles = mock.Mock(return_value=roles)
        result = iam_object.search_roles(condition='OR', name='test_role', id='123456789012')
        self.assertEqual(result[0].name, 'test_role')
        self.assertEqual(result[0].permissions_boundary.arn, 'arn:aws:iam::123456789012:policy/ManagedPolicy')

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.Session.get_session')
    @patch('pyawsopstoolkit.advsearch.IAM._list_roles', return_value=[{
        'RoleName': 'test_role',
        'Path': '/',
        'RoleId': '123456789012',
        'Arn': 'arn:aws:iam::123456789012:role/test_role',
        'Description': 'Test role',
        'MaxSessionDuration': 3600,
        'CreateDate': datetime(2022, 5, 18)
    }])
    @patch('pyawsopstoolkit.advsearch.IAM._get_role', return_value={
        'RoleName': 'test_role',
        'Path': '/',
        'RoleId': '123456789012',
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
    def test_search_roles_with_last_used(self, mock_region, mock_arn, mock_validation, mock_get_role, mock_list_roles,
                                         mock_get_session, mock_session):
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
            permissions_boundary=IAMRolePermissionsBoundary(
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
        result = iam_object.search_roles(condition='OR', name='test_role', id='123456789012')
        self.assertEqual(result[0].name, 'test_role')
        self.assertEqual(result[0].last_used.region, 'us-west-2')

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.Session.get_session')
    @patch('pyawsopstoolkit.advsearch.IAM._list_roles', return_value=[{
        'RoleName': 'test_role',
        'Path': '/',
        'RoleId': '123456789012',
        'Arn': 'arn:aws:iam::123456789012:role/test_role',
        'Description': 'Test role',
        'MaxSessionDuration': 3600,
        'CreateDate': datetime(2022, 5, 18)
    }])
    @patch('pyawsopstoolkit.advsearch.IAM._get_role', return_value={
        'RoleName': 'test_role',
        'Path': '/',
        'RoleId': '123456789012',
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
    def test_search_roles_with_tags(self, mock_region, mock_arn, mock_validation, mock_get_role, mock_list_roles,
                                    mock_get_session, mock_session):
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
            permissions_boundary=IAMRolePermissionsBoundary(
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
        result = iam_object.search_roles(condition='OR', name='test_role', id='123456789012')
        self.assertEqual(result[0].name, 'test_role')
        self.assertEqual(result[0].tags[0].get('Key'), 'test_key')


if __name__ == "__main__":
    unittest.main()
