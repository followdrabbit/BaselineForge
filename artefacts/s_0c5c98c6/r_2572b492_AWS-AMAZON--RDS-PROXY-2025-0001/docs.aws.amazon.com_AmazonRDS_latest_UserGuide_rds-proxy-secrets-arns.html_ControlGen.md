```json
[
  {
    "Title": "Separate Secrets for Each Database User Account in AWS Secrets Manager",
    "Description": "Each RDS Proxy database user must have an individual secret in AWS Secrets Manager, containing JSON keys 'username' and 'password'. This ensures secure and isolated credential management for each account.",
    "Applicability": "All accounts using RDS Proxy",
    "Security Risk": "If multiple users share a secret, compromise of one account can affect access to others, violating the principle of least privilege.",
    "Default Behavior / Limitations": "AWS Secrets Manager allows the creation of multiple secrets, but it must be enforced manually.",
    "Automation": "Manual setup required to create and manage individual secrets for each database user account.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-secrets-arns.html"
    ]
  },
  {
    "Title": "Ensure Case-Sensitivity for SQL Server User Account Secrets",
    "Description": "RDS Proxy secrets for SQL Server accounts in AWS Secrets Manager must be created with attention to case-sensitivity of usernames to prevent authentication issues.",
    "Applicability": "RDS Proxy instances connecting to SQL Server databases",
    "Security Risk": "Ignoring case-sensitivity may lead to authentication failures or unauthorized access if usernames are incorrectly stored.",
    "Default Behavior / Limitations": "By default, usernames are case-sensitive in SQL Server.",
    "Automation": "Manual verification required to ensure correct username casing in secrets.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-secrets-arns.html"
    ]
  },
  {
    "Title": "Specify Secret ARNs When Creating RDS Proxy via AWS CLI or API",
    "Description": "Include the ARNs of all necessary AWS Secrets Manager secrets for DB accounts when provisioning an RDS Proxy using AWS CLI or API. This ensures accurate proxy configuration.",
    "Applicability": "AWS CLI and API interactions for creating RDS Proxies",
    "Security Risk": "Omission of secret ARNs during proxy creation can result in misconfigurations, leading to access issues.",
    "Default Behavior / Limitations": "Specification of secret ARNs is a required step in proxy setup.",
    "Automation": "Manual process to specify ARNs during AWS CLI or API proxy creation.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-secrets-arns.html"
    ]
  },
  {
    "Title": "Encrypt Secrets in AWS Secrets Manager with a Custom AWS KMS Key",
    "Description": "Utilize a custom AWS KMS key for encrypting secrets stored in AWS Secrets Manager. This controls who can access and manage the key, enhancing overall security.",
    "Applicability": "AWS accounts using AWS Secrets Manager",
    "Security Risk": "Secrets may be inadequately protected if not encrypted with a custom KMS key, leading to potential unauthorized access.",
    "Default Behavior / Limitations": "By default, Secrets Manager uses the default KMS key for encryption unless a custom key is specified.",
    "Automation": "Setup requires manual configuration of KMS key usage during secret creation or modification.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-secrets-arns.html"
    ]
  },
  {
    "Title": "List and Verify Secrets in AWS Secrets Manager Using AWS CLI",
    "Description": "Use the 'aws secretsmanager list-secrets' command to list secret names and ARNs, and 'aws secretsmanager get-secret-value' to verify the correctness of stored credentials.",
    "Applicability": "AWS accounts managing secrets in AWS Secrets Manager",
    "Security Risk": "Incorrect secret configurations can lead to unauthorized access or service disruptions.",
    "Default Behavior / Limitations": "Command line operations are not automated and require user intervention.",
    "Automation": "Manual execution of AWS CLI commands required to retrieve and verify secrets.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-secrets-arns.html"
    ]
  }
]
```