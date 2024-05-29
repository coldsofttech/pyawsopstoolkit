import unittest

from pyawsopstoolkit import Account


class TestAccount(unittest.TestCase):
    """Unit test cases for Account."""

    def setUp(self) -> None:
        self.number = '123456789012'
        self.account = Account(self.number)

    def test_initialization(self):
        self.assertEqual(self.account.number, self.number)

    def test_set_number(self):
        new_number = '987654321012'
        self.account.number = new_number
        self.assertEqual(self.account.number, new_number)

    def test_str(self):
        expected_str = (
            f'Account('
            f'number="{self.number}"'
            f')'
        )
        self.assertEqual(str(self.account), expected_str)

    def test_to_dict(self):
        expected_dict = {
            "number": self.number
        }
        self.assertDictEqual(self.account.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
