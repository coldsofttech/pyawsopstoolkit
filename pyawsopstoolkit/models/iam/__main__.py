from pyawsopstoolkit.__validations__ import Validation
from pyawsopstoolkit.validators import ArnValidator


class PermissionsBoundary:
    """
    A class representing an IAM role permissions boundary.
    """

    def __init__(self, type: str, arn: str) -> None:
        """
        Initialize the PermissionsBoundary object.
        :param type: The type of the permissions boundary.
        :type type: str
        :param arn: The Amazon Resource Name (ARN) of the permissions boundary.
        :type arn: str
        """
        Validation.validate_type(type, str, 'type should be a string.')
        ArnValidator.arn(arn, True)

        self._type = type
        self._arn = arn

    @property
    def arn(self) -> str:
        """
        Gets the ARN of the permissions boundary.
        :return: The ARN of the permissions boundary.
        :rtype: str
        """
        return self._arn

    @arn.setter
    def arn(self, value: str) -> None:
        """
        Sets the ARN of the permissions boundary.
        :param value: The new ARN of the permissions boundary.
        :type value: str
        """
        ArnValidator.arn(value, True)
        self._arn = value

    @property
    def type(self) -> str:
        """
        Gets the type of the permissions boundary.
        :return: The type of the permissions boundary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        """
        Sets the type of the permissions boundary.
        :param value: The new type of the permissions boundary.
        :type value: str
        """
        Validation.validate_type(value, str, 'type should be a string.')
        self._type = value

    def __str__(self) -> str:
        """
        Return a string representation of the PermissionsBoundary object.
        :return: String representation of the PermissionsBoundary object.
        :rtype: str
        """
        return (
            f'PermissionsBoundary('
            f'type="{self.type}",'
            f'arn="{self.arn}"'
            f')'
        )

    def to_dict(self) -> dict:
        """
        Return a dictionary representation of the PermissionsBoundary object.
        :return: Dictionary representation of the PermissionsBoundary object.
        :rtype: dict
        """
        return {
            "type": self.type,
            "arn": self.arn
        }
