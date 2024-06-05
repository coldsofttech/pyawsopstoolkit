import unittest

from pyawsopstoolkit.models.ec2.network_interface import Association


class TestAssociation(unittest.TestCase):
    """Unit test cases for Association."""

    def setUp(self) -> None:
        self.maxDiff = None
        self.params = {
            'id': 'eipassoc-0123456789abcdef0',
            'allocation_id': 'eipalloc-0123456789abcdef0',
            'ip_owner_id': '123456789012',
            'public_dns_name': 'ec2-203-0-113-25.compute-1.amazonaws.com',
            'public_ip': '203.0.113.25',
            'customer_owned_ip': '198.51.100.25',
            'carrier_ip': '192.0.2.25'
        }
        self.association = Association(
            id=self.params['id'],
            allocation_id=self.params['allocation_id'],
            ip_owner_id=self.params['ip_owner_id'],
            public_ip=self.params['public_ip'],
            public_dns_name=self.params['public_dns_name'],
            customer_owned_ip=self.params['customer_owned_ip'],
            carrier_ip=self.params['carrier_ip']
        )

    def test_initialization(self):
        self.assertEqual(self.association.id, self.params['id'])
        self.assertEqual(self.association.allocation_id, self.params['allocation_id'])
        self.assertEqual(self.association.ip_owner_id, self.params['ip_owner_id'])
        self.assertEqual(self.association.public_dns_name, self.params['public_dns_name'])
        self.assertEqual(self.association.public_ip, self.params['public_ip'])
        self.assertEqual(self.association.customer_owned_ip, self.params['customer_owned_ip'])
        self.assertEqual(self.association.carrier_ip, self.params['carrier_ip'])

    def test_setters(self):
        new_params = {
            'id': 'eipassoc-0123456789abcdef1',
            'allocation_id': 'eipalloc-0123456789abcdef1',
            'ip_owner_id': '987654321012',
            'public_dns_name': 'ec2-200-0-0-0.compute-1.amazonaws.com',
            'public_ip': '200.0.0.0',
            'customer_owned_ip': '198.51.100.20',
            'carrier_ip': '192.0.2.20'
        }

        self.association.id = new_params['id']
        self.association.allocation_id = new_params['allocation_id']
        self.association.ip_owner_id = new_params['ip_owner_id']
        self.association.public_dns_name = new_params['public_dns_name']
        self.association.public_ip = new_params['public_ip']
        self.association.customer_owned_ip = new_params['customer_owned_ip']
        self.association.carrier_ip = new_params['carrier_ip']

        self.assertEqual(self.association.id, new_params['id'])
        self.assertEqual(self.association.allocation_id, new_params['allocation_id'])
        self.assertEqual(self.association.ip_owner_id, new_params['ip_owner_id'])
        self.assertEqual(self.association.public_dns_name, new_params['public_dns_name'])
        self.assertEqual(self.association.public_ip, new_params['public_ip'])
        self.assertEqual(self.association.customer_owned_ip, new_params['customer_owned_ip'])
        self.assertEqual(self.association.carrier_ip, new_params['carrier_ip'])

    def test_invalid_types(self):
        invalid_params = {
            'id': 123,
            'allocation_id': 123,
            'ip_owner_id': 123,
            'public_dns_name': 123,
            'public_ip': 123,
            'customer_owned_ip': 123,
            'carrier_ip': 123
        }

        with self.assertRaises(TypeError):
            Association(
                id=invalid_params['id'],
                allocation_id=self.params['allocation_id'],
                ip_owner_id=self.params['ip_owner_id'],
                public_ip=self.params['public_ip'],
                public_dns_name=self.params['public_dns_name'],
                customer_owned_ip=self.params['customer_owned_ip'],
                carrier_ip=self.params['carrier_ip']
            )
        with self.assertRaises(TypeError):
            Association(
                id=self.params['id'],
                allocation_id=invalid_params['allocation_id'],
                ip_owner_id=self.params['ip_owner_id'],
                public_ip=self.params['public_ip'],
                public_dns_name=self.params['public_dns_name'],
                customer_owned_ip=self.params['customer_owned_ip'],
                carrier_ip=self.params['carrier_ip']
            )
        with self.assertRaises(TypeError):
            Association(
                id=self.params['id'],
                allocation_id=self.params['allocation_id'],
                ip_owner_id=invalid_params['ip_owner_id'],
                public_ip=self.params['public_ip'],
                public_dns_name=self.params['public_dns_name'],
                customer_owned_ip=self.params['customer_owned_ip'],
                carrier_ip=self.params['carrier_ip']
            )
        with self.assertRaises(TypeError):
            Association(
                id=self.params['id'],
                allocation_id=self.params['allocation_id'],
                ip_owner_id=self.params['ip_owner_id'],
                public_ip=invalid_params['public_ip'],
                public_dns_name=self.params['public_dns_name'],
                customer_owned_ip=self.params['customer_owned_ip'],
                carrier_ip=self.params['carrier_ip']
            )
        with self.assertRaises(TypeError):
            Association(
                id=self.params['id'],
                allocation_id=self.params['allocation_id'],
                ip_owner_id=self.params['ip_owner_id'],
                public_ip=self.params['public_ip'],
                public_dns_name=invalid_params['public_dns_name'],
                customer_owned_ip=self.params['customer_owned_ip'],
                carrier_ip=self.params['carrier_ip']
            )
        with self.assertRaises(TypeError):
            Association(
                id=self.params['id'],
                allocation_id=self.params['allocation_id'],
                ip_owner_id=self.params['ip_owner_id'],
                public_ip=self.params['public_ip'],
                public_dns_name=self.params['public_dns_name'],
                customer_owned_ip=invalid_params['customer_owned_ip'],
                carrier_ip=self.params['carrier_ip']
            )
        with self.assertRaises(TypeError):
            Association(
                id=self.params['id'],
                allocation_id=self.params['allocation_id'],
                ip_owner_id=self.params['ip_owner_id'],
                public_ip=self.params['public_ip'],
                public_dns_name=self.params['public_dns_name'],
                customer_owned_ip=self.params['customer_owned_ip'],
                carrier_ip=invalid_params['carrier_ip']
            )

        with self.assertRaises(TypeError):
            self.association.id = invalid_params['id']
        with self.assertRaises(TypeError):
            self.association.allocation_id = invalid_params['allocation_id']
        with self.assertRaises(TypeError):
            self.association.ip_owner_id = invalid_params['ip_owner_id']
        with self.assertRaises(TypeError):
            self.association.public_ip = invalid_params['public_ip']
        with self.assertRaises(TypeError):
            self.association.public_dns_name = invalid_params['public_dns_name']
        with self.assertRaises(TypeError):
            self.association.customer_owned_ip = invalid_params['customer_owned_ip']
        with self.assertRaises(TypeError):
            self.association.carrier_ip = invalid_params['carrier_ip']

    def test_to_dict(self):
        expected_dict = {
            "id": self.params['id'],
            "allocation_id": self.params['allocation_id'],
            "ip_owner_id": self.params['ip_owner_id'],
            "public_ip": self.params['public_ip'],
            "public_dns_name": self.params['public_dns_name'],
            "customer_owned_ip": self.params['customer_owned_ip'],
            "carrier_ip": self.params['carrier_ip']
        }
        self.assertDictEqual(self.association.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
