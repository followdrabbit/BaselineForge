```json
[
  {
    "Title": "Enforce Multi-Factor Authentication (MFA) for All AWS Accounts",
    "Description": "Configure AWS IAM to enforce the use of multi-factor authentication (MFA) for all AWS account access, focusing on the AWS Management Console and API access.",
    "Applicability": "All AWS accounts associated with AWS Data Pipeline",
    "Security Risk": "Without MFA, unauthorized users could gain access using compromised credentials, leading to potential data breaches.",
    "Default Behavior / Limitations": "AWS IAM does not enforce MFA by default for all users or accounts. It requires manual configuration.",
    "Automation": "Can be enforced using AWS IAM policies and AWS Config rule `iam-user-mfa-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html"
    ]
  },
  {
    "Title": "Enforce TLS 1.2 or Later for All Communications",
    "Description": "Configure AWS services to use TLS 1.2 or later for all communications with AWS resources. This ensures data is encrypted in transit.",
    "Applicability": "All communications with AWS resources",
    "Security Risk": "Using outdated or no encryption protocols can expose sensitive data to interception or tampering.",
    "Default Behavior / Limitations": "TLS 1.2 is not enforced by default for all services and must be explicitly set.",
    "Automation": "Monitor compliance using AWS Config rules and AWS Security Hub to ensure TLS 1.2 is used.",
    "References": [
      "https://aws.amazon.com/blogs/security/how-to-ensure-that-ssl-tls-traffic-is-encrypted/"
    ]
  },
  {
    "Title": "Enable CloudTrail Logging for AWS API Calls and User Activities",
    "Description": "Ensure AWS CloudTrail is enabled in all regions to log API calls and user activities for auditing and monitoring purposes.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without proper logging, it is difficult to detect unauthorized activities and perform security audits.",
    "Default Behavior / Limitations": "AWS does not enable CloudTrail by default; it must be configured by the user.",
    "Automation": "Can be enforced using the AWS Config rule `cloud-trail-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html"
    ]
  },
  {
    "Title": "Enforce Encryption for All AWS Services",
    "Description": "Use AWS managed encryption solutions to ensure data at rest and in transit is always encrypted. This applies to all supported services.",
    "Applicability": "All AWS services used within AWS Data Pipeline",
    "Security Risk": "Unencrypted data is susceptible to unauthorized access leading to data breaches.",
    "Default Behavior / Limitations": "Not all AWS services are encrypted by default; configurations must be set manually.",
    "Automation": "Monitor and enforce using AWS Config rules and AWS Security Hub.",
    "References": [
      "https://docs.aws.amazon.com/general/latest/gr/aws-sec-standards.html"
    ]
  },
  {
    "Title": "Utilize FIPS 140-2 Validated Endpoints for CLI and API Access",
    "Description": "Configure AWS CLI and API calls to use FIPS endpoints when required, ensuring compliance with federal standards for cryptographic modules.",
    "Applicability": "All environments requiring FIPS compliance",
    "Security Risk": "Non-compliance with FIPS standards can result in weak cryptographic security and violations of regulatory requirements.",
    "Default Behavior / Limitations": "FIPS endpoints must be manually configured; they are not used by default.",
    "Automation": "Manual validation required to ensure endpoints are correctly configured.",
    "References": [
      "https://docs.aws.amazon.com/cli/latest/userguide/cli-fips.html"
    ]
  },
  {
    "Title": "Prevent Storing Sensitive Information in Tags and Free-Form Text Fields",
    "Description": "Implement checks to ensure that sensitive information is not stored in AWS resource tags or free-form text fields.",
    "Applicability": "All AWS resources",
    "Security Risk": "Sensitive data in unstructured fields may be exposed or leaked inadvertently.",
    "Default Behavior / Limitations": "AWS does not automatically scan for sensitive data in tags. Manual checks or third-party tools required.",
    "Automation": "Use AWS Lambda functions and AWS Config rules to scan and notify about policy violations.",
    "References": [
      "https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"
    ]
  },
  {
    "Title": "Ensure IMDSv2 Usage for Amazon EC2 and EMR",
    "Description": "Configure Amazon EC2 instances and EMR clusters to enforce the use of Instance Metadata Service Version 2 (IMDSv2) to enhance security.",
    "Applicability": "Amazon EC2 and EMR instances",
    "Security Risk": "IMDSv1 is vulnerable to SSRF attacks; switching to IMDSv2 mitigates this risk with enhanced controls.",
    "Default Behavior / Limitations": "IMDSv1 is allowed by default; explicit configuration is required to enforce IMDSv2.",
    "Automation": "Enforce using AWS Config rules and setup preventive controls with IAM Instance Profiles.",
    "References": [
      "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html"
    ]
  }
]
```