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