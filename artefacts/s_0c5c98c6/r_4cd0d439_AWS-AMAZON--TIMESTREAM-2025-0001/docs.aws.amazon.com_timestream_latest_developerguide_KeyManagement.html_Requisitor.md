```json
[
  {
    "Description": "Timestream Live Analytics requires the use of AWS KMS to encrypt your data. A Timestream-managed key is created automatically if no key is provided.",
    "Reference": "Key management section in the documentation - URL: https://docs.aws.amazon.com/timestream/latest/developerguide/KeyManagement.html",
    "Observations": "Ensure that the default configuration creates the `alias/aws/timestream` key if a user does not provide a key."
  },
  {
    "Description": "Support for KMS customer managed keys allows for more control over permissions and lifecycle, including automatic annual key rotation.",
    "Reference": "Key management section in the documentation - URL: https://docs.aws.amazon.com/timestream/latest/developerguide/KeyManagement.html",
    "Observations": "Verify that automatic annual rotation of customer managed keys is enabled if a customer managed key is used."
  },
  {
    "Description": "For Scheduled Query resources, Timestream uses its own KMS key if no key is provided, but customer managed keys are also supported.",
    "Reference": "Key management section in the documentation - URL: https://docs.aws.amazon.com/timestream/latest/developerguide/KeyManagement.html",
    "Observations": "Ensure customer managed keys, when used, follow best practices for security and management."
  },
  {
    "Description": "KMS keys in an external key store (XKS) are not supported by Timestream Live Analytics.",
    "Reference": "Key management section in the documentation - URL: https://docs.aws.amazon.com/timestream/latest/developerguide/KeyManagement.html",
    "Observations": "Consider this limitation when planning key management strategies that may involve external key stores."
  }
]
```