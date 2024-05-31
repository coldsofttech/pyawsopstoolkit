import unittest

from pyawsopstoolkit.models.ec2.security_group import UserIDGroupPair


class TestUserIDGroupPair(unittest.TestCase):
    """Unit test cases for UserIDGroupPair."""

    def setUp(self) -> None:
        self.maxDiff = None
        self.id = 'sg-12345678'
        self.name = 'load-balancer-sg'
        self.status = 'active'
        self.user_id = '123456789012'
        self.vpc_id = 'vpc-abcdefgh'
        self.description = 'Allow access from the load balancer'
        self.vpc_peering_connection_id = 'pcx-11223344'
        self.user_id_group_pair = UserIDGroupPair(self.id, self.name, self.status, self.user_id, self.vpc_id)
        self.user_id_group_pair_with_desc = UserIDGroupPair(
            self.id, self.name, self.status, self.user_id, self.vpc_id, self.description
        )
        self.user_id_group_pair_with_peering = UserIDGroupPair(
            self.id, self.name, self.status, self.user_id, self.vpc_id,
            vpc_peering_connection_id=self.vpc_peering_connection_id
        )
        self.user_id_group_pair_full = UserIDGroupPair(
            self.id, self.name, self.status, self.user_id, self.vpc_id, self.description, self.vpc_peering_connection_id
        )

    def test_initialization(self):
        self.assertEqual(self.user_id_group_pair.id, self.id)
        self.assertEqual(self.user_id_group_pair.name, self.name)
        self.assertEqual(self.user_id_group_pair.status, self.status)
        self.assertEqual(self.user_id_group_pair.user_id, self.user_id)
        self.assertEqual(self.user_id_group_pair.vpc_id, self.vpc_id)
        self.assertIsNone(self.user_id_group_pair.description)
        self.assertIsNone(self.user_id_group_pair.vpc_peering_connection_id)

    def test_initialization_with_desc(self):
        self.assertEqual(self.user_id_group_pair_with_desc.id, self.id)
        self.assertEqual(self.user_id_group_pair_with_desc.name, self.name)
        self.assertEqual(self.user_id_group_pair_with_desc.status, self.status)
        self.assertEqual(self.user_id_group_pair_with_desc.user_id, self.user_id)
        self.assertEqual(self.user_id_group_pair_with_desc.vpc_id, self.vpc_id)
        self.assertEqual(self.user_id_group_pair_with_desc.description, self.description)
        self.assertIsNone(self.user_id_group_pair_with_desc.vpc_peering_connection_id)

    def test_initialization_with_peering(self):
        self.assertEqual(self.user_id_group_pair_with_peering.id, self.id)
        self.assertEqual(self.user_id_group_pair_with_peering.name, self.name)
        self.assertEqual(self.user_id_group_pair_with_peering.status, self.status)
        self.assertEqual(self.user_id_group_pair_with_peering.user_id, self.user_id)
        self.assertEqual(self.user_id_group_pair_with_peering.vpc_id, self.vpc_id)
        self.assertIsNone(self.user_id_group_pair_with_peering.description)
        self.assertEqual(self.user_id_group_pair_with_peering.vpc_peering_connection_id, self.vpc_peering_connection_id)

    def test_initialization_full(self):
        self.assertEqual(self.user_id_group_pair_full.id, self.id)
        self.assertEqual(self.user_id_group_pair_full.name, self.name)
        self.assertEqual(self.user_id_group_pair_full.status, self.status)
        self.assertEqual(self.user_id_group_pair_full.user_id, self.user_id)
        self.assertEqual(self.user_id_group_pair_full.vpc_id, self.vpc_id)
        self.assertEqual(self.user_id_group_pair_full.description, self.description)
        self.assertEqual(self.user_id_group_pair_full.vpc_peering_connection_id, self.vpc_peering_connection_id)

    def test_set_id(self):
        new_id = 'sg-87654321'
        self.user_id_group_pair_full.id = new_id
        self.assertEqual(self.user_id_group_pair_full.id, new_id)

    def test_set_name(self):
        new_name = 'ec2-sg'
        self.user_id_group_pair_full.name = new_name
        self.assertEqual(self.user_id_group_pair_full.name, new_name)

    def test_set_status(self):
        new_status = 'inactive'
        self.user_id_group_pair_full.status = new_status
        self.assertEqual(self.user_id_group_pair_full.status, new_status)

    def test_set_user_id(self):
        new_id = '987654321012'
        self.user_id_group_pair_full.user_id = new_id
        self.assertEqual(self.user_id_group_pair_full.user_id, new_id)

    def test_set_vpc_id(self):
        new_vpc_id = 'vpc-hgfedcba'
        self.user_id_group_pair_full.vpc_id = new_vpc_id
        self.assertEqual(self.user_id_group_pair_full.vpc_id, new_vpc_id)

    def test_set_description(self):
        new_description = 'New EC2 Security Group'
        self.user_id_group_pair_full.description = new_description
        self.assertEqual(self.user_id_group_pair_full.description, new_description)

    def test_set_vpc_peering_connection_id(self):
        new_id = 'pcx-44332211'
        self.user_id_group_pair_full.vpc_peering_connection_id = new_id
        self.assertEqual(self.user_id_group_pair_full.vpc_peering_connection_id, new_id)

    def test_str(self):
        expected_str = (
            f'UserIDGroupPair('
            f'id="{self.id}",'
            f'name="{self.name}",'
            f'status="{self.status}",'
            f'user_id="{self.user_id}",'
            f'vpc_id="{self.vpc_id}",'
            f'description="{self.description}",'
            f'vpc_peering_connection_id="{self.vpc_peering_connection_id}"'
            f')'
        )
        self.assertEqual(str(self.user_id_group_pair_full), expected_str)

    def test_to_dict(self):
        expected_dict = {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "user_id": self.user_id,
            "vpc_id": self.vpc_id,
            "description": self.description,
            "vpc_peering_connection_id": self.vpc_peering_connection_id
        }
        self.assertDictEqual(self.user_id_group_pair_full.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
