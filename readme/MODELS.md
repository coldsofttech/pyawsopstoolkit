# pyawsopstoolkit.models

This package provides a comprehensive collection of data model classes specifically designed for various AWS Ops Toolkit
packages, such as finops and advsearch. These models are meticulously crafted to align closely with AWS services and
their respective properties, ensuring seamless integration and optimal performance.

## IAMRolePermissionsBoundary

A class representing an IAM role permissions boundary.

### Methods

- `__init__(self, type: str, arn: str) -> None`: Initialize the IAMRolePermissionsBoundary object.
-
    - `__str__(self) -> str`: Returns a string representation of the **IAMRolePermissionsBoundary** object.
- `__dict__(self) -> dict`: Returns a dictionary representation of the **IAMRolePermissionsBoundary** object.

### Properties

- `arn`: The ARN of the permissions boundary.
- `type`: The type of the permissions boundary.

## IAMRoleLastUsed

A class representing the last used information of an IAM role.

### Methods

- `__init__(self, used_date: Optional[datetime] = None, region: Optional[str] = None) -> None`: Initializes the
  IAMRoleLastUsed instance with optional used_date and region.
-
    -
        - `__str__(self) -> str`: Returns a string representation of the **IAMRoleLastUsed** object.
- `__dict__(self) -> dict`: Returns a dictionary representation of the **IAMRoleLastUsed** object.

### Properties

- `region`: The AWS region where the IAM role was last used.
- `used_date`: The last date and time the IAM role was used.

## IAMRole

A class representing an IAM role.

### Methods

- `__init__(self, account: IAccount, name: str, id: str, arn: str, max_session_duration: int, path: str = '/', created_date: Optional[datetime] = None, assume_role_policy_document: Optional[dict] = None, description: Optional[str] = None, permissions_boundary: Optional[IAMRolePermissionsBoundary] = None, last_used: Optional[IAMRoleLastUsed] = None, tags: Optional[list] = None) -> None`:
  Initialize a new IAMRole instance.
-
    -
        - `__str__(self) -> str`: Returns a string representation of the **IAMRole** object.
- `__dict__(self) -> dict`: Returns a dictionary representation of the **IAMRole** object.

### Properties

- `account`: The account associated with the IAM role.
- `arn`: The ARN of the IAM role.
- `assume_role_policy_document`: The trust relationship (or) assume role policy document associated with the IAM role.
- `created_date`: The created date of the IAM role.
- `description`: The description of the IAM role.
- `id`: The ID of the IAM role.
- `last_used`: The last used date of the IAM role.
- `max_session_duration`: The maximum session duration of the IAM role.
- `name`: The name of the IAM role.
- `path`: The path of the IAM role.
- `permissions_boundary`: The permissions boundary associated with the IAM role.
- `tags`: The tags associated with the IAM role.
