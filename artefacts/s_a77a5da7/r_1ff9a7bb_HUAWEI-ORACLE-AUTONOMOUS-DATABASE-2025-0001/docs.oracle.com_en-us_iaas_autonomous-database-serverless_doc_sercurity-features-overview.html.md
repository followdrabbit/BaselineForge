# Processed Content from URL: {'REFERENCE': 'https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/sercurity-features-overview.html'}

###  [ Oracle Cloud Infrastructure Documentation ](/iaas/Content/home.htm)

* * *

All Pages

Skip to main content

## Security Features Overview

Describes some of the robust security features that Autonomous Database
provides.

Autonomous Database security features include:

  * Autonomous Database meets a broad set of international and industry-specific compliance standards, and as part of Oracle Cloud Infrastructure Autonomous Database has achieved attestations for the common compliance frameworks providing an independent assessment of the service's security, privacy, and compliance controls. 

See [Regulatory Compliance Certification](gs-security-and-authentation-
autonomous-database.html#GUID-D620A69C-9B4A-433C-8E30-BAC7167CF241 "Oracle
Autonomous Database meets a broad set of international and industry-specific
compliance standards.") for more information.

  * Autonomous Database applies security patches automatically as soon as they become available. 

See [Configuration Management](gs-security-and-authentation-autonomous-
database.html#GUID-A7891293-C595-4E15-BD27-AD52F36EB741 "Oracle Autonomous
Database provides standard, hardened security configurations that reduce the
time and money managing configurations across your databases.") for more
information.

  * Autonomous Database is governed by the Oracle Cloud Hosting and Delivery Policies which explain the Oracle Cloud Security Policy. See the Delivery Policies area on [Oracle Contracts](https://www.oracle.com/corporate/contracts/cloud-services) for more information. 

  * Autonomous Database is subject to the Oracle Cloud Security Testing policy, which describes when and how you may conduct certain types of security testing of Oracle Cloud Infrastructure services, including vulnerability and penetration tests and tests involving data scraping tools. 

See [Security Testing Policies on Autonomous Database](autonomous-security-
testing-policies.html#GUID-A953378A-99A1-42BB-AD55-7AED503C454E "Autonomous
Database is subject to the Oracle Cloud Security Testing policy which
describes when and how you may conduct certain types of security testing of
Oracle Cloud Infrastructure services, including vulnerability and penetration
tests, as well as tests involving data scraping tools.") for more information.

  * Autonomous Database provides end-to-end encryption out of the box for the database, backups, and all network communication. All your data, including backups, are encrypted with AES256. You can use Oracle-managed or customer-managed keys to encrypt your data. 

See [Manage Encryption Keys on Autonomous Database](autonomous-encrypt-set-
rotate-keys.html#GUID-0795135D-B057-4DBC-92C9-368AF4C82D0A "Describes how to
use customer-managed encryption keys with Autonomous Database, and if you are
using customer-managed encryption keys, shows how to rotate the keys, switch
to Oracle-managed encryption keys, or view the encryption key history.") for
more information.

  * All network connections are encrypted using TLS 1.2. You can use mutual TLS or one-way TLS connections.

  * Autonomous Database provides several options to control client access to your database. You can use public endpoints with access control lists to specify which clients can connect. You can also use private endpoints to place the database in your VCN and use security lists and network security groups to control access to the database. 

See [Client Access Control](gs-security-and-authentation-autonomous-
database.html#GUID-54787674-8354-4183-8642-066C5C762511 "Client access control
for an Autonomous Database instance is enforced by network access control
policies, through client connection protocols, and by the access rights of the
database user the client uses to connect.") for more information.

  * Autonomous Database provides fully automated immutable backups that cannot be tampered with by the users in your tenancy. 

See [About Backup and Recovery on Autonomous Database](backup-
intro.html#GUID-3BF27FDE-F847-4A86-9C8B-4ED9B0C1D1B2 "Describes Autonomous
Database backup options.") for more information.

  * Autonomous Database provides several user authentication methods. You can use local database user names and passwords or external authentication methods, including: 

    * Oracle Cloud Infrastructure Identity and Access Management

    * Microsoft Active Directory

    * Azure Active Directory

    * Kerberos

See [Manage Users](manage-users.html#GUID-58DABEA3-9A17-4AA4-B32C-C0E301678A9E
"Describes administration tasks for managing database users on Autonomous
Database.") for more information.

  * You can configure Oracle Database Vault to control access to specific schemas from privileged database users such as the ADMIN user.

See [Use Oracle Database Vault with Autonomous Database](autonomous-database-
vault.html#GUID-70F233AF-458F-44B7-9418-F9AF70CFDD15 "Oracle Database Vault
implements powerful security controls for your database. These unique security
controls restrict access to application data by privileged database users,
reducing the risk of insider and outside threats and addressing common
compliance requirements.") for more information,

  * Autonomous Database provides robust auditing capabilities that enable you to track who did what on the service and on specific databases. You can configure database auditing to audit all actions, such as access to specific objects, schema changes, logons by specific users, and much more. 

See [Auditing Overview on Autonomous Database](gs-security-and-authentation-
autonomous-database.html#GUID-C1833338-A9D9-4F47-A99F-B7D5E498DF4B "Oracle
Autonomous Database provides robust auditing capabilities that enable you to
track who did what on the service and on specific databases. Comprehensive log
data allows you to audit and monitor actions on your resources, which helps
you to meet your audit requirements while reducing security and operational
risk.") for more information.

  * Oracle Cloud Operators do not have authorization to access your data or any other information in your database schemas. When access to your database schemas is required to troubleshoot or mitigate an issue, you can allow a cloud operator to access your Autonomous Database schemas for a limited time. 

See [Manage Oracle Cloud Operator Access](autonomous-operator-
access.html#GUID-B34B2D28-EE71-4738-9EBD-263BF77C628D "Describes how to grant
temporary access to your database for an Oracle Cloud Operator.") for more
information.

See [Security and Authentication in Oracle Autonomous Database](gs-security-
and-authentation-autonomous-
database.html#GUID-B26111FC-311F-4A80-96F7-E3608BEC25C7 "Oracle Autonomous
Database stores all data in encrypted format in the database. Only
authenticated users and applications can access the data when they connect to
the database.") for more information.

**Parent topic:** [Security](security-top-autonomous.html#GUID-
DFCC2932-AB47-41E1-ADB6-4BD1F992CF48 "Autonomous Database stores all data with
inbuilt security. Only authenticated users and applications can access the
data when they connect to the database.")

  * Copyright Â© 2025, Oracle and/or its affiliates.
  * [About Oracle](https://www.oracle.com/corporate/index.html)
  * [Contact Us](https://www.oracle.com/corporate/contact/index.html)
  * [Legal Notices](/iaas/Content/legalnotices.htm)
  * [Terms of Use & Privacy](https://www.oracle.com/legal/privacy/)
  * [Document Conventions](/iaas/Content/General/Reference/docconventions.htm)
  * 

