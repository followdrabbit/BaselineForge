```json
[
  {
    "Title": "Enforce Multi-Factor Authentication (MFA) for AWS Accounts",
    "Description": "Ensure that all AWS accounts have multi-factor authentication (MFA) enabled, especially for users with administrative privileges. Implement IAM policies to deny access when MFA is not enabled.",
    "Applicability": "All AWS accounts with IAM users",
    "Security Risk": "Without MFA, accounts are more vulnerable to unauthorized access, potentially leading to data breaches or unauthorized actions within the account.",
    "Default Behavior / Limitations": "AWS IAM does not enforce MFA by default; it must be configured manually.",
    "Automation": "Can be enforced using IAM policies and AWS Config rule `iam-user-mfa-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/data-protection.html"
    ]
  },
  {
    "Title": "Enforce TLS 1.2 or Higher for Communication with AWS Resources",
    "Description": "Configure all AWS resources to use SSL/TLS for communication, requiring TLS 1.2 as a minimum and recommending TLS 1.3 where possible. Ensure that security policies and network settings enforce the use of these protocols.",
    "Applicability": "All services communicating with AWS resources",
    "Security Risk": "Communication using outdated or unsecured protocols can lead to data interception and man-in-the-middle attacks.",
    "Default Behavior / Limitations": "AWS supports TLS 1.2 or higher, but enforcement depends on customer configuration.",
    "Automation": "Can be monitored using AWS Config rule `cloudfront-encryption-protocols-policy` for CloudFront and similar rules for other services.",
    "References": [
      "https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/data-protection.html"
    ]
  },
  {
    "Title": "Enable and Configure AWS CloudTrail for API and User Activity Logging",
    "Description": "Enable AWS CloudTrail in all regions and configure it to log both management and data events for auditing API calls and changes in account settings.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without logging, unauthorized activities might remain undetected, reducing the ability to audit and trace changes.",
    "Default Behavior / Limitations": "AWS CloudTrail is available but not enabled by default; customers must configure it.",
    "Automation": "Can be automated using AWS Config rule `cloud-trail-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/data-protection.html"
    ]
  },
  {
    "Title": "Utilize AWS Encryption Solutions for Data at Rest and in Transit",
    "Description": "Ensure that all data at rest is encrypted using AWS native solutions such as AWS KMS, and data in transit is secured using SSL/TLS protocols.",
    "Applicability": "All AWS resources storing or processing sensitive data",
    "Security Risk": "Unencrypted data could lead to unauthorized access and data breaches.",
    "Default Behavior / Limitations": "AWS provides encryption solutions, but implementation depends on customer configuration.",
    "Automation": "Can be monitored using AWS Config rules like `rds-storage-encrypted` and `s3-bucket-server-side-encryption-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/kms/latest/developerguide/overview.html",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/data-protection.html"
    ]
  },
  {
    "Title": "Prohibit Inclusion of Sensitive Data in Tags or Free-Form Text Fields",
    "Description": "Implement policies and monitoring to ensure sensitive information is not included in resource tags or free-form text fields.",
    "Applicability": "All AWS resources utilizing tagging or metadata fields",
    "Security Risk": "Embedding sensitive data in tags or text fields can lead to unauthorized access through metadata retrieval.",
    "Default Behavior / Limitations": "AWS does not natively enforce content of tags or text fields; requires manual checks.",
    "Automation": "Manual validation required; use AWS Lambda functions or custom AWS Config rules for scanning.",
    "References": [
      "https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/data-protection.html"
    ]
  },
  {
    "Title": "Use FIPS 140-3 Validated Cryptographic Modules",
    "Description": "Ensure compliance with federal standards by using FIPS 140-3 validated cryptographic modules for encryption.",
    "Applicability": "AWS accounts requiring compliance with federal regulations",
    "Security Risk": "Non-compliance with encryption standards can lead to legal and operational risks.",
    "Default Behavior / Limitations": "AWS provides FIPS compliance for certain services; users must select these endpoints.",
    "Automation": "Selection of FIPS-compliant endpoints requires manual configuration; no automated enforcement.",
    "References": [
      "https://aws.amazon.com/compliance/fips/",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/data-protection.html"
    ]
  },
  {
    "Title": "Leverage VPC Endpoints for Private AWS Resource Access",
    "Description": "Configure VPC endpoints to access AWS Service Catalog APIs privately, eliminating the need for internet gateways or VPN connections.",
    "Applicability": "All VPCs interacting with AWS Service Catalog",
    "Security Risk": "Using public internet gateways increases exposure to potential attack vectors.",
    "Default Behavior / Limitations": "VPC endpoints are not configured by default; needs manual setup.",
    "Automation": "Can be automated through AWS CloudFormation or custom scripts.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/data-protection.html"
    ]
  }
]
```