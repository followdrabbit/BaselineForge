# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.MasterAccounts.html'}

[](/pdfs/AmazonRDS/latest/AuroraUserGuide/aurora-
ug.pdf#UsingWithRDS.MasterAccounts "Open PDF")

[Documentation](/index.html)[Amazon RDS](/rds/index.html)[User Guide for
Aurora](CHAP_AuroraOverview.html)

# Master user account privileges

When you create a new DB cluster, the default master user that you use gets
certain privileges for that DB cluster. You can't change the master user name
after the DB cluster is created.

###### Important

We strongly recommend that you do not use the master user directly in your
applications. Instead, adhere to the best practice of using a database user
created with the minimal privileges required for your application.

###### Note

If you accidentally delete the permissions for the master user, you can
restore them by modifying the DB cluster and setting a new master user
password. For more information about modifying a DB cluster, see [Modifying an
Amazon Aurora DB cluster](./Aurora.Modifying.html).

The following table shows the privileges and database roles the master user
gets for each of the database engines.

Database engine | System privilege | Database role  
---|---|---  
Aurora MySQL |  Version 2: `ALTER`, `ALTER ROUTINE`, `CREATE`, `CREATE ROUTINE`, `CREATE TEMPORARY TABLES`, `CREATE USER`, `CREATE VIEW`, `DELETE`, `DROP`, `EVENT`, `EXECUTE`, `GRANT OPTION`, `INDEX`, `INSERT`, `LOAD FROM S3`, `LOCK TABLES`, `PROCESS`, `REFERENCES`, `RELOAD`, `REPLICATION CLIENT`, `REPLICATION SLAVE`, `SELECT`, `SELECT INTO S3`, `SHOW DATABASES`, `SHOW VIEW`, `TRIGGER`, `UPDATE` | â  
Version 3: `ALTER`, `APPLICATION_PASSWORD_ADMIN`, `ALTER ROUTINE`, `CONNECTION_ADMIN`, `CREATE`, `CREATE ROLE`, `CREATE ROUTINE`, `CREATE TEMPORARY TABLES`, `CREATE USER`, `CREATE VIEW`, `DELETE`, `DROP`, `DROP ROLE`, `EVENT`, `EXECUTE`, `INDEX`, `INSERT`, `LOCK TABLES`, `PROCESS`, `REFERENCES`, `RELOAD`, `REPLICATION CLIENT`, `REPLICATION SLAVE`, `ROLE_ADMIN`, `SET_USER_ID`, `SELECT`, `SHOW DATABASES`, `SHOW_ROUTINE` (Aurora MySQL version 3.04 and higher), `SHOW VIEW`, `TRIGGER`, `UPDATE`, `XA_RECOVER_ADMIN` |  `rds_superuser_role` For more information about rds_superuser_role, see [Role-based privilege model](./AuroraMySQL.Compare-80-v3.html#AuroraMySQL.privilege-model).  
Aurora PostgreSQL | `LOGIN`, `NOSUPERUSER`, `INHERIT`, `CREATEDB`, `CREATEROLE`, `NOREPLICATION`, `VALID UNTIL 'infinity'` | `RDS_SUPERUSER` For more information about RDS_SUPERUSER, see [Understanding PostgreSQL roles and permissions](./Appendix.PostgreSQL.CommonDBATasks.Roles.html).  
  
![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Controlling access with security groups

Service-linked roles

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

