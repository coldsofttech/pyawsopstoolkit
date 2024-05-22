# pyawsopstoolkit.insights

This package offers a comprehensive array of features designed to clean up and maintain hygiene within AWS (Amazon Web
Services). It includes tools for identifying unused IAM roles, EC2 Security Groups, and more. Meticulously engineered,
these features are finely tuned to meet the unique demands of the expansive AWS ecosystem, encompassing a diverse
spectrum of aspects.

## IAM

A class that encapsulates insights related to the IAM service, including roles, users, and other entities.

### Methods

- `__init__(self, session: ISession) -> None`: Initializes the IAM class with the provided session.
- `unused_roles(self, no_of_days: Optional[int] = 90, include_newly_created: Optional[bool] = False) -> list[pyawsopstoolkit.models.IAMRole]`:
  Returns a list of unused IAM roles based on the specified parameters.

### Usage

```python
from pyawsopstoolkit import Session
from pyawsopstoolkit.insights import IAM

# Create a session using the default profile
session = Session(profile_name='default')

# Initialize the IAM object
iam_object = IAM(session=session)

# Retrieve IAM roles unused for the last 90 days
unused_roles = iam_object.unused_roles()

# Print the list of unused roles
print(unused_roles)
```