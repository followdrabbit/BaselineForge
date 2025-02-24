```json
[
    {
        "Description": "Clients accessing Amazon SWF must support Transport Layer Security (TLS) 1.0 or later, with a recommendation for TLS 1.2 or later.",
        "Reference": "Infrastructure Security in Amazon Simple Workflow Service - URL: https://docs.aws.amazon.com/amazonswf/latest/developerguide/infrastructure-security.html",
        "Observations": "Ensure system configurations use TLS 1.2 or later for enhanced security."
    },
    {
        "Description": "Clients must support cipher suites with perfect forward secrecy (PFS) such as Ephemeral Diffie-Hellman (DHE) or Elliptic Curve Ephemeral Diffie-Hellman (ECDHE).",
        "Reference": "Infrastructure Security in Amazon Simple Workflow Service - URL: https://docs.aws.amazon.com/amazonswf/latest/developerguide/infrastructure-security.html",
        "Observations": "Verify that your environment supports these cipher suites for secure communication."
    },
    {
        "Description": "Requests must be signed by using an access key ID and a secret access key that is associated with an IAM principal.",
        "Reference": "Infrastructure Security in Amazon Simple Workflow Service - URL: https://docs.aws.amazon.com/amazonswf/latest/developerguide/infrastructure-security.html",
        "Observations": "Ensure that IAM principals are correctly configured for secure request signing."
    },
    {
        "Description": "Amazon SWF supports resource-based access policies, which can include restrictions based on the source IP address.",
        "Reference": "Infrastructure Security in Amazon Simple Workflow Service - URL: https://docs.aws.amazon.com/amazonswf/latest/developerguide/infrastructure-security.html",
        "Observations": "Implement IP address-based restrictions to control access to Amazon SWF resources."
    },
    {
        "Description": "Amazon SWF policies can control access from specific Amazon Virtual Private Cloud (Amazon VPC) endpoints or specific VPCs.",
        "Reference": "Infrastructure Security in Amazon Simple Workflow Service - URL: https://docs.aws.amazon.com/amazonswf/latest/developerguide/infrastructure-security.html",
        "Observations": "Use VPC endpoint policies to isolate network access to Amazon SWF resources."
    }
]
```