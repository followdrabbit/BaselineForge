```json
[
  {
    "Description": "Timestream for LiveAnalytics encrypts at rest all user data stored in tables using encryption keys stored in AWS KMS.",
    "Reference": "Encryption at rest section of the documentation - URL: https://docs.aws.amazon.com/timestream/latest/developerguide/best-practices-security-preventative.html",
    "Observations": "This uses a single service default key (AWS owned CMK) for encrypting all tables. Service default keys can't be disabled."
  },
  {
    "Description": "Access to Timestream for LiveAnalytics must use IAM roles to obtain temporary access keys instead of storing AWS credentials directly in applications or EC2 instances.",
    "Reference": "Use IAM roles to authenticate access section of the documentation - URL: https://docs.aws.amazon.com/timestream/latest/developerguide/best-practices-security-preventative.html",
    "Observations": "This mitigates the risk of having long-term credentials compromised since they are not rotated automatically."
  },
  {
    "Description": "Implement least privilege by using IAM policies to grant permissions to access Timestream for LiveAnalytics APIs and resources.",
    "Reference": "Use IAM policies for base authorization section of the documentation - URL: https://docs.aws.amazon.com/timestream/latest/developerguide/best-practices-security-preventative.html",
    "Observations": "Provide permissions using AWS managed policies, customer managed policies, or tag-based authorization."
  },
  {
    "Description": "If storing sensitive or confidential data in Timestream for LiveAnalytics, consider encrypting the data client-side to protect it throughout its lifecycle.",
    "Reference": "Consider client-side encryption section of the documentation - URL: https://docs.aws.amazon.com/timestream/latest/developerguide/best-practices-security-preventative.html",
    "Observations": "Protects plaintext data in transit and rest ensuring it is not available to third parties."
  }
]
```