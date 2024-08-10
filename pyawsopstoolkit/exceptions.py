from typing import Optional, Union

from pyawsopstoolkit.__validations__ import _validate_type


class AssumeRoleError(Exception):
    """
    Custom exception class designed for AWS Ops Toolkit.
    This exception is typically raised when there's a failure during the assumption of a role session.
    """

    def __init__(
            self,
            role_arn: str,
            exception: Optional[Exception] = None
    ) -> None:
        """
        Constructor for the AssumeRoleError class.

        :param role_arn: The Amazon Resource Name (ARN) of the role.
        :type role_arn: str
        :param exception: The exception that occurred, if any.
        :type exception: Exception
        """
        _validate_type(role_arn, str, 'role_arn should be a string.')
        _validate_type(exception, Union[Exception, None], 'exception should be of Exception type.')

        self._role_arn = role_arn
        self._exception = exception
        self._message = f'ERROR: Unable to assume role "{role_arn}".{f" {exception}." if exception else ""}'
        super().__init__(self._message)

    @property
    def exception(self) -> Optional[Exception]:
        """
        Getter for exception attribute.

        :return: The exception that occurred, if any.
        :rtype: Exception
        """
        return self._exception

    @property
    def message(self) -> str:
        """
        Getter for message attribute.

        :return: The error message.
        :rtype: str
        """
        return self._message

    @property
    def role_arn(self) -> str:
        """
        Getter for role_arn attribute.

        :return: The Amazon Resource Name (ARN) of the role.
        :rtype: str
        """
        return self._role_arn
