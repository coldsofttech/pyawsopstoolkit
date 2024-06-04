import unittest

from pyawsopstoolkit import Account
from pyawsopstoolkit.exceptions import ValidationError
from pyawsopstoolkit.models.ec2.security_group import IPPermission, SecurityGroup


class TestSecurityGroup(unittest.TestCase):
    """Unit test cases for SecurityGroup."""

    def setUp(self) -> None:
        self.maxDiff = None
        self.params = {
            'account': Account('123456789012'),
            'region': 'eu-west-1',
            'id': 'sg-12345678',
            'name': 'web-servers-sg',
            'owner_id': '123456789012',
            'vpc_id': 'vpc-abcdefgh',
            'ip_permissions': [IPPermission(80, 80, 'tcp')],
            'ip_permissions_egress': [IPPermission(443, 443, 'tcp')],
            'description': 'Primary security group for web servers',
            'tags': [{'Key': 'test_key', 'Value': 'test_value'}]
        }
        self.security_group = self.create_security_group()
        self.security_group_with_ip_permissions = self.create_security_group(
            ip_permissions=self.params['ip_permissions']
        )
        self.security_group_with_ip_permissions_egress = self.create_security_group(
            ip_permissions_egress=self.params['ip_permissions_egress']
        )
        self.security_group_with_desc = self.create_security_group(description=self.params['description'])
        self.security_group_with_tags = self.create_security_group(tags=self.params['tags'])
        self.security_group_full = self.create_security_group(
            ip_permissions=self.params['ip_permissions'],
            ip_permissions_egress=self.params['ip_permissions_egress'],
            description=self.params['description'],
            tags=self.params['tags']
        )

    def create_security_group(self, **kwargs):
        return SecurityGroup(
            account=self.params['account'],
            region=self.params['region'],
            id=self.params['id'],
            name=self.params['name'],
            owner_id=self.params['owner_id'],
            vpc_id=self.params['vpc_id'],
            **kwargs
        )

    def test_initialization(self):
        self.assertEqual(self.security_group.account, self.params['account'])
        self.assertEqual(self.security_group.region, self.params['region'])
        self.assertEqual(self.security_group.id, self.params['id'])
        self.assertEqual(self.security_group.name, self.params['name'])
        self.assertEqual(self.security_group.owner_id, self.params['owner_id'])
        self.assertEqual(self.security_group.vpc_id, self.params['vpc_id'])
        self.assertIsNone(self.security_group.ip_permissions)
        self.assertIsNone(self.security_group.ip_permissions_egress)
        self.assertIsNone(self.security_group.description)
        self.assertIsNone(self.security_group.tags)

    def test_initialization_with_optional_params(self):
        test_cases = [
            (self.security_group_with_ip_permissions, self.params['ip_permissions'], None, None, None),
            (self.security_group_with_ip_permissions_egress, None, self.params['ip_permissions_egress'], None, None),
            (self.security_group_with_desc, None, None, self.params['description'], None),
            (self.security_group_with_tags, None, None, None, self.params['tags']),
            (
                self.security_group_full,
                self.params['ip_permissions'],
                self.params['ip_permissions_egress'],
                self.params['description'],
                self.params['tags']
            )
        ]
        for security_group, ip_permissions, ip_permissions_egress, description, tags in test_cases:
            with self.subTest(security_group=security_group):
                self.assertEqual(security_group.account, self.params['account'])
                self.assertEqual(security_group.region, self.params['region'])
                self.assertEqual(security_group.id, self.params['id'])
                self.assertEqual(security_group.name, self.params['name'])
                self.assertEqual(security_group.owner_id, self.params['owner_id'])
                self.assertEqual(security_group.vpc_id, self.params['vpc_id'])
                self.assertEqual(security_group.ip_permissions, ip_permissions)
                self.assertEqual(security_group.ip_permissions_egress, ip_permissions_egress)
                self.assertEqual(security_group.description, description)
                self.assertEqual(security_group.tags, tags)

    def test_setters(self):
        new_params = {
            'account': Account('987654321012'),
            'region': 'us-east-2',
            'id': 'sg-87654321',
            'name': 'load-balancers-sg',
            'owner_id': '987654321012',
            'vpc_id': 'vpc-hgfedcba',
            'ip_permissions': [IPPermission(443, 443, 'tcp')],
            'ip_permissions_egress': [IPPermission(80, 80, 'tcp')],
            'description': 'Primary security group for load balancers',
            'tags': [{'Key': 'test_key1', 'Value': 'test_value1'}]
        }

        self.security_group_full.account = new_params['account']
        self.security_group_full.region = new_params['region']
        self.security_group_full.id = new_params['id']
        self.security_group_full.name = new_params['name']
        self.security_group_full.owner_id = new_params['owner_id']
        self.security_group_full.vpc_id = new_params['vpc_id']
        self.security_group_full.ip_permissions = new_params['ip_permissions']
        self.security_group_full.ip_permissions_egress = new_params['ip_permissions_egress']
        self.security_group_full.description = new_params['description']
        self.security_group_full.tags = new_params['tags']

        self.assertEqual(self.security_group_full.account, new_params['account'])
        self.assertEqual(self.security_group_full.region, new_params['region'])
        self.assertEqual(self.security_group_full.id, new_params['id'])
        self.assertEqual(self.security_group_full.name, new_params['name'])
        self.assertEqual(self.security_group_full.owner_id, new_params['owner_id'])
        self.assertEqual(self.security_group_full.vpc_id, new_params['vpc_id'])
        self.assertEqual(self.security_group_full.ip_permissions, new_params['ip_permissions'])
        self.assertEqual(self.security_group_full.ip_permissions_egress, new_params['ip_permissions_egress'])
        self.assertEqual(self.security_group_full.description, new_params['description'])
        self.assertEqual(self.security_group_full.tags, new_params['tags'])

    def test_invalid_types(self):
        invalid_params = {
            'account': '123456789012',
            'region': 'Ireland',
            'id': 123,
            'name': 123,
            'owner_id': 123,
            'vpc_id': 123,
            'ip_permissions': [80],
            'ip_permissions_egress': [443],
            'description': 123,
            'tags': 'tag_key=tag_value'
        }

        with self.assertRaises(TypeError):
            SecurityGroup(
                account=invalid_params['account'],
                region=self.params['region'],
                id=self.params['id'],
                name=self.params['name'],
                owner_id=self.params['owner_id'],
                vpc_id=self.params['vpc_id']
            )
        with self.assertRaises(ValidationError):
            SecurityGroup(
                account=self.params['account'],
                region=invalid_params['region'],
                id=self.params['id'],
                name=self.params['name'],
                owner_id=self.params['owner_id'],
                vpc_id=self.params['vpc_id']
            )
        with self.assertRaises(TypeError):
            SecurityGroup(
                account=self.params['account'],
                region=self.params['region'],
                id=invalid_params['id'],
                name=self.params['name'],
                owner_id=self.params['owner_id'],
                vpc_id=self.params['vpc_id']
            )
        with self.assertRaises(TypeError):
            SecurityGroup(
                account=self.params['account'],
                region=self.params['region'],
                id=self.params['id'],
                name=invalid_params['name'],
                owner_id=self.params['owner_id'],
                vpc_id=self.params['vpc_id']
            )
        with self.assertRaises(TypeError):
            SecurityGroup(
                account=self.params['account'],
                region=self.params['region'],
                id=self.params['id'],
                name=self.params['name'],
                owner_id=invalid_params['owner_id'],
                vpc_id=self.params['vpc_id']
            )
        with self.assertRaises(TypeError):
            SecurityGroup(
                account=self.params['account'],
                region=self.params['region'],
                id=self.params['id'],
                name=self.params['name'],
                owner_id=self.params['owner_id'],
                vpc_id=invalid_params['vpc_id']
            )
        with self.assertRaises(TypeError):
            self.create_security_group(ip_permissions=invalid_params['ip_permissions'])
        with self.assertRaises(TypeError):
            self.create_security_group(ip_permissions_egress=invalid_params['ip_permissions_egress'])
        with self.assertRaises(TypeError):
            self.create_security_group(description=invalid_params['description'])
        with self.assertRaises(TypeError):
            self.create_security_group(tags=invalid_params['tags'])

        with self.assertRaises(TypeError):
            self.security_group_full.account = invalid_params['account']
        with self.assertRaises(ValidationError):
            self.security_group_full.region = invalid_params['region']
        with self.assertRaises(TypeError):
            self.security_group_full.id = invalid_params['id']
        with self.assertRaises(TypeError):
            self.security_group_full.name = invalid_params['name']
        with self.assertRaises(TypeError):
            self.security_group_full.owner_id = invalid_params['owner_id']
        with self.assertRaises(TypeError):
            self.security_group_full.vpc_id = invalid_params['vpc_id']
        with self.assertRaises(TypeError):
            self.security_group_full.ip_permissions = invalid_params['ip_permissions']
        with self.assertRaises(TypeError):
            self.security_group_full.ip_permissions_egress = invalid_params['ip_permissions_egress']
        with self.assertRaises(TypeError):
            self.security_group_full.description = invalid_params['description']
        with self.assertRaises(TypeError):
            self.security_group_full.tags = invalid_params['tags']

    def test_to_dict(self):
        expected_dict = {
            "account": self.params['account'].to_dict(),
            "region": self.params['region'],
            "id": self.params['id'],
            "name": self.params['name'],
            "owner_id": self.params['owner_id'],
            "vpc_id": self.params['vpc_id'],
            "ip_permissions": [ip_perm.to_dict() for ip_perm in self.params['ip_permissions']],
            "ip_permissions_egress": [ip_perm.to_dict() for ip_perm in self.params['ip_permissions_egress']],
            "description": self.params['description'],
            "tags": self.params['tags']
        }
        self.assertDictEqual(self.security_group_full.to_dict(), expected_dict)

    def test_to_dict_with_missing_fields(self):
        expected_dict = {
            "account": self.params['account'].to_dict(),
            "region": self.params['region'],
            "id": self.params['id'],
            "name": self.params['name'],
            "owner_id": self.params['owner_id'],
            "vpc_id": self.params['vpc_id'],
            "ip_permissions": None,
            "ip_permissions_egress": None,
            "description": None,
            "tags": None
        }
        self.assertDictEqual(self.security_group.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
