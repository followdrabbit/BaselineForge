```json
[
  {
    "Title": "Enforce Multi-Factor Authentication (MFA) for All AWS Accounts",
    "Description": "All AWS user accounts must have MFA enabled to provide an additional layer of security. Configure IAM policies to require MFA for console and CLI access.",
    "Applicability": "All AWS user accounts",
    "Security Risk": "Without MFA, compromised credentials could lead to unauthorized account access, data breaches, and resource manipulation.",
    "Default Behavior / Limitations": "AWS IAM does not enforce MFA by default and requires manual setup.",
    "Automation": "Enforcement can be done using IAM policies and AWS Config rule `iam-user-mfa-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html",
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"
    ]
  },
  {
    "Title": "Ensure SSL/TLS Communication and Require TLS 1.2 or Higher",
    "Description": "Configure all AWS services to communicate using SSL/TLS with a minimum version of TLS 1.2. Update configurations to recommend the use of TLS 1.3 for better security.",
    "Applicability": "All services supporting SSL/TLS communication",
    "Security Risk": "Using outdated TLS versions can expose the service to vulnerabilities and data interception.",
    "Default Behavior / Limitations": "Some AWS services are configured to use TLS by default but version enforcement must be specified.",
    "Automation": "Enforced through service-specific configurations and monitoring via AWS Config for SSL policies.",
    "References": [
      "https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-fsbp-controls.html#fsbp-network-5",
      "https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html"
    ]
  },
  {
    "Title": "Enable CloudTrail for API and User Activity Logging",
    "Description": "Enable AWS CloudTrail for logging all API and user activities across all regions for auditing and monitoring purposes. Ensure management and data events are logged.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without logging, unauthorized or malicious activities may go undetected, complicating compliance and incident response efforts.",
    "Default Behavior / Limitations": "CloudTrail is not enabled by default; it must be configured by the user.",
    "Automation": "Can be automated using AWS CloudTrail setup and AWS Config rule `cloud-trail-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-best-practices.html",
      "https://docs.aws.amazon.com/config/latest/developerguide/cloud-trail-enabled.html"
    ]
  },
  {
    "Title": "Ensure Data Encryption using AWS Solutions",
    "Description": "Ensure that AWS encryption solutions are applied to data both at rest and in transit as per default AWS security controls. Utilize AWS KMS for managing encryption keys.",
    "Applicability": "All AWS services handling sensitive data",
    "Security Risk": "Lack of encryption can lead to data exposure if intercepted during transit or accessed by unauthorized entities in storage.",
    "Default Behavior / Limitations": "AWS provides encryption by default for some services, but user configuration is necessary for full coverage.",
    "Automation": "Automatable via AWS KMS policies and AWS Config rules checking encryption settings.",
    "References": [
      "https://docs.aws.amazon.com/kms/latest/developerguide/overview.html",
      "https://docs.aws.amazon.com/general/latest/gr/aws-security.html"
    ]
  },
  {
    "Title": "Use FIPS-Validated Cryptographic Modules When Required",
    "Description": "Where compliance mandates, configure AWS interactions via CLI or API to use FIPS 140-3 validated endpoints, ensuring cryptographic standards are met.",
    "Applicability": "Environments requiring FIPS compliance",
    "Security Risk": "Non-compliance with cryptographic standards can result in regulatory penalties and insecure data processing.",
    "Default Behavior / Limitations": "FIPS endpoints must be explicitly specified when needed.",
    "Automation": "Manual validation required; AWS documentation provides guidance for FIPS endpoint configurations.",
    "References": [
      "https://docs.aws.amazon.com/general/latest/gr/fips-endpoints.html",
      "https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-options.html"
    ]
  },
  {
    "Title": "Prevent Sensitive Information in Tags and Free-form Fields",
    "Description": "Ensure sensitive information such as personally identifiable information is not entered into AWS resource tags or free-form text fields by establishing strict tagging policies and automated validation.",
    "Applicability": "All AWS resource tags and metadata fields",
    "Security Risk": "Placement of sensitive information in tags could expose it through metadata queries or when logs are reviewed.",
    "Default Behavior / Limitations": "Manual review policies are required to ensure compliance.",
    "Automation": "Manual validation required; AWS provides mechanisms to audit tags, but sensitive data detection requires custom solutions.",
    "References": [
      "https://docs.aws.amazon.com/ARG/latest/userguide/tag-policies.html",
      "https://docs.aws.amazon.com/config/latest/developerguide/tagging.html"
    ]
  }
]
```