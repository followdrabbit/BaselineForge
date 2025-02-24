```json
[
  {
    "Title": "Restrict EC2 Instance Launch to Specific Tagged Templates",
    "Description": "IAM policy must restrict the `ec2:RunInstances` action to only those launch templates with the tag `purpose=testing`. Configure a resource-based policy to enforce this constraint.",
    "Applicability": "All AWS accounts managing EC2 instances through launch templates",
    "Security Risk": "If not enforced, EC2 instances can be launched using unintended or insecure configurations, leading to misconfigurations and potential security gaps.",
    "Default Behavior / Limitations": "By default, AWS allows launching instances with any template. Tag-based access must be explicitly configured.",
    "Automation": "Can be enforced via IAM policies using condition keys such as `aws:RequestTag/purpose` and `aws:TagKeys`.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-launch-template-permissions.html"
    ]
  },
  {
    "Title": "Enforce Launch Template and Version Specification for Auto Scaling",
    "Description": "IAM policies must require a launch template and its version number to be specified when creating or updating Auto Scaling groups. This prevents omitting version numbers, which can cause failures.",
    "Applicability": "All AWS accounts using Auto Scaling groups",
    "Security Risk": "Without specifying a launch template and version, there is a risk of using unintended configurations, potentially leading to errors and vulnerabilities.",
    "Default Behavior / Limitations": "AWS does not enforce this by default; users must specify this requirement in IAM policies.",
    "Automation": "Can be enforced using service control policies (SCPs) or IAM policies with condition keys to verify that both template and version are specified.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-launch-template-permissions.html"
    ]
  },
  {
    "Title": "Require IMDSv2 for EC2 Instance Launches",
    "Description": "Deny `ec2:RunInstances` permissions unless the instance is configured with `ec2:MetadataHttpTokens:required` to ensure the use of Instance Metadata Service Version 2 (IMDSv2).",
    "Applicability": "All AWS accounts launching EC2 instances",
    "Security Risk": "Using IMDSv1 exposes instances to potential metadata theft; IMDSv2 provides improved security via required token usage.",
    "Default Behavior / Limitations": "AWS allows instances to run with IMDSv1 unless manually restricted.",
    "Automation": "Can be enforced using IAM policies and condition keys to require the `ec2:MetadataHttpTokens:required` configuration.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-launch-template-permissions.html"
    ]
  },
  {
    "Title": "Allow Tagging of EC2 Instances and Volumes at Creation",
    "Description": "Provide users with the `ec2:CreateTags` permission to add tags to instances and volumes at the time of their creation.",
    "Applicability": "All AWS accounts using EC2 instances and volumes",
    "Security Risk": "Without proper tagging capabilities, it becomes challenging to manage and identify resources, potentially leading to compliance and management issues.",
    "Default Behavior / Limitations": "AWS IAM does not automatically allow users to create tags; permissions must be deliberately set.",
    "Automation": "Configurable via IAM policies by granting `ec2:CreateTags` permission.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-launch-template-permissions.html"
    ]
  },
  {
    "Title": "Grant Permissions for Describing Launch Templates",
    "Description": "Ensure users have `ec2:DescribeLaunchTemplates` and `ec2:DescribeLaunchTemplateVersions` permissions to utilize launch templates in the Auto Scaling wizard.",
    "Applicability": "All AWS accounts employing Auto Scaling groups",
    "Security Risk": "Without necessary permissions, users cannot access or use launch template features, impacting operational efficiency.",
    "Default Behavior / Limitations": "AWS requires explicit permissions for these actions; it is not granted by default.",
    "Automation": "Managed through IAM policies granting describe permissions.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-launch-template-permissions.html"
    ]
  },
  {
    "Title": "Validate Permissions Using Dry Run for Launch Templates",
    "Description": "IAM policies must ensure validation of permissions for `ec2:RunInstances` and `iam:PassRole` through a dry run of the specified launch template version.",
    "Applicability": "All AWS accounts running EC2 instances via IAM-managed launch templates",
    "Security Risk": "Without a dry run, permission misconfigurations may go unnoticed, leading to unauthorized actions or failed operations.",
    "Default Behavior / Limitations": "Dry run is not enabled by default; it must be specified during permission setup.",
    "Automation": "Can be enforced using IAM policy conditions to check permissions during a dry run.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-launch-template-permissions.html"
    ]
  },
  {
    "Title": "Restrict Access to Specific Launch Template Versions",
    "Description": "Use the `autoscaling:LaunchTemplateVersionSpecified` condition key to restrict access to only $Latest or $Default launch template versions.",
    "Applicability": "All AWS environments managing EC2 instances with launch templates",
    "Security Risk": "Access to unintended launch template versions can introduce outdated configurations, leading to potential vulnerabilities or operational failures.",
    "Default Behavior / Limitations": "AWS defaults do not restrict launch template versioning; explicit restrictions must be configured.",
    "Automation": "Enforced via IAM or SCP conditions by specifying the key `autoscaling:LaunchTemplateVersionSpecified`.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-launch-template-permissions.html"
    ]
  }
]
```