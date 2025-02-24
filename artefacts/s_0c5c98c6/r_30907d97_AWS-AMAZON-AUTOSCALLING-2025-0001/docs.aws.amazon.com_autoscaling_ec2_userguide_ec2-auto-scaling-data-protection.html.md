# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-data-protection.html'}

[](/pdfs/autoscaling/ec2/userguide/as-dg.pdf#ec2-auto-scaling-data-protection
"Open PDF")

[Documentation](/index.html)[Auto Scaling](/autoscaling/index.html)[User
Guide](what-is-amazon-ec2-auto-scaling.html)

Use AWS KMS keys to encrypt Amazon EBS volumesRelated resources

# Data protection in Amazon EC2 Auto Scaling

The AWS [shared responsibility
model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies
to data protection in Amazon EC2 Auto Scaling. As described in this model, AWS
is responsible for protecting the global infrastructure that runs all of the
AWS Cloud. You are responsible for maintaining control over your content that
is hosted on this infrastructure. You are also responsible for the security
configuration and management tasks for the AWS services that you use. For more
information about data privacy, see the [Data Privacy
FAQ](https://aws.amazon.com/compliance/data-privacy-faq/). For information
about data protection in Europe, see the [AWS Shared Responsibility Model and
GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-
model-and-gdpr/) blog post on the _AWS Security Blog_.

For data protection purposes, we recommend that you protect AWS account
credentials and set up individual users with AWS IAM Identity Center or AWS
Identity and Access Management (IAM). That way, each user is given only the
permissions necessary to fulfill their job duties. We also recommend that you
secure your data in the following ways:

  * Use multi-factor authentication (MFA) with each account.

  * Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.

  * Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html) in the _AWS CloudTrail User Guide_.

  * Use AWS encryption solutions, along with all default security controls within AWS services.

  * Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.

  * If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive
information, such as your customers' email addresses, into tags or free-form
text fields such as a **Name** field. This includes when you work with Amazon
EC2 Auto Scaling or other AWS services using the console, API, AWS CLI, or AWS
SDKs. Any data that you enter into tags or free-form text fields used for
names may be used for billing or diagnostic logs. If you provide a URL to an
external server, we strongly recommend that you do not include credentials
information in the URL to validate your request to that server.

When you launch an Amazon EC2 instance, you have the option of passing user
data to the instance to do additional configuration when the instance boots.
We also recommend that you never put confidential or sensitive information in
the user data that will get passed to an instance.

## Use AWS KMS keys to encrypt Amazon EBS volumes

You can configure your Auto Scaling group to encrypt Amazon EBS volume data
stored in the cloud with AWS KMS keys. Amazon EC2 Auto Scaling supports AWS
managed and customer managed keys to encrypt your data. Note that the
`KmsKeyId` option to specify a customer managed key is not available when you
use a launch configuration. To specify your customer managed key, use a launch
template instead. For more information, see [Create a launch template for an
Auto Scaling group](./create-launch-template.html). For information about how
to create, store, and manage your AWS KMS encryption keys, see the [AWS Key
Management Service Developer
Guide](https://docs.aws.amazon.com/kms/latest/developerguide/).

You can also configure a customer managed key in your EBS-backed AMI before
setting up the launch template or launch configuration, or use encryption by
default to enforce the encryption of the new EBS volumes and snapshot copies
that you create. For more information, see [Use encryption with EBS-backed
AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html)
in the _Amazon EC2 User Guide_ and [Encryption by
default](https://docs.aws.amazon.com/ebs/latest/userguide/encryption-by-
default.html) in the _Amazon EBS User Guide_.

###### Note

For information about how to set up the key policy that you need to launch
Auto Scaling instances when you use a customer managed key for encryption, see
[Required AWS KMS key policy for use with encrypted volumes](./key-policy-
requirements-EBS-encryption.html).

## Related resources

For the data protection guidelines provided by Amazon EBS, see [Data
protection in Amazon Elastic Block
Store](https://docs.aws.amazon.com/ebs/latest/userguide/data-protection.html)
in the _Amazon EBS User Guide_.

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Resilience

AWS KMS key policy for use with encrypted volumes

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

