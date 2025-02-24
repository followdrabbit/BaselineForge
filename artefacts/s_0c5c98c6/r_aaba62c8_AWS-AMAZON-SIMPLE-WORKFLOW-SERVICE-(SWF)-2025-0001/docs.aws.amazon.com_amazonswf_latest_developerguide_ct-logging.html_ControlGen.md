```json
[
  {
    "Title": "Capture Amazon SWF API Calls with AWS CloudTrail",
    "Description": "Enable logging of all API calls to the Amazon SWF service using AWS CloudTrail. This ensures that all actions taken via both the SWF console and code calls to the SWF API are recorded for auditing and monitoring.",
    "Applicability": "All AWS accounts using Amazon SWF",
    "Security Risk": "Without logging API calls, it's challenging to track and audit access and changes to Amazon SWF resources, potentially missing unauthorized or malicious activities.",
    "Default Behavior / Limitations": "AWS CloudTrail supports logging of SWF API calls, but it must be explicitly configured for the specific AWS account in use.",
    "Automation": "Can be enforced using AWS CloudTrail by enabling logging for SWF API calls across all required regions.",
    "References": [
      "https://docs.aws.amazon.com/amazonswf/latest/developerguide/ct-logging.html"
    ]
  },
  {
    "Title": "Configure Multi-Region CloudTrail Trail for Comprehensive Logging",
    "Description": "Set up a multi-Region CloudTrail trail to log all activities across AWS Regions. This ensures that every action, irrespective of the region where it occurs, is captured.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Failure to log activities across regions can result in visibility gaps, leading to potential undetected unauthorized or malicious activities.",
    "Default Behavior / Limitations": "AWS CloudTrail supports multi-region trails, but they must be explicitly configured.",
    "Automation": "Can be enforced and monitored using AWS Config rule `cloud-trail-enabled` for multi-Region setup.",
    "References": [
      "https://docs.aws.amazon.com/amazonswf/latest/developerguide/ct-logging.html"
    ]
  },
  {
    "Title": "Log Amazon SWF Data Events Using CloudTrail",
    "Description": "Ensure that data events for Amazon SWF resource types are logged via CloudTrail. Configure CloudTrail to capture these events either through the console, AWS CLI, or API operations.",
    "Applicability": "All AWS accounts using Amazon SWF",
    "Security Risk": "Not logging data events might result in critical operations being missed, leading to challenges in auditing and securing SWF resources.",
    "Default Behavior / Limitations": "Data events for SWF are not logged by default and require explicit configuration within CloudTrail.",
    "Automation": "Can be configured via AWS CloudTrail settings either through the console, AWS CLI, or API operations.",
    "References": [
      "https://docs.aws.amazon.com/amazonswf/latest/developerguide/ct-logging.html"
    ]
  },
  {
    "Title": "Implement Advanced Event Selectors for Amazon SWF in CloudTrail",
    "Description": "Use advanced event selectors to capture specific Amazon SWF data events of interest, filtering based on fields such as eventName, readOnly, and resources.ARN, to ensure efficient and targeted logging.",
    "Applicability": "All AWS accounts using Amazon SWF",
    "Security Risk": "Without filtering, logs can become cluttered with irrelevant data, making it difficult to identify important events or increasing storage costs unnecessarily.",
    "Default Behavior / Limitations": "Advanced event selectors must be manually configured in CloudTrail as per the specific logging requirements.",
    "Automation": "Can be automated by setting up advanced event selectors in CloudTrail through the AWS Management Console, AWS CLI, or CloudTrail API.",
    "References": [
      "https://docs.aws.amazon.com/amazonswf/latest/developerguide/ct-logging.html"
    ]
  },
  {
    "Title": "Capture Amazon SWF Management Events by Default in CloudTrail",
    "Description": "Ensure that management events related to Amazon SWF control plane operations are captured by default in CloudTrail. This includes actions related to account management and control changes.",
    "Applicability": "All AWS accounts using Amazon SWF",
    "Security Risk": "Management events not captured might lead to missed data regarding critical control plane operations, affecting the ability to audit configuration changes and access.",
    "Default Behavior / Limitations": "CloudTrail captures management events by default, but users must ensure this setting is verified for Amazon SWF.",
    "Automation": "Default AWS CloudTrail setup supports the capture of management events. Ensure that existing CloudTrail configurations include management events for comprehensive auditing.",
    "References": [
      "https://docs.aws.amazon.com/amazonswf/latest/developerguide/ct-logging.html"
    ]
  }
]
```