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


class PrefixListID:
    """
    A class representing Prefix List for a EC2 Security Group.
    """

    def __init__(self, id: str, description: Optional[str] = None) -> None:
        """
        Initializes a new PrefixListID instance with specified parameters.
        :param id: The unique identifier for the prefix list.
        :type id: str
        :param description: The description of the prefix list.
        :type description: str
        """
        Validation.validate_type(id, str, 'id should be a string.')
        Validation.validate_type(description, Union[str, None], 'description should be a string.')

        self._id = id
        self._description = description

    @property
    def id(self) -> str:
        """
        Gets the unique identifier of the prefix list.
        :return: The unique identifier of the prefix list.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        """
        Sets the unique identifier of the prefix list.
        :param value: The unique identifier of the prefix list.
        :type value: str
        """
        Validation.validate_type(value, str, 'id should be a string.')
        self._id = value

    @property
    def description(self) -> Optional[str]:
        """
        Gets the description of the prefix list.
        :return: The description of the prefix list.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, value: Optional[str]) -> None:
        """
        Sets the description of the prefix list.
        :param value: The description of the prefix list.
        :type value: str
        """
        Validation.validate_type(value, Union[str, None], 'description should be a string.')
        self._description = value

    def __str__(self) -> str:
        """
        Returns a string representation of the PrefixListID instance.
        :return: String representation of the PrefixListID instance.
        :rtype: str
        """
        description = f'"{self.description}"' if self.description else None

        return (
            f'PrefixListID('
            f'id="{self.id}",'
            f'description={description}'
            f')'
        )

    def __repr__(self) -> str:
        """
        Returns a detailed string representation of the PrefixListID instance.
        :return: Detailed string representation of the PrefixListID instance.
        :rtype: str
        """
        return self.__str__()

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the PrefixListID instance.
        :return: Dictionary representation of the PrefixListID instance.
        :rtype: dict
        """
        return {
            "id": self.id,
            "description": self.description
        }


class UserIDGroupPair:
    """
    A class representing User ID Group Pair for a EC2 Security Group.
    """

    def __init__(
            self,
            id: str,
            name: str,
            status: str,
            user_id: str,
            vpc_id: str,
            description: Optional[str] = None,
            vpc_peering_connection_id: Optional[str] = None
    ) -> None:
        """
        Initializes a new UserIDGroupPair instance with specified parameters.
        :param id: The unique identifier for the user id group pair.
        :type id: str
        :param name: The name for the user id group pair.
        :type name: str
        :param status: The status of the user id group pair.
        :type status: str
        :param user_id: The owner / user id of the user id group pair.
        :type user_id: str
        :param vpc_id: The VPC id of the user id group pair.
        :type vpc_id: str
        :param description: The description of the user id group pair.
        :type description: str
        :param vpc_peering_connection_id: The VPC peering connection id of the user id group pair.
        :type vpc_peering_connection_id: str
        """
        Validation.validate_type(id, str, 'id should be a string.')
        Validation.validate_type(name, str, 'name should be a string.')
        Validation.validate_type(status, str, 'status should be a string.')
        Validation.validate_type(user_id, str, 'user_id should be a string.')
        Validation.validate_type(vpc_id, str, 'vpc_id should be a string.')
        Validation.validate_type(description, Union[str, None], 'description should be a string.')
        Validation.validate_type(
            vpc_peering_connection_id, Union[str, None], 'vpc_peering_connection_id should be a string.'
        )

        self._id = id
        self._name = name
        self._status = status
        self._user_id = user_id
        self._vpc_id = vpc_id
        self._description = description
        self._vpc_peering_connection_id = vpc_peering_connection_id

    @property
    def description(self) -> Optional[str]:
        """
        Gets the description of the user id group pair.
        :return: The description of the user id group pair.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, value: Optional[str]) -> None:
        """
        Sets the description of the user id group pair.
        :param value: The description of the user id group pair.
        :type value: str
        """
        Validation.validate_type(value, Union[str, None], 'description should be a string.')
        self._description = value

    @property
    def id(self) -> str:
        """
        Gets the unique identifier of the user id group pair.
        :return: The unique identifier of the user id group pair.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        """
        Sets the unique identifier of the user id group pair.
        :param value: The unique identifier of the user id group pair.
        :type value: str
        """
        Validation.validate_type(value, str, 'id should be a string.')
        self._id = value

    @property
    def name(self) -> str:
        """
        Gets the name of the user id group pair.
        :return: The name of the user id group pair.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Sets the name of the user id group pair.
        :param value: The name of the user id group pair.
        :type value: str
        """
        Validation.validate_type(value, str, 'name should be a string.')
        self._name = value

    @property
    def status(self) -> str:
        """
        Gets the status of the user id group pair
        :return: The status of the user id group pair
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        """
        Sets the status of the user id group pair
        :param value: The status of the user id group pair.
        :type value: str
        """
        Validation.validate_type(value, str, 'status should be a string.')
        self._status = value

    @property
    def user_id(self) -> str:
        """
        Gets the owner / user id of the user id group pair.
        :return: The owner / user id of the user id group pair.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, value: str) -> None:
        """
        Sets the owner / user id of the user id group pair.
        :param value: The owner / user id of the user id group pair.
        :type value: str
        """
        Validation.validate_type(value, str, 'user_id should be a string.')
        self._user_id = value

    @property
    def vpc_id(self) -> str:
        """
        Gets the VPC id of the user id group pair.
        :return: The VPC id of the user id group pair.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, value: str) -> None:
        """
        Sets the VPC id of the user id group pair.
        :param value: The VPC id of the user id group pair.
        :type value: str
        """
        Validation.validate_type(value, str, 'vpc_id should be a string.')
        self._vpc_id = value

    @property
    def vpc_peering_connection_id(self) -> Optional[str]:
        """
        Gets the VPC peering connection id of the user id group pair.
        :return: The VPC peering connection id of the user id group pair.
        :rtype: str
        """
        return self._vpc_peering_connection_id

    @vpc_peering_connection_id.setter
    def vpc_peering_connection_id(self, value: Optional[str]) -> None:
        """
        Sets the VPC peering connection id of the user id group pair.
        :param value: The VPC peering connection id of the user id group pair.
        :type value: str
        """
        Validation.validate_type(value, Union[str, None], 'vpc_peering_connection_id should be a string.')
        self._vpc_peering_connection_id = value

    def __str__(self) -> str:
        """
        Returns a string representation of the UserIDGroupPair instance.
        :return: String representation of the UserIDGroupPair instance.
        :rtype: str
        """
        description = f'"{self.description}"' if self.description else None
        vpc_peering_connection_id = f'"{self.vpc_peering_connection_id}"' if self.vpc_peering_connection_id else None

        return (
            f'UserIDGroupPair('
            f'id="{self.id}",'
            f'name="{self.name}",'
            f'status="{self.status}",'
            f'user_id="{self.user_id}",'
            f'vpc_id="{self.vpc_id}",'
            f'description={description},'
            f'vpc_peering_connection_id={vpc_peering_connection_id}'
            f')'
        )

    def __repr__(self) -> str:
        """
        Returns a detailed string representation of the UserIDGroupPair instance.
        :return: Detailed string representation of the UserIDGroupPair instance.
        :rtype: str
        """
        return self.__str__()

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


class IPPermission:
    """
    A class representing the IP Permissions for a EC2 Security Group.
    """

    def __init__(
            self,
            from_port: int,
            to_port: int,
            ip_protocol: str,
            ip_ranges: Optional[list[IPRange]] = None,
            ipv6_ranges: Optional[list[IPv6Range]] = None,
            prefix_list_ids: Optional[list[PrefixListID]] = None,
            user_id_group_pairs: Optional[list[UserIDGroupPair]] = None
    ) -> None:
        """
        Initializes a new IPPermission object with specified parameters.
        :param from_port: The from port of an EC2 security group rule entry.
        :type from_port: int
        :param to_port: The to port of an EC2 security group rule entry.
        :type to_port: int
        :param ip_protocol: The IP protocol of an EC2 security group rule entry.
        :type ip_protocol: str
        :param ip_ranges: The list of IPv4 ranges of an EC2 security group rule entry.
        :type ip_ranges: list
        :param ipv6_ranges: The list of IPv6 ranges of an EC2 security group rule entry.
        :type ipv6_ranges: list
        :param prefix_list_ids: The list of prefix lists of an EC2 security group rule entry.
        :type prefix_list_ids: list
        :param user_id_group_pairs: The list of user id group pairs of an EC2 security group rule entry.
        :type user_id_group_pairs: list
        """
        Validation.validate_type(from_port, int, 'from_port should be an integer.')
        Validation.validate_type(to_port, int, 'to_port should be an integer.')
        Validation.validate_type(ip_protocol, str, 'ip_protocol should be a string.')
        Validation.validate_type(ip_ranges, Union[list, None], 'ip_ranges should be a list of IPRange.')
        if ip_ranges is not None and len(ip_ranges) > 0:
            all(
                Validation.validate_type(ip_range, IPRange, 'ip_ranges should be a list of IPRange.')
                for ip_range in ip_ranges
            )
        Validation.validate_type(ipv6_ranges, Union[list, None], 'ipv6_ranges should be a list of IPv6Range.')
        if ipv6_ranges is not None and len(ipv6_ranges) > 0:
            all(
                Validation.validate_type(ip_range, IPv6Range, 'ipv6_ranges should be a list of IPv6Range.')
                for ip_range in ipv6_ranges
            )
        Validation.validate_type(
            prefix_list_ids, Union[list, None], 'prefix_list_ids should be a list of PrefixListID.'
        )
        if prefix_list_ids is not None and len(prefix_list_ids) > 0:
            all(
                Validation.validate_type(
                    prefix_list_id, PrefixListID, 'prefix_list_ids should be a list of PrefixListID.'
                )
                for prefix_list_id in prefix_list_ids
            )
        Validation.validate_type(
            user_id_group_pairs, Union[list, None], 'user_id_group_pairs should be a list of UserIDGroupPair.'
        )
        if user_id_group_pairs is not None and len(user_id_group_pairs) > 0:
            all(
                Validation.validate_type(
                    user_id_group_pair, UserIDGroupPair, 'user_id_group_pairs should be a list of UserIDGroupPair.'
                )
                for user_id_group_pair in user_id_group_pairs
            )

        self._from_port = from_port
        self._to_port = to_port
        self._ip_protocol = ip_protocol
        self._ip_ranges = ip_ranges
        self._ipv6_ranges = ipv6_ranges
        self._prefix_list_ids = prefix_list_ids
        self._user_id_group_pairs = user_id_group_pairs

    @property
    def from_port(self) -> int:
        """
        Gets the from port of an EC2 security group rule entry.
        :return: The from port of an EC2 security group rule entry.
        :rtype: int
        """
        return self._from_port

    @from_port.setter
    def from_port(self, value: int) -> None:
        """
        Sets the from port of an EC2 security group rule entry.
        :param value: The from port of an EC2 security group rule entry.
        :type value: int
        """
        Validation.validate_type(value, int, 'from_port should be an integer.')
        self._from_port = value

    @property
    def ip_protocol(self) -> str:
        """
        Gets the IP protocol of an EC2 security group rule entry.
        :return: The IP protocol of an EC2 security group rule entry.
        :rtype: str
        """
        return self._ip_protocol

    @ip_protocol.setter
    def ip_protocol(self, value: str) -> None:
        """
        Sets the IP protocol of an EC2 security group rule entry.
        :param value: The IP protocol of an EC2 security group rule entry.
        :type value: str
        """
        Validation.validate_type(value, str, 'ip_protocol should be a string.')
        self._ip_protocol = value

    @property
    def ip_ranges(self) -> Optional[list[IPRange]]:
        """
        Gets the list of IPv4 ranges of an EC2 security group rule entry.
        :return: The list of IPv4 ranges of an EC2 security group rule entry.
        :rtype: list
        """
        return self._ip_ranges

    @ip_ranges.setter
    def ip_ranges(self, value: Optional[list[IPRange]]) -> None:
        """
        Sets the list of IPv4 ranges of an EC2 security group rule entry.
        :param value: The list of IPv4 ranges of an EC2 security group rule entry.
        :type value: list
        """
        Validation.validate_type(value, Union[list, None], 'ip_ranges should be a list of IPRange.')
        if value is not None and len(value) > 0:
            all(
                Validation.validate_type(ip_range, IPRange, 'ip_ranges should be a list of IPRange.')
                for ip_range in value
            )
        self._ip_ranges = value

    @property
    def ipv6_ranges(self) -> Optional[list[IPv6Range]]:
        """
        Gets the list of IPv6 ranges of an EC2 security group rule entry.
        :return: The list of IPv6 ranges of an EC2 security group rule entry.
        :rtype: list
        """
        return self._ipv6_ranges

    @ipv6_ranges.setter
    def ipv6_ranges(self, value: Optional[list[IPv6Range]]):
        """
        Sets the list of IPv6 ranges of an EC2 security group rule entry.
        :param value: The list of IPv6 ranges of an EC2 security group rule entry.
        :type value: list
        """
        Validation.validate_type(value, Union[list, None], 'ipv6_ranges should be a list of IPv6Range.')
        if value is not None and len(value) > 0:
            all(
                Validation.validate_type(ip_range, IPv6Range, 'ipv6_ranges should be a list of IPv6Range.')
                for ip_range in value
            )
        self._ipv6_ranges = value

    @property
    def prefix_list_ids(self) -> Optional[list[PrefixListID]]:
        """
        Gets the list of prefix lists of an EC2 security group rule entry.
        :return: The list of prefix lists of an EC2 security group rule entry.
        :rtype: list
        """
        return self._prefix_list_ids

    @prefix_list_ids.setter
    def prefix_list_ids(self, value: Optional[list[PrefixListID]]) -> None:
        """
        Sets the list of prefix lists of an EC2 security group rule entry.
        :param value: The list of prefix lists of an EC2 security group rule entry.
        :type value: list
        """
        Validation.validate_type(value, Union[list, None], 'prefix_list_ids should be a list of PrefixListID.')
        if value is not None and len(value) > 0:
            all(
                Validation.validate_type(
                    prefix_list_id, PrefixListID, 'prefix_list_ids should be a list of PrefixListID.'
                )
                for prefix_list_id in value
            )
        self._prefix_list_ids = value

    @property
    def to_port(self) -> int:
        """
        Gets the to port of an EC2 security group rule entry.
        :return: The to port of an EC2 security group rule entry.
        :rtype: int
        """
        return self._to_port

    @to_port.setter
    def to_port(self, value: int) -> None:
        """
        Sets the to port of an EC2 security group rule entry.
        :param value: The to port of an EC2 security group rule entry.
        :type value: int
        """
        Validation.validate_type(value, int, 'to_port should be an integer.')
        self._to_port = value

    @property
    def user_id_group_pairs(self) -> Optional[list[UserIDGroupPair]]:
        """
        Gets the list of user id group pairs of an EC2 security group rule entry.
        :return: The list of user id group pairs of an EC2 security group rule entry.
        :rtype: list
        """
        return self._user_id_group_pairs

    @user_id_group_pairs.setter
    def user_id_group_pairs(self, value: Optional[list[UserIDGroupPair]]) -> None:
        """
        Sets the list of user id group pairs of an EC2 security group rule entry.
        :param value: The list of user id group pairs of an EC2 security group rule entry.
        :type value: list
        """
        Validation.validate_type(value, Union[list, None], 'user_id_group_pairs should be a list of UserIDGroupPair.')
        if value is not None and len(value) > 0:
            all(
                Validation.validate_type(
                    user_id_group_pair, UserIDGroupPair, 'user_id_group_pairs should be a list of UserIDGroupPair.'
                )
                for user_id_group_pair in value
            )
        self._user_id_group_pairs = value

    def __str__(self) -> str:
        """
        Returns a string representation of the IPPermission instance.
        :return: String representation of the IPPermission instance.
        :rtype: str
        """
        ip_ranges = self.ip_ranges if self.ip_ranges and len(self.ip_ranges) > 0 else None
        ipv6_ranges = self.ipv6_ranges if self.ipv6_ranges and len(self.ipv6_ranges) > 0 else None
        prefix_list_ids = self.prefix_list_ids if self.prefix_list_ids and len(self.prefix_list_ids) > 0 else None
        user_id_group_pairs = (
            self.user_id_group_pairs if self.user_id_group_pairs and len(self.user_id_group_pairs) else None
        )

        return (
            f'IPPermission('
            f'from_port={self.from_port},'
            f'to_port={self.to_port},'
            f'ip_protocol="{self.ip_protocol}",'
            f'ip_ranges={ip_ranges},'
            f'ipv6_ranges={ipv6_ranges},'
            f'prefix_list_ids={prefix_list_ids},'
            f'user_id_group_pairs={user_id_group_pairs}'
            f')'
        )

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the IPPermission instance.
        :return: Dictionary representation of the IPPermission instance.
        :rtype: dict
        """
        ip_ranges = [
            ip.to_dict() for ip in self.ip_ranges
        ] if self.ip_ranges and len(self.ip_ranges) > 0 else None
        ipv6_ranges = [
            ip.to_dict() for ip in self.ipv6_ranges
        ] if self.ipv6_ranges and len(self.ipv6_ranges) > 0 else None
        prefix_list_ids = [
            prefix.to_dict() for prefix in self.prefix_list_ids
        ] if self.prefix_list_ids and len(self.prefix_list_ids) > 0 else None
        user_id_group_pairs = [
            pair.to_dict() for pair in self.user_id_group_pairs
        ] if self.user_id_group_pairs and len(self.user_id_group_pairs) > 0 else None

        return {
            "from_port": self.from_port,
            "to_port": self.to_port,
            "ip_protocol": self.ip_protocol,
            "ip_ranges": ip_ranges,
            "ipv6_ranges": ipv6_ranges,
            "prefix_list_ids": prefix_list_ids,
            "user_id_group_pairs": user_id_group_pairs
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
