```json
[
  {
    "Title": "Implement Least Privilege Access Control",
    "Description": "Utilize AWS IAM to create individual user accounts, ensuring each user is provided with only the permissions necessary for their job functions. Implement IAM policies that strictly adhere to the principle of least privilege.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Excessive permissions can lead to unauthorized access to sensitive resources, potentially leading to data breaches.",
    "Default Behavior / Limitations": "AWS IAM provides tools for implementing least privilege but requires manual configuration of policies.",
    "Automation": "Enforce using AWS IAM policies and monitor with AWS Config rules such as `iam-user-no-policies` to ensure no users have broad permissions.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"
    ]
  },
  {
    "Title": "Enforce Multi-Factor Authentication (MFA) for All Users",
    "Description": "Enable MFA for all users, including the root AWS account. Ensure that MFA is configured using either virtual MFA devices or physical MFA tokens.",
    "Applicability": "All AWS accounts and users",
    "Security Risk": "Without MFA, compromised credentials can lead to unauthorized access to AWS resources.",
    "Default Behavior / Limitations": "AWS does not enforce MFA by default; it must be configured for each user.",
    "Automation": "Monitor compliance using AWS Config rule `root-account-mfa-enabled` and `iam-user-mfa-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable.html"
    ]
  },
  {
    "Title": "Enforce TLS 1.2 or Higher for AWS and Amazon SWF Communications",
    "Description": "Ensure all communications with AWS resources, including Amazon SWF, are conducted over TLS 1.2 or higher. Configure AWS services and clients to reject connections using older TLS versions.",
    "Applicability": "All AWS services using network communication and all client applications accessing Amazon SWF",
    "Security Risk": "Older versions of TLS may have known vulnerabilities exploitable by attackers.",
    "Default Behavior / Limitations": "AWS services support TLS 1.2 by default, but explicit configurations may be required for some services and client applications.",
    "Automation": "Manual validation required for clients; AWS Config custom rules can validate AWS service configurations.",
    "References": [
      "https://docs.aws.amazon.com/general/latest/gr/aws-security-certificates.html",
      "https://docs.aws.amazon.com/amazonswf/latest/developerguide/infrastructure-security.html"
    ]
  },
  {
    "Title": "Enable and Configure AWS CloudTrail in All Regions",
    "Description": "Enable AWS CloudTrail for all AWS accounts in all regions to capture API calls and user activity. Configure CloudTrail to send logs to Amazon S3 for centralized storage.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without proper logging, unauthorized activities may go unnoticed, leading to undetected security incidents.",
    "Default Behavior / Limitations": "CloudTrail must be manually enabled and configured.",
    "Automation": "Enforce using AWS Config rule `cloud-trail-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html"
    ]
  },
  {
    "Title": "Implement AWS Managed Encryption Solutions",
    "Description": "Utilize AWS KMS or default encryption options in AWS services to encrypt data at rest and in transit. Configure policies to automatically use encryption for new resources.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Data without encryption is vulnerable to unauthorized access and breaches.",
    "Default Behavior / Limitations": "Some AWS services enable encryption by default, but it requires configuration for comprehensive coverage.",
    "Automation": "Enforce using AWS Config rules like `s3-bucket-server-side-encryption-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/kms/latest/developerguide/overview.html"
    ]
  },
  {
    "Title": "Use Amazon Macie for S3 Data Security",
    "Description": "Enable Amazon Macie to discover and protect sensitive data stored in Amazon S3 buckets. Configure policies to automate data classification and security alerts.",
    "Applicability": "All AWS accounts with S3 usage",
    "Security Risk": "Unprotected sensitive data can lead to data breaches and compliance violations.",
    "Default Behavior / Limitations": "Amazon Macie requires activation and configuration for each account.",
    "Automation": "Manage using AWS Security Hub to monitor Macie findings.",
    "References": [
      "https://docs.aws.amazon.com/macie/latest/userguide/what-is-macie.html"
    ]
  },
  {
    "Title": "Use FIPS-Validated Endpoints for Compliance",
    "Description": "If required by compliance, access AWS services via FIPS 140-3 validated endpoints to ensure cryptographic standards are met.",
    "Applicability": "All AWS accounts where FIPS compliance is necessary",
    "Security Risk": "Non-compliance with cryptographic standards can lead to regulatory breaches and security vulnerabilities.",
    "Default Behavior / Limitations": "Must manually configure applications to use FIPS endpoints.",
    "Automation": "Manual validation required to ensure the use of correct endpoints.",
    "References": [
      "https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#fips-endpoints"
    ]
  },
  {
    "Title": "Prevent Sensitive Data Exposure in Tags and Metadata",
    "Description": "Implement tagging policies to prevent the inclusion of sensitive information in tags or metadata fields in AWS resources. Regularly audit tags using automated scripts.",
    "Applicability": "All AWS resources",
    "Security Risk": "Exposed sensitive information can lead to data leaks and security vulnerabilities.",
    "Default Behavior / Limitations": "AWS does not enforce content checks on tags by default.",
    "Automation": "Manual review recommended; consider custom scripts for automated tag audits.",
    "References": [
      "https://docs.aws.amazon.com/organizations/latest/userguide/tag-policies.html"
    ]
  },
  {
    "Title": "Configure Interface VPC Endpoint for Amazon SWF",
    "Description": "Create an interface VPC endpoint within Amazon VPC to connect to Amazon SWF, eliminating the need for an internet gateway, NAT instance, or VPN connection.",
    "Applicability": "All Amazon VPC environments needing communication with Amazon SWF",
    "Security Risk": "Without using a VPC endpoint, communication with Amazon SWF may require internet access, increasing the attack surface.",
    "Default Behavior / Limitations": "VPC endpoints for Amazon SWF are not enabled by default.",
    "Automation": "Can be automated with AWS CloudFormation templates and monitored with AWS Config.",
    "References": [
      "https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-vpc-endpoints.html"
    ]
  },
  {
    "Title": "Attach IAM Endpoint Policy for Amazon SWF VPC Endpoint",
    "Description": "Attach a specific AWS IAM endpoint policy during the creation of a VPC endpoint for Amazon SWF to control access and enforce fine-grained access controls.",
    "Applicability": "All AWS VPCs with endpoint connections to Amazon SWF",
    "Security Risk": "Without endpoint policies, connections could allow unrestricted access, leading to potential data leakage.",
    "Default Behavior / Limitations": "IAM policies need to be specified; no default endpoint policy is associated with VPC endpoints.",
    "Automation": "Attach and audit endpoint policies using AWS IAM and AWS Config.",
    "References": [
      "https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-vpc-endpoints.html"
    ]
  },
  {
    "Title": "Capture Amazon SWF API Calls with AWS CloudTrail",
    "Description": "Enable logging of all API calls to Amazon SWF using AWS CloudTrail. This ensures all actions taken via both the SWF console and API are recorded for auditing and monitoring.",
    "Applicability": "All AWS accounts using Amazon SWF",
    "Security Risk": "Without logging API calls, it's challenging to track access and changes to Amazon SWF resources.",
    "Default Behavior / Limitations": "CloudTrail supports logging of SWF API calls, but it must be explicitly configured.",
    "Automation": "Enforce using AWS CloudTrail.",
    "References": [
      "https://docs.aws.amazon.com/amazonswf/latest/developerguide/ct-logging.html"
    ]
  },
  {
    "Title": "Enforce IAM Authentication and Authorization for Amazon SWF",
    "Description": "Ensure all requests to Amazon SWF require authentication using IAM. Configure IAM policies to specify permissions for each user or role accessing SWF resources.",
    "Applicability": "All users and roles accessing Amazon SWF",
    "Security Risk": "Without authenticated requests and defined permissions, unauthorized access could lead to data loss or service disruption.",
    "Default Behavior / Limitations": "IAM requires explicit permission grants; no permissions are provided by default.",
    "Automation": "Enforced using IAM policies and monitored via AWS IAM Access Analyzer.",
    "References": [
      "https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html"
    ]
  }
]
```