```json
[
  {
    "Description": "Amazon MQ must require Transport Layer Security (TLS) version 1.2 or higher for all client connections.",
    "Reference": "Section 'Infrastructure security in Amazon MQ' - URL: https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/infrastructure-security.html",
    "Observations": "TLS 1.3 is recommended for enhanced security."
  },
  {
    "Description": "Amazon MQ must support and prefer cipher suites with Perfect Forward Secrecy (PFS), such as DHE or ECDHE, for securing communications.",
    "Reference": "Section 'Infrastructure security in Amazon MQ' - URL: https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/infrastructure-security.html",
    "Observations": "Ensure Java 7 or later is used as it supports these cipher modes."
  },
  {
    "Description": "All requests to Amazon MQ must be signed using an IAM principal's access key ID and secret access key, or through AWS STS-generated temporary security credentials.",
    "Reference": "Section 'Infrastructure security in Amazon MQ' - URL: https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/infrastructure-security.html",
    "Observations": "This ensures authentication and integrity of the requests."
  }
]
```