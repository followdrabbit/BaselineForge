```json
[
  {
    "Description": "Each database user account that the RDS Proxy connects to must have a separate secret in AWS Secrets Manager with keys 'username' and 'password'.",
    "Reference": "Setting up database credentials in AWS Secrets Manager for RDS Proxy - https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-secrets-arns.html",
    "Observations": "These secrets are used by the proxy to authenticate with the corresponding database user accounts."
  },
  {
    "Description": "RDS Proxy requires secrets in AWS Secrets Manager that are case-sensitive for SQL Server user accounts.",
    "Reference": "Note under Setting up database credentials - https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-secrets-arns.html",
    "Observations": "For SQL Server, application code must consider username case sensitivity in secrets."
  },
  {
    "Description": "AWS CLI and RDS API require Amazon Resource Names (ARNs) of the secrets for all DB accounts that the proxy accesses when creating a proxy.",
    "Reference": "When creating a proxy through the AWS CLI or RDS API - https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-secrets-arns.html",
    "Observations": "Ensure that all relevant secret ARNs are specified during the creation of the proxy."
  },
  {
    "Description": "To secure Secrets Manager secrets, a custom AWS KMS key can be used for encryption.",
    "Reference": "Example command for creating secrets encrypted with a custom AWS KMS key - https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-secrets-arns.html",
    "Observations": "Consider creating a custom KMS key to control encryption and permissions more securely."
  },
  {
    "Description": "Use AWS CLI to list all secrets owned by the AWS account to verify their names and ARNs.",
    "Reference": "AWS CLI command 'aws secretsmanager list-secrets' usage - https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-secrets-arns.html",
    "Observations": "Adjust the AWS CLI version for the correct output parameter; 'table' for version 2, 'text' for version 1."
  },
  {
    "Description": "Verify the correctness and format of stored credentials in a secret using the AWS CLI command 'aws secretsmanager get-secret-value'.",
    "Reference": "Command example for verifying secret credentials - https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-secrets-arns.html",
    "Observations": "Ensure the secret contains the 'username' and 'password' in JSON format."
  }
]
```