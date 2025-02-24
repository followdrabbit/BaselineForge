```json
[
  {
    "Title": "Encrypt Data at Rest in Timestream Using AWS KMS",
    "Description": "Ensure all data stored in AWS Timestream is encrypted at rest using AWS KMS-managed encryption keys. This is automatically handled by AWS using the service default key.",
    "Applicability": "All AWS Timestream services storing user data",
    "Security Risk": "If data is not encrypted at rest, it could be vulnerable to unauthorized access or data breaches.",
    "Default Behavior / Limitations": "AWS Timestream encrypts all user data at rest by default using a service-managed key (AWS owned CMK). Service default keys cannot be disabled.",
    "Automation": "This control is automatically enforced by AWS; no additional configuration is needed.",
    "References": [
      "https://docs.aws.amazon.com/timestream/latest/developerguide/best-practices-security-preventative.html"
    ]
  },
  {
    "Title": "Use IAM Roles for Accessing AWS Timestream",
    "Description": "Configure applications and EC2 instances to use IAM roles to obtain temporary access keys for accessing AWS Timestream, avoiding hardcoding AWS credentials.",
    "Applicability": "All applications and EC2 instances accessing AWS Timestream",
    "Security Risk": "Storing AWS credentials directly increases the risk of compromising long-term credentials, leading to unauthorized access.",
    "Default Behavior / Limitations": "IAM provides the mechanism to use roles, but implementation must be done by the user.",
    "Automation": "Can be enforced and audited through AWS IAM by implementing role-based access controls.",
    "References": [
      "https://docs.aws.amazon.com/timestream/latest/developerguide/best-practices-security-preventative.html"
    ]
  },
  {
    "Title": "Implement Least Privilege for Timestream Access",
    "Description": "Create and apply IAM policies that grant the minimum permissions necessary to access Timestream APIs and resources. Use AWS managed policies, customer managed policies, or tag-based authorization as needed.",
    "Applicability": "All AWS accounts using Timestream",
    "Security Risk": "Excessive permissions can lead to unintentional data exposure, modification, or deletion.",
    "Default Behavior / Limitations": "AWS provides IAM policies, but users must enforce least privilege manually.",
    "Automation": "Use AWS IAM to manage and audit permissions, and AWS Config rules to monitor policy compliance.",
    "References": [
      "https://docs.aws.amazon.com/timestream/latest/developerguide/best-practices-security-preventative.html"
    ]
  },
  {
    "Title": "Consider Client-Side Encryption for Sensitive Data in Timestream",
    "Description": "To protect sensitive data throughout its lifecycle, implement client-side encryption before storing data in Timestream. Ensure only encrypted data is transmitted and stored, maintaining confidentiality in transit and at rest.",
    "Applicability": "Any application handling sensitive or confidential data stored in Timestream",
    "Security Risk": "Without client-side encryption, sensitive data may be exposed to unauthorized entities during transit or storage.",
    "Default Behavior / Limitations": "Client-side encryption must be implemented by the application. AWS does not enforce this automatically.",
    "Automation": "Manual validation required. Implement using cryptographic libraries in the client application.",
    "References": [
      "https://docs.aws.amazon.com/timestream/latest/developerguide/best-practices-security-preventative.html"
    ]
  }
]
```