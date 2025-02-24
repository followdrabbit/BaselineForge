```json
[
  {
    "Title": "Enable CloudTrail Logging for AWS Service Catalog API Calls",
    "Description": "AWS CloudTrail must be configured to capture and log all API calls made to AWS Service Catalog in all available regions. Ensure logs are delivered to a specified and secured Amazon S3 bucket.",
    "Applicability": "All AWS accounts using AWS Service Catalog",
    "Security Risk": "Without logging, unauthorized actions and security incidents could go untracked, increasing the risk of undetected data breaches and configuration changes.",
    "Default Behavior / Limitations": "AWS CloudTrail is not enabled by default for AWS Service Catalog. Users must manually set up CloudTrail and specify the S3 bucket for log storage.",
    "Automation": "Can be enforced using AWS Config with custom rules to ensure CloudTrail is configured to log AWS Service Catalog API calls. Use IAM policies to restrict access to the S3 bucket.",
    "References": [
      "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/logging-and-monitoring.html"
    ]
  },
  {
    "Title": "Configure AWS SNS Notifications for AWS Service Catalog Stack Events",
    "Description": "AWS Service Catalog must be configured to use AWS SNS notifications for stack events, ensuring notifications are correctly set up through notification constraints. Verify that the SNS topic has the appropriate access policy.",
    "Applicability": "All AWS accounts utilizing AWS Service Catalog to manage stacks",
    "Security Risk": "Without proper notification of stack events, critical changes could go unnoticed, potentially leading to unmonitored deployments and unnoticed failures.",
    "Default Behavior / Limitations": "AWS Service Catalog does not automatically configure SNS notifications. Users must configure SNS topics and notification constraints manually.",
    "Automation": "Manual validation required to ensure SNS topics and permissions are configured correctly, as automation depends on the specific architecture and integration of the SNS topics.",
    "References": [
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/notifying-events.html",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/logging-and-monitoring.html"
    ]
  }
]
```