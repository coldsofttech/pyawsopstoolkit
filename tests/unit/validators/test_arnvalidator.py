import unittest

from pyawsopstoolkit.exceptions import ValidationError
from pyawsopstoolkit.validators import ArnValidator


class TestArnValidator(unittest.TestCase):
    """Unit test cases for ArnValidator class."""

    def test_arn_valid(self):
        """Test if arn works as expected."""
        arns = {
            "IAMSLR": "arn:aws:iam::123456789012:role/aws-service-role/"
                      "access-analyzer.amazonaws.com/AWSServiceRoleForAccessAnalyzer",
            "IAMSR": "arn:aws:iam::123456789012:role/service-role/QuickSightAction",
            "IAMUser": "arn:aws:iam::123456789012:user/JohnDoe",
            "IAMUser_OrgChart": "arn:aws:iam::123456789012:user/division_abc/subdivision_xyz/JaneDoe",
            "Lambda": "arn:aws:lambda:eu-west-1:123456789012:function:function-name",
            "OIDC": "arn:aws:iam::123456789012:oidc-provider/oidc.eks.us-west-2.amazonaws.com/"
                    "id/a1b2c3d4567890abcdefEXAMPLE11111",
            "S3Bucket": "arn:aws:s3:::bucket-name",
            "S3Object1": "arn:aws:s3:::bucket-name/object-key",
            "S3Object2": "arn:aws:s3:::bucket-name/*",
            "SNSTopic": "arn:aws:sns:us-east-1:123456789012:example-sns-topic-name",
            "VPC": "arn:aws:ec2:us-east-1:123456789012:vpc/vpc-0e9801d129EXAMPLE"
        }

        for key, value in arns.items():
            self.assertTrue(ArnValidator.arn(value, custom_error_message=f'{key} is not valid.'))

    def test_arn_invalid(self):
        """Test if arn raises exception as expected."""
        arns = {
            "Test1": ":aws:iam::123456789012:user/JohnDoe",
            "Test2": "arn:junk:iam::123456789012:user/JohnDoe",
            "Test3": "arn::iam:us-east-1:123456789012:user",
            "Test4": "arn:aws:sns:us-east-1:123456789012345:*",
            "Test5": "arn:aws:sns:eu@west1:123:role"
        }

        for key, value in arns.items():
            with self.assertRaises(Exception) as context:
                ArnValidator.arn(value, custom_error_message=f'{key} is not valid.')

            self.assertTrue(isinstance(context.exception, (ValidationError, TypeError)))


if __name__ == "__main__":
    unittest.main()
