```json
[
  {
    "Title": "Enforce TLS 1.2 or Higher for Amazon MQ Client Connections",
    "Description": "Configure Amazon MQ to enforce TLS 1.2 or higher for all client connections to ensure secure communications. While TLS 1.3 is recommended for enhanced security, TLS 1.2 is the minimum acceptable level.",
    "Applicability": "All Amazon MQ client connections",
    "Security Risk": "Without enforcing TLS 1.2 or higher, data transmitted between clients and Amazon MQ can be susceptible to eavesdropping or man-in-the-middle attacks.",
    "Default Behavior / Limitations": "TLS 1.2 is the minimum version accepted by Amazon MQ as part of the AWS default security configuration.",
    "Automation": "Manual verification is required to ensure that TLS settings are configured appropriately in Amazon MQ as AWS does not provide an automated way to enforce a specific TLS version beyond the default settings.",
    "References": [
      "https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/infrastructure-security.html"
    ]
  },
  {
    "Title": "Support Cipher Suites with Perfect Forward Secrecy in Amazon MQ",
    "Description": "Configure Amazon MQ to use and prefer cipher suites that support Perfect Forward Secrecy (PFS), such as DHE or ECDHE, to maintain the confidentiality of communications even if the server's private key is compromised.",
    "Applicability": "All Amazon MQ client connections",
    "Security Risk": "Without PFS, intercepted data can be decrypted retroactively if the server's private key is compromised, jeopardizing the confidentiality of communications.",
    "Default Behavior / Limitations": "Selection of cipher suites is configured through the client and server settings. Ensure the environment uses Java 7 or later for compatibility.",
    "Automation": "Manual configuration on the client and server sides is required to ensure the use of cipher suites supporting PFS. AWS Config cannot enforce this setting.",
    "References": [
      "https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/infrastructure-security.html"
    ]
  },
  {
    "Title": "Sign Amazon MQ Requests with AWS Credentials",
    "Description": "All requests to Amazon MQ must be signed using either an IAM principal's access key ID and secret access key or through AWS STS-generated temporary security credentials to ensure authentication and integrity.",
    "Applicability": "All requests to Amazon MQ",
    "Security Risk": "Not signing requests can lead to unauthorized requests being made or request tampering, compromising the integrity and security of the messages.",
    "Default Behavior / Limitations": "Requests can be signed using AWS Signature Version 4; however, it's the responsibility of the client application to properly implement signing.",
    "Automation": "AWS Config can be used to monitor IAM policies and credentials usage but cannot enforce signing directly.",
    "References": [
      "https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/infrastructure-security.html"
    ]
  }
]
```