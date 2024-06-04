# pyawsopstoolkit.models.iam.role

This subpackage within **pyawsopstoolkit.models.iam** (AWS Ops Toolkit Models) provides specialized data model classes
designed for managing Identity and Access Management (IAM) roles in Amazon Web Services (AWS). These models are crafted
to facilitate the efficient handling, manipulation, and integration of IAM roles, ensuring seamless interaction with AWS
services.

## LastUsed

The `LastUsed` class encapsulates the information regarding the last time an IAM role was used.

### Constructors

- `LastUsed(used_date: Optional[datetime] = None, region: Optional[str] = None) -> None`: Initializes a new **LastUsed**
  instance with optional parameters for the date and time the IAM role was last used and the AWS region where it was
  used.

### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **LastUsed** object.

### Properties

- `region`: The AWS region where the IAM role was last used.
- `used_date`: The last date and time the IAM role was used.

## Role

The `Role` class represents an IAM role in AWS, encompassing various attributes and methods to manage the role
effectively.

### Constructors

- `Role(account: IAccount, name: str, id: str, arn: str, max_session_duration: int, path: str = '/', created_date: Optional[datetime] = None, assume_role_policy_document: Optional[dict] = None, description: Optional[str] = None, permissions_boundary: Optional[PermissionsBoundary] = None, last_used: Optional[LastUsed] = None, tags: Optional[list] = None) -> None`:
  Initializes a new **Role** instance with comprehensive parameters to define the IAM role, including account details,
  role name, ID, ARN, session duration, path, creation date, assume role policy, description, permissions boundary, last
  used information, and associated tags.

### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **Role** object.

### Properties

- `account`: The AWS account associated with the IAM role.
- `arn`: The Amazon Resource Name (ARN) of the IAM role.
- `assume_role_policy_document`: The trust relationship or assume role policy document defining the permissions for
  assuming the IAM role.
- `created_date`: The created date of the IAM role.
- `description`: A brief description of the IAM role.
- `id`: The unique identifier of the IAM role.
- `last_used`: An instance of `LastUsed` representing the last time the IAM role was utilized.
- `max_session_duration`: The maximum duration (in seconds) for which the IAM role can be assumed in a single session.
- `name`: The name of the IAM role.
- `path`: The path under which the IAM role is created, useful for organizational purposes.
- `permissions_boundary`: An optional permissions boundary that defines the maximum permissions the IAM role can have.
- `tags`: A list of tags associated with the IAM role for categorization and identification purposes.