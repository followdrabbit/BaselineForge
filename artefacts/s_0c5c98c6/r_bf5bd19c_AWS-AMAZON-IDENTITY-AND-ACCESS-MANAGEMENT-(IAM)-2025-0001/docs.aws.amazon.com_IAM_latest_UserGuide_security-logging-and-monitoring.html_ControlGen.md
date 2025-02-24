```json
[
  {
    "Title": "Enable AWS CloudTrail for IAM and AWS STS API Call Logging",
    "Description": "Ensure AWS CloudTrail is enabled for all regions to capture and log all API calls involving AWS Identity and Access Management (IAM) and AWS Security Token Service (STS). This is critical for auditing and monitoring security-relevant actions.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without logging API calls to IAM and STS, unauthorized access and identity-related actions may go unrecorded, making security auditing and forensic investigation difficult.",
    "Default Behavior / Limitations": "AWS CloudTrail is not enabled by default. Customers need to manually activate trails and configure them for specific services like IAM and STS.",
    "Automation": "Can be enforced using AWS Config rule `cloud-trail-enabled` and configuring the trail to log all management events. Use Security Hub to ensure coverage.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/security-logging-and-monitoring.html",
      "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html"
    ]
  },
  {
    "Title": "Use AWS IAM Access Analyzer to Detect External Access",
    "Description": "Activate AWS IAM Access Analyzer in all AWS accounts to automatically analyze all resource policies and detect any resources shared externally with entities outside the AWS account, such as other AWS accounts, organizations, or the internet.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without Access Analyzer, unintended or unauthorized external access to resources can occur, compromising data confidentiality and integrity.",
    "Default Behavior / Limitations": "AWS IAM Access Analyzer must be manually enabled in each AWS account.",
    "Automation": "Automated provisioning can be implemented through AWS CLI or SDK to create analyzers across multiple accounts and regions.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html"
    ]
  },
  {
    "Title": "Utilize Amazon CloudWatch for Real-time Monitoring of Resources",
    "Description": "Configure Amazon CloudWatch to monitor AWS infrastructure and applications. Set up alarms on critical metrics, such as CPU usage, memory usage, or application-specific logs, to trigger automatic notifications or actions upon threshold breaches.",
    "Applicability": "All AWS resources and applications",
    "Security Risk": "Without proactive monitoring, resource failures or abnormal activities may go unnoticed, leading to potential disruptions or security incidents.",
    "Default Behavior / Limitations": "CloudWatch does not monitor by default; custom metrics and alarms need configuration.",
    "Automation": "Can be set up using AWS CloudFormation templates or AWS CLI scripts to automate creation and management of CloudWatch alarms and dashboards.",
    "References": [
      "https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/"
    ]
  },
  {
    "Title": "Implement Amazon CloudWatch Logs for Centralized Logging",
    "Description": "Set up Amazon CloudWatch Logs to collect and monitor log data from EC2 instances, Lambda functions, and other resources. Store log data in a centralized and durable location for access and analysis. Implement retention policies to manage the log data lifecycle effectively.",
    "Applicability": "All AWS resources generating logs",
    "Security Risk": "Without central log management, critical security events might be overlooked, and the lack of historical data makes forensic investigations challenging.",
    "Default Behavior / Limitations": "AWS does not automatically store logs; CloudWatch Logs setup must be manually configured.",
    "Automation": "Can be automated using AWS CloudFormation, AWS CLI, and log agents such as the CloudWatch Logs agent installed on instances.",
    "References": [
      "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/"
    ]
  }
]
```