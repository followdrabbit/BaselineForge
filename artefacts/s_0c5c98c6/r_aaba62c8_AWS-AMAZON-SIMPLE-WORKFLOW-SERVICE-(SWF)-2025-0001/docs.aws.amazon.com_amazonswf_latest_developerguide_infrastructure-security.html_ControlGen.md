```json
[
    {
        "Title": "Enforce TLS 1.2 or Higher for Amazon SWF Client Connections",
        "Description": "Ensure that all clients accessing Amazon Simple Workflow Service (SWF) are configured to use Transport Layer Security (TLS) version 1.2 or higher. This can typically be enforced by configuring the client's TLS settings in the operational environment.",
        "Applicability": "All client applications accessing Amazon SWF",
        "Security Risk": "Using outdated TLS versions (less than 1.2) exposes data to potential interception and vulnerabilities such as man-in-the-middle attacks, reducing data confidentiality and integrity.",
        "Default Behavior / Limitations": "AWS supports TLS 1.0 and higher, but enforcement of TLS 1.2 must be configured by the client.",
        "Automation": "Manual validation required. Control the minimum TLS version through client application configurations as AWS API does not enforce specific TLS versions.",
        "References": [
            "https://docs.aws.amazon.com/amazonswf/latest/developerguide/infrastructure-security.html"
        ]
    },
    {
        "Title": "Implement Perfect Forward Secrecy (PFS) Cipher Suites",
        "Description": "Configure clients to support cipher suites that provide Perfect Forward Secrecy (PFS), such as DHE or ECDHE, when connecting to Amazon SWF. This requires setting the appropriate cipher suite configurations in the client environment.",
        "Applicability": "All client applications accessing Amazon SWF",
        "Security Risk": "Without PFS, captured encrypted data could potentially be decrypted in the future if the server's private key is compromised, reducing data confidentiality.",
        "Default Behavior / Limitations": "AWS supports PFS cipher suites, but they must be enabled in the client's configuration.",
        "Automation": "Manual validation required. Ensure proper cipher suite configuration on the client side as these settings are client-dependent.",
        "References": [
            "https://docs.aws.amazon.com/amazonswf/latest/developerguide/infrastructure-security.html"
        ]
    },
    {
        "Title": "Sign Requests Using IAM Credentials",
        "Description": "All requests to Amazon SWF must be signed using AWS Signature Version 4, which involves an access key ID and secret access key from an IAM principal. Configure applications to use these credentials for signing requests.",
        "Applicability": "All AWS applications making requests to Amazon SWF",
        "Security Risk": "Unsigned requests can be susceptible to tampering, potentially allowing unauthorized access or operations.",
        "Default Behavior / Limitations": "AWS requires requests to be signed. Enabling AWS SDKs or tools generally facilitates automatic signing.",
        "Automation": "Can be enforced using AWS IAM and SDKs that handle request signing automatically.",
        "References": [
            "https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html"
        ]
    },
    {
        "Title": "Implement Resource-Based Policies with IP Address Restrictions for Amazon SWF",
        "Description": "Use Amazon SWF resource-based access policies to restrict access based on the source IP address. Configure policies to allow access only from specific IP ranges.",
        "Applicability": "Amazon SWF resources accessed over public networks",
        "Security Risk": "Without IP restrictions, resources might be exposed to unauthorized access attempts from arbitrary locations.",
        "Default Behavior / Limitations": "AWS allows resource-based policies, but they must be defined explicitly to include IP address restrictions.",
        "Automation": "Can be enforced using SWF resource policies with specific IP conditions set in policy statements.",
        "References": [
            "https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-about-access-control.html"
        ]
    },
    {
        "Title": "Control Access to Amazon SWF via Specific VPC Endpoints",
        "Description": "Implement VPC endpoint policies to control access to Amazon SWF from specific VPC environments, providing network segmentation and isolation.",
        "Applicability": "Amazon SWF resources accessed within VPC",
        "Security Risk": "Without VPC endpoint policies, cross-network access may be possible, undermining network isolation and exposing resources to unauthorized access.",
        "Default Behavior / Limitations": "AWS supports VPC endpoints, but the associated policies must be explicitly defined to enforce restrictions.",
        "Automation": "Can be enforced using VPC endpoint policies with conditions set for specific VPCs or endpoints.",
        "References": [
            "https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-about-access-control.html"
        ]
    }
]
```