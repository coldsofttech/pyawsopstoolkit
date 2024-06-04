import unittest

from pyawsopstoolkit.models.ec2.security_group import IPv6Range


class TestIPv6Range(unittest.TestCase):
    """Unit test cases for IPv6Range."""

    def setUp(self) -> None:
        self.maxDiff = None
        self.params = {
            'cidr_ipv6': '2001:db8::/32',
            'description': '2001:db8::/32 IPv6 Series'
        }
        self.ipv6_range = self.create_ipv6_range()
        self.ipv6_range_full = self.create_ipv6_range(description=self.params['description'])

    def create_ipv6_range(self, **kwargs):
        return IPv6Range(self.params['cidr_ipv6'], **kwargs)

    def test_initialization(self):
        self.assertEqual(self.ipv6_range.cidr_ipv6, self.params['cidr_ipv6'])
        self.assertIsNone(self.ipv6_range.description)

    def test_initialization_with_optional_params(self):
        test_cases = [
            (self.ipv6_range_full, self.params['description'])
        ]
        for ipv6_range, description in test_cases:
            with self.subTest(ipv6_range=ipv6_range):
                self.assertEqual(ipv6_range.cidr_ipv6, self.params['cidr_ipv6'])
                self.assertEqual(ipv6_range.description, description)

    def test_setters(self):
        new_params = {
            'cidr_ipv6': '2001:db8::/64',
            'description': '2001:db8::/64 IPv6 Series'
        }

        self.ipv6_range_full.cidr_ipv6 = new_params['cidr_ipv6']
        self.ipv6_range_full.description = new_params['description']

        self.assertEqual(self.ipv6_range_full.cidr_ipv6, new_params['cidr_ipv6'])
        self.assertEqual(self.ipv6_range_full.description, new_params['description'])

    def test_invalid_types(self):
        invalid_params = {
            'cidr_ipv6': 123,
            'description': 123
        }

        with self.assertRaises(TypeError):
            IPv6Range(invalid_params['cidr_ipv6'])
        with self.assertRaises(TypeError):
            self.create_ipv6_range(description=invalid_params['description'])

        with self.assertRaises(TypeError):
            self.ipv6_range_full.cidr_ipv6 = invalid_params['cidr_ipv6']
        with self.assertRaises(TypeError):
            self.ipv6_range_full.description = invalid_params['description']

    def test_to_dict(self):
        expected_dict = {
            "cidr_ipv6": self.params['cidr_ipv6'],
            "description": self.params['description']
        }
        self.assertDictEqual(self.ipv6_range_full.to_dict(), expected_dict)

    def test_to_dict_with_missing_fields(self):
        expected_dict = {
            "cidr_ipv6": self.params['cidr_ipv6'],
            "description": None
        }
        self.assertDictEqual(self.ipv6_range.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
