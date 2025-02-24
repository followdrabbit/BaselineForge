```json
[
  {
    "Title": "Enforce TLS 1.2 or Higher for Amazon RDS",
    "Description": "Ensure that all client connections to Amazon RDS use TLS version 1.2 or higher by configuring the database to reject connections using older protocols.",
    "Applicability": "All Amazon RDS instances",
    "Security Risk": "Older TLS versions have known vulnerabilities that can be exploited, compromising data confidentiality and integrity.",
    "Default Behavior / Limitations": "Amazon RDS supports TLS 1.0, 1.1, 1.2, and in some cases 1.3. Manual configuration is necessary to restrict to 1.2 or higher.",
    "Automation": "Monitor RDS parameter groups to ensure TLS settings are configured using AWS Config rules or AWS Lambda.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html"
    ]
  },
  {
    "Title": "Enforce Perfect Forward Secrecy Cipher Suites for Amazon RDS",
    "Description": "Configure Amazon RDS to accept only cipher suites that offer Perfect Forward Secrecy, such as DHE or ECDHE.",
    "Applicability": "All Amazon RDS instances",
    "Security Risk": "Without Perfect Forward Secrecy, session keys could be compromised if long-term keys are intercepted.",
    "Default Behavior / Limitations": "AWS Managed instances provide support, but explicit configurations may vary by client application settings.",
    "Automation": "Manual validation required to ensure client applications use the required cipher suites.",
    "References": [
      "https://aws.amazon.com/blogs/security/how-to-control-tls-ciphers-in-amazon-rds/"
    ]
  },
  {
    "Title": "Enforce IAM or STS for Amazon RDS Requests",
    "Description": "Ensure all requests to Amazon RDS are signed and authenticated using IAM credentials or AWS STS.",
    "Applicability": "All Amazon RDS API access",
    "Security Risk": "Unsigned requests can lead to unauthorized access and potential data breaches.",
    "Default Behavior / Limitations": "AWS SDKs and CLI enforce signature by default for client-side requests.",
    "Automation": "Can be enforced via IAM policies by auditing API calls using AWS CloudTrail.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html"
    ]
  },
  {
    "Title": "Restrict Amazon RDS Network Access Using Security Groups",
    "Description": "Configure AWS security groups to allow only the minimum necessary inbound and outbound traffic to Amazon RDS instances.",
    "Applicability": "All Amazon RDS instances",
    "Security Risk": "Improperly configured security groups can lead to unauthorized access and potential data breaches.",
    "Default Behavior / Limitations": "By default, all traffic is denied until security group rules are explicitly added.",
    "Automation": "Can be monitored and enforced using AWS Config rules for security group configurations.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html"
    ]
  },
  {
    "Title": "Control Public Accessibility of Amazon RDS Instances",
    "Description": "Ensure that Amazon RDS instances are appropriately configured for public access based on the 'Public accessibility' parameter.",
    "Applicability": "Amazon RDS instances with the public access requirement",
    "Security Risk": "Publicly accessible RDS instances increase the attack surface and risk unauthorized access to the database.",
    "Default Behavior / Limitations": "By default, the public accessibility setting must be manually configured during RDS instance setup.",
    "Automation": "Use AWS Config rules to audit the 'Publicly accessible' settings of RDS instances.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html"
    ]
  }
]
```