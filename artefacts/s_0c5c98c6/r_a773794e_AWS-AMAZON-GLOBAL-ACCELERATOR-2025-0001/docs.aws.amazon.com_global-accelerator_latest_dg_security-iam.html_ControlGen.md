```json
[
  {
    "Title": "Enforce Multi-Factor Authentication (MFA) for Sign-In",
    "Description": "All IAM users and root accounts must have multi-factor authentication enabled to enhance security during the sign-in process.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without MFA, credentials can be easily compromised, leading to unauthorized account access and potential data breaches.",
    "Default Behavior / Limitations": "AWS does not enforce MFA by default for accounts. Manual configuration is required.",
    "Automation": "Can be enforced using AWS IAM policies and monitored using AWS Config rules `iam-user-mfa-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html"
    ]
  },
  {
    "Title": "Centralized Access Management with AWS IAM Identity Center",
    "Description": "Configure AWS IAM Identity Center to centralize user access management and synchronize with the organization's identity provider.",
    "Applicability": "All organizations using AWS IAM Identity Center",
    "Security Risk": "Failure to centralize access can lead to inconsistent permission management and potential security gaps.",
    "Default Behavior / Limitations": "IAM Identity Center setup depends on the integration with external identity providers.",
    "Automation": "Requires manual integration setup but can be monitored via AWS IAM Identity Center logging capabilities.",
    "References": [
      "https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html"
    ]
  },
  {
    "Title": "Regular Access Key Rotation",
    "Description": "Implement policies to rotate IAM user access keys regularly to minimize the risk of credential exposure.",
    "Applicability": "All IAM users with long-term credentials",
    "Security Risk": "Stale access keys increase the risk of unauthorized access if the keys are compromised.",
    "Default Behavior / Limitations": "AWS does not automatically enforce access key rotation.",
    "Automation": "Can be managed with AWS Secrets Manager or AWS Config rule `access-keys-rotated`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey"
    ]
  },
  {
    "Title": "Use IAM Roles for Federated User Access",
    "Description": "Create and configure IAM roles for federated users to allow access using temporary credentials.",
    "Applicability": "Organizations using federated authentications",
    "Security Risk": "Permanent credentials increase exposure compared to temporary credentials which have limited lifespan.",
    "Default Behavior / Limitations": "AWS supports federated authentication but setup and configuration are required.",
    "Automation": "Automate role creation and policies through CloudFormation or Terraform.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html"
    ]
  },
  {
    "Title": "Implement Service-Linked Roles for AWS Services",
    "Description": "Configure service-linked roles to allow AWS services to interact securely with each other.",
    "Applicability": "All AWS services requiring cross-service interaction",
    "Security Risk": "Improperly configured roles could lead to unauthorized access to services.",
    "Default Behavior / Limitations": "AWS services may create service-linked roles automatically when needed.",
    "Automation": "Monitoring via AWS Config and CloudTrail checks on role modifications.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html"
    ]
  },
  {
    "Title": "Set Permissions Boundaries on IAM Entities",
    "Description": "Use permissions boundaries to define the maximum permissions that any identity policy can grant.",
    "Applicability": "All IAM users and roles",
    "Security Risk": "Lack of boundaries can lead to over-provisioning and increase the risk of policy mismanagement.",
    "Default Behavior / Limitations": "Permissions boundaries must be manually defined and applied.",
    "Automation": "Monitor and audit using AWS Config rules and IAM policy validations.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html"
    ]
  },
  {
    "Title": "Apply Service Control Policies (SCPs) for AWS Organizations",
    "Description": "Use SCPs to enforce the maximum permissions that identities can have in an AWS Organization.",
    "Applicability": "All AWS Organizations and corresponding OUs",
    "Security Risk": "Without SCPs, organizations risk unauthorized actions beyond desired security limits.",
    "Default Behavior / Limitations": "SCPs must be manually configured and applied to OUs.",
    "Automation": "Enforced and managed using AWS Organizations and AWS Config.",
    "References": [
      "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html"
    ]
  }
]
```