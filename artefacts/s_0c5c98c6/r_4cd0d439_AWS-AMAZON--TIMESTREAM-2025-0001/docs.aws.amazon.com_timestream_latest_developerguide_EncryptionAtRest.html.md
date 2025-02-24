# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/timestream/latest/developerguide/EncryptionAtRest.html'}

[](/pdfs/timestream/latest/developerguide/timestream.pdf#EncryptionAtRest
"Open PDF")

[Documentation](/index.html)[Amazon
Timestream](/timestream/index.html)[Developer Guide](what-is-timestream.html)

# Encryption at rest

Timestream for LiveAnalytics encryption at rest provides enhanced security by
encrypting all your data at rest using encryption keys stored in [AWS Key
Management Service (AWS KMS)](https://aws.amazon.com/kms/). This functionality
helps reduce the operational burden and complexity involved in protecting
sensitive data. With encryption at rest, you can build security-sensitive
applications that meet strict encryption compliance and regulatory
requirements.

  * Encryption is turned on by default on your Timestream for LiveAnalytics database, and cannot be turned off. The industry standard AES-256 encryption algorithm is the default encryption algorithm used.

  * AWS KMS is required for encryption at rest in Timestream for LiveAnalytics.

  * You cannot encrypt only a subset of items in a table.

  * You don't need to modify your database client applications to use encryption. 

If you do not provide a key, Timestream for LiveAnalytics creates and uses an
AWS KMS key named `alias/aws/timestream` in your account.

You may use your own customer managed key in KMS to encrypt your Timestream
for LiveAnalytics data. For more information on keys in Timestream for
LiveAnalytics, see [Key management](./KeyManagement.html).

Timestream for LiveAnalytics stores your data in two storage tiers, memory
store and magnetic store. Memory store data is encrypted using a Timestream
for LiveAnalytics service key. Magnetic store data is encrypted using your AWS
KMS key.

The Timestream Query service requires credentials to access your data. These
credentials are encrypted using your KMS key.

###### Note

Timestream for LiveAnalytics doesn't call AWS KMS for every Decrypt operation.
Instead, it maintains a local cache of keys for 5 minutes with active traffic.
Any permission changes are propagated through the Timestream for LiveAnalytics
system with eventual consistency within at most 5 minutes.

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Data protection

Encryption in transit

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

