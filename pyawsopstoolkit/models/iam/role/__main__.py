from datetime import datetime
from typing import Optional, Union

from pyawsopstoolkit.__interfaces__ import IAccount
from pyawsopstoolkit.__validations__ import Validation
from pyawsopstoolkit.models.iam.__main__ import PermissionsBoundary
from pyawsopstoolkit.validators import Validator, ArnValidator


class LastUsed:
    """
    A class representing the last used information of an IAM role.
    """

    def __init__(self, used_date: Optional[datetime] = None, region: Optional[str] = None) -> None:
        """
        Initializes the LastUsed instance with optional used_date and region.
        :param used_date: The last date and time the IAM role was used.
        :type used_date: datetime
        :param region: The AWS region where the IAM role was last used.
        :type region: str
        """
        Validation.validate_type(used_date, Union[datetime, None], 'used_date should be a datetime.')

        if region is not None:
            Validator.region(region, True)

        self._used_date = used_date
        self._region = region

    @property
    def region(self) -> Optional[str]:
        """
        Gets the AWS region where the IAM role was last used.
        :return: The AWS region where the IAM role was last used.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, value: Optional[str]) -> None:
        """
        Sets the AWS region where the IAM role was last used.
        :param value: The AWS region to set.
        :type value: str
        """
        if value is not None:
            Validator.region(value, True)
        self._region = value

    @property
    def used_date(self) -> Optional[datetime]:
        """
        Gets the last date and time the IAM role was used.
        :return: The last date and time the IAM role was used.
        :rtype: datetime
        """
        return self._used_date

    @used_date.setter
    def used_date(self, value: Optional[datetime]) -> None:
        """
        Sets the last date and time the IAM role was used.
        :param value: The last date and time to set.
        :type value: datetime
        """
        Validation.validate_type(value, Union[datetime, None], 'used_date should be a datetime.')
        self._used_date = value

    def __str__(self) -> str:
        """
        Returns a string representation of the LastUsed instance.
        :return: String representation of the LastUsed instance.
        :rtype: str
        """
        used_date = self.used_date.isoformat() if self.used_date else None
        region = self.region if self.region else None

        return (
            f'LastUsed('
            f'used_date={used_date},'
            f'region="{region}"'
            f')'
        )

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the LastUsed instance.
        :return: Dictionary representation of the LastUsed instance.
        :rtype: dict
        """
        used_date = self.used_date.isoformat() if self.used_date else None
        region = self.region if self.region else None

        return {
            "used_date": used_date,
            "region": region
        }


class Role:
    """
    A class representing an IAM role.
    """

    def __init__(
            self,
            account: IAccount,
            name: str,
            id: str,
            arn: str,
            max_session_duration: int,
            path: str = '/',
            created_date: Optional[datetime] = None,
            assume_role_policy_document: Optional[dict] = None,
            description: Optional[str] = None,
            permissions_boundary: Optional[PermissionsBoundary] = None,
            last_used: Optional[LastUsed] = None,
            tags: Optional[list] = None
    ) -> None:
        """
        Initialize a new IAMRole instance.
        :param account: The account associated with the IAM role.
        :type account: IAccount
        :param name: The name of the IAM role.
        :type name: str
        :param id: The unique identifier of the IAM role.
        :type id: str
        :param arn: The Amazon Resource Name (ARN) of the IAM role.
        :type arn: str
        :param max_session_duration: The maximum session duration for the IAM role.
        :type max_session_duration: int
        :param path: The path for the IAM role. Defaults to '/'.
        :type path: str
        :param created_date: The creation date of the IAM role. Defaults to None.
        :type created_date: datetime
        :param assume_role_policy_document: The policy document for assuming the IAM role. Defaults to None.
        :type assume_role_policy_document: dict
        :param description: A description of the IAM role. Defaults to None.
        :type description: str
        :param permissions_boundary: The permissions boundary for the IAM role. Defaults to None.
        :type permissions_boundary: PermissionsBoundary
        :param last_used: Information about the last time the IAM role was used. Defaults to None.
        :type last_used: LastUsed
        :param tags: A list of tags associated with the IAM role. Defaults to None.
        :type tags: list
        """
        Validation.validate_type(account, IAccount, 'account should be of Account type.')
        Validation.validate_type(name, str, 'name should be a string.')
        Validation.validate_type(id, str, 'id should be a string.')
        ArnValidator.arn(arn, True)
        Validation.validate_type(max_session_duration, int, 'max_session_duration should be an integer.')
        Validation.validate_type(path, str, 'path should be a string.')
        Validation.validate_type(created_date, Union[datetime, None], 'created_date should be a datetime.')
        Validation.validate_type(
            assume_role_policy_document, Union[dict, None], 'assume_role_policy_document should be a dictionary.'
        )
        Validation.validate_type(description, Union[str, None], 'description should be a string.')
        Validation.validate_type(
            permissions_boundary,
            Union[PermissionsBoundary, None],
            'permissions_boundary should be of PermissionsBoundary type.'
        )
        Validation.validate_type(
            last_used, Union[LastUsed, None], 'last_used should be of LastUsed type.'
        )
        Validation.validate_type(tags, Union[list, None], 'tags should be a list.')

        self._account = account
        self._name = name
        self._id = id
        self._arn = arn
        self._max_session_duration = max_session_duration
        self._path = path
        self._created_date = created_date
        self._assume_role_policy_document = assume_role_policy_document
        self._description = description
        self._permissions_boundary = permissions_boundary
        self._last_used = last_used
        self._tags = tags

    @property
    def account(self) -> IAccount:
        """
        Gets the account associated with the IAM role.
        :return: The account associated with the IAM role.
        :rtype: IAccount
        """
        return self._account

    @account.setter
    def account(self, value: IAccount) -> None:
        """
        Sets the account associated with the IAM role.
        :param value: The account to be associated with the IAM role.
        :type value: IAccount
        """
        Validation.validate_type(value, IAccount, 'account should be of Account type.')
        self._account = value

    @property
    def arn(self) -> str:
        """
        Gets the ARN of the IAM role.
        :return: The ARN of the IAM role.
        :rtype: str
        """
        return self._arn

    @arn.setter
    def arn(self, value: str) -> None:
        """
        Sets the ARN of the IAM role.
        :param value: The ARN of the IAM role.
        :type value: str
        """
        ArnValidator.arn(value, True)
        self._arn = value

    @property
    def assume_role_policy_document(self) -> Optional[dict]:
        """
        Gets the trust relationship (or) assume role policy document associated with the IAM role.
        :return: The trust relationship (or) assume role policy document associated with the IAM role.
        :rtype: dict
        """
        return self._assume_role_policy_document

    @assume_role_policy_document.setter
    def assume_role_policy_document(self, value: Optional[dict] = None) -> None:
        """
        Sets the trust relationship (or) assume role policy document associated with the IAM role.
        :param value: The trust relationship (or) assume role policy document associated with the IAM role.
        :type value: dict
        """
        Validation.validate_type(value, Union[dict, None], 'assume_role_policy_document should be a dictionary.')
        self._assume_role_policy_document = value

    @property
    def created_date(self) -> Optional[datetime]:
        """
        Gets the created date of the IAM role.
        :return: The created date of the IAM role.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, value: Optional[datetime] = None) -> None:
        """
        Sets the created date of the IAM role.
        :param value: The created date of the IAM role.
        :type value: datetime
        """
        Validation.validate_type(value, Union[datetime, None], 'created_date should be a datetime.')
        self._created_date = value

    @property
    def description(self) -> Optional[str]:
        """
        Gets the description of the IAM role.
        :return: The description of the IAM role.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, value: Optional[str] = None) -> None:
        """
        Sets the description of the IAM role.
        :param value: The description of the IAM role.
        :type value: str
        """
        Validation.validate_type(value, Union[str, None], 'description should be a string.')
        self._description = value

    @property
    def id(self) -> str:
        """
        Gets the ID of the IAM role.
        :return: The ID of the IAM role.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        """
        Sets the ID of the IAM role.
        :param value: The ID of the IAM role.
        :type value: str
        """
        Validation.validate_type(value, str, 'id should be a string.')
        self._id = value

    @property
    def last_used(self) -> Optional[LastUsed]:
        """
        Gets the last used date of the IAM role.
        :return: The last used date of the IAM role.
        :rtype: LastUsed
        """
        return self._last_used

    @last_used.setter
    def last_used(self, value: Optional[LastUsed] = None) -> None:
        """
        Sets the last used date of the IAM role.
        :param value: The last used date of the IAM role.
        :type value: LastUsed
        """
        Validation.validate_type(value, Union[LastUsed, None], 'last_used should be of LastUsed type.')
        self._last_used = value

    @property
    def max_session_duration(self) -> int:
        """
        Gets the maximum session duration of the IAM role.
        :return: The maximum session duration of the IAM role.
        :rtype: int
        """
        return self._max_session_duration

    @max_session_duration.setter
    def max_session_duration(self, value: int) -> None:
        """
        Sets the maximum session duration of the IAM role.
        :param value: The maximum session duration of the IAM role.
        :type value: int
        """
        Validation.validate_type(value, int, 'max_session_duration should be an integer.')
        self._max_session_duration = value

    @property
    def name(self) -> str:
        """
        Gets the name of the IAM role.
        :return: The name of the IAM role.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Sets the name of the IAM role.
        :param value: The name of the IAM role.
        :type value: str
        """
        Validation.validate_type(value, str, 'name should be a string.')
        self._name = value

    @property
    def path(self) -> str:
        """
        Gets the path of the IAM role.
        :return: The path of the IAM role.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, value: str = '/') -> None:
        """
        Sets the path of the IAM role.
        :param value: The path of the IAM role.
        :type value: str
        """
        Validation.validate_type(value, str, 'path should be a string.')
        self._path = value

    @property
    def permissions_boundary(self) -> Optional[PermissionsBoundary]:
        """
        Gets the permissions boundary associated with the IAM role.
        :return: The permissions boundary associated with the IAM role.
        :rtype: PermissionsBoundary
        """
        return self._permissions_boundary

    @permissions_boundary.setter
    def permissions_boundary(self, value: Optional[PermissionsBoundary] = None) -> None:
        """
        Sets the permissions boundary associated with the IAM role.
        :param value: The permissions boundary associated with the IAM role.
        :type value: IAMPermissionsBoundary
        """
        Validation.validate_type(
            value, Union[PermissionsBoundary, None], 'permissions_boundary should be of PermissionsBoundary type.'
        )
        self._permissions_boundary = value

    @property
    def tags(self) -> Optional[list]:
        """
        Gets the tags associated with the IAM role.
        :return: The tags associated with the IAM role.
        :rtype: list
        """
        return self._tags

    @tags.setter
    def tags(self, value: Optional[list] = None) -> None:
        """
        Sets the tags associated with the IAM role.
        :param value: The tags associated with the IAM role.
        :type value: list
        """
        Validation.validate_type(value, Union[list, None], 'tags should be a list.')
        self._tags = value

    def __str__(self) -> str:
        """
        Return a string representation of the Role object.
        :return: String representation of the Role object.
        :rtype: str
        """
        account = self.account if self.account else None
        created_date = self.created_date.isoformat() if self.created_date else None
        assume_role_policy_document = self.assume_role_policy_document if self.assume_role_policy_document else None
        description = self.description if self.description else None
        last_used = self.last_used if self.last_used else None
        permissions_boundary = self.permissions_boundary if self.permissions_boundary else None
        tags = self.tags if self.tags else None

        return (
            f'Role('
            f'account={account},'
            f'path="{self.path}",'
            f'name="{self.name}",'
            f'id="{self.id}",'
            f'arn="{self.arn}",'
            f'created_date={created_date},'
            f'assume_role_policy_document={assume_role_policy_document},'
            f'description="{description}",'
            f'max_session_duration={self.max_session_duration},'
            f'permissions_boundary={permissions_boundary},'
            f'last_used={last_used},'
            f'tags={tags}'
            f')'
        )

    def to_dict(self) -> dict:
        """
        Return a dictionary representation of the Role object.
        :return: Dictionary representation of the Role object.
        :rtype: dict
        """
        account = self.account.to_dict() if self.account else None
        created_date = self.created_date.isoformat() if self.created_date else None
        assume_role_policy_document = self.assume_role_policy_document if self.assume_role_policy_document else None
        description = self.description if self.description else None
        last_used = self.last_used.to_dict() if self.last_used else None
        permissions_boundary = self.permissions_boundary.to_dict() if self.permissions_boundary else None
        tags = self.tags if self.tags else None

        return {
            "account": account,
            "path": self.path,
            "name": self.name,
            "id": self.id,
            "arn": self.arn,
            "created_date": created_date,
            "assume_role_policy_document": assume_role_policy_document,
            "description": description,
            "max_session_duration": self.max_session_duration,
            "permissions_boundary": permissions_boundary,
            "last_used": last_used,
            "tags": tags
        }