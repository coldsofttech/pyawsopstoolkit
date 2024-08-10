from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Union

from pyawsopstoolkit.__validations__ import _validate_type
from pyawsopstoolkit.account import Account
from pyawsopstoolkit.credentials import Credentials
from pyawsopstoolkit.exceptions import AssumeRoleError


@dataclass
class Session:
    """
    This class represents a boto3 Session with various attributes. It implements the ISession interface, offering
    functionality to manage sessions. Additionally, it provides the option to assume a session.
    """

    profile_name: Optional[str] = None
    credentials: Optional[Credentials] = None
    region_code: Optional[str] = 'eu-west-1'
    cert_path: Optional[str] = None

    def __post_init__(self):
        if (self.profile_name is not None) == (self.credentials is not None):
            raise ValueError('Either profile_name or credentials should be provided, but not both.')
        elif (self.profile_name is None) == (self.credentials is None):
            raise ValueError('At least profile_name or credentials is required.')

        for field_name, field_value in self.__dataclass_fields__.items():
            self.__validate__(field_name)

    def __validate__(self, field_name):
        from pyawsopstoolkit_validators.region_validator import region

        field_value = getattr(self, field_name)
        if field_name in ['profile_name', 'cert_path']:
            _validate_type(field_value, Union[str, None], f'{field_name} should be a string.')
        elif field_name in ['region_code']:
            region(field_value, True)
        elif field_name in ['credentials']:
            _validate_type(
                field_value, Union[Credentials, None], f'{field_name} should be of Credentials type.'
            )

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in self.__dataclass_fields__:
            self.__validate__(key)

    def get_session(self):
        """
        Returns the boto3.Session object based on the specified parameters within the class object. Priority is given
        to profile_name, followed by credentials.  This method performs a quick S3 list buckets action to verify if the
        session is valid.

        :return: The boto3 Session object based on the specified parameters within the class object.
        :rtype: boto3.Session
        """
        import boto3

        from botocore.exceptions import ClientError, ProfileNotFound

        session = None
        try:
            if self.profile_name:
                session = boto3.Session(profile_name=self.profile_name)
            elif self.credentials:
                session = boto3.Session(
                    aws_access_key_id=self.credentials.access_key,
                    aws_secret_access_key=self.credentials.secret_access_key,
                    aws_session_token=self.credentials.token
                )
            else:
                raise ValueError('At least profile_name or credentials is required.')

            if self.cert_path:
                session.client('s3', verify=self.cert_path).list_buckets()
            else:
                session.client('s3').list_buckets()
        except ProfileNotFound:
            raise ValueError(f'Profile "{self.profile_name}" not found.')
        except ClientError as e:
            if e.response['Error']['Code'] != 'AccessDenied':
                raise ValueError(f'Failed to create session: {e}.')

        return session

    def get_config(self):
        """
        Returns the botocore.config.Config based on the specified region code within the class object.

        :return: The botocore Config object based on the specified region code within the class object.
        :rtype: botocore.config.Config
        """
        from botocore.config import Config

        return Config(region_name=self.region_code)

    def get_account(self) -> Account:
        """
        Returns the AWS account number based on the get_session with specified parameters within the class object.

        :return: The AWS account number.
        :rtype: Account
        """
        from botocore.exceptions import ClientError

        session = self.get_session()
        try:
            if self.cert_path:
                account_id = session.client('sts', verify=self.cert_path).get_caller_identity().get('Account', None)
            else:
                account_id = session.client('sts').get_caller_identity().get('Account', None)
            if account_id:
                return Account(account_id)
        except ClientError as e:
            raise ValueError(f'Failed to retrieve AWS account number: {e}.')

    def get_credentials_for_profile(self) -> Credentials:
        """
        Returns the AWS credentials, i.e., access key, secret access key, and token based on the get_session with
        specified parameters within the class object.

        :return: The AWS credentials.
        :rtype: Credentials
        """
        from botocore.exceptions import ClientError, ProfileNotFound

        if self.profile_name is None:
            raise ValueError('profile_name is not set.')

        session = self.get_session()
        try:
            creds = session.get_credentials()
            return Credentials(
                access_key=creds.access_key,
                secret_access_key=creds.secret_key,
                token=creds.token
            )
        except ProfileNotFound:
            raise ValueError(f'Profile "{self.profile_name}" not found.')
        except ClientError as e:
            raise ValueError(f'Failed to retrieve AWS credentials: {e}.')

    def assume_role(
            self,
            role_arn: str,
            role_session_name: Optional[str] = 'AssumeSession',
            policy_arns: Optional[list] = None,
            policy: Optional[Union[str, dict]] = None,
            duration_seconds: Optional[int] = 3600,
            tags: Optional[list] = None
    ):
        """
        Returns the boto3.Session object for the assumed role based on the specified parameters.
        :param role_arn: The AWS ARN of the role to be assumed.
        :type role_arn: str
        :param role_session_name: Optional, The name for the AWS assumed session. Default is considered
        as 'AssumeSession'.
        :type role_session_name: str
        :param policy_arns: Optional, The list of IAM policy ARNs to attach to the assumed role session.
        :type policy_arns: list
        :param policy: Optional, The policy to be attached to the assumed role session.
        :type policy: str or dict
        :param duration_seconds: Optional, The duration (in seconds) to be set to the assumed role session.
        Default is considered as 3600 seconds.
        :type duration_seconds: int
        :param tags: Optional, The tags to be applied to the assumed role session.
        :type tags: dict
        :return: The Session object of the assumed role session.
        :rtype: ISession
        """
        from botocore.exceptions import ClientError
        from pyawsopstoolkit_validators.arn_validator import arn
        from pyawsopstoolkit_validators.policy_validator import policy as policy_val
        from pyawsopstoolkit_validators.tag_validator import tag

        arn(role_arn)
        _validate_type(role_session_name, Union[str, None], 'role_session_name should be a string.')
        _validate_type(policy_arns, Union[list, None], 'policy_arns should be list of strings.')
        if policy_arns:
            arn(policy_arns)
        if policy:
            policy_val(policy)
        _validate_type(duration_seconds, Union[int, None], 'duration_seconds should be an integer.')
        if tags:
            tag(tags)

        session = self.get_session()
        try:
            if self.cert_path:
                sts_client = session.client('sts', verify=self.cert_path)
            else:
                sts_client = session.client('sts')
            params = {
                "RoleArn": role_arn,
                "RoleSessionName": role_session_name,
                "DurationSeconds": duration_seconds
            }
            if policy_arns:
                params.update({"PolicyArns": policy_arns})
            if policy:
                params.update({"Policy": policy})
            if tags:
                params.update({"Tags": tags})
            response = sts_client.assume_role(**params)
            if response:
                creds = response.get('Credentials', {})
                if creds:
                    return Session(credentials=Credentials(
                        access_key=creds.get('AccessKeyId', ''),
                        secret_access_key=creds.get('SecretAccessKey', ''),
                        token=creds.get('SessionToken', ''),
                        expiry=creds.get('Expiration', datetime.utcnow())
                    ))
        except ClientError as e:
            raise AssumeRoleError(role_arn=role_arn, exception=e)
