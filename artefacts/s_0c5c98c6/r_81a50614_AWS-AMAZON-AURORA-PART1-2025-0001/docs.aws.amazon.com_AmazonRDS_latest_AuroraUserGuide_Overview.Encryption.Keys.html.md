# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.Keys.html'}

[](/pdfs/AmazonRDS/latest/AuroraUserGuide/aurora-
ug.pdf#Overview.Encryption.Keys "Open PDF")

[Documentation](/index.html)[Amazon RDS](/rds/index.html)[User Guide for
Aurora](CHAP_AuroraOverview.html)

Authorizing use of a customer managed keyAmazon RDS encryption context

# AWS KMS key management

Amazon Aurora automatically integrates with [AWS Key Management Service (AWS
KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/) for key
management. Amazon Aurora uses envelope encryption. For more information about
envelope encryption, see [ Envelope
encryption](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#enveloping)
in the _AWS Key Management Service Developer Guide_.

You can use two types of AWS KMS keys to encrypt your DB clusters.

  * If you want full control over a KMS key, you must create a _customer managed key_. For more information about customer managed keys, see [Customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) in the _AWS Key Management Service Developer Guide_.

  * _AWS managed keys_ are KMS keys in your account that are created, managed, and used on your behalf by an AWS service that is integrated with AWS KMS. By default, the RDS AWS managed key (`aws/rds`) is used for encryption. You can't manage, rotate, or delete the RDS AWS managed key. For more information about AWS managed keys, see [AWS managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk) in the _AWS Key Management Service Developer Guide_.

To manage KMS keys used for Amazon Aurora encrypted DB clusters, use the [AWS
Key Management Service (AWS
KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/) in the [AWS KMS
console](https://console.aws.amazon.com/kms), the AWS CLI, or the AWS KMS API.
To view audit logs of every action taken with an AWS managed or customer
managed key, use [AWS
CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/). For
more information about key rotation, see [Rotating AWS KMS
keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html).

## Authorizing use of a customer managed key

When Aurora uses a customer managed key in cryptographic operations, it acts
on behalf of the user who is creating or changing the Aurora resource.

To create an Aurora resource using a customer managed key, a user must have
permissions to call the following operations on the customer managed key:

  * `kms:CreateGrant`

  * `kms:DescribeKey`

You can specify these required permissions in a key policy, or in an IAM
policy if the key policy allows it.

###### Tip

To follow the principle of least privilege, do not allow full access to
`kms:CreateGrant`. Instead, use the [kms:ViaService condition
key](https://docs.aws.amazon.com/kms/latest/developerguide/policy-
conditions.html#conditions-kms-via-service) to allow the user to create grants
on the KMS key only when the grant is created on the user's behalf by an AWS
service.

You can make the IAM policy stricter in various ways. For example, if you want
to allow the customer managed key to be used only for requests that originate
in Aurora, use the [ kms:ViaService condition
key](https://docs.aws.amazon.com/kms/latest/developerguide/policy-
conditions.html#conditions-kms-via-service) with the
`rds.`<region>`.amazonaws.com` value. Also, you can use the keys or values in
the Amazon RDS encryption context as a condition for using the customer
managed key for encryption.

For more information, see [Allowing users in other accounts to use a KMS
key](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-
modifying-external-accounts.html) in the _AWS Key Management Service Developer
Guide_ and [Key policies in AWS
KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies).

## Amazon RDS encryption context

When Aurora uses your KMS key, or when Amazon EBS uses the KMS key on behalf
of Aurora, the service specifies an [encryption
context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context).
The encryption context is [additional authenticated
data](https://docs.aws.amazon.com/crypto/latest/userguide/cryptography-
concepts.html#term-aad) (AAD) that AWS KMS uses to ensure data integrity. When
an encryption context is specified for an encryption operation, the service
must specify the same encryption context for the decryption operation.
Otherwise, decryption fails. The encryption context is also written to your
[AWS CloudTrail](https://aws.amazon.com/cloudtrail/) logs to help you
understand why a given KMS key was used. Your CloudTrail logs might contain
many entries describing the use of a KMS key, but the encryption context in
each log entry can help you determine the reason for that particular use.

At minimum, Aurora always uses the DB cluster ID for the encryption context,
as in the following JSON-formatted example:

    
    
    { "aws:rds:dbc-id": "cluster-CQYSMDPBRZ7BPMH7Y3RTDG5QY" }

This encryption context can help you identify the DB cluster for which your
KMS key was used.

When your KMS key is used for a specific DB cluster and a specific Amazon EBS
volume, both the DB cluster ID and the Amazon EBS volume ID are used for the
encryption context, as in the following JSON-formatted example:

    
    
    {
      "aws:rds:dbc-id": "cluster-BRG7VYS3SVIFQW7234EJQOM5RQ",
      "aws:ebs:id": "vol-ad8c6542"
    }

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Encrypting Amazon Aurora resources

Using SSL/TLS to encrypt a connection

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

