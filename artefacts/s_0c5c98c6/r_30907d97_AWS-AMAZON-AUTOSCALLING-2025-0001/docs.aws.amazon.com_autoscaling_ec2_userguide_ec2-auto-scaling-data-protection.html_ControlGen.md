```json
[
  {
    "Title": "Enable Multi-Factor Authentication (MFA) for AWS Accounts",
    "Description": "Ensure that multi-factor authentication (MFA) is enabled on the root account and for all IAM users with console access to strengthen access security.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without MFA, unauthorized access through compromised credentials can lead to data breaches and unauthorized changes to AWS resources.",
    "Default Behavior / Limitations": "AWS does not enforce MFA by default. It requires manual activation.",
    "Automation": "MFA can be enforced by using AWS IAM policies and AWS Config rule `iam-user-mfa-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html",
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-data-protection.html"
    ]
  },
  {
    "Title": "Require TLS 1.2 or Higher for AWS Resource Communication",
    "Description": "Ensure all communication with AWS resources uses TLS 1.2 or higher to maintain data security during transit.",
    "Applicability": "All communication endpoints",
    "Security Risk": "Using older TLS versions can expose data to interception and attacks due to known vulnerabilities.",
    "Default Behavior / Limitations": "AWS services typically support TLS 1.2 by default, but verification is advisable.",
    "Automation": "Verification can be automated using AWS Config custom rules to check for allowed SSL/TLS protocols.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-data-protection.html"
    ]
  },
  {
    "Title": "Enable AWS CloudTrail for API and User Activity Logging",
    "Description": "Configure AWS CloudTrail to capture API calls and user activity across all regions for auditing and compliance.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without logging, malicious or accidental changes could go undetected, impeding incident response.",
    "Default Behavior / Limitations": "AWS CloudTrail is not enabled by default for all accounts or regions.",
    "Automation": "Can be enabled using AWS CLI or Console. Compliance can be checked with AWS Config rule `cloud-trail-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html"
    ]
  },
  {
    "Title": "Encrypt Amazon EBS Volumes Using AWS KMS Keys",
    "Description": "Use AWS KMS keys to encrypt Amazon EBS volumes to protect data at rest.",
    "Applicability": "All Amazon EBS volumes",
    "Security Risk": "Unencrypted EBS volumes may expose sensitive data if accessed by unauthorized users.",
    "Default Behavior / Limitations": "AWS supports encryption, but it is not enabled by default.",
    "Automation": "Can be enforced using AWS Config rule `ebs-volumes-encrypted`.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-data-protection.html"
    ]
  },
  {
    "Title": "Utilize Launch Templates for EBS Encryption with Customer Managed Keys",
    "Description": "Use a launch template to specify a customer managed KMS key for encrypting Amazon EBS volumes.",
    "Applicability": "All EC2 Launch Templates",
    "Security Risk": "Failing to specify a customer managed key can lead to less control over encryption key policies.",
    "Default Behavior / Limitations": "Launch configurations do not support customer managed keys.",
    "Automation": "Can be specified in EC2 Launch Templates via AWS Console or CLI.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-data-protection.html"
    ]
  },
  {
    "Title": "Enforce Encryption by Default for New EBS Volumes and Snapshots",
    "Description": "Enable encryption by default for new EBS volumes and snapshots to ensure data protection automatically upon creation.",
    "Applicability": "All EBS volumes and snapshots",
    "Security Risk": "Without automatic encryption, data may be inadvertently stored unencrypted.",
    "Default Behavior / Limitations": "AWS allows configuring regions to encrypt volumes by default.",
    "Automation": "Can be monitored using AWS Config rule `encrypted-volumes`.",
    "References": [
      "https://docs.aws.amazon.com/ebs/latest/userguide/encryption-by-default.html"
    ]
  },
  {
    "Title": "Avoid Sensitive Information in Tags and Free-Form Fields",
    "Description": "Prevent placing sensitive data like customer emails in tags or free-form text fields to avoid data leakage through logs or API responses.",
    "Applicability": "All AWS resources utilizing tags",
    "Security Risk": "Sensitive information may be unintentionally exposed to unauthorized access.",
    "Default Behavior / Limitations": "This requires manual adherence as AWS does not restrict tag content.",
    "Automation": "Manual validation required; tools like tag policies can help enforce tagging conventions.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-data-protection.html"
    ]
  },
  {
    "Title": "Use FIPS 140-3 Validated Cryptographic Modules",
    "Description": "Access AWS services through CLI or APIs using FIPS endpoints to ensure cryptographic module compliance with FIPS 140-3.",
    "Applicability": "All AWS CLI and API users requiring compliance",
    "Security Risk": "Non-compliance with FIPS standards can result in using weaker cryptographic protections, potentially leading to data compromise.",
    "Default Behavior / Limitations": "FIPS endpoints need to be explicitly specified by users.",
    "Automation": "Manual configuration required; guide users to configure their AWS CLI and SDKs to use FIPS endpoints.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-data-protection.html"
    ]
  }
]
```