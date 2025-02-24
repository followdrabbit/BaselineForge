```json
[
    {
        "Title": "Enforce Usage of AWSServiceRoleForRDS for Amazon RDS",
        "Description": "Ensure the use of the AWSServiceRoleForRDS service-linked role for Amazon RDS to call AWS services on behalf of your DB clusters.",
        "Applicability": "All AWS environments using Amazon RDS",
        "Security Risk": "Without the appropriate service-linked role, RDS may not have the necessary permissions, potentially disrupting service operations.",
        "Default Behavior / Limitations": "The service-linked role is automatically created when a DB cluster is created. Manual intervention is typically not required unless restricted by IAM policies.",
        "Automation": "Manual validation required; AWS IAM automatic creation upon DB cluster instantiation ensures compliance.",
        "References": [
            "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAM.ServiceLinkedRoles.html"
        ]
    },
    {
        "Title": "Validate IAM Permissions for Creating Service-Linked Roles",
        "Description": "Ensure IAM permissions 'iam:CreateServiceLinkedRole' are properly configured to allow the creation of service-linked roles.",
        "Applicability": "Accounts using service-linked roles in Amazon RDS",
        "Security Risk": "Improper configuration could hinder service operations and automatic setup of required service-linked roles.",
        "Default Behavior / Limitations": "Does not configure by default; requires manual policy adjustments.",
        "Automation": "Can be enforced using AWS IAM policy changes and regularly audited using AWS IAM Access Analyzer.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions"
        ]
    },
    {
        "Title": "Restrict Editing of AWSServiceRoleForRDS",
        "Description": "Deny editing permissions for the AWSServiceRoleForRDS service-linked role to maintain system integrity.",
        "Applicability": "All AWS accounts using Amazon RDS",
        "Security Risk": "Allowing edits to critical roles can lead to unauthorized changes and potential security breaches.",
        "Default Behavior / Limitations": "Role name changing is restricted by default, but the description can be modified.",
        "Automation": "Can be enforced using IAM policies to deny edit actions on the service-linked role.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role"
        ]
    },
    {
        "Title": "Verify Deletion of DB Clusters Before Removing AWSServiceRoleForRDS",
        "Description": "Implement checks to ensure all DB clusters are deleted before attempting to delete the AWSServiceRoleForRDS service-linked role.",
        "Applicability": "AWS accounts decommissioning RDS environments",
        "Security Risk": "Deleting the service-linked role while clusters are active could disrupt service operations.",
        "Default Behavior / Limitations": "Manual checks are necessary; no native AWS enforcement for active session detections.",
        "Automation": "Manual validation required; potentially use AWS Lambda functions to automate pre-deletion checks.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role"
        ]
    },
    {
        "Title": "Apply AmazonRDSServiceRolePolicy to Service-Linked Roles",
        "Description": "Attach the AmazonRDSServiceRolePolicy to service-linked roles to ensure necessary permissions are granted.",
        "Applicability": "All AWS accounts utilizing RDS with service-linked roles",
        "Security Risk": "Incorrect permissions could lead to operational failures or inadequate security postures.",
        "Default Behavior / Limitations": "Must be manually reviewed and applied; not automatically configured.",
        "Automation": "Can be monitored using AWS IAM Access Analyzer and enforced through AWS IAM policies.",
        "References": [
            "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRDSServiceRolePolicy.html"
        ]
    },
    {
        "Title": "Allow rds.amazonaws.com to Assume Service-Linked Roles",
        "Description": "Ensure that only rds.amazonaws.com is allowed to assume service-linked roles such as AWSServiceRoleForRDS, AWSServiceRoleForRDSBeta, and AWSServiceRoleForRDSPreview.",
        "Applicability": "All RDS environments using service-linked roles",
        "Security Risk": "Incorrect trust relationships could lead to unauthorized access or role assumptions.",
        "Default Behavior / Limitations": "Trust relationships need to be manually verified; not inherently enforced.",
        "Automation": "Can be enforced using IAM trust policy configurations and audited via AWS IAM Access Analyzer.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions"
        ]
    }
]
```