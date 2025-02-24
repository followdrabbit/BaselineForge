```json
[
  {
    "Title": "Implement Global Condition Keys 'aws:SourceArn' and 'aws:SourceAccount' in EC2 Auto Scaling Trust Policies",
    "Description": "In trust policies for Amazon EC2 Auto Scaling service roles, specify the use of 'aws:SourceArn' and 'aws:SourceAccount' global condition keys. These condition keys should restrict permissions to specific resources within an account, thereby preventing cross-service confused deputy problems through AWS Security Token Service (STS).",
    "Applicability": "Amazon EC2 Auto Scaling roles",
    "Security Risk": "Without these condition keys, there is a risk of cross-service attacks where a misconfigured policy allows unauthorized actions, leading to potential breaches or undesired operations within AWS resources.",
    "Default Behavior / Limitations": "AWS does not enforce these conditions by default; they must be explicitly set in the policy.",
    "Automation": "Can be enforced using AWS IAM policy editing via the IAM console or by using an infrastructure as code tool such as AWS CloudFormation or Terraform with IAM policies configured to include these condition keys.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/cross-service-confused-deputy-prevention.html"
    ]
  },
  {
    "Title": "Use Specific 'aws:SourceArn' in Service Role Trust Policies",
    "Description": "To enhance specificity in trust policies, configure the 'aws:SourceArn' global condition key to a specific Amazon Resource Name (ARN). If exact details aren't available, use a pattern with wildcards ('*') judiciously to prevent over-permissioning.",
    "Applicability": "Amazon EC2 Auto Scaling roles",
    "Security Risk": "Using broad ARNs or omitting them entirely increases the risk of unauthorized cross-account or cross-service API call executions, potentially leading to privilege escalation or resource access.",
    "Default Behavior / Limitations": "AWS IAM policies do not automatically enforce specific ARNs; detailed configuration is required.",
    "Automation": "Manual validation is required for precise ARN specification unless using automation tools like AWS CloudFormation to define ARNs programmatically.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/cross-service-confused-deputy-prevention.html"
    ]
  },
  {
    "Title": "Limit AssumeRole Capability in Service Role Trust Policies to Specific Auto Scaling Group",
    "Description": "Configure service role trust policies to include condition statements that restrict the 'AssumeRole' capability to a specific Auto Scaling group within a designated AWS account. Specify relevant values such as Region, account ID, UUID, and group name accurately.",
    "Applicability": "Amazon EC2 Auto Scaling roles",
    "Security Risk": "Neglecting to set these condition statements could allow unauthorized role assumption, making the account vulnerable to privilege misuse or compromise.",
    "Default Behavior / Limitations": "Service roles do not enforce such specificity without manual policy customization.",
    "Automation": "This can be automated by incorporating precise IAM policies in AWS CloudFormation templates or using IAM policy editing via scripts in AWS CLI or SDKs.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/cross-service-confused-deputy-prevention.html"
    ]
  }
]
```