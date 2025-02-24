# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/directconnect/latest/UserGuide/dc-incident-response.html'}

[](/pdfs/directconnect/latest/UserGuide/dc-ug.pdf#dc-incident-response "Open
PDF")

[Documentation](/index.html)[AWS Direct
Connect](/directconnect/index.html)[User Guide](Welcome.html)

# Logging and monitoring in AWS Direct Connect

You can use the following automated monitoring tools to watch AWS Direct
Connect and report when something is wrong:

  * **Amazon CloudWatch Alarms** â Watch a single metric over a time period that you specify. Perform one or more actions based on the value of the metric relative to a given threshold over a number of time periods. The action is a notification sent to an Amazon SNS topic. CloudWatch alarms do not invoke actions simply because they are in a particular state; the state must have changed and been maintained for a specified number of periods. For more information, see [Monitor with Amazon CloudWatch](./monitoring-cloudwatch.html).

  * **AWS CloudTrail Log Monitoring** â Share log files between accounts and monitor CloudTrail log files in real time by sending them to CloudWatch Logs. You can also write log processing applications in Java and validate that your log files have not changed after delivery by CloudTrail. For more information, see [Log AWS Direct Connect API calls using AWS CloudTrail](./logging_dc_api_calls.html) and [Working with CloudTrail Log Files](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.html) in the _AWS CloudTrail User Guide_.

For more information, see [Monitor Direct Connect resources](./monitoring-
overview.html).

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

