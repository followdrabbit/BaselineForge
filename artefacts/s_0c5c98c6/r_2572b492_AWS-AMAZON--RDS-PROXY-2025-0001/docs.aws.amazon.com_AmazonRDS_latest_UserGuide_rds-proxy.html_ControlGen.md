```json
[
  {
    "Title": "Limit RDS Proxies in a Single AWS Account",
    "Description": "Ensure that the number of RDS Proxies within a single AWS account does not exceed 20. Requests for an increase in this limit should be made via the AWS Management Console Service Quotas.",
    "Applicability": "All AWS accounts using Amazon RDS Proxy",
    "Security Risk": "Exceeding the proxy limit without proper request and approval can lead to disruption in setting up new proxies for applications.",
    "Default Behavior / Limitations": "The default limit is 20 RDS Proxies. This limitation is enforced by AWS and an increase requires AWS approval.",
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
    "Title": "Associate RDS Proxy Only with Writer DB Instances in Replication",
    "Description": "RDS Proxies should be configured to associate only with writer DB instances when databases are in a replication setup.",
    "Applicability": "RDS DB instances in replication with associated RDS Proxies",
    "Security Risk": "Associating RDS Proxies with non-writer instances in replication can lead to write operation handling issues.",
    "Default Behavior / Limitations": "There is no enforcement by default to restrict proxy association to writer instances only.",
    "Automation": "Monitoring configurations and alerts through CloudTrail for configuration changes that might associate a proxy with a non-writer instance.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html"
    ]
  },
  {
    "Title": "Prohibit RDS Proxy Usage with Dedicated Tenancy VPCs",
    "Description": "RDS Proxy cannot be deployed in VPCs with the tenancy set to 'dedicated'. Ensure that RDS Proxies are deployed in default tenancy VPCs.",
    "Applicability": "VPC configurations for RDS Proxy deployments",
    "Security Risk": "Attempting to use RDS Proxy in a dedicated tenancy VPC may prevent deployment and cause operational failures.",
    "Default Behavior / Limitations": "This limitation is inherent to AWS configurations.",
    "Automation": "AWS Config rules can be used to alert if an RDS Proxy is attempted to be deployed in a VPC with dedicated tenancy.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html"
    ]
  },
  {
    "Title": "Disable Custom DNS with SSL Hostname Validation for RDS Proxy",
    "Description": "Ensure that custom DNS entries are not used with RDS Proxy if SSL hostname validation is enabled.",
    "Applicability": "RDS Proxy configurations with SSL enabled",
    "Security Risk": "Using custom DNS with SSL hostname validation can lead to connection issues and security vulnerabilities.",
    "Default Behavior / Limitations": "SSL hostname validation requires adherence to strict DNS naming conventions.",
    "Automation": "Manual validation required, as detecting custom DNS usage with SSL hostname validation is not automatable directly.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html"
    ]
  },
  {
    "Title": "Configure Maximum and Additional Endpoints for RDS Proxy",
    "Description": "RDS Proxy can be configured with the default endpoint and up to 20 additional endpoints for routing and scaling purposes.",
    "Applicability": "RDS Proxy configuration for multi-endpoint scenarios",
    "Security Risk": "Not optimizing endpoint usage may lead to inefficient routing and scaling issues.",
    "Default Behavior / Limitations": "Up to 20 additional endpoints can be configured per RDS Proxy.",
    "Automation": "AWS Config can be set up to monitor the number of endpoints associated with RDS Proxies.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html"
    ]
  },
  {
    "Title": "Ensure Compliance with Availability Zone Restrictions for RDS Proxy",
    "Description": "Verify that RDS Proxies are not created in Availability Zones that have specific restrictions within certain AWS Regions.",
    "Applicability": "RDS Proxy deployment configurations",
    "Security Risk": "Deployment in restricted Availability Zones can lead to service unavailability or degraded performance.",
    "Default Behavior / Limitations": "AWS may have default restrictions based on the region.",
    "Automation": "AWS Config can validate if RDS Proxies are well-placed within supported Availability Zones.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html"
    ]
  },
  {
    "Title": "Maintain Default 'rdsproxyadmin' DB User for RDS Proxy",
    "Description": "Maintain the 'rdsproxyadmin' DB user created by the RDS Proxy to ensure operational stability and availability.",
    "Applicability": "All RDS Proxy-managed DB instances",
    "Security Risk": "Altering or removing the default user might disrupt proxy operations.",
    "Default Behavior / Limitations": "The 'rdsproxyadmin' user is automatically created, and its removal is not recommended.",
    "Automation": "AWS CloudTrail can monitor for changes to this user account.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html"
    ]
  },
  {
    "Title": "Monitor and Optimize Session Pinning in RDS Proxy",
    "Description": "Regularly monitor session pinning patterns and optimize queries to improve connection reuse and proxy efficiency.",
    "Applicability": "All applications using RDS Proxy",
    "Security Risk": "Poor session optimization can degrade performance and increase latency.",
    "Default Behavior / Limitations": "Session pinning must be managed manually.",
    "Automation": "AWS CloudWatch can be configured to create metrics around session usage patterns.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html"
    ]
  },
  {
    "Title": "Align Secrets Manager Secrets with RDS Proxy DB Collation and IAM Configurations",
    "Description": "Ensure that secrets managed within AWS Secrets Manager for RDS Proxy align with database collation and IAM authentication configurations.",
    "Applicability": "AWS Secrets Manager secret configurations for RDS Proxy integrations",
    "Security Risk": "Misaligned secrets can result in authentication failures and misconfigurations.",
    "Default Behavior / Limitations": "Manual configuration is necessary to ensure compliance with specific database settings.",
    "Automation": "AWS Config can audit the alignment of Secrets Manager configurations with specified compliance rules.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html"
    ]
  },
  {
    "Title": "Implement `SCRAM` or `MD5` Authentication for PostgreSQL RDS Proxies",
    "Description": "Ensure that RDS Proxies associated with PostgreSQL use `SCRAM` or `MD5` authentication settings to maintain availability and performance.",
    "Applicability": "RDS Proxy configurations for PostgreSQL",
    "Security Risk": "Incorrect authentication settings can cause downtime and data access issues.",
    "Default Behavior / Limitations": "Authentication settings must be configured according to application and security requirements.",
    "Automation": "AWS Config can monitor compliance with authentication settings for PostgreSQL RDS Proxies.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html"
    ]
  }
]
```