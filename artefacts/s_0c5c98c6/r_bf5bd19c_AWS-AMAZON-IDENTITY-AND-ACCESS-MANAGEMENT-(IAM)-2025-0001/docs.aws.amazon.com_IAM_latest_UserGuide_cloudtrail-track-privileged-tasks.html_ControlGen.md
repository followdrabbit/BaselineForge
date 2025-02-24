```json
[
  {
    "Title": "Track 'AssumeRoot' Sessions in CloudTrail Logs",
    "Description": "Ensure AWS CloudTrail is configured to log all 'AssumeRoot' events. Implement monitoring for the 'AssumeRoot' event in the 'eventName' field of CloudTrail logs to detect any unauthorized root-level actions.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Failure to track 'AssumeRoot' sessions could result in undetected unauthorized access to root-level operations, potentially leading to data breaches and system compromises.",
    "Default Behavior / Limitations": "AWS CloudTrail must be enabled to record API calls and allow tracking.",
    "Automation": "Can be monitored using AWS CloudTrail with AWS Security Hub or AWS Config custom rules to detect the 'AssumeRoot' event in logs.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-track-privileged-tasks.html"
    ]
  },
  {
    "Title": "Identify 'targetPrincipal' and 'accessKeyId' in CloudTrail for 'AssumeRoot' Sessions",
    "Description": "Configure CloudTrail to log events and detect the 'targetPrincipal' and 'accessKeyId' fields to correlate 'AssumeRoot' session actions with affected resources and accounts.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without identifying 'targetPrincipal' and 'accessKeyId', it is challenging to attribute actions to specific accounts and sessions, complicating incident response and remediation efforts.",
    "Default Behavior / Limitations": "Requires CloudTrail to be configured correctly to log these details.",
    "Automation": "Can be audited using AWS CloudTrail analysis tools and AWS Config rules to check for the presence of these fields in log entries.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-track-privileged-tasks.html"
    ]
  },
  {
    "Title": "Search for Privileged Tasks Using 'accessKeyId' in 'AssumeRoot' Sessions",
    "Description": "Implement a system to search CloudTrail logs using 'accessKeyId' from 'AssumeRoot' events to trace all privileged operations executed in a session.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Not tracking privileged tasks accurately can lead to unauthorized actions being performed without detection, risking resource compromise and the security posture of the AWS account.",
    "Default Behavior / Limitations": "Requires search capabilities and access to CloudTrail logs to be manually configured or automated.",
    "Automation": "Can be automated using AWS CloudTrail insights and AWS Lambda functions to periodically search and report activities tied to specific 'accessKeyId' values.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-track-privileged-tasks.html"
    ]
  },
  {
    "Title": "Limit 'AssumeRoot' Session Duration to 900 Seconds",
    "Description": "Configure IAM roles or policies to restrict the maximum session duration of 'AssumeRoot' to 900 seconds (15 minutes) using appropriate IAM policies and role settings.",
    "Applicability": "All AWS accounts with root user access",
    "Security Risk": "Extended root session durations increase the risk of prolonged unauthorized access and potential damage if credentials are compromised.",
    "Default Behavior / Limitations": "AWS does not enforce session time limits by default for the root user. Configuration is required manually.",
    "Automation": "Can be enforced using IAM role configurations and AWS Config rule customizations to audit session durations regularly.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-track-privileged-tasks.html"
    ]
  }
]
```