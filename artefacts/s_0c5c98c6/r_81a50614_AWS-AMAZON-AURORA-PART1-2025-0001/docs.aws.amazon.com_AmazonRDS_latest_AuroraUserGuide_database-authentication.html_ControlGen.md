```json
[
  {
    "Title": "Assign 'rds_iam' Role for IAM Database Authentication",
    "Description": "For PostgreSQL databases in Amazon Aurora, assign the 'rds_iam' role to users to enable IAM database authentication, allowing users to connect using IAM credentials.",
    "Applicability": "All Aurora PostgreSQL databases",
    "Security Risk": "Without IAM authentication, databases rely on static credentials, increasing the risk of credential leakage and unauthorized access.",
    "Default Behavior / Limitations": "This feature must be explicitly enabled; not enabled by default.",
    "Automation": "Can be enforced using AWS IAM roles and PostgreSQL role assignments via AWS CLI or RDS APIs.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/database-authentication.html"
    ]
  },
  {
    "Title": "Assign 'rds_ad' Role for Kerberos Authentication",
    "Description": "For PostgreSQL databases in Amazon Aurora, assign the 'rds_ad' role to users to integrate with AWS Directory Service for Kerberos authentication, enabling centralized user management.",
    "Applicability": "All Aurora PostgreSQL databases with AWS Directory Service",
    "Security Risk": "Without Kerberos authentication, identity management lacks centralization, and SSO capabilities may not be implemented, posing identity management challenges.",
    "Default Behavior / Limitations": "Requires a trust relationship with AWS Directory Service; not enabled by default.",
    "Automation": "Can be established via AWS Directory Service setup and PostgreSQL role assignments.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/database-authentication.html"
    ]
  },
  {
    "Title": "Prevent Assignment of Both 'rds_iam' and 'rds_ad' Roles",
    "Description": "Ensure that PostgreSQL users in Amazon Aurora are not assigned both 'rds_iam' and 'rds_ad' roles to avoid authentication conflicts.",
    "Applicability": "All Aurora PostgreSQL databases using IAM or Kerberos authentication",
    "Security Risk": "Assigning both roles could lead to unpredictable authentication behavior, risking unauthorized access.",
    "Default Behavior / Limitations": "Manual oversight is required as no default checks prevent dual role assignment.",
    "Automation": "Requires manual validation during user role assignment.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/database-authentication.html"
    ]
  },
  {
    "Title": "Integrate AWS Secrets Manager for Database Password Management",
    "Description": "Use AWS Secrets Manager to manage and rotate database passwords securely, avoiding the use of plain text passwords in configuration files.",
    "Applicability": "All Aurora databases",
    "Security Risk": "Static credentials in configuration files increase exposure to credential leaks and unauthorized access.",
    "Default Behavior / Limitations": "Secrets Manager integration must be configured; not enabled by default.",
    "Automation": "Can be automated using AWS Secrets Manager and RDS integration capabilities via Lambda functions.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/database-authentication.html"
    ]
  },
  {
    "Title": "Use IAM Authentication Tokens for Database Connection",
    "Description": "Implement IAM database authentication in Amazon Aurora to use IAM tokens for database connections, reducing the overhead of password management.",
    "Applicability": "Aurora databases supporting IAM authentication",
    "Security Risk": "Managing database passwords manually increases the risk of credential exposure and unauthorized access.",
    "Default Behavior / Limitations": "Availability depends on the DB engine; must be configured.",
    "Automation": "Automated via IAM policy configurations and appropriate RDS instance settings.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/database-authentication.html"
    ]
  },
  {
    "Title": "Configure Kerberos Authentication with AWS Directory Service",
    "Description": "Utilize AWS Directory Service to set up Kerberos authentication for Aurora databases, enabling single sign-on (SSO) capabilities.",
    "Applicability": "Aurora databases with AWS Directory integration",
    "Security Risk": "Without Kerberos SSO, separate credentials are required for each service, complicating identity management and increasing potential attack surfaces.",
    "Default Behavior / Limitations": "Requires configuration with AWS Directory Service.",
    "Automation": "Can be automated via AWS Directory Service setup and service linkage settings in Aurora.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/database-authentication.html"
    ]
  },
  {
    "Title": "Avoid Using the Master User for Applications",
    "Description": "Follow the best practice of not using the master user directly in applications; instead, create users with minimal privileges necessary for application functionality.",
    "Applicability": "All Aurora databases",
    "Security Risk": "Use of the master user for applications poses a high security risk if credentials are compromised, allowing full access to the database.",
    "Default Behavior / Limitations": "AWS provides no automated default mechanism to enforce this practice.",
    "Automation": "Requires manual validation and establishment of a least privilege model within the database.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/database-authentication.html"
    ]
  }
]
```