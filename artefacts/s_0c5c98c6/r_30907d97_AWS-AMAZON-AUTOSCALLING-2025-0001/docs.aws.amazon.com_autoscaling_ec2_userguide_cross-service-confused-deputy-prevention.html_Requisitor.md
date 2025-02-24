```json
[
  {
    "Description": "Use `aws:SourceArn` and `aws:SourceAccount` global condition keys in trust policies for Amazon EC2 Auto Scaling service roles to prevent cross-service confused deputy problem.",
    "Reference": "Section 1 - Example: Using `aws:SourceArn` and `aws:SourceAccount` condition keys. URL: https://docs.aws.amazon.com/autoscaling/ec2/userguide/cross-service-confused-deputy-prevention.html",
    "Observations": "The condition keys should limit permissions given by Amazon EC2 Auto Scaling to resources of a specific account. AWS STS is used for assuming roles."
  },
  {
    "Description": "Set the `aws:SourceArn` value to the specific Amazon Resource Name (ARN) for better specificity, or use an ARN pattern with wildcards (`*`) if portions are unknown.",
    "Reference": "Section 1 - Using `aws:SourceArn` and `aws:SourceAccount` condition keys. URL: https://docs.aws.amazon.com/autoscaling/ec2/userguide/cross-service-confused-deputy-prevention.html",
    "Observations": "Prefer `aws:SourceArn` over `aws:SourceAccount` when possible for higher specificity."
  },
  {
    "Description": "Ensure service role's trust policy uses condition statements to limit `AssumeRole` capability to specified Auto Scaling group within a specified account.",
    "Reference": "Section 1 - Example policy JSON snippet. URL: https://docs.aws.amazon.com/autoscaling/ec2/userguide/cross-service-confused-deputy-prevention.html",
    "Observations": "Replace Region, account ID, UUID, and group name with valid values specific to your account."
  }
]
```