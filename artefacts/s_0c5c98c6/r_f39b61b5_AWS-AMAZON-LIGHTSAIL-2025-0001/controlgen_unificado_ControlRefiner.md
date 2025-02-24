```json
[
  {
    "Title": "Block Public Access at the S3 Bucket Level",
    "Description": "Ensure that S3 public access is blocked at the bucket level to prevent unauthorized data exposure. Implement S3 Block Public Access settings on each bucket, using AWS Config to monitor compliance.",
    "Applicability": "All Amazon S3 buckets",
    "Security Risk": "Public buckets can lead to data leaks.",
    "Default Behavior / Limitations": "By default, S3 does not block public access automatically.",
    "Automation": "Can be enforced and monitored using AWS Config rules.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html"
    ]
  },
  {
    "Title": "Enable MFA-Delete on S3 Buckets",
    "Description": "Require Multi-Factor Authentication (MFA) for any S3 bucket deletion operation to prevent accidental or malicious data removal. Configure MFA-Delete on critical buckets and ensure MFA is used during delete operations.",
    "Applicability": "All S3 buckets with deletion capabilities",
    "Security Risk": "Without MFA-Delete, unauthorized users could permanently delete critical data.",
    "Default Behavior / Limitations": "MFA-Delete is not enabled by default; requires manual configuration.",
    "Automation": "Manual validation required; currently not enforceable through AWS Config or IAM.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/userguide/MFADelete.html"
    ]
  },
  {
    "Title": "Enforce Multi-Factor Authentication (MFA) for Root and IAM Users",
    "Description": "Ensure multi-factor authentication is configured for both the AWS account root user and all IAM users. Enforce using IAM policies and AWS Config rule `iam-user-mfa-enabled` for monitoring compliance.",
    "Applicability": "All AWS accounts and IAM users",
    "Security Risk": "Without MFA, stolen credentials can lead to unauthorized access, resulting in potential data breaches or privilege escalation.",
    "Default Behavior / Limitations": "AWS does not enforce MFA by default; it needs to be configured for each user.",
    "Automation": "Enforced using IAM policies and monitored through AWS Config.",
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
    "Description": "Ensure applications running on EC2 instances use IAM roles for access management instead of embedding credentials. Assign appropriate roles to EC2 instances upon launch.",
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
    "Description": "Configure IAM policies to grant only the permissions necessary to perform a user's required tasks, adhering to the principle of least privilege. Schedule regular reviews of IAM policies to maintain this principle.",
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
  },
  {
    "Title": "Enforce IAM Identity-Based Policies for Lightsail",
    "Description": "IAM policies for Amazon Lightsail should include action elements with the prefix 'lightsail:' to enforce permission settings correctly. Define explicit allow or deny actions for managing Lightsail resources.",
    "Applicability": "All AWS accounts utilizing Amazon Lightsail",
    "Security Risk": "Incorrect actions could lead to unauthorized access or modification of Lightsail resources.",
    "Default Behavior / Limitations": "IAM does not automatically prefix actions with 'lightsail:'.",
    "Automation": "Audited using AWS Config rule 'iam-policy-check' and IAM Access Analyzer.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html",
      "https://docs.aws.amazon.com/lightsail/latest/userguide/security_iam_service-with-iam.html"
    ]
  },
  {
    "Title": "Implement Resource-Level Permissions Using ARNs or Wildcards in Lightsail Policies",
    "Description": "When declaring resources in IAM policies for Lightsail, use specific ARNs where possible, or wildcards (*) for actions without resource-level support.",
    "Applicability": "All AWS accounts utilizing Amazon Lightsail",
    "Security Risk": "Indiscriminate use of wildcards can lead to overly permissive policies.",
    "Default Behavior / Limitations": "Some Lightsail actions do not support resource-specific ARNs.",
    "Automation": "Requires manual validation.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_resource.html",
      "https://docs.aws.amazon.com/lightsail/latest/userguide/security_iam_service-with-iam.html"
    ]
  },
  {
    "Title": "Use Global Condition Keys in IAM Policies for Lightsail",
    "Description": "Integrate global condition keys in IAM policies for Lightsail to enhance policy control, ensuring compatibility with supported actions and resources.",
    "Applicability": "All AWS accounts utilizing Amazon Lightsail",
    "Security Risk": "Misconfigured keys can disrupt permission enforcement.",
    "Default Behavior / Limitations": "Customer-managed.",
    "Automation": "Verified via AWS IAM Access Analyzer.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html",
      "https://docs.aws.amazon.com/lightsail/latest/userguide/security_iam_service-with-iam.html"
    ]
  },
  {
    "Title": "Use Tag-Based Authorization in Lightsail IAM Policies",
    "Description": "Control access based on tags by attaching tags to Lightsail resources and including them in IAM policy condition elements.",
    "Applicability": "All AWS accounts utilizing Amazon Lightsail",
    "Security Risk": "Improper tag management might allow unauthorized access.",
    "Default Behavior / Limitations": "Manual verification required for applicable actions.",
    "Automation": "Assisted with AWS Resource Access Manager.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html",
      "https://docs.aws.amazon.com/lightsail/latest/userguide/security_iam_service-with-iam.html"
    ]
  },
  {
    "Title": "Utilize Temporary Credentials for Lightsail Access",
    "Description": "Leverage AWS STS to obtain temporary credentials for Amazon Lightsail, ensuring these credentials are securely distributed and managed.",
    "Applicability": "All AWS accounts utilizing Amazon Lightsail",
    "Security Risk": "Permanent credentials have a higher compromise risk.",
    "Default Behavior / Limitations": "Credentials are transient and need ongoing monitoring.",
    "Automation": "Monitor lifecycle with AWS IAM Access Analyzer and CloudWatch.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html",
      "https://docs.aws.amazon.com/lightsail/latest/userguide/security_iam_service-with-iam.html"
    ]
  },
  {
    "Title": "Monitor Lightsail Service-Linked Roles",
    "Description": "Regularly review Lightsail service-linked roles to ensure secure resource access.",
    "Applicability": "All AWS accounts utilizing Amazon Lightsail",
    "Security Risk": "Unauthorized role changes can cause service disruption.",
    "Default Behavior / Limitations": "AWS defines roles permissions; cannot be modified.",
    "Automation": "Monitor with AWS CloudTrail and IAM Access Analyzer.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html",
      "https://docs.aws.amazon.com/lightsail/latest/userguide/security_iam_service-with-iam.html"
    ]
  },
  {
    "Title": "Ensure Automatic Creation of AWSServiceRoleForLightsail",
    "Description": "Monitor to ensure AWSServiceRoleForLightsail is automatically created as needed for instance export operations.",
    "Applicability": "All AWS accounts utilizing Amazon Lightsail",
    "Security Risk": "Manual role creation can lead to errors.",
    "Default Behavior / Limitations": "Auto-provision by AWS.",
    "Automation": "Monitor using AWS Config for role existence.",
    "References": [
      "https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-using-service-linked-roles.html#creating-service-linked-role"
    ]
  },
  {
    "Title": "Restrict IAM Role Actions to Necessary Lightsail Operations",
    "Description": "Limit IAM role permissions for actions necessary for Lightsail operations to minimize potential attack surfaces.",
    "Applicability": "IAM roles used with Amazon Lightsail service-linked operations",
    "Security Risk": "Excess permissions increase unauthorized action risks.",
    "Default Behavior / Limitations": "Default roles may have excessive permissions.",
    "Automation": "Apply least privilege principles with AWS IAM and enforce with AWS Config rules.",
    "References": [
      "https://docs.aws.amazon.com/lightsail/latest/userguide/security_iam_service-with-iam.html"
    ]
  },
  {
    "Title": "Automated Updates and Patches for Amazon Lightsail Instances and Applications",
    "Description": "Implement automated updates for Lightsail instances using operating system package managers to ensure systems are patched against vulnerabilities.",
    "Applicability": "All Amazon Lightsail instances and container services",
    "Security Risk": "Failure to maintain updates can lead to exploitation of vulnerabilities.",
    "Default Behavior / Limitations": "AWS does not automatically update instances; user responsibility.",
    "Automation": "Use OS-native tools for automated updates.",
    "References": [
      "https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-update-management.html"
    ]
  }
]
```