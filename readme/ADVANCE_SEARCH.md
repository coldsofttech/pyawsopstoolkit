# pyawsopstoolkit.advsearch

The **pyawsopstoolkit.advsearch** module delivers an exhaustive array of advanced search functionalities, tailor-made
for seamless integration with AWS (Amazon Web Services). Meticulously engineered, these advanced searches are finely
tuned to meet the distinctive demands inherent to the expansive AWS ecosystem, encompassing a diverse spectrum of
aspects.

## Constants

This package supports various conditions for advanced searches, outlined below as global constants:

- `OR`: Represents the **or** condition.
- `AND`: Represents the **and** condition.
- `LESS_THAN`: Represents the less than **<** value.
- `LESS_THAN_OR_EQUAL_TO`: Represents the less than or equal to **<=** value.
- `GREATER_THAN`: Represents the greater than **>** value.
- `GREATER_THAN_OR_EQUAL_TO`: Represents the greater than or equal to **>=** value.
- `EQUAL_TO`: Represents the equal to **=** value.
- `NOT_EQUAL_TO`: Represents the not equal to **!=** value.
- `BETWEEN`: Represents the between range **< x <** value.
  These constants facilitate the formulation of complex queries, enabling precise and efficient data retrieval within
  the AWS environment.

## IAM

A class encapsulating advanced IAM-related search functionalities, facilitating the exploration of roles, users, and
more.

### Methods

- `__init__(self, session: ISession) -> None`: Initializes the constructor of the IAM class.
- `search_roles(self, condition: str = OR, **kwargs) -> list[pyawsopstoolkit.models.IAMRole]`: Returns a list of IAM
  roles using advanced search features supported by the specified arguments. For details on supported kwargs, please
  refer to the section below.

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
  All the above arguments support string types and accept regular expression patterns. Additionally, the
  max_session_duration, created_date, and last_used_date arguments support conditions such as less than, greater than,
  and between. For more details, please refer to the constants above.

### Usage

```python
from datetime import datetime
from pyawsopstoolkit import Session
from pyawsopstoolkit.advsearch import IAM, OR, AND, LESS_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN, \
    GREATER_THAN_OR_EQUAL_TO, EQUAL_TO, NOT_EQUAL_TO, BETWEEN

# Create a session using the 'default' profile
session = Session(profile_name='default')

# Initialize the IAM object with the session
iam_object = IAM(session=session)

# Example searches:
# 1. Search for IAM roles with the name matching 'test_role'
print(iam_object.search_roles(condition=OR, name=r'test_role'))

# 2. Search for IAM roles with the name matching 'test_role' or description matching 'test'
print(iam_object.search_roles(condition=OR, name=r'test_role', description=r'test'))

# 3. Search for IAM roles with both path matching '/service-role/' and name matching 'test'
print(iam_object.search_roles(condition=AND, path='/service-role/', name='test'))

# 4. Search for IAM roles with a maximum session duration less than 4 hours (14400 seconds)
print(iam_object.search_roles(max_session_duration={LESS_THAN: 14400}))

# 5. Search for IAM roles last used between October 15, 2023, and October 15, 2024
print(iam_object.search_roles(last_used_date={BETWEEN: [datetime(2023, 10, 15), datetime(2024, 10, 15)]}))

# 6. Search for IAM roles that contain the tag key 'test_key'
print(iam_object.search_roles(tag_key='test_key'))

# 7. Search for IAM roles that contain a tag with key 'test_key' and value 'test_value'
print(iam_object.search_roles(tag={'key': 'test_key', 'value': 'test_value'}))
```