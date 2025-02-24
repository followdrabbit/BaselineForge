```json
[
  {
    "Description": "Ensure that your Amazon VPC endpoints are being used to allow secure connection to AWS cloud services without the need of an Internet Gateway (IGW), NAT device, VPN connection, or AWS Direct Connect connection.",
    "Reference": "[VPC Endpoints In Use](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/vpc-endpoints-in-use.html)",
    "Observations": "VPC endpoints provide communication between EC2 instances within your VPC and other supported AWS services without introducing availability risks or bandwidth constraints."
  },
  {
    "Description": "For interface endpoints, utilize Elastic Network Interfaces (ENIs) with private IP addresses powered by AWS PrivateLink to privately connect your VPC to supported AWS services, services hosted by other AWS accounts, and supported AWS Marketplace partner services.",
    "Reference": "[VPC Endpoints In Use](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/vpc-endpoints-in-use.html)",
    "Observations": "Each ENI acts as the entry point for the traffic intended to a specific service."
  },
  {
    "Description": "Gateway endpoints should be set for specific routes within the VPC route tables and used for traffic intended to supported services such as Amazon DynamoDB and Amazon S3.",
    "Reference": "[VPC Endpoints In Use](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/vpc-endpoints-in-use.html)",
    "Observations": "Gateway endpoints facilitate traffic management without the use of public IP addresses."
  },
  {
    "Description": "VPC endpoints are supported only within the same AWS cloud region. You cannot use VPC endpoints to connect an AWS service from one region to a VPC in a different region.",
    "Reference": "[VPC Endpoints In Use](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/vpc-endpoints-in-use.html)",
    "Observations": "Ensure regional compatibility when configuring VPC endpoints."
  },
  {
    "Description": "Use AWS CloudFormation, Terraform, or AWS CLI for deploying and configuring VPC endpoints within your AWS account by specifying necessary resources, properties, and configurations like the VPC network, service type, and associated subnets.",
    "Reference": "[VPC Endpoints In Use - Remediation / Resolution Section](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/vpc-endpoints-in-use.html)",
    "Observations": "Automated deployment ensures consistent and reproducible configurations across environments."
  },
  {
    "Description": "Utilize AWS CLI commands such as `describe-vpc-endpoints` and `describe-vpcs` to audit existing VPC endpoints and verify their deployment across regions.",
    "Reference": "[VPC Endpoints In Use - Audit Section](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/vpc-endpoints-in-use.html)",
    "Observations": "Automated audits can enhance compliance and security posture by ensuring expected configurations are in place."
  }
]
```