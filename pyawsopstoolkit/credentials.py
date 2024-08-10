from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Union

from pyawsopstoolkit.__validations__ import _validate_type


@dataclass
class Credentials:
    """
    Represents a set of credentials including an access key, secret access key, token, and optional expiry datetime.
    """

    access_key: str
    secret_access_key: str
    token: Optional[str] = None
    expiry: Optional[datetime] = None

    def __post_init__(self):
        for field_name, field_value in self.__dataclass_fields__.items():
            self.__validate__(field_name)

    def __validate__(self, field_name):
        field_value = getattr(self, field_name)
        if field_name in ['access_key', 'secret_access_key']:
            _validate_type(field_value, str, f'{field_name} should be a string.')
        elif field_name in ['token']:
            _validate_type(field_value, Union[str, None], f'{field_name} should be a string.')
        elif field_name in ['expiry']:
            _validate_type(field_value, Union[datetime, None], f'{field_name} should be a datetime.')

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in self.__dataclass_fields__:
            self.__validate__(key)

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of Credentials object.

        :return: Dictionary representation of Credentials object.
        :rtype: dict
        """
        return {
            "access_key": self.access_key,
            "secret_access_key": self.secret_access_key,
            "token": self.token if self.token is not None else None,
            "expiry": self.expiry.isoformat() if self.expiry is not None else None
        }
