# pyawsopstoolkit.models.ec2.network_interface

The **pyawsopstoolkit.models.ec2.network_interface** subpackage is part of the AWS Ops Toolkit Models, specifically
designed to provide specialized data model classes for handling Amazon Web Services (AWS) Elastic Compute Cloud (EC2)
network interfaces. These models ensure efficient manipulation and seamless integration of EC2 network interfaces.

## Association

The **Association** class represents the association of an EC2 network interface.

### Constructors

- `Association(id: str, allocation_id: str, ip_owner_id: str, public_ip: str, public_dns_name: str, customer_owned_ip: str, carrier_ip: str) -> None`:
  Initializes a new **Association** object with the specified parameters.

### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **Association** object.

### Properties

- `allocation_id`: The allocation ID associated with the EC2 network interface association.
- `carrier_ip`: The Carrier IP address associated with the EC2 network interface association.
- `customer_owned_ip`: The Customer Owned IP address associated with the EC2 network interface association.
- `id`: The unique identifier for the EC2 network interface association.
- `ip_owner_id`: The IP Owner ID associated with the EC2 network interface association.
- `public_dns_name`: The Public DNS Name associated with the EC2 network interface association.
- `public_ip`: The Public IP address associated with the EC2 network interface association.

## Attachment

The **Attachment** class represents the attachment of an EC2 network interface.

### Constructors

- `Attachment(id: str, device_index: int, status: str, delete_on_termination: Optional[bool] = False, attach_time: Optional[datetime] = None, network_card_index: Optional[int] = None, instance_id: Optional[str] = None, instance_owner_id: Optional[str] = None) -> None`:
  Initializes a new **Attachment** object with specified parameters.

### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **Attachment** object.

### Properties

- `attach_time`: The timestamp indicating when the EC2 network interface was attached.
- `delete_on_termination`: A boolean flag indicating whether the network interface attachment will be deleted when the
  associated EC2 instance is terminated.
- `device_index`: The device index associated with the EC2 network interface attachment, indicating its position among
  multiple network interfaces.
- `id`: The unique identifier of the EC2 network interface attachment, which distinguishes this attachment from others.
- `instance_id`: The unique identifier of the EC2 instance to which the network interface is attached.
- `instance_owner_id`: The AWS account ID of the owner of the EC2 instance to which the network interface is attached.
- `network_card_index`: The index of the network card for the EC2 network interface attachment, useful for instances
  with multiple network cards.
- `status`: The current status of the EC2 network interface attachment, reflecting whether it is attaching, attached,
  detaching, or detached.

## Group

The **Group** class represents the security group associated with EC2 network interface.

### Constructors

- `Group(id: str, name: str) -> None`: Initializes a new **Group** object with specified parameters.

### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **Group** object.

### Properties

- `id`: The unique identifier of the security group associated with the EC2 network interface.
- `name`: The name of the security group associated with the EC2 network interface.

## IPv6Address

The **IPv6Address** class represents the IPv6 address associated with EC2 network interface.

### Constructors

- `IPv6Address(address: str, is_primary: Optional[bool] = False) -> None`: Initializes a new **IPv6Address** object with
  specified parameters.

### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **IPv6Address** object.

### Properties

- `address`: The IPv6 address associated with the EC2 network interface.
- `is_primary`: A boolean flag indicating whether this IPv6 address is the primary address for the EC2 network
  interface.