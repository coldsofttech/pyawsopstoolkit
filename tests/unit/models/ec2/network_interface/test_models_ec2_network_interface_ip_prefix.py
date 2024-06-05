import unittest

from pyawsopstoolkit.models.ec2.network_interface import IPPrefix


class TestIPPrefix(unittest.TestCase):
    """Unit test cases for IPPrefix."""

    def setUp(self) -> None:
        self.maxDiff = None
        self.params = {
            'prefix_v4': '198.51.100.0/24',
            'prefix_v6': '2001:db8::/64',
            'is_ipv6': True
        }
        self.prefix = self.create_ip_prefix()
        self.prefix_full = self.create_ip_prefix(is_ipv6=self.params['is_ipv6'])

    def create_ip_prefix(self, **kwargs):
        if kwargs.get('is_ipv6', False):
            return IPPrefix(prefix=self.params['prefix_v6'], **kwargs)
        else:
            return IPPrefix(prefix=self.params['prefix_v4'], **kwargs)

    def test_initialization(self):
        self.assertEqual(self.prefix.prefix, self.params['prefix_v4'])

    def test_initialization_with_optional_params(self):
        test_cases = [
            (self.prefix_full, self.params['prefix_v6'], self.params['is_ipv6'])
        ]
        for prefix_obj, prefix, is_ipv6 in test_cases:
            with self.subTest(prefix_obj=prefix_obj):
                self.assertEqual(prefix_obj.prefix, prefix)
                self.assertEqual(prefix_obj.is_ipv6, is_ipv6)

    def test_setters(self):
        new_params = {
            'prefix_v4': '198.51.100.0/24',
            'is_ipv6': False
        }

        self.prefix_full.prefix = new_params['prefix_v4']
        self.prefix_full.is_ipv6 = new_params['is_ipv6']
        self.assertEqual(self.prefix_full.prefix, new_params['prefix_v4'])
        self.assertEqual(self.prefix_full.is_ipv6, new_params['is_ipv6'])

    def test_invalid_types(self):
        invalid_params = {
            'prefix_v4': 123,
            'is_ipv6': 'False'
        }

        with self.assertRaises(TypeError):
            IPPrefix(invalid_params['prefix_v4'])
        with self.assertRaises(TypeError):
            self.create_ip_prefix(is_ipv6=invalid_params['is_ipv6'])
        with self.assertRaises(TypeError):
            self.prefix_full.prefix = invalid_params['prefix_v4']
        with self.assertRaises(TypeError):
            self.prefix_full.is_ipv6 = invalid_params['is_ipv6']

    def test_to_dict(self):
        expected_dict = {
            "prefix": self.params['prefix_v6'],
            "is_ipv6": self.params['is_ipv6']
        }
        self.assertDictEqual(self.prefix_full.to_dict(), expected_dict)

    def test_to_dict_with_missing_fields(self):
        expected_dict = {
            "prefix": self.params['prefix_v4'],
            "is_ipv6": False
        }
        self.assertDictEqual(self.prefix.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
