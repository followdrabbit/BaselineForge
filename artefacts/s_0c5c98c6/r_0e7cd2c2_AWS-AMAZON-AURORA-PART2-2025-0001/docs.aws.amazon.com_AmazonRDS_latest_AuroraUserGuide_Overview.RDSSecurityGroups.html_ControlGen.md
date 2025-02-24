```json
[
  {
    "Title": "Enforce Specific IP Range and Port Rules in VPC Security Groups",
    "Description": "Each VPC security group must specify inbound and outbound rules allowing access from a defined IP address range and a specific port or another security group. Configure rules correctly to comply with organizational security policies and limit to 20 rules per security group.",
    "Applicability": "All environments using VPC security groups",
    "Security Risk": "Improperly configured security groups can expose resources to unauthorized access, leading to potential data breaches or compromise.",
    "Default Behavior / Limitations": "AWS does not enforce specific IP ranges or ports by default. Security group rules must be manually configured.",
    "Automation": "AWS Config rule `vpc-sg-open-only-authorized-ports` can enforce restrictions on allowed IP ranges and ports. Use AWS CloudFormation to automate security group rule creation.",
    "References": [
      "https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.html",
      "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group.html"
    ]
  },
  {
    "Title": "Single Port Specification Per IP Range in Security Group Rules",
    "Description": "Ensure each security group rule specifies a single port for each range of IP addresses it allows access to, thereby minimizing unnecessary open ports.",
    "Applicability": "All AWS security groups",
    "Security Risk": "Leaving multiple ports open increases the potential attack surface, enabling potential intrusions.",
    "Default Behavior / Limitations": "AWS allows specifying ranges of ports which could lead to multiple open ports unintentionally.",
    "Automation": "AWS Config custom rule can be created to enforce single port specification. Use AWS CloudFormation `Properties` or custom scripts to manage.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.RDSSecurityGroups.html"
    ]
  },
  {
    "Title": "Automate VPC Security Group Creation Using AWS CloudFormation",
    "Description": "Use AWS CloudFormation to create and manage VPC security groups ensuring that configurations are consistent with best practices and organizational requirements.",
    "Applicability": "All AWS accounts using VPCs",
    "Security Risk": "Manual creation of security groups can lead to misconfigurations and non-standard implementations.",
    "Default Behavior / Limitations": "CloudFormation provides infrastructure as code capabilities but manually created resources need consistent configurations.",
    "Automation": "Fully automated through AWS CloudFormation templates, triggering updates with changesets for managing lifecycle.",
    "References": [
      "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html"
    ]
  },
  {
    "Title": "Track Changes to DB Cluster Security Groups Using Modify-db-cluster",
    "Description": "Utilize the RDS API or AWS CLI to modify DB cluster security groups, ensuring all changes are logged and reviewed by security teams.",
    "Applicability": "All AWS environments using RDS DB clusters",
    "Security Risk": "Untracked modifications could lead to unapproved access configurations and potential security risks.",
    "Default Behavior / Limitations": "Modifications are not automatically logged for review unless CloudTrail is enabled.",
    "Automation": "Enable AWS CloudTrail and AWS Config to monitor changes, using Config Rules to enforce compliance with policies.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.RDSSecurityGroups.html",
      "https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html"
    ]
  },
  {
    "Title": "Secure Non-Publicly Accessible DB Clusters Using VPN or Direct Connect",
    "Description": "Configure an AWS Site-to-Site VPN or AWS Direct Connect for secure communication with DB clusters that are not publicly accessible, ensuring connection methods adhere to security and compliance requirements.",
    "Applicability": "All AWS environments with non-public DB clusters",
    "Security Risk": "Relying solely on the internet for transmission can lead to exposure of sensitive data during transit.",
    "Default Behavior / Limitations": "VPN or Direct Connect must be manually configured for secure private network connections.",
    "Automation": "Can be automated using AWS CloudFormation and AWS Transit Gateway for consistent VPN or Direct Connect configurations.",
    "References": [
      "https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-configurations.html",
      "https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html"
    ]
  }
]
```