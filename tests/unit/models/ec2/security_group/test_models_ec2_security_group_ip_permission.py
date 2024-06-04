import unittest

from pyawsopstoolkit.models.ec2.security_group import IPRange, IPv6Range, PrefixList, UserIDGroupPair, IPPermission


class TestIPPermission(unittest.TestCase):
    """Unit test cases for IPPermission."""

    def setUp(self) -> None:
        self.params = {
            'from_port': 80,
            'to_port': 80,
            'ip_protocol': 'tcp',
            'ip_ranges': [IPRange(
                cidr_ip='0.0.0.0/0', description='Allow all IPv4 traffic'
            )],
            'ipv6_ranges': [IPv6Range(
                cidr_ipv6='::/0', description='Allow all IPv6 traffic'
            )],
            'prefix_lists': [PrefixList(
                id='pl-12345678', description='Allow traffic from specific AWS services'
            )],
            'user_id_group_pairs': [UserIDGroupPair(
                id='sg-12345678',
                name='load-balancer-sg',
                status='active',
                user_id='123456789012',
                vpc_id='vpc-abcdefgh'
            )]
        }
        self.ip_permission = self.create_ip_permission()
        self.ip_permission_with_ip_ranges = self.create_ip_permission(ip_ranges=self.params['ip_ranges'])
        self.ip_permission_with_ipv6_ranges = self.create_ip_permission(ipv6_ranges=self.params['ipv6_ranges'])
        self.ip_permission_with_prefix_lists = self.create_ip_permission(prefix_lists=self.params['prefix_lists'])
        self.ip_permission_with_user_group_pairs = self.create_ip_permission(
            user_id_group_pairs=self.params['user_id_group_pairs']
        )
        self.ip_permission_full = self.create_ip_permission(
            ip_ranges=self.params['ip_ranges'],
            ipv6_ranges=self.params['ipv6_ranges'],
            prefix_lists=self.params['prefix_lists'],
            user_id_group_pairs=self.params['user_id_group_pairs']
        )

    def create_ip_permission(self, **kwargs):
        return IPPermission(
            from_port=self.params['from_port'],
            to_port=self.params['to_port'],
            ip_protocol=self.params['ip_protocol'],
            **kwargs
        )

    def test_initialization(self):
        self.assertEqual(self.ip_permission.from_port, self.params['from_port'])
        self.assertEqual(self.ip_permission.to_port, self.params['to_port'])
        self.assertEqual(self.ip_permission.ip_protocol, self.params['ip_protocol'])
        self.assertIsNone(self.ip_permission.ip_ranges)
        self.assertIsNone(self.ip_permission.ipv6_ranges)
        self.assertIsNone(self.ip_permission.prefix_lists)
        self.assertIsNone(self.ip_permission.user_id_group_pairs)

    def test_initialization_with_optional_params(self):
        test_cases = [
            (self.ip_permission_with_ip_ranges, self.params['ip_ranges'], None, None, None),
            (self.ip_permission_with_ipv6_ranges, None, self.params['ipv6_ranges'], None, None),
            (self.ip_permission_with_prefix_lists, None, None, self.params['prefix_lists'], None),
            (self.ip_permission_with_user_group_pairs, None, None, None, self.params['user_id_group_pairs']),
            (
                self.ip_permission_full,
                self.params['ip_ranges'],
                self.params['ipv6_ranges'],
                self.params['prefix_lists'],
                self.params['user_id_group_pairs']
            )
        ]
        for ip_permission, ip_ranges, ipv6_ranges, prefix_lists, user_id_group_pairs in test_cases:
            with self.subTest(ip_permission=ip_permission):
                self.assertEqual(ip_permission.from_port, self.params['from_port'])
                self.assertEqual(ip_permission.to_port, self.params['to_port'])
                self.assertEqual(ip_permission.ip_protocol, self.params['ip_protocol'])
                self.assertEqual(ip_permission.ip_ranges, ip_ranges)
                self.assertEqual(ip_permission.ipv6_ranges, ipv6_ranges)
                self.assertEqual(ip_permission.prefix_lists, prefix_lists)
                self.assertEqual(ip_permission.user_id_group_pairs, user_id_group_pairs)

    def test_setters(self):
        new_params = {
            'from_port': 443,
            'to_port': 443,
            'ip_protocol': 'udp',
            'ip_ranges': [IPRange(
                cidr_ip='10.0.0.0/8', description='Allow all IPv4 traffic'
            )],
            'ipv6_ranges': [IPv6Range(
                cidr_ipv6='2001:db8::/64', description='Allow all IPv6 traffic'
            )],
            'prefix_lists': [PrefixList(
                id='pl-87654321', description='Allow traffic from specific AWS services'
            )],
            'user_id_group_pairs': [UserIDGroupPair(
                id='sg-87654321',
                name='web-servers-sg',
                status='inactive',
                user_id='987654321012',
                vpc_id='vpc-hgfedcba'
            )]
        }

        self.ip_permission_full.from_port = new_params['from_port']
        self.ip_permission_full.to_port = new_params['to_port']
        self.ip_permission_full.ip_protocol = new_params['ip_protocol']
        self.ip_permission_full.ip_ranges = new_params['ip_ranges']
        self.ip_permission_full.ipv6_ranges = new_params['ipv6_ranges']
        self.ip_permission_full.prefix_lists = new_params['prefix_lists']
        self.ip_permission_full.user_id_group_pairs = new_params['user_id_group_pairs']

        self.assertEqual(self.ip_permission_full.from_port, new_params['from_port'])
        self.assertEqual(self.ip_permission_full.to_port, new_params['to_port'])
        self.assertEqual(self.ip_permission_full.ip_protocol, new_params['ip_protocol'])
        self.assertEqual(self.ip_permission_full.ip_ranges, new_params['ip_ranges'])
        self.assertEqual(self.ip_permission_full.ipv6_ranges, new_params['ipv6_ranges'])
        self.assertEqual(self.ip_permission_full.prefix_lists, new_params['prefix_lists'])
        self.assertEqual(self.ip_permission_full.user_id_group_pairs, new_params['user_id_group_pairs'])

    def test_invalid_types(self):
        invalid_params = {
            'from_port': '80',
            'to_port': '80',
            'ip_protocol': 123,
            'ip_ranges': [123],
            'ipv6_ranges': [123],
            'prefix_lists': [123],
            'user_id_group_pairs': [123]
        }

        with self.assertRaises(TypeError):
            IPPermission(invalid_params['from_port'], self.params['to_port'], self.params['ip_protocol'])
        with self.assertRaises(TypeError):
            IPPermission(self.params['from_port'], invalid_params['to_port'], self.params['ip_protocol'])
        with self.assertRaises(TypeError):
            IPPermission(self.params['from_port'], self.params['to_port'], invalid_params['ip_protocol'])
        with self.assertRaises(TypeError):
            self.create_ip_permission(ip_ranges=invalid_params['ip_ranges'])
        with self.assertRaises(TypeError):
            self.create_ip_permission(ipv6_ranges=invalid_params['ipv6_ranges'])
        with self.assertRaises(TypeError):
            self.create_ip_permission(prefix_lists=invalid_params['prefix_lists'])
        with self.assertRaises(TypeError):
            self.create_ip_permission(user_id_group_pairs=invalid_params['user_id_group_pairs'])

        with self.assertRaises(TypeError):
            self.ip_permission_full.from_port = invalid_params['from_port']
        with self.assertRaises(TypeError):
            self.ip_permission_full.to_port = invalid_params['to_port']
        with self.assertRaises(TypeError):
            self.ip_permission_full.ip_protocol = invalid_params['ip_protocol']
        with self.assertRaises(TypeError):
            self.ip_permission_full.ip_ranges = invalid_params['ip_ranges']
        with self.assertRaises(TypeError):
            self.ip_permission_full.ipv6_ranges = invalid_params['ipv6_ranges']
        with self.assertRaises(TypeError):
            self.ip_permission_full.prefix_lists = invalid_params['prefix_lists']
        with self.assertRaises(TypeError):
            self.ip_permission_full.user_id_group_pairs = invalid_params['user_id_group_pairs']

    def test_to_dict(self):
        expected_dict = {
            "from_port": self.params['from_port'],
            "to_port": self.params['to_port'],
            "ip_protocol": self.params['ip_protocol'],
            "ip_ranges": [ip_range.to_dict() for ip_range in self.params['ip_ranges']],
            "ipv6_ranges": [ip_range.to_dict() for ip_range in self.params['ipv6_ranges']],
            "prefix_lists": [prefix.to_dict() for prefix in self.params['prefix_lists']],
            "user_id_group_pairs": [pair.to_dict() for pair in self.params['user_id_group_pairs']]
        }
        self.assertDictEqual(self.ip_permission_full.to_dict(), expected_dict)

    def test_to_dict_with_missing_fields(self):
        expected_dict = {
            "from_port": self.params['from_port'],
            "to_port": self.params['to_port'],
            "ip_protocol": self.params['ip_protocol'],
            "ip_ranges": None,
            "ipv6_ranges": None,
            "prefix_lists": None,
            "user_id_group_pairs": None
        }
        self.assertDictEqual(self.ip_permission.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
