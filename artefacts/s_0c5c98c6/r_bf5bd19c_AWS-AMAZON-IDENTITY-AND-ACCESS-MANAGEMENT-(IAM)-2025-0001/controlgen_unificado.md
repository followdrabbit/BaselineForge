### ControlGen Output - Arquivo 1
```json
[
    {
        "Title": "Use Federation for Human Users",
        "Description": "Enforce the use of an identity provider for federated access to AWS, allowing human users to obtain temporary credentials for access.",
        "Applicability": "All AWS accounts with human users",
        "Security Risk": "Without federation, long-term credentials could be exposed, leading to potential unauthorized access and credential misuse.",
        "Default Behavior / Limitations": "AWS IAM does not enforce federation by default. Configuration via identity provider is required.",
        "Automation": "Configuration can be monitored via AWS IAM Identity Center.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"
        ]
    },
    {
        "Title": "Require Temporary Credentials for Workloads",
        "Description": "Configure workloads to use temporary credentials by associating them with IAM roles, reducing the risk of credential leaks.",
        "Applicability": "All AWS accounts with workload deployments",
        "Security Risk": "Permanent credentials are susceptible to being compromised, resulting in unauthorized full-time access.",
        "Default Behavior / Limitations": "By default, AWS services allow for both permanent and temporary credentials.",
        "Automation": "Implementation requires manual setup of IAM roles. Monitoring can be performed via AWS Config rules.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"
        ]
    },
    {
        "Title": "Enforce MFA for IAM Users and Root Access",
        "Description": "Require multi-factor authentication (MFA) for IAM users and the root user to access your AWS account for enhanced security.",
        "Applicability": "All AWS accounts",
        "Security Risk": "Without MFA, compromised credentials could enable unauthorized access, posing a significant security risk.",
        "Default Behavior / Limitations": "AWS does not enforce MFA by default. It must be configured manually.",
        "Automation": "Can be enforced using AWS IAM policies and Config rules for monitoring MFA status.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"
        ]
    },
    {
        "Title": "Regularly Update Long-term Credentials",
        "Description": "Perform regular audits and updates on access keys for IAM users, especially those with long-term credentials, to mitigate risk.",
        "Applicability": "All AWS accounts with users leveraging long-term credentials",
        "Security Risk": "Outdated access keys can be compromised, leading to unauthorized access.",
        "Default Behavior / Limitations": "AWS does not automatically rotate access keys; manual processes are necessary.",
        "Automation": "Monitoring can be done using AWS IAM policies for last accessed key information.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"
        ]
    },
    {
        "Title": "Apply Least-Privilege Permissions",
        "Description": "Grant only the permissions required to perform tasks, adhering to the principle of least privilege.",
        "Applicability": "All AWS resources and accounts",
        "Security Risk": "Excessive permissions can increase the attack surface, leading to potential abuse or misconfiguration.",
        "Default Behavior / Limitations": "AWS allows the creation of permissive policies, but least-privilege must be enforced manually.",
        "Automation": "Use AWS IAM Access Analyzer and AWS Config to enforce policy compliance.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"
        ]
    },
    {
        "Title": "Transition to Custom Least-Privilege Policies",
        "Description": "Begin with AWS managed policies and transition to custom policies to achieve least-privilege.",
        "Applicability": "All AWS accounts at initial deployment stages",
        "Security Risk": "Relying solely on managed policies may not always align with specific organizational requirements.",
        "Default Behavior / Limitations": "Managed policies are broad and may grant unnecessary permissions.",
        "Automation": "Manual policy customization is required; AWS IAM Access Analyzer can assist.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"
        ]
    },
    {
        "Title": "Use IAM Access Analyzer for Policy Generation",
        "Description": "Utilize IAM Access Analyzer to automatically generate least-privilege policies based on actual access patterns.",
        "Applicability": "All AWS accounts",
        "Security Risk": "Manually created policies without analysis may lead to overly broad permissions.",
        "Default Behavior / Limitations": "IAM Access Analyzer requires setup and does not operate by default.",
        "Automation": "Can be automated using AWS IAM Access Analyzer.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"
        ]
    },
    {
        "Title": "Remove Unused IAM Resources Regularly",
        "Description": "Perform regular reviews and removal of unused IAM users, roles, permissions, and access keys to minimize risk.",
        "Applicability": "All AWS accounts",
        "Security Risk": "Unused resources can be exploited if not adequately managed.",
        "Default Behavior / Limitations": "AWS does not automatically delete unused resources.",
        "Automation": "Automation can be achieved using AWS IAM Access Advisor and AWS Config.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"
        ]
    },
    {
        "Title": "Implement Conditions in IAM Policies",
        "Description": "Use conditions within IAM policies to further restrict access to resources, utilizing context such as IP address or time.",
        "Applicability": "All AWS accounts and resources",
        "Security Risk": "Policies without conditions may grant broader access than intended.",
        "Default Behavior / Limitations": "Condition keys must be explicitly specified in policies.",
        "Automation": "Manual configuration is required with validation possible via AWS IAM policy simulator.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"
        ]
    },
    {
        "Title": "Verify Access with IAM Access Analyzer",
        "Description": "Utilize IAM Access Analyzer to verify and analyze resource policies for public and cross-account access configurations.",
        "Applicability": "All AWS accounts with shared resources",
        "Security Risk": "Incorrect configurations may expose resources publicly or to unintended accounts.",
        "Default Behavior / Limitations": "IAM Access Analyzer setup is required.",
        "Automation": "Fully automatable using AWS IAM Access Analyzer.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"
        ]
    },
    {
        "Title": "Validate IAM Policies Using IAM Access Analyzer",
        "Description": "Employ IAM Access Analyzer to review and enhance IAM policies, ensuring they meet security and functional requirements.",
        "Applicability": "All AWS accounts",
        "Security Risk": "Policies may be overly permissive or restrictive if not validated.",
        "Default Behavior / Limitations": "IAM Access Analyzer requires activation and setup.",
        "Automation": "Can be automated using AWS IAM Access Analyzer.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"
        ]
    },
    {
        "Title": "Establish Permissions Guardrails with SCPs",
        "Description": "Employ AWS Organizations to define service control policies (SCPs) and resource control policies (RCPs) for consistent permissions enforcement across accounts.",
        "Applicability": "Multiple-account AWS environments managed by AWS Organizations",
        "Security Risk": "Without guardrails, accounts may drift from desired policy baseline, increasing security risks.",
        "Default Behavior / Limitations": "AWS Organizations is required for SCPs implementation.",
        "Automation": "Fully automatable using AWS Organizations.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"
        ]
    },
    {
        "Title": "Use Permissions Boundaries for Delegated Management",
        "Description": "Implement permissions boundaries within an AWS account to manage and enforce specific security controls while delegating permissions.",
        "Applicability": "Single AWS accounts where delegated permissions management is needed",
        "Security Risk": "Without control, delegated admins may grant broader permissions than intended.",
        "Default Behavior / Limitations": "Permissions boundaries must be explicitly defined; they do not grant permissions on their own.",
        "Automation": "Manual setup required; can be monitored using AWS IAM policies.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"
        ]
    }
]
```

### ControlGen Output - Arquivo 2
```json
[
  {
    "Title": "Enforce Multi-Factor Authentication (MFA) for Root User Sign-In",
    "Description": "Ensure that multi-factor authentication (MFA) is enabled for the root user of your AWS account. This is a critical security measure to protect your account from unauthorized access.",
    "Applicability": "Root user of all AWS accounts",
    "Security Risk": "Without MFA, the root account is vulnerable to unauthorized access if credentials are compromised, posing significant security risks.",
    "Default Behavior / Limitations": "AWS does not enforce MFA for root users by default. It must be manually configured.",
    "Automation": "Manual validation required to ensure MFA is enabled for root user. AWS Config rule `root-account-mfa-enabled` can help evaluate compliance.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html#root-user-mfa"
    ]
  },
  {
    "Title": "Prohibit Creation of Access Keys for Root User",
    "Description": "Do not create AWS access keys for the root user. Access should be managed through IAM users with more specific permissions.",
    "Applicability": "Root user of all AWS accounts",
    "Security Risk": "Access keys for the root user increase the risk of credential leakage and unauthorized access, leading to potential misuse of account privileges.",
    "Default Behavior / Limitations": "AWS allows creation of access keys for root users, but it is strongly discouraged.",
    "Automation": "Manual validation required to ensure root user does not have access keys. Regularly audit IAM credentials.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html#root-user-no-access-keys"
    ]
  },
  {
    "Title": "Require Strong and Unique Passwords for Root User",
    "Description": "Ensure that the root user password complies with AWS's recommended complexity requirements, including a mix of uppercase and lowercase letters, numbers, and symbols.",
    "Applicability": "Root user of all AWS accounts",
    "Security Risk": "Weak passwords increase the likelihood of unauthorized access to critical account functions.",
    "Default Behavior / Limitations": "AWS allows configuration of password policies for IAM users but does not enforce specific password complexity for root users.",
    "Automation": "Manual enforcement required to manage the root user's password complexity. Regular checks are advisable.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html#root-user-password"
    ]
  },
  {
    "Title": "Monitor and Notify on Root User Activity",
    "Description": "Configure Amazon EventBridge to monitor root user activities and CloudWatch to send notifications using SNS when root user activities are detected.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Root user activity without monitoring could lead to undetected unauthorized changes in the account.",
    "Default Behavior / Limitations": "AWS provides tools for monitoring but requires configuration to effectively track and notify root user actions.",
    "Automation": "Can be automated with Amazon EventBridge rules and CloudWatch alarms integrated with SNS to alert administrators.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html#root-user-monitoring"
    ]
  },
  {
    "Title": "Evaluate Root User MFA Compliance with AWS Config",
    "Description": "Utilize AWS Config rules to assess and ensure that MFA is enabled for root user credentials.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Lack of MFA on root accounts can lead to unauthorized access if credentials are compromised.",
    "Default Behavior / Limitations": "AWS provides AWS Config rules to evaluate compliance but does not automatically enforce MFA.",
    "Automation": "Can be automated using AWS Config rule `root-account-mfa-enabled` to continuously evaluate MFA compliance.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html#root-user-mfa-evaluation"
    ]
  },
  {
    "Title": "Restrict Root User Actions with Service Control Policies (SCP)",
    "Description": "Apply SCPs in AWS Organizations to restrict unnecessary root user actions and prevent unauthorized activities in member accounts.",
    "Applicability": "AWS Organizations",
    "Security Risk": "Excessive permissions for root users can lead to unauthorized changes across the organization's accounts.",
    "Default Behavior / Limitations": "SCPs provide a mechanism to limit permissions but require proper configuration.",
    "Automation": "Effective use of SCPs can automatically enforce restrictions on root activities across all member accounts.",
    "References": [
      "https://docs.aws.amazon.com/organizations/latest/userguide/best-practices_member-acct.html#bp_member-acct_use-scp"
    ]
  },
  {
    "Title": "Centralize Management of Root Credentials",
    "Description": "Securely manage and centralize root credentials within AWS Organizations, eliminating individual root access for member accounts and ensuring security measures like MFA are in place.",
    "Applicability": "AWS Organizations",
    "Security Risk": "Dispersed root credentials increase the threat surface and vulnerability to unauthorized account control.",
    "Default Behavior / Limitations": "AWS advises centralization but organizations must implement this by designing their management structure.",
    "Automation": "Manual implementation is necessary to centralize credential management and enforce security policies for root users.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html#secure-org-account"
    ]
  }
]
```

### ControlGen Output - Arquivo 3
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

### ControlGen Output - Arquivo 4
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

### ControlGen Output - Arquivo 5
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

### ControlGen Output - Arquivo 6
```json
[
  {
    "Title": "Enforce Multi-Factor Authentication (MFA) for AWS Accounts",
    "Description": "Ensure that MFA is enabled and required for access to all AWS accounts. This can be done by setting up mandatory MFA using IAM policies and configuring user settings to enforce MFA usage.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without MFA, unauthorized users could gain access to the account, leading to potential data breaches or resource misuse.",
    "Default Behavior / Limitations": "AWS IAM does not enforce MFA by default on all accounts.",
    "Automation": "Can be enforced using IAM identity center settings and AWS Config rule `iam-user-mfa-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html"
    ]
  },
  {
    "Title": "Require TLS 1.2+ for All Communications with AWS",
    "Description": "Ensure that all communications with AWS resources use a minimum of TLS 1.2, recommending TLS 1.3. This can be enforced by configuring security settings on AWS services that accept SSL/TLS connections.",
    "Applicability": "All AWS resources",
    "Security Risk": "Using outdated TLS versions can expose communications to attacks like man-in-the-middle, compromising data integrity and confidentiality.",
    "Default Behavior / Limitations": "Some AWS services may require manual configuration to enforce TLS 1.3.",
    "Automation": "Can be monitored using AWS Config with custom rules.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/data-protection.html"
    ]
  },
  {
    "Title": "Enable CloudTrail for API and User Activity Logging",
    "Description": "Set up AWS CloudTrail in all AWS regions to log all API and user activity to a centralized S3 bucket for security and compliance purposes.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without logging, it becomes difficult to monitor and audit changes, posing a risk of undetected unauthorized activities.",
    "Default Behavior / Limitations": "AWS does not enable AWS CloudTrail by default globally.",
    "Automation": "Can be enforced using AWS Config rule `cloud-trail-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html"
    ]
  },
  {
    "Title": "Implement AWS Encryption and Utilize Default Security Controls",
    "Description": "Enable AWS encryption options such as SSE-S3, SSE-KMS, and other encryption services across supported AWS resources. Ensure all default security controls are active for enhanced data protection.",
    "Applicability": "All AWS resources with encryption capability",
    "Security Risk": "Unencrypted data at rest can be accessed by unauthorized users, leading to data breaches and integrity issues.",
    "Default Behavior / Limitations": "Encryption must be configured for specific services like S3 and RDS.",
    "Automation": "Can be partly enforced using AWS Config rules for specific services.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/data-protection.html"
    ]
  },
  {
    "Title": "Use FIPS 140-3 Validated Cryptography for Compliance",
    "Description": "Configure FIPS-approved virtual interfaces and enabled components to use FIPS 140-3 validated cryptography where necessary.",
    "Applicability": "AWS services used in government or compliance-heavy environments",
    "Security Risk": "Non-validated cryptography may not meet regulatory compliance requirements, exposing the organization to legal and operational risks.",
    "Default Behavior / Limitations": "Requires specific configuration of endpoints.",
    "Automation": "Requires manual validation to ensure services are using FIPS endpoints.",
    "References": [
      "https://aws.amazon.com/compliance/fips/"
    ]
  },
  {
    "Title": "Avoid Storing Sensitive Data in Tags and Free-Form Fields",
    "Description": "Ensure that sensitive information such as PII is not stored in metadata tags or free-text fields within AWS services.",
    "Applicability": "All AWS services supporting tags and metadata fields",
    "Security Risk": "Sensitive information stored in tags can be exposed through API calls or when accessing metadata.",
    "Default Behavior / Limitations": "AWS does not restrict information typed into tags.",
    "Automation": "Requires manual validation and internal policy enforcement.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/data-protection.html"
    ]
  },
  {
    "Title": "Encrypt Data Collected by IAM at Rest Using AES-256",
    "Description": "Ensure that all data collected by IAM, including customer account metadata and identifying data, is encrypted at rest using AES-256.",
    "Applicability": "IAM service data storage",
    "Security Risk": "Lack of encryption can lead to unauthorized access to sensitive information.",
    "Default Behavior / Limitations": "Encryption configurations might differ across AWS services.",
    "Automation": "Can be monitored using AWS Config with custom rules.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/data-protection.html#encryption-in-IAM"
    ]
  },
  {
    "Title": "Encrypt Customer Identifying Data in Transit Using TLS",
    "Description": "Ensure that all customer identifying data is encrypted when in transit using a minimum of TLS 1.2, recommending TLS 1.3.",
    "Applicability": "All AWS services handling customer data in transit",
    "Security Risk": "Data in transit without encryption is susceptible to interception and tampering.",
    "Default Behavior / Limitations": "Certain integrations might require additional configuration to support advanced TLS settings.",
    "Automation": "Can be monitored using AWS Config and security audits.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/data-protection.html#encryption-in-transit"
    ]
  },
  {
    "Title": "Enforce TLS for IAM Requests",
    "Description": "Ensure that all requests to AWS IAM are conducted over TLS to provide encrypted communication channels.",
    "Applicability": "All clients interfacing with IAM",
    "Security Risk": "Lack of secure transport could expose data to interception and compromise.",
    "Default Behavior / Limitations": "TLS must be explicitly enforced in client configurations.",
    "Automation": "Requires manual validation and client-side configuration.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/data-protection.html#internetwork-traffic-in-IAM"
    ]
  },
  {
    "Title": "Use VPC Endpoints for Secure AWS STS Connections",
    "Description": "Utilize VPC endpoints to securely connect to AWS STS, protecting data by keeping traffic within the Amazon network.",
    "Applicability": "AWS services requiring STS access in VPC",
    "Security Risk": "Without VPC endpoints, traffic could leave the Amazon network, being exposed to various risks.",
    "Default Behavior / Limitations": "Requires VPC endpoint configuration for STS.",
    "Automation": "Can be enforced using AWS Config with rules monitoring VPC endpoint usage.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_interface_vpc_endpoints.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 7
```json
[
  {
    "Title": "Enable AWS CloudTrail for IAM and AWS STS API Call Logging",
    "Description": "Ensure AWS CloudTrail is enabled for all regions to capture and log all API calls involving AWS Identity and Access Management (IAM) and AWS Security Token Service (STS). This is critical for auditing and monitoring security-relevant actions.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without logging API calls to IAM and STS, unauthorized access and identity-related actions may go unrecorded, making security auditing and forensic investigation difficult.",
    "Default Behavior / Limitations": "AWS CloudTrail is not enabled by default. Customers need to manually activate trails and configure them for specific services like IAM and STS.",
    "Automation": "Can be enforced using AWS Config rule `cloud-trail-enabled` and configuring the trail to log all management events. Use Security Hub to ensure coverage.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/security-logging-and-monitoring.html",
      "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html"
    ]
  },
  {
    "Title": "Use AWS IAM Access Analyzer to Detect External Access",
    "Description": "Activate AWS IAM Access Analyzer in all AWS accounts to automatically analyze all resource policies and detect any resources shared externally with entities outside the AWS account, such as other AWS accounts, organizations, or the internet.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without Access Analyzer, unintended or unauthorized external access to resources can occur, compromising data confidentiality and integrity.",
    "Default Behavior / Limitations": "AWS IAM Access Analyzer must be manually enabled in each AWS account.",
    "Automation": "Automated provisioning can be implemented through AWS CLI or SDK to create analyzers across multiple accounts and regions.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html"
    ]
  },
  {
    "Title": "Utilize Amazon CloudWatch for Real-time Monitoring of Resources",
    "Description": "Configure Amazon CloudWatch to monitor AWS infrastructure and applications. Set up alarms on critical metrics, such as CPU usage, memory usage, or application-specific logs, to trigger automatic notifications or actions upon threshold breaches.",
    "Applicability": "All AWS resources and applications",
    "Security Risk": "Without proactive monitoring, resource failures or abnormal activities may go unnoticed, leading to potential disruptions or security incidents.",
    "Default Behavior / Limitations": "CloudWatch does not monitor by default; custom metrics and alarms need configuration.",
    "Automation": "Can be set up using AWS CloudFormation templates or AWS CLI scripts to automate creation and management of CloudWatch alarms and dashboards.",
    "References": [
      "https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/"
    ]
  },
  {
    "Title": "Implement Amazon CloudWatch Logs for Centralized Logging",
    "Description": "Set up Amazon CloudWatch Logs to collect and monitor log data from EC2 instances, Lambda functions, and other resources. Store log data in a centralized and durable location for access and analysis. Implement retention policies to manage the log data lifecycle effectively.",
    "Applicability": "All AWS resources generating logs",
    "Security Risk": "Without central log management, critical security events might be overlooked, and the lack of historical data makes forensic investigations challenging.",
    "Default Behavior / Limitations": "AWS does not automatically store logs; CloudWatch Logs setup must be manually configured.",
    "Automation": "Can be automated using AWS CloudFormation, AWS CLI, and log agents such as the CloudWatch Logs agent installed on instances.",
    "References": [
      "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/"
    ]
  }
]
```

### ControlGen Output - Arquivo 8
```json
[
  {
    "Title": "Enable AWS CloudTrail for Logging IAM and AWS STS API Requests",
    "Description": "Ensure that all IAM and AWS STS API requests are captured by AWS CloudTrail and the logs are stored in an Amazon S3 bucket.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Failure to log IAM and AWS STS API calls may result in insufficient traceability for auditing and security investigations, potentially allowing unauthorized actions to go undetected.",
    "Default Behavior / Limitations": "CloudTrail is enabled by default in new accounts, but creating a specific trail is necessary for continuous logging in S3.",
    "Automation": "Can be enforced using AWS CloudTrail and AWS Config rule `cloud-trail-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html"
    ]
  },
  {
    "Title": "Configure CloudTrail to Capture Logs from All AWS Regions",
    "Description": "Ensure AWS CloudTrail is set to record activity from all AWS Regions by configuring a multi-region trail.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Not logging cross-region activity can lead to gaps in audit trails, making incident response less effective in multi-region deployments.",
    "Default Behavior / Limitations": "Trails created via the console apply to all Regions by default.",
    "Automation": "Can be enforced using AWS CloudTrail setup in the AWS Management Console.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html"
    ]
  },
  {
    "Title": "Log Specific Non-Authenticated IAM and AWS STS API Requests",
    "Description": "Configure CloudTrail to log all IAM and AWS STS authenticated API requests, including specific non-authenticated requests such as AssumeRoleWithSAML and AssumeRoleWithWebIdentity.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Omitting non-authenticated IAM and AWS STS calls can reduce visibility into federated identity actions, impacting threat detection and auditing.",
    "Default Behavior / Limitations": "These events are inherently logged when CloudTrail is enabled.",
    "Automation": "Monitored via AWS CloudTrail configuration.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html"
    ]
  },
  {
    "Title": "Include Essential Details in CloudTrail Logs for Auditing",
    "Description": "Ensure that CloudTrail logs include critical details such as IP address, requester identity, and request time to assist in auditing and troubleshooting.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Incomplete log details may hinder investigations and auditing, leading to an inability to pinpoint unauthorized access sources.",
    "Default Behavior / Limitations": "AWS CloudTrail automatically logs these details by default.",
    "Automation": "Ensured by AWS CloudTrail setups.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html"
    ]
  },
  {
    "Title": "Monitor Major IAM Operations Using CloudTrail",
    "Description": "Utilize CloudTrail to log all major IAM operations such as CreateUser, DeleteRole, and ListGroups to ensure they are actively monitored by the security team.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Unmonitored IAM operations can lead to unauthorized management and access changes, increasing the risk of privilege escalation.",
    "Default Behavior / Limitations": "IAM operations are logged when CloudTrail logging is enabled.",
    "Automation": "Monitored and managed through AWS CloudTrail views.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html"
    ]
  },
  {
    "Title": "Utilize sts:SourceIdentity Condition Key in Role Trust Policies",
    "Description": "Implement the sts:SourceIdentity condition key in AWS STS role trust policies to require users to specify their identity, providing traceability of actions for federated roles.",
    "Applicability": "AWS accounts using roles for federated access",
    "Security Risk": "Without identifying who assumes a role, it's challenging to track user actions via temporary credentials, affecting accountability.",
    "Default Behavior / Limitations": "Requires update in IAM role trust policies.",
    "Automation": "Manual validation required. Roles and policies need manual updates.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html"
    ]
  },
  {
    "Title": "Log Successful and Failed User Sign-In Events with CloudTrail",
    "Description": "Configure CloudTrail to log both successful and failed sign-in attempts to the AWS Management Console and other AWS services for enhanced security monitoring.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Not logging failed sign-in attempts could allow unauthorized access attempts to go unnoticed, compromising account security.",
    "Default Behavior / Limitations": "Sign-in events are logged when CloudTrail is properly configured.",
    "Automation": "Audited via AWS CloudTrail settings.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html"
    ]
  },
  {
    "Title": "Log Sign-In Attempts with Temporary Credentials",
    "Description": "Ensure CloudTrail logs sign-in attempts using temporary credentials, capturing multiple API calls needed for cross-account operations to ensure comprehensive monitoring.",
    "Applicability": "All AWS accounts using temporary credentials",
    "Security Risk": "Lack of logs for temporary credential usage can obscure cross-account access patterns, affecting security monitoring.",
    "Default Behavior / Limitations": "Logging of sign-in attempts is supported by enabling CloudTrail.",
    "Automation": "Managed via AWS CloudTrail log configuration.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html"
    ]
  },
  {
    "Title": "Redact Sensitive Information in CloudTrail for Failed Sign-In Attempts",
    "Description": "Configure CloudTrail to redact sensitive information from logs, such as usernames, when there is a failed sign-in attempt due to an incorrect username, to protect sensitive data.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Disclosure of raw usernames in logs can expose sensitive information, leading to potential exploitation in social engineering attacks.",
    "Default Behavior / Limitations": "Sensitive information masquing is a best practice but requires configuration.",
    "Automation": "Manual validation required to ensure redaction policies are applied.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html"
    ]
  },
  {
    "Title": "Ensure Persistence of CloudTrail Logs During Account Compromise",
    "Description": "Configure persistence mechanisms, such as S3 bucket versioning and cross-account access, to prevent deletion of CloudTrail logs in case of account compromise.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without protections, an attacker could delete or alter log data, hindering incident response and forensic investigations.",
    "Default Behavior / Limitations": "Requires manual configuration of S3 settings.",
    "Automation": "Manual validation required. S3 bucket settings need to be configured.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 9
```json
[
  {
    "Title": "Track 'AssumeRoot' Sessions in CloudTrail Logs",
    "Description": "Ensure AWS CloudTrail is configured to log all 'AssumeRoot' events. Implement monitoring for the 'AssumeRoot' event in the 'eventName' field of CloudTrail logs to detect any unauthorized root-level actions.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Failure to track 'AssumeRoot' sessions could result in undetected unauthorized access to root-level operations, potentially leading to data breaches and system compromises.",
    "Default Behavior / Limitations": "AWS CloudTrail must be enabled to record API calls and allow tracking.",
    "Automation": "Can be monitored using AWS CloudTrail with AWS Security Hub or AWS Config custom rules to detect the 'AssumeRoot' event in logs.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-track-privileged-tasks.html"
    ]
  },
  {
    "Title": "Identify 'targetPrincipal' and 'accessKeyId' in CloudTrail for 'AssumeRoot' Sessions",
    "Description": "Configure CloudTrail to log events and detect the 'targetPrincipal' and 'accessKeyId' fields to correlate 'AssumeRoot' session actions with affected resources and accounts.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without identifying 'targetPrincipal' and 'accessKeyId', it is challenging to attribute actions to specific accounts and sessions, complicating incident response and remediation efforts.",
    "Default Behavior / Limitations": "Requires CloudTrail to be configured correctly to log these details.",
    "Automation": "Can be audited using AWS CloudTrail analysis tools and AWS Config rules to check for the presence of these fields in log entries.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-track-privileged-tasks.html"
    ]
  },
  {
    "Title": "Search for Privileged Tasks Using 'accessKeyId' in 'AssumeRoot' Sessions",
    "Description": "Implement a system to search CloudTrail logs using 'accessKeyId' from 'AssumeRoot' events to trace all privileged operations executed in a session.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Not tracking privileged tasks accurately can lead to unauthorized actions being performed without detection, risking resource compromise and the security posture of the AWS account.",
    "Default Behavior / Limitations": "Requires search capabilities and access to CloudTrail logs to be manually configured or automated.",
    "Automation": "Can be automated using AWS CloudTrail insights and AWS Lambda functions to periodically search and report activities tied to specific 'accessKeyId' values.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-track-privileged-tasks.html"
    ]
  },
  {
    "Title": "Limit 'AssumeRoot' Session Duration to 900 Seconds",
    "Description": "Configure IAM roles or policies to restrict the maximum session duration of 'AssumeRoot' to 900 seconds (15 minutes) using appropriate IAM policies and role settings.",
    "Applicability": "All AWS accounts with root user access",
    "Security Risk": "Extended root session durations increase the risk of prolonged unauthorized access and potential damage if credentials are compromised.",
    "Default Behavior / Limitations": "AWS does not enforce session time limits by default for the root user. Configuration is required manually.",
    "Automation": "Can be enforced using IAM role configurations and AWS Config rule customizations to audit session durations regularly.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-track-privileged-tasks.html"
    ]
  }
]
```