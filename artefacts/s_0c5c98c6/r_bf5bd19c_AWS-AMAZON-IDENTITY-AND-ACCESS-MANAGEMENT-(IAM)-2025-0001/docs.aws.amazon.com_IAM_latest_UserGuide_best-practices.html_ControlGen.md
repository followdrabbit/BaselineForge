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