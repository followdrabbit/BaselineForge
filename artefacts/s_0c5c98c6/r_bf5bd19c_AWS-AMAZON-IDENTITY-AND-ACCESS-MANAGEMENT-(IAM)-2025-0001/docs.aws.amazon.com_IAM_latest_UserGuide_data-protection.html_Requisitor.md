```json
[
  {
    "Description": "Ensure multi-factor authentication (MFA) is enabled for all AWS accounts.",
    "Reference": "[Data protection in AWS Identity and Access Management - User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/data-protection.html)",
    "Observations": "Check if the default configuration enables MFA on all accounts."
  },
  {
    "Description": "Use SSL/TLS for all communications with AWS resources, requiring TLS 1.2 and recommending TLS 1.3.",
    "Reference": "[Data protection in AWS Identity and Access Management - User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/data-protection.html)",
    "Observations": "TLS 1.3 is recommended for enhanced security."
  },
  {
    "Description": "Enable API and user activity logging with AWS CloudTrail.",
    "Reference": "[Working with CloudTrail trails - AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html)",
    "Observations": ""
  },
  {
    "Description": "Implement AWS encryption solutions and utilize all default security controls within AWS services.",
    "Reference": "[Data protection in AWS Identity and Access Management - User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/data-protection.html)",
    "Observations": "Ensure all default security controls are active."
  },
  {
    "Description": "For cryptographic needs requiring FIPS 140-3 validation, use a FIPS endpoint.",
    "Reference": "[Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/)",
    "Observations": "Validate whether specific APIs or services require FIPS compliance."
  },
  {
    "Description": "Do not place sensitive information in tags or free-form text fields.",
    "Reference": "[Data protection in AWS Identity and Access Management - User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/data-protection.html)",
    "Observations": "Includes the console, APIs, AWS CLI, and AWS SDKs."
  },
  {
    "Description": "Data collected by IAM should be encrypted at rest using AES 256 or hashed using SHA 256.",
    "Reference": "[Data encryption in IAM and AWS STS - User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/data-protection.html#encryption-in-IAM)",
    "Observations": "Applies to IP addresses, customer account metadata, and identifying data."
  },
  {
    "Description": "Ensure customer identifying data is encrypted in transit using TLS 1.2 or 1.3.",
    "Reference": "[Data encryption in transit - User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/data-protection.html#encryption-in-transit)",
    "Observations": "Verify that all endpoints support HTTPS."
  },
  {
    "Description": "Requests to IAM must be made using the Transport Layer Security protocol (TLS).",
    "Reference": "[Internetwork traffic privacy in IAM and AWS STS - User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/data-protection.html#internetwork-traffic-in-IAM)",
    "Observations": ""
  },
  {
    "Description": "Secure connections to AWS STS using VPC endpoints.",
    "Reference": "[Interface VPC endpoints - User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_interface_vpc_endpoints.html)",
    "Observations": "Refer to endpoint management for STS services."
  }
]
```