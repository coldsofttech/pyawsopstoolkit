import unittest

from pyawsopstoolkit.models.ec2.security_group import IPRange, IPv6Range, PrefixListID, UserIDGroupPair, IPPermission


class TestIPPermission(unittest.TestCase):
    """Unit test cases for IPPermission."""

    def setUp(self) -> None:
        self.from_port = 80
        self.to_port = 80
        self.ip_protocol = 'tcp'
        self.ip_ranges = [
            IPRange('0.0.0.0/0', 'Allow all IPv4 traffic')
        ]
        self.ipv6_ranges = [
            IPv6Range('::/0', 'Allow all IPv6 traffic')
        ]
        self.prefix_list_ids = [
            PrefixListID('pl-12345678', 'Allow traffic from specific AWS services')
        ]
        self.user_id_group_pairs = [
            UserIDGroupPair('sg-12345678', 'load-balancer-sg', 'active', '123456789012', 'vpc-abcdefgh')
        ]
        self.ip_permission = IPPermission(self.from_port, self.to_port, self.ip_protocol)
        self.ip_permission_with_ip_ranges = IPPermission(self.from_port, self.to_port, self.ip_protocol, self.ip_ranges)
        self.ip_permission_with_ipv6_ranges = IPPermission(
            self.from_port, self.to_port, self.ip_protocol, ipv6_ranges=self.ipv6_ranges
        )
        self.ip_permission_with_prefix_lists = IPPermission(
            self.from_port, self.to_port, self.ip_protocol, prefix_list_ids=self.prefix_list_ids
        )
        self.ip_permission_with_user_group_pairs = IPPermission(
            self.from_port, self.to_port, self.ip_protocol, user_id_group_pairs=self.user_id_group_pairs
        )
        self.ip_permission_full = IPPermission(
            self.from_port, self.to_port, self.ip_protocol, self.ip_ranges, self.ipv6_ranges, self.prefix_list_ids,
            self.user_id_group_pairs
        )

    def test_initialization(self):
        self.assertEqual(self.ip_permission.from_port, self.from_port)
        self.assertEqual(self.ip_permission.to_port, self.to_port)
        self.assertEqual(self.ip_permission.ip_protocol, self.ip_protocol)
        self.assertIsNone(self.ip_permission.ip_ranges)
        self.assertIsNone(self.ip_permission.ipv6_ranges)
        self.assertIsNone(self.ip_permission.prefix_list_ids)
        self.assertIsNone(self.ip_permission.user_id_group_pairs)

    def test_initialization_with_ip_ranges(self):
        self.assertEqual(self.ip_permission_with_ip_ranges.from_port, self.from_port)
        self.assertEqual(self.ip_permission_with_ip_ranges.to_port, self.to_port)
        self.assertEqual(self.ip_permission_with_ip_ranges.ip_protocol, self.ip_protocol)
        self.assertEqual(self.ip_permission_with_ip_ranges.ip_ranges, self.ip_ranges)
        self.assertIsNone(self.ip_permission_with_ip_ranges.ipv6_ranges)
        self.assertIsNone(self.ip_permission_with_ip_ranges.prefix_list_ids)
        self.assertIsNone(self.ip_permission_with_ip_ranges.user_id_group_pairs)

    def test_initialization_with_ipv6_ranges(self):
        self.assertEqual(self.ip_permission_with_ipv6_ranges.from_port, self.from_port)
        self.assertEqual(self.ip_permission_with_ipv6_ranges.to_port, self.to_port)
        self.assertEqual(self.ip_permission_with_ipv6_ranges.ip_protocol, self.ip_protocol)
        self.assertIsNone(self.ip_permission_with_ipv6_ranges.ip_ranges)
        self.assertEqual(self.ip_permission_with_ipv6_ranges.ipv6_ranges, self.ipv6_ranges)
        self.assertIsNone(self.ip_permission_with_ipv6_ranges.prefix_list_ids)
        self.assertIsNone(self.ip_permission_with_ipv6_ranges.user_id_group_pairs)

    def test_initialization_with_prefix_lists(self):
        self.assertEqual(self.ip_permission_with_prefix_lists.from_port, self.from_port)
        self.assertEqual(self.ip_permission_with_prefix_lists.to_port, self.to_port)
        self.assertEqual(self.ip_permission_with_prefix_lists.ip_protocol, self.ip_protocol)
        self.assertIsNone(self.ip_permission_with_prefix_lists.ip_ranges)
        self.assertIsNone(self.ip_permission_with_prefix_lists.ipv6_ranges)
        self.assertEqual(self.ip_permission_with_prefix_lists.prefix_list_ids, self.prefix_list_ids)
        self.assertIsNone(self.ip_permission_with_prefix_lists.user_id_group_pairs)

    def test_initialization_with_user_id_group_pairs(self):
        self.assertEqual(self.ip_permission_with_user_group_pairs.from_port, self.from_port)
        self.assertEqual(self.ip_permission_with_user_group_pairs.to_port, self.to_port)
        self.assertEqual(self.ip_permission_with_user_group_pairs.ip_protocol, self.ip_protocol)
        self.assertIsNone(self.ip_permission_with_user_group_pairs.ip_ranges)
        self.assertIsNone(self.ip_permission_with_user_group_pairs.ipv6_ranges)
        self.assertIsNone(self.ip_permission_with_user_group_pairs.prefix_list_ids)
        self.assertEqual(self.ip_permission_with_user_group_pairs.user_id_group_pairs, self.user_id_group_pairs)

    def test_initialization_full(self):
        self.assertEqual(self.ip_permission_full.from_port, self.from_port)
        self.assertEqual(self.ip_permission_full.to_port, self.to_port)
        self.assertEqual(self.ip_permission_full.ip_protocol, self.ip_protocol)
        self.assertEqual(self.ip_permission_full.ip_ranges, self.ip_ranges)
        self.assertEqual(self.ip_permission_full.ipv6_ranges, self.ipv6_ranges)
        self.assertEqual(self.ip_permission_full.prefix_list_ids, self.prefix_list_ids)
        self.assertEqual(self.ip_permission_full.user_id_group_pairs, self.user_id_group_pairs)

    def test_set_from_port(self):
        new_port = 443
        self.ip_permission_full.from_port = new_port
        self.assertEqual(self.ip_permission_full.from_port, new_port)

    def test_set_to_port(self):
        new_port = 443
        self.ip_permission_full.to_port = new_port
        self.assertEqual(self.ip_permission_full.to_port, new_port)

    def test_set_ip_protocol(self):
        new_protocol = 'udp'
        self.ip_permission_full.ip_protocol = new_protocol
        self.assertEqual(self.ip_permission_full.ip_protocol, new_protocol)

    def test_set_ip_ranges(self):
        new_ranges = [
            IPRange('10.0.0.0/18')
        ]
        self.ip_permission_full.ip_ranges = new_ranges
        self.assertEqual(self.ip_permission_full.ip_ranges, new_ranges)

    def test_set_ipv6_ranges(self):
        new_ranges = [
            IPv6Range('fd12:3456:789a::/48')
        ]
        self.ip_permission_full.ipv6_ranges = new_ranges
        self.assertEqual(self.ip_permission_full.ipv6_ranges, new_ranges)

    def test_set_prefix_list_ids(self):
        new_lists = [
            PrefixListID('pl-87654321')
        ]
        self.ip_permission_full.prefix_list_ids = new_lists
        self.assertEqual(self.ip_permission_full.prefix_list_ids, new_lists)

    def test_set_user_id_group_pairs(self):
        new_pairs = [
            UserIDGroupPair('sg-87654321', 'ec2-sg', 'inactive', '987654321012', 'vpc-hgfedcba')
        ]
        self.ip_permission_full.user_id_group_pairs = new_pairs
        self.assertEqual(self.ip_permission_full.user_id_group_pairs, new_pairs)

    def test_str(self):
        expected_str = (
            f'IPPermission('
            f'from_port={self.from_port},'
            f'to_port={self.to_port},'
            f'ip_protocol="{self.ip_protocol}",'
            f'ip_ranges={self.ip_ranges},'
            f'ipv6_ranges={self.ipv6_ranges},'
            f'prefix_list_ids={self.prefix_list_ids},'
            f'user_id_group_pairs={self.user_id_group_pairs}'
            f')'
        )
        self.assertEqual(str(self.ip_permission_full), expected_str)

    def test_to_dict(self):
        expected_dict = {
            "from_port": self.from_port,
            "to_port": self.to_port,
            "ip_protocol": self.ip_protocol,
            "ip_ranges": self.ip_ranges,
            "ipv6_ranges": self.ipv6_ranges,
            "prefix_list_ids": self.prefix_list_ids,
            "user_id_group_pairs": self.user_id_group_pairs
        }
        self.assertDictEqual(self.ip_permission_full.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
