```json
[
  {
    "Title": "Enforce Encryption at Rest Using Nitro Security Key for AWS Outposts",
    "Description": "Configure data in AWS Outposts to be encrypted at rest using a Nitro Security Key (NSK) to ensure secure data storage and decryption processes.",
    "Applicability": "All AWS Outposts deployments",
    "Security Risk": "Without encryption at rest using NSK, sensitive data may be vulnerable to unauthorized access if physical security of Outposts is compromised.",
    "Default Behavior / Limitations": "AWS Outposts requires manual configuration to use Nitro Security Keys for encryption.",
    "Automation": "Can be audited using AWS CloudTrail logs to monitor NSK creation, handling, and destruction events.",
    "References": [
      "https://docs.aws.amazon.com/outposts/latest/userguide/data-protection.html"
    ]
  },
  {
    "Title": "Enforce Amazon EBS Encryption for Volumes and Snapshots",
    "Description": "Enable Amazon EBS encryption using AWS KMS and enforce KMS key policies to protect EBS volumes and snapshots at rest.",
    "Applicability": "All EC2 instances using EBS volumes and snapshots",
    "Security Risk": "Unencrypted EBS volumes and snapshots can lead to data breaches if compromised during migration or from inside threats.",
    "Default Behavior / Limitations": "AWS does not automatically encrypt EBS volumes. This must be enabled individually for each volume.",
    "Automation": "Can be enforced and monitored using AWS Config rules `ebs-encrypted-volumes` and IAM policies for KMS key management.",
    "References": [
      "https://docs.aws.amazon.com/outposts/latest/userguide/data-protection.html"
    ]
  },
  {
    "Title": "Verify End-to-End Encryption for Data In Transit Between Outpost and AWS Region",
    "Description": "Ensure that all data in transit between AWS Outposts and its AWS Region is encrypted using AWS-provided mechanisms to prevent unauthorized interception.",
    "Applicability": "All AWS Outposts deployments communicating with AWS Regions",
    "Security Risk": "Data interception or tampering could occur if in-transit encryption mechanisms are bypassed or improperly configured.",
    "Default Behavior / Limitations": "AWS encrypts data in transit by default but verification of the encryption setup is needed.",
    "Automation": "Verification requires manual review as AWS handles encryption in transit, but logging and monitoring can be implemented for traffic patterns.",
    "References": [
      "https://docs.aws.amazon.com/outposts/latest/userguide/data-protection.html"
    ]
  },
  {
    "Title": "Enforce TLS for Encrypting Sensitive Data in Transit Through Local Gateways",
    "Description": "Implement TLS protocols for securing sensitive data transmitted through local gateways connecting Outposts to local networks.",
    "Applicability": "All local network connections through Outpost local gateways",
    "Security Risk": "Without TLS, sensitive data could be exposed to network eavesdropping and unauthorized access.",
    "Default Behavior / Limitations": "TLS is not enforced by AWS for all customer local gateway configurations; it must be configured by the user.",
    "Automation": "Automation requires manual validation of TLS implementation and configuration checks. AWS Security Hub can be used for identifying known weak configurations.",
    "References": [
      "https://docs.aws.amazon.com/outposts/latest/userguide/data-protection.html"
    ]
  },
  {
    "Title": "Monitor EC2 Instance State Changes for Memory Scrubbing Compliance",
    "Description": "Enable monitoring of EC2 instance transitions to ensure memory scrubbing processes occur when instances are stopped or terminated.",
    "Applicability": "All EC2 instances managed on AWS Outposts and AWS regions",
    "Security Risk": "Failure to scrub memory could lead to residual data exposure if EC2 instances are improperly decommissioned.",
    "Default Behavior / Limitations": "Memory scrubbing is automatically handled by AWS EC2 hypervisor, but monitoring can provide assurance and compliance evidence.",
    "Automation": "Can be monitored using AWS CloudWatch events and detailed logging through AWS CloudTrail.",
    "References": [
      "https://docs.aws.amazon.com/outposts/latest/userguide/data-protection.html"
    ]
  },
  {
    "Title": "Audit and Log Nitro Security Key Destruction Events",
    "Description": "Ensure Nitro Security Key destruction events are logged and audited to confirm the cryptographic shredding of data on AWS Outposts.",
    "Applicability": "All AWS Outposts using Nitro Security Key for data encryption",
    "Security Risk": "Without logging NSK destruction, there is a risk of data remnants that could be recovered if NSF is not properly destroyed.",
    "Default Behavior / Limitations": "AWS does not automatically log every NSK destruction event; users must ensure logging is enabled.",
    "Automation": "Can be audited and logged using AWS CloudTrail and analyzed with AWS Security Hub for compliance checks.",
    "References": [
      "https://docs.aws.amazon.com/outposts/latest/userguide/data-protection.html"
    ]
  }
]
```