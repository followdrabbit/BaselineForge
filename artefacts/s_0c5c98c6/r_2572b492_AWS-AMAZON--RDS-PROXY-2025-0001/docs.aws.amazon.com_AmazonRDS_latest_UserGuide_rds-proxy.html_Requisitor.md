### Extracted Requirements for Automated Security Controls

#### Metadata
- **Baseline Base ID:** AWS-AMAZON-RDS-PROXY-2025
- **Source URL:** https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html

#### JSON Output

```json
[
  {
    "Description": "A single AWS account is limited to 20 RDS Proxies. An increase can be requested via the AWS Management Console Service Quotas.",
    "Reference": "Section: Quotas and limitations for RDS Proxy - [Documentation URL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)",
    "Observations": "The default limit is 20 proxies; requests for increases require AWS approval."
  },
  {
    "Description": "RDS Proxy must reside in the same VPC as the associated database.",
    "Reference": "Section: Quotas and limitations for RDS Proxy - [Documentation URL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)",
    "Observations": "The proxy can't be publicly accessible, but the database can be."
  },
  {
    "Description": "For RDS DB instances in replication, only the writer DB instance can be associated with a proxy.",
    "Reference": "Section: Quotas and limitations for RDS Proxy - [Documentation URL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)",
    "Observations": "It ensures proper handling of write operations through RDS Proxy."
  },
  {
    "Description": "RDS Proxy cannot be used with VPCs with the tenancy set to 'dedicated'.",
    "Reference": "Section: Quotas and limitations for RDS Proxy - [Documentation URL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)",
    "Observations": "This will prevent deployment in such VPC configurations."
  },
  {
    "Description": "Custom DNS cannot be used with RDS Proxy if SSL hostname validation is enabled.",
    "Reference": "Section: Quotas and limitations for RDS Proxy - [Documentation URL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)",
    "Observations": "SSL hostname validation requires adherence to strict DNS naming."
  },
  {
    "Description": "Proxies associated with RDS for MariaDB, MySQL, SQL Server, and PostgreSQL have engine-specific limitations that must be considered.",
    "Reference": "Sections: Additional limitations for each DB engine - [Documentation URL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)",
    "Observations": "Ensure compatibility with database engine specifics and configurations."
  },
  {
    "Description": "The default endpoint and up to 20 additional endpoints can be configured for each RDS Proxy.",
    "Reference": "Section: Quotas and limitations for RDS Proxy - [Documentation URL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)",
    "Observations": "Endpoints can be managed for application-specific routing and scaling."
  },
  {
    "Description": "RDS Proxy has specific Availability Zone restrictions in certain AWS Regions.",
    "Reference": "Section: Quotas and limitations for RDS Proxy - [Documentation URL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)",
    "Observations": "Ensure proxy creation avoids unsupported AZs in affected regions."
  },
  {
    "Description": "RDS Proxy automatically creates the 'rdsproxyadmin' DB user; altering or removing it can impact proxy availability.",
    "Reference": "Section: Quotas and limitations for RDS Proxy - [Documentation URL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)",
    "Observations": "Maintain default user to ensure continuity and stability of operations."
  },
  {
    "Description": "Session pinning must be monitored as it impacts connection reuse and proxy efficiency.",
    "Reference": "See documentation on avoiding pinning an RDS Proxy - [Documentation URL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)",
    "Observations": "Adjust application queries to reduce unnecessary session pinning."
  },
  {
    "Description": "Secrets Manager secrets associated with RDS Proxy should align with DB collation and IAM configurations.",
    "Reference": "Sections specific to MariaDB, MySQL, and SQL Server - [Documentation URL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)",
    "Observations": "Create and manage secrets according to app-specific authentication needs."
  },
  {
    "Description": "RDS Proxies associated with PostgreSQL must ensure `SCRAM` or `MD5` authentication settings to avoid downtime.",
    "Reference": "Section: Additional limitations for RDS for PostgreSQL - [Documentation URL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)",
    "Observations": "Plan authentication changes and migration strategies carefully."
  }
]
```

### Notes
- The requirements extracted focus on aspects that can be managed through AWS services and configurations, such as IAM, VPC, and AWS Secrets Manager.
- The observations indicate areas where further verification or monitoring may be necessary to ensure compliance and optimal operations.
- This structured extraction serves as a foundation for creating automated security controls and operations monitoring scripts.