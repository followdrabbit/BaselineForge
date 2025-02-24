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