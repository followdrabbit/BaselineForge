```json
[
  {
    "Title": "Enforce TLS 1.2 or Higher for AWS Global Accelerator",
    "Description": "Ensure that all communications with AWS Global Accelerator use Transport Layer Security (TLS) version 1.2 or higher. Configure AWS Global Accelerator to reject connections that do not meet this requirement.",
    "Applicability": "All clients accessing AWS Global Accelerator",
    "Security Risk": "Using TLS versions below 1.2 exposes communications to vulnerabilities such as POODLE and BEAST attacks, compromising confidentiality and integrity.",
    "Default Behavior / Limitations": "AWS Global Accelerator supports TLS 1.2 and higher by default, however, enforcement must be configured.",
    "Automation": "This can be partially automated using AWS Global Accelerator settings. Continuous monitoring is recommended via AWS Config or AWS CloudTrail logs for connections using outdated protocols.",
    "References": [
      "https://docs.aws.amazon.com/global-accelerator/latest/dg/infrastructure-security.html"
    ]
  },
  {
    "Title": "Require Perfect Forward Secrecy (PFS) Cipher Suites for AWS Global Accelerator",
    "Description": "Ensure that AWS Global Accelerator only accepts connections encrypted with cipher suites that support perfect forward secrecy (PFS), such as DHE or ECDHE.",
    "Applicability": "All clients accessing AWS Global Accelerator",
    "Security Risk": "Without PFS, the compromise of a private key can lead to decryption of all past and future sessions even if encrypted.",
    "Default Behavior / Limitations": "Supported depending on client configuration. Ensure client systems support required cipher suites.",
    "Automation": "Monitor and enforce compliance via AWS Config or custom CloudWatch metrics by inspecting SSL/TLS client connections to verify cipher suite usage.",
    "References": [
      "https://docs.aws.amazon.com/global-accelerator/latest/dg/infrastructure-security.html"
    ]
  },
  {
    "Title": "Enforce Signed Requests for AWS Global Accelerator",
    "Description": "All API requests to AWS Global Accelerator must be signed using the caller's IAM principal credentials. This includes using access key ID, secret access key, or temporary security credentials obtained via AWS Security Token Service (STS).",
    "Applicability": "All API requests to AWS Global Accelerator",
    "Security Risk": "Unsigned requests can lead to unauthorized operations, making it difficult to attribute actions to specific users, affecting accountability.",
    "Default Behavior / Limitations": "AWS API requests require signature, but correct implementation must be ensured on client-side.",
    "Automation": "Enforce and monitor using AWS CloudTrail and AWS Config to ensure all requests are signed and track compliance against IAM policies.",
    "References": [
      "https://docs.aws.amazon.com/global-accelerator/latest/dg/infrastructure-security.html",
      "https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html"
    ]
  }
]
```