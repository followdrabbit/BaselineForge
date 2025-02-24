```json
[
  {
    "Title": "Use Short-Term Access Keys Instead of Long-Term AWS Access Keys",
    "Description": "Ensure that applications and systems use short-term access keys generated through IAM roles or AWS Security Token Service (STS) instead of long-term access keys to enhance security.",
    "Applicability": "All AWS accounts and applications",
    "Security Risk": "Long-term access keys pose a higher security risk if compromised as they remain valid indefinitely until manually rotated or revoked.",
    "Default Behavior / Limitations": "AWS does not automatically enforce the use of short-term credentials; it requires manual configuration.",
    "Automation": "Can be partially automated using AWS Config rule to monitor for IAM roles usage, but requires manual policy enforcement to avoid long-term key creation.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds-programmatic-access.html"
    ]
  },
  {
    "Title": "Avoid Embedding AWS Access Keys in Code Repositories",
    "Description": "Implement AWS Secrets Manager or AWS Systems Manager Parameter Store to manage access keys and secrets securely, ensuring they are not embedded in application code or code repositories.",
    "Applicability": "All AWS applications and development environments",
    "Security Risk": "Embedding access keys in code exposes them to unauthorized access, leading to potential IAM user credential compromise.",
    "Default Behavior / Limitations": "No default behavior to prevent this; requires explicit setup and education of developers.",
    "Automation": "Use AWS Secrets Manager or AWS Systems Manager Parameter Store to automate the management and retrieval of credentials.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds-best-practices.html",
      "https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html"
    ]
  },
  {
    "Title": "Leverage IAM Roles for Temporary Security Credentials",
    "Description": "Configure AWS resources and applications to use IAM roles for temporary security credentials, thus eliminating the need for long-term access keys.",
    "Applicability": "All AWS environments supporting IAM roles",
    "Security Risk": "Without the use of IAM roles, long-term credentials can be mishandled, leading to credential exposure and potential AWS account compromises.",
    "Default Behavior / Limitations": "IAM roles need to be assigned; AWS does not configure this automatically upon resource creation.",
    "Automation": "AWS IAM can be used with AWS Config rules to enforce IAM role use on resources like EC2, Lambda through rules such as `required-tags`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html"
    ]
  },
  {
    "Title": "Use AWS CloudShell or AWS CLI Version 2 for Access Key Management",
    "Description": "Adopt AWS CloudShell or AWS CLI Version 2 integrated with IAM Identity Center for managing short-term access keys efficiently without exposing them to manual handling.",
    "Applicability": "AWS environments where management tools are used for resource interaction",
    "Security Risk": "Manual handling of keys increases the risk of exposure; automation tools like CloudShell reduce this risk.",
    "Default Behavior / Limitations": "Not configured by default; requires user adoption and configuration.",
    "Automation": "AWS CloudShell is automatically configured to use a unique environment for each user, reducing configuration complexity.",
    "References": [
      "https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html",
      "https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html"
    ]
  },
  {
    "Title": "Restrict Long-Term Access Keys for Human Users",
    "Description": "Human users requiring AWS service access should use IAM Identity Center for temporary credentials instead of creating long-term access keys.",
    "Applicability": "All AWS accounts managing human user access",
    "Security Risk": "Long-term keys increase the risk of unauthorized access if compromised; temporary keys minimize this risk.",
    "Default Behavior / Limitations": "IAM Identity Center enables temporary credentials but needs to be configured properly.",
    "Automation": "Automatable through IAM Identity Center setup and policy enforcement using SCPs to prevent key creation.",
    "References": [
      "https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html"
    ]
  },
  {
    "Title": "Eliminate Long-Term Access Keys in AWS Compute Services",
    "Description": "Integrate IAM roles with compute services like EC2 to provide automatically rotating temporary security credentials, eliminating the need for long-term credentials stored in instances.",
    "Applicability": "All AWS compute services",
    "Security Risk": "Storing access keys on compute resources exposes them to security risks such as unauthorized access or data leak.",
    "Default Behavior / Limitations": "IAM roles can be assigned at the resource level, but need to be configured; AWS does not do this by default.",
    "Automation": "Can be enforced via AWS Config rules for resource configuration compliance checks.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html"
    ]
  }
]
```