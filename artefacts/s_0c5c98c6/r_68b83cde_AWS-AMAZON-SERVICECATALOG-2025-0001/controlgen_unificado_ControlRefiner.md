```json
[
  {
    "Title": "Enforce Multi-Factor Authentication (MFA) for All AWS Accounts",
    "Description": "Ensure that all AWS accounts have multi-factor authentication (MFA) enabled, particularly for users with administrative privileges. Implement IAM policies to deny access if MFA is not enabled.",
    "Applicability": "All AWS accounts with IAM users",
    "Security Risk": "Without MFA, accounts are susceptible to unauthorized access, increasing the risk of data breaches or unauthorized actions.",
    "Default Behavior / Limitations": "AWS IAM does not enforce MFA by default. It requires manual configuration.",
    "Automation": "Can be enforced using IAM policies and AWS Config rule `iam-user-mfa-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html"
    ]
  },
  {
    "Title": "Enforce TLS 1.2 or Higher for Communication",
    "Description": "Ensure all AWS resources use SSL/TLS for communication, requiring TLS 1.2 as a minimum and recommending TLS 1.3 where possible. Implement security policies and network settings to enforce these protocols.",
    "Applicability": "All services communicating with AWS resources",
    "Security Risk": "Communication using outdated protocols can result in data interception and man-in-the-middle attacks.",
    "Default Behavior / Limitations": "AWS supports TLS 1.2 or higher, but enforcement is dependent on customer configuration.",
    "Automation": "Can be monitored using AWS Config rules like `cloudfront-encryption-protocols-policy`.",
    "References": [
      "https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html"
    ]
  },
  {
    "Title": "Enable and Configure AWS CloudTrail for Comprehensive Logging",
    "Description": "Enable AWS CloudTrail in all regions and configure it to log management and data events for auditing API calls and changes within the account.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without logging, unauthorized activities might remain undetected, impeding audit and traceability.",
    "Default Behavior / Limitations": "AWS CloudTrail is available but not enabled by default.",
    "Automation": "Can be enforced using AWS Config rule `cloud-trail-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html"
    ]
  },
  {
    "Title": "Utilize AWS Encryption Solutions for Data Protection",
    "Description": "Ensure that all data at rest is encrypted using AWS-native solutions such as AWS KMS, and secure data in transit using SSL/TLS protocols.",
    "Applicability": "All AWS resources storing or processing sensitive data",
    "Security Risk": "Unencrypted data is vulnerable to unauthorized access and breaches.",
    "Default Behavior / Limitations": "AWS provides encryption solutions, but implementation requires customer configuration.",
    "Automation": "Monitored through AWS Config rules like `s3-bucket-server-side-encryption-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/kms/latest/developerguide/overview.html"
    ]
  },
  {
    "Title": "Prohibit Sensitive Data in Tags or Free-Form Text",
    "Description": "Implement policies and monitoring to prevent the inclusion of sensitive information in resource tags or free-form text fields.",
    "Applicability": "All AWS resources utilizing tagging or metadata",
    "Security Risk": "Exposure through metadata retrieval if sensitive data is included in tags.",
    "Default Behavior / Limitations": "AWS does not natively enforce tag content; manual checks required.",
    "Automation": "Manual validation required; AWS Lambda functions or custom AWS Config rules can be used.",
    "References": [
      "https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"
    ]
  },
  {
    "Title": "Leverage VPC Endpoints for Private Access",
    "Description": "Configure Virtual Private Cloud (VPC) endpoints to privately access AWS resources, reducing dependency on internet gateways.",
    "Applicability": "All VPCs interacting with AWS services",
    "Security Risk": "Public internet gateways increase exposure to potential attack vectors.",
    "Default Behavior / Limitations": "VPC endpoints are not configured by default; manual setup required.",
    "Automation": "Can be automated using AWS CloudFormation or scripts.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html"
    ]
  },
  {
    "Title": "Ensure Use of FIPS 140-3 Validated Cryptographic Modules",
    "Description": "Configure services to use FIPS 140-3 validated cryptographic modules where compliance with federal standards is required.",
    "Applicability": "AWS accounts under federal compliance requirements",
    "Security Risk": "Non-compliance can lead to legal and regulatory challenges.",
    "Default Behavior / Limitations": "AWS offers FIPS-compliant endpoints; user selection is required.",
    "Automation": "Manual configuration of FIPS-compliant endpoints is necessary.",
    "References": [
      "https://aws.amazon.com/compliance/fips/"
    ]
  },
  {
    "Title": "Ensure CloudTrail Logs for Service Catalog API Calls",
    "Description": "AWS CloudTrail must capture all API calls to AWS Service Catalog, ensuring logs are delivered to a secure Amazon S3 bucket.",
    "Applicability": "All AWS accounts using AWS Service Catalog",
    "Security Risk": "Without logging, unauthorized actions could go undetected, leading to security incidents.",
    "Default Behavior / Limitations": "CloudTrail logging must be manually configured for AWS Service Catalog.",
    "Automation": "Use AWS Config to ensure CloudTrail is logging AWS Service Catalog API calls.",
    "References": [
      "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html"
    ]
  },
  {
    "Title": "Implement AWS Service Catalog Configuration and Constraints",
    "Description": "Apply template constraints within AWS Service Catalog for CloudFormation templates to control parameter values, and ensure restrictive constraints for product provisioning.",
    "Applicability": "All products and services deployed via AWS Service Catalog",
    "Security Risk": "Lack of constraints may lead to non-compliance and security vulnerabilities.",
    "Default Behavior / Limitations": "Constraints are not applied by default; customers must specify them.",
    "Automation": "Managed through AWS Service Catalog configurations.",
    "References": [
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security-best-practices.html"
    ]
  }
]
```