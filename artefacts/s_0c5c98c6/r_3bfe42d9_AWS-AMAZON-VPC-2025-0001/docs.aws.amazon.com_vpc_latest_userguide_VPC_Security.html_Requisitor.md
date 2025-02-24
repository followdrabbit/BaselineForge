```json
[
  {
    "Description": "Each EC2 instance within a VPC must be associated with at least one security group to control inbound and outbound traffic.",
    "Reference": "Section on Security groups - URL: https://docs.aws.amazon.com/vpc-security-groups.html",
    "Observations": "Instances default to the VPC's default security group if none is specified."
  },
  {
    "Description": "Network ACLs must be configured to allow or deny specific inbound and outbound traffic at the subnet level.",
    "Reference": "Section on Control subnet traffic with network access control lists - URL: https://docs.aws.amazon.com/vpc-network-acls.html",
    "Observations": ""
  },
  {
    "Description": "Flow logs must be enabled to capture IP traffic going to and from network interfaces in the VPC.",
    "Reference": "Section on Logging IP traffic using VPC Flow Logs - URL: https://docs.aws.amazon.com/vpc/flow-logs.html",
    "Observations": "Flow logs data can be published to CloudWatch Logs or Amazon S3."
  },
  {
    "Description": "Enable traffic mirroring to copy network traffic from an elastic network interface of an EC2 instance for monitoring purposes.",
    "Reference": "Traffic Mirroring Guide - URL: https://docs.aws.amazon.com/vpc/latest/mirroring/",
    "Observations": "Traffic can be sent to out-of-band security and monitoring appliances."
  }
]
```