from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Union

from pyawsopstoolkit.__validations__ import Validation


@dataclass
class Association:
    """
    A class representing the association of EC2 network interface.
    """
    id: str
    allocation_id: str
    ip_owner_id: str
    public_ip: str
    public_dns_name: str
    customer_owned_ip: str
    carrier_ip: str

    def __post_init__(self):
        for field_name, field_value in self.__dataclass_fields__.items():
            self.__validate__(field_name)

    def __validate__(self, field_name):
        field_value = getattr(self, field_name)
        if field_name in [
            'id', 'allocation_id', 'ip_owner_id', 'public_ip', 'public_dns_name', 'customer_owned_ip', 'carrier_ip'
        ]:
            Validation.validate_type(field_value, str, f'{field_name} should be a string.')

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in self.__dataclass_fields__:
            self.__validate__(key)

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the Association instance.
        :return: Dictionary representation of the Association instance.
        :rtype: dict
        """
        return {
            "id": self.id,
            "allocation_id": self.allocation_id,
            "ip_owner_id": self.ip_owner_id,
            "public_ip": self.public_ip,
            "public_dns_name": self.public_dns_name,
            "customer_owned_ip": self.customer_owned_ip,
            "carrier_ip": self.carrier_ip
        }


@dataclass
class Attachment:
    """
    A class representing the attachment of EC2 network interface.
    """
    id: str
    device_index: int
    status: str
    delete_on_termination: Optional[bool] = False
    attach_time: Optional[datetime] = None
    network_card_index: Optional[int] = None
    instance_id: Optional[str] = None
    instance_owner_id: Optional[str] = None

    def __post_init__(self):
        for field_name, field_value in self.__dataclass_fields__.items():
            self.__validate__(field_name)

    def __validate__(self, field_name):
        field_value = getattr(self, field_name)
        if field_name in ['id', 'status']:
            Validation.validate_type(field_value, str, f'{field_name} should be a string.')
        elif field_name in ['device_index']:
            Validation.validate_type(field_value, int, f'{field_name} should be an integer.')
        elif field_name in ['delete_on_termination']:
            Validation.validate_type(field_value, Union[bool, None], f'{field_name} should be a boolean.')
        elif field_name in ['attach_time']:
            Validation.validate_type(field_value, Union[datetime, None], f'{field_name} should be a datetime.')
        elif field_name in ['network_card_index']:
            Validation.validate_type(field_value, Union[int, None], f'{field_name} should be an integer.')
        elif field_name in ['instance_id', 'instance_owner_id']:
            Validation.validate_type(field_value, Union[str, None], f'{field_name} should be a string.')

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in self.__dataclass_fields__:
            self.__validate__(key)

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the Attachment instance.
        :return: Dictionary representation of the Attachment instance.
        :rtype: dict
        """
        return {
            "id": self.id,
            "device_index": self.device_index,
            "status": self.status,
            "delete_on_termination": self.delete_on_termination,
            "attach_time": self.attach_time.isoformat() if self.attach_time is not None else None,
            "network_card_index": self.network_card_index,
            "instance_id": self.instance_id,
            "instance_owner_id": self.instance_owner_id
        }


@dataclass
class Group:
    """
    A class representing the security group associated with EC2 network interface.
    """
    id: str
    name: str

    def __post_init__(self):
        for field_name, field_value in self.__dataclass_fields__.items():
            self.__validate__(field_name)

    def __validate__(self, field_name):
        field_value = getattr(self, field_name)
        if field_name in ['id', 'name']:
            Validation.validate_type(field_value, str, f'{field_name} should be a string.')

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in self.__dataclass_fields__:
            self.__validate__(key)

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the Group instance.
        :return: Dictionary representation of the Group instance.
        :rtype: dict
        """
        return {
            "id": self.id,
            "name": self.name
        }


@dataclass
class IPv6Address:
    """
    A class representing the IPv6 address associated with EC2 network interface.
    """
    address: str
    is_primary: Optional[bool] = False

    def __post_init__(self):
        for field_name, field_value in self.__dataclass_fields__.items():
            self.__validate__(field_name)

    def __validate__(self, field_name):
        field_value = getattr(self, field_name)
        if field_name in ['address']:
            Validation.validate_type(field_value, str, f'{field_name} should be a string.')
        elif field_name in ['is_primary']:
            Validation.validate_type(field_value, Union[bool, None], f'{field_name} should be a boolean.')

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in self.__dataclass_fields__:
            self.__validate__(key)

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the IPv6Address instance.
        :return: Dictionary representation of the IPv6Address instance.
        :rtype: dict
        """
        return {
            "address": self.address,
            "is_primary": self.is_primary
        }


@dataclass
class PrivateIPAddress:
    """
    A class representing the private IP address associated with EC2 network interface.
    """
    address: str
    dns_name: str
    is_primary: Optional[bool] = False
    association: Optional[Association] = None

    def __post_init__(self):
        for field_name, field_value in self.__dataclass_fields__.items():
            self.__validate__(field_name)

    def __validate__(self, field_name):
        field_value = getattr(self, field_name)
        if field_name in ['address', 'dns_name']:
            Validation.validate_type(field_value, str, f'{field_name} should be a string.')
        elif field_name in ['is_primary']:
            Validation.validate_type(field_value, Union[bool, None], f'{field_name} should be a boolean.')
        elif field_name in ['association']:
            Validation.validate_type(
                field_value, Union[Association, None], f'{field_name} should be of Association type.'
            )

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in self.__dataclass_fields__:
            self.__validate__(key)

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the PrivateIPAddress instance.
        :return: Dictionary representation of the PrivateIPAddress instance.
        :rtype: dict
        """
        return {
            "address": self.address,
            "dns_name": self.dns_name,
            "is_primary": self.is_primary,
            "association": self.association.to_dict() if self.association is not None else None
        }
