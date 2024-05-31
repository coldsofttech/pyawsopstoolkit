import unittest

from pyawsopstoolkit.models.ec2.security_group import IPPermission, SecurityGroup


class TestSecurityGroup(unittest.TestCase):
    """Unit test cases for SecurityGroup."""

    def setUp(self) -> None:
        self.id = 'sg-12345678'
        self.name = 'web-servers-sg'
        self.owner_id = '123456789012'
        self.vpc_id = 'vpc-abcdefgh'
        self.ip_permissions = [
            IPPermission(80, 80, 'tcp')
        ]
        self.ip_permissions_egress = [
            IPPermission(443, 443, 'tcp')
        ]
        self.description = 'Primary security group for web servers'
        self.tags = [
            {'Key': 'test_key', 'Value': 'test_value'}
        ]
        self.security_group = SecurityGroup(self.id, self.name, self.owner_id, self.vpc_id)
        self.security_group_with_ip_permissions = SecurityGroup(
            self.id, self.name, self.owner_id, self.vpc_id, self.ip_permissions
        )
        self.security_group_with_ip_permissions_egress = SecurityGroup(
            self.id, self.name, self.owner_id, self.vpc_id, ip_permissions_egress=self.ip_permissions_egress
        )
        self.security_group_with_desc = SecurityGroup(
            self.id, self.name, self.owner_id, self.vpc_id, description=self.description
        )
        self.security_group_with_tags = SecurityGroup(
            self.id, self.name, self.owner_id, self.vpc_id, tags=self.tags
        )
        self.security_group_full = SecurityGroup(
            self.id, self.name, self.owner_id, self.vpc_id, self.ip_permissions, self.ip_permissions_egress,
            self.description, self.tags
        )

    def test_initialization(self):
        self.assertEqual(self.security_group.id, self.id)
        self.assertEqual(self.security_group.name, self.name)
        self.assertEqual(self.security_group.owner_id, self.owner_id)
        self.assertEqual(self.security_group.vpc_id, self.vpc_id)
        self.assertIsNone(self.security_group.ip_permissions)
        self.assertIsNone(self.security_group.ip_permissions_egress)
        self.assertIsNone(self.security_group.description)
        self.assertIsNone(self.security_group.tags)

    def test_initialization_with_ip_permissions(self):
        self.assertEqual(self.security_group_with_ip_permissions.id, self.id)
        self.assertEqual(self.security_group_with_ip_permissions.name, self.name)
        self.assertEqual(self.security_group_with_ip_permissions.owner_id, self.owner_id)
        self.assertEqual(self.security_group_with_ip_permissions.vpc_id, self.vpc_id)
        self.assertEqual(self.security_group_with_ip_permissions.ip_permissions, self.ip_permissions)
        self.assertIsNone(self.security_group_with_ip_permissions.ip_permissions_egress)
        self.assertIsNone(self.security_group_with_ip_permissions.description)
        self.assertIsNone(self.security_group_with_ip_permissions.tags)

    def test_initialization_with_ip_permissions_egress(self):
        self.assertEqual(self.security_group_with_ip_permissions_egress.id, self.id)
        self.assertEqual(self.security_group_with_ip_permissions_egress.name, self.name)
        self.assertEqual(self.security_group_with_ip_permissions_egress.owner_id, self.owner_id)
        self.assertEqual(self.security_group_with_ip_permissions_egress.vpc_id, self.vpc_id)
        self.assertIsNone(self.security_group_with_ip_permissions_egress.ip_permissions)
        self.assertEqual(
            self.security_group_with_ip_permissions_egress.ip_permissions_egress, self.ip_permissions_egress
        )
        self.assertIsNone(self.security_group_with_ip_permissions_egress.description)
        self.assertIsNone(self.security_group_with_ip_permissions_egress.tags)

    def test_initialization_with_desc(self):
        self.assertEqual(self.security_group_with_desc.id, self.id)
        self.assertEqual(self.security_group_with_desc.name, self.name)
        self.assertEqual(self.security_group_with_desc.owner_id, self.owner_id)
        self.assertEqual(self.security_group_with_desc.vpc_id, self.vpc_id)
        self.assertIsNone(self.security_group_with_desc.ip_permissions)
        self.assertIsNone(self.security_group_with_desc.ip_permissions_egress)
        self.assertEqual(self.security_group_with_desc.description, self.description)
        self.assertIsNone(self.security_group_with_desc.tags)

    def test_initialization_with_tags(self):
        self.assertEqual(self.security_group_with_tags.id, self.id)
        self.assertEqual(self.security_group_with_tags.name, self.name)
        self.assertEqual(self.security_group_with_tags.owner_id, self.owner_id)
        self.assertEqual(self.security_group_with_tags.vpc_id, self.vpc_id)
        self.assertIsNone(self.security_group_with_tags.ip_permissions)
        self.assertIsNone(self.security_group_with_tags.ip_permissions_egress)
        self.assertIsNone(self.security_group_with_tags.description)
        self.assertEqual(self.security_group_with_tags.tags, self.tags)

    def test_initialization_full(self):
        self.assertEqual(self.security_group_full.id, self.id)
        self.assertEqual(self.security_group_full.name, self.name)
        self.assertEqual(self.security_group_full.owner_id, self.owner_id)
        self.assertEqual(self.security_group_full.vpc_id, self.vpc_id)
        self.assertEqual(self.security_group_full.ip_permissions, self.ip_permissions)
        self.assertEqual(self.security_group_full.ip_permissions_egress, self.ip_permissions_egress)
        self.assertEqual(self.security_group_full.description, self.description)
        self.assertEqual(self.security_group_full.tags, self.tags)

    def test_set_id(self):
        new_id = 'sg-87654321'
        self.security_group_full.id = new_id
        self.assertEqual(self.security_group_full.id, new_id)

    def test_set_name(self):
        new_name = 'Test Security Group'
        self.security_group_full.name = new_name
        self.assertEqual(self.security_group_full.name, new_name)

    def test_set_owner_id(self):
        new_owner = '987654321012'
        self.security_group_full.owner_id = new_owner
        self.assertEqual(self.security_group_full.owner_id, new_owner)

    def test_set_vpc_id(self):
        new_vpc = 'vpc-hgfedcba'
        self.security_group_full.vpc_id = new_vpc
        self.assertEqual(self.security_group_full.vpc_id, new_vpc)

    def test_set_ip_permissions(self):
        new_permissions = [
            IPPermission(443, 443, 'tcp')
        ]
        self.security_group_full.ip_permissions = new_permissions
        self.assertEqual(self.security_group_full.ip_permissions, new_permissions)

    def test_set_ip_permissions_egress(self):
        new_permissions = [
            IPPermission(80, 80, 'tcp')
        ]
        self.security_group_full.ip_permissions_egress = new_permissions
        self.assertEqual(self.security_group_full.ip_permissions_egress, new_permissions)

    def test_set_description(self):
        new_description = 'Updated security group for web servers'
        self.security_group_full.description = new_description
        self.assertEqual(self.security_group_full.description, new_description)

    def test_set_tags(self):
        new_tags = [
            {'Key': 'test_key1', 'Value': 'test_value1'}
        ]
        self.security_group_full.tags = new_tags
        self.assertEqual(self.security_group_full.tags, new_tags)

    def test_str(self):
        expected_str = (
            f'SecurityGroup('
            f'id="{self.id}",'
            f'name="{self.name}",'
            f'owner_id="{self.owner_id}",'
            f'vpc_id="{self.vpc_id}",'
            f'ip_permissions={self.ip_permissions},'
            f'ip_permissions_egress={self.ip_permissions_egress},'
            f'description="{self.description}",'
            f'tags={self.tags}'
            f')'
        )
        self.assertEqual(str(self.security_group_full), expected_str)

    def test_to_dict(self):
        expected_dict = {
            "id": self.id,
            "name": self.name,
            "owner_id": self.owner_id,
            "vpc_id": self.vpc_id,
            "ip_permissions": self.ip_permissions,
            "ip_permissions_egress": self.ip_permissions_egress,
            "description": self.description,
            "tags": self.tags
        }
        self.assertDictEqual(self.security_group_full.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
