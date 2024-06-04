from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Union

_property_message: str = 'This property should be implemented in child class.'
_method_message: str = 'This method should be implemented in child class.'


@dataclass
class ICredentials(ABC):
    """
    This module serves as an interface for implementing the Credentials class, providing a blueprint
    for defining the structure and behavior of credential management within the application.
    """
    access_key: str
    secret_access_key: str
    token: Optional[str] = None
    expiry: Optional[datetime] = None

    @abstractmethod
    def to_dict(self) -> dict:
        raise NotImplementedError(_method_message)


@dataclass
class IAccount(ABC):
    """
    This module serves as an interface for implementing the Account class, offering a blueprint for defining
    the structure and behavior of an AWS account within the application.
    """
    number: str

    @abstractmethod
    def to_dict(self) -> dict:
        raise NotImplementedError(_method_message)


class ISession(ABC):
    """
    This module serves as an interface for implementing the Session class, providing a blueprint for defining
    the structure and behavior of AWS session management within the application.
    """

    @abstractmethod
    def __init__(
            self,
            profile_name: Optional[str] = None,
            credentials: Optional[ICredentials] = None,
            region_code: Optional[str] = 'eu-west-1'
    ) -> None:
        raise NotImplementedError(_method_message)

    @property
    @abstractmethod
    def profile_name(self) -> str:
        raise NotImplementedError(_property_message)

    @profile_name.setter
    @abstractmethod
    def profile_name(self, value: Optional[str] = None) -> None:
        raise NotImplementedError(_property_message)

    @property
    @abstractmethod
    def credentials(self) -> ICredentials:
        raise NotImplementedError(_property_message)

    @credentials.setter
    @abstractmethod
    def credentials(self, value: Optional[ICredentials] = None) -> None:
        raise NotImplementedError(_property_message)

    @property
    @abstractmethod
    def region_code(self) -> str:
        raise NotImplementedError(_property_message)

    @region_code.setter
    @abstractmethod
    def region_code(self, value: Optional[str] = 'eu-west-1') -> None:
        raise NotImplementedError(_property_message)

    @abstractmethod
    def get_session(self):
        raise NotImplementedError(_method_message)

    @abstractmethod
    def get_config(self):
        raise NotImplementedError(_method_message)

    @abstractmethod
    def get_account(self) -> IAccount:
        raise NotImplementedError(_method_message)

    @abstractmethod
    def get_credentials_for_profile(self) -> ICredentials:
        raise NotImplementedError(_method_message)

    @abstractmethod
    def assume_role(
            self,
            role_arn: str,
            role_session_name: Optional[str] = 'AssumeSession',
            policy_arns: Optional[list] = None,
            policy: Optional[Union[str, dict]] = None,
            duration_seconds: Optional[int] = 3600,
            tags: Optional[list] = None
    ):
        raise NotImplementedError(_method_message)
