```json
[
  {
    "Title": "Validate Server Certificates for SSL/TLS Connections in RDS",
    "Description": "Ensure that all SSL/TLS connections to your RDS databases validate the server certificates to verify server identity. This involves configuring the client application to require SSL/TLS connections and validate the server certificate.",
    "Applicability": "All applications utilizing SSL/TLS connections to AWS RDS instances",
    "Security Risk": "Without server certificate validation, there's a risk of man-in-the-middle attacks, compromising data confidentiality and integrity.",
    "Default Behavior / Limitations": "Certificate validation must be configured in the client application connecting to RDS; it is not enforced by RDS itself.",
    "Automation": "Manual validation required for client application configuration; cannot be fully automated using AWS native services.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html"
    ]
  },
  {
    "Title": "Automatic Rotation of RDS Server Certificates",
    "Description": "Ensure that the RDS databases are configured to use automatically managed server certificates, which are rotated by RDS before expiration.",
    "Applicability": "All AWS RDS instances",
    "Security Risk": "Failure to rotate server certificates can lead to expired certificates, resulting in connection failures or the use of outdated certificates.",
    "Default Behavior / Limitations": "AWS RDS automatically manages and rotates server certificates for supported database engines.",
    "Automation": "This is automatically handled by AWS RDS and requires no user intervention.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html"
    ]
  },
  {
    "Title": "Set the Correct Certificate Authority (CA) for RDS Instances",
    "Description": "Configure your RDS instances to use the appropriate Certificate Authority (CA) by using AWS CLI or RDS API, if different from the default `rds-ca-rsa2048-g1`.",
    "Applicability": "All AWS RDS instances",
    "Security Risk": "Using an incorrect or compromised CA can expose the database to risks of data theft and unauthorized access.",
    "Default Behavior / Limitations": "Default CA is `rds-ca-rsa2048-g1`, can be changed manually using AWS CLI or API.",
    "Automation": "Can be automated by scripting AWS CLI commands to set the CA during provisioning.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html"
    ]
  },
  {
    "Title": "List Available Certificate Authorities using AWS CLI",
    "Description": "Use the AWS CLI to list all available Certificate Authorities (CAs) and ensure the appropriate CA is chosen based on expiration date and supported DB engine versions.",
    "Applicability": "AWS accounts managing SSL/TLS configurations for RDS",
    "Security Risk": "Selecting an inappropriate CA could lead to expired certificates or unsupported configurations, affecting availability.",
    "Default Behavior / Limitations": "Manual intervention required to check available CAs; use AWS CLI for listing.",
    "Automation": "AWS CLI command `describe-certificates` can be used to automate the listing and monitoring process.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html"
    ]
  },
  {
    "Title": "Download and Register Root CA Certificates for Application Trust Stores",
    "Description": "Ensure your applications download and register the appropriate root CA certificates to establish trust for SSL/TLS connections to AWS RDS.",
    "Applicability": "All applications connecting to AWS RDS",
    "Security Risk": "Without proper CA certificates in the trust store, SSL/TLS connections may be improperly validated leading to data interception.",
    "Default Behavior / Limitations": "Manual process required; applications must be configured to trust the CA certificate.",
    "Automation": "Manual validation is required to ensure correct certificates are downloaded and registered.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html"
    ]
  },
  {
    "Title": "Utilize ACM Certificates for RDS Proxy and Aurora Serverless v1",
    "Description": "Leverage AWS Certificate Manager (ACM) certificates for RDS Proxy and Aurora Serverless v1, simplifying certificate management by eliminating the need to manually download and install RDS certificates.",
    "Applicability": "AWS accounts using RDS Proxy and Aurora Serverless v1",
    "Security Risk": "Improper certificate management increases the risk of expired or insecure connections.",
    "Default Behavior / Limitations": "These services automatically use ACM certificates, reducing manual management requirements.",
    "Automation": "Managed automatically by AWS for RDS Proxy and Aurora Serverless v1 users.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html"
    ]
  }
]
```