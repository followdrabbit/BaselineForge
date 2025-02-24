# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.html'}

[](/pdfs/AmazonRDS/latest/AuroraUserGuide/aurora-ug.pdf#UsingWithRDS "Open
PDF")

[Documentation](/index.html)[Amazon RDS](/rds/index.html)[User Guide for
Aurora](CHAP_AuroraOverview.html)

# Security in Amazon Aurora

Cloud security at AWS is the highest priority. As an AWS customer, you benefit
from a data center and network architecture that are built to meet the
requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared
responsibility model](https://aws.amazon.com/compliance/shared-responsibility-
model/) describes this as security _of_ the cloud and security _in_ the cloud:

  * **Security of the cloud** â AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS compliance programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to Amazon Aurora (Aurora), see [AWS services in scope by compliance program](https://aws.amazon.com/compliance/services-in-scope/).

  * **Security in the cloud** â Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your organization's requirements, and applicable laws and regulations. 

This documentation helps you understand how to apply the shared responsibility
model when using Amazon Aurora. The following topics show you how to configure
Amazon Aurora to meet your security and compliance objectives. You also learn
how to use other AWS services that help you monitor and secure your Amazon
Aurora resources.

You can manage access to your Amazon Aurora resources and your databases on a
DB cluster. The method you use to manage access depends on what type of task
the user needs to perform with Amazon Aurora:

  * Run your DB cluster in a virtual private cloud (VPC) based on the Amazon VPC service for the greatest possible network access control. For more information about creating a DB cluster in a VPC, see [Amazon VPC and Amazon Aurora](./USER_VPC.html).

  * Use AWS Identity and Access Management (IAM) policies to assign permissions that determine who is allowed to manage Amazon Aurora resources. For example, you can use IAM to determine who is allowed to create, describe, modify, and delete DB clusters, tag resources, or modify security groups.

To review IAM policy examples, see [Identity-based policy examples for Amazon
Aurora](./security_iam_id-based-policy-examples.html).

  * Use security groups to control what IP addresses or Amazon EC2 instances can connect to your databases on a DB cluster. When you first create a DB cluster, its firewall prevents any database access except through rules specified by an associated security group. 

  * Use Secure Socket Layer (SSL) or Transport Layer Security (TLS) connections with DB clusters running the Aurora MySQL or Aurora PostgreSQL. For more information on using SSL/TLS with a DB cluster, see [Using SSL/TLS to encrypt a connection to a DB cluster](./UsingWithRDS.SSL.html).

  * Use Amazon Aurora encryption to secure your DB clusters and snapshots at rest. Amazon Aurora encryption uses the industry standard AES-256 encryption algorithm to encrypt your data on the server that hosts your DB cluster. For more information, see [Encrypting Amazon Aurora resources](./Overview.Encryption.html).

  * Use the security features of your DB engine to control who can log in to the databases on a DB cluster. These features work just as if the database was on your local network. 

For information about security with Aurora MySQL, see [Security with Amazon
Aurora MySQL](./AuroraMySQL.Security.html). For information about security
with Aurora PostgreSQL, see [Security with Amazon Aurora
PostgreSQL](./AuroraPostgreSQL.Security.html).

Aurora is part of the managed database service Amazon Relational Database
Service (Amazon RDS). Amazon RDS is a web service that makes it easier to set
up, operate, and scale a relational database in the cloud. If you are not
already familiar with Amazon RDS, see the [_Amazon RDS user
guide_](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html).

Aurora includes a high-performance storage subsystem. Its MySQL- and
PostgreSQL-compatible database engines are customized to take advantage of
that fast distributed storage. Aurora also automates and standardizes database
clustering and replication, which are typically among the most challenging
aspects of database configuration and administration.

For both Amazon RDS and Aurora, you can access the RDS API programmatically,
and you can use the AWS CLI to access the RDS API interactively. Some RDS API
operations and AWS CLI commands apply to both Amazon RDS and Aurora, while
others apply to either Amazon RDS or Aurora. For information about RDS API
operations, see [Amazon RDS API
reference](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/Welcome.html).
For more information about the AWS CLI, see [AWS Command Line Interface
reference for Amazon
RDS](https://docs.aws.amazon.com/cli/latest/reference/rds/index.html).

###### Note

You have to configure security only for your use cases. You don't have to
configure security access for processes that Amazon Aurora manages. These
include creating backups, automatic failover, and other processes.

For more information on managing access to Amazon Aurora resources and your
databases on a DB cluster, see the following topics.

###### Topics

  * [Database authentication with Amazon Aurora](./database-authentication.html)
  * [Password management with Amazon Aurora and AWS Secrets Manager](./rds-secrets-manager.html)
  * [Data protection in Amazon RDS](./DataDurability.html)
  * [Identity and access management for Amazon Aurora](./UsingWithRDS.IAM.html)
  * [Logging and monitoring in Amazon Aurora](./Overview.LoggingAndMonitoring.html)
  * [Compliance validation for Amazon Aurora](./RDS-compliance.html)
  * [Resilience in Amazon Aurora](./disaster-recovery-resiliency.html)
  * [Infrastructure security in Amazon Aurora](./infrastructure-security.html)
  * [Amazon RDS API and interface VPC endpoints (AWS PrivateLink)](./vpc-interface-endpoints.html)
  * [Security best practices for Amazon Aurora](./CHAP_BestPractices.Security.html)
  * [Controlling access with security groups](./Overview.RDSSecurityGroups.html)
  * [Master user account privileges](./UsingWithRDS.MasterAccounts.html)
  * [Using service-linked roles for Amazon Aurora](./UsingWithRDS.IAM.ServiceLinkedRoles.html)
  * [Amazon VPC and Amazon Aurora](./USER_VPC.html)

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Performing an Aurora proof of concept

Database authentication

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

