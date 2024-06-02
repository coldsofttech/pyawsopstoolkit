from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Union

from pyawsopstoolkit.__interfaces__ import IAccount
from pyawsopstoolkit.__validations__ import Validation
from pyawsopstoolkit.models.iam import PermissionsBoundary
from pyawsopstoolkit.validators import Validator, ArnValidator


@dataclass
class AccessKey:
    """
    A class representing the access key information of an IAM user.
    """
    id: str
    status: str
    created_date: Optional[datetime] = None
    last_used_date: Optional[datetime] = None
    last_used_service: Optional[str] = None
    last_used_region: Optional[str] = None

    def __post_init__(self):
        for field_name, field_value in self.__dataclass_fields__.items():
            self.__validate__(field_name)

    def __validate__(self, field_name):
        field_value = getattr(self, field_name)
        if field_name in ['id', 'status']:
            Validation.validate_type(field_value, str, f'{field_name} should be a string.')
        elif field_name in ['created_date', 'last_used_date']:
            Validation.validate_type(field_value, Union[datetime, None], f'{field_name} should be a datetime.')
        elif field_name in ['last_used_service']:
            Validation.validate_type(field_value, Union[str, None], f'{field_name} should be a string.')
        elif field_name in ['last_used_region']:
            if field_value is not None:
                Validator.region(field_value, True)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in self.__dataclass_fields__:
            self.__validate__(key)

    def to_dict(self) -> dict:
        """
        Return a dictionary representation of the AccessKey object.
        :return: Dictionary representation of the AccessKey object.
        :rtype: dict
        """
        return {
            "id": self.id,
            "status": self.status,
            "created_date": self.created_date.isoformat() if self.created_date is not None else None,
            "last_used_date": self.last_used_date.isoformat() if self.last_used_date is not None else None,
            "last_used_service": self.last_used_service,
            "last_used_region": self.last_used_region
        }


@dataclass
class LoginProfile:
    """
    A class representing the login profile information of an IAM user.
    """
    created_date: Optional[datetime] = None
    password_reset_required: Optional[bool] = False

    def __post_init__(self):
        for field_name, field_value in self.__dataclass_fields__.items():
            self.__validate__(field_name)

    def __validate__(self, field_name):
        field_value = getattr(self, field_name)
        if field_name in ['created_date']:
            Validation.validate_type(field_value, Union[datetime, None], f'{field_name} should be a datetime.')
        elif field_name in ['password_reset_required']:
            Validation.validate_type(field_value, Union[bool, None], f'{field_name} should be a boolean.')

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in self.__dataclass_fields__:
            self.__validate__(key)

    def to_dict(self) -> dict:
        """
        Return a dictionary representation of the LoginProfile object.
        :return: Dictionary representation of the LoginProfile object.
        :rtype: dict
        """
        return {
            "created_date": self.created_date.isoformat() if self.created_date is not None else None,
            "password_reset_required": self.password_reset_required
        }


class User:
    """
    A class representing an IAM user.
    """

    def __init__(
            self,
            account: IAccount,
            name: str,
            id: str,
            arn: str,
            path: str = '/',
            created_date: Optional[datetime] = None,
            password_last_used_date: Optional[datetime] = None,
            permissions_boundary: Optional[PermissionsBoundary] = None,
            login_profile: Optional[LoginProfile] = None,
            access_keys: Optional[list[AccessKey]] = None,
            tags: Optional[list] = None
    ) -> None:
        """
        Initialize a new IAMUser instance.
        :param account: The account associated with the IAM user.
        :type account: IAccount
        :param name: The name of the IAM user.
        :type name: str
        :param id: The unique identifier of the IAM user.
        :type id: str
        :param arn: The Amazon Resource Name (ARN) of the IAM user.
        :type arn: str
        :param path: The path for the IAM user. Defaults to '/'
        :type path: str
        :param created_date: The creation date of the IAM user. Defaults to None.
        :type created_date: datetime
        :param password_last_used_date: Information about the last time the IAM user password was used.
        Defaults to None.
        :type password_last_used_date: datetime
        :param permissions_boundary: The permissions boundary for the IAM user. Defaults to None.
        :type permissions_boundary: PermissionsBoundary
        :param login_profile: The login profile of the IAM user. Defaults to None.
        :type login_profile: LoginProfile
        :param access_keys: A list of access keys associated with the IAM user. Defaults to None.
        :type access_keys: list
        :param tags: A list of tags associated with the IAM user. Defaults to None.
        :type tags: list
        """
        Validation.validate_type(account, IAccount, 'account should be of Account type.')
        Validation.validate_type(name, str, 'name should be a string.')
        Validation.validate_type(id, str, 'id should be a string.')
        ArnValidator.arn(arn, True)
        Validation.validate_type(path, str, 'path should be a string.')
        Validation.validate_type(created_date, Union[datetime, None], 'created_date should be a datetime.')
        Validation.validate_type(
            password_last_used_date, Union[datetime, None], 'password_last_used_date should be a datetime.'
        )
        Validation.validate_type(
            permissions_boundary,
            Union[PermissionsBoundary, None],
            'permissions_boundary should be of PermissionsBoundary type.'
        )
        Validation.validate_type(
            login_profile, Union[LoginProfile, None], 'login_profile should be of LoginProfile type.'
        )
        Validation.validate_type(access_keys, Union[list, None], 'access_keys should be a list of AccessKey.')
        if access_keys is not None and len(access_keys) > 0:
            all(
                Validation.validate_type(
                    access_key, AccessKey, 'access_keys should be a list of AccessKey.'
                ) for access_key in access_keys
            )
        Validation.validate_type(tags, Union[list, None], 'tags should be a list.')

        self._account = account
        self._name = name
        self._id = id
        self._arn = arn
        self._path = path
        self._created_date = created_date
        self._password_last_used_date = password_last_used_date
        self._permissions_boundary = permissions_boundary
        self._login_profile = login_profile
        self._access_keys = access_keys
        self._tags = tags

    @property
    def access_keys(self) -> Optional[list[AccessKey]]:
        """
        Gets the list of access keys associated with the IAM user.
        :return: The list of access keys associated with the IAM user.
        :rtype: list
        """
        return self._access_keys

    @access_keys.setter
    def access_keys(self, value: Optional[list[AccessKey]]) -> None:
        """
        Sets the list of access keys associated with the IAM user.
        :param value: The list of access keys associated with the IAM user.
        :type value: list
        """
        Validation.validate_type(value, Union[list, None], 'access_keys should be a list of AccessKey.')
        if value is not None and len(value) > 0:
            all(
                Validation.validate_type(
                    access_key, AccessKey, 'access_keys should be a list of AccessKey.'
                ) for access_key in value
            )

        self._access_keys = value

    @property
    def account(self) -> IAccount:
        """
        Gets the account associated with the IAM user.
        :return: The account associated with the IAM user.
        :rtype: IAccount
        """
        return self._account

    @account.setter
    def account(self, value: IAccount) -> None:
        """
        Sets the account associated with the IAM user.
        :param value: The account to be associated with the IAM user.
        :type value: IAccount
        """
        Validation.validate_type(value, IAccount, 'account should be of Account type.')
        self._account = value

    @property
    def arn(self) -> str:
        """
        Gets the ARN of the IAM user.
        :return: The ARN of the IAM user.
        :rtype: str
        """
        return self._arn

    @arn.setter
    def arn(self, value: str) -> None:
        """
        Sets the ARN of the IAM user.
        :param value: The ARN of the IAM user.
        :type value: str
        """
        ArnValidator.arn(value, True)
        self._arn = value

    @property
    def created_date(self) -> Optional[datetime]:
        """
        Gets the created date of the IAM user.
        :return: The created date of the IAM user.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, value: Optional[datetime]) -> None:
        """
        Sets the created date of the IAM user.
        :param value: The created date of the IAM user.
        :type value: datetime
        """
        Validation.validate_type(value, Union[datetime, None], 'created_date should be a datetime.')
        self._created_date = value

    @property
    def id(self) -> str:
        """
        Gets the ID of the IAM user.
        :return: The ID of the IAM user.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        """
        Sets the ID of the IAM user.
        :param value: The ID of the IAM user.
        :type value: str
        """
        Validation.validate_type(value, str, 'id should be a string.')
        self._id = value

    @property
    def login_profile(self) -> Optional[LoginProfile]:
        """
        Gets the login profile of the IAM user.
        :return: The login profile of the IAM user.
        :rtype: LoginProfile
        """
        return self._login_profile

    @login_profile.setter
    def login_profile(self, value: Optional[LoginProfile]) -> None:
        """
        Sets the login profile of the IAM user.
        :param value: The login profile of the IAM user.
        :type value: LoginProfile
        """
        Validation.validate_type(
            value, Union[LoginProfile, None], 'login_profile should be of LoginProfile type.'
        )

        self._login_profile = value

    @property
    def name(self) -> str:
        """
        Gets the name of the IAM user.
        :return: The name of the IAM user.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Sets the name of the IAM user.
        :param value: The name of the IAM user.
        :type value: str
        """
        Validation.validate_type(value, str, 'name should be a string.')
        self._name = value

    @property
    def password_last_used_date(self) -> Optional[datetime]:
        """
        Gets the password last used date of the IAM user.
        :return: The password last used date of the IAM user.
        :rtype: datetime
        """
        return self._password_last_used_date

    @password_last_used_date.setter
    def password_last_used_date(self, value: Optional[datetime]) -> None:
        """
        Sets the password last used date of the IAM user.
        :param value: The password last used date of the IAM user.
        :type value: datetime
        """
        Validation.validate_type(value, Union[datetime, None], 'password_last_used_date should be a datetime.')
        self._password_last_used_date = value

    @property
    def path(self) -> str:
        """
        Gets the path of the IAM user.
        :return: The path of the IAM user.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, value: str) -> None:
        """
        Sets the path of the IAM user.
        :param value: The path of the IAM user.
        :type value: str
        """
        Validation.validate_type(value, str, 'path should be a string.')
        self._path = value

    @property
    def permissions_boundary(self) -> Optional[PermissionsBoundary]:
        """
        Gets the permissions boundary associated with the IAM user.
        :return: The permissions boundary associated with the IAM user.
        :rtype: PermissionsBoundary
        """
        return self._permissions_boundary

    @permissions_boundary.setter
    def permissions_boundary(self, value: Optional[PermissionsBoundary]) -> None:
        """
        Sets the permissions boundary associated with the IAM user.
        :param value: The permissions boundary associated with the IAM user.
        :type value: PermissionsBoundary
        """
        Validation.validate_type(
            value, Union[PermissionsBoundary, None], 'permissions_boundary should be of PermissionsBoundary type.'
        )
        self._permissions_boundary = value

    @property
    def tags(self) -> Optional[list]:
        """
        Gets the tags associated with the IAM user.
        :return: The tags associated with the IAM user.
        :rtype: list
        """
        return self._tags

    @tags.setter
    def tags(self, value: Optional[list]) -> None:
        """
        Sets the tags associated with the IAM user.
        :param value: The tags associated with the IAM user.
        :type value: list
        """
        Validation.validate_type(value, Union[list, None], 'tags should be a list.')
        self._tags = value

    def __str__(self) -> str:
        """
        Return a string representation of the User object.
        :return: String representation of the User object.
        :rtype: str
        """
        account = self.account if self.account else None
        created_date = self.created_date.isoformat() if self.created_date else None
        password_last_used_date = self.password_last_used_date.isoformat() if self.password_last_used_date else None
        permissions_boundary = self.permissions_boundary if self.permissions_boundary else None
        tags = self.tags if self.tags else None
        login_profile = self.login_profile if self.login_profile else None
        access_keys = self.access_keys if self.access_keys and len(self.access_keys) > 0 else None

        return (
            f'User('
            f'account={account},'
            f'path="{self.path}",'
            f'name="{self.name}",'
            f'id="{self.id}",'
            f'arn="{self.arn}",'
            f'created_date={created_date},'
            f'password_last_used_date={password_last_used_date},'
            f'permissions_boundary={permissions_boundary},'
            f'login_profile={login_profile},'
            f'access_keys={access_keys},'
            f'tags={tags}'
            f')'
        )

    def to_dict(self) -> dict:
        """
        Return a dictionary representation of the User object.
        :return: Dictionary representation of the User object.
        :rtype: dict
        """
        account = self.account.to_dict() if self.account else None
        created_date = self.created_date.isoformat() if self.created_date else None
        password_last_used_date = self.password_last_used_date.isoformat() if self.password_last_used_date else None
        permissions_boundary = self.permissions_boundary.to_dict() if self.permissions_boundary else None
        tags = self.tags if self.tags else None
        login_profile = self.login_profile.to_dict() if self.login_profile else None
        access_keys = [
            key.to_dict() for key in self.access_keys
        ] if self.access_keys and len(self.access_keys) > 0 else None

        return {
            "account": account,
            "path": self.path,
            "name": self.name,
            "id": self.id,
            "arn": self.arn,
            "created_date": created_date,
            "password_last_used_date": password_last_used_date,
            "permissions_boundary": permissions_boundary,
            "login_profile": login_profile,
            "access_keys": access_keys,
            "tags": tags
        }
