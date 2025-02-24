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