```json
[
  {
    "Title": "Enforce Use of Temporary Security Credentials for Amazon SimpleDB Access",
    "Description": "Configure IAM roles to provide temporary security credentials for accessing Amazon SimpleDB. Ensure that all request signatures replace AWSAccessKeyId with these temporary credentials and include a valid SecurityToken parameter.",
    "Applicability": "All users accessing Amazon SimpleDB",
    "Security Risk": "Failure to use temporary credentials could lead to unauthorized access if permanent access keys are compromised, increasing the risk of data exposure and credential misuse.",
    "Default Behavior / Limitations": "Temporary security credentials must be generated through AWS STS and configured explicitly for SimpleDB access. AWS IAM does not enforce this automatically.",
    "Automation": "This control can be automated using IAM roles configured with AWS STS and monitoring access patterns via AWS CloudTrail logs.",
    "References": [
      "https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/UsingTemporarySecurityCredentials_SDB.html",
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html"
    ]
  },
  {
    "Title": "Ensure HMAC-SHA256 Signing Method for SimpleDB Requests Using Temporary Credentials",
    "Description": "Verify that all requests to Amazon SimpleDB, when using temporary security credentials, are signed using the HMAC-SHA256 method. The SignatureMethod field in these requests must be set to HmacSHA256.",
    "Applicability": "All API requests to Amazon SimpleDB using temporary security credentials",
    "Security Risk": "Using an insecure or unsupported signing method could allow unauthorized modification of requests, leading to potential replay attacks or data integrity issues.",
    "Default Behavior / Limitations": "AWS SDKs and tools typically use HMAC-SHA256 by default. However, custom implementations must be configured to enforce this explicitly.",
    "Automation": "Automate verification using tools that inspect API request headers and verify the SignatureMethod field. AWS CloudTrail can be configured to capture events, which can then be analyzed.",
    "References": [
      "https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/UsingTemporarySecurityCredentials_SDB.html",
      "https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html"
    ]
  }
]
```