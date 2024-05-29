import unittest
from datetime import datetime
from unittest.mock import patch, MagicMock

import botocore.config
from botocore.exceptions import ProfileNotFound, ClientError

from pyawsopstoolkit import Credentials, Session
from pyawsopstoolkit.exceptions import AssumeRoleError


class TestSession(unittest.TestCase):
    """Unit test cases for Session."""

    def setUp(self) -> None:
        self.profile_name = 'temp'
        self.credentials = Credentials('access_key', 'secret_access_key', 'token')
        self.region_code = 'us-east-1'
        self.session_with_profile = Session(profile_name=self.profile_name)
        self.session_with_creds = Session(credentials=self.credentials)

    def test_initialization_empty(self):
        with self.assertRaises(ValueError):
            Session()

    def test_initialization_with_profile_and_credentials(self):
        with self.assertRaises(ValueError):
            Session(profile_name=self.profile_name, credentials=self.credentials)

    def test_initialization_with_profile(self):
        self.assertEqual(self.session_with_profile.profile_name, self.profile_name)
        self.assertIsNone(self.session_with_profile.credentials)
        self.assertEqual(self.session_with_profile.region_code, 'eu-west-1')

    def test_initialization_with_credentials(self):
        self.assertIsNone(self.session_with_creds.profile_name)
        self.assertEqual(self.session_with_creds.credentials, self.credentials)
        self.assertEqual(self.session_with_creds.region_code, 'eu-west-1')

    def test_set_profile_name(self):
        new_profile_name = 'sample'
        self.session_with_profile.profile_name = new_profile_name
        self.assertEqual(self.session_with_profile.profile_name, new_profile_name)

    def test_set_credentials(self):
        new_credentials = Credentials('new_access_key', 'new_secret_access_key', 'new_token')
        self.session_with_creds.credentials = new_credentials
        self.assertEqual(self.session_with_creds.credentials, new_credentials)

    def test_set_region_code(self):
        new_region = 'us-east-2'
        self.session_with_creds.region_code = new_region
        self.assertEqual(self.session_with_creds.region_code, new_region)

    @patch('boto3.Session')
    def test_get_session_with_profile_name(self, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        self.assertIsNotNone(self.session_with_profile.get_session())
        mock_session.assert_called_once_with(profile_name=self.profile_name)

    @patch('boto3.Session')
    def test_get_session_with_credentials(self, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        self.assertIsNotNone(self.session_with_creds.get_session())
        mock_session.assert_called_once_with(
            aws_access_key_id=self.credentials.access_key,
            aws_secret_access_key=self.credentials.secret_access_key,
            aws_session_token=self.credentials.token
        )

    @patch('boto3.Session')
    def test_get_session_with_no_profile_or_credentials(self, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.return_value = {}

        with self.assertRaises(ValueError):
            session = Session()
            session.get_session()

    @patch('boto3.Session')
    def test_get_session_profile_not_found(self, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.side_effect = ProfileNotFound(profile=self.profile_name)

        with self.assertRaises(ValueError):
            self.session_with_profile.get_session()

    @patch('boto3.Session')
    def test_get_session_client_error(self, mock_session):
        session_instance = mock_session.return_value
        session_instance.client.return_value.list_buckets.side_effect = ClientError(
            {'Error': {'Code': 'SomeErrorCode'}}, 'operation_name'
        )

        with self.assertRaises(ValueError):
            session = Session()
            session.get_session()

    def test_get_config(self):
        self.assertEqual(type(self.session_with_profile.get_config()), botocore.config.Config)

    @patch('pyawsopstoolkit.Session.get_session')
    def test_get_account_success(self, mock_get_session):
        mock_client = MagicMock()
        mock_caller_identity = MagicMock()
        mock_caller_identity.get.return_value = '123456789012'
        mock_client.get_caller_identity.return_value = mock_caller_identity
        mock_get_session.return_value.client.return_value = mock_client

        self.assertEqual(self.session_with_profile.get_account().number, '123456789012')

    @patch('pyawsopstoolkit.Session.get_session')
    def test_get_account_failure(self, mock_get_session):
        mock_client = MagicMock()
        mock_client.get_caller_identity.side_effect = ClientError({}, 'operation_name')
        mock_get_session.return_value.client.return_value = mock_client

        with self.assertRaises(ValueError):
            self.session_with_profile.get_account()

    @patch('boto3.Session')
    def test_get_credentials_for_profile_success(self, mock_session):
        mock_credentials = MagicMock()
        mock_credentials.access_key = 'mock_access_key'
        mock_credentials.secret_key = 'mock_secret_key'
        mock_credentials.token = 'mock_token'
        mock_session_instance = mock_session.return_value
        mock_session_instance.get_credentials.return_value = mock_credentials

        result = self.session_with_profile.get_credentials_for_profile()

        self.assertIsInstance(result, Credentials)
        self.assertEqual(result.access_key, 'mock_access_key')
        self.assertEqual(result.secret_access_key, 'mock_secret_key')
        self.assertEqual(result.token, 'mock_token')

    @patch('boto3.Session')
    def test_get_credentials_for_profile_profile_not_found(self, mock_session):
        mock_session_instance = mock_session.return_value
        mock_session_instance.get_credentials.side_effect = ProfileNotFound(profile=self.profile_name)

        with self.assertRaises(ValueError):
            self.session_with_profile.get_credentials_for_profile()

    @patch('boto3.Session')
    def test_get_credentials_for_profile_client_error(self, mock_session):
        mock_session_instance = mock_session.return_value
        mock_session_instance.get_credentials.side_effect = ClientError({}, 'operation_name')

        with self.assertRaises(ValueError):
            self.session_with_profile.get_credentials_for_profile()

    def test_get_credentials_for_profile_no_profile_name(self):
        with self.assertRaises(ValueError):
            self.session_with_creds.get_credentials_for_profile()

    @patch('pyawsopstoolkit.Session.get_session')
    def test_assume_role_basic(self, mock_get_session):
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

        result = self.session_with_profile.assume_role(
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

        result = self.session_with_profile.assume_role(
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

        result = self.session_with_profile.assume_role(
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

        with self.assertRaises(AssumeRoleError) as context:
            self.session_with_profile.assume_role(
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
