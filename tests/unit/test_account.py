import unittest

from pyawsopstoolkit import Account


class TestAccount(unittest.TestCase):
    """Unit test cases for Account class."""

    def setUp(self) -> None:
        self.number = "123456789012"
        self.account = Account(self.number)

    def test_init_valid(self):
        """Test if init works as expected."""
        account = Account(self.number)
        self.assertEqual(account._number, self.number)

    def test_init_invalid(self):
        """Test if init raises exception as expected."""
        with self.assertRaises(TypeError):
            Account(123456789012)

    def test_get_number(self):
        """Test if number works as expected."""
        self.assertEqual(self.account.number, self.number)

    def test_set_number_valid(self):
        """Test if number works as expected."""
        new_number = '012345678910'
        self.account.number = new_number
        self.assertEqual(self.account.number, new_number)

    def test_set_number_invalid(self):
        """Test if number raises exception as expected."""
        with self.assertRaises(TypeError):
            self.account.number = 123456789012


if __name__ == "__main__":
    unittest.main()
