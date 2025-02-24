```json
[
  {
    "Title": "Restrict VPC Endpoint Policies to Avoid Full Access",
    "Description": "Ensure VPC endpoint policies do not use the wildcard '*' in the 'Principal' element without appropriate 'Condition' clauses to limit access. This prevents full, unrestricted access to the VPC endpoint.",
    "Applicability": "All AWS accounts with VPC endpoints",
    "Security Risk": "Allowing full access using wildcard principals can lead to unauthorized access to resources, potential data exposure, and unexpected charges.",
    "Default Behavior / Limitations": "AWS does not automatically restrict the 'Principal' element in VPC endpoint policies. It must be manually configured by the user.",
    "Automation": "Can be monitored using AWS Config with custom configuration rules or AWS Security Hub for policy misconfigurations.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/endpoint-exposed.html",
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html"
    ]
  },
  {
    "Title": "Automate Audits of VPC Endpoint Policies for Secure Configuration",
    "Description": "Regularly audit VPC endpoint policies to ensure the 'Principal' element is not set to '*' without conditions. Use AWS Config rules or Security Hub for regular auditing across all AWS regions.",
    "Applicability": "All AWS accounts with VPC endpoints",
    "Security Risk": "Without regular audits, configuration drifts might go unnoticed, leading to potential security vulnerabilities and unauthorized access.",
    "Default Behavior / Limitations": "AWS does not provide automatic auditing of VPC endpoint policies by default; it must be configured using AWS Config or Security Hub.",
    "Automation": "Can be audited using AWS Config with custom rules and AWS Security Hub integration for continuous compliance checks.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/endpoint-exposed.html",
      "https://docs.aws.amazon.com/cli/latest/userguide/cli-services-vpce.html"
    ]
  },
  {
    "Title": "Update VPC Endpoint Policies to Restrict Access",
    "Description": "Use AWS CloudFormation templates or AWS CLI to modify VPC endpoint policies, replacing wildcard principals with specified trusted entities. Ensure updates are deployed to all relevant endpoints across regions.",
    "Applicability": "All AWS accounts configuring VPC endpoint policies",
    "Security Risk": "Improperly configured policies with wildcard principals can lead to unauthorized access, data leaks, and unanticipated costs.",
    "Default Behavior / Limitations": "AWS does not enforce restriction on principals; manual updates are necessary.",
    "Automation": "Can be enforced and deployed using AWS CloudFormation for infrastructure as code and audited via AWS Config for compliance.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/endpoint-exposed.html",
      "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html"
    ]
  }
]
```