import unittest

from pyawsopstoolkit.models.ec2.security_group import PrefixListID


class TestPrefixListID(unittest.TestCase):
    """Unit test cases for PrefixListID."""

    def setUp(self) -> None:
        self.id = 'pl-12345678'
        self.description = 'Sample Prefix List'
        self.prefix_list = PrefixListID(self.id)
        self.prefix_list_with_desc = PrefixListID(self.id, self.description)

    def test_initialization(self):
        self.assertEqual(self.prefix_list.id, self.id)
        self.assertIsNone(self.prefix_list.description)

    def test_initialization_with_desc(self):
        self.assertEqual(self.prefix_list_with_desc.id, self.id)
        self.assertEqual(self.prefix_list_with_desc.description, self.description)

    def test_set_id(self):
        new_id = 'pl-87654321'
        self.prefix_list_with_desc.id = new_id
        self.assertEqual(self.prefix_list_with_desc.id, new_id)

    def test_set_description(self):
        new_description = 'New Prefix List'
        self.prefix_list_with_desc.description = new_description
        self.assertEqual(self.prefix_list_with_desc.description, new_description)

    def test_str(self):
        expected_str = (
            f'PrefixListID('
            f'id="{self.id}",'
            f'description="{self.description}"'
            f')'
        )
        self.assertEqual(str(self.prefix_list_with_desc), expected_str)

    def test_to_dict(self):
        expected_dict = {
            "id": self.id,
            "description": self.description
        }
        self.assertDictEqual(self.prefix_list_with_desc.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
