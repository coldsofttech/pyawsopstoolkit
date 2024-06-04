import unittest

from pyawsopstoolkit.models.ec2.security_group import PrefixList


class TestPrefixList(unittest.TestCase):
    """Unit test cases for PrefixList."""

    def setUp(self) -> None:
        self.maxDiff = None
        self.params = {
            'id': 'pl-12345678',
            'description': 'Sample Prefix List'
        }
        self.prefix_list = self.create_prefix_list()
        self.prefix_list_full = self.create_prefix_list(description=self.params['description'])

    def create_prefix_list(self, **kwargs):
        return PrefixList(self.params['id'], **kwargs)

    def test_initialization(self):
        self.assertEqual(self.prefix_list.id, self.params['id'])
        self.assertIsNone(self.prefix_list.description)

    def test_initialization_with_optional_params(self):
        test_cases = [
            (self.prefix_list_full, self.params['description'])
        ]
        for prefix_list, description in test_cases:
            with self.subTest(prefix_list=prefix_list):
                self.assertEqual(prefix_list.id, self.params['id'])
                self.assertEqual(prefix_list.description, description)

    def test_setters(self):
        new_params = {
            'id': 'pl-87654321',
            'description': 'Updated Prefix List'
        }

        self.prefix_list_full.id = new_params['id']
        self.prefix_list_full.description = new_params['description']

        self.assertEqual(self.prefix_list_full.id, new_params['id'])
        self.assertEqual(self.prefix_list_full.description, new_params['description'])

    def test_invalid_types(self):
        invalid_params = {
            'id': 123,
            'description': 123
        }

        with self.assertRaises(TypeError):
            PrefixList(invalid_params['id'])
        with self.assertRaises(TypeError):
            self.create_prefix_list(description=invalid_params['description'])

        with self.assertRaises(TypeError):
            self.prefix_list_full.id = invalid_params['id']
        with self.assertRaises(TypeError):
            self.prefix_list_full.description = invalid_params['description']

    def test_to_dict(self):
        expected_dict = {
            "id": self.params['id'],
            "description": self.params['description']
        }
        self.assertDictEqual(self.prefix_list_full.to_dict(), expected_dict)

    def test_to_dict_with_missing_fields(self):
        expected_dict = {
            "id": self.params['id'],
            "description": None
        }
        self.assertDictEqual(self.prefix_list.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
