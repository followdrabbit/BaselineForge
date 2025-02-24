```json
[
  {
    "Title": "Use IAM Role for EC2 Instances to Access AWS Services",
    "Description": "Ensure all Amazon EC2 instances use an IAM role that supplies temporary permissions for accessing AWS resources by configuring them through an attached instance profile.",
    "Applicability": "All EC2 instances",
    "Security Risk": "Without IAM roles, applications might require permanent credentials, increasing the risk of credential leakage and unauthorized access.",
    "Default Behavior / Limitations": "EC2 instances can run without an attached IAM role if not explicitly configured.",
    "Automation": "Enforce by creating and associating instance profiles via AWS CloudFormation templates or AWS CLI scripts.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html"
    ]
  },
  {
    "Title": "Associate Instance Profile with Auto Scaling Groups",
    "Description": "Ensure all EC2 instances in Auto Scaling groups are associated with an appropriate IAM instance profile using a launch template or launch configuration.",
    "Applicability": "EC2 instances in Auto Scaling groups",
    "Security Risk": "Without an instance profile, instances cannot assume the required IAM role, hindering their ability to securely access AWS services.",
    "Default Behavior / Limitations": "Requires manual configuration of instance profiles within launch templates or configurations.",
    "Automation": "Automate through AWS CloudFormation or by scripting AWS CLI commands to include IAM instance profiles in launch configurations.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html"
    ]
  },
  {
    "Title": "Deploy Least Privilege Principle for IAM Roles",
    "Description": "IAM roles must be constructed with permissions that are limited to the minimal functions required for the application or service to operate.",
    "Applicability": "All IAM roles",
    "Security Risk": "Excessive permissions can be exploited if credentials are compromised, leading to data exposure or resource manipulation.",
    "Default Behavior / Limitations": "AWS IAM does not mandate minimal permission constraints by default.",
    "Automation": "Use AWS IAM Access Analyzer to review and suggest least privilege policies that can be applied automatically.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html",
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html"
    ]
  },
  {
    "Title": "Ensure 'iam:PassRole' Permission in Identity-Based Policies",
    "Description": "Include the 'iam:PassRole' permission in IAM policies for roles that need to create or update Auto Scaling groups associated with an instance profile.",
    "Applicability": "IAM roles for users managing Auto Scaling groups",
    "Security Risk": "Without the 'iam:PassRole' permission, users might be unable to create resources with the intended access roles, potentially disrupting necessary integrations.",
    "Default Behavior / Limitations": "This permission must be explicitly granted in IAM policies.",
    "Automation": "Utilize IAM policy management tools or templates to include 'iam:PassRole' in relevant policies.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html"
    ]
  },
  {
    "Title": "Restrict 'iam:PassRole' to Specific Patterns",
    "Description": "Restrict which IAM roles can be passed via 'iam:PassRole' by setting a policy condition that only allows role names matching a specified pattern, e.g., 'qateam-*'.",
    "Applicability": "All IAM roles used in 'iam:PassRole'",
    "Security Risk": "Without restrictions, unauthorized roles could be assigned, leading to excessive permissions and potential security breaches.",
    "Default Behavior / Limitations": "IAM policies can allow unrestricted role passes without explicit name pattern restrictions.",
    "Automation": "Implement identity-based policies with conditions that utilize the 'iam:PassedToService' and 'StringLike' operators.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html"
    ]
  },
  {
    "Title": "Specify IAM Instance Profile in Launch Templates",
    "Description": "When creating launch templates, ensure the 'IamInstanceProfile' attribute specifies an IAM instance profile to be associated with the launched EC2 instances.",
    "Applicability": "Any environment using EC2 launch templates",
    "Security Risk": "Omission of an IAM instance profile might prevent instances from assuming required roles, affecting service functionality and security.",
    "Default Behavior / Limitations": "The 'IamInstanceProfile' attribute must be specified manually in launch templates.",
    "Automation": "Automate launch templates by using AWS CloudFormation or AWS CLI to include the necessary 'IamInstanceProfile'.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html"
    ]
  }
]
```