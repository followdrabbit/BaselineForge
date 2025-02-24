# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-cloudtrail-logging.html'}

[](/pdfs/datapipeline/latest/DeveloperGuide/datapipeline-dg.pdf#dp-cloudtrail-
logging "Open PDF")

[Documentation](/index.html)[AWS Data Pipeline](/data-
pipeline/index.html)[Developer Guide](what-is-datapipeline.html)

AWS Data Pipeline Information in CloudTrailUnderstanding AWS Data Pipeline Log
File Entries

AWS Data Pipeline is no longer available to new customers. Existing customers
of AWS Data Pipeline can continue to use the service as normal. [Learn
more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-
pipeline/)

# Logging and Monitoring in AWS Data Pipeline

AWS Data Pipeline is integrated with AWS CloudTrail, a service that provides a
record of actions taken by a user, role, or an AWS service in AWS Data
Pipeline. CloudTrail captures all API calls for AWS Data Pipeline as events.
The calls captured include calls from the AWS Data Pipeline console and code
calls to the AWS Data Pipeline API operations. If you create a trail, you can
enable continuous delivery of CloudTrail events to an Amazon S3 bucket,
including events for AWS Data Pipeline. If you don't configure a trail, you
can still view the most recent events in the CloudTrail console in **Event
history**. Using the information collected by CloudTrail, you can determine
the request that was made to AWS Data Pipeline, the IP address from which the
request was made, who made the request, when it was made, and additional
details.

To learn more about CloudTrail, see the [AWS CloudTrail User
Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

## AWS Data Pipeline Information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When
activity occurs in AWS Data Pipeline, that activity is recorded in a
CloudTrail event along with other AWS service events in **Event history**. You
can view, search, and download recent events in your AWS account. For more
information, see [Viewing Events with CloudTrail Event
History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-
cloudtrail-events.html).

For an ongoing record of events in your AWS account, including events for AWS
Data Pipeline, create a trail. A _trail_ enables CloudTrail to deliver log
files to an Amazon S3 bucket. By default, when you create a trail in the
console, the trail applies to all AWS Regions. The trail logs events from all
Regions in the AWS partition and delivers the log files to the Amazon S3
bucket that you specify. Additionally, you can configure other AWS services to
further analyze and act upon the event data collected in CloudTrail logs. For
more information, see the following:

  * [Overview for Creating a Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)

  * [CloudTrail Supported Services and Integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations)

  * [Configuring Amazon SNS Notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)

  * [Receiving CloudTrail Log Files from Multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail Log Files from Multiple Accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

All of the AWS Data Pipeline actions are logged by CloudTrail and are
documented in the [AWS Data Pipeline API Reference Actions
chapter](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_Operations.html).
For example, calls to the **CreatePipeline** action generate entries in the
CloudTrail log files.

Every event or log entry contains information about who generated the request.
The identity information helps you determine the following:

  * Whether the request was made with root or IAM role credentials.

  * Whether the request was made with temporary security credentials for a role or federated user.

  * Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity
Element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-
event-reference-user-identity.html).

## Understanding AWS Data Pipeline Log File Entries

A trail is a configuration that enables delivery of events as log files to an
Amazon S3 bucket that you specify. CloudTrail log files contain one or more
log entries. An event represents a single request from any source and includes
information about the requested action, the date and time of the action,
request parameters, and so on. CloudTrail log files aren't an ordered stack
trace of the public API calls, so they don't appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the
`CreatePipeline` operation:

    
    
          {
      "Records": [
        {
          "eventVersion": "1.02",
          "userIdentity": {
            "type": "Root",
            "principalId": "123456789012",
            "arn": "arn:aws:iam::aws-account-id:role/role-name",
            "accountId": "role-account-id",
            "accessKeyId": "role-access-key"
          },
          "eventTime": "2014-11-13T19:15:15Z",
          "eventSource": "datapipeline.amazonaws.com",
          "eventName": "CreatePipeline",
          "awsRegion": "us-east-1",
          "sourceIPAddress": "72.21.196.64",
          "userAgent": "aws-cli/1.5.2 Python/2.7.5 Darwin/13.4.0",
          "requestParameters": {
            "name": "testpipeline",
            "uniqueId": "sounique"
          },
          "responseElements": {
            "pipelineId": "df-06372391ZG65EXAMPLE"
          },
          "requestID": "65cbf1e8-6b69-11e4-8816-cfcbadd04c45",
          "eventID": "9f99dce0-0864-49a0-bffa-f72287197758",
          "eventType": "AwsApiCall",
          "recipientAccountId": "role-account-id"
        }, 
          ...additional entries
      ]
    }

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

IAM Roles

Incident Response

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

