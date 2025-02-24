```json
[
  {
    "Title": "Enforce Multi-Factor Authentication (MFA) for Root and IAM Users",
    "Description": "Enable MFA for the root user and all IAM users in the AWS account to provide an additional layer of security. This can be achieved by configuring IAM policies that require MFA as a condition for AWS Management Console access.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without MFA, compromised credentials could lead to unauthorized access, resulting in potential data breaches and unauthorized changes.",
    "Default Behavior / Limitations": "AWS IAM does not enforce MFA by default. It requires manual setup.",
    "Automation": "Enforced using IAM policies with AWS Config rule `iam-user-mfa-enabled`. AWS IAM Access Analyzer can be used for alerts.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html"
    ]
  },
  {
    "Title": "Central Management of Root User Credentials via AWS Organizations",
    "Description": "Utilize AWS Organizations to centrally manage root credentials of member accounts. Implement Organizational Unit (OU) structures to enforce management policies and secure root access.",
    "Applicability": "AWS Organization management accounts",
    "Security Risk": "Lack of centralized management can lead to mismanaged or leaked root credentials, increasing the risk of unauthorized account access.",
    "Default Behavior / Limitations": "Central management of root credentials is not enforced by default and must be configured using AWS Organizations.",
    "Automation": "Manage using AWS Organizations with SCPs and AWS Config for monitoring non-root access usage.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html",
      "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_type-auth.html"
    ]
  },
  {
    "Title": "Use IAM Policies for Controlled Access to AWS Resources",
    "Description": "Design and implement IAM policies to define permissions structured around the principle of least privilege. This ensures users and services have the minimum necessary access.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without appropriate IAM policies, there may be the risk of excessive permissions which could lead to unauthorized usage or data leaks.",
    "Default Behavior / Limitations": "IAM provides tools but requires explicit policy configuration based on organizational needs.",
    "Automation": "AWS Config rules like `iam-policy-no-statements-with-admin-access` can be used to monitor policy compliance.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html",
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html"
    ]
  },
  {
    "Title": "Use Temporary Security Credentials via IAM Roles and Federation",
    "Description": "Configure IAM roles and federated access to provide temporary security credentials instead of relying on long-term access keys. This strategy minimizes exposure risk by reducing credential lifespan.",
    "Applicability": "All AWS accounts and applications using AWS services",
    "Security Risk": "Long-term access keys are vulnerable to leaks and misuse which could result in unauthorized access.",
    "Default Behavior / Limitations": "AWS supports temporary credentials but implementation is contingent on application architecture.",
    "Automation": "AWS Config can monitor IAM roles and IAM Access Analyzer can verify adherence.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html"
    ]
  },
  {
    "Title": "Limit Root User Permissions via Service Control Policies (SCPs)",
    "Description": "Implement service control policies (SCPs) within AWS Organizations to restrict actions that can be performed by root users, enhancing security by limiting privileged access.",
    "Applicability": "AWS accounts under an AWS Organization",
    "Security Risk": "Unrestricted root user permissions can lead to potentially catastrophic unauthorized changes.",
    "Default Behavior / Limitations": "AWS does not apply SCPs by default; they must be defined and attached to the organization.",
    "Automation": "Managed through AWS Organizations SCPs and audited using AWS CloudTrail and AWS Config.",
    "References": [
      "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_type-auth.html",
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html"
    ]
  },
  {
    "Title": "Secure Storage for Emergency Access Credentials",
    "Description": "Ensure that Emergency Access IAM user's access keys and credentials are securely stored, such as using a password manager or secure vault, to prevent unauthorized access.",
    "Applicability": "AWS accounts with emergency access mechanisms",
    "Security Risk": "Misplaced or accessible emergency credentials could lead to potentially catastrophic unauthorized actions.",
    "Default Behavior / Limitations": "AWS does not provide internal storage solutions for credentials, requiring manual secure handling.",
    "Automation": "Requires manual validation to ensure secure storage practices are in place.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html"
    ]
  }
]
```