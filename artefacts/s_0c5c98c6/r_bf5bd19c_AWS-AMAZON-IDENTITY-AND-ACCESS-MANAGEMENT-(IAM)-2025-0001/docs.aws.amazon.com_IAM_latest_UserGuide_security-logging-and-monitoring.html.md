# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/IAM/latest/UserGuide/security-logging-and-monitoring.html'}

[](/pdfs/IAM/latest/UserGuide/iam-ug.pdf#security-logging-and-monitoring "Open
PDF")

[Documentation](/index.html)[AWS Identity and Access
Management](/iam/index.html)[User Guide](introduction.html)

# Logging and monitoring in AWS Identity and Access Management

Monitoring is an important part of maintaining the reliability, availability,
and performance of AWS Identity and Access Management (IAM), AWS Security
Token Service (AWS STS) and your other AWS solutions. AWS provides several
tools for monitoring your AWS resources and responding to potential incidents:

  * _AWS CloudTrail_ captures all API calls for IAM and AWS STS as events, including calls from the console and API calls. To learn more about using CloudTrail with IAM and AWS STS, see [Logging IAM and AWS STS API calls with AWS CloudTrail](./cloudtrail-integration.html). For more information about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

  * _AWS Identity and Access Management and Access Analyzer_ helps you identify the resources in your organization and accounts, such as Amazon S3 buckets or IAM roles, that are shared with an external entity. This helps you identify unintended access to your resources and data, which is a security risk. To learn more, see [What is IAM Access Analyzer?](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)

  * _Amazon CloudWatch_ monitors your AWS resources and the applications that you run on AWS in real time. You can collect and track metrics, create customized dashboards, and set alarms that notify you or take actions when a specified metric reaches a threshold that you specify. For example, you can have CloudWatch track CPU usage or other metrics of your Amazon EC2 instances and automatically launch new instances when needed. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

  * _Amazon CloudWatch Logs_ helps you monitor, store, and access your log files from Amazon EC2 instances, CloudTrail, and other sources. CloudWatch Logs can monitor information in the log files and notify you when certain thresholds are met. You can also archive your log data in highly durable storage. For more information, see the [Amazon CloudWatch Logs User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/).

For additional resources and security best practices for IAM, see [Security
best practices and use cases in AWS Identity and Access Management](./best-
practices-use-cases.html).

###### Topics

  * [Logging IAM and AWS STS API calls with AWS CloudTrail](./cloudtrail-integration.html)
  * [Track privileged tasks in AWS CloudTrail](./cloudtrail-track-privileged-tasks.html)

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Data protection

Log events with CloudTrail

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

