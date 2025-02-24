```json
[
  {
    "Description": "IAM database authentication must be configured to use SSL/TLS for encrypting network traffic to and from the database.",
    "Reference": "[Using SSL/TLS to encrypt a connection to a DB cluster](./UsingWithRDS.SSL.html) - URL: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html",
    "Observations": "Ensure SSL/TLS is enabled in the database configuration."
  },
  {
    "Description": "Avoid exceeding 200 new IAM database authentication connections per second to prevent throttling.",
    "Reference": "Recommendations for IAM database authentication - URL: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html",
    "Observations": "Implement connection pooling or use RDS Proxy to manage high frequency connections."
  },
  {
    "Description": "Authentication tokens for IAM database authentication have a lifetime of 15 minutes.",
    "Reference": "IAM database authentication section - URL: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html",
    "Observations": "Tokens should be reused whenever possible within their validity period."
  },
  {
    "Description": "Ensure IAM DB authorization has between 300 and 1000 MiB extra memory on the database cluster for reliable connectivity.",
    "Reference": "Limitations for IAM database authentication - URL: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html",
    "Observations": "If using a burstable class instance, adjust memory usage parameters to accommodate this requirement."
  },
  {
    "Description": "CloudWatch and CloudTrail do not log IAM authentication activities or generate-db-auth-token API calls.",
    "Reference": "Limitations for IAM database authentication - URL: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html",
    "Observations": "Consider additional logging mechanisms to monitor IAM authentication activities."
  },
  {
    "Description": "For Aurora PostgreSQL, ensure IAM role (`rds_iam`) is used for authentication instead of password-based methods.",
    "Reference": "Limitations for IAM database authentication - URL: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html",
    "Observations": "This configuration change requires user to log in as an IAM user."
  }
]
```