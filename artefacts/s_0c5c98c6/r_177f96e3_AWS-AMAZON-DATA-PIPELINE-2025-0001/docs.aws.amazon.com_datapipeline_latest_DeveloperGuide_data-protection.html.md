# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/data-protection.html'}

[](/pdfs/datapipeline/latest/DeveloperGuide/datapipeline-dg.pdf#data-
protection "Open PDF")

[Documentation](/index.html)[AWS Data Pipeline](/data-
pipeline/index.html)[Developer Guide](what-is-datapipeline.html)

AWS Data Pipeline is no longer available to new customers. Existing customers
of AWS Data Pipeline can continue to use the service as normal. [Learn
more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-
pipeline/)

# Data Protection in AWS Data Pipeline

The AWS [shared responsibility
model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies
to data protection in AWS Data Pipeline. As described in this model, AWS is
responsible for protecting the global infrastructure that runs all of the AWS
Cloud. You are responsible for maintaining control over your content that is
hosted on this infrastructure. This content includes the security
configuration and management tasks for the AWS services that you use. For more
information about data privacy, see the [Data Privacy
FAQ](https://aws.amazon.com/compliance/data-privacy-faq). For information
about data protection in Europe, see the [AWS Shared Responsibility Model and
GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-
model-and-gdpr/) blog post on the _AWS Security Blog_.

For data protection purposes, we recommend that you protect AWS account
credentials and set up individual users with AWS IAM Identity Center or AWS
Identity and Access Management (IAM). That way, each user is given only the
permissions necessary to fulfill their job duties. We also recommend that you
secure your data in the following ways:

  * Use multi-factor authentication (MFA) with each account.

  * Use SSL/TLS to communicate with AWS resources. We recommend TLS 1.2 or later.

  * Set up API and user activity logging with AWS CloudTrail.

  * Use AWS encryption solutions, along with all default security controls within AWS services.

  * Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.

  * If you require FIPS 140-2 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-2](https://aws.amazon.com/compliance/fips/).

  * AWS Data Pipeline supports IMDSv2 for Amazon EMR and Amazon EC2 resources. To use IMDSv2 with Amazon EMR, use versions 5.23.1, 5.27.1, or 5.32 or later or version 6.2 or later. For more information, see [Configure metadata service requests to Amazon EC2 instances](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-create-security-configuration.html#emr-security-configuration-imdsv2) and [Use IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html).

We strongly recommend that you never put confidential or sensitive
information, such as your customers' email addresses, into tags or free-form
text fields such as a **Name** field. This includes when you work with AWS
Data Pipeline or other AWS services using the console, API, AWS CLI, or AWS
SDKs. Any data that you enter into tags or free-form text fields used for
names may be used for billing or diagnostic logs. If you provide a URL to an
external server, we strongly recommend that you do not include credentials
information in the URL to validate your request to that server.

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Security

Identity and Access Management

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

