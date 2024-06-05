import unittest

from pyawsopstoolkit.models.ec2.network_interface import Group


class TestGroup(unittest.TestCase):
    """Unit test cases for Group."""

    def setUp(self) -> None:
        self.maxDiff = None
        self.params = {
            'id': 'sg-0123456789abcdef0',
            'name': 'default'
        }
        self.group = Group(self.params['id'], self.params['name'])

    def test_initialization(self):
        self.assertEqual(self.group.id, self.params['id'])
        self.assertEqual(self.group.name, self.params['name'])

    def test_setters(self):
        new_params = {
            'id': 'sg-0123456789abcdef1',
            'name': 'default_temp'
        }

        self.group.id = new_params['id']
        self.group.name = new_params['name']
        self.assertEqual(self.group.id, new_params['id'])
        self.assertEqual(self.group.name, new_params['name'])

    def test_invalid_types(self):
        invalid_params = {
            'id': 123,
            'name': 123
        }

        with self.assertRaises(TypeError):
            Group(invalid_params['id'], self.params['name'])
        with self.assertRaises(TypeError):
            Group(self.params['id'], invalid_params['name'])

        with self.assertRaises(TypeError):
            self.group.id = invalid_params['id']
        with self.assertRaises(TypeError):
            self.group.name = invalid_params['name']

    def test_to_dict(self):
        expected_dict = {
            "id": self.params['id'],
            "name": self.params['name']
        }
        self.assertDictEqual(self.group.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
