```json
[
  {
    "Title": "Ensure Every EC2 Instance is Associated with a Security Group",
    "Description": "All EC2 instances in a VPC must be associated with at least one security group. Security groups act as a virtual firewall to control the inbound and outbound traffic to and from the instance.",
    "Applicability": "All EC2 instances within a VPC",
    "Security Risk": "Without a security group, instances may be exposed to unintended inbound and outbound traffic, increasing the risk of unauthorized access and data breaches.",
    "Default Behavior / Limitations": "By default, an EC2 instance gets associated with the VPC's default security group if no specific security group is mentioned.",
    "Automation": "Can be monitored using AWS Config rule `ec2-instance-no-associated-security-group` to ensure each instance is associated with a security group.",
    "References": [
      "https://docs.aws.amazon.com/vpc-security-groups.html"
    ]
  },
  {
    "Title": "Configure Network ACLs to Control Subnet Traffic",
    "Description": "Network Access Control Lists (ACLs) must be configured to explicitly allow or deny specific inbound and outbound traffic at the subnet level in a VPC.",
    "Applicability": "All subnets within a VPC",
    "Security Risk": "Improperly configured network ACLs can lead to unauthorized access or unintended blocking of legitimate traffic, impacting the confidentiality and availability of resources.",
    "Default Behavior / Limitations": "Network ACLs are stateless and must be manually defined for specific traffic requirements.",
    "Automation": "Manual validation required. Currently, there is no direct AWS Config rule for managing specific network ACL configurations, thus requiring periodic review and updates as network requirements change.",
    "References": [
      "https://docs.aws.amazon.com/vpc-network-acls.html"
    ]
  },
  {
    "Title": "Enable VPC Flow Logs to Capture VPC Network Traffic",
    "Description": "VPC Flow Logs must be enabled for all VPCs to capture IP traffic going to and from network interfaces, which can be useful for monitoring traffic patterns and troubleshooting.",
    "Applicability": "All VPCs",
    "Security Risk": "Without VPC Flow Logs, it is difficult to track and analyze IP traffic, potentially hindering the detection of suspicious activities and troubleshooting.",
    "Default Behavior / Limitations": "VPC Flow Logs are not enabled by default and must be explicitly configured either to stream to Amazon CloudWatch Logs or Amazon S3.",
    "Automation": "Can be enforced using AWS Config rule `vpc-flow-logs-enabled` to ensure that flow logs are enabled for the entire VPC.",
    "References": [
      "https://docs.aws.amazon.com/vpc/flow-logs.html"
    ]
  },
  {
    "Title": "Implement Traffic Mirroring for Network Monitoring",
    "Description": "Traffic Mirroring should be enabled to copy network traffic from the elastic network interface of specific EC2 instances for detailed monitoring and analysis by security tools.",
    "Applicability": "Select EC2 instances with high security or monitoring requirements",
    "Security Risk": "Without traffic mirroring, potential threats in the network traffic cannot be identified and analyzed in real time, increasing the likelihood of undetected intrusions.",
    "Default Behavior / Limitations": "Traffic Mirroring is not enabled by default and requires configuration specifying the source and target ENIs.",
    "Automation": "Manual validation required. AWS currently does not provide automation support through AWS Config for verifying traffic mirroring configurations; it must be manually set in the VPC console.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/mirroring/"
    ]
  }
]
```