# pyawsopstoolkit.models.iam

The **pyawsopstoolkit.models.iam** subpackage, part of the AWS Ops Toolkit Models, provides specialized data model
classes
specifically designed for the Identity and Access Management (IAM) service of AWS (Amazon Web Services). These models
facilitate efficient handling and manipulation of IAM resources, ensuring seamless integration and interaction with AWS
IAM functionalities.

## PermissionsBoundary

A class representing an IAM role permissions boundary.

### Constructors

- `PermissionsBoundary(type: str, arn: str) -> None`: Initializes a **PermissionsBoundary** object with the specified
  type and Amazon Resource Name (ARN).

### Methods

- `__str__() -> str`: Returns a string representation of the **PermissionsBoundary** object.
- `to_dict() -> dict`: Returns a dictionary representation of the **PermissionsBoundary** object.

### Properties

- `arn`: The Amazon Resource Name (ARN) of the permissions boundary.
- `type`: The type of the permissions boundary.

## Additional IAM Models

### pyawsopstoolkit.models.iam.role

For detailed information and usage examples about IAM roles, please refer to the [ROLE](iam/ROLE.md).

### pyawsopstoolkit.models.iam.user

For detailed information and usage examples about IAM users, please refer to the [USER](iam/USER.md).