```json
[
  {
    "Title": "Implement Template Constraints for AWS CloudFormation",
    "Description": "Create template constraints within AWS Service Catalog for CloudFormation templates to control parameter values that users can enter when launching resources. These constraints ensure compliance with organizational security policies by enforcing a set of allowable values and limits, such as instance types, AMI IDs, and key pairs.",
    "Applicability": "All products and services deployed via AWS Service Catalog in the organization",
    "Security Risk": "Without template constraints, users may deploy resources that don't comply with security policies, resulting in potential exposure to security vulnerabilities and non-compliance with regulatory requirements.",
    "Default Behavior / Limitations": "AWS CloudFormation templates do not have constraints by default; they must be specified manually in the Service Catalog.",
    "Automation": "Can be enforced by configuring template constraints in AWS Service Catalog portfolios and products.",
    "References": [
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security-best-practices.html"
    ]
  },
  {
    "Title": "Apply Restrictive Constraints for Product Provisioning in AWS Service Catalog",
    "Description": "Define and apply the most restrictive constraints when provisioning or updating a product within AWS Service Catalog. For example, restrict instance types to a predefined list such as 't1.micro' and 'm1.small' to ensure cost-effective and secure deployments.",
    "Applicability": "All products and services provisioned via AWS Service Catalog",
    "Security Risk": "Lack of restrictive constraints can lead to unexpected resource usage, increased costs, and deployment of non-compliant resources that pose security risks.",
    "Default Behavior / Limitations": "Constraints must be defined manually; no default restrictions are applied.",
    "Automation": "Constraint enforcement is managed through AWS Service Catalog configurations.",
    "References": [
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security-best-practices.html"
    ]
  },
  {
    "Title": "Limit User Access to Resources with IAM Policies and Launch Constraints",
    "Description": "Attach a restrictive IAM policy to a launch role and utilize AWS Service Catalog to create launch constraints for roles to limit user access to AWS resources. This establishes role-based access control (RBAC), segmenting access according to user roles and permissions.",
    "Applicability": "All roles used to provision products via AWS Service Catalog",
    "Security Risk": "Failure to limit user access can result in unauthorized access to AWS resources, leading to potential data breaches and unauthorized modifications or deletions.",
    "Default Behavior / Limitations": "IAM policies provide the mechanism to enforce role-based access control but must be appropriately configured.",
    "Automation": "Role-based access controls can be enforced through IAM policies and AWS Service Catalog launch constraints.",
    "References": [
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security-best-practices.html"
    ]
  }
]
```