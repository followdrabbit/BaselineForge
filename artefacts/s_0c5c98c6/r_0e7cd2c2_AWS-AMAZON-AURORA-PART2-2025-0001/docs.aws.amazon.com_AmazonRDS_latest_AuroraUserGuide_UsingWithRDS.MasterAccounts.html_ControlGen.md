```json
[
  {
    "Title": "Enforce Restricted Use of Master User in AWS RDS",
    "Description": "Ensure that the master user account for any Amazon Aurora DB cluster is not used by applications directly. Applications should use a separate database user with only the necessary privileges to perform their operations.",
    "Applicability": "All Amazon Aurora DB clusters",
    "Security Risk": "Using the master user directly increases the attack surface and potential impact from compromised applications, as it has extensive privileges.",
    "Default Behavior / Limitations": "AWS allows the use of master credentials by default; users must implement security best practices manually.",
    "Automation": "Manual validation required. Currently, AWS offers no automated method to enforce the non-use of the master user by applications. Periodic audits and application reviews are recommended.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.MasterAccounts.html"
    ]
  },
  {
    "Title": "Automate Restoration of Master User Permissions in Amazon Aurora",
    "Description": "If permissions for the master user account are removed, restore them by modifying the DB cluster and updating the master user password. This operation resets the master user's privileges to the default set.",
    "Applicability": "All Amazon Aurora DB clusters",
    "Security Risk": "Without the default permissions, the master user may be unable to perform necessary administrative actions, leading to operational disruptions.",
    "Default Behavior / Limitations": "This is a manual operation. AWS management console or CLI is required to change the master password and reset permissions.",
    "Automation": "Manual process; requires user intervention to modify the DB cluster and set a new password. Potential automation could be implemented using custom AWS Lambda scripts triggered by monitoring.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.MasterAccounts.html"
    ]
  },
  {
    "Title": "Verify System Privileges for Aurora MySQL Master User",
    "Description": "The master user in Aurora MySQL should have specific system privileges, including ALTER, CREATE USER, DELETE, based on engine version, and potentially 'rds_superuser_role' for version 3.",
    "Applicability": "Amazon Aurora MySQL DB clusters",
    "Security Risk": "Incorrect privileges may prevent necessary administrative actions or increase security risks if excessive privileges are granted.",
    "Default Behavior / Limitations": "AWS provides default master user privileges; however, adjustments can be made post-creation.",
    "Automation": "Can be monitored using AWS Config and custom rules to audit existing privileges against a defined baseline.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.MasterAccounts.html"
    ]
  },
  {
    "Title": "Verify System Privileges for Aurora PostgreSQL Master User",
    "Description": "The master user in Aurora PostgreSQL should have specific system privileges such as LOGIN, CREATEDB, CREATEROLE, and the 'RDS_SUPERUSER' role, which provides comprehensive database privileges.",
    "Applicability": "Amazon Aurora PostgreSQL DB clusters",
    "Security Risk": "Lack of necessary privileges may lead to inadequate database administration capabilities or security vulnerabilities if excessive privileges are granted.",
    "Default Behavior / Limitations": "Post-creation privilege modifications are possible. Default privileges are assigned upon DB cluster creation.",
    "Automation": "Can be verified automatically with AWS Config rules tailored to audit the privileges of the master user against predefined standards.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.MasterAccounts.html"
    ]
  }
]
```