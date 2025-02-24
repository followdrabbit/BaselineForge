```json
[
  {
    "Title": "Automatic Creation of Service-Linked Role for AWS Application Migration Service",
    "Description": "AWS Application Migration Service automatically creates the service-linked role `AWSServiceRoleForApplicationMigrationService` when configuring the Replication Configuration Template. This role is managed by AWS, eliminating the need for manual role creation.",
    "Applicability": "AWS Application Migration Service users",
    "Security Risk": "Manual role creation could introduce configuration errors, leading to potential security flaws or service outages.",
    "Default Behavior / Limitations": "The service-linked role is automatically created by AWS, and users cannot alter this behavior.",
    "Automation": "This control is enforced automatically by AWS when using the service. Monitoring is not required.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/using-service-linked-roles.html"
    ]
  },
  {
    "Title": "Immutable Name for AWS Service-Linked Role",
    "Description": "The name of the service-linked role `AWSServiceRoleForApplicationMigrationService` cannot be modified after creation, though its description can be edited.",
    "Applicability": "AWS Application Migration Service users",
    "Security Risk": "Changing role names can disrupt service operations and lead to unauthorized access if not tracked correctly.",
    "Default Behavior / Limitations": "AWS enforces this restriction automatically, maintaining role integrity.",
    "Automation": "AWS manages this automatically, and no configuration is needed from the user.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/using-service-linked-roles.html"
    ]
  },
  {
    "Title": "Service-Linked Role Permissions Management",
    "Description": "The `AWSServiceRoleForApplicationMigrationService` includes permissions for services like EC2, IAM, KMS, and Organizations. It assumes trust for `mgn.amazonaws.com` and contains various permissions related to AWS resources.",
    "Applicability": "AWS Application Migration Service users",
    "Security Risk": "Incorrect permissions could allow unauthorized actions on AWS resources, impacting confidentiality, integrity, or availability.",
    "Default Behavior / Limitations": "Permission updates on service-linked roles are managed by AWS.",
    "Automation": "AWS manages role permissions automatically. Users should review IAM policies regularly.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/using-service-linked-roles.html"
    ]
  },
  {
    "Title": "Conditional Deletion of Service-Linked Role",
    "Description": "Before deleting the `AWSServiceRoleForApplicationMigrationService`, all associated AWS resources (waves, applications, source servers, and jobs) must be cleaned up in every AWS region to ensure permissions are not inadvertently removed.",
    "Applicability": "AWS Application Migration Service users",
    "Security Risk": "Premature deletion of the service-linked role can lead to orphaned resources and unintentional data exposure or loss.",
    "Default Behavior / Limitations": "AWS does not automatically handle the cleanup of associated resources before role deletion.",
    "Automation": "Manual validation is required to ensure all resources are removed before role deletion.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/using-service-linked-roles.html"
    ]
  },
  {
    "Title": "Restriction of EC2 Actions Based on Resource Tagging",
    "Description": "The permissions policy for `AWSServiceRoleForApplicationMigrationService` allows actions like `StartInstances`, `StopInstances`, and `TerminateInstances` on EC2, except when the resource tag `AWSApplicationMigrationServiceManaged` is true.",
    "Applicability": "AWS Application Migration Service users",
    "Security Risk": "Allowing unrestricted actions on EC2 instances can lead to unauthorized changes affecting system availability and data integrity.",
    "Default Behavior / Limitations": "Tag-based permissions are enforced automatically within the role's policy.",
    "Automation": "AWS IAM policies inherently support this through policy definitions. Monitoring through AWS Config for compliance is recommended.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/using-service-linked-roles.html"
    ]
  },
  {
    "Title": "Conditional EC2 Resource Creation by Request Tags",
    "Description": "The `AWSServiceRoleForApplicationMigrationService` includes permissions to create EC2 resources such as volumes and security groups, with conditions based on request tags.",
    "Applicability": "AWS Application Migration Service users",
    "Security Risk": "Unrestricted resource creation can lead to misconfigurations or unexpected costs impacting the security and budget of the organization.",
    "Default Behavior / Limitations": "Request tag conditioning is natively supported in IAM and enforced by AWS.",
    "Automation": "AWS IAM policies enable this control inherently. Additional monitoring can be configured using AWS Config.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/using-service-linked-roles.html"
    ]
  }
]
```