# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/timestream/latest/developerguide/KeyManagement.html'}

[](/pdfs/timestream/latest/developerguide/timestream.pdf#KeyManagement "Open
PDF")

[Documentation](/index.html)[Amazon
Timestream](/timestream/index.html)[Developer Guide](what-is-timestream.html)

# Key management

You can manage keys for Amazon Timestream Live Analytics using the [AWS Key
Management Service (AWS
KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/). **Timestream
Live Analytics requires the use of KMS to encrypt your data.** You have the
following options for key management, depending on how much control you
require over your keys:

###### Database and table resources

  * _Timestream Live Analytics-managed key:_ If you do not provide a key, Timestream Live Analytics will create a `alias/aws/timestream` key using KMS. 

  * _Customer managed key:_ KMS customer managed keys are supported. Choose this option if you require more control over the permissions and lifecycle of your keys, including the ability to have them automatically rotated on an annual basis.

###### Scheduled query resource

  * _Timestream Live Analytics-owned key:_ If you do not provide a key, Timestream Live Analytics will use its own a KMS key to encrypt the Query resource, this key is present in timestream account. See [AWS owned keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) in the KMS developer guide for more details.

  * _Customer managed key:_ KMS customer managed keys are supported. Choose this option if you require more control over the permissions and lifecycle of your keys, including the ability to have them automatically rotated on an annual basis.

KMS keys in an external key store (XKS) are not supported.

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Encryption in transit

Identity and access management

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

