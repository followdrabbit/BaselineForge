```json
[
  {
    "Title": "Enforce TLS 1.2 or Higher for Connections to Amazon Aurora",
    "Description": "Amazon Aurora database instances must be configured to only accept secure connections using TLS with a minimum version of TLS 1.2. Additionally, support for TLS 1.3 should be enabled where possible to enhance security.",
    "Applicability": "All Amazon Aurora database instances",
    "Security Risk": "Using outdated versions of TLS exposes connections to vulnerabilities that can compromise data integrity and confidentiality.",
    "Default Behavior / Limitations": "Amazon Aurora does not enforce a minimum TLS version by default. TLS version must be specified in the database cluster parameter group.",
    "Automation": "Monitoring can be implemented using AWS Config with a custom rule to check for this configuration in Amazon Aurora parameter groups.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html",
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Reference.ParameterGroups.html"
    ]
  },
  {
    "Title": "Support Perfect Forward Secrecy Cipher Suites in Amazon Aurora Connections",
    "Description": "Client systems connecting to Amazon Aurora must support cipher suites that offer perfect forward secrecy (PFS) such as DHE or ECDHE.",
    "Applicability": "All client systems connecting to Amazon Aurora",
    "Security Risk": "Without support for PFS, intercepted encrypted traffic remains vulnerable to decryption if the private key is compromised in the future.",
    "Default Behavior / Limitations": "Amazon Aurora supports PFS cipher suites by default, but client configurations need to be verified to ensure they adhere to this standard.",
    "Automation": "Manual validation required to test client systems for compliance with PFS cipher suites.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html"
    ]
  },
  {
    "Title": "Use Signed Requests for Amazon Aurora with IAM Credentials",
    "Description": "Ensure that all requests to Amazon Aurora are signed using AWS CLI/SDKs that utilize an access key ID and a secret access key associated with an IAM principal, or through AWS STS for temporary credentials.",
    "Applicability": "All services and applications interacting with Amazon Aurora",
    "Security Risk": "Unsigned requests can be intercepted and could lead to unauthorized data access or manipulation.",
    "Default Behavior / Limitations": "AWS services typically require signed requests by default, but it's important to ensure all client-side configurations comply.",
    "Automation": "Manual validation required to ensure all client requests are properly signed.",
    "References": [
      "https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html",
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html"
    ]
  }
]
```