### ControlGen Output - Arquivo 1
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

### ControlGen Output - Arquivo 2
```json
[
  {
    "Title": "Disable Access Control Lists (ACLs) on Amazon S3 Buckets",
    "Description": "Configure S3 buckets to disable ACLs and use IAM policies to manage access. This provides unified access management through AWS Identity and Access Management (IAM).",
    "Applicability": "All S3 buckets in all AWS accounts",
    "Security Risk": "Using ACLs may lead to permission misconfigurations and unauthorized access to S3 buckets.",
    "Default Behavior / Limitations": "ACLs are disabled by default for new S3 buckets.",
    "Automation": "Can be monitored using AWS Config rule `s3-bucket-acl-prohibited`.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html"
    ]
  },
  {
    "Title": "Block Public Access to Amazon S3 Buckets",
    "Description": "Enable S3 Block Public Access to ensure no public access to buckets or objects. Audit bucket policies and ACLs to verify compliance.",
    "Applicability": "All S3 buckets in all AWS accounts",
    "Security Risk": "Publicly accessible buckets may lead to data breaches and unauthorized data exposure.",
    "Default Behavior / Limitations": "S3 Block Public Access settings must be manually enabled.",
    "Automation": "Can be enforced using AWS Config rules `s3-bucket-public-read-prohibited` and `s3-bucket-public-write-prohibited`.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html"
    ]
  },
  {
    "Title": "Implement Least Privilege Access for Amazon S3",
    "Description": "Use IAM policies to grant the minimal level of access necessary for users and services to perform their tasks on S3 resources.",
    "Applicability": "All S3 buckets and IAM roles in all AWS accounts",
    "Security Risk": "Excessive permissions can lead to unauthorized data access and compromise data integrity.",
    "Default Behavior / Limitations": "Requires manual policy review and adjustments.",
    "Automation": "Can be audited using IAM Access Analyzer to verify least privilege adherence.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html"
    ]
  },
  {
    "Title": "Use IAM Roles for Amazon S3 Access",
    "Description": "Configure IAM roles for applications and services that access S3 to avoid using long-term credentials, leveraging temporary security credentials.",
    "Applicability": "All applications and services accessing S3",
    "Security Risk": "Long-term credentials are at higher risk of being compromised, leading to unauthorized access.",
    "Default Behavior / Limitations": "IAM roles must be properly managed and assigned.",
    "Automation": "Use IAM best practices for role management.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html"
    ]
  },
  {
    "Title": "Ensure Encryption of Data at Rest in Amazon S3",
    "Description": "Enable server-side encryption (SSE-S3, SSE-KMS, DSSE-KMS, or SSE-C) for S3 buckets to secure data at rest.",
    "Applicability": "All S3 buckets in all AWS accounts",
    "Security Risk": "Data stored without encryption is vulnerable to unauthorized access and data breaches.",
    "Default Behavior / Limitations": "SSE-S3 is enabled by default for new bucket objects unless specified otherwise.",
    "Automation": "Can be enforced using AWS Config rule `s3-bucket-server-side-encryption-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html"
    ]
  },
  {
    "Title": "Enforce HTTPS for Amazon S3 Data in Transit",
    "Description": "Apply the `aws:SecureTransport` condition in bucket policies to ensure that data is only transmitted over HTTPS.",
    "Applicability": "All S3 buckets in all AWS accounts",
    "Security Risk": "Unencrypted data in transit can be intercepted or modified, compromising data integrity and confidentiality.",
    "Default Behavior / Limitations": "Encryption in transit must be enabled via policies.",
    "Automation": "Monitor HTTP access attempts with CloudWatch alarms.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html"
    ]
  },
  {
    "Title": "Enable S3 Object Lock for Data Protection",
    "Description": "Implement S3 Object Lock to protect objects against accidental or intentional deletion using a Write Once Read Many (WORM) model.",
    "Applicability": "Buckets storing immutable data such as legal or compliance logs",
    "Security Risk": "Without object lock, critical data can be altered or deleted, compromising data integrity.",
    "Default Behavior / Limitations": "Object lock must be configured explicitly.",
    "Automation": "Requires configuration through S3 API or console.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html"
    ]
  },
  {
    "Title": "Enable S3 Versioning for Object Variants",
    "Description": "Enable versioning on S3 buckets to maintain and manage multiple versions of objects to protect against accidental deletion.",
    "Applicability": "All S3 buckets in all AWS accounts",
    "Security Risk": "Without versioning, object loss or accidental overwrites can result in data loss.",
    "Default Behavior / Limitations": "Versioning is not enabled by default and must be activated.",
    "Automation": "Can be enforced using AWS Config rule `s3-bucket-versioning-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html"
    ]
  },
  {
    "Title": "Implement S3 Cross-Region Replication",
    "Description": "Utilize S3 Cross-Region Replication to replicate objects across different AWS regions for compliance and redundancy.",
    "Applicability": "S3 buckets with cross-regional compliance requirements",
    "Security Risk": "Without replication, data may not be compliant with regional data handling requirements.",
    "Default Behavior / Limitations": "Versioning must be enabled on both source and destination buckets.",
    "Automation": "Requires configuration via S3 API or console.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html"
    ]
  },
  {
    "Title": "Use VPC Endpoints for S3 Access",
    "Description": "Configure VPC endpoints for private connectivity to S3, ensuring that network traffic does not traverse the internet.",
    "Applicability": "All S3 access within VPC environments",
    "Security Risk": "Without VPC endpoints, data in transit could be exposed to eavesdropping over public networks.",
    "Default Behavior / Limitations": "VPC endpoints must be explicitly set up for private access.",
    "Automation": "Requires configuration through VPC and S3 settings.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html"
    ]
  },
  {
    "Title": "Leverage Managed Security Services",
    "Description": "Integrate and use AWS managed services like GuardDuty, Detective, IAM Access Analyzer, and AWS Security Hub to monitor and enhance data security for S3.",
    "Applicability": "All AWS accounts and regions with S3 usage",
    "Security Risk": "Without adequate monitoring, security incidents may go unnoticed leading to data breaches.",
    "Default Behavior / Limitations": "Additional configuration may be required to tune and integrate these services into existing systems.",
    "Automation": "Integrates with AWS Security services and can feed data into SIEMs.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html"
    ]
  },
  {
    "Title": "Enable AWS CloudTrail for Amazon S3",
    "Description": "Activate CloudTrail to log API calls to S3, capturing both management and data events. This facilitates auditing and forensic analysis.",
    "Applicability": "All AWS accounts where S3 is deployed",
    "Security Risk": "Without detailed logging, unauthorized actions may go undetected, hampering incident response efforts.",
    "Default Behavior / Limitations": "CloudTrail must be manually enabled and configured for S3 data events.",
    "Automation": "Enforced via AWS Config rule `cloudtrail-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html"
    ]
  },
  {
    "Title": "Implement AWS Config Resource Monitoring",
    "Description": "Use AWS Config to continuously monitor and assess the configurations of S3 resources for compliance.",
    "Applicability": "All S3 buckets in AWS accounts utilizing AWS Config",
    "Security Risk": "Without consistent monitoring, non-compliant changes may go unnoticed, increasing security risks.",
    "Default Behavior / Limitations": "AWS Config must be enabled and properly configured to include S3.",
    "Automation": "Supports continuous compliance checks using AWS Config rules.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html"
    ]
  },
  {
    "Title": "Utilize Amazon S3 Inventory and Tag Editor",
    "Description": "Implement S3 Inventory to audit object replication and encryption status, leveraging Tag Editor for enhanced reporting.",
    "Applicability": "S3 buckets requiring detailed compliance and inventory checks",
    "Security Risk": "Without proper auditing, non-encrypted or non-compliant objects may remain undetected.",
    "Default Behavior / Limitations": "Requires explicit setup for reporting and auditing tasks.",
    "Automation": "Requires configuration and utilization of S3 Inventory jobs.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html"
    ]
  },
  {
    "Title": "Enable Amazon S3 Server Access Logging",
    "Description": "Activate server access logging for S3 buckets to maintain a detailed record of requests made to the bucket.",
    "Applicability": "S3 buckets where access tracking is required",
    "Security Risk": "Without access logs, unauthorized access may not be tracked effectively, hindering security investigations.",
    "Default Behavior / Limitations": "Server access logging must be manually enabled for each bucket.",
    "Automation": "Enforced via AWS Config rule `s3-bucket-logging-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 3
```json
[
  {
    "Title": "Implement Least Privilege Access for S3 Buckets Using IAM",
    "Description": "IAM policies must grant the least privilege necessary for S3 bucket operations. Resource-based policies should restrict access to specific IP ranges or VPCs. Access control lists (ACLs) should be avoided or minimized.",
    "Applicability": "All AWS accounts using S3",
    "Security Risk": "Overly permissive access could lead to unauthorized data exposure or modification.",
    "Default Behavior / Limitations": "IAM provides tools for implementing policies, but configuration requires user input.",
    "Automation": "Monitor IAM policies and access patterns using AWS Config rules, and audit with AWS Security Hub.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html",
      "https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html"
    ]
  },
  {
    "Title": "Ensure S3 Buckets Are Not Publicly Accessible",
    "Description": "Enable S3 Block Public Access on all buckets to prevent public exposure. Evaluate permissions regularly and use pre-signed or CloudFront signed URLs for controlled access.",
    "Applicability": "All S3 buckets",
    "Security Risk": "Publicly accessible buckets can lead to data leaks and unauthorized access.",
    "Default Behavior / Limitations": "Block Public Access must be configured manually per bucket or account.",
    "Automation": "Automate detection using AWS Config rule `s3-bucket-public-read-prohibited`.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html"
    ]
  },
  {
    "Title": "Enable Access Logging for S3 Buckets",
    "Description": "Configure S3 server access logging to store logs in a separate, restricted-access S3 bucket. Ensure logs are secured and monitored for integrity and anomalies.",
    "Applicability": "All S3 buckets where logging is required",
    "Security Risk": "Without logging, unauthorized access may go undetected, hindering incident response.",
    "Default Behavior / Limitations": "Logging must be manually enabled and configured.",
    "Automation": "AWS CloudTrail and AWS Config can monitor logging status, and Amazon GuardDuty can be used for anomaly detection.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerLogs.html"
    ]
  },
  {
    "Title": "Enforce S3 Bucket Versioning and MFA Delete",
    "Description": "Enable versioning on all S3 buckets and configure MFA delete for critical data. Use lifecycle policies to manage outdated versions.",
    "Applicability": "All critical S3 buckets",
    "Security Risk": "Without versioning, accidental or unauthorized data deletions cannot be easily recovered.",
    "Default Behavior / Limitations": "Versioning and MFA delete require manual configuration.",
    "Automation": "AWS Config can monitor versioning status. MFA policies must be manually enforced.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html",
      "https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMFADelete.html"
    ]
  },
  {
    "Title": "Enable Default Encryption for S3 Buckets Using SSE-KMS",
    "Description": "Configure S3 buckets to use server-side encryption with AWS KMS-managed keys (SSE-KMS) for all objects.",
    "Applicability": "All S3 buckets containing sensitive data",
    "Security Risk": "Without encryption, sensitive data is vulnerable if accessed by unauthorized users.",
    "Default Behavior / Limitations": "Encryption settings must be manually configured per bucket.",
    "Automation": "AWS Config rule `s3-bucket-server-side-encryption-enabled` can ensure compliance.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html"
    ]
  },
  {
    "Title": "Automated Alerting for Unauthorized Access or Changes in S3",
    "Description": "Use Amazon Macie to detect data access anomalies and alert on unauthorized bucket access or configuration changes.",
    "Applicability": "All AWS accounts using S3",
    "Security Risk": "Without real-time alerting, unauthorized access might remain undetected.",
    "Default Behavior / Limitations": "Alert configurations must be manually set up.",
    "Automation": "Amazon Macie and AWS Security Hub can facilitate detection and alerting.",
    "References": [
      "https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html"
    ]
  },
  {
    "Title": "Regular Review and Update of S3 ACLs and Bucket Policies",
    "Description": "Periodically review S3 ACLs and policies to eliminate public-read and public-read-write permissions, using conditions like MFA or IP address restrictions where needed.",
    "Applicability": "All S3 buckets",
    "Security Risk": "Outdated or misconfigured policies could lead to unintentional exposures.",
    "Default Behavior / Limitations": "Review process is typically manual but scripting and automation tools can assist.",
    "Automation": "AWS Config and AWS Security Hub for monitoring and reporting policy compliance.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/dev/access-policy-alternatives-guidelines.html"
    ]
  },
  {
    "Title": "Centralize S3 Security Settings Across Multiple Accounts",
    "Description": "Use AWS Organizations to centralize security settings and enforce policies across accounts with Service Control Policies (SCPs).",
    "Applicability": "Organizations using multiple AWS accounts",
    "Security Risk": "Without centralized control, inconsistencies may lead to security gaps.",
    "Default Behavior / Limitations": "Requires setup and management within AWS Organizations.",
    "Automation": "AWS Organizations and SCPs automate policy enforcement across accounts.",
    "References": [
      "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html"
    ]
  },
  {
    "Title": "Implement Cross-Region Replication and Backups for S3",
    "Description": "Set up cross-region replication for critical S3 data as a disaster recovery measure. Regularly test backup and recovery procedures.",
    "Applicability": "S3 buckets containing critical data",
    "Security Risk": "Data loss or unavailability during disasters without adequate backups.",
    "Default Behavior / Limitations": "Replication and backups require manual configuration.",
    "Automation": "AWS Backup and S3 CRR (Cross-Region Replication) can automate this process.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/dev/crr.html",
      "https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html"
    ]
  },
  {
    "Title": "Tag S3 Objects for Data Sensitivity and Implement Lifecycle Policies",
    "Description": "Assign metadata tags to S3 objects to classify data sensitivity levels. Use lifecycle policies to automate data management processes such as deletions.",
    "Applicability": "All S3 buckets containing classified data",
    "Security Risk": "Improper data classification can lead to exposed sensitive information.",
    "Default Behavior / Limitations": "Tags and lifecycle policies need to be defined and applied.",
    "Automation": "AWS Config and AWS Lambda can assist in tagging and lifecycle policy management.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/dev/object-tagging.html",
      "https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html"
    ]
  }
]
```