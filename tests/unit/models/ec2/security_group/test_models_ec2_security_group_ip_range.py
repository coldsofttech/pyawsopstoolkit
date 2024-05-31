import unittest

from pyawsopstoolkit.models.ec2.security_group import IPRange


class TestIPRange(unittest.TestCase):
    """Unit test cases for IPRange."""

    def setUp(self) -> None:
        self.cidr_ip = '10.0.0.0/18'
        self.description = '10.x.x.x IP Series'
        self.ip_range = IPRange(self.cidr_ip)
        self.ip_range_full = IPRange(self.cidr_ip, self.description)

    def test_initialization(self):
        self.assertEqual(self.ip_range.cidr_ip, self.cidr_ip)
        self.assertIsNone(self.ip_range.description)

    def test_initialization_full(self):
        self.assertEqual(self.ip_range_full.cidr_ip, self.cidr_ip)
        self.assertEqual(self.ip_range_full.description, self.description)

    def test_set_cidr_ip(self):
        new_cidr_ip = '100.0.0.0/18'
        self.ip_range_full.cidr_ip = new_cidr_ip
        self.assertEqual(self.ip_range_full.cidr_ip, new_cidr_ip)

    def test_set_description(self):
        new_description = 'New IP Series'
        self.ip_range_full.description = new_description
        self.assertEqual(self.ip_range_full.description, new_description)

    def test_str(self):
        expected_str = (
            f'IPRange('
            f'cidr_ip="{self.cidr_ip}",'
            f'description="{self.description}"'
            f')'
        )
        self.assertEqual(str(self.ip_range_full), expected_str)

    def test_to_dict(self):
        expected_dict = {
            "cidr_ip": self.cidr_ip,
            "description": self.description
        }
        self.assertDictEqual(self.ip_range_full.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
