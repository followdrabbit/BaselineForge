```json
[
  {
    "Title": "Enforce IAM Authentication and Authorization for Amazon SWF",
    "Description": "Ensure that all requests to Amazon Simple Workflow Service (SWF) require authentication using AWS Identity and Access Management (IAM). Configure IAM policies that specify the necessary permissions for each user or role to access SWF resources. This includes defining actions, resources, and conditions in the IAM policies.",
    "Applicability": "All users and roles accessing Amazon SWF",
    "Security Risk": "Without authenticated requests and properly defined permissions, unauthorized access could occur, leading to potential data loss or service disruption.",
    "Default Behavior / Limitations": "IAM requires explicit permission grants; no permissions are provided by default.",
    "Automation": "Can be enforced using AWS IAM policies and monitored via AWS IAM Access Analyzer.",
    "References": [
      "https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html"
    ]
  },
  {
    "Title": "Configure IAM Policies for Amazon SWF Access",
    "Description": "Administrators must create and attach IAM policies that explicitly grant the necessary actions on Amazon SWF resources. These policies should detail the specific actions, resources, and conditions applicable to the IAM entities.",
    "Applicability": "IAM Administrators configuring access for Amazon SWF",
    "Security Risk": "Improperly configured IAM policies might permit unauthorized access or deny necessary access, potentially impacting operational efficiency and security.",
    "Default Behavior / Limitations": "IAM policies must be explicitly created and attached; there are no default permissions.",
    "Automation": "Can be configured manually; policy configuration can be audited using AWS Config rules.",
    "References": [
      "https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html"
    ]
  },
  {
    "Title": "Implement Centralized Access Management with AWS Identity Center",
    "Description": "Use AWS Identity Center to manage user identities and access to AWS resources, including SWF, leveraging temporary security credentials for all AWS access. Configure identity federation as needed to streamline user management and access provisioning.",
    "Applicability": "Organizations using AWS Identity Center for centralized access management",
    "Security Risk": "Failing to utilize centralized access increases administrative overhead and the likelihood of outdated or over-permissive access rights.",
    "Default Behavior / Limitations": "Centralized identity management is not enforced by default; requires setup and configuration.",
    "Automation": "AWS Identity Center can be configured for centralized management and is managed through the AWS Management Console.",
    "References": [
      "https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html"
    ]
  },
  {
    "Title": "Regularly Rotate Access Keys for IAM Users",
    "Description": "Implement automated mechanisms to rotate access keys for IAM users regularly to minimize the risk of compromised credentials. Leverage AWS Lambda or AWS Secrets Manager for automated key rotation where possible.",
    "Applicability": "All IAM users using long-term credentials",
    "Security Risk": "Stale or unrotated access keys pose a significant security risk, as they may be vulnerable to compromise and unauthorized access.",
    "Default Behavior / Limitations": "AWS does not automatically rotate access keys; manual or automated solutions must be implemented.",
    "Automation": "Automate using AWS Lambda functions or leverage AWS Secrets Manager's automatic key rotation.",
    "References": [
      "https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html"
    ]
  },
  {
    "Title": "Define IAM Policy Components for Amazon SWF",
    "Description": "Ensure all IAM policies for Amazon SWF include specific principals, actions, resources, and conditions as needed to achieve least privilege access control. Regularly review and update policies to reflect changes in business requirements or AWS configurations.",
    "Applicability": "IAM policies governing access to Amazon SWF",
    "Security Risk": "Undefined or misconfigured policy components can lead to over-permissive access or denial of legitimate access requests.",
    "Default Behavior / Limitations": "IAM policies require manual configuration to include necessary components.",
    "Automation": "Manual validation required; policies should be reviewed using AWS IAM Access Analyzer for compliance.",
    "References": [
      "https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html"
    ]
  },
  {
    "Title": "Implement Attribute-Based Access Control (ABAC) with Amazon SWF",
    "Description": "Leverage ABAC by using tags on resources and IAM policies to control access based on these tags, implementing fine-grained permissions management and ensuring the secure handling of Amazon SWF operations.",
    "Applicability": "Taggable resources within Amazon SWF",
    "Security Risk": "Without proper tagging and ABAC implementation, managing complex access permissions becomes cumbersome and error-prone, leading to potential security breaches.",
    "Default Behavior / Limitations": "ABAC requires tagging resources and configuring IAM policies accordingly; not automatically enforced.",
    "Automation": "Manual validation required; tagging can be implemented through AWS Tag Editor.",
    "References": [
      "https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html"
    ]
  },
  {
    "Title": "Utilize Service Roles for Delegated Permissions in Amazon SWF",
    "Description": "Deploy service roles to delegate necessary permissions within Amazon SWF, ensuring that workflows and tasks can operate within the defined security boundaries. Regular audit of service role configurations should be conducted to prevent unauthorized changes.",
    "Applicability": "Amazon SWF workflows and tasks requiring delegated permissions",
    "Security Risk": "Improper configuration of service roles can lead to breakdowns in workflow execution and potential security vulnerabilities.",
    "Default Behavior / Limitations": "Service roles must be explicitly created and managed; defaults do not apply.",
    "Automation": "Enforced using IAM roles setup manually; automated change detection can be monitored using AWS Config.",
    "References": [
      "https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html"
    ]
  }
]
```