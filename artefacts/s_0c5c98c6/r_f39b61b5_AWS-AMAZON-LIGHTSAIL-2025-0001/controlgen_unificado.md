### ControlGen Output - Arquivo 1
```json
[
    {
        "Title": "Enforce IAM Identity-Based Policies for Lightsail",
        "Description": "IAM policies for Lightsail must include either an Action or NotAction element with the prefix 'lightsail:' to ensure that permissions are applied correctly. This includes defining explicit allow or deny actions for managing Lightsail resources.",
        "Applicability": "All AWS accounts utilizing Amazon Lightsail",
        "Security Risk": "Failure to specify correct actions can result in unintended resource access, leading to potential unauthorized access or modification of Lightsail resources.",
        "Default Behavior / Limitations": "IAM does not automatically prefix actions with 'lightsail:'; this requires explicit configuration within policies.",
        "Automation": "Can be audited using AWS Config rule 'iam-policy-check', and access can be monitored via AWS IAM Access Analyzer.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html",
            "https://docs.aws.amazon.com/lightsail/latest/userguide/security_iam_service-with-iam.html"
        ]
    },
    {
        "Title": "Implement Resource-Level Permissions Using ARNs or Wildcards in Lightsail Policies",
        "Description": "When declaring resources in IAM policies for Lightsail, use ARNs for specific resources where possible. For actions that do not support resource-level granularity, utilize wildcards (*) to specify applicable actions.",
        "Applicability": "All AWS accounts utilizing Amazon Lightsail",
        "Security Risk": "Using wildcards indiscriminately can lead to an overly permissive policy, risking unauthorized access to all Lightsail resources.",
        "Default Behavior / Limitations": "Some Lightsail actions do not support resource-specific ARNs, necessitating the use of wildcards in policies.",
        "Automation": "Manual validation required to ensure policy compliance and suitability for the specific use case.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_resource.html",
            "https://docs.aws.amazon.com/lightsail/latest/userguide/security_iam_service-with-iam.html"
        ]
    },
    {
        "Title": "Use Global Condition Keys in IAM Policies for Lightsail",
        "Description": "IAM policies for Lightsail should utilize global condition keys to specify conditions. Verify that these condition keys are compatible with specific Lightsail actions and resources to enhance policy controls.",
        "Applicability": "All AWS accounts utilizing Amazon Lightsail",
        "Security Risk": "Misconfigured condition keys can lead to improper enforcement of permissions, allowing unauthorized actions or inadvertently blocking legitimate access.",
        "Default Behavior / Limitations": "Lightsail does not support service-specific condition keys; global condition keys must be used.",
        "Automation": "AWS IAM Access Analyzer can help ensure that IAM policies are using compatible condition keys effectively.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html",
            "https://docs.aws.amazon.com/lightsail/latest/userguide/security_iam_service-with-iam.html"
        ]
    },
    {
        "Title": "Use Tag-Based Authorization in Lightsail IAM Policies",
        "Description": "Attach tags to Lightsail resources and include them in IAM policy condition elements using 'lightsail:ResourceTag/key-name', 'aws:RequestTag/key-name', or 'aws:TagKeys' to control access based on tags.",
        "Applicability": "All AWS accounts utilizing Amazon Lightsail",
        "Security Risk": "Failure to consistently apply or check tags in policies could allow unauthorized users to perform actions on misconfigured or incorrectly tagged resources.",
        "Default Behavior / Limitations": "Not all Lightsail API actions support tag-based authorization; manual verification of applicable actions is required.",
        "Automation": "AWS Resource Access Manager can assist in verifying correct tag-based authorization configurations.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html",
            "https://docs.aws.amazon.com/lightsail/latest/userguide/security_iam_service-with-iam.html"
        ]
    },
    {
        "Title": "Utilize Temporary Credentials for Lightsail Access",
        "Description": "Use AWS Security Token Service (STS) operations such as AssumeRole and GetFederationToken to acquire temporary credentials for accessing Amazon Lightsail services, ensuring these credentials are securely distributed and managed.",
        "Applicability": "All AWS accounts utilizing Amazon Lightsail",
        "Security Risk": "Permanent credentials pose a higher risk of compromise than temporary credentials, which when mismanaged, could lead to unauthorized access and actions within Lightsail.",
        "Default Behavior / Limitations": "Temporary credentials are transient and require ongoing monitoring to manage and rotate.",
        "Automation": "Use AWS IAM Access Analyzer and Amazon CloudWatch to monitor the use and lifecycle of temporary credentials.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html",
            "https://docs.aws.amazon.com/lightsail/latest/userguide/security_iam_service-with-iam.html"
        ]
    },
    {
        "Title": "Monitor Lightsail Service-Linked Roles",
        "Description": "Regularly review and monitor Lightsail service-linked roles to ensure that AWS services can access resources securely and that permissions remain unchanged.",
        "Applicability": "All AWS accounts utilizing Amazon Lightsail",
        "Security Risk": "Unauthorized changes to service-linked roles could disrupt service operations and lead to potential misuse or denial of service.",
        "Default Behavior / Limitations": "Permissions for service-linked roles are defined by AWS and cannot be modified, only monitored.",
        "Automation": "Use AWS CloudTrail to log and monitor changes in service-linked roles, and AWS IAM Access Analyzer to review role configurations.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html",
            "https://docs.aws.amazon.com/lightsail/latest/userguide/security_iam_service-with-iam.html"
        ]
    }
]
```

### ControlGen Output - Arquivo 2
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

### ControlGen Output - Arquivo 3
```json
[
  {
    "Title": "Ensure Automatic Creation of AWSServiceRoleForLightsail",
    "Description": "Ensure that AWS automatically creates the AWSServiceRoleForLightsail when exporting instances or block storage disk snapshots to Amazon EC2, avoiding the need for manual creation.",
    "Applicability": "All AWS accounts utilizing Amazon Lightsail",
    "Security Risk": "Manual creation of service-linked roles can lead to configuration errors and potential security vulnerabilities, affecting role-based access controls.",
    "Default Behavior / Limitations": "Amazon Lightsail automatically provisions the AWSServiceRoleForLightsail as needed.",
    "Automation": "Monitoring can be done using AWS Config to ensure that the role exists upon appropriate operations being performed.",
    "References": [
      "https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-using-service-linked-roles.html#creating-service-linked-role"
    ]
  },
  {
    "Title": "Grant IAM Permissions for Creating AWSServiceRoleForLightsail",
    "Description": "Configure IAM policies that allow Amazon Lightsail to automatically create the AWSServiceRoleForLightsail, thus enabling essential service operations without manual intervention.",
    "Applicability": "All AWS accounts using Lightsail services",
    "Security Risk": "Failure to give proper IAM permissions may prevent Lightsail from performing automatic operations, thereby disrupting expected functionalities.",
    "Default Behavior / Limitations": "IAM roles might not be configured by default to allow automatic role creation by Lightsail.",
    "Automation": "Enforce with AWS IAM policies using permission boundaries defined for auto-creation operations.",
    "References": [
      "https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-using-service-linked-roles.html#service-linked-role-permissions"
    ]
  },
  {
    "Title": "Prevent Deletion of AWSServiceRoleForLightsail Until All Lightsail Resources Are Deleted",
    "Description": "Implement a guard to prevent the deletion of the AWSServiceRoleForLightsail service-linked role until all related Amazon Lightsail resources are fully deleted, ensuring functional integrity.",
    "Applicability": "Amazon Lightsail operations requiring role management",
    "Security Risk": "Premature deletion of the role can lead to resource management failures and potential data loss.",
    "Default Behavior / Limitations": "AWS does not prevent role deletion without manual checks.",
    "Automation": "Utilize AWS Config rules to monitor role status and enforce policy using AWS Lambda to ensure dependencies are cleared before role deletion.",
    "References": [
      "https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-using-service-linked-roles.html#deleting-service-linked-role"
    ]
  },
  {
    "Title": "Manage IAM Policies for Service-Linked Roles",
    "Description": "Configure IAM policies to allow entities to manage the lifecycle (creation, deletion, description editing) of AWSServiceRoleForLightsail, ensuring controlled and authorized role management.",
    "Applicability": "Users needing control over service-linked roles in AWS accounts",
    "Security Risk": "Insufficient control over role lifecycle can lead to unauthorized access and security breach.",
    "Default Behavior / Limitations": "IAM policies by default may not cater to fine-grained control without explicit definitions.",
    "Automation": "Use IAM policies configured through AWS IAM for specific service-linked role management actions.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#provide-permissions"
    ]
  },
  {
    "Title": "Restrict IAM Role Actions to Necessary Lightsail Operations",
    "Description": "Limit IAM role permissions for actions such as ec2:CopySnapshot and s3:GetAccountPublicAccessBlock to only those necessary for Amazon Lightsail operations, minimizing potential attack surfaces.",
    "Applicability": "IAM roles used with Amazon Lightsail service-linked operations",
    "Security Risk": "Excess permissions increase the risk of unauthorized actions and data exposure.",
    "Default Behavior / Limitations": "Roles may by default have excessive permissions without proper configuration.",
    "Automation": "Implement least privilege access principles with AWS IAM and enforce compliance using AWS Config rules.",
    "References": [
      "https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-using-service-linked-roles.html#service-linked-role-permissions"
    ]
  }
]
```

### ControlGen Output - Arquivo 4
```json
[
  {
    "Title": "Automated Updates and Patches for Amazon Lightsail Instances and Applications",
    "Description": "Ensure Amazon Lightsail instances and applications are regularly updated and patched to mitigate vulnerabilities. Implement automated scripts or use the instance's operating system package manager (e.g., apt for Ubuntu, yum for Amazon Linux) to schedule updates and patches.",
    "Applicability": "All Amazon Lightsail instances and container services",
    "Security Risk": "Failure to regularly update and patch the operating system and applications can lead to exploitation of known vulnerabilities, resulting in unauthorized access, data breaches, or other security incidents.",
    "Default Behavior / Limitations": "AWS and Lightsail do not automatically update or patch instances after creation. It is the customer's responsibility to configure and manage updates.",
    "Automation": "Automation requires using OS-native tools (e.g., cron jobs with package managers for Linux, task scheduler for Windows) to apply security patches regularly. Manual processes must be designed and tested.",
    "References": [
      "https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-update-management.html"
    ]
  },
  {
    "Title": "Implementation of Automatic Update Services for Lightsail Applications",
    "Description": "Utilize automatic update services provided by application vendors or configure recommended update mechanisms to ensure applications running on Lightsail instances are up-to-date.",
    "Applicability": "All applications hosted on Amazon Lightsail instances",
    "Security Risk": "Unpatched applications can be prone to exploits that compromise application functionality, data integrity, or expose sensitive data.",
    "Default Behavior / Limitations": "The responsibility to enable and configure automatic updates services is on the user, as AWS does not provide automatic updates for applications on Lightsail.",
    "Automation": "Automate updates by configuring application-specific update settings or utilizing third-party update management tools that support automatic patching.",
    "References": [
      "https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-update-management.html"
    ]
  }
]
```