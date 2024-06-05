import unittest

from pyawsopstoolkit.models.ec2.network_interface import IPv6Address


class TestIPv6Address(unittest.TestCase):
    """Unit test cases for IPv6Address."""

    def setUp(self) -> None:
        self.maxDiff = None
        self.params = {
            'address': '2001:db8::1234:5678:abcd:ef12',
            'is_primary': True
        }
        self.ipv6_address = self.create_ipv6_address()
        self.ipv6_address_full = self.create_ipv6_address(is_primary=self.params['is_primary'])

    def create_ipv6_address(self, **kwargs):
        return IPv6Address(address=self.params['address'], **kwargs)

    def test_initialization(self):
        self.assertEqual(self.ipv6_address.address, self.params['address'])
        self.assertFalse(self.ipv6_address.is_primary)

    def test_initialization_with_optional_params(self):
        test_cases = [
            (self.ipv6_address_full, self.params['is_primary'])
        ]
        for ipv6_address, is_primary in test_cases:
            with self.subTest(ipv6_address=ipv6_address):
                self.assertEqual(ipv6_address.address, self.params['address'])
                self.assertEqual(ipv6_address.is_primary, is_primary)

    def test_setters(self):
        new_params = {
            'address': '2001:db8::1234:5678:abcd:ef13',
            'is_primary': False
        }

        self.ipv6_address_full.address = new_params['address']
        self.ipv6_address_full.is_primary = new_params['is_primary']
        self.assertEqual(self.ipv6_address_full.address, new_params['address'])
        self.assertEqual(self.ipv6_address_full.is_primary, new_params['is_primary'])

    def test_invalid_types(self):
        invalid_params = {
            'address': 123,
            'is_primary': 'False'
        }

        with self.assertRaises(TypeError):
            IPv6Address(invalid_params['address'])
        with self.assertRaises(TypeError):
            self.create_ipv6_address(is_primary=invalid_params['is_primary'])

        with self.assertRaises(TypeError):
            self.ipv6_address_full.address = invalid_params['address']
        with self.assertRaises(TypeError):
            self.ipv6_address_full.is_primary = invalid_params['is_primary']

    def test_to_dict(self):
        expected_dict = {
            "address": self.params['address'],
            "is_primary": self.params['is_primary']
        }
        self.assertDictEqual(self.ipv6_address_full.to_dict(), expected_dict)

    def test_to_dict_with_missing_fields(self):
        expected_dict = {
            "address": self.params['address'],
            "is_primary": False
        }
        self.assertDictEqual(self.ipv6_address.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
