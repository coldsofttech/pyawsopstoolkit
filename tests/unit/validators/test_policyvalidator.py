import unittest

from pyawsopstoolkit.exceptions import ValidationError
from pyawsopstoolkit.validators import PolicyValidator


class TestPolicyValidator(unittest.TestCase):
    """Unit test cases for PolicyValidator class."""

    def test_version_valid(self):
        """Test if version works as expected."""
        versions = {
            "Version1": "2008-10-17",
            "Version2": "2012-10-17"
        }

        for key, value in versions.items():
            self.assertTrue(PolicyValidator._version(value, custom_error_message=f'{key} is not valid.'))

    def test_version_invalid(self):
        """Test if version raises exception as expected."""
        versions = {
            "Version1": 123,
            "Version2": "2024-05-06"
        }

        for key, value in versions.items():
            with self.assertRaises(Exception) as context:
                PolicyValidator._version(value, custom_error_message=f'{key} is not valid.')

                self.assertTrue(isinstance(context.exception, (ValidationError, TypeError)))

    def test_id_valid(self):
        """Test if the id works as expected."""
        self.assertTrue(PolicyValidator._id('sample-id'))

    def test_id_invalid(self):
        """Test if the id raises exception as expected."""
        with self.assertRaises(TypeError):
            PolicyValidator._id(1)

    def test_sid_valid(self):
        """Test if sid works as expected."""
        self.assertTrue(PolicyValidator._sid('sample-id'))

    def test_sid_invalid(self):
        """Test if sid raises exception as expected."""
        with self.assertRaises(TypeError):
            PolicyValidator._sid(1)

    def test_effect_valid(self):
        """Test if the effect works as expected."""
        effects = {
            "Effect1": "Allow",
            "Effect2": "Deny"
        }

        for key, value in effects.items():
            self.assertTrue(PolicyValidator._effect(value, custom_error_message=f'{key} is not valid.'))

    def test_effect_invalid(self):
        """Test if the effect raises exception as expected."""
        effects = {
            "Effect1": 1,
            "Effect2": "NotAllow"
        }

        for key, value in effects.items():
            with self.assertRaises(Exception) as context:
                PolicyValidator._effect(value, custom_error_message=f'{key} is not valid.')

            self.assertTrue(isinstance(context.exception, (ValidationError, TypeError)))

    def test_action_valid(self):
        """Test if the action works as expected."""
        actions = {
            "Action1": "*",
            "Action2": ["iam:*", "ec2:*"],
            "Action3": ["*"]
        }

        for key, value in actions.items():
            self.assertTrue(PolicyValidator._action(value, custom_error_message=f'{key} is not valid.'))

    def test_action_invalid(self):
        """Test if the action raises exception as expected."""
        actions = {
            "Action1": ["iam:*", 1],
            "Action2": 1,
            "Action3": "iam:*",
            "Action4": []
        }

        for key, value in actions.items():
            with self.assertRaises(Exception) as context:
                PolicyValidator._action(value)

            self.assertTrue(isinstance(context.exception, (ValidationError, TypeError)))

    def test_resource_valid(self):
        """Test if the resource works as expected."""
        resources = {
            "Resource1": "*",
            "Resource2": "role",
            "Resource3": ["role1"],
            "Resource4": ["role1", "role2"]
        }

        for key, value in resources.items():
            self.assertTrue(PolicyValidator._resource(value, custom_error_message=f'{key} is not valid.'))

    def test_resource_invalid(self):
        """Test if the resource raises exception as expected."""
        resources = {
            "Resource1": ["role1", 1],
            "Resource2": 1,
            "Resource3": []
        }

        for key, value in resources.items():
            with self.assertRaises(Exception) as context:
                PolicyValidator._resource(value)

            self.assertTrue(isinstance(context.exception, (ValidationError, TypeError)))

    def test_principal_valid(self):
        """Test if the principal works as expected."""
        principals = {
            "Principal1": "*",
            "Principal2": {"AWS": ["pri1"]},
            "Principal3": {"Service": ["service1", "service2"]}
        }

        for key, value in principals.items():
            self.assertTrue(PolicyValidator._principal(value, custom_error_message=f'{key} is not valid.'))

    def test_principal_invalid(self):
        """Test if the principal raises exception as expected."""
        principals = {
            "Principal1": "pri1",
            "Principal2": 1,
            "Principal3": {"test": ["pri1"]},
            "Principal4": {"AWS": "pri1"},
            "Principal5": {},
            "Principal6": {"AWS": []}
        }

        for key, value in principals.items():
            with self.assertRaises(Exception) as context:
                PolicyValidator._principal(value)

            self.assertTrue(isinstance(context.exception, (ValidationError, TypeError)))

    def test_condition_valid(self):
        """Test if the condition works as expected."""
        conditions = {
            "Condition1": {"Bool": {"aws:SecureTransport": "true"}},
            "Condition2": {"ForAnyValue:StringEquals": {"dynamodb:Attributes": ["ID", "PostDateTime"]}}
        }

        for key, value in conditions.items():
            self.assertTrue(PolicyValidator._condition(value, custom_error_message=f'{key} is not valid.'))

    def test_condition_invalid(self):
        """Test if the condition raises exception as expected."""
        conditions = {
            "Condition1": {},
            "Condition2": {1: {}},
            "Condition3": {"condition_map": {}},
            "Condition4": {"condition_map": {1: {}}},
            "Condition5": {"condition_map": {"condition_type_string": {}}},
            "Condition6": {"condition_map": {"condition_type_string": {1: ["value1"]}}},
            "Condition7": {"condition_map": {"condition_type_string": {"condition_key_string": []}}},
            "Condition8": {"condition_map": {"condition_type_string": {"condition_key_string": {}}}}
        }

        for key, value in conditions.items():
            with self.assertRaises(Exception) as context:
                PolicyValidator._condition(value)

            self.assertTrue(isinstance(context.exception, (ValidationError, TypeError)))

    def test_policy_valid(self):
        """Test if the policy works as expected."""
        policies = {
            "Policy1": {
                "Version": "2012-10-17",
                "Id": "1",
                "Statement": {
                    "Sid": "1",
                    "Principal": "*",
                    "Effect": "Allow",
                    "Action": "*",
                    "Resource": "*",
                    "Condition": {
                        "Bool": {
                            "aws:SecureTransport": "true"
                        }
                    }
                }
            },
            "Policy2": {
                "Id": "1",
                "Statement": {
                    "Sid": "1",
                    "Principal": "*",
                    "Effect": "Allow",
                    "Action": "*",
                    "Resource": "*",
                    "Condition": {
                        "Bool": {
                            "aws:SecureTransport": "true"
                        }
                    }
                }
            },
            "Policy3": {
                "Statement": {
                    "Sid": "1",
                    "Principal": "*",
                    "Effect": "Allow",
                    "Action": "*",
                    "Resource": "*",
                    "Condition": {
                        "Bool": {
                            "aws:SecureTransport": "true"
                        }
                    }
                }
            },
            "Policy4": {
                "Statement": {
                    "NotPrincipal": "*",
                    "Effect": "Allow",
                    "Action": "*",
                    "Resource": "*",
                    "Condition": {
                        "Bool": {
                            "aws:SecureTransport": "true"
                        }
                    }
                }
            },
            "Policy5": {
                "Statement": {
                    "Effect": "Allow",
                    "Action": "*",
                    "Resource": "*",
                    "Condition": {
                        "Bool": {
                            "aws:SecureTransport": "true"
                        }
                    }
                }
            },
            "Policy6": {
                "Statement": {
                    "Effect": "Allow",
                    "Action": "*",
                    "Resource": "*"
                }
            }
        }

        for key, value in policies.items():
            self.assertTrue(PolicyValidator.policy(value, custom_error_message=f'{key} is not valid.'))

    def test_policy_invalid(self):
        """Test if the policy raises exception as expected."""
        policies = {
            "Policy1": {
                "Version": "2012-10-17",
                "Id": "1"
            },
            "Policy2": {
                "Statement": {
                    "Sid": "1",
                    "Principal": "*",
                    "Action": "*",
                    "Resource": "*",
                    "Condition": {
                        "Bool": {
                            "aws:SecureTransport": "true"
                        }
                    }
                }
            },
            "Policy3": {
                "Statement": {
                    "Sid": "1",
                    "Principal": "*",
                    "Effect": "Allow",
                    "Resource": "*",
                    "Condition": {
                        "Bool": {
                            "aws:SecureTransport": "true"
                        }
                    }
                }
            },
            "Policy4": {
                "Statement": {
                    "Sid": "1",
                    "Principal": "*",
                    "Effect": "Allow",
                    "Action": "*",
                    "Condition": {
                        "Bool": {
                            "aws:SecureTransport": "true"
                        }
                    }
                }
            }
        }

        for key, value in policies.items():
            with self.assertRaises(Exception) as context:
                PolicyValidator.policy(value)

            self.assertTrue(isinstance(context.exception, (ValidationError, TypeError)))


if __name__ == "__main__":
    unittest.main()
