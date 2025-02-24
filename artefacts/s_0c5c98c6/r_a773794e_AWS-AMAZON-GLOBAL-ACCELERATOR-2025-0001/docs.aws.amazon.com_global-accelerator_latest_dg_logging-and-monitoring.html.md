# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/global-accelerator/latest/dg/logging-and-monitoring.html'}

[](/pdfs/global-accelerator/latest/dg/global-accelerator-guide.pdf#logging-
and-monitoring "Open PDF")

[Documentation](/index.html)[AWS Global Accelerator](/global-
accelerator/index.html)[Developer Guide](what-is-global-accelerator.html)

# Logging and monitoring in AWS Global Accelerator

Monitoring is an important part of maintaining the availability and
performance of Global Accelerator and your AWS solutions. You should collect
monitoring data from all of the parts of your AWS solution so that you can
more easily debug a multi-point failure if one occurs. AWS provides several
tools for monitoring your Global Accelerator resources and activity, and
responding to potential incidents:

Global Accelerator provides the following three main avenues for logging and
tracking:

**Amazon CloudWatch metrics and alarms**

    

Using CloudWatch, you can monitor, in real time, your AWS resources and the
applications that you run on AWS. As soon as your accelerator is deployed,
CloudWatch begins collect and tracking metrics for Global Accelerator. Metrics
are variables that you can view for confirmation that traffic is flowing, or
that you can measure over time.

You can use metrics, for example, to verify that traffic is flowing through
Global Accelerator to your endpoints, and back out to clients, and to help
troubleshoot issues. You can also create alarms that watch specific metrics,
and then send notifications or automatically make changes to the resources you
are monitoring when the metric exceeds a certain threshold for a period of
time.

For more information, see [Using Amazon CloudWatch with AWS Global
Accelerator](./cloudwatch-monitoring.html).

**Global Accelerator flow logs**

    

Server flow logs are logs that you set up in Global Accelerator that provide
detailed records about traffic that flows through an accelerator to an
endpoint. Server flow logs are useful for many applications, for example, for
security and access audits. For more information, see [Configuring and using
flow logs in AWS Global Accelerator](./monitoring-global-accelerator.flow-
logs.html).

**AWS CloudTrail logs**

    

CloudTrail provides a record of actions taken by a user, role, or an AWS
service in Global Accelerator. CloudTrail captures all API calls for Global
Accelerator as events, including calls from the Global Accelerator console and
from code calls to the Global Accelerator API. For more information, see
[Using AWS CloudTrail to log AWS Global Accelerator API calls](./logging-
using-cloudtrail.html).

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Secure VPC connections

Compliance validation

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

