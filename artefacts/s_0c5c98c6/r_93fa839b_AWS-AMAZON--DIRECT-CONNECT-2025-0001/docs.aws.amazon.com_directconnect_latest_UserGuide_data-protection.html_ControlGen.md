```json
[
  {
    "Title": "Implement Multi-Factor Authentication (MFA) for AWS Accounts",
    "Description": "MFA must be enabled for all AWS accounts to enhance security and prevent unauthorized access. This can be achieved by enrolling user accounts in MFA and configuring IAM policies to require MFA for accessing sensitive resources.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without MFA, unauthorized individuals may gain access to AWS accounts, potentially leading to data breaches and unauthorized changes.",
    "Default Behavior / Limitations": "AWS does not enable MFA by default; it requires manual configuration.",
    "Automation": "Can be enforced using IAM policies and AWS Config with the `iam-user-mfa-enabled` rule.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html",
      "https://docs.aws.amazon.com/directconnect/latest/UserGuide/data-protection.html"
    ]
  },
  {
    "Title": "Enforce TLS 1.2 or Higher for AWS Resources",
    "Description": "Ensure that all communications with AWS resources use SSL/TLS with at least TLS 1.2, preferably TLS 1.3, to protect data in transit from interception and tampering.",
    "Applicability": "All AWS communications",
    "Security Risk": "Using older encryption protocols may expose data to interception and cryptographic attacks.",
    "Default Behavior / Limitations": "AWS services generally support TLS 1.2 by default; configuration may be required to enforce higher standards.",
    "Automation": "Can use AWS Config rules for SSL policies and AWS Certificate Manager to verify TLS configurations.",
    "References": [
      "https://docs.aws.amazon.com/directconnect/latest/UserGuide/data-protection.html",
      "https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-tls.html"
    ]
  },
  {
    "Title": "Enable API and User Activity Logging with AWS CloudTrail",
    "Description": "Configure AWS CloudTrail to log all API calls and user activities across accounts and regions. This setup should include capturing management and data events for auditing purposes.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without logging, unauthorized actions may go undetected, hindering incident detection and forensic capabilities.",
    "Default Behavior / Limitations": "AWS CloudTrail is not enabled by default for all activities; configuration is necessary.",
    "Automation": "Enforceable using AWS Config with the `cloudtrail-enabled` rule.",
    "References": [
      "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html",
      "https://docs.aws.amazon.com/directconnect/latest/UserGuide/data-protection.html"
    ]
  },
  {
    "Title": "Utilize AWS Encryption Solutions for Data Protection",
    "Description": "Leverage AWS encryption services like KMS and default security controls to encrypt data at rest and in transit, using customer-managed or AWS-managed keys.",
    "Applicability": "All data storage and transmission within AWS",
    "Security Risk": "Unencrypted data may be susceptible to unauthorized access and tampering.",
    "Default Behavior / Limitations": "Many AWS services provide encryption by default, but specific setup is necessary for compliance with customer policies.",
    "Automation": "Enable using AWS Config rules for encryption verification.",
    "References": [
      "https://docs.aws.amazon.com/kms/latest/developerguide/overview.html",
      "https://docs.aws.amazon.com/directconnect/latest/UserGuide/data-protection.html"
    ]
  },
  {
    "Title": "Protect Sensitive Data in Amazon S3 with Amazon Macie",
    "Description": "Integrate Amazon Macie to automatically discover, classify, and protect sensitive data stored in Amazon S3, ensuring that data exposure is minimized and compliance requirements are met.",
    "Applicability": "All S3 buckets containing sensitive data",
    "Security Risk": "Unprotected sensitive data can lead to data breaches and compliance violations.",
    "Default Behavior / Limitations": "Amazon Macie requires explicit setup and configurations.",
    "Automation": "Automated through Amazon Macie setup and integrations.",
    "References": [
      "https://docs.aws.amazon.com/macie/latest/user-guide/what-is-macie.html",
      "https://docs.aws.amazon.com/directconnect/latest/UserGuide/data-protection.html"
    ]
  },
  {
    "Title": "Use FIPS Endpoints for Compliance with Cryptographic Standards",
    "Description": "Configure AWS CLI and SDKs to use FIPS 140-3 validated endpoints for secure communication when federal compliance is necessary.",
    "Applicability": "AWS services in sensitive environments",
    "Security Risk": "Avoidance of FIPS endpoints may result in non-compliance with regulatory standards, impacting operations in federal agencies or contracts.",
    "Default Behavior / Limitations": "FIPS endpoints must be manually specified and are not used by default.",
    "Automation": "Manual configuration required; automated reminders can be set using AWS Config for compliance checks.",
    "References": [
      "https://aws.amazon.com/compliance/fips/",
      "https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-fips.html"
    ]
  },
  {
    "Title": "Avoid Sensitive Information in AWS Tags and Text Fields",
    "Description": "Ensure that no confidential or sensitive information, such as customer email addresses, is stored in free-form text fields or tags, as these fields can be exposed in logs.",
    "Applicability": "All AWS resources across accounts",
    "Security Risk": "Sensitive information in these fields can lead to privacy violations or data breaches if exposed.",
    "Default Behavior / Limitations": "AWS does not restrict sensitive data entry in tags by default.",
    "Automation": "Requires manual policy enforcement; AWS Config can alert on detected sensitive patterns.",
    "References": [
      "https://docs.aws.amazon.com/directconnect/latest/UserGuide/data-protection.html"
    ]
  }
]
```