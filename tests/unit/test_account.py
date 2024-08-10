import unittest

from pyawsopstoolkit.account import Account


class TestAccount(unittest.TestCase):
    def setUp(self) -> None:
        self.maxDiff = None
        self.params = {
            'number': '123456789012'
        }
        self.account = Account(self.params['number'])

    def test_initialization(self):
        self.assertEqual(self.account.number, self.params['number'])

    def test_setters(self):
        new_params = {
            'number': '987654321012'
        }

        self.account.number = new_params['number']
        self.assertEqual(self.account.number, new_params['number'])

    def test_invalid_types(self):
        invalid_params = {
            'number': 123
        }

        with self.assertRaises(TypeError):
            Account(invalid_params['number'])
        with self.assertRaises(TypeError):
            self.account.number = invalid_params['number']

    def test_to_dict(self):
        expected_dict = {
            "number": self.params['number']
        }
        self.assertDictEqual(self.account.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
