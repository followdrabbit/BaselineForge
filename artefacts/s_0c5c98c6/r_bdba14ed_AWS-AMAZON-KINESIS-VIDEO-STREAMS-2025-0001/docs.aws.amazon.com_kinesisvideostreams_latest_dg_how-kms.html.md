# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-kms.html'}

[](/pdfs/kinesisvideostreams/latest/dg/kinesisvideo-dg.pdf#how-kms "Open PDF")

[Documentation](/index.html)[Amazon Kinesis Video
Streams](/kinesis/index.html)[Developer Guide](what-is-kinesis-video.html)

What is server-side encryption for Kinesis Video Streams?Costs, Regions, and
performance considerationsHow do I get started with server-side
encryption?Creating and using a customer managed keyPermissions to use a
customer managed key

# Data protection in Kinesis Video Streams

You can use server-side encryption (SSE) using AWS Key Management Service (AWS
KMS) keys to meet strict data management requirements by encrypting your data
at rest in Amazon Kinesis Video Streams.

###### Topics

  * What is server-side encryption for Kinesis Video Streams?
  * Costs, Regions, and performance considerations
  * How do I get started with server-side encryption?
  * Creating and using a customer managed key
  * Permissions to use a customer managed key

## What is server-side encryption for Kinesis Video Streams?

Server-side encryption is a feature in Kinesis Video Streams that
automatically encrypts data before it's stored at rest using an AWS KMS key
that you specify. Data is encrypted before it's written to the Kinesis Video
Streams stream storage layer, and it's decrypted after it's retrieved from
storage. As a result, your data is always encrypted at rest within the Kinesis
Video Streams service.

With server-side encryption, your Kinesis video stream producers and consumers
don't need to manage KMS keys or cryptographic operations. If data retention
is enabled, your data is automatically encrypted as it enters and leaves
Kinesis Video Streams, so your data at rest is encrypted. AWS KMS provides all
the keys that are used by the server-side encryption feature. AWS KMS
streamlines the use of a KMS key for Kinesis Video Streams that's managed by
AWS, a user-specified AWS KMS key imported into the AWS KMS service.

## Costs, Regions, and performance considerations

When you apply server-side encryption, you are subject to AWS KMS API usage
and key costs. Unlike custom AWS KMS keys, the default `aws/kinesisvideo` KMS
key is offered with no charge. However, you still must pay for the API usage
costs that Kinesis Video Streams incurs on your behalf.

API usage costs apply for every KMS key, including custom ones. The AWS KMS
costs scale with the number of user credentials that you use on your data
producers and consumers because each user credential requires a unique API
call to AWS KMS.

The following describes the costs by resource:

###### Keys

  * The KMS key for Kinesis Video Streams that's managed by AWS (alias = `aws/kinesisvideo`) has no charge.

  * User-generated KMS keys are subject to AWS KMS key costs. For more information, see [AWS Key Management Service Pricing](https://aws.amazon.com/kms/pricing/#Keys).

### AWS KMS API usage

API requests to generate new data encryption keys or to retrieve existing
encryption keys increase as traffic increases, and are subject to AWS KMS
usage costs. For more information, see [AWS Key Management Service Pricing:
Usage](https://aws.amazon.com/kms/pricing/#Usage).

Kinesis Video Streams generates key requests even when retention is set to 0
(no retention).

### Availability of server-side encryption by Region

Server-side encryption of Kinesis video streams is available in all the AWS
Regions where Kinesis Video Streams is available.

## How do I get started with server-side encryption?

Server-side encryption is always enabled on Kinesis Video Streams. If a user-
provided key isn't specified when the stream is created, the AWS managed key
(provided by Kinesis Video Streams) is used.

A user-provided KMS key must be assigned to a Kinesis video stream when it's
created. You can't assign a different key to a stream using the
[UpdateStream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_UpdateStream.html)
API later on.

You can assign a user-provided KMS key to a Kinesis video stream in two ways:

  * When creating a Kinesis video stream in the AWS Management Console, specify the KMS key in the **Encryption** tab on the **Create a new video stream** page.

  * When creating a Kinesis video stream using the [CreateStream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_CreateStream.html) API, specify the key ID in the `KmsKeyId` parameter.

## Creating and using a customer managed key

This section describes how to create and use your own KMS keys instead of
using the key administered by Amazon Kinesis Video Streams.

### Creating a customer managed key

For information about how to create your own keys, see [Creating
Keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html)
in the _AWS Key Management Service Developer Guide_. After you create keys for
your account, the Kinesis Video Streams service returns these keys in the
**Customer managed keys** list.

### Using a customer managed key

After the correct permissions are applied to your consumers, producers, and
administrators, you can use custom KMS keys in your own AWS account or another
AWS account. All KMS keys in your account appear in the **Customer managed
keys** list on the console.

To use custom KMS keys that are located in another account, you must have
permissions to use those keys. You must also create the stream using the
`CreateStream` API. You can't use KMS keys from different accounts in streams
created in the console.

###### Note

The KMS key isn't accessed until the `PutMedia` or `GetMedia` operation is
carried out. This has the following results:

  * If the key that you specify doesn't exist, the `CreateStream` operation succeeds, but `PutMedia` and `GetMedia` operations on the stream fail.

  * If you use the provided key (`aws/kinesisvideo`), the key isn't present in your account until the first `PutMedia` or `GetMedia` operation is performed.

## Permissions to use a customer managed key

Before you can use server-side encryption with a customer managed key, you
must configure KMS key policies to allow encryption of streams and encryption
and decryption of stream records. For examples and more information about AWS
KMS permissions, see [AWS KMS API Permissions: Actions and Resources
Reference](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-
permissions-reference.html).

###### Note

The use of the default service key for encryption doesn't require application
of custom IAM permissions.

Before you use a customer managed key, verify that your Kinesis video stream
producers and consumers (IAM principals) are users in the AWS KMS default key
policy. Otherwise, writes and reads from a stream will fail, which could
ultimately result in data loss, delayed processing, or hung applications. You
can manage permissions for KMS keys using IAM policies. For more information,
see [Using IAM Policies with AWS
KMS](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies.html).

### Example producer permissions

Your Kinesis video stream producers must have the `kms:GenerateDataKey`
permission:

    
    
    {
      "Version": "2012-10-17",
      "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:us-west-2:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab"
        }, 
        {
            "Effect": "Allow",
            "Action": [
                "kinesis-video:PutMedia",
            ],
            "Resource": "arn:aws:kinesis-video:*:123456789012:MyStream"
        }
      ]
    }

### Example consumer Permissions

Your Kinesis video stream consumers must have the `kms:Decrypt` permission:

    
    
    {
      "Version": "2012-10-17",
      "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt"
            ],
            "Resource": "arn:aws:kms:us-west-2:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab"
        }, 
        {
            "Effect": "Allow",
            "Action": [
                "kinesis-video:GetMedia",
            ],
            "Resource": "arn:aws:kinesis-video:*:123456789012:MyStream"
        }
      ]
    }

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Security

Controlling access to Kinesis Video Streams resources using IAM

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

