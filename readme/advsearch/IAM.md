# pyawsopstoolkit.advsearch.iam

This subpackage of **pyawsopstoolkit.advsearch** offers sophisticated search capabilities specifically designed for
AWS (Amazon Web Services) Identity and Access Management (IAM).

## Role

A class representing advanced search features related to IAM roles.

### Constructors

- `Role(session: ISession) -> None`: Initializes a new **Role** object.

### Methods

- `search_roles(condition: str = OR, include_details: bool = False, **kwargs) -> list`: Returns a list of IAM roles
  using advanced search features supported by the specified arguments. For details on supported kwargs, please refer to
  the section below.

#### `search_roles` Supported Keyword Arguments

The **search_roles** function allows you to search for IAM roles using various keyword arguments. Below are the
supported keyword arguments:

- `path`: Specifies the path of the IAM role. Example: `path='/service-role/'`.
- `name`: Specifies the name of the IAM role. Example: `name='test_role'`.
- `id`: Specifies the ID of the IAM role. Example: `id='AIDACKCEVSQ6C2EXAMPLE'`.
- `arn`: Specifies the ARN of the IAM role. Example: `arn='arn:aws:iam::111122223333:role/role-name'`.
- `description`: Specifies the description of the IAM role. Example: `description='test'`.
- `permissions_boundary_type`: Specifies the type of permissions boundary for the IAM role.
  Example: `permissions_boundary_type='Policy'`.
- `permissions_boundary_arn`: Specifies the ARN of the permissions boundary for the IAM role.
  Example: `permissions_boundary_arn='arn:aws:iam::111122223333:policy/policy-name'`.
- `last_used_region`: Specifies the region where the IAM role was last used. Example: `last_used_region='eu-west-1'`.
- `tag_key`: Specifies the tag key associated with the IAM role. Example: `tag_key='test_key'`.
- `tag`: Specifies the tag key and value combination associated with the IAM role (dictionary format).
  Example: `tag={'key': 'test_key', 'value': 'test_value'}`.
- `max_session_duration`: Specifies the maximum session duration of the IAM role (in seconds, integer type).
  Example: `max_session_duration={LESS_THAN: 3600}`.
- `created_date`: Specifies the created date of the IAM role (datetime format).
  Example: `created_date={GREATER_THAN: datetime(2024, 10, 15)}`.
- `last_used_date`: Specifies the last used date of the IAM role (datetime format).
  Example: `last_used_date={BETWEEN: [datetime(2023, 10, 15), datetime(2024, 10, 15)]}`.

All the above arguments support string types and accept regular expression patterns. Additionally,
the `max_session_duration`, `created_date`, and `last_used_date` arguments support conditions such as less than, greater
than, and between. For more details, please refer to the constants above.

##### Usage

```python
from datetime import datetime

from pyawsopstoolkit import Session
from pyawsopstoolkit.advsearch.iam import Role
from pyawsopstoolkit.advsearch import OR, AND, LESS_THAN, BETWEEN

# Create a session using the 'default' profile
session = Session(profile_name='default')

# Initialize the IAM Role object with the session
role_object = Role(session=session)

# Example searches:
# 1. Search for all IAM roles
print(role_object.search_roles())

# 2. Search for IAM roles with the name matching 'test_role'
print(role_object.search_roles(condition=OR, name=r'test_role'))

# 3. Search for IAM roles with the name matching 'test_role' or description matching 'test'
print(role_object.search_roles(condition=OR, name=r'test_role', description=r'test'))

# 4. Search for IAM roles with both path matching '/service-role/' and name matching 'test'
print(role_object.search_roles(condition=AND, path='/service-role/', name='test'))

# 5. Search for IAM roles with a maximum session duration less than 4 hours (14400 seconds)
print(role_object.search_roles(max_session_duration={LESS_THAN: 14400}))

# 6. Search for IAM roles last used between October 15, 2023, and October 15, 2024
print(role_object.search_roles(last_used_date={BETWEEN: [datetime(2023, 10, 15), datetime(2024, 10, 15)]}))

# 7. Search for IAM roles that contain the tag key 'test_key'
print(role_object.search_roles(tag_key='test_key'))

# 8. Search for IAM roles that contain a tag with key 'test_key' and value 'test_value'
print(role_object.search_roles(tag={'key': 'test_key', 'value': 'test_value'}))
```

## User

A class representing advance search features related with IAM users.

### Constructors

- `User(session: ISession) -> None`: Initializes a new **User** object.

### Methods

- `search_users(condition: str = OR, include_details: bool = False, **kwargs) -> list`: Returns a list of IAM users
  using advanced search features supported by the specified arguments. For details on supported kwargs, please refer to
  the section below.

#### `search_users` Supported Keyword Arguments

The **search_users** function allows you to search for IAM users using various keyword arguments. Below are the
supported keyword arguments:

- `path`: Specifies the path of the IAM user. Example: `path='/'`.
- `name`: Specifies the name of the IAM user. Example: `name='test_user'`.
- `id`: Specifies the ID of the IAM user. Example: `id='AIDACKCEVSQ6C2EXAMPLE'`.
- `arn`: Specifies the ARN of the IAM user. Example: `arn='arn:aws:iam::111122223333:user/test_user'`.
- `permissions_boundary_type`: Specifies the type of permissions boundary for the IAM user.
  Example: `permissions_boundary_type='Policy'`.
- `permissions_boundary_arn`: Specifies the ARN of the permissions boundary for the IAM user.
  Example: `permissions_boundary_arn='arn:aws:iam::111122223333:policy/policy-name'`.
- `tag_key`: Specifies the tag key associated with the IAM user. Example: `tag_key='test_key'`.
- `tag`: Specifies the tag key and value combination associated with the IAM user (dictionary format).
  Example: `tag={'Key': 'test_key', 'Value': 'test_value'}`.
- `created_date`: Specifies the created date of the IAM user (datetime format).
  Example: `created_date={GREATER_THAN: datetime(2024, 10, 15)}`.
- `password_last_used_date`: Specifies the password last used date of the IAM user (datetime format).
  Example: `password_last_used_date={BETWEEN: [datetime(2023, 10, 15), datetime(2024, 10, 15)]}`.
- `login_profile_created_date`: Specifies the login profile created date of the IAM user (datetime format).
  Example: `login_profile_created_date={GREATER_THAN: datetime(2024, 10, 15)}`.
- `login_profile_password_reset_required`: Specifies the flag of the login profile to check if a password reset is
  required for the IAM user (boolean format). Example: `login_profile_password_reset_required=False`.
- `access_key_id`: Specifies the ID of the IAM user access key. Example: `access_key_id='ABCD'`.
- `access_key_status`: Specifies the status of the IAM user access key. Example: `access_key_status='Active'`.
- `access_key_service`: Specifies the last used service of the IAM user access key.
  Example: `access_key_service='ec2.amazonaws.com'`.
- `access_key_region`: Specifies the last used region of the IAM user access key.
  Example: `access_key_region='eu-west-1'`.
  All the above arguments support string types and accept regular expression patterns. Additionally, the `created_date`
  and `password_last_used_date` arguments support conditions such as less than, greater than, and between. For more
  details, please refer to the constants above.

##### Usage

```python
from datetime import datetime

from pyawsopstoolkit import Session
from pyawsopstoolkit.advsearch.iam import User
from pyawsopstoolkit.advsearch import OR, AND, BETWEEN

# Create a session using the 'default' profile
session = Session(profile_name='default')

# Initialize the IAM User object with the session
user_object = User(session=session)

# Example searches:
# 1. Search for all IAM users
print(user_object.search_users())

# 2. Search for IAM users with the name matching 'test_user'
print(user_object.search_users(condition=OR, name=r'test_user'))

# 3. Search for IAM users with both path matching '/' and name matching 'test'
print(user_object.search_users(condition=AND, path='/', name='test'))

# 4. Search for IAM users password last used between October 15, 2023, and October 15, 2024
print(user_object.search_users(password_last_used_date={BETWEEN: [datetime(2023, 10, 15), datetime(2024, 10, 15)]}))

# 5. Search for IAM roles that contain the tag key 'test_key'
print(user_object.search_users(tag_key='test_key'))

# 6. Search for IAM roles that contain a tag with key 'test_key' and value 'test_value'
print(user_object.search_users(tag={'key': 'test_key', 'value': 'test_value'}))
```