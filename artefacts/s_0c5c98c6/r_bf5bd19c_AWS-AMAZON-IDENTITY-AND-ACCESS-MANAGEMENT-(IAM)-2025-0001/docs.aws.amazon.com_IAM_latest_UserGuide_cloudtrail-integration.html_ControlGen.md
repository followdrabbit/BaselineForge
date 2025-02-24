```json
[
  {
    "Title": "Enable AWS CloudTrail for Logging IAM and AWS STS API Requests",
    "Description": "Ensure that all IAM and AWS STS API requests are captured by AWS CloudTrail and the logs are stored in an Amazon S3 bucket.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Failure to log IAM and AWS STS API calls may result in insufficient traceability for auditing and security investigations, potentially allowing unauthorized actions to go undetected.",
    "Default Behavior / Limitations": "CloudTrail is enabled by default in new accounts, but creating a specific trail is necessary for continuous logging in S3.",
    "Automation": "Can be enforced using AWS CloudTrail and AWS Config rule `cloud-trail-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html"
    ]
  },
  {
    "Title": "Configure CloudTrail to Capture Logs from All AWS Regions",
    "Description": "Ensure AWS CloudTrail is set to record activity from all AWS Regions by configuring a multi-region trail.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Not logging cross-region activity can lead to gaps in audit trails, making incident response less effective in multi-region deployments.",
    "Default Behavior / Limitations": "Trails created via the console apply to all Regions by default.",
    "Automation": "Can be enforced using AWS CloudTrail setup in the AWS Management Console.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html"
    ]
  },
  {
    "Title": "Log Specific Non-Authenticated IAM and AWS STS API Requests",
    "Description": "Configure CloudTrail to log all IAM and AWS STS authenticated API requests, including specific non-authenticated requests such as AssumeRoleWithSAML and AssumeRoleWithWebIdentity.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Omitting non-authenticated IAM and AWS STS calls can reduce visibility into federated identity actions, impacting threat detection and auditing.",
    "Default Behavior / Limitations": "These events are inherently logged when CloudTrail is enabled.",
    "Automation": "Monitored via AWS CloudTrail configuration.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html"
    ]
  },
  {
    "Title": "Include Essential Details in CloudTrail Logs for Auditing",
    "Description": "Ensure that CloudTrail logs include critical details such as IP address, requester identity, and request time to assist in auditing and troubleshooting.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Incomplete log details may hinder investigations and auditing, leading to an inability to pinpoint unauthorized access sources.",
    "Default Behavior / Limitations": "AWS CloudTrail automatically logs these details by default.",
    "Automation": "Ensured by AWS CloudTrail setups.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html"
    ]
  },
  {
    "Title": "Monitor Major IAM Operations Using CloudTrail",
    "Description": "Utilize CloudTrail to log all major IAM operations such as CreateUser, DeleteRole, and ListGroups to ensure they are actively monitored by the security team.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Unmonitored IAM operations can lead to unauthorized management and access changes, increasing the risk of privilege escalation.",
    "Default Behavior / Limitations": "IAM operations are logged when CloudTrail logging is enabled.",
    "Automation": "Monitored and managed through AWS CloudTrail views.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html"
    ]
  },
  {
    "Title": "Utilize sts:SourceIdentity Condition Key in Role Trust Policies",
    "Description": "Implement the sts:SourceIdentity condition key in AWS STS role trust policies to require users to specify their identity, providing traceability of actions for federated roles.",
    "Applicability": "AWS accounts using roles for federated access",
    "Security Risk": "Without identifying who assumes a role, it's challenging to track user actions via temporary credentials, affecting accountability.",
    "Default Behavior / Limitations": "Requires update in IAM role trust policies.",
    "Automation": "Manual validation required. Roles and policies need manual updates.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html"
    ]
  },
  {
    "Title": "Log Successful and Failed User Sign-In Events with CloudTrail",
    "Description": "Configure CloudTrail to log both successful and failed sign-in attempts to the AWS Management Console and other AWS services for enhanced security monitoring.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Not logging failed sign-in attempts could allow unauthorized access attempts to go unnoticed, compromising account security.",
    "Default Behavior / Limitations": "Sign-in events are logged when CloudTrail is properly configured.",
    "Automation": "Audited via AWS CloudTrail settings.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html"
    ]
  },
  {
    "Title": "Log Sign-In Attempts with Temporary Credentials",
    "Description": "Ensure CloudTrail logs sign-in attempts using temporary credentials, capturing multiple API calls needed for cross-account operations to ensure comprehensive monitoring.",
    "Applicability": "All AWS accounts using temporary credentials",
    "Security Risk": "Lack of logs for temporary credential usage can obscure cross-account access patterns, affecting security monitoring.",
    "Default Behavior / Limitations": "Logging of sign-in attempts is supported by enabling CloudTrail.",
    "Automation": "Managed via AWS CloudTrail log configuration.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html"
    ]
  },
  {
    "Title": "Redact Sensitive Information in CloudTrail for Failed Sign-In Attempts",
    "Description": "Configure CloudTrail to redact sensitive information from logs, such as usernames, when there is a failed sign-in attempt due to an incorrect username, to protect sensitive data.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Disclosure of raw usernames in logs can expose sensitive information, leading to potential exploitation in social engineering attacks.",
    "Default Behavior / Limitations": "Sensitive information masquing is a best practice but requires configuration.",
    "Automation": "Manual validation required to ensure redaction policies are applied.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html"
    ]
  },
  {
    "Title": "Ensure Persistence of CloudTrail Logs During Account Compromise",
    "Description": "Configure persistence mechanisms, such as S3 bucket versioning and cross-account access, to prevent deletion of CloudTrail logs in case of account compromise.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without protections, an attacker could delete or alter log data, hindering incident response and forensic investigations.",
    "Default Behavior / Limitations": "Requires manual configuration of S3 settings.",
    "Automation": "Manual validation required. S3 bucket settings need to be configured.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html"
    ]
  }
]
```