```json
[
  {
    "Title": "Separate Bucket for Amazon S3 Server Access Logs",
    "Description": "Configure Amazon S3 Server Access Logging to use a different bucket for storing access logs. This ensures logs are stored separately for security and audit purposes.",
    "Applicability": "All AWS accounts using Amazon S3",
    "Security Risk": "Storing access logs in the same bucket as the source could lead to log tampering or loss in case the bucket is compromised.",
    "Default Behavior / Limitations": "Amazon S3 allows logs to be stored in the same bucket by default. Separate log storage must be configured manually.",
    "Automation": "Use AWS Config to monitor if server access logs are being stored in a separate bucket.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/S3/server-access-log-storage-different-bucket.html"
    ]
  },
  {
    "Title": "Block Public Access to S3 at Account Level",
    "Description": "Ensure that Amazon S3 public access is blocked at the AWS account level to prevent unintended public exposure of data.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Public access to data increases the risk of data breach and unauthorized access.",
    "Default Behavior / Limitations": "Public access is not blocked by default; users need to explicitly configure account-level settings.",
    "Automation": "Enforce using AWS Config rule `s3-account-level-public-access-blocks`.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/S3/account-public-access-block.html"
    ]
  },
  {
    "Title": "Block Public Access at S3 Bucket Level",
    "Description": "Ensure that Amazon S3 public access is blocked at the individual bucket level to prevent unintended data exposure.",
    "Applicability": "All AWS S3 buckets",
    "Security Risk": "Public access increases the risk of unauthorized access and data leakage.",
    "Default Behavior / Limitations": "Public access is not blocked by default at the bucket level.",
    "Automation": "Automatable using AWS Config with `s3-bucket-public-read-prohibited`, `s3-bucket-public-write-prohibited`, `s3-bucket-policy-public`, and `s3-block-public-access-bucket` rules.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/S3/bucket-public-access-block.html"
    ]
  },
  {
    "Title": "Restrict FULL_CONTROL ACLs for Authenticated Users on S3 Buckets",
    "Description": "Ensure that S3 buckets do not allow FULL_CONTROL access to AWS authenticated users via ACLs.",
    "Applicability": "All AWS S3 buckets",
    "Security Risk": "FULL_CONTROL access allows users to modify and delete data, potentially leading to unauthorized data exposure or loss.",
    "Default Behavior / Limitations": "FULL_CONTROL can be granted via ACLs; caution must be taken to avoid unintended access.",
    "Automation": "Use AWS Config rule `s3-bucket-acl-prohibited` to prevent FULL_CONTROL access.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/S3/s3-bucket-authenticated-users-full-control-access.html"
    ]
  },
  {
    "Title": "Enable Access Logging for S3 Buckets",
    "Description": "Ensure S3 bucket access logging is enabled to maintain an audit trail of access requests.",
    "Applicability": "All S3 buckets in AWS accounts",
    "Security Risk": "Lack of logs can impair the ability to detect unauthorized access or investigate security incidents.",
    "Default Behavior / Limitations": "Access logging is disabled by default and must be explicitly enabled.",
    "Automation": "AWS Config rule `s3-bucket-logging-enabled` can be used to enforce this control.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/S3/s3-bucket-logging-enabled.html"
    ]
  },
  {
    "Title": "Enforce MFA-Delete on S3 Buckets",
    "Description": "Ensure S3 buckets enable MFA-Delete to protect against accidental or malicious deletion of objects.",
    "Applicability": "Sensitive S3 buckets where data integrity is critical",
    "Security Risk": "Without MFA-Delete, objects can be deleted without additional verification, increasing the risk of accidental or intentional data loss.",
    "Default Behavior / Limitations": "MFA-Delete is not enabled by default and must be configured.",
    "Automation": "Requires manual intervention to configure and enforce MFA; no native AWS Config rule exists.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/S3/s3-bucket-mfa-delete-enabled.html"
    ]
  },
  {
    "Title": "Prevent Public Access in S3 Bucket Policies",
    "Description": "Ensure that S3 bucket policies are configured to disallow public access.",
    "Applicability": "All S3 buckets",
    "Security Risk": "Publicly accessible bucket policies can expose data to unintended users, leading to data breaches.",
    "Default Behavior / Limitations": "Bucket policies do not prevent public access by default; must be configured explicitly.",
    "Automation": "AWS Config rule `s3-bucket-policy-not-more-public` can be used to audit policy settings.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/S3/s3-bucket-public-access-via-policy.html"
    ]
  },
  {
    "Title": "Enforce SSL for S3 Bucket Access",
    "Description": "Ensure AWS S3 buckets enforce SSL to secure data in transit.",
    "Applicability": "All S3 buckets transmitting sensitive data",
    "Security Risk": "Without SSL, data in transit can be intercepted, compromising confidentiality and integrity.",
    "Default Behavior / Limitations": "SSL is not enforced by default for S3 communications; must be configured via bucket policy.",
    "Automation": "AWS Config rule `s3-bucket-ssl-requests-only` to enforce SSL-only access.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/S3/secure-transport.html"
    ]
  },
  {
    "Title": "Enforce Server-Side Encryption (SSE) on S3 Buckets",
    "Description": "Ensure AWS S3 buckets enforce Server-Side Encryption (SSE) to protect data at rest.",
    "Applicability": "All S3 buckets storing sensitive data",
    "Security Risk": "Without encryption, data stored in S3 may be susceptible to unauthorized access.",
    "Default Behavior / Limitations": "SSE is not enabled by default; must be configured on a per-bucket basis.",
    "Automation": "AWS Config rule `s3-bucket-server-side-encryption-enabled` to automatically enforce SSE.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/S3/server-side-encryption.html"
    ]
  },
  {
    "Title": "Utilize Lifecycle Configurations for S3 Buckets",
    "Description": "Ensure S3 buckets have lifecycle configurations to automate storage management and cost reduction.",
    "Applicability": "All S3 buckets with large or archival data sets",
    "Security Risk": "Without lifecycle policies, unnecessary data may remain, increasing storage costs and risk exposure.",
    "Default Behavior / Limitations": "Lifecycle management must be set up manually for each bucket.",
    "Automation": "Monitoring and auditing via AWS Config but requires manual configuration.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/S3/lifecycle-configuration.html"
    ]
  },
  {
    "Title": "Prohibit Unknown Cross-Account Access via S3 Bucket Policies",
    "Description": "Ensure that S3 buckets do not allow cross-account access via bucket policies unless explicitly validated.",
    "Applicability": "All S3 buckets with cross-account permissions",
    "Security Risk": "Cross-account access can lead to unauthorized data exposure.",
    "Default Behavior / Limitations": "Cross-account permissions can be easily configured and misunderstood, leading to unintentional exposure.",
    "Automation": "Use AWS Config rule `s3-bucket-policy-not-more-public` to detect cross-account policies.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/S3/s3-cross-account-access.html"
    ]
  },
  {
    "Title": "Deny Log Delivery Group Write Permissions to S3 Source Buckets",
    "Description": "Ensure that S3 Log Delivery Group write permissions are denied for the S3 source bucket to prevent unauthorized data modifications.",
    "Applicability": "All S3 buckets intended for logging",
    "Security Risk": "Uncontrolled write access can lead to log manipulation or data corruption.",
    "Default Behavior / Limitations": "IAM policies and bucket ACLs must be carefully crafted to deny write access.",
    "Automation": "Audit using AWS Config to ensure IAM policies deny such permissions.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/S3/deny-log-delivery-group-write-permission.html"
    ]
  }
]
```