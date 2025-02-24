```json
[
  {
    "Description": "Ensure the master user account for a new DB cluster is not used directly by applications. A separate database user with minimal privileges should be created instead.",
    "Reference": "Section titled 'Master user account privileges' in the documentation - URL: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.MasterAccounts.html",
    "Observations": "This practice is a security best practice to reduce potential attack vectors by limiting privileges."
  },
  {
    "Description": "Restore permissions for the master user by modifying the DB cluster and setting a new master user password if permissions are accidentally deleted.",
    "Reference": "Section titled 'Master user account privileges' - Note under the table - URL: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.MasterAccounts.html",
    "Observations": "Changing the master user password restores default permissions."
  },
  {
    "Description": "The Aurora MySQL master user must have specific system privileges based on the version, such as ALTER, CREATE USER, DELETE, etc., and may include 'rds_superuser_role' for version 3.",
    "Reference": "Table under 'Master user account privileges', specifying privileges for Aurora MySQL - URL: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.MasterAccounts.html",
    "Observations": "Refer to specific privileges based on the database engine and version."
  },
  {
    "Description": "The Aurora PostgreSQL master user must have specific system privileges such as LOGIN, CREATEDB, CREATEROLE, and the 'RDS_SUPERUSER' role.",
    "Reference": "Table under 'Master user account privileges', specifying privileges for Aurora PostgreSQL - URL: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.MasterAccounts.html",
    "Observations": "RDS_SUPERUSER provides comprehensive privileges similar to the PostgreSQL superuser."
  }
]
```
