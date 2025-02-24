```json
[
  {
    "Title": "Enforce TLS for RDS Proxy Connections",
    "Description": "Ensure that all connections between RDS Proxy and your database require Transport Layer Security (TLS). This setting can be configured in the AWS Management Console when creating or modifying a proxy.",
    "Applicability": "All RDS Proxy configurations",
    "Security Risk": "Without TLS, data in transit may be intercepted or altered, compromising data integrity and confidentiality.",
    "Default Behavior / Limitations": "TLS is not enforced by default and must be configured explicitly.",
    "Automation": "Can be enforced by setting the TLS requirement during RDS Proxy setup in the AWS Management Console.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.howitworks.html"
    ]
  },
  {
    "Title": "Store Database Credentials in AWS Secrets Manager",
    "Description": "All database credentials for RDS DB instances accessed by RDS Proxy must be stored in AWS Secrets Manager. Ensure that each database user has a corresponding secret.",
    "Applicability": "All RDS DB instances accessed through RDS Proxy",
    "Security Risk": "Storing credentials directly on servers or applications increases the risk of credential theft or exposure.",
    "Default Behavior / Limitations": "Credentials must be manually stored in Secrets Manager as this is not an automatic process.",
    "Automation": "Can be automated using AWS Secrets Manager API to manage and retrieve credentials for RDS Proxy.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.howitworks.html"
    ]
  },
  {
    "Title": "Enable IAM Authentication for RDS Proxy",
    "Description": "Configure RDS Proxy to allow and enforce IAM authentication for users accessing the database. This complements native password authentication by allowing the use of IAM roles.",
    "Applicability": "All applications using RDS Proxy",
    "Security Risk": "Without IAM authentication, credential management is less centralized and consistent, increasing the risk of unauthorized access.",
    "Default Behavior / Limitations": "IAM authentication must be configured as it is not enabled by default for RDS Proxy.",
    "Automation": "Can be enforced using IAM roles and policies within the AWS Management Console.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.howitworks.html"
    ]
  },
  {
    "Title": "Use IAM Roles for RDS Proxy Connections",
    "Description": "Always use IAM roles for application connections to RDS Proxy, ensuring robust authentication even if the proxy connects to the database using native authentication.",
    "Applicability": "All applications connecting through RDS Proxy",
    "Security Risk": "Relying solely on database-native authentication limits the security posture available through IAM policies.",
    "Default Behavior / Limitations": "Using IAM roles requires configuration as this is not the default setting.",
    "Automation": "Can be automated through the configuration of IAM roles and associated policies.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.howitworks.html"
    ]
  },
  {
    "Title": "Enforce SSL with VERIFY_CA/VERIFY_IDENTITY for MySQL Clients",
    "Description": "Ensure MySQL clients use the `--ssl-mode` parameter set to `VERIFY_CA` or `VERIFY_IDENTITY`, and specify the CA certificate using the `--ssl-ca` option to enforce SSL connections and CA verification.",
    "Applicability": "MySQL clients connecting through RDS Proxy",
    "Security Risk": "Without verifying the CA, SSL connections could be subject to MITM attacks, undermining connection security.",
    "Default Behavior / Limitations": "Clients need to be manually configured with the `--ssl-mode` and `--ssl-ca` parameters.",
    "Automation": "Manual client configuration is required; cannot be enforced directly via AWS configuration.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.howitworks.html"
    ]
  },
  {
    "Title": "Specify Client-Side TLS/SSL Session Requirements",
    "Description": "For MySQL, use the `--ssl-mode` parameter; for PostgreSQL, use `sslmode=require` to specify client-side TLS/SSL session requirements when connecting to RDS Proxy.",
    "Applicability": "All clients connecting through RDS Proxy",
    "Security Risk": "Not specifying TLS/SSL could lead to unencrypted connections, risking data interception.",
    "Default Behavior / Limitations": "TLS/SSL session requirements must be manually configured on the client-side.",
    "Automation": "Manual client configuration is needed to enforce TLS/SSL settings; not directly automatable through AWS.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.howitworks.html"
    ]
  },
  {
    "Title": "Ensure RDS Proxy Handles Failover Efficiently",
    "Description": "RDS Proxy should maintain accepting connections at the same IP during failover and automatically redirect to the new primary DB instance to minimize disruption.",
    "Applicability": "RDS Proxy with high-availability configurations",
    "Security Risk": "Improper handling of failovers could result in downtime and reduced availability, affecting service reliability.",
    "Default Behavior / Limitations": "Failover handling is an inherent feature of RDS Proxy but requires proper setup to function seamlessly.",
    "Automation": "Setup and test failover scenarios to ensure RDS Proxy correctly manages transitions; requires manual validation.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.howitworks.html"
    ]
  },
  {
    "Title": "Utilize Native TLS/SSL Configurations in RDS Proxy",
    "Description": "Ensure that RDS Proxy leverages existing native TLS/SSL configurations to enforce encryption for all connections.",
    "Applicability": "All RDS Proxy connections",
    "Security Risk": "Without encryption, data transmitted may be exposed to interception and unauthorized access.",
    "Default Behavior / Limitations": "TLS/SSL support is provided but must be properly configured to suit specific security needs.",
    "Automation": "TLS/SSL can be enforced through configurations made during the RDS Proxy setup process.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.howitworks.html"
    ]
  }
]
```