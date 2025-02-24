```json
[
  {
    "Description": "Ensure that the Amazon VPC peering connection configuration is compliant with the desired routing policy.",
    "Reference": "[AWS VPC Peering Connections Route Tables Access](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/vpc-peering-access.html)",
    "Observations": "Compliance with routing policy ensures secure and intended data flow between peered VPCs."
  },
  {
    "Description": "Ensure the state of your AWS Virtual Private Network (VPN) tunnels is UP.",
    "Reference": "[AWS VPN Tunnel State](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/vpn-tunnel-up.html)",
    "Observations": "VPN tunnels in UP state confirm accessibility and connectivity."
  },
  {
    "Description": "Ensure that Amazon Network ACL DENY rules are effective within the VPC configuration.",
    "Reference": "[Ineffective Network ACL DENY Rules](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/network-acl-deny-rules.html)",
    "Observations": "Effective DENY rules are important for enforcing security boundaries within the VPC."
  },
  {
    "Description": "Ensure that the Managed NAT Gateway service is enabled for high availability (HA).",
    "Reference": "[Managed NAT Gateway in Use](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/managed-nat-gateway-in-use.html)",
    "Observations": "Enabling HA for NAT Gateways ensures continued operation even during failures."
  },
  {
    "Description": "Ensure that a specific Internet/NAT gateway is attached to a specific VPC.",
    "Reference": "[Specific Gateway Attached To Specific VPC](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/gateways.html)",
    "Observations": "Prevent misconfigurations that could impede connectivity or security."
  },
  {
    "Description": "Ensure that no Network ACL (NACL) allows unrestricted inbound traffic on TCP ports 22 and 3389.",
    "Reference": "[Unrestricted Inbound Traffic on Remote Server Administration Ports](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/acl-inbound-access-on-admin-ports.html)",
    "Observations": "TCP ports 22 and 3389 are commonly targeted ports, so restrictions protect against unauthorized access."
  },
  {
    "Description": "Ensure that no Network ACL (NACL) allows inbound/ingress traffic from all ports.",
    "Reference": "[Unrestricted Network ACL Inbound Traffic](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/network-acl-inbound-traffic-all-ports.html)",
    "Observations": "General unrestricted access can lead to potential security breaches."
  },
  {
    "Description": "Ensure that no Network ACL (NACL) allows outbound/egress traffic to all ports.",
    "Reference": "[Unrestricted Network ACL Outbound Traffic](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/network-acl-outbound-traffic-all-ports.html)",
    "Observations": "Restricting outbound traffic helps in controlling data exfiltration."
  },
  {
    "Description": "Ensure unused VPC Internet Gateways and Egress-Only Internet Gateways are removed.",
    "Reference": "[Unused VPC Internet Gateways](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/unused-internet-gateway.html)",
    "Observations": "Removing unused gateways reduces attack surface and potential misconfigurations."
  },
  {
    "Description": "Ensure unused Virtual Private Gateways (VGWs) are removed.",
    "Reference": "[Unused Virtual Private Gateways](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/unused-virtual-private-gateway.html)",
    "Observations": "Removal of unused VGWs helps in streamlining resource management and minimizing maintenance overhead."
  },
  {
    "Description": "Ensure Amazon VPC endpoints don't allow unknown cross account access.",
    "Reference": "[VPC Endpoint Cross Account Access](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/endpoint-cross-account-access.html)",
    "Observations": "Controlled access ensures that only trusted accounts can access sensitive resources."
  },
  {
    "Description": "Ensure Amazon VPC endpoints aren't exposed to everyone.",
    "Reference": "[VPC Endpoint Exposed](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/endpoint-exposed.html)",
    "Observations": "Limiting exposure reduces risk of unwanted access."
  },
  {
    "Description": "Ensure that VPC endpoints are being used to connect your VPC to another AWS cloud service.",
    "Reference": "[VPC Endpoints In Use](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/vpc-endpoints-in-use.html)",
    "Observations": "VPC Endpoints facilitate private connections to AWS services within the VPC."
  },
  {
    "Description": "Ensure VPC flow logging is enabled in all VPCs.",
    "Reference": "[VPC Flow Logs Enabled](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/vpc-flow-logs-enabled.html)",
    "Observations": "Flow logs are crucial for monitoring and troubleshooting network traffic."
  },
  {
    "Description": "Follow proper naming conventions for Virtual Private Clouds.",
    "Reference": "[VPC Naming Conventions](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/vpc-naming-conventions.html)",
    "Observations": "Consistent naming conventions help in better identification and management of VPC resources."
  },
  {
    "Description": "Ensure VPC peering communication is only between AWS accounts, members of the same AWS Organization.",
    "Reference": "[VPC Peering Connections To Accounts Outside AWS Organization](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/vpc-peering-connections-to-accounts-outside-aws-organizations.html)",
    "Observations": "Limits peering exposure to ensure secure and compliant interactions."
  },
  {
    "Description": "Ensure AWS VPNs have always two tunnels active in order to enable redundancy.",
    "Reference": "[VPN Tunnel Redundancy](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/vpn-tunnel-redundancy.html)",
    "Observations": "Active redundancy reduces risks associated with single points of failure."
  }
]
```