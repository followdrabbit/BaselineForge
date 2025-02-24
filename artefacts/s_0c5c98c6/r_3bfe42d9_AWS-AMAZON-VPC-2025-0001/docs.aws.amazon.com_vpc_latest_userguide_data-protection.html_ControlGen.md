```json
[
  {
    "Title": "Implement Least Privilege Access for IAM Users",
    "Description": "Ensure that all IAM or IAM Identity Center users have permissions strictly necessary to fulfill their job duties. Use IAM policies to grant the least privilege.",
    "Applicability": "All users in the AWS environment",
    "Security Risk": "Excessive permissions can lead to unauthorized access and potential data breaches.",
    "Default Behavior / Limitations": "AWS IAM does not enforce least privilege; permissions must be configured according to the principle of least privilege manually.",
    "Automation": "Can be monitored and audited using AWS IAM Access Analyzer or AWS Config to ensure compliance with the least privilege.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html"
    ]
  },
  {
    "Title": "Enforce Multi-Factor Authentication (MFA) Across All Accounts",
    "Description": "Configure AWS accounts so that MFA is enabled for all users, especially those with administrative privileges. Use IAM policies to deny access to the console if MFA is not configured.",
    "Applicability": "All AWS accounts and users",
    "Security Risk": "Without MFA, accounts are susceptible to unauthorized access due to credential compromise.",
    "Default Behavior / Limitations": "AWS IAM does not enable MFA by default. It needs to be configured.",
    "Automation": "Can be enforced using IAM policies and AWS Config rule `iam-user-mfa-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html"
    ]
  },
  {
    "Title": "Enforce TLS 1.2 or Higher for All Communications with AWS",
    "Description": "Ensure that all communications with AWS services utilize SSL/TLS with a minimum of TLS 1.2. Configure AWS service endpoints to enforce this protocol version.",
    "Applicability": "All AWS services and endpoints",
    "Security Risk": "Use of weak SSL/TLS protocols (below TLS 1.2) can lead to data breaches due to interception by malicious actors.",
    "Default Behavior / Limitations": "AWS services generally support TLS 1.2 by default, but configuration should be verified.",
    "Automation": "Monitor using AWS Config and AWS Security Hub for ensuring compliance with minimum TLS settings.",
    "References": [
      "https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/create-https-listener.html"
    ]
  },
  {
    "Title": "Enable AWS CloudTrail for API and User Activity Logging",
    "Description": "Activate AWS CloudTrail for all regions in the account, ensuring all AWS service events are logged. Configure trails to log management and data events.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without logging, unauthorized activities may go undetected, complicating incident response.",
    "Default Behavior / Limitations": "AWS CloudTrail is not enabled by default.",
    "Automation": "Can be enforced using AWS Config rule `cloud-trail-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html"
    ]
  },
  {
    "Title": "Ensure All AWS Data is Encrypted at Rest and in Transit",
    "Description": "Configure AWS services to use encryption solutions for data at rest and in transit. AWS KMS can be used to manage encryption keys.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Unencrypted data is at risk of unauthorized access or theft.",
    "Default Behavior / Limitations": "AWS provides options to encrypt data, but configuration is required.",
    "Automation": "Monitor encryption compliance using AWS Config rules like `rds-storage-encrypted` or `s3-bucket-server-side-encryption-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/general/latest/gr/aws_security.html#aws-security-encryption"
    ]
  },
  {
    "Title": "Deploy Amazon Macie for Sensitive Data Discovery and Protection",
    "Description": "Enable Amazon Macie to discover, classify, and protect sensitive data stored in Amazon S3. Regularly review Macie findings for sensitive data exposure.",
    "Applicability": "All AWS accounts utilizing Amazon S3",
    "Security Risk": "Sensitive data exposure can lead to data breaches and compliance violations.",
    "Default Behavior / Limitations": "Amazon Macie is a paid service and must be enabled manually.",
    "Automation": "Findings can be monitored using AWS Security Hub and Amazon Macie dashboards.",
    "References": [
      "https://docs.aws.amazon.com/macie/latest/userguide/what-is-macie.html"
    ]
  },
  {
    "Title": "Use FIPS Endpoints for Compliance Requirements",
    "Description": "Configure AWS CLI and SDKs to communicate with AWS services using FIPS 140-3 endpoints if required by compliance policies.",
    "Applicability": "All AWS environments where FIPS compliance is necessary",
    "Security Risk": "Non-compliance with federal standards can result in penalties and data protection weaknesses.",
    "Default Behavior / Limitations": "FIPS endpoints are available but must be configured manually.",
    "Automation": "Compliance can be verified through audits of endpoint usage settings.",
    "References": [
      "https://aws.amazon.com/compliance/fips/"
    ]
  },
  {
    "Title": "Prevent Sensitive Information in Tags and Free-Form Text Fields",
    "Description": "Implement tag policies using AWS Organizations to prevent entry of sensitive or confidential information in tags and free-form text fields.",
    "Applicability": "All AWS resources where tagging is used",
    "Security Risk": "Sensitive data in tags can be exposed inadvertently, leading to information leaks.",
    "Default Behavior / Limitations": "Tag policies need to be defined by users.",
    "Automation": "Can be enforced using AWS Organizations Tag Policies.",
    "References": [
      "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html"
    ]
  }
]
```