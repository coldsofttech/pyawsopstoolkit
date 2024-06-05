import unittest

from pyawsopstoolkit.models.ec2.network_interface import Association, PrivateIPAddress


class TestPrivateIPAddress(unittest.TestCase):
    """Unit test cases for PrivateIPAddress."""

    def setUp(self) -> None:
        self.maxDiff = None
        self.params = {
            'address': '10.0.0.2',
            'dns_name': 'ip-10-0-0-2.ec2.internal',
            'is_primary': True,
            'association': Association(
                id='eipassoc-0123456789abcdef0',
                allocation_id='eipalloc-0123456789abcdef0',
                ip_owner_id='123456789012',
                public_ip='203.0.113.25',
                public_dns_name='ec2-203-0-113-25.compute-1.amazonaws.com',
                customer_owned_ip='198.51.100.25',
                carrier_ip='192.0.2.25'
            )
        }
        self.private_ip_address = self.create_private_ip_address()
        self.private_ip_address_with_primary = self.create_private_ip_address(is_primary=self.params['is_primary'])
        self.private_ip_address_with_association = self.create_private_ip_address(
            association=self.params['association']
        )
        self.private_ip_address_full = self.create_private_ip_address(
            is_primary=self.params['is_primary'],
            association=self.params['association']
        )

    def create_private_ip_address(self, **kwargs):
        return PrivateIPAddress(
            address=self.params['address'],
            dns_name=self.params['dns_name'],
            **kwargs
        )

    def test_initialization(self):
        self.assertEqual(self.private_ip_address.address, self.params['address'])
        self.assertEqual(self.private_ip_address.dns_name, self.params['dns_name'])
        self.assertFalse(self.private_ip_address.is_primary)
        self.assertIsNone(self.private_ip_address.association)

    def test_initialization_with_optional_params(self):
        test_cases = [
            (self.private_ip_address_with_primary, self.params['is_primary'], None),
            (self.private_ip_address_with_association, False, self.params['association']),
            (self.private_ip_address_full, self.params['is_primary'], self.params['association'])
        ]
        for ip_address, is_primary, association in test_cases:
            with self.subTest(ip_address=ip_address):
                self.assertEqual(ip_address.address, self.params['address'])
                self.assertEqual(ip_address.dns_name, self.params['dns_name'])
                self.assertEqual(ip_address.is_primary, is_primary)
                self.assertEqual(ip_address.association, association)

    def test_setters(self):
        new_params = {
            'address': '10.0.0.1',
            'dns_name': 'ip-10-0-0-1.ec2.internal',
            'is_primary': False,
            'association': Association(
                id='eipassoc-0123456789abcdef1',
                allocation_id='eipalloc-0123456789abcdef1',
                ip_owner_id='987654321012',
                public_ip='203.0.113.20',
                public_dns_name='ec2-203-0-113-20.compute-1.amazonaws.com',
                customer_owned_ip='198.51.100.20',
                carrier_ip='192.0.2.20'
            )
        }

        self.private_ip_address_full.address = new_params['address']
        self.private_ip_address_full.dns_name = new_params['dns_name']
        self.private_ip_address_full.is_primary = new_params['is_primary']
        self.private_ip_address_full.association = new_params['association']

        self.assertEqual(self.private_ip_address_full.address, new_params['address'])
        self.assertEqual(self.private_ip_address_full.dns_name, new_params['dns_name'])
        self.assertEqual(self.private_ip_address_full.is_primary, new_params['is_primary'])
        self.assertEqual(self.private_ip_address_full.association, new_params['association'])

    def test_invalid_types(self):
        invalid_params = {
            'address': 123,
            'dns_name': 123,
            'is_primary': 'False',
            'association': 123
        }

        with self.assertRaises(TypeError):
            PrivateIPAddress(invalid_params['address'], self.params['dns_name'])
        with self.assertRaises(TypeError):
            PrivateIPAddress(self.params['address'], invalid_params['dns_name'])
        with self.assertRaises(TypeError):
            self.create_private_ip_address(is_primary=invalid_params['is_primary'])
        with self.assertRaises(TypeError):
            self.create_private_ip_address(association=invalid_params['association'])

        with self.assertRaises(TypeError):
            self.private_ip_address_full.address = invalid_params['address']
        with self.assertRaises(TypeError):
            self.private_ip_address_full.dns_name = invalid_params['dns_name']
        with self.assertRaises(TypeError):
            self.private_ip_address_full.is_primary = invalid_params['is_primary']
        with self.assertRaises(TypeError):
            self.private_ip_address_full.association = invalid_params['association']

    def test_to_dict(self):
        expected_dict = {
            "address": self.params['address'],
            "dns_name": self.params['dns_name'],
            "is_primary": self.params['is_primary'],
            "association": self.params['association'].to_dict()
        }
        self.assertDictEqual(self.private_ip_address_full.to_dict(), expected_dict)

    def test_to_dict_with_missing_fields(self):
        expected_dict = {
            "address": self.params['address'],
            "dns_name": self.params['dns_name'],
            "is_primary": False,
            "association": None
        }
        self.assertDictEqual(self.private_ip_address.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
