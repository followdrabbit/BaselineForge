```json
[
  {
    "Title": "Use IAM Roles for EC2 Instances Instead of Long-Term Credentials",
    "Description": "Configure an instance profile that includes an IAM role for applications running on Amazon EC2 instances, ensuring these applications use temporary security credentials instead of creating IAM users with long-term credentials.",
    "Applicability": "All Amazon EC2 instances running applications",
    "Security Risk": "Using long-term credentials increases the risk of credential exposure and unauthorized access to AWS resources.",
    "Default Behavior / Limitations": "AWS supports the use of IAM roles via instance profiles but requires manual configuration.",
    "Automation": "Can be monitored using AWS Config rule `ec2-instance-no-associated-iam-instance-profile`.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/security-iam.html",
      "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html"
    ]
  },
  {
    "Title": "Implement Multi-Factor Authentication (MFA) for Root and IAM Users",
    "Description": "Enable MFA for the AWS account root user and for IAM users to enhance the security of their account access. Configure IAM policies to enforce this.",
    "Applicability": "AWS account root user and all IAM users where applicable",
    "Security Risk": "Without MFA, compromised credentials can lead to unauthorized account access and data breaches.",
    "Default Behavior / Limitations": "AWS does not enforce MFA by default; it must be manually enabled.",
    "Automation": "Can be audited using AWS Security Hub and AWS Config rule `root-account-mfa-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html",
      "https://docs.aws.amazon.com/vpc/latest/userguide/security-iam.html"
    ]
  },
  {
    "Title": "Regularly Rotate IAM Access Keys",
    "Description": "Implement a schedule to rotate access keys for IAM users that require long-term credentials and ensure no unenforced credentials are exploited.",
    "Applicability": "All IAM users with long-term credentials",
    "Security Risk": "Stale or exposed access keys can lead to unauthorized AWS resource access if compromised.",
    "Default Behavior / Limitations": "AWS does not automatically rotate access keys; it requires manual intervention or custom automation.",
    "Automation": "Can be enforced using AWS Lambda to automate key rotation or monitored using AWS Config rule `access-keys-rotated`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html",
      "https://docs.aws.amazon.com/vpc/latest/userguide/security-iam.html"
    ]
  },
  {
    "Title": "Monitor IAM Policies Compliance with Least Privilege Principle",
    "Description": "Use AWS Config to ensure that IAM policies grant only the permissions necessary to perform specified tasks in accordance with the principle of least privilege.",
    "Applicability": "All IAM policies across AWS accounts",
    "Security Risk": "Excessive permissions increase vulnerability to attacks and unauthorized access.",
    "Default Behavior / Limitations": "AWS policies do not automatically restrict minimal permissions; they need manual analysis and configuration.",
    "Automation": "Can be enforced using AWS Config rule `iam-policy-no-statements-with-admin-access`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html",
      "https://docs.aws.amazon.com/vpc/latest/userguide/security-iam.html"
    ]
  },
  {
    "Title": "Set Permissions Boundaries for IAM Policies",
    "Description": "Define permissions boundaries for IAM roles and users to restrict the maximum permissions they can receive, thus ensuring they cannot exceed predefined boundaries.",
    "Applicability": "Specific IAM roles and users as per organizational requirement",
    "Security Risk": "Without boundaries, users and roles may be granted excessive permissions leading to potential misuse.",
    "Default Behavior / Limitations": "Permissions boundaries require manual setup and configuration.",
    "Automation": "Can be audited using AWS Config rule `iam-permissions-boundary-set`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html",
      "https://docs.aws.amazon.com/vpc/latest/userguide/security-iam.html"
    ]
  },
  {
    "Title": "Utilize Service Control Policies (SCPs) for Centralized Permissions Management",
    "Description": "Implement SCPs within AWS Organizations to enforce a centralized permissions control strategy across all member accounts.",
    "Applicability": "All AWS accounts within an organization using AWS Organizations",
    "Security Risk": "Unmanaged permissions could lead to breaches and inconsistent security posture across accounts.",
    "Default Behavior / Limitations": "SCPs are not enabled by default for all organizations' accounts and require manual configuration.",
    "Automation": "Can be managed centrally using AWS Organizations.",
    "References": [
      "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html",
      "https://docs.aws.amazon.com/vpc/latest/userguide/security-iam.html"
    ]
  }
]
```