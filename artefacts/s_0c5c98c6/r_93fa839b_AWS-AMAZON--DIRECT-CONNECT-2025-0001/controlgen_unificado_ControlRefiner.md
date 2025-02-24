```json
[
  {
    "Title": "Implement Multi-Factor Authentication (MFA) for AWS Accounts",
    "Description": "Enable MFA for all AWS accounts to enhance security and prevent unauthorized access. Configure IAM policies to require MFA for accessing sensitive resources and monitor compliance using AWS Config.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without MFA, unauthorized individuals may gain access to AWS accounts, potentially leading to data breaches and unauthorized changes.",
    "Default Behavior / Limitations": "AWS does not enable MFA by default; it requires manual configuration.",
    "Automation": "Can be enforced using IAM policies and AWS Config with the `iam-user-mfa-enabled` rule.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html"
    ]
  },
  {
    "Title": "Enforce Data Encryption at Rest and In Transit Using AWS Services",
    "Description": "Use AWS KMS or AWS-managed keys to encrypt data at rest for various AWS services, and enforce TLS 1.2 or higher to secure data in transit. Utilize AWS Config to verify encryption compliance.",
    "Applicability": "All data storage and transmission within AWS",
    "Security Risk": "Unencrypted data may be exposed to unauthorized access and tampering, compromising confidentiality and integrity.",
    "Default Behavior / Limitations": "Many AWS services provide encryption by default, but specific configuration is necessary for compliance with customer policies.",
    "Automation": "Enable using AWS Config rules to verify encryption for both data at rest and in transit.",
    "References": [
      "https://docs.aws.amazon.com/kms/latest/developerguide/overview.html",
      "https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-tls.html"
    ]
  },
  {
    "Title": "Enable API and User Activity Logging with AWS CloudTrail",
    "Description": "Configure AWS CloudTrail to log all API calls and user activities, including management and data events, across accounts and regions for auditing purposes.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without logging, unauthorized actions may go undetected, hindering incident detection and forensic capabilities.",
    "Default Behavior / Limitations": "AWS CloudTrail is not enabled by default for all activities; configuration is necessary.",
    "Automation": "Enforceable using AWS Config with the `cloudtrail-enabled` rule.",
    "References": [
      "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html"
    ]
  },
  {
    "Title": "Protect Sensitive Data in Amazon S3 with Amazon Macie",
    "Description": "Leverage Amazon Macie to automatically discover, classify, and protect sensitive data stored in Amazon S3, ensuring compliance with data protection regulations.",
    "Applicability": "All S3 buckets containing sensitive data",
    "Security Risk": "Unprotected sensitive data can lead to data breaches and compliance violations.",
    "Default Behavior / Limitations": "Amazon Macie requires explicit setup and configurations.",
    "Automation": "Automated through Amazon Macie setup and integrations.",
    "References": [
      "https://docs.aws.amazon.com/macie/latest/user-guide/what-is-macie.html"
    ]
  },
  {
    "Title": "Ensure AWS Direct Connect is Secured with Encryption",
    "Description": "Use IPsec VPN or MACsec for AWS Direct Connect connections to encrypt data in transit, ensuring confidentiality and integrity between on-premises networks and AWS.",
    "Applicability": "All AWS Direct Connect connections",
    "Security Risk": "Without encryption, data is susceptible to interception, compromising confidentiality and data integrity.",
    "Default Behavior / Limitations": "AWS Direct Connect does not encrypt traffic in transit by default; manual configuration is required.",
    "Automation": "Monitored using AWS Config for compliance with encryption requirements.",
    "References": [
      "https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-in-transit.html"
    ]
  },
  {
    "Title": "Configure CloudWatch Alarms for AWS Direct Connect",
    "Description": "Set up Amazon CloudWatch Alarms for AWS Direct Connect to monitor essential metrics. Configure alarms to trigger actions like notifications or scale actions when thresholds are crossed.",
    "Applicability": "All AWS Direct Connect connections",
    "Security Risk": "Without CloudWatch Alarms, issues like network downtime or unexpected data transfer spikes could go undetected.",
    "Default Behavior / Limitations": "CloudWatch Alarms require manual setup and configuration for each metric and action.",
    "Automation": "Can be automated using AWS CloudFormation or AWS CLI.",
    "References": [
      "https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html"
    ]
  },
  {
    "Title": "Avoid Storing Sensitive Information in AWS Tags and Text Fields",
    "Description": "Ensure that no confidential or sensitive information is stored in free-form text fields or tags within AWS resources to prevent exposure in logs.",
    "Applicability": "All AWS resources across accounts",
    "Security Risk": "Sensitive data in tags or text fields can lead to privacy violations if exposed.",
    "Default Behavior / Limitations": "AWS does not restrict sensitive data entry in tags by default.",
    "Automation": "Requires manual policy enforcement; AWS Config can alert on detected sensitive patterns.",
    "References": [
      "https://docs.aws.amazon.com/directconnect/latest/UserGuide/data-protection.html"
    ]
  },
  {
    "Title": "Sign AWS Direct Connect Requests with IAM Credentials",
    "Description": "Ensure all requests to AWS Direct Connect are signed using an IAM access key or AWS STS-generated credentials to authenticate operations.",
    "Applicability": "All AWS Direct Connect requests",
    "Security Risk": "Unsigned requests can lead to unauthorized operations or data leakage.",
    "Default Behavior / Limitations": "Signing requests is required for authentication; proper management of access keys is essential.",
    "Automation": "IAM and AWS Config can monitor and alert on unsanctioned API usage.",
    "References": [
      "https://docs.aws.amazon.com/directconnect/latest/UserGuide/infrastructure-security.html"
    ]
  },
  {
    "Title": "Implement Resource-Based Access Policies for AWS Direct Connect",
    "Description": "Ensure AWS Direct Connect resource-based policies are in place to restrict access based on source IP or specific VPC endpoints.",
    "Applicability": "All AWS Direct Connect resources",
    "Security Risk": "Without proper access controls, unauthorized access to Direct Connect resources could occur.",
    "Default Behavior / Limitations": "Resource-based policies must be configured by the user.",
    "Automation": "Use AWS Config and IAM policies to enforce and audit resource-based access controls.",
    "References": [
      "https://docs.aws.amazon.com/directconnect/latest/UserGuide/infrastructure-security.html"
    ]
  }
]
```