```json
[
  {
    "Title": "Create VPC Endpoint with IAM Policy Language",
    "Description": "Create a VPC endpoint with an attached endpoint policy in JSON format using IAM policy language that includes a 'Principal' element. Ensure the policy does not exceed 20,480 characters, including whitespace.",
    "Applicability": "All VPC endpoints created with custom policies",
    "Security Risk": "Without defining specific Principals in the policy, unauthorized access could be granted to sensitive resources.",
    "Default Behavior / Limitations": "The default policy allows full access if no custom policies are attached.",
    "Automation": "Use AWS IAM and AWS CLI to create and manage endpoint policies. Ensure policies are reviewed and monitored for compliance.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html"
    ]
  },
  {
    "Title": "Ensure Default Endpoint Policy Grants Full Access",
    "Description": "Ensure that the default endpoint policy grants full access when no explicit custom policy is attached.",
    "Applicability": "All VPC endpoints",
    "Security Risk": "If the default policy is unintentionally overridden, it could lead to unauthorized access restrictions or denial of legitimate service operations.",
    "Default Behavior / Limitations": "AWS default endpoint policy grants full access if no custom policy is attached.",
    "Automation": "Manually validate the endpoint policies to ensure compliance.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html"
    ]
  },
  {
    "Title": "Allow Full Access for Non-AWS Service VPC Endpoints by Default",
    "Description": "When creating a VPC endpoint for a non-AWS service, configure the default policy to allow full access. Modify the policy to include restrictions only if necessary.",
    "Applicability": "Non-AWS service VPC endpoints",
    "Security Risk": "Unintended access restrictions could impede service functionality or data flow.",
    "Default Behavior / Limitations": "Allowing full access by default is necessary unless specific restrictions are needed.",
    "Automation": "Review and update endpoint policies using the `modify-vpc-endpoint` AWS CLI command.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html"
    ]
  },
  {
    "Title": "Avoid Wildcards with System-Generated Identifiers in VPC Policies",
    "Description": "Ensure that your VPC endpoint policies do not use wildcard (*) or numeric condition operators with global context keys that reference system-generated identifiers.",
    "Applicability": "All VPC endpoint policies",
    "Security Risk": "Using wildcards with system identifiers may lead to broader access than intended, risking unauthorized access or data breaches.",
    "Default Behavior / Limitations": "Requires manual inspection and validation of policies.",
    "Automation": "Flag policy violations using AWS IAM Access Analyzer.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html"
    ]
  },
  {
    "Title": "Enforce Proper String Condition Usage in VPC Policies",
    "Description": "When using a string condition operator in VPC endpoint policies, include at least six consecutive characters before or after each wildcard character.",
    "Applicability": "All VPC endpoint policies utilizing string conditions",
    "Security Risk": "Improper use of string conditions can lead to overly permissive policies, increasing the risk of unauthorized access.",
    "Default Behavior / Limitations": "Manual validation is required to ensure compliance.",
    "Automation": "Monitor policy compliance using AWS IAM Access Analyzer.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html"
    ]
  },
  {
    "Title": "Gateway Endpoint Principal Configuration",
    "Description": "For gateway endpoints, set the 'Principal' to '*' and use the 'aws:PrincipalArn' key for restriction to specific principals. This provides granular access control to specified AWS resources.",
    "Applicability": "Gateway VPC endpoints",
    "Security Risk": "Misconfigured policies may allow unauthorized principal access, leading to data leakage or modification.",
    "Default Behavior / Limitations": "AWS IAM policies must be properly configured to enforce this.",
    "Automation": "Monitor and validate policy configurations using AWS Config.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html"
    ]
  },
  {
    "Title": "Use AWS CLI to Update Endpoint Policies",
    "Description": "Utilize `modify-vpc-endpoint` command in AWS CLI to update endpoint policies. This command allows for efficient updates and application of new policy versions.",
    "Applicability": "All VPC endpoints requiring policy updates",
    "Security Risk": "Outdated or incorrect policies can lead to unintended access permissions.",
    "Default Behavior / Limitations": "Policy changes may take some time to propagate. Manual verification is necessary post-implementation.",
    "Automation": "Automate policy updates using AWS CLI scripting.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html"
    ]
  },
  {
    "Title": "Restrict Gateway Endpoint Access to Root Account",
    "Description": "In gateway endpoints, specify the ‘Principal’ as ‘account_id’ to grant access solely to the root user of the AWS account. Adjust policies to accommodate other user requirements as needed.",
    "Applicability": "Gateway VPC endpoints",
    "Security Risk": "Failure to configure this may result in unauthorized access to sensitive endpoints.",
    "Default Behavior / Limitations": "Default configurations do not enforce this; manual policy configuration is necessary.",
    "Automation": "Verify implementation using AWS IAM policy simulation tools.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html"
    ]
  }
]
```