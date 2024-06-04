import unittest

from pyawsopstoolkit.models.ec2.security_group import UserIDGroupPair


class TestUserIDGroupPair(unittest.TestCase):
    """Unit test cases for UserIDGroupPair."""

    def setUp(self) -> None:
        self.maxDiff = None
        self.params = {
            'id': 'sg-12345678',
            'name': 'load-balancer-sg',
            'status': 'active',
            'user_id': '123456789012',
            'vpc_id': 'vpc-abcdefgh',
            'description': 'Allow access from the load balancer',
            'vpc_peering_connection_id': 'pcx-11223344'
        }
        self.user_id_group_pair = self.create_user_id_group_pair()
        self.user_id_group_pair_with_desc = self.create_user_id_group_pair(description=self.params['description'])
        self.user_id_group_pair_with_peering = self.create_user_id_group_pair(
            vpc_peering_connection_id=self.params['vpc_peering_connection_id']
        )
        self.user_id_group_pair_full = self.create_user_id_group_pair(
            description=self.params['description'],
            vpc_peering_connection_id=self.params['vpc_peering_connection_id']
        )

    def create_user_id_group_pair(self, **kwargs):
        return UserIDGroupPair(
            id=self.params['id'],
            name=self.params['name'],
            status=self.params['status'],
            user_id=self.params['user_id'],
            vpc_id=self.params['vpc_id'],
            **kwargs
        )

    def test_initialization(self):
        self.assertEqual(self.user_id_group_pair.id, self.params['id'])
        self.assertEqual(self.user_id_group_pair.name, self.params['name'])
        self.assertEqual(self.user_id_group_pair.status, self.params['status'])
        self.assertEqual(self.user_id_group_pair.user_id, self.params['user_id'])
        self.assertEqual(self.user_id_group_pair.vpc_id, self.params['vpc_id'])
        self.assertIsNone(self.user_id_group_pair.description)
        self.assertIsNone(self.user_id_group_pair.vpc_peering_connection_id)

    def test_initialization_with_optional_params(self):
        test_cases = [
            (self.user_id_group_pair_with_desc, self.params['description'], None),
            (self.user_id_group_pair_with_peering, None, self.params['vpc_peering_connection_id']),
            (self.user_id_group_pair_full, self.params['description'], self.params['vpc_peering_connection_id'])
        ]
        for user_id_group_pair, description, peering in test_cases:
            with self.subTest(user_id_group_pair=user_id_group_pair):
                self.assertEqual(user_id_group_pair.id, self.params['id'])
                self.assertEqual(user_id_group_pair.name, self.params['name'])
                self.assertEqual(user_id_group_pair.status, self.params['status'])
                self.assertEqual(user_id_group_pair.user_id, self.params['user_id'])
                self.assertEqual(user_id_group_pair.vpc_id, self.params['vpc_id'])
                self.assertEqual(user_id_group_pair.description, description)
                self.assertEqual(user_id_group_pair.vpc_peering_connection_id, peering)

    def test_setters(self):
        new_params = {
            'id': 'sg-87654321',
            'name': 'web-servers-sg',
            'status': 'inactive',
            'user_id': '987654321012',
            'vpc_id': 'vpc-hgfedcba',
            'description': 'Allow access from the web servers',
            'vpc_peering_connection_id': 'pcx-44332211'
        }

        self.user_id_group_pair_full.id = new_params['id']
        self.user_id_group_pair_full.name = new_params['name']
        self.user_id_group_pair_full.status = new_params['status']
        self.user_id_group_pair_full.user_id = new_params['user_id']
        self.user_id_group_pair_full.vpc_id = new_params['vpc_id']
        self.user_id_group_pair_full.description = new_params['description']
        self.user_id_group_pair_full.vpc_peering_connection_id = new_params['vpc_peering_connection_id']

        self.assertEqual(self.user_id_group_pair_full.id, new_params['id'])
        self.assertEqual(self.user_id_group_pair_full.name, new_params['name'])
        self.assertEqual(self.user_id_group_pair_full.status, new_params['status'])
        self.assertEqual(self.user_id_group_pair_full.user_id, new_params['user_id'])
        self.assertEqual(self.user_id_group_pair_full.vpc_id, new_params['vpc_id'])
        self.assertEqual(self.user_id_group_pair_full.description, new_params['description'])
        self.assertEqual(
            self.user_id_group_pair_full.vpc_peering_connection_id, new_params['vpc_peering_connection_id']
        )

    def test_invalid_types(self):
        invalid_params = {
            'id': 123,
            'name': 123,
            'status': 123,
            'user_id': 123,
            'vpc_id': 123,
            'description': 123,
            'vpc_peering_connection_id': 123
        }

        with self.assertRaises(TypeError):
            UserIDGroupPair(
                id=invalid_params['id'],
                name=self.params['name'],
                status=self.params['status'],
                user_id=self.params['user_id'],
                vpc_id=self.params['vpc_id']
            )
        with self.assertRaises(TypeError):
            UserIDGroupPair(
                id=self.params['id'],
                name=invalid_params['name'],
                status=self.params['status'],
                user_id=self.params['user_id'],
                vpc_id=self.params['vpc_id']
            )
        with self.assertRaises(TypeError):
            UserIDGroupPair(
                id=self.params['id'],
                name=self.params['name'],
                status=invalid_params['status'],
                user_id=self.params['user_id'],
                vpc_id=self.params['vpc_id']
            )
        with self.assertRaises(TypeError):
            UserIDGroupPair(
                id=self.params['id'],
                name=self.params['name'],
                status=self.params['status'],
                user_id=invalid_params['user_id'],
                vpc_id=self.params['vpc_id']
            )
        with self.assertRaises(TypeError):
            UserIDGroupPair(
                id=self.params['id'],
                name=self.params['name'],
                status=self.params['status'],
                user_id=self.params['user_id'],
                vpc_id=invalid_params['vpc_id']
            )
        with self.assertRaises(TypeError):
            self.create_user_id_group_pair(description=invalid_params['description'])
        with self.assertRaises(TypeError):
            self.create_user_id_group_pair(vpc_peering_connection_id=invalid_params['vpc_peering_connection_id'])

        with self.assertRaises(TypeError):
            self.user_id_group_pair_full.id = invalid_params['id']
        with self.assertRaises(TypeError):
            self.user_id_group_pair_full.name = invalid_params['name']
        with self.assertRaises(TypeError):
            self.user_id_group_pair_full.status = invalid_params['status']
        with self.assertRaises(TypeError):
            self.user_id_group_pair_full.user_id = invalid_params['user_id']
        with self.assertRaises(TypeError):
            self.user_id_group_pair_full.vpc_id = invalid_params['vpc_id']
        with self.assertRaises(TypeError):
            self.user_id_group_pair_full.description = invalid_params['description']
        with self.assertRaises(TypeError):
            self.user_id_group_pair_full.vpc_peering_connection_id = invalid_params['vpc_peering_connection_id']

    def test_to_dict(self):
        expected_dict = {
            "id": self.params['id'],
            "name": self.params['name'],
            "status": self.params['status'],
            "user_id": self.params['user_id'],
            "vpc_id": self.params['vpc_id'],
            "description": self.params['description'],
            "vpc_peering_connection_id": self.params['vpc_peering_connection_id']
        }
        self.assertDictEqual(self.user_id_group_pair_full.to_dict(), expected_dict)

    def test_to_dict_with_missing_fields(self):
        expected_dict = {
            "id": self.params['id'],
            "name": self.params['name'],
            "status": self.params['status'],
            "user_id": self.params['user_id'],
            "vpc_id": self.params['vpc_id'],
            "description": None,
            "vpc_peering_connection_id": None
        }
        self.assertDictEqual(self.user_id_group_pair.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
