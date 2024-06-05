from dataclasses import dataclass

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
