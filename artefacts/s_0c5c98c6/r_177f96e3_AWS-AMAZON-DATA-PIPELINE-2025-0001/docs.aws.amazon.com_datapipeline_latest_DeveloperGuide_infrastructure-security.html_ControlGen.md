```json
[
  {
    "Title": "Enforce Minimum TLS Version for AWS Services",
    "Description": "Configure AWS services to require all client connections to use at least TLS 1.2 for secure data transmission. This can be enforced by setting the minimum TLS version to 1.2 in the configuration of services like AWS Elastic Load Balancer or AWS CloudFront that support this customization.",
    "Applicability": "All AWS services supporting TLS configuration",
    "Security Risk": "Using outdated or insecure TLS versions like 1.0 can expose services to vulnerabilities that could be exploited for data interception or tampering.",
    "Default Behavior / Limitations": "AWS services generally support newer TLS versions by default, but explicit configuration may be required to enforce a minimum version.",
    "Automation": "Can be automated and monitored using AWS Config rules such as `elbv2-desired-tls-policy` to ensure TLS policies are compliant.",
    "References": [
      "https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#describe-ssl-policies",
      "https://aws.amazon.com/about-aws/whats-new/2020/10/aws-announces-support-for-tls-1-2-at-minimum/",
      "https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-fsbp-controls.html"
    ]
  },
  {
    "Title": "Enforce Use of Cipher Suites with Perfect Forward Secrecy (PFS)",
    "Description": "Configure AWS services to only accept cipher suites that support Perfect Forward Secrecy, such as DHE or ECDHE. This can be enforced in services like AWS Elastic Load Balancing and AWS CloudFront by choosing appropriate security policies.",
    "Applicability": "All AWS services with customizable cipher suites",
    "Security Risk": "Using cipher suites without forward secrecy may allow recorded encrypted sessions to be decrypted later if the private key is compromised.",
    "Default Behavior / Limitations": "Certain AWS services provide default configurations with PFS-enabled suites, but verification and explicit configuration may still be required.",
    "Automation": "Compliance can be checked using AWS Config to ensure that the correct TLS policies are applied.",
    "References": [
      "https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#describe-ssl-policies",
      "https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ViewerCertificate.html",
      "https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-fsbp-controls.html"
    ]
  },
  {
    "Title": "Ensure AWS API Requests are Signed with IAM Credentials",
    "Description": "All requests to AWS services must be signed using valid IAM credentials, including an access key ID and a secret access key. Consider using AWS STS for generating temporary credentials to minimize the use of long-term credentials.",
    "Applicability": "All AWS API requests",
    "Security Risk": "Unsigned requests or those signed with incorrect credentials could result in unauthorized access or operations within AWS, leading to data breaches or integrity issues.",
    "Default Behavior / Limitations": "AWS SDKs and CLI by default require requests to be signed with IAM credentials, but it is essential to ensure misuse is prevented.",
    "Automation": "Can be enforced by AWS IAM policies ensuring no APIs are accessible with unsigned requests.",
    "References": [
      "https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html",
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html",
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"
    ]
  }
]
```