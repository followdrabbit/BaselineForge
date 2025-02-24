```json
[
  {
    "Description": "Define rules to limit parameter values users enter when launching a product by creating template constraints for AWS CloudFormation templates.",
    "Reference": "Security Best Practices for AWS Service Catalog - URL: https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security-best-practices.html",
    "Observations": "Template constraints help in maintaining control over the resources deployed and ensuring compliance with security policies."
  },
  {
    "Description": "Apply the most restrictive constraint when provisioning or updating a product. Constraints can limit instance types, e.g., allowing only t1.micro and m1.small instances.",
    "Reference": "Security Best Practices for AWS Service Catalog - URL: https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security-best-practices.html",
    "Observations": "Ensure that the constraints are defined to meet security requirements and compliance standards."
  },
  {
    "Description": "Limit user access to AWS resources by attaching an IAM policy to a launch role and using AWS Service Catalog to create a launch constraint for the role.",
    "Reference": "Security Best Practices for AWS Service Catalog - URL: https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security-best-practices.html",
    "Observations": "Creating specific launch constraints with IAM policies helps segment access control based on user roles."
  }
]
```
