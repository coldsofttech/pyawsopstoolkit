# pyawsopstoolkit

Welcome to pyawsopstoolkit! This Python package is your all-in-one solution for managing Amazon Web Services (AWS)
operations efficiently. Whether you're a seasoned AWS user or just getting started, this toolkit offers a comprehensive
set of features and enhancements to streamline your AWS interactions.

## Features

- **Session Management**: Seamlessly integrate session management classes into your application ecosystem, empowering
  refined control over workflow dynamics.
- **Assume Role Function**: Access a versatile function for assuming roles, augmenting security and flexibility within
  your AWS operations.
- **Subpackages**:
    - **Validator Functions**: Validate AWS ARNs, IAM policy formats, and more with ease, ensuring the correctness of
      crucial parameters.
    - **Advance Search**: Harness advanced search capabilities to efficiently navigate and filter AWS resources,
      streamlining resource discovery and management.
    - **Security Risks/Vulnerabilities**: Safeguard your AWS infrastructure by proactively identifying and addressing
      security threats and vulnerabilities. Leverage dedicated tools to detect misconfigurations, insecure permissions,
      and
      potential entry points for cyberattacks. Stay vigilant with continuous monitoring and auditing to maintain a
      robust
      security posture and mitigate risks effectively.
    - **Insights**: Gain comprehensive insights into various aspects of your AWS infrastructure to maintain optimal
      hygiene
      and clean up unused or obsolete resources.

## What's Next?

Stay tuned as we continue to evolve this toolkit! We're constantly working on adding new features and enhancements to
make your AWS-related workflows even more efficient and productive. Watch this space for updates and upcoming additions.

## Getting Started

Ready to supercharge your AWS operations? Let's get started with **pyawsopstoolkit**!

### Installation

Install **pyawsopstoolkit** via pip:

```bash
pip install pyawsopstookit
```

### Usage

Import the package in your Python script:

```python
import pyawsopstoolkit
```

Now you're all set to harness the power of **pyawsopstoolkit** in your AWS workflows!

# Documentation

## pyawsopstoolkit

### Credentials

The **Credentials** class represents a set of AWS credentials, including an access key, secret access key, token, and
optional expiry datetime.

#### Constructors

- `Credentials(access_key: str, secret_access_key: str, token: str, expiry: Optional[datetime] = None) -> None`:
  Initializes a **Credentials** object with the provided access key, secret access key, token, and expiry datetime if
  available.

#### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **Credentials** object.

#### Usage

```python
from pyawsopstoolkit.credentials import Credentials

# Create a Credentials object
creds = Credentials(access_key='access_key', secret_access_key='secret_access_key', token='token')

# Access individual attributes
print(creds.access_key)  # Output: access_key
print(creds.secret_access_key)  # Output: secret_access_key
print(creds.token)  # Output: token

# Print the Credentials object
print(creds)
# Output: Credentials(access_key="access_key",secret_access_key="secret_access_key",token="token",expiry=None)

# Convert Credentials object to dictionary
print(creds.to_dict())
# Output:
# {
#     "access_key": "access_key",
#     "secret_access_key": "secret_access_key",
#     "token": "token",
#     "expiry": None
# }
```

### Account

The **Account** class represents an AWS account with various attributes. This class provides basic functionality for
managing an AWS account.

#### Constructors

- `Account(number: str) -> None`: Initializes an **Account** object with the provided account number.

#### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **Account** object.

#### Usage

```python
from pyawsopstoolkit.account import Account

# Create an Account object
account = Account('123456789012')

# Access the account number attribute
print(account.number)  # Output: 123456789012
```

### Session

The **Session** class represents a boto3 Session with various attributes, offering functionality to manage sessions.
Additionally, it provides the option to assume a session.

#### Constructors

- `Session(profile_name: Optional[str] = None, credentials: Optional[ICredentials] = None, region_code: Optional[str] = 'eu-west-1', cert_path: Optional[str] = None) -> None`:
  Initializes a **Session** object for AWS with optional parameters for profile name, credentials, and region code.

#### Methods

- `get_session() -> boto3.Session`: Returns the **boto3.Session** object based on the specified parameters within
  the class object. This method prioritizes the profile name, followed by credentials. It verifies the session validity
  by performing a quick S3 list buckets action.
- `get_config() -> botocore.config.Config`: Returns the **botocore.config.Config** based on the specified region
  code within the class object.
- `get_account() -> IAccount`: Returns the AWS account number based on the **get_session** with specified parameters
  within the class object.
- `get_credentials_for_profile() -> ICredentials`: Returns the AWS credentials (access key, secret access key, and
  token) based on the **get_session** with specified parameters within the class object.
- `assume_role(role_arn: str, role_session_name: Optional[str] = 'AssumeSession', policy_arns: Optional[list] = None, policy: Optional[Union[str, dict]] = None, duration_seconds: Optional[int] = 3600, tags: Optional[list] = None) -> ISession`:
  Returns the **ISession** object for the assumed role based on the specified parameters.

#### Usage

```python
from pyawsopstoolkit.session import Session

# Initialize a Session object with a profile name
profile_name = 'default'
session = Session(profile_name=profile_name)

# Get boto3 Session
boto3_session = session.get_session()
print(boto3_session)  # Output: Session(region_name='eu-west-1')

# Get AWS account number
account = session.get_account()
print(account.number)  # Output: 123456789012

# Get botocore config
config = session.get_config()
print(config)  # Output: <botocore.config.Config object at 0x0000022097630040>

# Get credentials for profile
creds = session.get_credentials_for_profile()
print(
    creds)  # Output: Credentials(access_key="access_key",secret_access_key="secret_access_key",token=None,expiry=None)
```

## pyawsopstoolkit_validators

For detailed information and usage examples, please refer
to [pyawsopstoolkit_validators](https://github.com/coldsofttech/pyawsopstoolkit-validators)

# License

Please refer to the [MIT License](LICENSE) within the project for more information.

# Contributing

We welcome contributions from the community! Whether you have ideas for new features, bug fixes, or enhancements, feel
free to open an issue or submit a pull request on [GitHub](https://github.com/coldsofttech/pyawsopstoolkit).

