```json
[
  {
    "Title": "Ensure Encryption of Amazon Aurora DB Clusters with AES-256",
    "Description": "Amazon Aurora DB clusters must be encrypted using AES-256 encryption to secure data at rest, including automated backups, read replicas, and snapshots.",
    "Applicability": "All Amazon Aurora DB clusters",
    "Security Risk": "Without encryption, sensitive data may be exposed if accessed by unauthorized users, resulting in data breaches and compliance violations.",
    "Default Behavior / Limitations": "Encryption must be enabled at the creation of the DB cluster and cannot be changed afterwards.",
    "Automation": "Can be verified using AWS Config rule `rds-instance-encrypted` to ensure that all DB clusters have encryption enabled.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html"
    ]
  },
  {
    "Title": "Manage Encryption Keys with AWS KMS for Amazon Aurora",
    "Description": "Utilize AWS Key Management Service (KMS) to manage the encryption keys used for decrypting Amazon Aurora resources. Both AWS-managed keys and customer-managed keys are supported.",
    "Applicability": "All Amazon Aurora DB clusters",
    "Security Risk": "Improper management of encryption keys can lead to unauthorized data access and potential data loss.",
    "Default Behavior / Limitations": "Once a DB instance is encrypted, the associated KMS key cannot be changed.",
    "Automation": "Can be configured through AWS CloudFormation or manually via AWS Management Console when creating the cluster.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html"
    ]
  },
  {
    "Title": "Enable Encryption for New Amazon Aurora DB Clusters",
    "Description": "Ensure that encryption is enabled when creating a new Amazon Aurora DB cluster by setting the --storage-encrypted parameter to true using the AWS CLI.",
    "Applicability": "All new Amazon Aurora DB clusters",
    "Security Risk": "If encryption is not enabled at the creation of the DB cluster, data may be vulnerable to unauthorized access.",
    "Default Behavior / Limitations": "Encryption settings cannot be modified after the DB cluster is created.",
    "Automation": "Ensure compliance via AWS Config rule `rds-instance-encrypted` for newly created clusters.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html"
    ]
  },
  {
    "Title": "Verify Encryption at Rest for Amazon Aurora DB Clusters",
    "Description": "Periodically check that encryption at rest is enabled on Amazon Aurora DB clusters using AWS Management Console, AWS CLI, or RDS API.",
    "Applicability": "All Amazon Aurora DB clusters",
    "Security Risk": "Failure to verify encryption status can result in unencrypted data exposure.",
    "Default Behavior / Limitations": "Manual validation may be required if automation is not feasible.",
    "Automation": "Use AWS Config rule `rds-instance-encrypted` to continuously monitor the encryption status.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html"
    ]
  },
  {
    "Title": "Use Envelope Encryption for Cross-Region Snapshot Copies",
    "Description": "Protect Amazon Aurora snapshots during cross-region copies using envelope encryption. Specify a KMS key in the destination AWS Region.",
    "Applicability": "All cross-region snapshot operations",
    "Security Risk": "Without proper encryption, data may be compromised during transfer between regions.",
    "Default Behavior / Limitations": "KMS keys are region-specific and cannot be reused across different regions.",
    "Automation": "Configure automatic KMS key usage for cross-region copying via AWS Lambda or AWS SDK scripts.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html"
    ]
  },
  {
    "Title": "Leverage Automatic Encryption for Cross-Region Data Traffic",
    "Description": "Utilize the automatic encryption provided at the physical layer for cross-region data traffic within the AWS global network and between AZs.",
    "Applicability": "All cross-region data transfers",
    "Security Risk": "Unencrypted data in transit could be intercepted, compromising confidentiality and integrity.",
    "Default Behavior / Limitations": "Encryption is provided automatically by AWS and cannot be configured.",
    "Automation": "No specific automation is required as AWS secures this by default.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html"
    ]
  },
  {
    "Title": "Ensure Cross-Account KMS Key Sharing for Operations",
    "Description": "When using cross-account KMS keys, ensure that the necessary account permissions are set to allow operations like snapshot copying.",
    "Applicability": "Cross-account operations involving KMS keys",
    "Security Risk": "Failure to share keys can prevent important operations, while improper permissions may expose keys to unauthorized users.",
    "Default Behavior / Limitations": "Revoking key access does not impact existing clusters, but disabling the key will affect all operations.",
    "Automation": "Use AWS IAM policies to manage cross-account key permissions effectively.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html"
    ]
  }
]
```