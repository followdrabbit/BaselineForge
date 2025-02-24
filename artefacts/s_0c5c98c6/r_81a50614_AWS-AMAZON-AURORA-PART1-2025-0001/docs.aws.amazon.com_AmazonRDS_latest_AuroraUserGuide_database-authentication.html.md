# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/database-authentication.html'}

[](/pdfs/AmazonRDS/latest/AuroraUserGuide/aurora-ug.pdf#database-
authentication "Open PDF")

[Documentation](/index.html)[Amazon RDS](/rds/index.html)[User Guide for
Aurora](CHAP_AuroraOverview.html)

Password authenticationIAM database authenticationKerberos authentication

# Database authentication with Amazon Aurora

Amazon Aurora supports several ways to authenticate database users.

Password authentication is available by default for all DB clusters. For
Aurora MySQL and Aurora PostgreSQL, you can also add either or both IAM
database authentication and Kerberos authentication for the same DB cluster.

Password, Kerberos, and IAM database authentication use different methods of
authenticating to the database. Therefore, a specific user can log in to a
database using only one authentication method.

For PostgreSQL, use only one of the following role settings for a user of a
specific database:

  * To use IAM database authentication, assign the `rds_iam` role to the user.

  * To use Kerberos authentication, assign the `rds_ad` role to the user.

  * To use password authentication, don't assign either the `rds_iam` or `rds_ad` roles to the user.

Don't assign both the `rds_iam` and `rds_ad` roles to a user of a PostgreSQL
database either directly or indirectly by nested grant access. If the
`rds_iam` role is added to the master user, IAM authentication takes
precedence over password authentication so the master user has to log in as an
IAM user.

###### Important

We strongly recommend that you do not use the master user directly in your
applications. Instead, adhere to the best practice of using a database user
created with the minimal privileges required for your application.

###### Topics

  * Password authentication
  * IAM database authentication
  * Kerberos authentication

## Password authentication

With _password authentication,_ your database performs all administration of
user accounts. You create users with SQL statements such as `CREATE USER`,
with the appropriate clause required by the DB engine for specifying
passwords. For example, in MySQL the statement is `CREATE USER` `name`
`IDENTIFIED BY` `password`, while in PostgreSQL, the statement is `CREATE
USER` `name` `WITH PASSWORD` `password`.

With password authentication, your database controls and authenticates user
accounts. If a DB engine has strong password management features, they can
enhance security. Database authentication might be easier to administer using
password authentication when you have small user communities. Because clear
text passwords are generated in this case, integrating with AWS Secrets
Manager can enhance security.

For information about using Secrets Manager with Amazon Aurora, see [Creating
a basic
secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-
basic-secret.html) and [Rotating secrets for supported Amazon RDS
databases](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-
secrets-rds.html) in the _AWS Secrets Manager User Guide_. For information
about programmatically retrieving your secrets in your custom applications,
see [Retrieving the secret
value](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_retrieve-
secret.html) in the _AWS Secrets Manager User Guide_.

## IAM database authentication

You can authenticate to your DB cluster using AWS Identity and Access
Management (IAM) database authentication. With this authentication method, you
don't need to use a password when you connect to a DB cluster. Instead, you
use an authentication token.

For more information about IAM database authentication, including information
about availability for specific DB engines, see [IAM database
authentication](./UsingWithRDS.IAMDBAuth.html).

## Kerberos authentication

Amazon Aurora supports external authentication of database users using
Kerberos and Microsoft Active Directory. Kerberos is a network authentication
protocol that uses tickets and symmetric-key cryptography to eliminate the
need to transmit passwords over the network. Kerberos has been built into
Active Directory and is designed to authenticate users to network resources,
such as databases.

Amazon Aurora support for Kerberos and Active Directory provides the benefits
of single sign-on and centralized authentication of database users. You can
keep your user credentials in Active Directory. Active Directory provides a
centralized place for storing and managing credentials for multiple DB
clusters.

To use credentials from your self-managed Active Directory, you need to setup
a trust relationship to the AWS Directory Service for Microsoft Active
Directory that the DB cluster is joined to.

Aurora PostgreSQL and Aurora MySQL support one-way and two-way forest trust
relationships with forest-wide authentication or selective authentication.

In some scenarios, you can configure Kerberos authentication over an external
trust relationship. This requires your self-managed Active Directory to have
additional settings. This includes but is not limited to [ Kerberos Forest
Search Order](https://learn.microsoft.com/en-us/troubleshoot/windows-
server/active-directory/kfso-not-work-in-external-trust-event-is-17).

Aurora supports Kerberos authentication for Aurora MySQL and Aurora PostgreSQL
DB clusters. For more information, see [Using Kerberos authentication for
Aurora MySQL](./aurora-mysql-kerberos.html) and [Using Kerberos authentication
with Aurora PostgreSQL](./postgresql-kerberos.html).

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Security

Password management with Aurora and Secrets Manager

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

