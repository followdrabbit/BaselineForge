# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.LoggingAndMonitoring.html'}

[](/pdfs/AmazonRDS/latest/AuroraUserGuide/aurora-
ug.pdf#Overview.LoggingAndMonitoring "Open PDF")

[Documentation](/index.html)[Amazon RDS](/rds/index.html)[User Guide for
Aurora](CHAP_AuroraOverview.html)

# Logging and monitoring in Amazon Aurora

Monitoring is an important part of maintaining the reliability, availability,
and performance of Amazon Aurora and your AWS solutions. You should collect
monitoring data from all of the parts of your AWS solution so that you can
more easily debug a multi-point failure if one occurs. AWS provides several
tools for monitoring your Amazon Aurora resources and responding to potential
incidents:

**Amazon CloudWatch Alarms**

    

Using Amazon CloudWatch alarms, you watch a single metric over a time period
that you specify. If the metric exceeds a given threshold, a notification is
sent to an Amazon SNS topic or AWS Auto Scaling policy. CloudWatch alarms do
not invoke actions because they are in a particular state. Rather the state
must have changed and been maintained for a specified number of periods.

**AWS CloudTrail Logs**

    

CloudTrail provides a record of actions taken by a user, role, or an AWS
service in Amazon Aurora. CloudTrail captures all API calls for Amazon Aurora
as events, including calls from the console and from code calls to Amazon RDS
API operations. Using the information collected by CloudTrail, you can
determine the request that was made to Amazon Aurora, the IP address from
which the request was made, who made the request, when it was made, and
additional details. For more information, see [Monitoring Amazon Aurora API
calls in AWS CloudTrail](./logging-using-cloudtrail.html).

**Enhanced Monitoring**

    

Amazon Aurora provides metrics in real time for the operating system (OS) that
your DB cluster runs on. You can view the metrics for your DB cluster using
the console, or consume the Enhanced Monitoring JSON output from Amazon
CloudWatch Logs in a monitoring system of your choice. For more information,
see [Monitoring OS metrics with Enhanced
Monitoring](./USER_Monitoring.OS.html).

**Amazon RDS Performance Insights**

    

Performance Insights expands on existing Amazon Aurora monitoring features to
illustrate your database's performance and help you analyze any issues that
affect it. With the Performance Insights dashboard, you can visualize the
database load and filter the load by waits, SQL statements, hosts, or users.
For more information, see [Monitoring DB load with Performance Insights on
Amazon Aurora](./USER_PerfInsights.html).

**Database Logs**

    

You can view, download, and watch database logs using the AWS Management
Console, AWS CLI, or RDS API. For more information, see [Monitoring Amazon
Aurora log files](./USER_LogAccess.html).

**Amazon Aurora Recommendations**

    

Amazon Aurora provides automated recommendations for database resources. These
recommendations provide best practice guidance by analyzing DB cluster
configuration, usage, and performance data. For more information, see
[Recommendations from Amazon Aurora](./monitoring-recommendations.html).

**Amazon Aurora Event Notification**

    

Amazon Aurora uses the Amazon Simple Notification Service (Amazon SNS) to
provide notification when an Amazon Aurora event occurs. These notifications
can be in any notification form supported by Amazon SNS for an AWS Region,
such as an email, a text message, or a call to an HTTP endpoint. For more
information, see [Working with Amazon RDS event
notification](./USER_Events.html).

**AWS Trusted Advisor**

    

Trusted Advisor draws upon best practices learned from serving hundreds of
thousands of AWS customers. Trusted Advisor inspects your AWS environment and
then makes recommendations when opportunities exist to save money, improve
system availability and performance, or help close security gaps. All AWS
customers have access to five Trusted Advisor checks. Customers with a
Business or Enterprise support plan can view all Trusted Advisor checks.

Trusted Advisor has the following Amazon Aurora-related checks:

  * Amazon Aurora Idle DB Instances

  * Amazon Aurora Security Group Access Risk

  * Amazon Aurora Backups

  * Amazon Aurora Multi-AZ

  * Aurora DB Instance Accessibility

For more information on these checks, see [Trusted Advisor best practices
(checks)](https://aws.amazon.com/premiumsupport/trustedadvisor/best-
practices/).

**Database activity streams**

    

Database activity streams can protect your databases from internal threats by
controlling DBA access to the database activity streams. Thus, the collection,
transmission, storage, and subsequent processing of the database activity
stream is beyond the access of the DBAs that manage the database. Database
activity streams can provide safeguards for your database and meet compliance
and regulatory requirements. For more information, see [Monitoring Amazon
Aurora with Database Activity Streams](./DBActivityStreams.html).

For more information about monitoring Aurora see [Monitoring metrics in an
Amazon Aurora cluster](./MonitoringAurora.html).

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Troubleshooting

Compliance validation

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

