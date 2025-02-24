```json
[
  {
    "Title": "Ensure AWS Timestream Data Encryption Using KMS",
    "Description": "All data stored in AWS Timestream must be encrypted using AWS Key Management Service (KMS). If no customer managed key (CMK) is provided during setup, ensure that the Timestream-managed key (`alias/aws/timestream`) is automatically created and used for encryption.",
    "Applicability": "All Timestream databases and scheduled query resources",
    "Security Risk": "Unencrypted data may be vulnerable to unauthorized access, compromising confidentiality and data integrity.",
    "Default Behavior / Limitations": "Timestream automatically creates a Timestream-managed KMS key for encryption if no key is provided.",
    "Automation": "Automatically applied during Timestream database creation. Monitoring can be performed using AWS Config rule `kms-key-enabled` for ensuring key usage.",
    "References": [
      "https://docs.aws.amazon.com/timestream/latest/developerguide/KeyManagement.html"
    ]
  },
  {
    "Title": "Enable Automatic Annual Rotation for Customer Managed Keys (CMKs) in Timestream",
    "Description": "If a customer managed key (CMK) is being used for AWS Timestream, enable automatic annual key rotation to enhance key security by limiting the lifespan of cryptographic material.",
    "Applicability": "All customer managed keys used with Timestream",
    "Security Risk": "Non-rotated keys increase the risk of compromised keys being used indefinitely, potentially leading to unauthorized data decryption.",
    "Default Behavior / Limitations": "Automatic key rotation is not enabled by default and must be configured by the user.",
    "Automation": "Can be enforced using AWS Config rule `kms-cmk-rotation-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/timestream/latest/developerguide/KeyManagement.html"
    ]
  },
  {
    "Title": "Use Customer Managed Keys Following Best Practices for Timestream Scheduled Queries",
    "Description": "When using customer managed keys (CMKs) for Timestream scheduled query resources, ensure that best security practices for key management and permissions are followed, including restricting key usage permissions and enabling logging.",
    "Applicability": "All customer managed keys used with Timestream scheduled queries",
    "Security Risk": "Mismanagement of CMKs could lead to unauthorized access or misuse, potentially resulting in data breaches or loss.",
    "Default Behavior / Limitations": "User must ensure best practices are followed. AWS does not automatically enforce these practices.",
    "Automation": "Manual validation required for adherence to best practices. AWS Security Hub can be used to detect permission anomalies.",
    "References": [
      "https://docs.aws.amazon.com/timestream/latest/developerguide/KeyManagement.html",
      "https://docs.aws.amazon.com/kms/latest/developerguide/best-practices.html"
    ]
  },
  {
    "Title": "Avoid Use of External Key Stores with Timestream",
    "Description": "Do not plan to use KMS keys stored in an external key store (XKS) for AWS Timestream Live Analytics, as this feature is not supported.",
    "Applicability": "All AWS usage of Timestream",
    "Security Risk": "Attempting to use XKS keys could lead to operational failures and encryption/decryption errors, impacting data availability.",
    "Default Behavior / Limitations": "Timestream does not support external key stores for KMS keys.",
    "Automation": "Configuration limitations prevent automated enforcement. Manual design consideration required.",
    "References": [
      "https://docs.aws.amazon.com/timestream/latest/developerguide/KeyManagement.html"
    ]
  }
]
```