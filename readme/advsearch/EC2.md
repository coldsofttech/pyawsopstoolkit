# pyawsopstoolkit.advsearch.ec2

This subpackage of **pyawsopstoolkit.advsearch** offers sophisticated search capabilities specifically designed for
AWS (Amazon Web Services) Elastic Compute Cloud (EC2).

## SecurityGroup

The **SecurityGroup** class provides advanced search features related to EC2 security groups.

### Constructors

- `SecurityGroup(session: ISession) -> None`: Initializes a new **SecurityGroup** object.

### Methods

- `search_security_groups(condition: str = OR, region: str | list = 'eu-west-1', **kwargs) -> list`: Returns a list of
  EC2 security groups using advanced search features supported by the specified arguments. For details on supported
  keyword arguments, please refer to the section below.

#### `search_security_groups` Supported Keyword Arguments

The **search_security_groups** method allows you to search for EC2 security groups using various keyword arguments.
Below are the supported keyword arguments:

- `id`: Specifies the unique identifier of the EC2 security group. Example: `id='sg-12345678'`.
- `name`: Specifies the name of the EC2 security group. Example: `name='web-servers-sg'`.
- `owner_id`: Specifies the owner ID of the EC2 security group. Example: `owner_id='123456789012'`.
- `vpc_id`: Specifies the VPC ID of the EC2 security group. Example: `vpc_id='vpc-abcdefgh'`.
- `description`: Specifies the description of the EC2 security group. Example: `description='test'`.
- `tag_key`: Specifies the tag key associated with the EC2 security group. Example: `tag_key='test_key'`.
- `tag`: Specifies the tag key and value combination associated with the EC2 security group (dictionary format).
  Example: `tag={'key': 'test_key', 'value': 'test_value'}`.
- `in_from_port`: Specifies the inbound EC2 security group rule entry "from" port. Example: `in_from_port=80`.
- `out_from_port`: Specifies the outbound EC2 security group rule entry "from" port. Example: `out_from_port=80`.
- `in_to_port`: Specifies the inbound EC2 security group rule entry "to" port. Example: `in_to_port=443`.
- `out_to_port`: Specifies the outbound EC2 security group rule entry "to" port. Example: `out_to_port=443`.
- `in_port_range`: Specifies the inbound EC2 security group rule entry port if it exists within range "from" and "to".
  Example: `in_port_range=80`.
- `out_port_range`: Specifies the outbound EC2 security group rule entry port if it exists within range "from" and "to".
  Example: `out_port_range=443`.
- `in_ip_protocol`: Specifies the inbound EC2 security group rule entry protocol. Example: `in_ip_protocol='tcp'`.
- `out_ip_protocol`: Specifies the outbound EC2 security group rule entry protocol. Example: `out_ip_protocol='udp'`.
  All the above arguments support string types and accept regular expression patterns. Additionally,
  the `in_from_port`, `out_from_port`, `in_to_port`, `out_to_port`, `in_port_range`, and `out_port_range` arguments
  support integer types.

##### Usage

```python
from pyawsopstoolkit import Session
from pyawsopstoolkit.advsearch.ec2 import SecurityGroup
from pyawsopstoolkit.advsearch import OR

# Create a session using the 'default' profile
session = Session(profile_name='default')

# Initialize the EC2 security group object with the session
sg_object = SecurityGroup(session=session)

# Example searches:

# 1. Search for all EC2 security groups
print(sg_object.search_security_groups())

# 2. Search for EC2 security groups with the name matching 'test_sg'
print(sg_object.search_security_groups(condition=OR, region='us-east-2', name=r'test_sg'))

# 3. Search for EC2 security groups with the name matching 'test_sg' or description matching 'test'
print(sg_object.search_security_groups(condition=OR, region='us-east-2', name=r'test_sg', description=r'test'))

# 4. Search for EC2 security groups that contain the tag key 'test_key'
print(sg_object.search_security_groups(tag_key='test_key'))

# 5. Search for EC2 security groups that contain a tag with key 'test_key' and value 'test_value'
print(sg_object.search_security_groups(tag={'key': 'test_key', 'value': 'test_value'}))

# 6. Search for EC2 security groups that contain port 80 as an inbound rule entry
print(sg_object.search_security_groups(in_from_port=80))

# 7. Search for EC2 security groups that contain 'all' traffic within inbound rule entry protocols
print(sg_object.search_security_groups(in_ip_protocol='all'))
```