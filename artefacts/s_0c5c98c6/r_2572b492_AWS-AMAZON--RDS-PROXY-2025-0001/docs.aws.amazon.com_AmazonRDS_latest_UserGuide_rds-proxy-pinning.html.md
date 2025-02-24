# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-pinning.html'}

[](/pdfs/AmazonRDS/latest/UserGuide/rds-ug.pdf#rds-proxy-pinning "Open PDF")

[Documentation](/index.html)[Amazon RDS](/rds/index.html)[User
Guide](Welcome.html)

What RDS Proxy tracks for RDS for SQL Server databasesWhat RDS Proxy tracks
for RDS for MariaDB and RDS for MySQL databasesMinimizing pinningConditions
that cause pinning for all engine familiesConditions that cause pinning for
RDS for Microsoft SQL ServerConditions that cause pinning for RDS for MariaDB
and RDS for MySQLConditions that cause pinning for RDS for PostgreSQL

# Avoiding pinning an RDS Proxy

Multiplexing is more efficient when database requests don't rely on state
information from previous requests. In that case, RDS Proxy can reuse a
connection at the conclusion of each transaction. Examples of such state
information include most variables and configuration parameters that you can
change through `SET` or `SELECT` statements. SQL transactions on a client
connection can multiplex between underlying database connections by default.

Your connections to the proxy can enter a state known as _pinning_. When a
connection is pinned, each later transaction uses the same underlying database
connection until the session ends. Other client connections also can't reuse
that database connection until the session ends. The session ends when the
client connection is dropped.

RDS Proxy automatically pins a client connection to a specific DB connection
when it detects a session state change that isn't appropriate for other
sessions. Pinning reduces the effectiveness of connection reuse. If all or
almost all of your connections experience pinning, consider modifying your
application code or workload to reduce the conditions that cause the pinning.

For example, your application changes a session variable or configuration
parameter. In this case, later statements can rely on the new variable or
parameter to be in effect. Thus, when RDS Proxy processes requests to change
session variables or configuration settings, it pins that session to the DB
connection. That way, the session state remains in effect for all later
transactions in the same session.

For some database engines, this rule doesn't apply to all parameters that you
can set. RDS Proxy tracks certain statements and variables. Thus, RDS Proxy
doesn't pin the session when you modify them. In this case, RDS Proxy only
reuses the connection for other sessions that have the same values for those
settings. For details about what RDS Proxy tracks for a database engine, see
the following:

  * What RDS Proxy tracks for RDS for SQL Server databases

  * What RDS Proxy tracks for RDS for MariaDB and RDS for MySQL databases

## What RDS Proxy tracks for RDS for SQL Server databases

RDS Proxy tracks the following SQL Server statements:

  * `USE`

  * `SET ANSI_NULLS`

  * `SET ANSI_PADDING`

  * `SET ANSI_WARNINGS`

  * `SET ARITHABORT`

  * `SET CONCAT_NULL_YIELDS_NULL`

  * `SET CURSOR_CLOSE_ON_COMMIT`

  * `SET DATEFIRST`

  * `SET DATEFORMAT`

  * `SET LANGUAGE`

  * `SET LOCK_TIMEOUT`

  * `SET NUMERIC_ROUNDABORT`

  * `SET QUOTED_IDENTIFIER`

  * `SET TEXTSIZE`

  * `SET TRANSACTION ISOLATION LEVEL`

## What RDS Proxy tracks for RDS for MariaDB and RDS for MySQL databases

RDS Proxy tracks the following MariaDB and MySQL statements:

  * DROP DATABASE

  * DROP SCHEMA

  * USE

RDS Proxy tracks the following MySQL and MariaDB variables:

  * `AUTOCOMMIT`

  * `AUTO_INCREMENT_INCREMENT`

  * `CHARACTER SET (or CHAR SET)`

  * `CHARACTER_SET_CLIENT`

  * `CHARACTER_SET_DATABASE`

  * `CHARACTER_SET_FILESYSTEM`

  * `CHARACTER_SET_CONNECTION`

  * `CHARACTER_SET_RESULTS`

  * `CHARACTER_SET_SERVER`

  * `COLLATION_CONNECTION`

  * `COLLATION_DATABASE`

  * `COLLATION_SERVER`

  * `INTERACTIVE_TIMEOUT`

  * `NAMES`

  * `NET_WRITE_TIMEOUT`

  * `QUERY_CACHE_TYPE`

  * `SESSION_TRACK_SCHEMA`

  * `SQL_MODE`

  * `TIME_ZONE`

  * `TRANSACTION_ISOLATION (or TX_ISOLATION)`

  * `TRANSACTION_READ_ONLY (or TX_READ_ONLY)`

  * `WAIT_TIMEOUT`

###### Note

RDS Proxy tracks changes to the `TRANSACTION_ISOLATION` and
`TRANSACTION_READ_ONLY` variables when you set them at the session scope.
However, if you set them at the next transaction scope, RDS Proxy pins
connections. This behavior applies whether you use a `SET` statement or a `SET
TRANSACTION` statement to configure these values.

## Minimizing pinning

Performance tuning for RDS Proxy involves trying to maximize transaction-level
connection reuse (multiplexing) by minimizing pinning.

You can minimize pinning by doing the following:

  * Avoid unnecessary database requests that might cause pinning. 

  * Set variables and configuration settings consistently across all connections. That way, later sessions are more likely to reuse connections that have those particular settings. 

However, for PostgreSQL setting a variable leads to session pinning.

  * For a MySQL engine family database, apply a session pinning filter to the proxy. You can exempt certain kinds of operations from pinning the session if you know that doing so doesn't affect the correct operation of your application. 

  * See how frequently pinning occurs by monitoring the Amazon CloudWatch metric `DatabaseConnectionsCurrentlySessionPinned`. For information about this and other CloudWatch metrics, see [Monitoring RDS Proxy metrics with Amazon CloudWatch](./rds-proxy.monitoring.html). 

  * If you use `SET` statements to perform identical initialization for each client connection, you can do so while preserving transaction-level multiplexing. In this case, you move the statements that set up the initial session state into the initialization query used by a proxy. This property is a string containing one or more SQL statements, separated by semicolons. 

For example, you can define an initialization query for a proxy that sets
certain configuration parameters. Then, RDS Proxy applies those settings
whenever it sets up a new connection for that proxy. You can remove the
corresponding `SET` statements from your application code, so that they don't
interfere with transaction-level multiplexing.

For metrics about how often pinning occurs for a proxy, see [Monitoring RDS
Proxy metrics with Amazon CloudWatch](./rds-proxy.monitoring.html).

## Conditions that cause pinning for all engine families

The proxy pins the session to the current connection in the following
situations where multiplexing might cause unexpected behavior:

  * Any statement with a text size greater than 16 KB causes the proxy to pin the session.

## Conditions that cause pinning for RDS for Microsoft SQL Server

For RDS for SQL Server, the following interactions also cause pinning:

  * Using multiple active result sets (MARS). For information about MARS, see the [SQL Server](https://docs.microsoft.com/en-us/sql/relational-databases/native-client/features/using-multiple-active-result-sets-mars?view=sql-server-ver16) documentation.

  * Using distributed transaction coordinator (DTC) communication.

  * Creating temporary tables, transactions, cursors, or prepared statements.

  * Using the following `SET` statements:

    * `SET ANSI_DEFAULTS`

    * `SET ANSI_NULL_DFLT`

    * `SET ARITHIGNORE`

    * `SET DEADLOCK_PRIORITY`

    * `SET FIPS_FLAGGER`

    * `SET FMTONLY`

    * `SET FORCEPLAN`

    * `SET IDENTITY_INSERT`

    * `SET NOCOUNT`

    * `SET NOEXEC`

    * `SET OFFSETS`

    * `SET PARSEONLY`

    * `SET QUERY_GOVERNOR_COST_LIMIT`

    * `SET REMOTE_PROC_TRANSACTIONS`

    * `SET ROWCOUNT`

    * `SET SHOWPLAN_ALL`, `SHOWPLAN_TEXT`, and `SHOWPLAN_XML`

    * `SET STATISTICS`

    * `SET XACT_ABORT`

## Conditions that cause pinning for RDS for MariaDB and RDS for MySQL

For MariaDB and MySQL, the following interactions also cause pinning:

  * Explicit table lock statements `LOCK TABLE`, `LOCK TABLES`, or `FLUSH TABLES WITH READ LOCK` cause the proxy to pin the session. 

  * Creating named locks by using `GET_LOCK` causes the proxy to pin the session. 

  * Setting a user or system variable (with some exceptions) pins the session to the proxy. If this significantly limits connection reuse, you can configure `SET` operations to avoid pinning. To do this, adjust the session pinning filters property. For more information, see [Creating an RDS proxy](./rds-proxy-creating.html) and [Modifying an RDS Proxy](./rds-proxy-modifying-proxy.html).

  * Creating a temporary table causes the proxy to pin the session. That way, the contents of the temporary table are preserved throughout the session regardless of transaction boundaries. 

  * Calling the `ROW_COUNT` and `FOUND_ROWS` functions sometimes causes pinning. 

  * Prepared statements cause the proxy to pin the session. This rule applies whether the prepared statement uses SQL text or the binary protocol. 

  * RDS Proxy does not pin connections when you use SET LOCAL.

  * Calling stored procedures and stored functions doesn't cause pinning. RDS Proxy doesn't detect any session state changes resulting from such calls. Make sure that your application doesn't change session state inside stored routines if you rely on that session state to persist across transactions. For example, RDS Proxy isn't currently compatible with a stored procedure that creates a temporary table that persists across all transactions. 

If you have expert knowledge about your application behavior, you can skip the
pinning behavior for certain application statements. To do so, choose the
**Session pinning filters** option when creating the proxy. Currently, you can
opt out of session pinning for setting session variables and configuration
settings.

## Conditions that cause pinning for RDS for PostgreSQL

For PostgreSQL, the following interactions also cause pinning:

  * Using `SET` commands.

  * Using `PREPARE`, `DISCARD`, `DEALLOCATE`, or `EXECUTE` commands to manage prepared statements.

  * Creating temporary sequences, tables, or views.

  * Declaring cursors.

  * Discarding the session state.

  * Listening on a notification channel.

  * Loading a library module such as `auto_explain`.

  * Manipulating sequences using functions such as `nextval` and `setval`.

  * Interacting with locks using functions such as `pg_advisory_lock` and `pg_try_advisory_lock`. 

###### Note

RDS Proxy does not pin on transaction level advisory locks, specifically
`pg_advisory_xact_lock`, `pg_advisory_xact_lock_shared`,
`pg_try_advisory_xact_lock`, and `pg_try_advisory_xact_lock_shared`.

  * Setting a parameter, or resetting a parameter to its default. Specifically, using `SET` and `set_config` commands to assign default values to session variables.

  * Calling stored procedures and stored functions doesn't cause pinning. RDS Proxy doesn't detect any session state changes resulting from such calls. Make sure that your application doesn't change session state inside stored routines if you rely on that session state to persist across transactions. For example, RDS Proxy isn't currently compatible with a stored procedure that creates a temporary table that persists across all transactions. 

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

RDS Proxy connection considerations

Deleting an RDS Proxy

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

