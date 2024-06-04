import unittest

from pyawsopstoolkit.models.ec2.security_group import IPRange


class TestIPRange(unittest.TestCase):
    """Unit test cases for IPRange."""

    def setUp(self) -> None:
        self.maxDiff = None
        self.params = {
            'cidr_ip': '10.0.0.0/18',
            'description': '10.x.x.x IP Series'
        }
        self.ip_range = self.create_ip_range()
        self.ip_range_full = self.create_ip_range(description=self.params['description'])

    def create_ip_range(self, **kwargs):
        return IPRange(self.params['cidr_ip'], **kwargs)

    def test_initialization(self):
        self.assertEqual(self.ip_range.cidr_ip, self.params['cidr_ip'])
        self.assertIsNone(self.ip_range.description)

    def test_setters(self):
        new_params = {
            'cidr_ip': '100.0.0.0/18',
            'description': '100.x.x.x IP Series'
        }

        self.ip_range_full.cidr_ip = new_params['cidr_ip']
        self.ip_range_full.description = new_params['description']

        self.assertEqual(self.ip_range_full.cidr_ip, new_params['cidr_ip'])
        self.assertEqual(self.ip_range_full.description, new_params['description'])

    def test_invalid_types(self):
        invalid_params = {
            'cidr_ip': 123,
            'description': 123
        }

        with self.assertRaises(TypeError):
            IPRange(invalid_params['cidr_ip'])
        with self.assertRaises(TypeError):
            self.create_ip_range(description=invalid_params['description'])

        with self.assertRaises(TypeError):
            self.ip_range_full.cidr_ip = invalid_params['cidr_ip']
        with self.assertRaises(TypeError):
            self.ip_range_full.description = invalid_params['description']

    def test_initialization_with_optional_params(self):
        test_cases = [
            (self.ip_range_full, self.params['description'])
        ]
        for ip_range, description in test_cases:
            with self.subTest(ip_range=ip_range):
                self.assertEqual(ip_range.cidr_ip, self.params['cidr_ip'])
                self.assertEqual(ip_range.description, description)

    def test_to_dict(self):
        expected_dict = {
            "cidr_ip": self.params['cidr_ip'],
            "description": self.params['description']
        }
        self.assertDictEqual(self.ip_range_full.to_dict(), expected_dict)

    def test_to_dict_with_missing_fields(self):
        expected_dict = {
            "cidr_ip": self.params['cidr_ip'],
            "description": None
        }
        self.assertDictEqual(self.ip_range.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
