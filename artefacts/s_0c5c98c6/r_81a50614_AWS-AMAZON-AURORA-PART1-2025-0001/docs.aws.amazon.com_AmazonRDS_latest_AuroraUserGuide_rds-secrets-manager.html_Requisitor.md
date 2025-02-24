```json
[
  {
    "Description": "Aurora must automatically generate and store the master user password in AWS Secrets Manager for new or modified DB clusters or those restored from S3.",
    "Reference": "Section 'Overview of managing master user passwords with AWS Secrets Manager' - URL: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html",
    "Observations": "The default rotation period is seven days, which can be modified."
  },
  {
    "Description": "Aurora must encrypt secrets using a KMS key, either customer managed or the default key provided by Secrets Manager.",
    "Reference": "Managing master user password for a DB cluster with Secrets Manager - URL: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html",
    "Observations": "Once set, the KMS key cannot be changed unless the entire DB cluster is modified."
  },
  {
    "Description": "Permissions required for managing master user passwords in Secrets Manager must include `kms:DescribeKey`, `secretsmanager:CreateSecret`, and `secretsmanager:TagResource`.",
    "Reference": "Section 'Permissions required for Secrets Manager integration' - URL: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html",
    "Observations": "Additional permissions like `kms:Decrypt` and `kms:GenerateDataKey` are required for specific operations."
  },
  {
    "Description": "IAM policies must enforce that the master user password is managed by Aurora in AWS Secrets Manager during DB cluster creations and modifications.",
    "Reference": "Section 'Enforcing Aurora management of the master user password in AWS Secrets Manager' - URL: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html",
    "Observations": "This can be achieved by using IAM condition keys in policy statements."
  },
  {
    "Description": "Aurora must enable immediate password rotation upon user request using Secrets Manager's capabilities.",
    "Reference": "Section 'Rotating the master user password secret for a DB cluster' - URL: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html",
    "Observations": "To execute immediate rotation, both AWS CLI and RDS console instructions are provided."
  },
  {
    "Description": "Aurora must support retrieving and managing secret details using AWS CLI and RDS API, providing secret ARN, status, and KMS key info.",
    "Reference": "Section 'Viewing the details about a secret for a DB cluster' - URL: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html",
    "Observations": "The status values include 'creating', 'active', 'rotating', and 'impaired'."
  }
]
```
