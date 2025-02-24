```json
[
  {
    "Title": "Disable and Remove Unused AWS Root Access Keys",
    "Description": "Ensure that root access keys are monitored and removed if not in use, as it is recommended to use temporary credentials such as those provided by AWS IAM Identity Center instead.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Keeping root access keys active increases the risk of unauthorized access, potentially leading to full account compromise.",
    "Default Behavior / Limitations": "AWS does not automatically disable root access keys even if they are unused.",
    "Automation": "Can be monitored using AWS Security Hub to log and alert on any usage of root access keys. Manual removal through IAM is required.",
    "References": [
      "https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html#root-password"
    ]
  },
  {
    "Title": "Automated Generation and Review of IAM Credential Reports",
    "Description": "Set up a scheduled task to generate and download an IAM credential report regularly. Identify and remove credentials that have not been used recently.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Stale credentials may become potential security vulnerabilities if they remain active unnecessarily.",
    "Default Behavior / Limitations": "Credentials must be manually reviewed and removed based on the report.",
    "Automation": "Automate credential report generation using AWS CLI and schedule using AWS Lambda or a similar solution for periodic reviews.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html"
    ]
  },
  {
    "Title": "Ensure Principle of Least Privilege for IAM Permissions",
    "Description": "Regularly review IAM users, groups, and roles to ensure they have only the permissions needed for their roles.",
    "Applicability": "All IAM users, groups, and roles",
    "Security Risk": "Excessive permissions can lead to potential security breaches by unauthorized actions.",
    "Default Behavior / Limitations": "Manual review and adjustment of IAM policies are required.",
    "Automation": "AWS IAM Access Analyzer can be used for auditing and identifying overly permissive access.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html"
    ]
  },
  {
    "Title": "Restrict iam:PassRole Permission for EC2 Launching Users",
    "Description": "Ensure that users with the ability to launch EC2 instances have restricted iam:PassRole permissions to explicitly listed roles only.",
    "Applicability": "AWS accounts where AWS IAM users can launch EC2 instances",
    "Security Risk": "Incorrectly configured iam:PassRole permissions can lead to privilege escalation by passing unauthorized roles.",
    "Default Behavior / Limitations": "IAM policies must be configured accordingly.",
    "Automation": "Use AWS IAM and AWS Config to enforce and audit these configurations via policies.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-usingrole-ec2instance.html#roles-usingrole-ec2instance-passrole"
    ]
  },
  {
    "Title": "Use IAM GetAccountAuthorizationDetails for Policy Optimization",
    "Description": "Regularly review IAM policies using the GetAccountAuthorizationDetails API to ensure they do not include permissions for unused services.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Having policies for unused services expands the attack surface unnecessarily.",
    "Default Behavior / Limitations": "Requires regular manual analysis and policy updates.",
    "Automation": "Automate the API call to GetAccountAuthorizationDetails and use scripting to identify discrepancies for review.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountAuthorizationDetails.html"
    ]
  },
  {
    "Title": "Regular Review and Update of SAML Identity Provider Metadata",
    "Description": "Ensure SAML Identity Provider metadata documents are regularly reviewed and updated to align with current business requirements.",
    "Applicability": "AWS accounts using SAML-based federated authentication",
    "Security Risk": "Outdated metadata can lead to authentication issues or unauthorized access.",
    "Default Behavior / Limitations": "AWS does not automatically update or verify these documents.",
    "Automation": "Manual validation is required; automate reminders or scripts to verify and update as needed.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html"
    ]
  },
  {
    "Title": "Prevent Embedding of AWS Access Keys in Mobile Applications",
    "Description": "Ensure mobile applications do not embed AWS access keys. Instead, use temporary credentials like those provided through Amazon Cognito.",
    "Applicability": "AWS accounts with mobile applications accessing AWS resources",
    "Security Risk": "Leaked access keys in mobile applications can lead to unauthorized AWS resource access.",
    "Default Behavior / Limitations": "Requires source code and build process reviews.",
    "Automation": "Use AWS CodeGuru or third-party tools to scan mobile source code automatically.",
    "References": [
      "https://aws.amazon.com/cognito/"
    ]
  },
  {
    "Title": "Restrict IAM Permissions for Creation of Roles, Groups, and Policies",
    "Description": "Limit IAM permission to create roles, groups, and policies to a small trusted set of identities.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Inadequately restricted permissions could result in privilege escalation through custom role and policy creation.",
    "Default Behavior / Limitations": "Requires setting IAM policies appropriately.",
    "Automation": "Enforce using AWS Service Control Policies (SCPs) and IAM policies. Monitor with AWS IAM Access Analyzer.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"
    ]
  }
]
```