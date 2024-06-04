# pyawsopstoolkit.models.iam.user

This subpackage within **pyawsopstoolkit.models.iam** (AWS Ops Toolkit Models) provides specialized data model classes
designed for managing Identity and Access Management (IAM) users in Amazon Web Services (AWS). These models are crafted
to facilitate the efficient handling, manipulation, and integration of IAM users, ensuring seamless interaction with AWS
services.

## AccessKey

A class representing the access key information of an IAM user.

### Constructors

- `AccessKey(id: str, status: str, created_date: Optional[datetime] = None, last_used_date: Optional[datetime] = None, last_used_service: Optional[str] = None, last_used_region: Optional[str] = None) -> None`:
  Initializes a new **AccessKey** object with the specified parameters.

### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **AccessKey** object.

### Properties

- `created_date`: The creation date of the IAM user access key.
- `id`: The unique identifier of the IAM user access key.
- `last_used_date`: The last usage date of the IAM user access key.
- `last_used_region`: The AWS region where the IAM user access key was last used.
- `last_used_service`: The AWS service where the IAM user access key was last used.
- `status`: The current status of the IAM user access key (e.g., Active, Inactive).

## LoginProfile

A class representing the login profile information of an IAM user.

### Constructors

- `LoginProfile(created_date: Optional[datetime] = None, password_reset_required: Optional[bool] = False) -> None`:
  Initializes a new **LoginProfile** object with the specified parameters.

### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **LoginProfile** object.

### Properties

- `created_date`: The creation date of the IAM user login profile.
- `password_reset_required`: Indicates whether a password reset is required for the IAM user.

## User

A class representing an IAM user.

### Constructors

- `User(account: IAccount, name: str, id: str, arn: str, path: str = '/', created_date: Optional[datetime] = None, password_last_used_date: Optional[datetime] = None, permissions_boundary: Optional[PermissionsBoundary] = None, login_profile: Optional[LoginProfile] = None, access_keys: Optional[list[AccessKey]] = None, tags: Optional[list] = None) -> None`:
  Initializes a new **User** object with the specified parameters.

### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **User** object.

### Properties

- `access_keys`: A list of access keys associated with the IAM user.
- `account`: The AWS account associated with the IAM user.
- `arn`: The Amazon Resource Name (ARN) of the IAM user.
- `created_date`: The creation date of the IAM user.
- `id`: The unique ID of the IAM user.
- `login_profile`: The login profile associated with the IAM user.
- `name`: The name of the IAM user.
- `password_last_used_date`: The last date the IAM user's password was used.
- `path`: The path of the IAM user within the AWS IAM hierarchy.
- `permissions_boundary`: The permissions boundary associated with the IAM user.
- `tags`: A list of tags associated with the IAM user, useful for organization and management purposes.