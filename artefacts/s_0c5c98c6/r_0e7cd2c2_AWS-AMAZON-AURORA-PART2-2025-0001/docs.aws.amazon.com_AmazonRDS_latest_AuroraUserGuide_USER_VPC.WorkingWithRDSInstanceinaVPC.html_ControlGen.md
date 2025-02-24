```json
[
  {
    "Title": "Ensure VPC has Subnets across Multiple Availability Zones",
    "Description": "Deploy the Amazon Aurora DB cluster in a VPC that contains at least two subnets across different Availability Zones to ensure high availability.",
    "Applicability": "All Amazon Aurora DB clusters in AWS",
    "Security Risk": "Without multiple availability zones, a failure in one zone could lead to database inaccessibility, affecting availability and resilience.",
    "Default Behavior / Limitations": "AWS does not enforce this automatically; users must configure subnets correctly.",
    "Automation": "Can be enforced using AWS CloudFormation by specifying 'AvailabilityZones' parameter for VPC. AWS Config can monitor using custom rules for VPC configuration.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.VPC.html"
    ]
  },
  {
    "Title": "Configure DB Subnet Groups with Multiple Availability Zones",
    "Description": "Ensure DB subnet groups contain subnets in at least two Availability Zones within an AWS Region for fault tolerance.",
    "Applicability": "All Amazon Aurora DB subnet groups",
    "Security Risk": "Single availability zone failure could result in loss of database connectivity.",
    "Default Behavior / Limitations": "AWS requires configuration; there is no automatic enforcement of multiple availability zones.",
    "Automation": "Managed via AWS CloudFormation template definitions for subnet groups. AWS Config can report compliance using custom rules.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_VPC.Scenarios.html"
    ]
  },
  {
    "Title": "Enable DNS Hostnames and DNS Resolution in VPC",
    "Description": "For public accessibility, ensure 'DNS hostnames' and 'DNS resolution' are enabled in the VPC.",
    "Applicability": "Amazon Aurora DB clusters requiring public access",
    "Security Risk": "Disabling DNS settings can prevent public endpoint resolution, causing network accessibility issues.",
    "Default Behavior / Limitations": "These settings are not enabled by default for all VPCs and must be configured.",
    "Automation": "Configured via AWS CLI or AWS Management Console. Monitoring via AWS Config custom rules.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html"
    ]
  },
  {
    "Title": "Allocate Adequate CIDR Blocks for Subnets",
    "Description": "Ensure subnets have sufficiently large CIDR blocks to accommodate spare IP addresses needed during maintenance.",
    "Applicability": "All subnets in Amazon Aurora deployments",
    "Security Risk": "Insufficient IP addresses could lead to resource exhaustion, affecting service availability during maintenance.",
    "Default Behavior / Limitations": "AWS does not automatically manage subnet CIDR block sizes.",
    "Automation": "Configured using AWS CloudFormation for initial setup. AWS Config can alert on compliance using custom rules.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Sizing.html"
    ]
  },
  {
    "Title": "Support Dual-Stack Mode in DB Subnet Groups",
    "Description": "DB subnet groups must have an associated IPv6 CIDR block to support dual-stack operations.",
    "Applicability": "Amazon Aurora DB subnet groups configured for dual-stack mode",
    "Security Risk": "Inadequate support for IPv6 can lead to future compatibility and scalability issues.",
    "Default Behavior / Limitations": "AWS does not enforce IPv6 support; it must be configured.",
    "Automation": "Managed through AWS CLI or AWS CloudFormation. AWS Config can verify the presence of IPv6 CIDR blocks.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html"
    ]
  },
  {
    "Title": "Ensure Security Groups Allow IPv4 and IPv6 Traffic",
    "Description": "Security groups must be configured to allow traffic over both IPv4 and IPv6 for dual-stack mode functionality.",
    "Applicability": "All Amazon Aurora DB clusters using dual-stack mode",
    "Security Risk": "Inadequate security group configurations can prevent proper connectivity and expose services to potential threats.",
    "Default Behavior / Limitations": "Security groups default to allowing only IPv4 unless explicitly configured for IPv6.",
    "Automation": "Configured using AWS CLI, AWS Management Console, or AWS CloudFormation, and monitored through AWS Config rules.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html"
    ]
  },
  {
    "Title": "Restrict Dual-Stack Mode DB Clusters to Private Access",
    "Description": "Ensure dual-stack mode DB clusters are private and not publicly accessible to enhance security.",
    "Applicability": "All dual-stack mode Amazon Aurora DB clusters",
    "Security Risk": "Publicly accessible endpoints can lead to increased risk of unauthorized access and exposure.",
    "Default Behavior / Limitations": "By design, dual-stack mode does not enforce private access; configurations are necessary.",
    "Automation": "Managed via AWS Security Group rules and controlled through AWS CloudFormation. Verified using AWS Config and Security Hub findings.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.manual.html"
    ]
  },
  {
    "Title": "Enable Internet Gateway for Publicly Accessible DB Clusters",
    "Description": "Ensure subnets for publicly accessible DB clusters are connected to an Internet Gateway for necessary public connectivity.",
    "Applicability": "Publicly accessible Amazon Aurora DB clusters",
    "Security Risk": "Without an Internet Gateway, publicly declared endpoints may become unreachable, impacting service availability.",
    "Default Behavior / Limitations": "Internet Gateways are not automatically associated with public subnets.",
    "Automation": "Configured via AWS Management Console, AWS CLI, or AWS CloudFormation, and audited via AWS Config.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html"
    ]
  },
  {
    "Title": "Verify DB Instance Class for Dedicated Hosting",
    "Description": "Ensure the DB instance class used is approved for dedicated instances when setting the instance tenancy attribute to dedicated.",
    "Applicability": "Amazon Aurora DB clusters with dedicated instance tenancy",
    "Security Risk": "Using unapproved instance classes with dedicated hosting may cause performance degradation and unsupported configurations.",
    "Default Behavior / Limitations": "AWS does not automatically validate compatibility of instance classes for dedicated tenancy.",
    "Automation": "Manually validated for compatibility; automated checks can be incorporated using AWS Config for specific class verifications.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Dedicated-Hardware.html"
    ]
  }
]
```