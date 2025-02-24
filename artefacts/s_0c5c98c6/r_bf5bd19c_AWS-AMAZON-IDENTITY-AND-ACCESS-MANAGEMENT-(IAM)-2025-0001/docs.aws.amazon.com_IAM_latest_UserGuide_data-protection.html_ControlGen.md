```json
[
  {
    "Title": "Enforce Multi-Factor Authentication (MFA) for AWS Accounts",
    "Description": "Ensure that MFA is enabled and required for access to all AWS accounts. This can be done by setting up mandatory MFA using IAM policies and configuring user settings to enforce MFA usage.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without MFA, unauthorized users could gain access to the account, leading to potential data breaches or resource misuse.",
    "Default Behavior / Limitations": "AWS IAM does not enforce MFA by default on all accounts.",
    "Automation": "Can be enforced using IAM identity center settings and AWS Config rule `iam-user-mfa-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html"
    ]
  },
  {
    "Title": "Require TLS 1.2+ for All Communications with AWS",
    "Description": "Ensure that all communications with AWS resources use a minimum of TLS 1.2, recommending TLS 1.3. This can be enforced by configuring security settings on AWS services that accept SSL/TLS connections.",
    "Applicability": "All AWS resources",
    "Security Risk": "Using outdated TLS versions can expose communications to attacks like man-in-the-middle, compromising data integrity and confidentiality.",
    "Default Behavior / Limitations": "Some AWS services may require manual configuration to enforce TLS 1.3.",
    "Automation": "Can be monitored using AWS Config with custom rules.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/data-protection.html"
    ]
  },
  {
    "Title": "Enable CloudTrail for API and User Activity Logging",
    "Description": "Set up AWS CloudTrail in all AWS regions to log all API and user activity to a centralized S3 bucket for security and compliance purposes.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without logging, it becomes difficult to monitor and audit changes, posing a risk of undetected unauthorized activities.",
    "Default Behavior / Limitations": "AWS does not enable AWS CloudTrail by default globally.",
    "Automation": "Can be enforced using AWS Config rule `cloud-trail-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html"
    ]
  },
  {
    "Title": "Implement AWS Encryption and Utilize Default Security Controls",
    "Description": "Enable AWS encryption options such as SSE-S3, SSE-KMS, and other encryption services across supported AWS resources. Ensure all default security controls are active for enhanced data protection.",
    "Applicability": "All AWS resources with encryption capability",
    "Security Risk": "Unencrypted data at rest can be accessed by unauthorized users, leading to data breaches and integrity issues.",
    "Default Behavior / Limitations": "Encryption must be configured for specific services like S3 and RDS.",
    "Automation": "Can be partly enforced using AWS Config rules for specific services.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/data-protection.html"
    ]
  },
  {
    "Title": "Use FIPS 140-3 Validated Cryptography for Compliance",
    "Description": "Configure FIPS-approved virtual interfaces and enabled components to use FIPS 140-3 validated cryptography where necessary.",
    "Applicability": "AWS services used in government or compliance-heavy environments",
    "Security Risk": "Non-validated cryptography may not meet regulatory compliance requirements, exposing the organization to legal and operational risks.",
    "Default Behavior / Limitations": "Requires specific configuration of endpoints.",
    "Automation": "Requires manual validation to ensure services are using FIPS endpoints.",
    "References": [
      "https://aws.amazon.com/compliance/fips/"
    ]
  },
  {
    "Title": "Avoid Storing Sensitive Data in Tags and Free-Form Fields",
    "Description": "Ensure that sensitive information such as PII is not stored in metadata tags or free-text fields within AWS services.",
    "Applicability": "All AWS services supporting tags and metadata fields",
    "Security Risk": "Sensitive information stored in tags can be exposed through API calls or when accessing metadata.",
    "Default Behavior / Limitations": "AWS does not restrict information typed into tags.",
    "Automation": "Requires manual validation and internal policy enforcement.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/data-protection.html"
    ]
  },
  {
    "Title": "Encrypt Data Collected by IAM at Rest Using AES-256",
    "Description": "Ensure that all data collected by IAM, including customer account metadata and identifying data, is encrypted at rest using AES-256.",
    "Applicability": "IAM service data storage",
    "Security Risk": "Lack of encryption can lead to unauthorized access to sensitive information.",
    "Default Behavior / Limitations": "Encryption configurations might differ across AWS services.",
    "Automation": "Can be monitored using AWS Config with custom rules.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/data-protection.html#encryption-in-IAM"
    ]
  },
  {
    "Title": "Encrypt Customer Identifying Data in Transit Using TLS",
    "Description": "Ensure that all customer identifying data is encrypted when in transit using a minimum of TLS 1.2, recommending TLS 1.3.",
    "Applicability": "All AWS services handling customer data in transit",
    "Security Risk": "Data in transit without encryption is susceptible to interception and tampering.",
    "Default Behavior / Limitations": "Certain integrations might require additional configuration to support advanced TLS settings.",
    "Automation": "Can be monitored using AWS Config and security audits.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/data-protection.html#encryption-in-transit"
    ]
  },
  {
    "Title": "Enforce TLS for IAM Requests",
    "Description": "Ensure that all requests to AWS IAM are conducted over TLS to provide encrypted communication channels.",
    "Applicability": "All clients interfacing with IAM",
    "Security Risk": "Lack of secure transport could expose data to interception and compromise.",
    "Default Behavior / Limitations": "TLS must be explicitly enforced in client configurations.",
    "Automation": "Requires manual validation and client-side configuration.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/data-protection.html#internetwork-traffic-in-IAM"
    ]
  },
  {
    "Title": "Use VPC Endpoints for Secure AWS STS Connections",
    "Description": "Utilize VPC endpoints to securely connect to AWS STS, protecting data by keeping traffic within the Amazon network.",
    "Applicability": "AWS services requiring STS access in VPC",
    "Security Risk": "Without VPC endpoints, traffic could leave the Amazon network, being exposed to various risks.",
    "Default Behavior / Limitations": "Requires VPC endpoint configuration for STS.",
    "Automation": "Can be enforced using AWS Config with rules monitoring VPC endpoint usage.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_interface_vpc_endpoints.html"
    ]
  }
]
```