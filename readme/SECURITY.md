# pyawsopstoolkit.security

This package is a robust toolkit tailored to pinpoint security risks and vulnerabilities within AWS (Amazon Web
Services) infrastructure, addressing concerns like IAM roles lacking permissions boundaries. It's meticulously crafted
to cater to the intricate nuances of the expansive AWS ecosystem, covering a wide range of critical aspects.

## IAM

This class serves as a comprehensive repository for identifying security risks and vulnerabilities within the IAM
service.

### Methods

- `__init__(self, session: ISession) -> None`: Constructor method initializing the IAM class.
- `roles_without_permissions_boundary(self) -> list[pyawsopstoolkit.models.IAMRole]`: Retrieves a list of IAM roles
  lacking associated permissions boundaries, facilitating targeted risk assessment and mitigation.
- `users_without_permissions_boundary(self) -> list[pyawsopstoolkit.models.IAMUser]`: Retrieves a list of IAM users
  lacking associated permissions boundaries, facilitating targeted risk assessment and mitigation.

### Usage

```python
from pyawsopstoolkit import Session
from pyawsopstoolkit.security import IAM

# Create a session using default profile
session = Session(profile_name='default')

# Initialize IAM object
iam_object = IAM(session=session)

# Retrieve IAM roles without permissions boundaries
roles_without_boundaries = iam_object.roles_without_permissions_boundary()

# Print the list of roles without permissions boundaries
print(roles_without_boundaries)

# Retrieve IAM users without permissions boundaries
users_without_boundaries = iam_object.users_without_permissions_boundary()

# Print the list of users without permissions boundaries
print(users_without_boundaries)
```

### References

- [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)
- [When and where to use IAM permissions boundaries](https://aws.amazon.com/blogs/security/when-and-where-to-use-iam-permissions-boundaries/)
