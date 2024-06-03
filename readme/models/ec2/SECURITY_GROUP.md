# pyawsopstoolkit.models.iam.security_group

This subpackage of **pyawsopstoolkit.models.ec2** (AWS Ops Toolkit Models) offers specialized data model classes
tailored for managing and manipulating Amazon Web Services (AWS) Elastic Compute Cloud (EC2) security groups. These
models facilitate efficient handling of security groups, ensuring seamless integration and interaction within AWS
environments.

## IPRange

A class representing an IPv4 range for an EC2 Security Group.

### Constructors

- `IPRange(cidr_ip: str, description: Optional[str] = None) -> None`: Initializes a new **IPRange** object with the
  specified parameters.

### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **IPRange** object.

### Properties

- `cidr_ip`: The IPv4 CIDR range.
- `description`: The description of the IPv4 CIDR range.

## IPv6Range

A class representing an IPv6 range for an EC2 Security Group.

### Constructors

- `IPv6Range(cidr_ipv6: str, description: Optional[str] = None) -> None`: Initializes a new **IPv6Range** object with
  the specified parameters.

### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **IPv6Range** object.

### Properties

- `cidr_ipv6`: The IPv6 CIDR range.
- `description`: The description of the IPv6 CIDR range.

## PrefixList

A class representing a Prefix List for an EC2 Security Group.

### Constructors

- `PrefixList(id: str, description: Optional[str] = None) -> None`: Initializes a new **PrefixList** object with the
  specified parameters.

### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **PrefixList** object.

### Properties

- `id`: The unique identifier of the prefix list.
- `description`: The description of the prefix list.

## UserIDGroupPair

A class representing a User ID Group Pair for an EC2 Security Group.

### Constructors

- `UserIDGroupPair(id: str, name: str, status: str, user_id: str, vpc_id: str, description: Optional[str] = None, vpc_peering_connection_id: Optional[str] = None) -> None`:
  Initializes a new **UserIDGroupPair** object with the specified parameters.

### Methods

- `__str__() -> str`: Returns a string representation of the **UserIDGroupPair** object.
- `__repr__() -> str`: Returns a detailed string representation of the **UserIDGroupPair** object.
- `to_dict() -> dict`: Returns a dictionary representation of the **UserIDGroupPair** object.

### Properties

- `id`: The unique identifier of the user ID group pair.
- `name`: The name of the user ID group pair.
- `status`: The status of the user ID group pair.
- `user_id`: The owner/user ID of the user ID group pair.
- `vpc_id`: The VPC ID of the user ID group pair.
- `description`: The description of the user ID group pair.
- `vpc_peering_connection_id`: The VPC peering connection ID of the user ID group pair.

## IPPermission

A class representing the IP Permissions for an EC2 Security Group.

### Constructors

- `IPPermission(from_port: int, to_port: int, ip_protocol: str, ip_ranges: Optional[list[IPRange]] = None, ipv6_ranges: Optional[list[IPv6Range]] = None, prefix_list_ids: Optional[list[PrefixListID]] = None, user_id_group_pairs: Optional[list[UserIDGroupPair]] = None) -> None`:
  Initializes a new **IPPermission** object with the specified parameters.

### Methods

- `__str__() -> str`: Returns a string representation of the **IPPermission** object.
- `to_dict() -> dict`: Returns a dictionary representation of the **IPPermission** object.

### Properties

- `from_port`: The starting port of an EC2 security group rule entry.
- `to_port`: The ending port of an EC2 security group rule entry.
- `ip_protocol`: The IP protocol of an EC2 security group rule entry.
- `ip_ranges`: The list of IPv4 ranges for an EC2 security group rule entry.
- `ipv6_ranges`: The list of IPv6 ranges for an EC2 security group rule entry.
- `prefix_list_ids`: The list of prefix lists for an EC2 security group rule entry.
- `user_id_group_pairs`: The list of user ID group pairs for an EC2 security group rule entry.

## SecurityGroup

A class representing an EC2 Security Group.

### Constructors

- `SecurityGroup(id: str, name: str, owner_id: str, vpc_id: str, ip_permissions: Optional[list[IPPermission]] = None, ip_permissions_egress: Optional[list[IPPermission]] = None, description: Optional[str] = None, tags: Optional[list] = None) -> None`:
  Initializes a new **SecurityGroup** object with the specified parameters.

### Methods

- `__str__() -> str`: Returns a string representation of the **SecurityGroup** object.
- `to_dict() -> dict`: Returns a dictionary representation of the **SecurityGroup** object.

### Properties

- `id`: The unique identifier of the EC2 security group.
- `name`: The name of the EC2 security group.
- `owner_id`: The owner ID of the EC2 security group.
- `vpc_id`: The VPC ID of the EC2 security group.
- `ip_permissions`: The list of inbound rule entries for the EC2 security group.
- `ip_permissions_egress`: The list of outbound rule entries for the EC2 security group.
- `description`: The description of the EC2 security group.
- `tags`: The tags associated with the EC2 security group.