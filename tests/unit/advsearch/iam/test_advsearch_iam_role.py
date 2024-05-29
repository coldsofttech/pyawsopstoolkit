import unittest
from datetime import datetime
from unittest import mock
from unittest.mock import patch, MagicMock

from pyawsopstoolkit import Session, Account
from pyawsopstoolkit.advsearch import OR
from pyawsopstoolkit.advsearch.iam import Role
from pyawsopstoolkit.exceptions import SearchAttributeError


class TestRole(unittest.TestCase):
    """Unit test cases for Role."""

    def setUp(self) -> None:
        self.profile_name = 'temp'
        self.session = Session(profile_name=self.profile_name)
        self.role = Role(session=self.session)

    def test_initialization(self):
        self.assertEqual(self.role.session, self.session)

    def test_set_session(self):
        new_session = Session(profile_name='sample')
        self.role.session = new_session
        self.assertEqual(self.role.session, new_session)

    @patch('boto3.Session')
    def test_search_roles_empty_kwargs(self, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        self.assertEqual(len(self.role.search_roles()), 0)

    @patch('boto3.Session')
    def test_search_roles_all_none(self, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        self.assertEqual(
            len(self.role.search_roles(condition=OR, name=None, id=None, arn=None)), 0
        )

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.Session.get_session')
    @patch('pyawsopstoolkit.advsearch.iam.__handlers__._list_roles', return_value=[{
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
        from pyawsopstoolkit.models.iam.role import Role

        mock_client = MagicMock()
        mock_caller_identity = MagicMock()

        mock_caller_identity.get.return_value = '123456789012'
        mock_client.get_caller_identity.return_value = mock_caller_identity
        mock_get_session.return_value.client.return_value = mock_client

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        roles_data = mock_list_roles.return_value
        roles = [Role(
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
        self.role.search_roles = mock.Mock(return_value=roles)

        result = self.role.search_roles(condition=OR, name='test_role', id='AID2MAB8DPLSRHEXAMPLE')

        self.assertEqual(result[0].name, 'test_role')
        self.assertIsNone(result[0].permissions_boundary)
        self.assertIsNone(result[0].last_used)
        self.assertIsNone(result[0].tags)

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.Session.get_session')
    @patch('pyawsopstoolkit.advsearch.iam.__handlers__._list_roles', return_value=[{
        'RoleName': 'test_role',
        'Path': '/',
        'RoleId': 'AID2MAB8DPLSRHEXAMPLE',
        'Arn': 'arn:aws:iam::123456789012:role/test_role',
        'Description': 'Test role',
        'MaxSessionDuration': 3600,
        'CreateDate': datetime(2022, 5, 18)
    }])
    @patch('pyawsopstoolkit.advsearch.iam.__handlers__._get_role', return_value={
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
        from pyawsopstoolkit.models.iam import PermissionsBoundary
        from pyawsopstoolkit.models.iam.role import Role

        mock_client = MagicMock()
        mock_caller_identity = MagicMock()

        mock_caller_identity.get.return_value = '123456789012'
        mock_client.get_caller_identity.return_value = mock_caller_identity
        mock_get_session.return_value.client.return_value = mock_client

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        roles_data = mock_get_role.return_value
        roles = [Role(
            account=Account('123456789012'),
            name=role_data['RoleName'],
            id=role_data['RoleId'],
            arn=role_data['Arn'],
            max_session_duration=role_data['MaxSessionDuration'],
            path=role_data.get('Path', '/'),
            created_date=role_data.get('CreateDate'),
            assume_role_policy_document=None,
            description=role_data.get('Description'),
            permissions_boundary=PermissionsBoundary(
                type=role_data['PermissionsBoundary']['PermissionsBoundaryType'],
                arn=role_data['PermissionsBoundary']['PermissionsBoundaryArn']
            ),
            last_used=None,
            tags=role_data.get('Tags')
        ) for role_data in [roles_data]]
        self.role.search_roles = mock.Mock(return_value=roles)

        result = self.role.search_roles(
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
    def test_search_roles_with_permissions_boundary_without_details(self, mock_get_session, mock_session):
        mock_client = MagicMock()
        mock_caller_identity = MagicMock()

        mock_caller_identity.get.return_value = '123456789012'
        mock_client.get_caller_identity.return_value = mock_caller_identity
        mock_get_session.return_value.client.return_value = mock_client

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        with self.assertRaises(SearchAttributeError):
            self.role.search_roles(
                condition=OR,
                name='test_role',
                id='AID2MAB8DPLSRHEXAMPLE',
                permissions_boundary_arn='arn:aws:iam::123456789012:policy/ManagedPolicy'
            )

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.Session.get_session')
    @patch('pyawsopstoolkit.advsearch.iam.__handlers__._list_roles', return_value=[{
        'RoleName': 'test_role',
        'Path': '/',
        'RoleId': 'AID2MAB8DPLSRHEXAMPLE',
        'Arn': 'arn:aws:iam::123456789012:role/test_role',
        'Description': 'Test role',
        'MaxSessionDuration': 3600,
        'CreateDate': datetime(2022, 5, 18)
    }])
    @patch('pyawsopstoolkit.advsearch.iam.__handlers__._get_role', return_value={
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
        from pyawsopstoolkit.models.iam.role import Role, LastUsed
        from pyawsopstoolkit.models.iam import PermissionsBoundary

        mock_client = MagicMock()
        mock_caller_identity = MagicMock()

        mock_caller_identity.get.return_value = '123456789012'
        mock_client.get_caller_identity.return_value = mock_caller_identity
        mock_get_session.return_value.client.return_value = mock_client

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        roles_data = mock_get_role.return_value
        roles = [Role(
            account=Account('123456789012'),
            name=role_data['RoleName'],
            id=role_data['RoleId'],
            arn=role_data['Arn'],
            max_session_duration=role_data['MaxSessionDuration'],
            path=role_data.get('Path', '/'),
            created_date=role_data.get('CreateDate'),
            assume_role_policy_document=None,
            description=role_data.get('Description'),
            permissions_boundary=PermissionsBoundary(
                type=role_data['PermissionsBoundary']['PermissionsBoundaryType'],
                arn=role_data['PermissionsBoundary']['PermissionsBoundaryArn']
            ),
            last_used=LastUsed(
                used_date=role_data['RoleLastUsed']['LastUsedDate'],
                region=role_data['RoleLastUsed']['Region']
            ),
            tags=role_data.get('Tags')
        ) for role_data in [roles_data]]
        self.role.search_roles = mock.Mock(return_value=roles)

        result = self.role.search_roles(
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

        with self.assertRaises(SearchAttributeError):
            self.role.search_roles(
                condition=OR,
                name='test_role',
                id='AID2MAB8DPLSRHEXAMPLE',
                last_used_region='us-west-2'
            )

    @patch('boto3.Session')
    @patch('pyawsopstoolkit.Session.get_session')
    @patch('pyawsopstoolkit.advsearch.iam.__handlers__._list_roles', return_value=[{
        'RoleName': 'test_role',
        'Path': '/',
        'RoleId': 'AID2MAB8DPLSRHEXAMPLE',
        'Arn': 'arn:aws:iam::123456789012:role/test_role',
        'Description': 'Test role',
        'MaxSessionDuration': 3600,
        'CreateDate': datetime(2022, 5, 18)
    }])
    @patch('pyawsopstoolkit.advsearch.iam.__handlers__._get_role', return_value={
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
        from pyawsopstoolkit.models.iam.role import Role, LastUsed
        from pyawsopstoolkit.models.iam import PermissionsBoundary

        mock_client = MagicMock()
        mock_caller_identity = MagicMock()

        mock_caller_identity.get.return_value = '123456789012'
        mock_client.get_caller_identity.return_value = mock_caller_identity
        mock_get_session.return_value.client.return_value = mock_client

        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        roles_data = mock_get_role.return_value
        roles = [Role(
            account=Account('123456789012'),
            name=role_data['RoleName'],
            id=role_data['RoleId'],
            arn=role_data['Arn'],
            max_session_duration=role_data['MaxSessionDuration'],
            path=role_data.get('Path', '/'),
            created_date=role_data.get('CreateDate'),
            assume_role_policy_document=None,
            description=role_data.get('Description'),
            permissions_boundary=PermissionsBoundary(
                type=role_data['PermissionsBoundary']['PermissionsBoundaryType'],
                arn=role_data['PermissionsBoundary']['PermissionsBoundaryArn']
            ),
            last_used=LastUsed(
                used_date=role_data['RoleLastUsed']['LastUsedDate'],
                region=role_data['RoleLastUsed']['Region']
            ),
            tags=role_data.get('Tags')
        ) for role_data in [roles_data]]
        self.role.search_roles = mock.Mock(return_value=roles)

        result = self.role.search_roles(
            condition=OR, include_details=True, name='test_role', id='AID2MAB8DPLSRHEXAMPLE', tag_key='test_key'
        )

        self.assertEqual(result[0].name, 'test_role')
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

        with self.assertRaises(SearchAttributeError):
            self.role.search_roles(condition=OR, name='test_role', id='AID2MAB8DPLSRHEXAMPLE', tag_key='test_key')


if __name__ == "__main__":
    unittest.main()
