```json
[
  {
    "Title": "Enforce Multi-Factor Authentication (MFA) for Root and IAM Users",
    "Description": "Ensure multi-factor authentication is configured for both the AWS account root user and all IAM users. This can be enforced by setting up MFA for users via IAM and applying policies that restrict console access unless MFA is used.",
    "Applicability": "All AWS accounts and IAM users",
    "Security Risk": "Without MFA, stolen credentials can lead to unauthorized access, resulting in potential data breaches or privilege escalation.",
    "Default Behavior / Limitations": "AWS does not enforce MFA by default; it needs to be configured for each user.",
    "Automation": "Enforced using IAM policies and monitored through AWS Config rule `iam-user-mfa-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html"
    ]
  },
  {
    "Title": "Rotate IAM User Access Keys Every 90 Days",
    "Description": "Implement a policy to ensure that IAM user access keys are rotated at least every 90 days. Use AWS Config to monitor and alert if keys become non-compliant with this lifecycle policy.",
    "Applicability": "IAM users with long-term credentials",
    "Security Risk": "Stale access keys increase the risk of exposure and unauthorized access if compromised.",
    "Default Behavior / Limitations": "AWS does not automatically rotate access keys; users need to rotate keys manually.",
    "Automation": "Monitored using AWS Config rule `access-keys-rotated`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#rotate-credentials"
    ]
  },
  {
    "Title": "Utilize IAM Roles for Applications on EC2 Instances",
    "Description": "Ensure applications running on EC2 instances use IAM roles for access management instead of embedding credentials. This involves assigning the appropriate role to each EC2 instance upon launch.",
    "Applicability": "All EC2 instances",
    "Security Risk": "Hardcoding credentials increases the risk of credential leakage and complicates management.",
    "Default Behavior / Limitations": "Requires proper configuration of IAM roles and EC2 instance profiles.",
    "Automation": "Enforced by assigning IAM roles to EC2 instances via AWS Management Console or CLI.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html"
    ]
  },
  {
    "Title": "Grant Least Privilege with IAM Policies",
    "Description": "Configure IAM policies to grant only the permissions necessary to perform a user's required tasks, adhering to the principle of least privilege. Regular reviews should be scheduled to maintain this principle.",
    "Applicability": "All IAM users and roles",
    "Security Risk": "Excessive permissions can lead to unintentional data exposure or misuse of resources.",
    "Default Behavior / Limitations": "IAM policies require manual creation and updates to reflect least privilege.",
    "Automation": "Policies can be validated using AWS IAM Access Analyzer.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json"
    ]
  },
  {
    "Title": "Implement Federated Access Using IAM Roles",
    "Description": "Use IAM roles to enable federated access for users from external identity providers, ensuring roles are configured with appropriate permissions.",
    "Applicability": "Federated users accessing AWS resources",
    "Security Risk": "Improperly configured federation can result in unauthorized access.",
    "Default Behavior / Limitations": "Roles need correct configuration and federated access setup using AWS IAM or AWS IAM Identity Center.",
    "Automation": "Management through AWS IAM Identity Center or AWS Management Console.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html"
    ]
  },
  {
    "Title": "Use AWS STS for Temporary IAM Credentials",
    "Description": "Deploy AWS Security Token Service (STS) to generate temporary, limited-privilege credentials for applications, ensuring token expiration aligns with organizational security policies.",
    "Applicability": "All applications requiring temporary access",
    "Security Risk": "Compromised long-lived credentials can lead to unauthorized access.",
    "Default Behavior / Limitations": "Requires applications to support token-based authentication.",
    "Automation": "Credentials can be generated programmatically via AWS SDKs or CLI.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temporary.html"
    ]
  },
  {
    "Title": "Manage Cross-Account Access Using IAM Roles",
    "Description": "Establish IAM roles for cross-account access, ensuring permissions granted are restricted to necessary actions for trusted accounts only.",
    "Applicability": "Accounts requiring shared resource access",
    "Security Risk": "Inappropriate permissions increase risk of data breach across accounts.",
    "Default Behavior / Limitations": "Cross-account role establishment requires mutual trust setup.",
    "Automation": "Configured using IAM role trust policies and monitored with AWS Config.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_cross-account.html"
    ]
  },
  {
    "Title": "Apply Permissions Boundaries to IAM Entities",
    "Description": "Implement permissions boundaries to define maximum allowable permissions for users or roles, aligning these boundaries with organizational security policies.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without boundaries, privilege escalation could lead to unauthorized actions.",
    "Default Behavior / Limitations": "Policies must be correctly configured and attached to IAM entities.",
    "Automation": "Permissions boundaries can be managed through IAM policy configurations.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html"
    ]
  },
  {
    "Title": "Enforce Organization-Wide Security with SCPs",
    "Description": "Utilize AWS Organizations to manage Service Control Policies (SCPs) across all member accounts, enforcing minimum security standards and restrictions.",
    "Applicability": "All accounts within an AWS Organization",
    "Security Risk": "Without SCPs, individual accounts may exceed designated permissions, leading to potential security vulnerabilities.",
    "Default Behavior / Limitations": "Requires AWS Organizations and policies need periodic review.",
    "Automation": "Monitored and enforced through AWS Organizations.",
    "References": [
      "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html"
    ]
  }
]
```