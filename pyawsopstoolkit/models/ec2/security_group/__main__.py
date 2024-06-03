from dataclasses import dataclass
from typing import Optional, Union

from pyawsopstoolkit.__interfaces__ import IAccount
from pyawsopstoolkit.__validations__ import Validation
from pyawsopstoolkit.validators import AccountValidator, Validator


@dataclass
class IPRange:
    """
    A class representing IPv4 range for a EC2 Security Group.
    """
    cidr_ip: str
    description: Optional[str] = None

    def __post_init__(self):
        for field_name, field_value in self.__dataclass_fields__.items():
            self.__validate__(field_name)

    def __validate__(self, field_name):
        field_value = getattr(self, field_name)
        if field_name in ['cidr_ip']:
            Validation.validate_type(field_value, str, f'{field_name} should be a string.')
        elif field_name in ['description']:
            Validation.validate_type(field_value, Union[str, None], f'{field_name} should be a string.')

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in self.__dataclass_fields__:
            self.__validate__(key)

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the IPRange instance.
        :return: Dictionary representation of the IPRange instance.
        :rtype: dict
        """
        return {
            "cidr_ip": self.cidr_ip,
            "description": self.description
        }


@dataclass
class IPv6Range:
    """
    A class representing IPv6 range for a EC2 Security Group.
    """
    cidr_ipv6: str
    description: Optional[str] = None

    def __post_init__(self):
        for field_name, field_value in self.__dataclass_fields__.items():
            self.__validate__(field_name)

    def __validate__(self, field_name):
        field_value = getattr(self, field_name)
        if field_name in ['cidr_ipv6']:
            Validation.validate_type(field_value, str, f'{field_name} should be a string.')
        elif field_name in ['description']:
            Validation.validate_type(field_value, Union[str, None], f'{field_name} should be a string.')

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in self.__dataclass_fields__:
            self.__validate__(key)

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the IPv6Range instance.
        :return: Dictionary representation of the IPv6Range instance.
        :rtype: dict
        """
        return {
            "cidr_ipv6": self.cidr_ipv6,
            "description": self.description
        }


@dataclass
class PrefixList:
    """
    A class representing Prefix List for a EC2 Security Group.
    """
    id: str
    description: Optional[str] = None

    def __post_init__(self):
        for field_name, field_value in self.__dataclass_fields__.items():
            self.__validate__(field_name)

    def __validate__(self, field_name):
        field_value = getattr(self, field_name)
        if field_name in ['id']:
            Validation.validate_type(field_value, str, f'{field_name} should be a string.')
        elif field_name in ['description']:
            Validation.validate_type(field_value, Union[str, None], f'{field_name} should be a string.')

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in self.__dataclass_fields__:
            self.__validate__(key)

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the PrefixList instance.
        :return: Dictionary representation of the PrefixList instance.
        :rtype: dict
        """
        return {
            "id": self.id,
            "description": self.description
        }


@dataclass
class UserIDGroupPair:
    """
    A class representing User ID Group Pair for a EC2 Security Group.
    """
    id: str
    name: str
    status: str
    user_id: str
    vpc_id: str
    description: Optional[str] = None
    vpc_peering_connection_id: Optional[str] = None

    def __post_init__(self):
        for field_name, field_value in self.__dataclass_fields__.items():
            self.__validate__(field_name)

    def __validate__(self, field_name):
        field_value = getattr(self, field_name)
        if field_name in ['id', 'name', 'status', 'user_id', 'vpc_id']:
            Validation.validate_type(field_value, str, f'{field_name} should be a string.')
        elif field_name in ['description', 'vpc_peering_connection_id']:
            Validation.validate_type(field_value, Union[str, None], f'{field_name} should be a string.')

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in self.__dataclass_fields__:
            self.__validate__(key)

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the UserIDGroupPair instance.
        :return: Dictionary representation of the UserIDGroupPair instance.
        :rtype: dict
        """
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "user_id": self.user_id,
            "vpc_id": self.vpc_id,
            "description": self.description,
            "vpc_peering_connection_id": self.vpc_peering_connection_id
        }


@dataclass
class IPPermission:
    """
    A class representing the IP Permissions for a EC2 Security Group.
    """
    from_port: int
    to_port: int
    ip_protocol: str
    ip_ranges: Optional[list[IPRange]] = None
    ipv6_ranges: Optional[list[IPv6Range]] = None
    prefix_lists: Optional[list[PrefixList]] = None
    user_id_group_pairs: Optional[list[UserIDGroupPair]] = None

    def __post_init__(self):
        for field_name, field_value in self.__dataclass_fields__.items():
            self.__validate__(field_name)

    def __validate__(self, field_name):
        mappings = {
            'ip_ranges': IPRange,
            'ipv6_ranges': IPv6Range,
            'prefix_lists': PrefixList,
            'user_id_group_pairs': UserIDGroupPair
        }
        field_value = getattr(self, field_name)
        if field_name in ['from_port', 'to_port']:
            Validation.validate_type(field_value, int, f'{field_name} should be an integer.')
        elif field_name in ['ip_protocol']:
            Validation.validate_type(field_value, str, f'{field_name} should be a string.')
        elif field_name in ['ip_ranges', 'ipv6_ranges', 'prefix_lists', 'user_id_group_pairs']:
            field_type = mappings.get(field_name)
            message = f'{field_name} should be of {field_type.__name__} type.'
            Validation.validate_type(field_value, Union[list, None], message)
            if field_value is not None and len(field_value) > 0:
                all(Validation.validate_type(item, field_type, message) for item in field_value)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in self.__dataclass_fields__:
            self.__validate__(key)

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the IPPermission instance.
        :return: Dictionary representation of the IPPermission instance.
        :rtype: dict
        """
        return {
            "from_port": self.from_port,
            "to_port": self.to_port,
            "ip_protocol": self.ip_protocol,
            "ip_ranges": [
                ip.to_dict() for ip in self.ip_ranges
            ] if self.ip_ranges and len(self.ip_ranges) > 0 else None,
            "ipv6_ranges": [
                ip.to_dict() for ip in self.ipv6_ranges
            ] if self.ipv6_ranges and len(self.ipv6_ranges) > 0 else None,
            "prefix_lists": [
                prefix.to_dict() for prefix in self.prefix_lists
            ] if self.prefix_lists and len(self.prefix_lists) > 0 else None,
            "user_id_group_pairs": [
                pair.to_dict() for pair in self.user_id_group_pairs
            ] if self.user_id_group_pairs and len(self.user_id_group_pairs) > 0 else None
        }


class SecurityGroup:
    """
    A class representing the EC2 Security Group.
    """

    def __init__(
            self,
            account: IAccount,
            region: str,
            id: str,
            name: str,
            owner_id: str,
            vpc_id: str,
            ip_permissions: Optional[list[IPPermission]] = None,
            ip_permissions_egress: Optional[list[IPPermission]] = None,
            description: Optional[str] = None,
            tags: Optional[list] = None
    ) -> None:
        """
        Initializes a new SecurityGroup instance with specified parameters.
        :param account: The account associated with the EC2 security group.
        :type account: IAccount
        :param region: The region associated with the EC2 security group.
        :type region: str
        :param id: The unique identifier of the EC2 security group.
        :type id: str
        :param name: The name of the EC2 security group.
        :type name: str
        :param owner_id: The owner id of the EC2 security group.
        :type owner_id: str
        :param vpc_id: The VPC id of the EC2 security group.
        :type vpc_id: str
        :param ip_permissions: The list of inbound rule entries of the EC2 security group.
        :type ip_permissions: list
        :param ip_permissions_egress: The list of outbound rule entries of the EC2 security group.
        :type ip_permissions_egress: list
        :param description: The description of the EC2 security group.
        :type description: str
        :param tags: The tags of the EC2 security group.
        :type tags: list
        """
        Validation.validate_type(account, IAccount, 'account should be of IAccount type.')
        Validator.region(region, True)
        Validation.validate_type(id, str, 'id should be a string.')
        Validation.validate_type(name, str, 'name should be a string.')
        AccountValidator.number(owner_id)
        Validation.validate_type(vpc_id, str, 'vpc_id should be a string.')
        Validation.validate_type(ip_permissions, Union[list, None], 'ip_permissions should be a list of IPPermission.')
        if ip_permissions is not None and len(ip_permissions) > 0:
            all(
                Validation.validate_type(
                    ip_permission, IPPermission, 'ip_permissions should be a list of IPPermission.'
                ) for ip_permission in ip_permissions
            )
        Validation.validate_type(
            ip_permissions_egress, Union[list, None], 'ip_permissions_egress should be a list of IPPermission.'
        )
        if ip_permissions_egress is not None and len(ip_permissions_egress) > 0:
            all(
                Validation.validate_type(
                    ip_permission, IPPermission, 'ip_permissions_egress should be a list of IPPermission.'
                ) for ip_permission in ip_permissions_egress
            )
        Validation.validate_type(description, Union[str, None], 'description should be a string.')
        Validation.validate_type(tags, Union[list, None], 'tags should be a list.')

        self._account = account
        self._region = region
        self._id = id
        self._name = name
        self._owner_id = owner_id
        self._vpc_id = vpc_id
        self._ip_permissions = ip_permissions
        self._ip_permissions_egress = ip_permissions_egress
        self._description = description
        self._tags = tags

    @property
    def account(self) -> IAccount:
        """
        Gets the account associated with the EC2 security group.
        :return: The account associated with the EC2 security group.
        :rtype: IAccount
        """
        return self._account

    @account.setter
    def account(self, value: IAccount) -> None:
        """
        Sets the account associated with the EC2 security group.
        :param value: The account to be associated with the EC2 security group.
        :type value: IAccount
        """
        Validation.validate_type(value, IAccount, 'account should be of Account type.')
        self._account = value

    @property
    def description(self) -> Optional[str]:
        """
        Gets the description of the EC2 security group.
        :return: The description of the EC2 security group.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, value: Optional[str]) -> None:
        """
        Sets the description of the EC2 security group.
        :param value: The description of the EC2 security group.
        :type value: str
        """
        Validation.validate_type(value, Union[str, None], 'description should be a string.')
        self._description = value

    @property
    def id(self) -> str:
        """
        Gets the unique identifier of the EC2 security group.
        :return: The unique identifier of the EC2 security group.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        """
        Sets the unique identifier of the EC2 security group.
        :param value: The unique identifier of the EC2 security group.
        :type value: str
        """
        Validation.validate_type(value, str, 'id should be a string.')
        self._id = value

    @property
    def ip_permissions(self) -> Optional[list[IPPermission]]:
        """
        Gets the list of inbound rule entries of the EC2 security group.
        :return: The list of inbound rule entries of the EC2 security group.
        :rtype: list
        """
        return self._ip_permissions

    @ip_permissions.setter
    def ip_permissions(self, value: Optional[list[IPPermission]]) -> None:
        """
        Sets the list of inbound rule entries of the EC2 security group.
        :param value: The list of inbound rule entries of the EC2 security group.
        :type value: list
        """
        Validation.validate_type(value, Union[list, None], 'ip_permissions should be a list of IPPermission.')
        if value is not None and len(value) > 0:
            all(
                Validation.validate_type(ip_permission, IPPermission,
                                         'ip_permissions should be a list of IPPermission.')
                for ip_permission in value
            )
        self._ip_permissions = value

    @property
    def ip_permissions_egress(self) -> Optional[list[IPPermission]]:
        """
        Gets the list of outbound rule entries of the EC2 security group.
        :return: The list of outbound rule entries of the EC2 security group.
        :rtype: list
        """
        return self._ip_permissions_egress

    @ip_permissions_egress.setter
    def ip_permissions_egress(self, value: Optional[list[IPPermission]]) -> None:
        """
        Sets the list of outbound rule entries of the EC2 security group.
        :param value: The list of outbound rule entries of the EC2 security group.
        :type value: list
        """
        Validation.validate_type(value, Union[list, None], 'ip_permissions_egress should be a list of IPPermission.')
        if value is not None and len(value) > 0:
            all(
                Validation.validate_type(
                    ip_permission, IPPermission, 'ip_permissions_egress should be a list of IPPermission.'
                )
                for ip_permission in value
            )
        self._ip_permissions_egress = value

    @property
    def name(self) -> str:
        """
        Gets the name of the EC2 security group.
        :return: The name of the EC2 security group.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Sets the name of the EC2 security group.
        :param value: The name of the EC2 security group.
        :type value: str
        """
        Validation.validate_type(value, str, 'name should be a string.')
        self._name = value

    @property
    def owner_id(self) -> str:
        """
        Gets the owner id of the EC2 security group.
        :return: The owner id of the EC2 security group.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value: str) -> None:
        """
        Sets the owner id of the EC2 security group.
        :param value: The owner id of the EC2 security group.
        :type value: str
        """
        AccountValidator.number(value)
        self._owner_id = value

    @property
    def region(self) -> str:
        """
        Gets the region associated with the EC2 security group.
        :return: The region associated with the EC2 security group.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, value: str) -> None:
        """
        Sets the region associated with the EC2 security group.
        :param value: The region associated with the EC2 security group.
        :type value: str
        """
        Validator.region(value, True)
        self._region = value

    @property
    def tags(self) -> Optional[list]:
        """
        Gets the tags of the EC2 security group.
        :return: The tags of the EC2 security group.
        :rtype: list
        """
        return self._tags

    @tags.setter
    def tags(self, value: Optional[list]) -> None:
        """
        Sets the tags of the EC2 security group.
        :param value: The tags of the EC2 security group.
        :type value: list
        """
        Validation.validate_type(value, Union[list, None], 'tags should be a list.')
        self._tags = value

    @property
    def vpc_id(self) -> str:
        """
        Gets the VPC id of the EC2 security group.
        :return: The VPC id of the EC2 security group.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, value: str) -> None:
        """
        Sets the VPC id of the EC2 security group.
        :param value: The VPC id of the EC2 security group.
        :type value: str
        """
        Validation.validate_type(value, str, 'vpc_id should be a string.')
        self._vpc_id = value

    def __str__(self) -> str:
        """
        Returns a string representation of the SecurityGroup instance.
        :return: String representation of the SecurityGroup instance.
        :rtype: str
        """
        ip_permissions = self.ip_permissions if self.ip_permissions and len(self.ip_permissions) > 0 else None
        ip_permissions_egress = (
            self.ip_permissions_egress if self.ip_permissions_egress and len(self.ip_permissions_egress) > 0 else None
        )
        description = f'"{self.description}"' if self.description else None
        tags = self.tags if self.tags else None

        return (
            f'SecurityGroup('
            f'account={self.account},'
            f'region="{self.region}",'
            f'id="{self.id}",'
            f'name="{self.name}",'
            f'owner_id="{self.owner_id}",'
            f'vpc_id="{self.vpc_id}",'
            f'ip_permissions={ip_permissions},'
            f'ip_permissions_egress={ip_permissions_egress},'
            f'description={description},'
            f'tags={tags}'
            f')'
        )

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the SecurityGroup instance.
        :return: Dictionary representation of the SecurityGroup instance.
        :rtype: dict
        """
        ip_permissions = [
            ip_perm.to_dict() for ip_perm in self.ip_permissions
        ] if self.ip_permissions and len(self.ip_permissions) else None
        ip_permissions_egress = [
            ip_perm.to_dict() for ip_perm in self.ip_permissions_egress
        ] if self.ip_permissions_egress and len(self.ip_permissions_egress) else None
        tags = self.tags if self.tags else None

        return {
            "account": self.account.to_dict(),
            "region": self.region,
            "id": self.id,
            "name": self.name,
            "owner_id": self.owner_id,
            "vpc_id": self.vpc_id,
            "ip_permissions": ip_permissions,
            "ip_permissions_egress": ip_permissions_egress,
            "description": self.description,
            "tags": tags
        }
