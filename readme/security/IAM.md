# pyawsopstoolkit.security.iam

This subpackage of **pyawsopstoolkit.security** offers features designed to identify security risks and vulnerabilities
associated with AWS (Amazon Web Services) Identity and Access Management (IAM).

## Role

A class representing security risks and vulnerabilities related to IAM roles.

### Constructors

- `Role(session: ISession) -> None`: Initializes a new **Role** object.

### Methods

- `roles_without_permissions_boundary() -> list`: Retrieves a list of IAM roles lacking associated permissions
  boundaries, facilitating targeted risk assessment and mitigation.

### Properties

- `session`: An ISession object providing access to AWS services.

### Usage

```python
from pyawsopstoolkit import Session
from pyawsopstoolkit.security.iam import Role

# Create a session using default profile
session = Session(profile_name='default')

# Initialize IAM Role object
role_object = Role(session=session)

# Retrieve IAM roles without permissions boundaries
roles_without_boundaries = role_object.roles_without_permissions_boundary()

# Print the list of roles without permissions boundaries
print(roles_without_boundaries)
```

### References

- [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)
- [When and where to use IAM permissions boundaries](https://aws.amazon.com/blogs/security/when-and-where-to-use-iam-permissions-boundaries/)

## User

A class representing security risks and vulnerabilities related to IAM users.

### Constructors

- `User(session: ISession) -> None`: Initializes a new **User** object.

### Methods

- `users_without_permissions_boundary() -> list`: Retrieves a list of IAM users lacking associated permissions
  boundaries, facilitating targeted risk assessment and mitigation.

### Usage

```python
from pyawsopstoolkit import Session
from pyawsopstoolkit.security.iam import User

# Create a session using default profile
session = Session(profile_name='default')

# Initialize IAM User object
user_object = User(session=session)

# Retrieve IAM users without permissions boundaries
users_without_boundaries = user_object.users_without_permissions_boundary()

# Print the list of users without permissions boundaries
print(users_without_boundaries)
```

### References

- [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)
- [When and where to use IAM permissions boundaries](https://aws.amazon.com/blogs/security/when-and-where-to-use-iam-permissions-boundaries/)
