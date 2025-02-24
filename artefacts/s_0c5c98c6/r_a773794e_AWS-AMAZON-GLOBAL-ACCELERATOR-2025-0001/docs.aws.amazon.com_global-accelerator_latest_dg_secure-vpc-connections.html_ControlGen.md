```json
[
  {
    "Title": "Ensure VPC has Internet Gateway for AWS Global Accelerator",
    "Description": "Attach an internet gateway to any VPC containing a Network Load Balancer, internal Application Load Balancer, or Amazon EC2 instance used as AWS Global Accelerator endpoints, to enable acceptance of internet traffic.",
    "Applicability": "All VPCs containing AWS Global Accelerator endpoints",
    "Security Risk": "Without an internet gateway, AWS Global Accelerator cannot route internet traffic to the intended endpoints, potentially leading to loss of connectivity or service unavailability.",
    "Default Behavior / Limitations": "AWS does not automatically attach an internet gateway to VPCs. This requires manual configuration.",
    "Automation": "Can be enforced using AWS Config rule `vpc-gateway-attached` to ensure an internet gateway is attached to the target VPC.",
    "References": [
      "https://docs.aws.amazon.com/global-accelerator/latest/dg/secure-vpc-connections.html",
      "https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html"
    ]
  },
  {
    "Title": "Use Private Subnets for Amazon EC2 Instances with AWS Global Accelerator",
    "Description": "Configure Amazon EC2 instances within private subnets to ensure that all traffic directed by AWS Global Accelerator is managed efficiently through security groups.",
    "Applicability": "All deployments using AWS Global Accelerator with Amazon EC2 instances",
    "Security Risk": "Publicly accessible instances in public subnets may expose vulnerabilities and increase the attack surface.",
    "Default Behavior / Limitations": "AWS provides the capability to use private subnets, but configuration must be done manually. Routing and security group configurations are not automatically enforced.",
    "Automation": "Manual validation required for subnet configuration. Use AWS Config rules to ensure instances do not have public IPs.",
    "References": [
      "https://docs.aws.amazon.com/global-accelerator/latest/dg/secure-vpc-connections.html",
      "https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html"
    ]
  },
  {
    "Title": "Review IAM Policies for Network Perimeter Configurations",
    "Description": "Review and configure IAM policies to account for permissions affecting internet access and network perimeter security, ensuring compliance with organizational security postures.",
    "Applicability": "IAM roles managing VPC configurations and internet access",
    "Security Risk": "Improper IAM policies may allow unauthorized changes to network configurations, potentially exposing internal resources to the internet.",
    "Default Behavior / Limitations": "IAM permissions related to network configurations are not explicitly managed by default and require detailed policy setup.",
    "Automation": "Manual validation required. Regular IAM policy reviews and audits can be performed using AWS IAM Access Analyzer and AWS Config rules.",
    "References": [
      "https://docs.aws.amazon.com/global-accelerator/latest/dg/secure-vpc-connections.html",
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html"
    ]
  }
]
```