# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/security-best-practices.html'}

[](/pdfs/kinesisvideostreams/latest/dg/kinesisvideo-dg.pdf#security-best-
practices "Open PDF")

[Documentation](/index.html)[Amazon Kinesis Video
Streams](/kinesis/index.html)[Developer Guide](what-is-kinesis-video.html)

Implement least privilege accessUse IAM rolesUse CloudTrail to monitor API
calls

# Security best practices for Kinesis Video Streams

Amazon Kinesis Video Streams provides a number of security features to
consider as you develop and implement your own security policies. The
following best practices are general guidelines and donât represent a
complete security solution. Because these best practices might not be
appropriate or sufficient for your environment, treat them as helpful
considerations rather than prescriptions.

For security best practices for your remote devices, see [Security Best
Practices for Device
Agents](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-
DetectMetricsMessagesBestPract.html).

## Implement least privilege access

When granting permissions, you decide who is getting what permissions to which
Kinesis Video Streams resources. You enable specific actions that you want to
allow on those resources. Therefore you should grant only the permissions that
are required to perform a task. Implementing least privilege access is
fundamental in reducing security risk and the impact that could result from
errors or malicious intent.

For example, a producer that sends data to Kinesis Video Streams requires only
`PutMedia`, `GetStreamingEndpoint`, and `DescribeStream`. Do not grant
producer applications permissions for all actions (`*`), or for other actions
such as `GetMedia`.

For more information, see [What Is Least Privilege & Why Do You Need
It?](https://www.beyondtrust.com/blog/entry/what-is-least-privilege)

## Use IAM roles

Producer and client applications must have valid credentials to access Kinesis
Video Streams. You should not store AWS credentials directly in a client
application or in an Amazon S3 bucket. These are long-term credentials that
aren't automatically rotated and could have a significant business impact if
they are compromised.

Instead, you should use an IAM role to manage temporary credentials for your
producer and client applications to access Kinesis Video Streams. When you use
a role, you don't have to use long-term credentials (such as a username and
password or access keys) to access other resources.

For more information, see the following topics in the _IAM User Guide_ :

  * [IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)

  * [Common Scenarios for Roles: Users, Applications, and Services](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios.html)

## Use CloudTrail to monitor API calls

Kinesis Video Streams works with AWS CloudTrail, a service that provides a
record of actions taken by a user, role, or an AWS service in Kinesis Video
Streams.

You can use the information collected by CloudTrail to determine the request
that was made to Kinesis Video Streams, the IP address from which the request
was made, who made the request, when it was made, and additional details.

For more information, see [Log Amazon Kinesis Video Streams API calls with AWS
CloudTrail](./monitoring-cloudtrail.html).

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Infrastructure Security

Troubleshooting

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

