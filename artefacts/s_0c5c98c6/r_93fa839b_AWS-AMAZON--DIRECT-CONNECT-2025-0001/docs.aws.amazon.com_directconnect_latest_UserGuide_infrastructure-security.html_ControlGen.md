```json
[
  {
    "Title": "Enforce TLS 1.2 or Later for AWS Direct Connect",
    "Description": "Configure AWS Direct Connect connections to only accept Transport Layer Security (TLS) version 1.2 or later to ensure secure communication.",
    "Applicability": "All AWS Direct Connect clients",
    "Security Risk": "Using outdated TLS versions could expose connections to vulnerabilities, compromising data confidentiality and integrity.",
    "Default Behavior / Limitations": "AWS Direct Connect does not enforce TLS versions by default. Users must configure their clients to use the required TLS version.",
    "Automation": "Can be monitored using AWS Config custom rules or AWS Security Hub to ensure compliance with TLS version requirements.",
    "References": [
      "https://docs.aws.amazon.com/directconnect/latest/UserGuide/infrastructure-security.html"
    ]
  },
  {
    "Title": "Ensure Use of Cipher Suites with Perfect Forward Secrecy (PFS)",
    "Description": "Ensure that clients connecting to AWS Direct Connect support cipher suites that offer Perfect Forward Secrecy (PFS) such as Ephemeral Diffie-Hellman (DHE) or Elliptic Curve Ephemeral Diffie-Hellman (ECDHE).",
    "Applicability": "All AWS Direct Connect clients",
    "Security Risk": "Without PFS, past communications could be decrypted if a private key is compromised, violating confidentiality.",
    "Default Behavior / Limitations": "AWS does not enforce the use of specific cipher suites automatically.",
    "Automation": "Manual validation is required to verify client configuration as AWS does not provide automated tools for enforcing cipher suite compliance.",
    "References": [
      "https://docs.aws.amazon.com/directconnect/latest/UserGuide/infrastructure-security.html"
    ]
  },
  {
    "Title": "Sign AWS Direct Connect Requests with IAM Credentials",
    "Description": "All requests to AWS Direct Connect must be signed using an IAM principal's access key ID and secret access key, or AWS STS-generated temporary security credentials.",
    "Applicability": "All AWS Direct Connect requests",
    "Security Risk": "Unsigned requests can lead to unauthorized operations or data leakage.",
    "Default Behavior / Limitations": "Signing requests is required for authentication; however, improper management of access keys can still pose a risk.",
    "Automation": "IAM and AWS Config can be used to monitor and alert on unsanctioned API usage and key management compliance.",
    "References": [
      "https://docs.aws.amazon.com/directconnect/latest/UserGuide/infrastructure-security.html"
    ]
  },
  {
    "Title": "Implement Resource-Based Access Policies for AWS Direct Connect",
    "Description": "Configure AWS Direct Connect resource-based policies to restrict access based on the source IP address or specific VPC endpoints.",
    "Applicability": "All AWS Direct Connect resources",
    "Security Risk": "Without proper access controls, unauthorized access to Direct Connect resources could occur, leading to potential data leaks or breaches.",
    "Default Behavior / Limitations": "Resource-based policies must be configured by the user; they are not automatically enforced by AWS.",
    "Automation": "AWS Config and IAM policies can be used to enforce and audit the configurations of resource-based access controls.",
    "References": [
      "https://docs.aws.amazon.com/directconnect/latest/UserGuide/infrastructure-security.html"
    ]
  }
]
```