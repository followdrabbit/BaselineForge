# Processed Content from URL: {'REFERENCE': 'https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/gs-security-and-authentation-autonomous-database.html'}

###  [ Oracle Cloud Infrastructure Documentation ](/iaas/Content/home.htm)

* * *

All Pages

Skip to main content

## Security and Authentication in Oracle Autonomous Database

Oracle Autonomous Database stores all data in encrypted format in the
database. Only authenticated users and applications can access the data when
they connect to the database.

**Note**  
  
Oracle Autonomous Database supports the standard security features of the
Oracle Database including privilege analysis, network encryption, centrally
managed users, secure application roles, transparent sensitive data
protection, and others. Additionally, Oracle Autonomous Database adds Label
Security, Database Vault, Data Safe, and other advanced security features at
no additional cost.

  * [Configuration Management](gs-security-and-authentation-autonomous-database.html#GUID-A7891293-C595-4E15-BD27-AD52F36EB741)  
Oracle Autonomous Database provides standard, hardened security configurations
that reduce the time and money managing configurations across your databases.

  * [Data Encryption](gs-security-and-authentation-autonomous-database.html#GUID-383C11FC-9D82-4A12-9FC7-1F0D7931ADC5)  
Oracle Autonomous Database uses always-on encryption that protects data at
rest and in transit. Data at rest and in motion is encrypted by default.
Encryption cannot be turned off.

  * [Data Access Control](gs-security-and-authentation-autonomous-database.html#GUID-9B98BC3F-AD86-4098-925C-6F141D719BAE)  
Securing access to your Oracle Autonomous Database and your data uses several
different kinds of access control:

  * [Auditing Overview on Autonomous Database](gs-security-and-authentation-autonomous-database.html#GUID-C1833338-A9D9-4F47-A99F-B7D5E498DF4B)  
Oracle Autonomous Database provides robust auditing capabilities that enable
you to track who did what on the service and on specific databases.
Comprehensive log data allows you to audit and monitor actions on your
resources, which helps you to meet your audit requirements while reducing
security and operational risk.

  * [Assessing the Security of Your Database and its Data](gs-security-and-authentation-autonomous-database.html#GUID-290D60CB-FAED-452F-AEC8-3CB58D835DDC)  
Oracle Autonomous Database integrates with Oracle Data Safe to help you assess
and secure your databases.

  * [Regulatory Compliance Certification](gs-security-and-authentation-autonomous-database.html#GUID-D620A69C-9B4A-433C-8E30-BAC7167CF241)  
Oracle Autonomous Database meets a broad set of international and industry-
specific compliance standards.

**Parent topic:** [Security](security-top-autonomous.html#GUID-
DFCC2932-AB47-41E1-ADB6-4BD1F992CF48 "Autonomous Database stores all data with
inbuilt security. Only authenticated users and applications can access the
data when they connect to the database.")

### Configuration Management

Oracle Autonomous Database provides standard, hardened security configurations
that reduce the time and money managing configurations across your databases.

Security patches and updates are done automatically, so you don't spend time,
money, or attention to keeping security up to date. These capabilities protect
your databases and data from costly and potentially disastrous security
vulnerabilities and breaches.

**Parent topic:** [Security and Authentication in Oracle Autonomous
Database](gs-security-and-authentation-autonomous-
database.html#GUID-B26111FC-311F-4A80-96F7-E3608BEC25C7 "Oracle Autonomous
Database stores all data in encrypted format in the database. Only
authenticated users and applications can access the data when they connect to
the database.")

### Data Encryption

Oracle Autonomous Database uses always-on encryption that protects data at
rest and in transit. Data at rest and in motion is encrypted by default.
Encryption cannot be turned off.

Encryption of Data at Rest

Data at rest is encrypted using TDE (Transparent Data Encryption), a
cryptographic solution that protects the processing, transmission, and storage
of data. Using AES256 tablespace encryption, each database has its own
encryption key, and any backups have their own different encryption keys.

By default, Oracle Autonomous Database creates and manages all the master
encryption keys used to protect your data, storing them in a secure PKCS 12
keystore on the same systems where the database resides. If your company
security policies require, Oracle Autonomous Database can instead use keys you
create and manage in the Oracle Cloud Infrastructure Vault service. For more
information, see [About Master Encryption Key Management on Autonomous
Database](about-user-managed-key.html#GUID-F7FE0CAD-
FE11-46DF-A14C-4A1E56DC5777 "Autonomous Database provides two options for
Transparent Data Encryption \(TDE\) to encrypt your database: Oracle-managed
encryption keys and Customer-managed encryption keys.").

Additionally, customer-managed keys can be rotated when needed in order to
meet your organization's security policies.

**Note** : When you clone a database, the new database gets its own new set of
encryption keys.

Encryption of Data in Transit

Clients (applications and tools) connect to Oracle Autonomous Database using
supported protocols including SQL*Net, JDBC, and ODBC.

**TCPS (Secure TCP) database connection services** use the industry-standard
TLS 1.2 (Transport Layer Security) protocol for connections and symmetric-key
data encryption.

  * With mTLS connections, Oracle Autonomous Database users download a connection wallet that contains all necessary files for a client to connect using TCPS. Distribute this wallet only to those users who need and are permitted to have database access. The client-side configuration uses information in the wallet to perform symmetric-key data encryption. 

  * Autonomous Database by default supports Mutual TLS (mTLS) connections. You have the option to configure an Autonomous Database instance to allow both mTLS and TLS connections. Using TLS connections, some clients, such as JDBC Thin Driver clients, do not need to download a wallet if you use a TLS connection string and TLS is enabled for the Autonomous Database instance. 

See [Secure Connections to Autonomous Database](connect-
introduction.html#GUID-C0F28C43-723B-4E23-84A4-1A1490C80CF6 "Connections to
Autonomous Database are made either over the public Internet, optionally with
Access Control Rules \(ACLs\) defined, or using a private endpoint inside a
Virtual Cloud Network \(VCN\) in your tenancy.") for more information.

**Parent topic:** [Security and Authentication in Oracle Autonomous
Database](gs-security-and-authentation-autonomous-
database.html#GUID-B26111FC-311F-4A80-96F7-E3608BEC25C7 "Oracle Autonomous
Database stores all data in encrypted format in the database. Only
authenticated users and applications can access the data when they connect to
the database.")

### Data Access Control

Securing access to your Oracle Autonomous Database and your data uses several
different kinds of access control:

  * [Client Access Control](gs-security-and-authentation-autonomous-database.html#GUID-54787674-8354-4183-8642-066C5C762511)  
Client access control for an Autonomous Database instance is enforced by
network access control policies, through client connection protocols, and by
the access rights of the database user the client uses to connect.

  * [Database User Access Control](gs-security-and-authentation-autonomous-database.html#GUID-177B2419-54FF-48EA-B9D3-A6E1CE727352)  
The Oracle Autonomous Database is configured with an administrative account,
ADMIN, that is used to create and manage other database accounts. Oracle
Autonomous Database provides a robust set of features and controls including
system and object privileges and roles. User profiles allows you to customize
password policies to define and implement a secure database user access
strategy.

  * [Oracle Cloud User Access Control](gs-security-and-authentation-autonomous-database.html#GUID-03C022AE-59C0-462F-8B06-A61FEDF6B069)  
You use Identity and Access Management (IAM) services to control the
privileges of your Oracle Cloud users by specifying the actions those users
can perform on your Oracle Autonomous Database.

  * [Authorized Access on Autonomous Database](gs-security-and-authentation-autonomous-database.html#GUID-382E5312-2276-4AE0-B92C-08D908720D24)  
Only authorized users are allowed access to an Autonomous Database instance.

  * [Autonomous Database Fully Managed Service](gs-security-and-authentation-autonomous-database.html#GUID-2F61AAF7-F038-4896-AEF3-58E59C3E395E)  
Autonomous Database is a fully managed service and Oracle uses its own Oracle
Cloud Infrastructure tenancies to run the Autonomous Database service.

**Parent topic:** [Security and Authentication in Oracle Autonomous
Database](gs-security-and-authentation-autonomous-
database.html#GUID-B26111FC-311F-4A80-96F7-E3608BEC25C7 "Oracle Autonomous
Database stores all data in encrypted format in the database. Only
authenticated users and applications can access the data when they connect to
the database.")

#### Client Access Control

Client access control for an Autonomous Database instance is enforced by
network access control policies, through client connection protocols, and by
the access rights of the database user the client uses to connect.

Network Access Control

You define network access control when you set up and configure your Oracle
Autonomous Database. There are two options to consider.

  * **Private Endpoints and Security Lists:** This is the recommended option. Create your Oracle Autonomous Database in your virtual cloud network (VCN) using private endpoints. You control access to your database using security lists and network security groups allowing you to specify who can create connections to your database. 

For detailed information about creating these resources, see [Configure
Network Access with Private Endpoints](private-endpoints-
autonomous.html#GUID-60FE6BFD-B05C-4C97-8B4A-83285F31D575 "You can specify
that Autonomous Database uses a private endpoint inside your Virtual Cloud
Network \(VCN\) in your tenancy. You can configure a private endpoint during
provisioning or cloning your Autonomous Database, or you can switch to using a
private endpoint in an existing database that uses a public endpoint. This
allows you to keep all traffic to and from your database off of the public
internet.").

  * **Public Endpoints and Access Control Lists:** Create your Oracle Autonomous Database using public endpoints allowing access from any client with client credentials. You control access to your database using network access control lists (ACLs) allowing you to specify IP addresses, CIDR blocks, or VCNs that can connect to your database. Public IPs are easier to discover and attack, and Private Endpoints are recommended where possible. 

For detailed information about setting up an ACL, see [Configure Access
Control Lists for an Existing Autonomous Database Instance](access-control-
rules-autonomous.html#GUID-B6389402-3F4D-45A2-A4DE-EAF1B31D8E50 "You can
control and restrict access to your Autonomous Database by specifying network
access control lists \(ACLs\). On an existing Autonomous Database instance
with a public endpoint you can add, change, or remove ACLs.").

Client Connection Control

Clients connect through a TCPS (Secure TCP) database connection using standard
TLS 1.2 to secure the connection. Oracle Autonomous Database uses self-signed
certificates. You can rotate the self-signed certificates from the Oracle
Cloud Infrastructure console to meet your organization's security compliance
needs. See [Rotate Wallets with Immediate Rotation](wallet-
rotate.html#GUID-F0995A6A-78BD-4C9D-9A34-B970BD152CAD "Immediate wallet
rotation lets you invalidate existing client certification keys for an
Autonomous Database instance or for all Autonomous Database instances that a
cloud account owns in a region.").

The access the client has to the database is restricted by the access rights
of the database user the client uses to connect.

**Parent topic:** [Data Access Control](gs-security-and-authentation-
autonomous-database.html#GUID-9B98BC3F-AD86-4098-925C-6F141D719BAE "Securing
access to your Oracle Autonomous Database and your data uses several different
kinds of access control:")

#### Database User Access Control

The Oracle Autonomous Database is configured with an administrative account,
ADMIN, that is used to create and manage other database accounts. Oracle
Autonomous Database provides a robust set of features and controls including
system and object privileges and roles. User profiles allows you to customize
password policies to define and implement a secure database user access
strategy.

For basic information about standard user management, see [User
Accounts](/pls/topic/lookup?ctx=en/cloud/paas/autonomous-
database/serverless/adbsb&id=CNCPT-GUID-CE700CE1-BF1B-48C0-A905-50CEE055C4BC)
in Oracle Database Concepts. For detailed information and guidance, see
[Managing Security for Oracle Database
Users](/pls/topic/lookup?ctx=en/cloud/paas/autonomous-
database/serverless/adbsb&id=DBSEG-GUID-8C779885-01F2-48E0-9612-E33508885B19)
in Oracle Database Security Guide.

If your database user access strategy demands more controls than are provided
by standard user management, you can configure your Oracle Autonomous Database
to use Database Vault to meet more rigorous requirements.

Using Microsoft Active Directory to Manage Database Users

If you use Microsoft Active Directory as a user repository, you can configure
your database to authenticate and authorize Microsoft Active Directory users.
This integration enables you to consolidate your user repository while still
implementing a rigorous database user access strategy, regardless of whether
you use standard user management or Database Vault.

For more information about integrating Microsoft Active Directory with your
databases, see [Use Microsoft Active Directory with Autonomous
Database](manage-users-active-
directory.html#GUID-11754210-CCD7-48B3-BC16-0E537A27217C "You can configure
Autonomous Database to authenticate and authorize Microsoft Active Directory
users.").

Database Vault

Oracle Database Vault comes preconfigured and ready to use. You can use its
powerful security controls to restrict access to application data by
privileged database users, reducing the risk threats, and addressing common
compliance requirements.

You configure controls to block privileged account access to application data
and control sensitive operations inside the database. You configure trusted
paths to add additional security controls to authorized data access, database
objects, and database commands. Database Vault secures existing database
environments transparently, eliminating costly and time consuming application
changes.

Before using Database Vault, be sure to review [Use Oracle Database Vault with
Autonomous Database](autonomous-database-
vault.html#GUID-70F233AF-458F-44B7-9418-F9AF70CFDD15 "Oracle Database Vault
implements powerful security controls for your database. These unique security
controls restrict access to application data by privileged database users,
reducing the risk of insider and outside threats and addressing common
compliance requirements.") to gain an understanding of the impact of
configuring and enabling Database Vault.

For detailed information on implementing Database Vault features, refer to
[Oracle Database Vault Administratorâs
Guide](/pls/topic/lookup?ctx=en/cloud/paas/autonomous-
database/serverless/adbsb&id=DVADM-GUID-0C8AF1B2-6CE9-4408-BFB3-7B2C7F9E7284).

**Parent topic:** [Data Access Control](gs-security-and-authentation-
autonomous-database.html#GUID-9B98BC3F-AD86-4098-925C-6F141D719BAE "Securing
access to your Oracle Autonomous Database and your data uses several different
kinds of access control:")

#### Oracle Cloud User Access Control

You use Identity and Access Management (IAM) services to control the
privileges of your Oracle Cloud users by specifying the actions those users
can perform on your Oracle Autonomous Database.

The IAM service provides several kinds of components to help you define and
implement a secure cloud user access strategy:

  * **Compartment** : A collection of related resources. Compartments are a fundamental component of Oracle Cloud Infrastructure for organizing and isolating your cloud resources. 

  * **Group** : A collection of users who all need the same type of access to a particular set of resources or compartment. 

  * **Dynamic Group** : A special type of group that contains resources that match rules that you define. Thus, the membership can change dynamically as matching resources are created or deleted. 

  * **Policy** : A group of statements that specify who can access which resources, and how. Access is granted at the group and compartment level, which means you write a policy statement that gives a specific group a specific type of access to a specific type of resource within a specific compartment. 

Of these, the policy is the primary tool you use to control access because it
provides the "Who", "How", "What" and "Where" of a single access constraint. A
policy statement has this format:

The format of a policy statement is:

    
    
    Allow 
      group _< group-name>_ 
      to _< control-verb>_ 
      _< resource-type>_ 
      in compartment _< compartment-name>_

  * **`group <group-name>`** specifies the "Who" by providing the name of an existing IAM group. 

  * **`to <control-verb>`** specifies the "How" using one of these predefined control verbs: 

    * **`inspect`** : the ability to list resources of the given type, without access to any confidential information or user-specified metadata that may be part of that resource. 
    * **`read`** : `inspect` plus the ability to get user-specified metadata and the actual resource itself. 
    * **`use`** : `read` plus the ability to work with existing resources, but not to create or delete them. Additionally, "work with" means different operations for different resource types. 
    * **`manage`** : all permissions for the resource type, including creation and deletion. 
  * **`< resource-type>`** specifies the "What" using a predefined resource-type. The resource-type values for infrastructure resources are: 

    * **`autonomous-databases`**
    * **`autonomous-backups`**

You may create policy statements that refer to the **`tag-namespaces`**
resource-type value if tagging is used in your tenancy.

  * **`in compartment <compartment-name>`** specifies the "Where" by providing the name of an existing IAM compartment. 

For information about how the IAM service and its components work and how to
use them, see [Overview of Oracle Cloud Infrastructure Identity and Access
Management](/iaas/Content/Identity/Concepts/overview.htm). For quick answers
to common questions about IAM, see the [Identity and Access Management
FAQ](https://www.oracle.com/cloud/security/cloud-services/identity-access-
cloud-faq.html).

**Parent topic:** [Data Access Control](gs-security-and-authentation-
autonomous-database.html#GUID-9B98BC3F-AD86-4098-925C-6F141D719BAE "Securing
access to your Oracle Autonomous Database and your data uses several different
kinds of access control:")

#### Authorized Access on Autonomous Database

Only authorized users are allowed access to an Autonomous Database instance.

Oracle Cloud Operators do not have authorization to access your Autonomous
Database. When access to your database is required to troubleshoot or mitigate
an issue, you can allow a Cloud Operator to access a database for a limited
time.

You allow a Cloud Operator to access the database by running the procedure
`DBMS_CLOUD_ADMIN.ENABLE_OPERATOR_ACCESS`. This means if you file a service
request with [Oracle Cloud Support](https://support.oracle.com/) or by
contacting your support representative and Oracle Cloud Operators need to
access your database, you must also enable operator access by running
`DBMS_CLOUD_ADMIN.ENABLE_OPERATOR_ACCESS`.

Each database access by Oracle Cloud Operators is logged with a request ID and
reason.

See [Manage Oracle Cloud Operator Access](autonomous-operator-
access.html#GUID-B34B2D28-EE71-4738-9EBD-263BF77C628D "Describes how to grant
temporary access to your database for an Oracle Cloud Operator.") and [View
Oracle Cloud Infrastructure Operations Actions](view-operator-
access.html#GUID-B26E4486-CD00-4A87-9E08-88027D97101C "The DBA_OPERATOR_ACCESS
view stores information on the actions that Oracle Cloud Infrastructure cloud
operations performs on your Autonomous Database.") for more information.

**Parent topic:** [Data Access Control](gs-security-and-authentation-
autonomous-database.html#GUID-9B98BC3F-AD86-4098-925C-6F141D719BAE "Securing
access to your Oracle Autonomous Database and your data uses several different
kinds of access control:")

#### Autonomous Database Fully Managed Service

Autonomous Database is a fully managed service and Oracle uses its own Oracle
Cloud Infrastructure tenancies to run the Autonomous Database service.

Oracle Cloud Operators do not have access to customer tenancies and cloud
operators cannot access the network.

**Parent topic:** [Data Access Control](gs-security-and-authentation-
autonomous-database.html#GUID-9B98BC3F-AD86-4098-925C-6F141D719BAE "Securing
access to your Oracle Autonomous Database and your data uses several different
kinds of access control:")

### Auditing Overview on Autonomous Database

Oracle Autonomous Database provides robust auditing capabilities that enable
you to track who did what on the service and on specific databases.
Comprehensive log data allows you to audit and monitor actions on your
resources, which helps you to meet your audit requirements while reducing
security and operational risk.

  * [Auditing Service Level Activities](gs-security-and-authentation-autonomous-database.html#GUID-7A38B9A7-ACF7-4DD6-867A-8602D899D358)  
All actions Oracle Cloud users perform on the resources that make up your
deployment of Oracle Autonomous Database are logged by the Audit service,
regardless of the interface used: the Oracle Cloud Infrastructure Console,
REST API, Command Line Interface (CLI), Software Development Kits (SDK) and so
on.

  * [Auditing Database Activities](gs-security-and-authentation-autonomous-database.html#GUID-1A917C69-EEAA-4220-AEF2-7376A9ED1268)  
Oracle Autonomous Database configures the autonomous databases you create to
use the unified auditing feature of Oracle Database.

**Parent topic:** [Security and Authentication in Oracle Autonomous
Database](gs-security-and-authentation-autonomous-
database.html#GUID-B26111FC-311F-4A80-96F7-E3608BEC25C7 "Oracle Autonomous
Database stores all data in encrypted format in the database. Only
authenticated users and applications can access the data when they connect to
the database.")

#### Auditing Service Level Activities

All actions Oracle Cloud users perform on the resources that make up your
deployment of Oracle Autonomous Database are logged by the Audit service,
regardless of the interface used: the Oracle Cloud Infrastructure Console,
REST API, Command Line Interface (CLI), Software Development Kits (SDK) and so
on.

You can use the Audit service to perform diagnostics, track resource usage,
monitor compliance, and collect security-related events. For more information
about the Audit service, see [Overview of
Audit](/iaas/Content/Audit/Concepts/auditoverview.htm) in Oracle Cloud
Infrastructure Documentation.

Additionally, when users perform operations on your Oracle Autonomous
Database, the database publishes _events_ to the Oracle Cloud Events service.
The Oracle Cloud Events service allows you to create rules to capture these
events and perform actions.

For more information about how the Events service works and how to set up the
rules and actions it uses, see [ Overview of
Events](/iaas/Content/Events/Concepts/eventsoverview.htm). For listings of the
Oracle Autonomous Database operations that generate events, see [Autonomous
Database Event
Types](/iaas/Content/Events/Reference/eventsproducers.htm#auto_database).

**Parent topic:** [Auditing Overview on Autonomous Database](gs-security-and-
authentation-autonomous-
database.html#GUID-C1833338-A9D9-4F47-A99F-B7D5E498DF4B "Oracle Autonomous
Database provides robust auditing capabilities that enable you to track who
did what on the service and on specific databases. Comprehensive log data
allows you to audit and monitor actions on your resources, which helps you to
meet your audit requirements while reducing security and operational risk.")

#### Auditing Database Activities

Oracle Autonomous Database configures the autonomous databases you create to
use the unified auditing feature of Oracle Database.

This feature captures audit records from the following sources and gathers
them in a single audit trail in a uniform format:

  * Audit records (including `SYS` audit records) from unified audit policies and `AUDIT` settings 
  * Fine-grained audit records from the `DBMS_FGA` PL/SQL package 
  * Oracle Database Real Application Security audit records
  * Oracle Recovery Manager audit records
  * Oracle Database Vault audit records
  * Oracle Label Security audit records
  * Oracle Data Mining records
  * Oracle Data Pump
  * Oracle SQL*Loader Direct Load

Audit information is retained for up to 14 days, after which it is
automatically purged. To retain audit information for longer, and to easily
analyze and report on database activity, use Oracle Data Safe (included with
your Oracle Autonomous Database subscription).

See [About Auditing Autonomous Database](adb-
audit.html#GUID-A3B0680B-5BEC-44CF-9D9B-E1D95C5C91EB "Autonomous Database
provides auditing to track, monitor, and record database actions. Auditing can
help you detect security risks and improve regulatory compliance for your
database.") for more information.

**Parent topic:** [Auditing Overview on Autonomous Database](gs-security-and-
authentation-autonomous-
database.html#GUID-C1833338-A9D9-4F47-A99F-B7D5E498DF4B "Oracle Autonomous
Database provides robust auditing capabilities that enable you to track who
did what on the service and on specific databases. Comprehensive log data
allows you to audit and monitor actions on your resources, which helps you to
meet your audit requirements while reducing security and operational risk.")

### Assessing the Security of Your Database and its Data

Oracle Autonomous Database integrates with Oracle Data Safe to help you assess
and secure your databases.

Oracle Data Safe helps you understand the sensitivity of your data, evaluate
risks to data, mask sensitive data, implement and monitor security controls,
assess user security, monitor user activity, and address data security
compliance requirements in your databases.

You use Oracle Data Safe to identify and protect sensitive and regulated data
your Oracle Autonomous Database by registering your database with Data Safe.
Then, you use the Data Safe console directly from the Details page of your
database.

For more information about using Data Safe, see [Use Oracle Data Safe
Features](autonomous-data-safe.html#GUID-2D36B6A7-BA83-4F75-A46C-51E419D4D3AA
"After you register Autonomous Database with Oracle Data Safe you can use the
Data Safe features.").

**Parent topic:** [Security and Authentication in Oracle Autonomous
Database](gs-security-and-authentation-autonomous-
database.html#GUID-B26111FC-311F-4A80-96F7-E3608BEC25C7 "Oracle Autonomous
Database stores all data in encrypted format in the database. Only
authenticated users and applications can access the data when they connect to
the database.")

### Regulatory Compliance Certification

Oracle Autonomous Database meets a broad set of international and industry-
specific compliance standards.

Certification | Description  
---|---  
C5 |  The Cloud Computing Compliance Controls Catalog (C5)  
CSA STAR |  The Cloud Security Alliance (CSA) Security Trust, Assurance and Risk (STAR)  
Cyber Essentials (UK)  Cyber Essentials Plus (UK) |  Oracle Cloud Infrastructure has achieved Cyber Essentials and Cyber Essentials Plus certification in these regions: 

  * UK Gov South (London)
  * UK Gov West (Newport)

  
DESC (UAE) |  Dubai Electronic Security Center CSP Security Standard  
DoD IL4/IL5 |  DISA Impact Level 5 authorization in these regions:

  * US DoD East (Ashburn)
  * US DoD North (Chicago)
  * US DoD West (Phoenix)

  
ENS High (Spain) |  The Esquema Nacional de Seguridad with the level of accreditation High.  
FedRAMP High |  Federal Risk and Authorization Management Program (U.S. Government Regions only)  
FSI (S. Korea) |  The Financial Security Institute   
HDS |  The French Public Health Code requires healthcare organizations that control, process, or store health or medical data to use infrastructure, hosting, and platform service providers that are HÃ©bergeur de DonnÃ©es de SantÃ© (HDS) accredited and certified  
HIPAA |  Health Insurance Portability and Accountability Act  
HITRUST |  The Health Information Trust Alliance  
IRAP (Australia) |  The Infosec Registered Assessors Program. Sydney and Melbourne regions  
ISMS (S. Korea) |  The Information Security Management System  
ISO/IEC 27001:2013 |  International Organization for Standardization 27001  
ISO/IEC 27017:2015 |  Code of Practice for Information Security Controls Based on ISO/IEC 27002 for Cloud Services  
ISO/IEC 27018:2014 |  Code of Practice for Protection of Personally Identifiable Information (PII) In Public Clouds Acting as PII Processors  
MeitY (India) |  The Ministry of Electronics and Information Technology  
MTCS (Singapore) |  Multi-Tier Cloud Service (MTCS) Level 3  
PASF (UK OC4) |  Police Assured Secure Facilities (PASF) in these regions:

  * UK Gov South (London)
  * UK Gov West (Newport)

  
PCI DSS |  Payment Card Industry Data Security Standard is a set of requirements intended to ensure that all companies that process, store, or transmit credit card information maintain a secure environment  
SOC 1 |  System and Organization Controls 1  
SOC 2 |  System and Organization Controls 2  
  
For more information and a complete list of certifications, see [Oracle Cloud
Compliance](https://www.oracle.com/cloud/cloud-infrastructure-compliance/).

**Parent topic:** [Security and Authentication in Oracle Autonomous
Database](gs-security-and-authentation-autonomous-
database.html#GUID-B26111FC-311F-4A80-96F7-E3608BEC25C7 "Oracle Autonomous
Database stores all data in encrypted format in the database. Only
authenticated users and applications can access the data when they connect to
the database.")

  * Security and Authentication in Oracle Autonomous Database 
  * Configuration Management 
  * Data Encryption 
  * Data Access Control 
  * Auditing Overview on Autonomous Database 
  * Assessing the Security of Your Database and its Data 
  * Regulatory Compliance Certification 

  * Copyright Â© 2025, Oracle and/or its affiliates.
  * [About Oracle](https://www.oracle.com/corporate/index.html)
  * [Contact Us](https://www.oracle.com/corporate/contact/index.html)
  * [Legal Notices](/iaas/Content/legalnotices.htm)
  * [Terms of Use & Privacy](https://www.oracle.com/legal/privacy/)
  * [Document Conventions](/iaas/Content/General/Reference/docconventions.htm)
  * 

