# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/timestream/latest/developerguide/best-practices-security-preventative.html'}

[](/pdfs/timestream/latest/developerguide/timestream.pdf#best-practices-
security-preventative "Open PDF")

[Documentation](/index.html)[Amazon
Timestream](/timestream/index.html)[Developer Guide](what-is-timestream.html)

# Timestream for LiveAnalytics preventative security best practices

The following best practices can help you anticipate and prevent security
incidents in Timestream for LiveAnalytics.

**Encryption at rest**

    

Timestream for LiveAnalytics encrypts at rest all user data stored in tables
using encryption keys stored in [AWS Key Management Service (AWS
KMS)](https://aws.amazon.com/kms/). This provides an additional layer of data
protection by securing your data from unauthorized access to the underlying
storage.

Timestream for LiveAnalytics uses a single service default key (AWS owned CMK)
for encrypting all of your tables. If this key doesn't exist, it is created
for you. Service default keys can't be disabled. For more information, see
[Timestream for LiveAnalytics Encryption at
Rest](https://docs.aws.amazon.com/mcs/latest/devguide/EncryptionAtRest.html).

**Use IAM roles to authenticate access to Timestream for LiveAnalytics**

    

For users, applications, and other AWS services to access Timestream for
LiveAnalytics, they must include valid AWS credentials in their AWS API
requests. You should not store AWS credentials directly in the application or
EC2 instance. These are long-term credentials that are not automatically
rotated, and therefore could have significant business impact if they are
compromised. An IAM role enables you to obtain temporary access keys that can
be used to access AWS services and resources.

For more information, see [IAM
Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html).

**Use IAM policies for Timestream for LiveAnalytics base authorization**

    

When granting permissions, you decide who is getting them, which Timestream
for LiveAnalytics APIs they are getting permissions for, and the specific
actions you want to allow on those resources. Implementing least privilege is
key in reducing security risk and the impact that can result from errors or
malicious intent.

Attach permissions policies to IAM identities (that is, users, groups, and
roles) and thereby grant permissions to perform operations on Timestream for
LiveAnalytics resources.

You can do this by using the following:

  * [AWS managed (predefined) policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies)

  * [Customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies)

  * [Tag-based authorization](./security_iam_service-with-iam.html#security_iam_service-with-iam-tags)

**Consider client-side encryption**

    

If you store sensitive or confidential data in Timestream for LiveAnalytics,
you might want to encrypt that data as close as possible to its origin so that
your data is protected throughout its lifecycle. Encrypting your sensitive
data in transit and at rest helps ensure that your plaintext data isn't
available to any third party.

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Security best practices

Working with other services

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

