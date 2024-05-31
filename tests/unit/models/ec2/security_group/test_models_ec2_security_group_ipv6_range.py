import unittest

from pyawsopstoolkit.models.ec2.security_group import IPv6Range


class TestIPv6Range(unittest.TestCase):
    """Unit test cases for IPv6Range."""

    def setUp(self) -> None:
        self.cidr_ipv6 = '2001:db8::/32'
        self.description = '2001:db8::/32 IPv6 Series'
        self.ipv6_range = IPv6Range(self.cidr_ipv6)
        self.ipv6_range_full = IPv6Range(self.cidr_ipv6, self.description)

    def test_initialization(self):
        self.assertEqual(self.ipv6_range.cidr_ipv6, self.cidr_ipv6)
        self.assertIsNone(self.ipv6_range.description)

    def test_initialization_full(self):
        self.assertEqual(self.ipv6_range_full.cidr_ipv6, self.cidr_ipv6)
        self.assertEqual(self.ipv6_range_full.description, self.description)

    def test_set_cidr_ipv6(self):
        new_cidr_ipv6 = 'fd12:3456:789a::/48'
        self.ipv6_range_full.cidr_ip = new_cidr_ipv6
        self.assertEqual(self.ipv6_range_full.cidr_ip, new_cidr_ipv6)

    def test_set_description(self):
        new_description = 'New IP Series'
        self.ipv6_range_full.description = new_description
        self.assertEqual(self.ipv6_range_full.description, new_description)

    def test_str(self):
        expected_str = (
            f'IPv6Range('
            f'cidr_ipv6="{self.cidr_ipv6}",'
            f'description="{self.description}"'
            f')'
        )
        self.assertEqual(str(self.ipv6_range_full), expected_str)

    def test_to_dict(self):
        expected_dict = {
            "cidr_ipv6": self.cidr_ipv6,
            "description": self.description
        }
        self.assertDictEqual(self.ipv6_range_full.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
