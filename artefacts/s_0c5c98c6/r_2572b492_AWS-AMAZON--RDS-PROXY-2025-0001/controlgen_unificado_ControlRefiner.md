```json
[
  {
    "Title": "Limit RDS Proxies in a Single AWS Account",
    "Description": "Ensure that the number of RDS Proxies within a single AWS account does not exceed 20. Requests for an increase should be made via the AWS Management Console Service Quotas.",
    "Applicability": "All AWS accounts using Amazon RDS Proxy",
    "Security Risk": "Exceeding the proxy limit without proper request and approval can lead to disruption in setting up new proxies for applications.",
    "Default Behavior / Limitations": "The default limit is 20 RDS Proxies. AWS enforces this limitation and an increase requires AWS approval.",
    "Automation": "Monitoring can be implemented using AWS Service Quotas and CloudWatch to alert when the limit is approached.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html"
    ]
  },
  {
    "Title": "Ensure RDS Proxy is in the Same VPC as Associated Database",
    "Description": "Configure the RDS Proxy to reside within the same Virtual Private Cloud (VPC) as the associated database to ensure network connectivity and security.",
    "Applicability": "RDS Proxy configurations",
    "Security Risk": "Placing an RDS Proxy in a different VPC than its associated database could result in connectivity issues and potential security vulnerabilities.",
    "Default Behavior / Limitations": "RDS Proxy cannot be publicly accessible, ensuring that it operates within the correct network configuration.",
    "Automation": "AWS Config can be used to establish a rule that checks if the RDS Proxy is in the same VPC as the associated database.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html"
    ]
  },
  {
    "Title": "Use IAM Roles for RDS Proxy Connections",
    "Description": "Always use IAM roles for application connections to RDS Proxy to ensure robust authentication, enhancing security posture through IAM policies.",
    "Applicability": "All applications connecting through RDS Proxy",
    "Security Risk": "Relying solely on native authentication limits security posture available through IAM policies.",
    "Default Behavior / Limitations": "IAM roles require configuration as this is not the default setting.",
    "Automation": "Can be automated through the configuration of IAM roles and associated policies.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.howitworks.html"
    ]
  },
  {
    "Title": "Store Database Credentials in AWS Secrets Manager",
    "Description": "All database credentials for RDS DB instances accessed by RDS Proxy must be stored in AWS Secrets Manager, ensuring secure and isolated credential management.",
    "Applicability": "All RDS DB instances accessed through RDS Proxy",
    "Security Risk": "Storing credentials directly on servers or applications increases the risk of credential theft or exposure.",
    "Default Behavior / Limitations": "Credentials must be manually stored in Secrets Manager.",
    "Automation": "Can be automated using AWS Secrets Manager API to manage credentials for RDS Proxy.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.howitworks.html"
    ]
  },
  {
    "Title": "Monitor CloudWatch Metrics for DB Connection Limits",
    "Description": "Configure CloudWatch to track metrics related to RDS DB connections and memory usage. Set alarms to signal potential need for RDS Proxy.",
    "Applicability": "RDS instances nearing connection or memory limits",
    "Security Risk": "Failing to monitor these metrics may lead to unexpected service disruptions or incapacity to handle peak loads.",
    "Default Behavior / Limitations": "Default metric monitoring is available, but specific alarms must be set up.",
    "Automation": "Can be enforced using AWS CloudWatch Metrics and Alarms.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-planning.html"
    ]
  },
  {
    "Title": "Enforce TLS for RDS Proxy Connections",
    "Description": "Ensure that all connections between RDS Proxy and your database require TLS for data in transit. This setting can be configured during RDS Proxy setup.",
    "Applicability": "All RDS Proxy configurations",
    "Security Risk": "Without TLS, data in transit may be intercepted or altered, compromising data integrity and confidentiality.",
    "Default Behavior / Limitations": "TLS is not enforced by default.",
    "Automation": "Can be enforced by setting the TLS requirement during RDS Proxy setup in the AWS Management Console.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.howitworks.html"
    ]
  },
  {
    "Title": "Implement RDS Proxy for High Frequency Short-Lived DB Connections",
    "Description": "Deploy RDS Proxy for applications that frequently open and close connections to the database, reducing overhead by pooling connections.",
    "Applicability": "Applications with short-lived, frequent database connections",
    "Security Risk": "High overhead from frequent connections can degrade performance and increase costs.",
    "Default Behavior / Limitations": "RDS Proxy is not enabled by default.",
    "Automation": "Configuration can be automated using AWS CloudFormation templates.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-planning.html"
    ]
  },
  {
    "Title": "Encrypt Secrets in AWS Secrets Manager with a Custom AWS KMS Key",
    "Description": "Utilize a custom AWS KMS key for encrypting secrets in AWS Secrets Manager to enhance security by controlling who can access and manage the key.",
    "Applicability": "AWS accounts using AWS Secrets Manager",
    "Security Risk": "Secrets may be inadequately protected if not encrypted with a custom KMS key.",
    "Default Behavior / Limitations": "Secrets Manager uses the default KMS key for encryption unless specified.",
    "Automation": "Manual configuration of KMS key usage during secret creation or modification.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-secrets-arns.html"
    ]
  },
  {
    "Title": "Configure RDS Proxy Idle Client Timeout",
    "Description": "Set the IdleClientTimeout in RDS Proxy to manage idle client connections, ensuring efficient resource utilization.",
    "Applicability": "All RDS Proxy configurations",
    "Security Risk": "Improper configuration could lead to prolonged inactive connections consuming resources.",
    "Default Behavior / Limitations": "The default value is 1,800 seconds.",
    "Automation": "Configuration can be automated and monitored using AWS CloudFormation or AWS CLI.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-connections.html"
    ]
  },
  {
    "Title": "Monitor 'DatabaseConnectionsCurrentlySessionPinned' Metric in AWS CloudWatch",
    "Description": "Configure AWS CloudWatch to monitor the 'DatabaseConnectionsCurrentlySessionPinned' metric for RDS Proxy to notify administrators of performance issues due to excessive session pinning.",
    "Applicability": "All AWS accounts using RDS Proxy",
    "Security Risk": "Without monitoring, excessive session pinning could degrade database performance.",
    "Default Behavior / Limitations": "Requires manual configuration of alarms.",
    "Automation": "Automated using AWS CloudWatch alarms.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-pinning.html"
    ]
  }
]
```