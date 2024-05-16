## pyawsopstoolkit.validators

The **pyawsopstoolkit.validators** package provides a comprehensive set of validation classes specifically crafted for
use with AWS (Amazon Web Services). These validators are meticulously designed to cater to the unique requirements
within the AWS ecosystem, covering a wide array of aspects such as AWS Resource Names (ARNs), Policy Statements, and
more. By leveraging these validators, developers can ensure that their AWS-related inputs and configurations adhere to
the necessary standards and formats, thereby enhancing the reliability and security of their applications deployed on
AWS.

### AccountValidator

The **AccountValidator** class provides methods to validate AWS account information, ensuring accuracy and consistency
in account details. It includes constants and methods for validating account numbers.

#### Constants

- `NUMBER_PATTERN (str)`: Regular expression pattern for validating account numbers. The pattern ensures that the
  account number consists of exactly 12 digits.

#### Methods

- `number(cls, value: str, raise_error: Optional[bool] = True, custom_error_message: Optional[str] = None) -> bool`:
  Validate the account number.

#### Usage

```python
from pyawsopstoolkit.validators import AccountValidator

# Validate account number
print(AccountValidator.number('123456789012'))  # Output: True
print(AccountValidator.number('123'))  # Output: False
```

#### References

- [AWS Documentation: DescribeAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeAccount.html)

### ArnValidator

The **ArnValidator** class validates AWS ARNs (Amazon Resource Names) according to the AWS ARN format. This class
provides methods to validate various aspects of ARNs, including the partition, service, region, account ID, and resource
ID.

#### Constants

- `ARN_PATTERN (str)`: Regular expression pattern for AWS ARNs.

#### Methods

- `arn(cls, value: Union[str, list], raise_error: Optional[bool] = True, custom_error_message: Optional[str] = None) -> bool`:
  Validates if the given ARN(s) match the ARN pattern.

#### Usage

```python
from pyawsopstoolkit.validators import ArnValidator

# Validate ARNs
print(ArnValidator.arn('arn:aws:ec2:us-east-1:123456789012:vpc/vpc-0e9801d129EXAMPLE', False))  # Output: True
print(ArnValidator.arn('arn::iam:us-east-1:123456789012:user', False))  # Output: False
```

#### References

- [AWS Documentation: ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html)

### PolicyValidator

The **PolicyValidator** class validates AWS IAM policy documents. This class provides methods to validate various
aspects of IAM policies, ensuring their correctness and compliance.

#### Constants

- `VERSION_PATTERN (str)`: Regular expression pattern for validating version strings in policies.
- `EFFECT_PATTERN (str)`: Regular expression pattern for validating effect strings in policies.
- `PRINCIPAL_PATTERN (str)`: Regular expression pattern for validating principal strings in policies.

#### Methods

- `policy(cls, value: dict, raise_error: Optional[bool] = True, custom_error_message: Optional[str] = None) -> bool`:
  Validates a policy dictionary.

#### Usage

```python
from pyawsopstoolkit.validators import PolicyValidator

# Validate IAM policy document
print(PolicyValidator.policy(
    {
        "Version": "2012-10-17",
        "Id": "1",
        "Statement": {
            "Sid": "1",
            "Principal": "*",
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*",
            "Condition": {
                "Bool": {
                    "aws:SecureTransport": "true"
                }
            }
        }
    }, False
))  # Output: True

print(PolicyValidator.policy(
    {
        "Version": "2012-10-17",
        "Id": "1"
    }, False
))  # Output: False
```

#### References

- [AWS Documentation: IAM Policy Grammar](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_grammar.html)

### TagValidator

The **TagValidator** class validates tags according to predefined patterns. This class provides methods to validate keys
and values of tags in dictionaries or lists of dictionaries.

#### Constants

- `KEY_PATTERN (str)`: Regular expression pattern used to validate keys in a dictionary of tags.
- `VALUE_PATTERN (str)`: Regular expression pattern used to validate values in a dictionary of tags.

#### Methods

- `tag(cls, value: Union[dict, list], raise_error: Optional[bool] = True, custom_error_message: Optional[str] = None) -> bool`:
  Validates a dictionary or a list of dictionaries of tags.

#### Usage

```python
from pyawsopstoolkit.validators import TagValidator

# Validate tag dictionary
print(TagValidator.tag(
    {
        'Key': 'sample',
        'Value': 'sample-test'
    }, False
))  # Output: True

print(TagValidator.tag(
    {
        'Key': 1,
        1: 'sample-test'
    }, False
))  # Output: False
```

#### References

- [AWS Documentation: Tagging](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html)

### Validator

The **Validator** class validates according to predefined patterns. This class provides methods to validate various
aspects of AWS, such as region code.

#### Constants

- `REGION_PATTERN (str)`: Regular expression pattern used to validate region codes.

#### Methods

- `region(cls, value: str, raise_error: Optional[bool] = True, custom_error_message: Optional[str] = None) -> bool`:
  Validates a region value.

#### Usage

```python
from pyawsopstoolkit.validators import Validator

# Validate region code
print(Validator.region('eu-west-1', False))  # Output: True
print(Validator.region('Ohio', False))  # Output: False
```

#### References

- [AWS Documentation: DescribeAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeAccount.html)
