# pyawsopstoolkit.models.ec2.network_interface

The **pyawsopstoolkit.models.ec2.network_interface** subpackage is part of the AWS Ops Toolkit Models, specifically
designed to provide specialized data model classes for handling Amazon Web Services (AWS) Elastic Compute Cloud (EC2)
network interfaces. These models ensure efficient manipulation and seamless integration of EC2 network interfaces.

## Association

The **Association** class represents the association of an EC2 network interface

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