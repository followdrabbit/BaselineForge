# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/timestream/latest/developerguide/logging-using-cloudtrail.html'}

[](/pdfs/timestream/latest/developerguide/timestream.pdf#logging-using-
cloudtrail "Open PDF")

[Documentation](/index.html)[Amazon
Timestream](/timestream/index.html)[Developer Guide](what-is-timestream.html)

Timestream for LiveAnalytics information in CloudTrail

# Logging Timestream for LiveAnalytics API calls with AWS CloudTrail

Timestream for LiveAnalytics is integrated with AWS CloudTrail, a service that
provides a record of actions taken by a user, role, or an AWS service in
Timestream for LiveAnalytics. CloudTrail captures Data Definition Language
(DDL) API calls for Timestream for LiveAnalytics as events. The calls that are
captured include calls from the Timestream for LiveAnalytics console and code
calls to the Timestream for LiveAnalytics API operations. If you create a
trail, you can enable continuous delivery of CloudTrail events to an Amazon
Simple Storage Service (Amazon S3) bucket, including events for Timestream for
LiveAnalytics. If you don't configure a trail, you can still view the most
recent events on the CloudTrail console in **Event history**. Using the
information collected by CloudTrail, you can determine the request that was
made to Timestream for LiveAnalytics, the IP address from which the request
was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User
Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

## Timestream for LiveAnalytics information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When
activity occurs in Timestream for LiveAnalytics, that activity is recorded in
a CloudTrail event along with other AWS service events in **Event history**.
You can view, search, and download recent events in your AWS account. For more
information, see [Viewing Events with CloudTrail Event
History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-
cloudtrail-events.html).

###### Warning

Currently, Timestream for LiveAnalytics generates CloudTrail events for all
management and `Query` API operations, but does not generate events for
`WriteRecords` and `DescribeEndpoints` APIs.

For an ongoing record of events in your AWS account, including events for
Timestream for LiveAnalytics, create a trail. A _trail_ enables CloudTrail to
deliver log files to an Amazon S3 bucket. By default, when you create a trail
in the console, the trail applies to all AWS Regions. The trail logs events
from all Regions in the AWS partition and delivers the log files to the Amazon
S3 bucket that you specify. Additionally, you can configure other AWS services
to further analyze and act upon the event data collected in CloudTrail logs.

For more information, see the following topics in the _AWS CloudTrail User
Guide_ :

  * [Overview for Creating a Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)

  * [CloudTrail Supported Services and Integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations)

  * [Configuring Amazon SNS Notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)

  * [Receiving CloudTrail Log Files from Multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html)

  * [Receiving CloudTrail Log Files from Multiple Accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

  * [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html)

Every event or log entry contains information about who generated the request.
The identity information helps you determine the following:

  * Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials

  * Whether the request was made with temporary security credentials for a role or federated user

  * Whether the request was made by another AWS service

For more information, see the [CloudTrail userIdentity
Element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-
event-reference-user-identity.html).

For `Query` API events:

  * Create a trail that receives all events or select events with Timestream for LiveAnalytics resource type `AWS::Timestream::Database` or `AWS::Timestream::Table`.

  * `Query` API requests that do not access any database or table or that result in a validation exception due to a malformed query string are recorded in CloudTrail with a resource type `AWS::Timestream::Database` and an ARN value of:
    
        arn:aws:timestream:(region):(accountId):database/NO_RESOURCE_ACCESSED

These events are delivered only to trails that receive events with resource
type `AWS::Timestream::Database`.

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Monitoring tools

Resilience

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

