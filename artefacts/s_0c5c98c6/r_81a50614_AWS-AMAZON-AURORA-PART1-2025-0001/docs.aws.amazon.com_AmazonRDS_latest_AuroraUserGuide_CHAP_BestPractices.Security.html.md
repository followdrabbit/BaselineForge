# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_BestPractices.Security.html'}

[](/pdfs/AmazonRDS/latest/AuroraUserGuide/aurora-
ug.pdf#CHAP_BestPractices.Security "Open PDF")

[Documentation](/index.html)[Amazon RDS](/rds/index.html)[User Guide for
Aurora](CHAP_AuroraOverview.html)

# Security best practices for Amazon Aurora

Use AWS Identity and Access Management (IAM) accounts to control access to
Amazon RDS API operations, especially operations that create, modify, or
delete Amazon Aurora resources. Such resources include DB clusters, security
groups, and parameter groups. Also use IAM to control actions that perform
common administrative actions such as backing up and restoring DB clusters.

  * Create an individual user for each person who manages Amazon Aurora resources, including yourself. Don't use AWS root credentials to manage Amazon Aurora resources.

  * Grant each user the minimum set of permissions required to perform his or her duties.

  * Use IAM groups to effectively manage permissions for multiple users.

  * Rotate your IAM credentials regularly.

  * Configure AWS Secrets Manager to automatically rotate the secrets for Amazon Aurora. For more information, see [Rotating your AWS Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) in the _AWS Secrets Manager User Guide_. You can also retrieve the credential from AWS Secrets Manager programmatically. For more information, see [Retrieving the secret value](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_retrieve-secret.html) in the _AWS Secrets Manager User Guide_.

For more information about Amazon Aurora security, see [Security in Amazon
Aurora](./UsingWithRDS.html). For more information about IAM, see [AWS
Identity and Access
Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/Welcome.html).
For information on IAM best practices, see [IAM best
practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/IAMBestPractices.html).

AWS Security Hub uses security controls to evaluate resource configurations
and security standards to help you comply with various compliance frameworks.
For more information about using Security Hub to evaluate RDS resources, see
[Amazon Relational Database Service
controls](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-
controls.html) in the AWS Security Hub User Guide.

You can monitor your usage of RDS as it relates to security best practices by
using Security Hub. For more information, see [What is AWS Security
Hub?](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-
securityhub.html).

Use the AWS Management Console, the AWS CLI, or the RDS API to change the
password for your master user. If you use another tool, such as a SQL client,
to change the master user password, it might result in privileges being
revoked for the user unintentionally.

Amazon GuardDuty is a continuous security monitoring service that analyzes and
processes various data sources, including Amazon RDS login activity. It uses
threat intelligence feeds and machine learning to identify unexpected,
potentially unauthorized, suspicious login behavior, and malicious activity
within your AWS environment.

When Amazon GuardDuty RDS Protection detects a potentially suspicious or
anomalous login attempt that indicates a threat to your database, GuardDuty
generates a new finding with details about the potentially compromised
database. For more information, see [Monitoring threats with Amazon GuardDuty
RDS Protection for Amazon Aurora](./guard-duty-rds-protection.html).

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

VPC endpoints (AWS PrivateLink)

Controlling access with security groups

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

