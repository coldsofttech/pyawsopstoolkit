import unittest
from datetime import datetime
from unittest.mock import patch, MagicMock

import botocore.config
from botocore.exceptions import ProfileNotFound, ClientError

from pyawsopstoolkit import Credentials, Session
from pyawsopstoolkit.exceptions import AssumeRoleError, ValidationError


class TestSession(unittest.TestCase):
    """Unit test cases for Session class."""

    def setUp(self) -> None:
        self.profile_name = 'default'
        self.credentials = Credentials('access_key', 'secret_access_key', 'token')
        self.region_code = 'us-east-1'
        self.session_with_profile = Session(profile_name=self.profile_name)
        self.session_with_creds = Session(credentials=self.credentials)
        self.mock_session_with_profile = Session(profile_name='valid_profile')

    def test_init_valid_profile_name(self):
        """Test if init works as expected."""
        session = Session(profile_name=self.profile_name)

        self.assertEqual(session._profile_name, self.profile_name)
        self.assertIsNone(session._credentials)
        self.assertEqual(session._region_code, 'eu-west-1')

    def test_init_valid_credentials(self):
        """Test if init works as expected."""
        session = Session(credentials=self.credentials)

        self.assertIsNone(session._profile_name)
        self.assertEqual(session._credentials, self.credentials)
        self.assertEqual(session._region_code, 'eu-west-1')

    def test_init_invalid_profile_name(self):
        """Test if init raises exception as expected."""
        with self.assertRaises(TypeError):
            Session(profile_name=123)

    def test_init_invalid_credentials(self):
        """Test if init raises exception as expected."""
        with self.assertRaises(TypeError):
            Session(credentials=123)

    def test_init_invalid_region_code(self):
        """Test if init raises exception as expected."""
        with self.assertRaises(ValidationError):
            Session(profile_name=self.profile_name, region_code='usa-east-1')

    def test_init_invalid_both_provided(self):
        """Test if init raises exception as expected."""
        with self.assertRaises(ValueError):
            Session(profile_name=self.profile_name, credentials=self.credentials)

    def test_init_invalid_both_not_provided(self):
        """Test if init raises exception as expected."""
        with self.assertRaises(ValueError):
            Session()

    def test_get_profile_name(self):
        """Test if profile name works as expected."""
        self.assertEqual(self.session_with_profile.profile_name, self.profile_name)

    def test_set_profile_name_valid(self):
        """Test if profile name works as expected."""
        new_profile_name = 'new_profile_name'
        self.session_with_profile.profile_name = new_profile_name
        self.assertEqual(self.session_with_profile.profile_name, new_profile_name)

    def test_set_profile_name_invalid_type(self):
        """Test if profile name raises exception as expected."""
        with self.assertRaises(TypeError):
            self.session_with_profile.profile_name = 123

    def test_set_profile_name_invalid(self):
        """Test if profile name raises exception as expected."""
        with self.assertRaises(ValueError):
            self.session_with_creds.profile_name = self.profile_name

    def test_get_credentials(self):
        """Test if credentials works as expected."""
        self.assertEqual(self.session_with_creds.credentials, self.credentials)

    def test_set_credentials_valid(self):
        """Test if credentials works as expected."""
        new_credentials = Credentials('new_access_key', 'new_secret_access_key', 'new_token')
        self.session_with_creds.credentials = new_credentials
        self.assertEqual(self.session_with_creds.credentials, new_credentials)

    def test_set_credentials_invalid_type(self):
        """Test if credentials raises exception as expected."""
        with self.assertRaises(TypeError):
            self.session_with_creds.credentials = 123

    def test_set_credentials_invalid(self):
        """Test if credentials raises exception as expected."""
        with self.assertRaises(ValueError):
            self.session_with_profile.credentials = self.credentials

    def test_get_region_code(self):
        """Test if region code works as expected."""
        self.assertEqual(self.session_with_profile.region_code, 'eu-west-1')

    def test_set_region_code_valid(self):
        """Test if region code works as expected."""
        self.session_with_profile.region_code = self.region_code
        self.assertEqual(self.session_with_profile.region_code, self.region_code)

    def test_set_region_code_invalid(self):
        """Test if region code raises exception as expected."""
        with self.assertRaises(TypeError):
            self.session_with_profile.region_code = 123

    @patch('boto3.Session')
    def test_get_session_with_profile_name(self, mock_session):
        """Test if the get session works as expected."""
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(profile_name=self.profile_name)
        result = session.get_session()

        self.assertIsNotNone(result)
        mock_session.assert_called_once_with(profile_name=self.profile_name)

    @patch('boto3.Session')
    def test_get_session_with_credentials(self, mock_session):
        """Test if the get session works as expected."""
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        session = Session(credentials=self.credentials)
        result = session.get_session()

        self.assertIsNotNone(result)
        mock_session.assert_called_once_with(
            aws_access_key_id=self.credentials.access_key,
            aws_secret_access_key=self.credentials.secret_access_key,
            aws_session_token=self.credentials.token
        )

    @patch('boto3.Session')
    def test_get_session_with_no_profile_or_credentials(self, mock_session):
        """Test if the get session raises exception as expected."""
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        with self.assertRaises(ValueError):
            session = Session()
            session.get_session()

    @patch('boto3.Session')
    def test_get_session_profile_not_found(self, mock_session):
        """Test if the get session raises exception as expected."""
        session_instance = mock_session.return_value
        session_instance.client.side_effect = ProfileNotFound(profile=self.profile_name)

        # Act & Assert
        with self.assertRaises(ValueError):
            session = Session(profile_name=self.profile_name)
            session.get_session()

    @patch('boto3.Session')
    def test_get_session_client_error(self, mock_session):
        """Test if the get session raises exception as expected."""
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.side_effect = ClientError(
            {'Error': {'Code': 'SomeErrorCode'}}, 'operation_name'
        )

        with self.assertRaises(ValueError):
            session = Session()
            session.get_session()

    def test_get_config(self):
        """Test if the get config works as expected."""
        config = self.session_with_profile.get_config()
        self.assertEqual(type(config), botocore.config.Config)

    @patch('pyawsopstoolkit.Session.get_session')
    def test_get_account_success(self, mock_get_session):
        """Test if the get account works as expected."""
        mock_client = MagicMock()
        mock_caller_identity = MagicMock()

        mock_caller_identity.get.return_value = '123456789012'
        mock_client.get_caller_identity.return_value = mock_caller_identity
        mock_get_session.return_value.client.return_value = mock_client

        session = Session(profile_name=self.profile_name)
        result = session.get_account()
        self.assertEqual(result.number, '123456789012')

    @patch('pyawsopstoolkit.Session.get_session')
    def test_get_account_failure(self, mock_get_session):
        """Test if the get account raises exception as expected."""
        mock_client = MagicMock()

        mock_client.get_caller_identity.side_effect = ClientError({}, 'operation_name')
        mock_get_session.return_value.client.return_value = mock_client

        session = Session(profile_name=self.profile_name)
        with self.assertRaises(ValueError):
            session.get_account()

    @patch('boto3.Session')
    def test_get_credentials_for_profile_success(self, mock_session):
        """Test if the get credentials works as expected."""
        mock_credentials = MagicMock()
        mock_credentials.access_key = 'mock_access_key'
        mock_credentials.secret_key = 'mock_secret_key'
        mock_credentials.token = 'mock_token'
        mock_session_instance = mock_session.return_value
        mock_session_instance.get_credentials.return_value = mock_credentials

        session = Session(profile_name=self.profile_name)
        result = session.get_credentials_for_profile()

        self.assertIsInstance(result, Credentials)
        self.assertEqual(result.access_key, 'mock_access_key')
        self.assertEqual(result.secret_access_key, 'mock_secret_key')
        self.assertEqual(result.token, 'mock_token')

    @patch('boto3.Session')
    def test_get_credentials_for_profile_profile_not_found(self, mock_session):
        """Test if the get credentials raises exception as expected."""
        mock_session_instance = mock_session.return_value
        mock_session_instance.get_credentials.side_effect = ProfileNotFound(profile=self.profile_name)

        session = Session(profile_name=self.profile_name)
        with self.assertRaises(ValueError):
            session.get_credentials_for_profile()

    @patch('boto3.Session')
    def test_get_credentials_for_profile_client_error(self, mock_session):
        """Test if the get credentials raises exception as expected."""
        mock_session_instance = mock_session.return_value
        mock_session_instance.get_credentials.side_effect = ClientError({}, 'operation_name')

        session = Session(profile_name=self.profile_name)
        with self.assertRaises(ValueError):
            session.get_credentials_for_profile()

    def test_get_credentials_for_profile_no_profile_name(self):
        """Test if the get credentials raises exception as expected."""
        session = Session(credentials=self.credentials)
        with self.assertRaises(ValueError):
            session.get_credentials_for_profile()

    @patch('pyawsopstoolkit.Session.get_session')
    def test_assume_role_basic(self, mock_get_session):
        """Test if the assume role works as expected."""
        mock_expiry = datetime.utcnow()
        mock_session = MagicMock()
        mock_get_session.return_value = mock_session
        mock_sts_client = MagicMock()
        mock_session.client.return_value = mock_sts_client
        mock_sts_client.assume_role.return_value = {
            'Credentials': {
                'AccessKeyId': 'mock_access_key',
                'SecretAccessKey': 'mock_secret_key',
                'SessionToken': 'mock_token',
                'Expiration': mock_expiry
            }
        }

        role_arn = 'arn:aws:iam::123456789012:role/mock-role'
        role_session_name = 'test_session'
        duration_seconds = 3600

        session = Session(profile_name=self.profile_name)
        result = session.assume_role(
            role_arn=role_arn,
            role_session_name=role_session_name,
            duration_seconds=duration_seconds
        )

        self.assertIsNotNone(result)
        mock_session.client.assert_called_once_with('sts')
        mock_sts_client.assume_role.assert_called_once_with(
            RoleArn=role_arn,
            RoleSessionName=role_session_name,
            DurationSeconds=duration_seconds
        )
        self.assertEqual(result.credentials.access_key, 'mock_access_key')
        self.assertEqual(result.credentials.secret_access_key, 'mock_secret_key')
        self.assertEqual(result.credentials.token, 'mock_token')
        self.assertEqual(result.credentials.expiry, mock_expiry)

    @patch('pyawsopstoolkit.Session.get_session')
    def test_assume_role_with_policy(self, mock_get_session):
        """Test if the assume role works as expected."""
        mock_expiry = datetime.utcnow()
        mock_session = MagicMock()
        mock_get_session.return_value = mock_session
        mock_sts_client = MagicMock()
        mock_session.client.return_value = mock_sts_client
        mock_sts_client.assume_role.return_value = {
            'Credentials': {
                'AccessKeyId': 'mock_access_key',
                'SecretAccessKey': 'mock_secret_key',
                'SessionToken': 'mock_token',
                'Expiration': mock_expiry
            }
        }

        role_arn = 'arn:aws:iam::123456789012:role/mock-role'
        role_session_name = 'test_session'
        duration_seconds = 3600
        policy_arns = ['arn:aws:iam::123456789012:policy/mock-policy']

        session = Session(profile_name=self.profile_name)
        result = session.assume_role(
            role_arn=role_arn,
            role_session_name=role_session_name,
            duration_seconds=duration_seconds,
            policy_arns=policy_arns
        )

        self.assertIsNotNone(result)
        mock_session.client.assert_called_once_with('sts')
        mock_sts_client.assume_role.assert_called_once_with(
            RoleArn=role_arn,
            RoleSessionName=role_session_name,
            DurationSeconds=duration_seconds,
            PolicyArns=policy_arns
        )
        self.assertEqual(result.credentials.access_key, 'mock_access_key')
        self.assertEqual(result.credentials.secret_access_key, 'mock_secret_key')
        self.assertEqual(result.credentials.token, 'mock_token')
        self.assertEqual(result.credentials.expiry, mock_expiry)

    @patch('pyawsopstoolkit.Session.get_session')
    def test_assume_role_with_tags(self, mock_get_session):
        """Test if the assume role works as expected."""
        mock_expiry = datetime.utcnow()
        mock_session = MagicMock()
        mock_get_session.return_value = mock_session
        mock_sts_client = MagicMock()
        mock_session.client.return_value = mock_sts_client
        mock_sts_client.assume_role.return_value = {
            'Credentials': {
                'AccessKeyId': 'mock_access_key',
                'SecretAccessKey': 'mock_secret_key',
                'SessionToken': 'mock_token',
                'Expiration': mock_expiry
            }
        }

        role_arn = 'arn:aws:iam::123456789012:role/mock-role'
        role_session_name = 'test_session'
        duration_seconds = 3600
        tags = [{'Key': 'Key1', 'Value': 'Value1'}, {'Key': 'Key2', 'Value': 'Value2'}]

        session = Session(profile_name=self.profile_name)
        result = session.assume_role(
            role_arn=role_arn,
            role_session_name=role_session_name,
            duration_seconds=duration_seconds,
            tags=tags
        )

        self.assertIsNotNone(result)
        mock_session.client.assert_called_once_with('sts')
        mock_sts_client.assume_role.assert_called_once_with(
            RoleArn=role_arn,
            RoleSessionName=role_session_name,
            DurationSeconds=duration_seconds,
            Tags=tags
        )
        self.assertEqual(result.credentials.access_key, 'mock_access_key')
        self.assertEqual(result.credentials.secret_access_key, 'mock_secret_key')
        self.assertEqual(result.credentials.token, 'mock_token')
        self.assertEqual(result.credentials.expiry, mock_expiry)

    @patch('pyawsopstoolkit.Session.get_session')
    def test_assume_role_error_handling(self, mock_get_session):
        """Test if the assume role raises exception as expected."""
        mock_session = MagicMock()
        mock_get_session.return_value = mock_session
        mock_sts_client = MagicMock()
        mock_session.client.return_value = mock_sts_client
        mock_sts_client.assume_role.side_effect = ClientError(
            error_response={'Error': {'Code': 'TestException', 'Message': 'Test error message'}},
            operation_name='AssumeRole'
        )

        role_arn = 'arn:aws:iam::123456789012:role/mock-role'
        role_session_name = 'test_session'
        duration_seconds = 3600

        session = Session(profile_name=self.profile_name)
        with self.assertRaises(AssumeRoleError) as context:
            session.assume_role(
                role_arn=role_arn, role_session_name=role_session_name, duration_seconds=duration_seconds
            )

        self.assertEqual(context.exception.role_arn, role_arn)
        self.assertIsInstance(context.exception.exception, ClientError)
        mock_session.client.assert_called_once_with('sts')
        mock_sts_client.assume_role.assert_called_once_with(
            RoleArn=role_arn,
            RoleSessionName=role_session_name,
            DurationSeconds=duration_seconds
        )


if __name__ == "__main__":
    unittest.main()
