### ControlGen Output - Arquivo 1
```json
[
  {
    "Title": "Deploy Subnets Across Multiple Availability Zones",
    "Description": "Ensure that subnets are set up in multiple AWS Availability Zones (AZs) to provide high availability and fault tolerance for applications running in VPC.",
    "Applicability": "All production environments",
    "Security Risk": "Failure to distribute subnets across multiple AZs could lead to outages in the event of an AZ failure, impacting service availability and resilience.",
    "Default Behavior / Limitations": "AWS allows creation of subnets in multiple AZs but does not enforce it by default. Manual configuration is required.",
    "Automation": "Manual validation required. AWS Config rule cannot enforce cross-AZ subnet distribution.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html"
    ]
  },
  {
    "Title": "Use Security Groups to Control EC2 Instance Traffic",
    "Description": "Configure security groups to allow specific ingress and egress traffic to EC2 instances in VPC subnets, enhancing security by only permitting known traffic.",
    "Applicability": "All AWS environments using EC2 instances",
    "Security Risk": "Not using security groups can expose EC2 instances to unwanted traffic, leading to potential data breaches or unauthorized access.",
    "Default Behavior / Limitations": "Security groups must be explicitly configured; no default inbound rule exists.",
    "Automation": "Can be monitored using AWS Config rule `ec2-security-group-attached`.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html"
    ]
  },
  {
    "Title": "Implement Network ACLs at the Subnet Level",
    "Description": "Use network access control lists (ACLs) to control inbound and outbound traffic at a subnet level, providing an additional layer of security.",
    "Applicability": "All AWS environments with VPCs",
    "Security Risk": "Without network ACLs, subnets might be exposed to unauthorized traffic, leading to potential security vulnerabilities.",
    "Default Behavior / Limitations": "Network ACLs are stateless and are independent of security groups; must be configured manually.",
    "Automation": "Can be monitored using AWS Config for subnet configuration compliance.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html"
    ]
  },
  {
    "Title": "Enable VPC Flow Logs for Traffic Monitoring",
    "Description": "Activate VPC Flow Logs to capture information about the IP traffic going to and from network interfaces in your VPC for auditing and troubleshooting purposes.",
    "Applicability": "All VPCs in all AWS accounts",
    "Security Risk": "Without VPC Flow Logs, suspicious activities or network traffic issues may go unnoticed, making it hard to detect and respond to security incidents.",
    "Default Behavior / Limitations": "VPC Flow Logs are not enabled by default and require manual activation.",
    "Automation": "Can be enforced using AWS Config rule `vpc-flow-logs-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html"
    ]
  },
  {
    "Title": "Deploy AWS Network Firewall for VPC Traffic Filtering",
    "Description": "Utilize AWS Network Firewall to filter traffic entering and exiting VPCs, providing a high level of network security and threat protection.",
    "Applicability": "All VPCs requiring advanced network security",
    "Security Risk": "Without a network firewall, VPC traffic may be vulnerable to attacks or data exfiltration attempts.",
    "Default Behavior / Limitations": "AWS Network Firewall needs to be deployed and configured based on specific security requirements; not enabled by default.",
    "Automation": "Manual validation required. Deployment must be configured through AWS Management Console or APIs.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html"
    ]
  },
  {
    "Title": "Activate Amazon GuardDuty for Threat Detection",
    "Description": "Enable Amazon GuardDuty to monitor VPC Flow Logs, CloudTrail event logs, and DNS logs to detect suspicious activities and potential threats.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without GuardDuty, potential threats and suspicious activities may go undetected, risking the security of AWS workloads.",
    "Default Behavior / Limitations": "Amazon GuardDuty is not enabled by default and requires manual activation.",
    "Automation": "Can be enabled and managed through AWS Management Console or AWS CLI.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 2
```json
[
  {
    "Title": "Ensure Compliance of Amazon VPC Peering Connection Configuration with Desired Routing Policy",
    "Description": "Validate that Amazon VPC peering connections have route tables configured according to the organization's desired routing policy. Audit VPC route tables for correct propagation settings and route configurations.",
    "Applicability": "All AWS accounts utilizing VPC peering connections",
    "Security Risk": "Incorrect routing configurations can lead to unintended data exposure or routing loops, compromising network integrity.",
    "Default Behavior / Limitations": "AWS does not automatically enforce compliance with custom routing policies.",
    "Automation": "Manual validation required through periodic inspections and AWS Config for monitoring route table changes.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-peering-routing.html"
    ]
  },
  {
    "Title": "Ensure AWS VPN Tunnels are Continuously in UP State",
    "Description": "Monitor AWS VPN dashboards to confirm that VPN tunnels are in an 'UP' state, ensuring stable connectivity.",
    "Applicability": "All AWS accounts using VPN connections",
    "Security Risk": "A VPN tunnel in a 'DOWN' state can disrupt communications, impacting availability and productivity.",
    "Default Behavior / Limitations": "VPN tunnels can occasionally be in 'DOWN' state due to network issues.",
    "Automation": "Configure AWS CloudWatch Alarms to monitor VPN tunnel status and alert when tunnels transition to 'DOWN' state.",
    "References": [
      "https://docs.aws.amazon.com/vpn/latest/s2svpn/monitoring-cloudwatch-vpn.html"
    ]
  },
  {
    "Title": "Ensure Effectiveness of Network ACL DENY Rules in VPCs",
    "Description": "Inspect Network ACL configurations to ensure that DENY rules are appropriately implemented and effective in blocking unauthorized traffic.",
    "Applicability": "All AWS VPCs",
    "Security Risk": "Ineffective DENY rules might fail to obstruct malicious traffic, exposing the network to potential threats.",
    "Default Behavior / Limitations": "Network ACL rules must be accurately configured for effective operation.",
    "Automation": "Use AWS Config rules to audit NACL configurations and alert on any misconfigurations.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html"
    ]
  },
  {
    "Title": "Enable High Availability for Managed NAT Gateway Service",
    "Description": "Ensure that Managed NAT Gateways are deployed across multiple Availability Zones to guarantee high availability.",
    "Applicability": "All VPCs using Managed NAT Gateways",
    "Security Risk": "A single AZ failure could result in a loss of outbound internet connectivity without HA configuration.",
    "Default Behavior / Limitations": "High availability requires deliberate multi-AZ deployment strategies.",
    "Automation": "Use AWS CloudFormation templates to deploy NAT Gateways across multiple AZs.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html"
    ]
  },
  {
    "Title": "Ensure Specific Internet/NAT Gateway is Attached to Specific VPC",
    "Description": "Verify that each Internet or NAT Gateway is correctly attached to its designated VPC to avoid network misconfigurations.",
    "Applicability": "All AWS VPCs",
    "Security Risk": "Misconfigurations can lead to connectivity issues and unexpected network exposures.",
    "Default Behavior / Limitations": "Manual configuration is required for gateway-to-VPC attachments.",
    "Automation": "Utilize AWS Config to monitor and alert against any unauthorized changes in gateway attachments.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-gateway.html"
    ]
  },
  {
    "Title": "Restrict Network ACL Inbound Traffic on TCP Ports 22 and 3389",
    "Description": "Configure Network ACLs to deny unrestricted inbound traffic on TCP ports 22 (SSH) and 3389 (RDP) to secure remote access.",
    "Applicability": "All AWS VPCs",
    "Security Risk": "Unrestricted access on these ports can lead to unauthorized access and potential system compromise.",
    "Default Behavior / Limitations": "Security best practices require explicit configuration of restrictions.",
    "Automation": "Enforce using AWS Config Rule for monitoring and alerting on ACL changes affecting these ports.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html"
    ]
  },
  {
    "Title": "Restrict Network ACL Inbound Traffic on All Ports",
    "Description": "Inspect and configure Network ACLs to ensure no inbound rules allow traffic on all ports.",
    "Applicability": "All AWS VPCs",
    "Security Risk": "Allowing unrestricted inbound traffic can expose the network to attacks.",
    "Default Behavior / Limitations": "Security requires intentional setup of ACLs to block unwanted traffic.",
    "Automation": "Use AWS Config rules to audit ACL settings and prohibit unrestricted inbound access.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html"
    ]
  },
  {
    "Title": "Restrict Network ACL Outbound Traffic on All Ports",
    "Description": "Ensure that Network ACLs are configured to prevent unrestricted egress traffic, thereby controlling data flow out of the network.",
    "Applicability": "All AWS VPCs",
    "Security Risk": "Uncontrolled outbound traffic can lead to unauthorized data exfiltration.",
    "Default Behavior / Limitations": "Requires precise configuration of ACL egress rules.",
    "Automation": "Use AWS Config to enforce and monitor NACL settings for compliant traffic control.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html"
    ]
  },
  {
    "Title": "Remove Unused VPC Internet Gateways and Egress-Only Internet Gateways",
    "Description": "Periodically audit and remove any unused VPC Internet Gateways and Egress-Only Internet Gateways to minimize risk.",
    "Applicability": "All AWS VPCs",
    "Security Risk": "Unused gateways increase the network attack surface and congestion risks.",
    "Default Behavior / Limitations": "Requires manual removal of unused resources.",
    "Automation": "Manual validation is required for identifying and decommissioning unused gateways.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html"
    ]
  },
  {
    "Title": "Remove Unused Virtual Private Gateways (VGWs)",
    "Description": "Conduct regular assessments to identify and disconnect any unused Virtual Private Gateways.",
    "Applicability": "All AWS VPCs",
    "Security Risk": "Unused VGWs can create unnecessary security and management overhead.",
    "Default Behavior / Limitations": "Unused VGWs require discovery and manual decommissioning.",
    "Automation": "Manual assessment required to identify unused VGWs, followed by appropriate action for removal.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/VPC_VpnGateway.html"
    ]
  },
  {
    "Title": "Prevent Unknown Cross-Account Access to VPC Endpoints",
    "Description": "Configure VPC endpoints to restrict access to known and trusted AWS accounts only, preventing unauthorized cross-account access.",
    "Applicability": "All AWS VPCs utilizing VPC endpoints",
    "Security Risk": "Open cross-account access can lead to unauthorized data access and compromise.",
    "Default Behavior / Limitations": "Access restrictions need explicit configuration in endpoint policy.",
    "Automation": "Use AWS IAM policies to enforce access restrictions and AWS Config to monitor policy changes.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html"
    ]
  },
  {
    "Title": "Restrict VPC Endpoints from Public Exposure",
    "Description": "Ensure that your VPC endpoints are configured to limit exposure and prevent public access.",
    "Applicability": "All AWS VPCs using VPC endpoints",
    "Security Risk": "Public exposure of VPC endpoints can result in unauthorized access.",
    "Default Behavior / Limitations": "Endpoint security configurations must be manually established.",
    "Automation": "AWS Config rules can be used to ensure compliance with endpoint exposure security policies.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html"
    ]
  },
  {
    "Title": "Ensure Usage of VPC Endpoints for AWS Service Connectivity",
    "Description": "Verify and ensure that VPC endpoints are utilized to connect VPCs to supported AWS services, bypassing the public internet.",
    "Applicability": "All applicable AWS VPCs",
    "Security Risk": "Failure to use VPC endpoints may expose data to potential interception over public networks.",
    "Default Behavior / Limitations": "Endpoint creation must be initiated by the user.",
    "Automation": "AWS Config rules can be established to verify and ensure endpoint compliance.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html"
    ]
  },
  {
    "Title": "Enable VPC Flow Logging in All VPCs",
    "Description": "Configure VPC flow logging to capture detailed network traffic information for security and operational auditing.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without flow logs, network issues may be undiscoverable, leading to unchecked vulnerabilities and difficulties in troubleshooting.",
    "Default Behavior / Limitations": "VPC flow logs are not enabled by default and require user activation.",
    "Automation": "Enforced using AWS Config to enable logging across VPCs and monitor log generation.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html"
    ]
  },
  {
    "Title": "Adhere to Proper Naming Conventions for VPCs",
    "Description": "Implement and maintain consistent naming conventions for VPCs to improve resource identity and management.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Improper naming can lead to confusion and management challenges, increasing operational risks.",
    "Default Behavior / Limitations": "Naming standards need to be manually defined and enforced.",
    "Automation": "Manual validation is required to ensure adherence to naming conventions.",
    "References": [
      "https://aws.amazon.com/architecture/"
    ]
  },
  {
    "Title": "Restrict VPC Peering to AWS Accounts within the Same Organization",
    "Description": "Configure VPC peering to allow communication between VPCs only from accounts that are members of the same AWS Organization.",
    "Applicability": "All AWS VPCs",
    "Security Risk": "Allowing peering with external accounts can expose sensitive resources to unauthorized users.",
    "Default Behavior / Limitations": "Peering configurations must be set manually per organizational policies.",
    "Automation": "Implement AWS Organization Service Control Policies (SCPs) to manage VPC peering connections.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-peering.html"
    ]
  },
  {
    "Title": "Ensure Redundancy for AWS VPN Tunnels with Two Active Tunnels",
    "Description": "Maintain two active tunnels for each AWS VPN connection to ensure redundancy and avoid single points of failure.",
    "Applicability": "All AWS accounts using VPN connections",
    "Security Risk": "A non-redundant VPN setup can lead to network outages and loss of connectivity.",
    "Default Behavior / Limitations": "AWS automatically creates two tunnels per VPN connection but requires monitoring for operational status.",
    "Automation": "AWS CloudWatch Alarms can be used to monitor tunnel status and ensure both are active.",
    "References": [
      "https://docs.aws.amazon.com/vpn/latest/s2svpn/VPNTunnels.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 3
```json
[
  {
    "Title": "Implement Least Privilege Access for IAM Users",
    "Description": "Ensure that all IAM or IAM Identity Center users have permissions strictly necessary to fulfill their job duties. Use IAM policies to grant the least privilege.",
    "Applicability": "All users in the AWS environment",
    "Security Risk": "Excessive permissions can lead to unauthorized access and potential data breaches.",
    "Default Behavior / Limitations": "AWS IAM does not enforce least privilege; permissions must be configured according to the principle of least privilege manually.",
    "Automation": "Can be monitored and audited using AWS IAM Access Analyzer or AWS Config to ensure compliance with the least privilege.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html"
    ]
  },
  {
    "Title": "Enforce Multi-Factor Authentication (MFA) Across All Accounts",
    "Description": "Configure AWS accounts so that MFA is enabled for all users, especially those with administrative privileges. Use IAM policies to deny access to the console if MFA is not configured.",
    "Applicability": "All AWS accounts and users",
    "Security Risk": "Without MFA, accounts are susceptible to unauthorized access due to credential compromise.",
    "Default Behavior / Limitations": "AWS IAM does not enable MFA by default. It needs to be configured.",
    "Automation": "Can be enforced using IAM policies and AWS Config rule `iam-user-mfa-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html"
    ]
  },
  {
    "Title": "Enforce TLS 1.2 or Higher for All Communications with AWS",
    "Description": "Ensure that all communications with AWS services utilize SSL/TLS with a minimum of TLS 1.2. Configure AWS service endpoints to enforce this protocol version.",
    "Applicability": "All AWS services and endpoints",
    "Security Risk": "Use of weak SSL/TLS protocols (below TLS 1.2) can lead to data breaches due to interception by malicious actors.",
    "Default Behavior / Limitations": "AWS services generally support TLS 1.2 by default, but configuration should be verified.",
    "Automation": "Monitor using AWS Config and AWS Security Hub for ensuring compliance with minimum TLS settings.",
    "References": [
      "https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/create-https-listener.html"
    ]
  },
  {
    "Title": "Enable AWS CloudTrail for API and User Activity Logging",
    "Description": "Activate AWS CloudTrail for all regions in the account, ensuring all AWS service events are logged. Configure trails to log management and data events.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without logging, unauthorized activities may go undetected, complicating incident response.",
    "Default Behavior / Limitations": "AWS CloudTrail is not enabled by default.",
    "Automation": "Can be enforced using AWS Config rule `cloud-trail-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html"
    ]
  },
  {
    "Title": "Ensure All AWS Data is Encrypted at Rest and in Transit",
    "Description": "Configure AWS services to use encryption solutions for data at rest and in transit. AWS KMS can be used to manage encryption keys.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Unencrypted data is at risk of unauthorized access or theft.",
    "Default Behavior / Limitations": "AWS provides options to encrypt data, but configuration is required.",
    "Automation": "Monitor encryption compliance using AWS Config rules like `rds-storage-encrypted` or `s3-bucket-server-side-encryption-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/general/latest/gr/aws_security.html#aws-security-encryption"
    ]
  },
  {
    "Title": "Deploy Amazon Macie for Sensitive Data Discovery and Protection",
    "Description": "Enable Amazon Macie to discover, classify, and protect sensitive data stored in Amazon S3. Regularly review Macie findings for sensitive data exposure.",
    "Applicability": "All AWS accounts utilizing Amazon S3",
    "Security Risk": "Sensitive data exposure can lead to data breaches and compliance violations.",
    "Default Behavior / Limitations": "Amazon Macie is a paid service and must be enabled manually.",
    "Automation": "Findings can be monitored using AWS Security Hub and Amazon Macie dashboards.",
    "References": [
      "https://docs.aws.amazon.com/macie/latest/userguide/what-is-macie.html"
    ]
  },
  {
    "Title": "Use FIPS Endpoints for Compliance Requirements",
    "Description": "Configure AWS CLI and SDKs to communicate with AWS services using FIPS 140-3 endpoints if required by compliance policies.",
    "Applicability": "All AWS environments where FIPS compliance is necessary",
    "Security Risk": "Non-compliance with federal standards can result in penalties and data protection weaknesses.",
    "Default Behavior / Limitations": "FIPS endpoints are available but must be configured manually.",
    "Automation": "Compliance can be verified through audits of endpoint usage settings.",
    "References": [
      "https://aws.amazon.com/compliance/fips/"
    ]
  },
  {
    "Title": "Prevent Sensitive Information in Tags and Free-Form Text Fields",
    "Description": "Implement tag policies using AWS Organizations to prevent entry of sensitive or confidential information in tags and free-form text fields.",
    "Applicability": "All AWS resources where tagging is used",
    "Security Risk": "Sensitive data in tags can be exposed inadvertently, leading to information leaks.",
    "Default Behavior / Limitations": "Tag policies need to be defined by users.",
    "Automation": "Can be enforced using AWS Organizations Tag Policies.",
    "References": [
      "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 4
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

### ControlGen Output - Arquivo 5
```json
[
  {
    "Title": "Use IAM Roles for EC2 Instances Instead of Long-Term Credentials",
    "Description": "Configure an instance profile that includes an IAM role for applications running on Amazon EC2 instances, ensuring these applications use temporary security credentials instead of creating IAM users with long-term credentials.",
    "Applicability": "All Amazon EC2 instances running applications",
    "Security Risk": "Using long-term credentials increases the risk of credential exposure and unauthorized access to AWS resources.",
    "Default Behavior / Limitations": "AWS supports the use of IAM roles via instance profiles but requires manual configuration.",
    "Automation": "Can be monitored using AWS Config rule `ec2-instance-no-associated-iam-instance-profile`.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/security-iam.html",
      "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html"
    ]
  },
  {
    "Title": "Implement Multi-Factor Authentication (MFA) for Root and IAM Users",
    "Description": "Enable MFA for the AWS account root user and for IAM users to enhance the security of their account access. Configure IAM policies to enforce this.",
    "Applicability": "AWS account root user and all IAM users where applicable",
    "Security Risk": "Without MFA, compromised credentials can lead to unauthorized account access and data breaches.",
    "Default Behavior / Limitations": "AWS does not enforce MFA by default; it must be manually enabled.",
    "Automation": "Can be audited using AWS Security Hub and AWS Config rule `root-account-mfa-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html",
      "https://docs.aws.amazon.com/vpc/latest/userguide/security-iam.html"
    ]
  },
  {
    "Title": "Regularly Rotate IAM Access Keys",
    "Description": "Implement a schedule to rotate access keys for IAM users that require long-term credentials and ensure no unenforced credentials are exploited.",
    "Applicability": "All IAM users with long-term credentials",
    "Security Risk": "Stale or exposed access keys can lead to unauthorized AWS resource access if compromised.",
    "Default Behavior / Limitations": "AWS does not automatically rotate access keys; it requires manual intervention or custom automation.",
    "Automation": "Can be enforced using AWS Lambda to automate key rotation or monitored using AWS Config rule `access-keys-rotated`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html",
      "https://docs.aws.amazon.com/vpc/latest/userguide/security-iam.html"
    ]
  },
  {
    "Title": "Monitor IAM Policies Compliance with Least Privilege Principle",
    "Description": "Use AWS Config to ensure that IAM policies grant only the permissions necessary to perform specified tasks in accordance with the principle of least privilege.",
    "Applicability": "All IAM policies across AWS accounts",
    "Security Risk": "Excessive permissions increase vulnerability to attacks and unauthorized access.",
    "Default Behavior / Limitations": "AWS policies do not automatically restrict minimal permissions; they need manual analysis and configuration.",
    "Automation": "Can be enforced using AWS Config rule `iam-policy-no-statements-with-admin-access`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html",
      "https://docs.aws.amazon.com/vpc/latest/userguide/security-iam.html"
    ]
  },
  {
    "Title": "Set Permissions Boundaries for IAM Policies",
    "Description": "Define permissions boundaries for IAM roles and users to restrict the maximum permissions they can receive, thus ensuring they cannot exceed predefined boundaries.",
    "Applicability": "Specific IAM roles and users as per organizational requirement",
    "Security Risk": "Without boundaries, users and roles may be granted excessive permissions leading to potential misuse.",
    "Default Behavior / Limitations": "Permissions boundaries require manual setup and configuration.",
    "Automation": "Can be audited using AWS Config rule `iam-permissions-boundary-set`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html",
      "https://docs.aws.amazon.com/vpc/latest/userguide/security-iam.html"
    ]
  },
  {
    "Title": "Utilize Service Control Policies (SCPs) for Centralized Permissions Management",
    "Description": "Implement SCPs within AWS Organizations to enforce a centralized permissions control strategy across all member accounts.",
    "Applicability": "All AWS accounts within an organization using AWS Organizations",
    "Security Risk": "Unmanaged permissions could lead to breaches and inconsistent security posture across accounts.",
    "Default Behavior / Limitations": "SCPs are not enabled by default for all organizations' accounts and require manual configuration.",
    "Automation": "Can be managed centrally using AWS Organizations.",
    "References": [
      "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html",
      "https://docs.aws.amazon.com/vpc/latest/userguide/security-iam.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 6
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