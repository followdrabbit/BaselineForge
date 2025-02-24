```json
[
    {
        "Title": "Use Federation for Human User Access",
        "Description": "Enforce the use of an identity provider for federated access to AWS, allowing human users to obtain temporary credentials for access, reducing long-term credential usage.",
        "Applicability": "All AWS accounts with human users",
        "Security Risk": "Long-term credentials could be exposed, leading to unauthorized access and credential misuse.",
        "Default Behavior / Limitations": "AWS IAM does not enforce federation by default. Requires configuration via identity provider.",
        "Automation": "Configuration can be monitored via AWS IAM Identity Center.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"
        ]
    },
    {
        "Title": "Enforce MFA for IAM Users and Root Access",
        "Description": "Require multi-factor authentication (MFA) for IAM users and the root user to access AWS accounts, leveraging AWS Config and IAM policies for compliance checks.",
        "Applicability": "All AWS accounts",
        "Security Risk": "Compromised credentials could enable unauthorized access, posing significant security risks.",
        "Default Behavior / Limitations": "AWS does not enforce MFA by default. It must be configured manually.",
        "Automation": "AWS Config rules like `iam-user-mfa-enabled` and IAM policies can be used to enforce MFA requirements.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html"
        ]
    },
    {
        "Title": "Apply Least-Privilege Permissions",
        "Description": "Grant the minimum necessary permissions to users and resources based on specific tasks, using AWS IAM policies and AWS IAM Access Analyzer for policy compliance.",
        "Applicability": "All AWS resources and accounts",
        "Security Risk": "Excessive permissions can increase the attack surface and risk of abuse.",
        "Default Behavior / Limitations": "AWS allows creation of permissive policies. Implementation of least-privilege is manual.",
        "Automation": "AWS IAM Access Analyzer and AWS Config can enforce and audit compliance.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"
        ]
    },
    {
        "Title": "Use Temporary Credentials via IAM Roles and Federation",
        "Description": "Configure workloads and human users to use temporary credentials by associating them with IAM roles or federated access, avoiding long-term credential use.",
        "Applicability": "All AWS accounts and applications",
        "Security Risk": "Long-term credentials are susceptible to compromise, increasing the risk of unauthorized access.",
        "Default Behavior / Limitations": "Both permanent and temporary credentials are allowed by default.",
        "Automation": "Use AWS IAM Access Analyzer and AWS Config to verify adherence to temporary credential usage.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html"
        ]
    },
    {
        "Title": "Enable AWS CloudTrail for Comprehensive Logging",
        "Description": "Configure AWS CloudTrail to capture all API and user activity in all regions and store logs centrally in an S3 bucket for compliance and auditing.",
        "Applicability": "All AWS accounts",
        "Security Risk": "Without logging, monitoring and auditing changes and unauthorized activities is challenging.",
        "Default Behavior / Limitations": "CloudTrail is not enabled globally by default.",
        "Automation": "Use AWS Config rule `cloud-trail-enabled` to enforce CloudTrail activation across all regions.",
        "References": [
            "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html"
        ]
    },
    {
        "Title": "Prevent Creation of Access Keys for Root User",
        "Description": "Ensure that AWS access keys are not created for the root user. Manage access through IAM users with defined permissions.",
        "Applicability": "Root user of all AWS accounts",
        "Security Risk": "Long-lived root user access keys increase credential leakage risk.",
        "Default Behavior / Limitations": "AWS allows creation of access keys for root users, but it's discouraged.",
        "Automation": "Manual validation required. Regularly audit IAM credentials.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html#root-user-no-access-keys"
        ]
    },
    {
        "Title": "Central Management of Root User Credentials via AWS Organizations",
        "Description": "Utilize AWS Organizations to centrally manage root credentials of member accounts, implementing Organizational Units (OU) for management policies.",
        "Applicability": "AWS Organization management accounts",
        "Security Risk": "Lack of central management can lead to mismanaged root credentials.",
        "Default Behavior / Limitations": "Central management is not enforced by default.",
        "Automation": "Enforce management policies using AWS Organizations and SCPs.",
        "References": [
            "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_type-auth.html"
        ]
    },
    {
        "Title": "Invalidate and Remove Unused Access Keys Regularly",
        "Description": "Conduct periodic audits of IAM access keys to identify and remove unused or stale credentials, ensuring keys in use are only for active accounts.",
        "Applicability": "All AWS accounts with IAM users",
        "Security Risk": "Stale or unused credentials pose potential security risks.",
        "Default Behavior / Limitations": "AWS does not automatically disable or remove unused keys.",
        "Automation": "Regular reports through AWS IAM Credential Reports and AWS Lambda for automation.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/credential-reports.html"
        ]
    },
    {
        "Title": "Utilize IAM Access Analyzer for Policy Generation and Verification",
        "Description": "Use IAM Access Analyzer to automatically generate least-privilege policies and validate compliance with best practice security configurations.",
        "Applicability": "All AWS accounts",
        "Security Risk": "Overly permissive or misconfigured policies could lead to data breaches.",
        "Default Behavior / Limitations": "IAM Access Analyzer requires activation.",
        "Automation": "Fully automate using AWS IAM Access Analyzer.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html"
        ]
    },
    {
        "Title": "Implement Service Control Policies (SCPs) for Organizational Guardrails",
        "Description": "Apply SCPs in AWS Organizations to restrict and manage permissions across member accounts, ensuring consistent policy enforcement.",
        "Applicability": "AWS Organizations",
        "Security Risk": "Without SCPs, accounts may drift from compliance standards.",
        "Default Behavior / Limitations": "AWS Organizations required for SCPs.",
        "Automation": "Automated through AWS Organizations.",
        "References": [
            "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_type-auth.html"
        ]
    }
]
```