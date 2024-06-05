# pyawsopstoolkit.insights.iam

This subpackage of **pyawsopstoolkit.insights** offers sophisticated insights specifically designed for AWS (Amazon Web
Services) Identity and Access Management (IAM). It provides tools to analyze and manage IAM roles and users, ensuring
efficient and secure AWS operations.

## Role

The **Role** class represents insights related to IAM roles.

### Constructors

- `Role(session: ISession) -> None`: Initializes a new **Role** object with the provided session.

### Methods

- `unused_roles(no_of_days: Optional[int] = 90, include_newly_created: Optional[bool] = False) -> list`: Returns a list
  of unused IAM roles based on the specified parameters.

### Properties

- `session`: An ISession object providing access to AWS services.

### Usage

```python
from pyawsopstoolkit import Session
from pyawsopstoolkit.insights.iam import Role

# Create a session using the default profile
session = Session(profile_name='default')

# Initialize the IAM Role object
role_object = Role(session=session)

# Retrieve IAM roles unused for the last 90 days
unused_roles = role_object.unused_roles()

# Print the list of unused roles
print(unused_roles)
```

## User

The **User** class represents insights related to IAM users.

### Constructors

- `User(session: ISession) -> None`: Initializes a new **User** object with the provided session.

### Methods

- `unused_users(no_of_days: Optional[int] = 90, include_newly_created: Optional[bool] = False) -> list`: Returns a list
  of unused IAM users based on the specified parameters.

### Usage

```python
from pyawsopstoolkit import Session
from pyawsopstoolkit.insights.iam import User

# Create a session using the default profile
session = Session(profile_name='default')

# Initialize the IAM User object
user_object = User(session=session)

# Retrieve IAM users unused for the last 90 days
unused_users = user_object.unused_users()

# Print the list of unused users
print(unused_users)
```