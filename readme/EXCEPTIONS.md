# pyawsopstoolkit.exceptions

This package offers a collection of exception classes tailored for handling errors within the AWS Ops Toolkit. These
exceptions are specifically designed to address different scenarios and errors that may occur during the execution of
pyawsopstoolkit operations, providing comprehensive support for error handling and debugging within the toolkit.

# Documentation

## AdvanceSearchError

Custom exception class designed for AWS Ops Toolkit. This exception is typically raised when there's a failure during
advance search.

### Constructors

- `AdvanceSearchError(message: str, exception: Optional[Exception] = None) -> None`: Constructor for the
  SearchAttributeError
  class.

## AssumeRoleError

Custom exception class designed for AWS Ops Toolkit. This exception is typically raised when there's a failure during
the assumption of a role session.

### Constructors

- `AssumeRoleError(role_arn: str, exception: Optional[Exception] = None) -> None`: Constructor for the AssumeRoleError
  class.

## SearchAttributeError

Custom exception class designed for AWS Ops Toolkit. This exception is typically raised when either invalid attributes
are provided or key attributes are missing.

### Constructors

- `SearchAttributeError(message: str, exception: Optional[Exception] = None) -> None`: Constructor for the
  SearchAttributeError
  class.

## ValidationError

Custom exception class designed for AWS Ops Toolkit. This exception is typically raised when there's a failure during
validation.

### Constructors

- `ValidationError(message: str, exception: Optional[Exception] = None) -> None`: Constructor for the ValidationError
  class.