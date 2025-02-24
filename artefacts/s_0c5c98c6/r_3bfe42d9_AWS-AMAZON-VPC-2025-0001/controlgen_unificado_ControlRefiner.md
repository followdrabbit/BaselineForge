```json
[
  {
    "Title": "Block Public Access for VPC Resources",
    "Description": "Implement VPC Block Public Access (BPA) to prevent unauthorized public internet access to VPC resources across all AWS accounts in an organization. Configure BPA in 'Bidirectional,' 'Ingress-only,' or specific modes as needed, and manage exceptions carefully to ensure minimal exposure.",
    "Applicability": "All AWS accounts within an AWS Organization or specific VPCs as defined",
    "Security Risk": "Public resource exposure can result in unauthorized access and data breaches.",
    "Default Behavior / Limitations": "VPC BPA is not enabled by default and requires manual configuration.",
    "Automation": "Can be enforced using AWS Organization SCPs and AWS Config rules for monitoring compliance.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html"
    ]
  },
  {
    "Title": "Implement Least Privilege Access for IAM Users",
    "Description": "Ensure all IAM users have the least privileges necessary to perform their duties. Use IAM Access Analyzer and AWS Config to monitor and audit IAM policies for compliance with this principle.",
    "Applicability": "All IAM policies across AWS accounts",
    "Security Risk": "Excessive permissions can lead to unauthorized access and potential data breaches.",
    "Default Behavior / Limitations": "AWS IAM does not enforce least privilege by default; permissions must be configured manually.",
    "Automation": "Can be monitored using AWS IAM Access Analyzer and AWS Config.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html"
    ]
  },
  {
    "Title": "Enforce Multi-Factor Authentication (MFA) for IAM Users",
    "Description": "Enable MFA for all IAM users, emphasizing those with administrative privileges, to enhance account security. Use IAM policies and AWS Config to enforce MFA compliance.",
    "Applicability": "All AWS accounts and IAM users",
    "Security Risk": "Without MFA, accounts are vulnerable to unauthorized access.",
    "Default Behavior / Limitations": "AWS IAM does not enable MFA by default.",
    "Automation": "Enforced using IAM policies and AWS Config rule `iam-user-mfa-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html"
    ]
  },
  {
    "Title": "Enable AWS CloudTrail for Comprehensive Logging",
    "Description": "Activate AWS CloudTrail in all regions to log API calls and user activity, covering both management and data events for comprehensive auditing.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without logging, unauthorized activities may go undetected.",
    "Default Behavior / Limitations": "CloudTrail is not enabled by default.",
    "Automation": "Managed using AWS Config rule `cloud-trail-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html"
    ]
  },
  {
    "Title": "Use IAM Roles for EC2 Instances",
    "Description": "Configure EC2 instances to use IAM roles for obtaining temporary security credentials through instance profiles, minimizing the use of long-term credentials.",
    "Applicability": "All EC2 instances running applications",
    "Security Risk": "Long-term credentials increase the risk of exposure.",
    "Default Behavior / Limitations": "IAM roles must be manually configured.",
    "Automation": "Monitored using AWS Config rule `ec2-instance-no-associated-iam-instance-profile`.",
    "References": [
      "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html"
    ]
  },
  {
    "Title": "Ensure VPC Flow Logs are Enabled",
    "Description": "Enable VPC Flow Logs in all VPCs to capture network traffic information for security analysis and troubleshooting.",
    "Applicability": "All VPCs",
    "Security Risk": "Without flow logs, security incidents may go undetected.",
    "Default Behavior / Limitations": "Flow logs are not enabled by default.",
    "Automation": "Managed using AWS Config rule `vpc-flow-logs-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html"
    ]
  },
  {
    "Title": "Activate Amazon GuardDuty for Threat Detection",
    "Description": "Enable GuardDuty across accounts to utilize VPC Flow Logs, CloudTrail event logs, and DNS logs for detecting threats.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Threats may go undetected without GuardDuty.",
    "Default Behavior / Limitations": "GuardDuty must be manually enabled.",
    "Automation": "Managed via AWS Management Console or CLI.",
    "References": [
      "https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html"
    ]
  },
  {
    "Title": "Ensure Proper Network ACL Configuration",
    "Description": "Configure Network Access Control Lists (ACLs) to control inbound and outbound subnet traffic, applying DENY rules to unauthorized access attempts.",
    "Applicability": "All AWS VPCs with subnets",
    "Security Risk": "Improper ACL configurations can allow unauthorized access.",
    "Default Behavior / Limitations": "Network ACLs are stateless and configurable.",
    "Automation": "Audit using AWS Config for compliance.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html"
    ]
  },
  {
    "Title": "Restrict and Monitor IAM Permissions Using SCPs",
    "Description": "Utilize Service Control Policies (SCPs) to manage permissions centrally within AWS Organizations, ensuring a consistent security posture across accounts.",
    "Applicability": "All AWS accounts within an organization",
    "Security Risk": "Inconsistent permissions can lead to vulnerabilities.",
    "Default Behavior / Limitations": "SCPs require manual setup.",
    "Automation": "Managed using AWS Organizations.",
    "References": [
      "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html"
    ]
  },
  {
    "Title": "Use TLS 1.2 or Higher for Secure Communications",
    "Description": "Ensure all communications with AWS services enforce a minimum TLS version of 1.2, configuring endpoints accordingly.",
    "Applicability": "All AWS services and endpoints",
    "Security Risk": "Old protocols can be vulnerable to attacks.",
    "Default Behavior / Limitations": "TLS 1.2 is generally supported by AWS services.",
    "Automation": "Monitor compliance with AWS Config and Security Hub.",
    "References": [
      "https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/create-https-listener.html"
    ]
  },
  {
    "Title": "Encrypt Data at Rest and in Transit",
    "Description": "Configure AWS services to use encryption for both data at rest and data in transit, utilizing AWS KMS for key management.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Unencrypted data is vulnerable to unauthorized access.",
    "Default Behavior / Limitations": "AWS provides encryption options, but setup is required.",
    "Automation": "Ensure compliance using AWS Config rules like `rds-storage-encrypted`.",
    "References": [
      "https://docs.aws.amazon.com/general/latest/gr/aws_security.html#aws-security-encryption"
    ]
  }
]
```