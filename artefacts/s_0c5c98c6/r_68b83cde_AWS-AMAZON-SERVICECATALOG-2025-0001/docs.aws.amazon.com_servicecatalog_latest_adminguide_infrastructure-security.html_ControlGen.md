```json
[
  {
    "Title": "Enforce TLS 1.2 or 1.3 for AWS Service Catalog Communications",
    "Description": "Configure AWS Service Catalog and all interacting client systems to enforce Transport Layer Security (TLS) version 1.2 or 1.3 for all communications to ensure encryption and secure communication channels.",
    "Applicability": "All AWS accounts using AWS Service Catalog",
    "Security Risk": "Using outdated versions of TLS increases the risk of eavesdropping, man-in-the-middle attacks, and data breaches due to vulnerabilities in older protocols.",
    "Default Behavior / Limitations": "AWS services typically require TLS 1.2 or higher by default, but client systems interfacing with AWS must also be configured to support it.",
    "Automation": "Monitor and enforce using AWS Config rule `tls-v12-enabled` to validate enforcement of TLS 1.2 or 1.3 on connected resources.",
    "References": [
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/infrastructure-security.html",
      "https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-fsbp-controls.html"
    ]
  },
  {
    "Title": "Enforce Use of Cipher Suites with Perfect Forward Secrecy (PFS)",
    "Description": "Ensure that all communication with AWS Service Catalog utilizes cipher suites that support Perfect Forward Secrecy (PFS) such as DHE or ECDHE to enhance session security and protect past sessions from future compromises.",
    "Applicability": "All AWS accounts using AWS Service Catalog",
    "Security Risk": "Without PFS, compromised server keys could lead to the decryption of past sessions, compromising data confidentiality.",
    "Default Behavior / Limitations": "AWS services often prefer or enforce PFS-enabled cipher suites, but client-side configurations must be verified.",
    "Automation": "Manual validation required; verify configurations for compatibility with PFS-enabled cipher suites.",
    "References": [
      "https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-tls-listener.html",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/infrastructure-security.html"
    ]
  },
  {
    "Title": "Sign All Requests to AWS Service Catalog Using IAM Credentials or STS",
    "Description": "Configure all API requests to AWS Service Catalog to be signed using AWS Signature Version 4 with an IAM user's access key ID and secret access key or temporary credentials from AWS Security Token Service (STS).",
    "Applicability": "All AWS accounts using AWS Service Catalog",
    "Security Risk": "Unsigned or improperly signed requests can lead to unauthorized access or man-in-the-middle attacks, threatening the integrity and confidentiality of requests.",
    "Default Behavior / Limitations": "AWS requires requests to be signed, but correct configuration is necessary for enforcement.",
    "Automation": "Verify through AWS CloudTrail to monitor API calls and check for signed requests.",
    "References": [
      "https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/infrastructure-security.html"
    ]
  },
  {
    "Title": "Control AWS Service Catalog Product Availability by Region",
    "Description": "Use the AWS Service Catalog `CopyProduct` API to control in which AWS Regions your portfolios and products are available, ensuring data residency and compliance requirements are met.",
    "Applicability": "All AWS accounts using AWS Service Catalog",
    "Security Risk": "Unrestricted data placement across regions can lead to compliance violations and data sovereignty issues.",
    "Default Behavior / Limitations": "Manual configuration required; AWS does not restrict region replication by default for products.",
    "Automation": "Utilize AWS CloudFormation or AWS Service Catalog APIs for automated deployment and management of products across specific regions.",
    "References": [
      "https://docs.aws.amazon.com/servicecatalog/latest/dg/API_CopyProduct.html",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/infrastructure-security.html"
    ]
  }
]
```