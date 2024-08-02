# Troubleshooting

This document provides comprehensive guidance on troubleshooting issues related to the package.

## SSL Certificate Error

**Error Message:**

```html
botocore.exceptions.SSLError: SSL validation failed for https://s3.eu-west-1.amazonaws.com/ [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl:c:1002).
```

**Description:**
This error typically occurs when `boto3` (a dependency) cannot verify your proxy's SSL certificate.
This situation arises if the proxy's certificate is self-signed or issued by your company's internal Certification
Authority (CA).
As a result, `boto3` cannot locate your company's CA root certificate in the local CA registry.

**Solution:**
To resolve this issue, set the environment variable `AWS_CA_BUNDLE` to the path of your proxy's certificate.
This should be done before creating the `Session` object. The following code snippet demonstrates how to set this
variable.

```python
import os

# Set the path to your company's CA certificate
os.environ['AWS_CA_BUNDLE'] = '/path/to/certificate.crt'
```

**Example:**
Here's an example of initializing a session using the `pyawsopstoolkit` package with the specified CA certificate.

```python
from pyawsopstoolkit import Session
import os

# Set the path to your company's CA certificate
os.environ['AWS_CA_BUNDLE'] = '/path/to/certificate.crt'

# Create a session with the default profile
session = Session(profile_name='default')
```

Ensure the path provided in `os.environ['AWS_CA_BUNDLE']` points to the correct location of your proxy's certificate
file.
This will allow `boto3` to trust the self-signed certificate and establish a secure connection.

**Additional Notes:**

- Make sure the certificate file is accessible and properly formatted.
- If the issue persists, verify that the certificate is valid and correctly installed on your system.