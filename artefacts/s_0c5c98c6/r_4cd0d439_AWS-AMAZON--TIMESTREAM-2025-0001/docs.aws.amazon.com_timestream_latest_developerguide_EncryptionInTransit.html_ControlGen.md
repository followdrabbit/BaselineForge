```json
[
  {
    "Title": "Enforce TLS Encryption for AWS Timestream Communications",
    "Description": "All interactions with Amazon Timestream must be encrypted using TLS to ensure confidentiality and integrity of data in transit. Verify that all applications accessing Timestream endpoints are configured to use HTTPS with TLS.",
    "Applicability": "All AWS accounts utilizing Amazon Timestream",
    "Security Risk": "Without TLS, data in transit is vulnerable to interception, posing a threat to confidentiality and integrity.",
    "Default Behavior / Limitations": "Amazon Timestream enforces TLS for all network communications by default.",
    "Automation": "Can be audited using AWS Config to ensure that applications accessing Timestream are using secure HTTPS URLs.",
    "References": [
      "https://docs.aws.amazon.com/timestream/latest/developerguide/EncryptionInTransit.html"
    ]
  }
]
```