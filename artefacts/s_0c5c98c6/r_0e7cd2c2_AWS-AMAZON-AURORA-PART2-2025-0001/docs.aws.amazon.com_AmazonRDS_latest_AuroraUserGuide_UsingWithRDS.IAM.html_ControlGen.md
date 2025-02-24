```json
[
  {
    "Title": "Enforce Multi-Factor Authentication (MFA) for AWS Accounts",
    "Description": "All AWS accounts must have MFA enabled for additional security. Use AWS IAM policies to enforce MFA for console access.",
    "Applicability": "All AWS accounts and IAM users",
    "Security Risk": "Without MFA, accounts are vulnerable to unauthorized access, data breaches, and privilege escalation.",
    "Default Behavior / Limitations": "AWS IAM does not enforce MFA by default and requires manual configuration.",
    "Automation": "Monitor and enforce using AWS Config rule `iam-user-mfa-enabled`. Validate with AWS Security Hub.",
    "References": [
      "https://docs.aws.amazon.com/singlesignon/latest/userguide/enable-mfa.html"
    ]
  },
  {
    "Title": "Regular Rotation of IAM User Access Keys",
    "Description": "Set up an automated schedule for rotating IAM user access keys to reduce exposure risk of compromised keys.",
    "Applicability": "All IAM users with long-term credentials",
    "Security Risk": "Stale or compromised access keys can lead to unauthorized access and potential breaches.",
    "Default Behavior / Limitations": "AWS does not automatically rotate access keys.",
    "Automation": "Automate using AWS IAM Access Analyzer for access key age monitoring. Enforce action with AWS Lambda to rotate keys periodically.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#rotate-credentials"
    ]
  },
  {
    "Title": "Attach IAM Policies to Control Access Permissions",
    "Description": "Ensure IAM policies are effectively attached to identities or resources to grant necessary permissions only.",
    "Applicability": "All IAM identities and resources",
    "Security Risk": "Excessive permissions can lead to misuse or breaches of sensitive data.",
    "Default Behavior / Limitations": "IAM policy attachments must be manually configured.",
    "Automation": "Use AWS Config and AWS IAM Access Analyzer to audit permissions regularly.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json"
    ]
  },
  {
    "Title": "Use IAM Roles for EC2 Instances",
    "Description": "Assign IAM roles to EC2 instances to provide temporary credentials instead of embedding access keys directly in the configuration.",
    "Applicability": "All Amazon EC2 instances",
    "Security Risk": "Hard-coded access keys can be exposed through instance compromise, leading to unauthorized API calls.",
    "Default Behavior / Limitations": "IAM roles must be manually attached via instance profiles.",
    "Automation": "Monitor using AWS Config rule `ec2-instance-profile-attached`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html"
    ]
  },
  {
    "Title": "Centralized Access Management with AWS Identity Center",
    "Description": "Leverage AWS Identity Center for centralized access control to streamline identity management across AWS accounts and applications.",
    "Applicability": "Organizations using multiple AWS accounts",
    "Security Risk": "Decentralized identity management can lead to inconsistency in access permissions and increased security risks.",
    "Default Behavior / Limitations": "Requires setup and maintenance of synchronization configurations manually.",
    "Automation": "Use AWS Single Sign-On (SSO) to automate user access provisioning.",
    "References": [
      "https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html"
    ]
  },
  {
    "Title": "Set Permissions Boundaries for IAM Entities",
    "Description": "Implement permissions boundaries to restrict the maximum permissions that can be granted to IAM users and roles.",
    "Applicability": "IAM roles and users with sensitive permissions",
    "Security Risk": "Overprivileged users or roles may lead to unauthorized access to critical resources.",
    "Default Behavior / Limitations": "Permissions boundaries need to be defined and associated manually.",
    "Automation": "Audit using AWS Config and IAM Access Analyzer to ensure compliance.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html"
    ]
  },
  {
    "Title": "Restrict Use of AWS Root User",
    "Description": "Limit the tasks performed by the AWS root user and avoid its use for regular operations. Monitor root user activity for any anomalous access.",
    "Applicability": "All AWS accounts",
    "Security Risk": "The root user has unrestricted access, making its credentials a critical target for attackers.",
    "Default Behavior / Limitations": "Root user restrictions are not enforced by AWS by default.",
    "Automation": "Track root user actions using AWS CloudTrail and notify via AWS Security Hub for anomalous usage.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks"
    ]
  }
]
```