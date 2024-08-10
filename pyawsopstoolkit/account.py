from dataclasses import dataclass


@dataclass
class Account:
    """
    Represents an AWS account with various attributes. This class implements the IAccount interface, providing basic
    functionality for managing an AWS account.
    """

    number: str

    def __post_init__(self):
        for field_name, field_value in self.__dataclass_fields__.items():
            self.__validate__(field_name)

    def __validate__(self, field_name):
        from pyawsopstoolkit_validators.account_validator import number

        field_value = getattr(self, field_name)
        if field_name in ['number']:
            number(field_value, True)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in self.__dataclass_fields__:
            self.__validate__(key)

    def to_dict(self) -> dict:
        """
        Return a dictionary representation of the Account object.

        :return: Dictionary representation of the Account object.
        :rtype: dict
        """
        return {
            "number": self.number
        }
