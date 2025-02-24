```json
[
  {
    "Title": "Enforce VPC Block Public Access (BPA) Across All AWS Accounts",
    "Description": "Enable VPC Block Public Access to prevent public internet access to VPC resources across all AWS accounts. Ensure that BPA is configured at the AWS Organization level and applied to every VPC by default to restrict any unintended public exposure.",
    "Applicability": "All AWS accounts within an AWS Organization",
    "Security Risk": "Public access to VPC resources can expose sensitive data to unauthorized access, leading to potential data breaches.",
    "Default Behavior / Limitations": "VPC BPA needs to be manually implemented; AWS does not enforce it by default.",
    "Automation": "Can be enforced using AWS Organization Service Control Policies (SCP) and AWS Config rule `vpc-no-public-subnets`.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html"
    ]
  },
  {
    "Title": "Enforce 'Bidirectional' VPC BPA Mode",
    "Description": "Configure VPC Block Public Access (BPA) in 'Bidirectional' mode to block all inbound and outbound traffic through internet gateways and egress-only internet gateways for specified non-essential VPCs and subnets.",
    "Applicability": "All non-essential VPCs and subnets within AWS accounts",
    "Security Risk": "Without proper control, VPC resources can inadvertently communicate with the internet, leading to data exfiltration or exposure.",
    "Default Behavior / Limitations": "Requires explicit configuration; AWS does not automatically enforce bidirectional blocking.",
    "Automation": "Manual validation required to ensure correct configuration in bidirectional mode; can use AWS Config to monitor subnet configurations.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html"
    ]
  },
  {
    "Title": "Configure VPC BPA in 'Ingress-only' Mode",
    "Description": "Configure VPC Block Public Access (BPA) in 'Ingress-only' mode to block all inbound traffic from the internet while allowing necessary outbound traffic to NAT gateways and egress-only internet gateways as required.",
    "Applicability": "AWS VPCs requiring restricted inbound access with necessity for specific outbound traffic",
    "Security Risk": "Unrestricted inbound traffic can lead to unauthorized access and attacks on the network.",
    "Default Behavior / Limitations": "AWS does not enforce ingress-only blocking by default; requires deliberate setup.",
    "Automation": "Enforceable using AWS Config rules for monitoring; manual configuration required to define ingress-only mode.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html"
    ]
  },
  {
    "Title": "Manage VPC BPA Exclusions",
    "Description": "Set up exclusions for specific VPCs or subnets to enable allowed traffic modes such as 'Bidirectional' or 'Egress-only'. Ensure periodic audits of exclusion lists to verify justifications and necessity.",
    "Applicability": "Specific VPCs or subnets requiring exceptions to default BPA configurations",
    "Security Risk": "Unjustified exclusions can permit unwanted traffic, potentially compromising network security.",
    "Default Behavior / Limitations": "Exclusions must be managed manually as AWS does not automatically audit these exceptions.",
    "Automation": "Requires manual validation and periodic auditing of exclusions; use AWS IAM policies to restrict modification access.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html"
    ]
  }
]
```