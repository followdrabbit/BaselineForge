# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html'}

[](/pdfs/AmazonRDS/latest/UserGuide/rds-ug.pdf#rds-proxy "Open PDF")

[Documentation](/index.html)[Amazon RDS](/rds/index.html)[User
Guide](Welcome.html)

Region and version availabilityQuotas and limitations

# Amazon RDS Proxy

By using Amazon RDS Proxy, you can allow your applications to pool and share
database connections to improve their ability to scale. RDS Proxy makes
applications more resilient to database failures by automatically connecting
to a standby DB instance while preserving application connections. By using
RDS Proxy, you can also enforce AWS Identity and Access Management (IAM)
authentication for databases, and securely store credentials in AWS Secrets
Manager.

Using RDS Proxy, you can handle unpredictable surges in database traffic.
Otherwise, these surges might cause issues due to oversubscribing connections
or new connections being created at a fast rate. RDS Proxy establishes a
database connection pool and reuses connections in this pool. This approach
avoids the memory and CPU overhead of opening a new database connection each
time. To protect a database against oversubscription, you can control the
number of database connections that are created.

RDS Proxy queues or throttles application connections that can't be served
immediately from the connection pool. Although latencies might increase, your
application can continue to scale without abruptly failing or overwhelming the
database. If connection requests exceed the limits you specify, RDS Proxy
rejects application connections (that is, it sheds load). At the same time, it
maintains predictable performance for the load that RDS can serve with the
available capacity.

You can reduce the overhead to process credentials and establish a secure
connection for each new connection. RDS Proxy can handle some of that work on
behalf of the database.

RDS Proxy is fully compatible with the engine versions that it supports. You
can enable RDS Proxy for most applications with no code changes.

###### Topics

  * Region and version availability
  * Quotas and limitations for RDS Proxy
  * [Planning where to use RDS Proxy](./rds-proxy-planning.html)
  * [RDS Proxy concepts and terminology](./rds-proxy.howitworks.html)
  * [Getting started with RDS Proxy](./rds-proxy-setup.html)
  * [Managing an RDS Proxy](./rds-proxy-managing.html)
  * [Working with Amazon RDS Proxy endpoints](./rds-proxy-endpoints.html)
  * [Monitoring RDS Proxy metrics with Amazon CloudWatch](./rds-proxy.monitoring.html)
  * [Working with RDS Proxy events](./rds-proxy.events.html)
  * [Troubleshooting for RDS Proxy](./rds-proxy.troubleshooting.html)
  * [Using RDS Proxy with AWS CloudFormation](./rds-proxy-cfn.html)

## Region and version availability

Feature availability and support varies across specific versions of each
database engine, and across AWS Regions. For more information on version and
Region availability of Amazon RDS with RDS Proxy, see [Supported Regions and
DB engines for Amazon RDS Proxy](./Concepts.RDS_Fea_Regions_DB-
eng.Feature.RDSProxy.html).

## Quotas and limitations for RDS Proxy

The following quotas and limitations apply to RDS Proxy:

  * Each AWS account ID is limited to 20 proxies. If your application requires more proxies, request an increase via the **Service Quotas** page within the AWS Management Console. In the **Service Quotas** page, select **Amazon Relational Database Service (Amazon RDS)** and locate **Proxies** to request a quota increase. AWS can automatically increase your quota or pending review of your request by Support.

  * Each proxy can have up to 200 associated Secrets Manager secrets. Thus, each proxy can connect to with up to 200 different user accounts at any given time. 

  * Each proxy has a default endpoint. You can also add up to 20 proxy endpoints for each proxy. You can create, view, modify, and delete these endpoints. 

  * For RDS DB instances in replication configurations, you can associate a proxy only with the writer DB instance, not a read replica.

  * Your RDS Proxy must be in the same virtual private cloud (VPC) as the database. The proxy can't be publicly accessible, although the database can be. For example, if you're prototyping your database on a local host, you can't connect to your proxy unless you set up the necessary network requirements to allow connection to the proxy. This is because your local host is outside of the proxyâs VPC. 

  * You can't use RDS Proxy with a VPC that has its tenancy set to `dedicated`. 

  * If you use RDS Proxy with an RDS DB instance that has IAM authentication enabled, check user authentication. Users who connect through a proxy must authenticate through sign-in credentials. For details about Secrets Manager and IAM support in RDS Proxy, see [Setting up database credentials in AWS Secrets Manager for RDS Proxy](./rds-proxy-secrets-arns.html) and [Configuring IAM authentication for RDS Proxy](./rds-proxy-iam-setup.html). 

  * You can't use RDS Proxy with custom DNS when using SSL hostname validation. 

  * Each proxy can be associated with a single target DB instance . However, you can associate multiple proxies with the same DB instance .

  * Any statement with a text size greater than 16 KB causes the proxy to pin the session to the current connection.

  * Certain Regions have Availability-Zone (AZ) restrictions to consider while creating your proxy. US East (N. Virginia) Region does not support RDS Proxy in the `use1-az3` Availability Zone. US West (N. California) Region does not support RDS Proxy in the `usw1-az2` Availability Zone. When selecting subnets while creating your proxy, make sure that you don't select subnets in the Availability Zones mentioned above. 

  * Currently, RDS Proxy doesn't support any global condition context keys.

For more information about global condition context keys, see [AWS global
condition context
keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-
keys.html) in the _IAM User Guide_.

  * You can't use RDS Proxy with RDS Custom for SQL Server.

  * To reflect any database parameter group modification to your proxy, an instance reboot is required even if your chose to apply your changes immediately. For cluster-level parameters, a cluster-wide reboot is required.

  * Your proxy automatically creates the `rdsproxyadmin` DB user when you register a proxy target. Deleting or modifying the `rdsproxyadmin` user or its permissions might impact the availability of the proxy to your application.

For additional limitations for each DB engine, see the following sections:

  * Additional limitations for RDS for MariaDB

  * Additional limitations for RDS for Microsoft SQL Server

  * Additional limitations for RDS for MySQL

  * Additional limitations for RDS for PostgreSQL

### Additional limitations for RDS for MariaDB

The following additional limitations apply to RDS Proxy with RDS for MariaDB
databases:

  * Currently, all proxies listen on port 3306 for MariaDB. The proxies still connect to your database using the port that you specified in the database settings. 

  * You can't use RDS Proxy with self-managed MariaDB databases in Amazon EC2 instances.

  * You can't use RDS Proxy with an RDS for MariaDB DB instance that has the `read_only` parameter in its DB parameter group set to `1`.

  * RDS Proxy doesn't support MariaDB compressed mode. For example, it doesn't support the compression used by the `--compress` or `-C` options of the `mysql` command.

  * Some SQL statements and functions can change the connection state without causing pinning. For the most current pinning behavior, see [Avoiding pinning an RDS Proxy](./rds-proxy-pinning.html).

  * RDS Proxy doesn't support the MariaDB `auth_ed25519` plugin.

  * RDS Proxy doesn't support Transport Layer Security (TLS) version 1.3 for MariaDB databases.

  * Database connections processing a `GET DIAGNOSTIC` command might return inaccurate information when RDS Proxy reuses the same database connection to run another query. This can happen when RDS Proxy multiplexes database connections. For more information, see [Overview of RDS Proxy concepts](./rds-proxy.howitworks.html#rds-proxy-overview).

  * RDS Proxy currently doesn't support the `caching_sha2_password` option for `ClientPasswordAuthType` for MariaDB.

###### Important

For proxies associated with MariaDB databases, don't set the configuration
parameter `sql_auto_is_null` to `true` or a nonzero value in the
initialization query. Doing so might cause incorrect application behavior.

### Additional limitations for RDS for Microsoft SQL Server

The following additional limitations apply to RDS Proxy with RDS for Microsoft
SQL Server databases:

  * The number of Secrets Manager secrets that you need to create for a proxy depends on the collation that your DB instance uses. For example, suppose that your DB instance uses case-sensitive collation. If your application accepts both "Admin" and "admin," then your proxy needs two separate secrets. For more information about collation in SQL Server, see the [ Microsoft SQL Server](https://docs.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver16) documentation.

  * RDS Proxy doesn't support connections that use Active Directory.

  * You can't use IAM authentication with clients that don't support token properties. For more information, see [Considerations for connecting to a proxy with Microsoft SQL Server](./rds-proxy-connecting.html#rds-proxy-connecting-sqlserver).

  * The results of `@@IDENTITY`, `@@ROWCOUNT`, and `SCOPE_IDENTITY` aren't always accurate. As a work-around, retrieve their values in the same session statement to ensure that they return the correct information.

  * If the connection uses multiple active result sets (MARS), RDS Proxy doesn't run the initialization queries. For information about MARS, see the [ Microsoft SQL Server](https://docs.microsoft.com/en-us/sql/relational-databases/native-client/features/using-multiple-active-result-sets-mars?view=sql-server-ver16) documentation.

  * Currently, RDS Proxy does not support RDS for SQL Server DB instances that run on major version _SQL Server 2022_.

  * RDS Proxy does not support RDS for SQL Server DB instances that run on major version _SQL Server 2014_.

  * RDS Proxy does not support client applications that can't handle multiple response messages in one TLS record.

### Additional limitations for RDS for MySQL

The following additional limitations apply to RDS Proxy with RDS for MySQL
databases:

  * RDS Proxy support for `caching_sha2_password` authentication requires a secure (TLS) connection.

  * RDS Proxy support for `caching_sha2_password` is known to have compatibility issues with certain go-sql driver versions.

  * When using the MySQL 8.4 C driver, the `mysql_stmt_bind_named_param` API might form malformed packets if parameter count exceeds placeholder count in a prepared statements. This results in incorrect responses. For more information, see [MySQL bug report](https://bugs.mysql.com/bug.php?id=116860&thanks=4).

  * Currently, all proxies listen on port 3306 for MySQL. The proxies still connect to your database using the port that you specified in the database settings. 

  * You can't use RDS Proxy with self-managed MySQL databases in EC2 instances.

  * You can't use RDS Proxy with an RDS for MySQL DB instance that has the `read_only` parameter in its DB parameter group set to `1`.

  * RDS Proxy doesn't support MySQL compressed mode. For example, it doesn't support the compression used by the `--compress` or `-C` options of the `mysql` command.

  * Database connections processing a `GET DIAGNOSTIC` command might return inaccurate information when RDS Proxy reuses the same database connection to run another query. This can happen when RDS Proxy multiplexes database connections.

  * Some SQL statements and functions such as `SET LOCAL` can change the connection state without causing pinning. For the most current pinning behavior, see [Avoiding pinning an RDS Proxy](./rds-proxy-pinning.html).

  * Using the `ROW_COUNT()` function in a multi-statement query is not supported.

  * RDS Proxy does not support client applications that can't handle multiple response messages in one TLS record.

###### Important

For proxies associated with MySQL databases, don't set the configuration
parameter `sql_auto_is_null` to `true` or a nonzero value in the
initialization query. Doing so might cause incorrect application behavior.

### Additional limitations for RDS for PostgreSQL

The following additional limitations apply to RDS Proxy with RDS for
PostgreSQL databases:

  * RDS Proxy doesn't support session pinning filters for PostgreSQL.

  * Currently, all proxies listen on port 5432 for PostgreSQL.

  * For PostgreSQL, RDS Proxy doesn't currently support canceling a query from a client by issuing a `CancelRequest`. This is the case, for example, when you cancel a long-running query in an interactive psql session by using Ctrl+C. 

  * The results of the PostgreSQL function [lastval](https://www.postgresql.org/docs/current/functions-sequence.html) aren't always accurate. As a work-around, use the [INSERT](https://www.postgresql.org/docs/current/sql-insert.html) statement with the `RETURNING` clause.

  * RDS Proxy currently doesn't support streaming replication mode.

  * With RDS for PostgreSQL 16, modifications to the `scram_iterations` value exclusively impact the authentication process between the proxy and the database. Specifically, if you configure `ClientPasswordAuthType` to `scram-sha-256`, any customizations made to the `scram_iterations` value doesn't influence client-to-proxy password authentication. Instead, the iteration value for client-to-proxy password authentication is fixed at 4096.

  * The `default` database must exist.

  * If you use `ALTER ROLE` or `SET ROLE` to change the user role, subsequent connections as that user to the proxy might not use this role setting, if those connections encounter pinning. To prevent this, when using proxy, use `SET ROLE` in the initialization query of the proxy. For more information, see **Initialization query** in [Creating an RDS proxy](./rds-proxy-creating.html).

###### Important

For existing proxies with PostgreSQL databases, if you modify the database
authentication to use `SCRAM` only, the proxy becomes unavailable for up to 60
seconds. To avoid the issue, do one of the following:

  * Ensure that the database allows both `SCRAM` and `MD5` authentication.

  * To use only `SCRAM` authentication, create a new proxy, migrate your application traffic to the new proxy, then delete the proxy previously associated with the database.

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Considerations for restoring DB instances

Planning where to use RDS Proxy

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

