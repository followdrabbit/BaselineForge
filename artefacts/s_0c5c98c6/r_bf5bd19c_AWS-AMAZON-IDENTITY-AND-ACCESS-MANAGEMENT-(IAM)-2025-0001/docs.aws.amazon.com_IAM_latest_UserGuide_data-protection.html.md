# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/IAM/latest/UserGuide/data-protection.html'}

[](/pdfs/IAM/latest/UserGuide/iam-ug.pdf#data-protection "Open PDF")

[Documentation](/index.html)[AWS Identity and Access
Management](/iam/index.html)[User Guide](introduction.html)

Data encryption in IAM and AWS STSKey management in IAM and AWS
STSInternetwork traffic privacy in IAM and AWS STS

# Data protection in AWS Identity and Access Management

The AWS [shared responsibility
model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies
to data protection in AWS Identity and Access Management. As described in this
model, AWS is responsible for protecting the global infrastructure that runs
all of the AWS Cloud. You are responsible for maintaining control over your
content that is hosted on this infrastructure. You are also responsible for
the security configuration and management tasks for the AWS services that you
use. For more information about data privacy, see the [Data Privacy
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
text fields such as a **Name** field. This includes when you work with IAM or
other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that
you enter into tags or free-form text fields used for names may be used for
billing or diagnostic logs. If you provide a URL to an external server, we
strongly recommend that you do not include credentials information in the URL
to validate your request to that server.

## Data encryption in IAM and AWS STS

Data encryption typically falls into two categories: encryption at rest and
encryption in transit.

### Encryption at rest

Data that is collected and stored by IAM is encrypted at rest.

  * **IAM** â Data collected and stored within IAM includes IP addresses, customer account metadata, and customer identifying data that includes passwords. Customer account metadata and customer identifying data are encrypted at rest using AES 256 or is hashed using SHA 256.

  * **AWS STS** â AWS STS does not collect customer content except for service logs that log successful, erroneous, and faulty requests to the service. 

### Encryption in transit

Customer identifying data, including passwords, is encrypted in transit using
TLS 1.2 and 1.3. All AWS STS endpoints support HTTPS for encrypting data in
transit. For a list of AWS STS endpoints, see [AWS STS Regions and
endpoints](./id_credentials_temp_region-endpoints.html).

## Key management in IAM and AWS STS

You can't manage encryption keys using IAM or AWS STS. For more information
about encryption keys, see [What is AWS
KMS?](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) in
the AWS Key Management Service Developer Guide

## Internetwork traffic privacy in IAM and AWS STS

Requests to IAM must be made using Transport Layer Security protocol (TLS).
You can secure connections to the AWS STS service by using VPC endpoints. To
learn more, see [Interface VPC
endpoints](./reference_interface_vpc_endpoints.html).

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

AWS security audit guidelines

Logging and monitoring

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

