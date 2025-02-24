```json
[
  {
    "Title": "Enable Encryption at Rest for Elasticsearch Domains",
    "Description": "Ensure encryption at rest is enabled for all Elasticsearch domains using AWS KMS with AES-256 keys to protect data in storage.",
    "Applicability": "All Elasticsearch domains in AWS",
    "Security Risk": "Without encryption at rest, sensitive data stored in Elasticsearch domains may be exposed if the underlying storage is compromised.",
    "Default Behavior / Limitations": "Some instance types may not support encryption at rest.",
    "Automation": "Can be enforced using AWS Config rule `opensearch-encrypted-at-rest-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/opensearch-service/latest/developerguide/encryption-at-rest.html"
    ]
  },
  {
    "Title": "Restrict Public Access to Elasticsearch Domains",
    "Description": "Ensure Elasticsearch domains are hosted within a VPC to prevent public access, which can lead to unauthorized data exposure.",
    "Applicability": "All Elasticsearch domains in AWS",
    "Security Risk": "Publicly accessible Elasticsearch domains can be accessed by unauthorized users, leading to potential data exposure and integrity issues.",
    "Default Behavior / Limitations": "Domains should be within a VPC, and public subnets are not recommended.",
    "Automation": "Can be audited using AWS Config rule `opensearch-in-vpc-only`.",
    "References": [
      "https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html"
    ]
  },
  {
    "Title": "Enable Node-to-Node Encryption for Elasticsearch Domains",
    "Description": "Configure Elasticsearch domains to use node-to-node encryption to secure communications between cluster nodes.",
    "Applicability": "All Elasticsearch clusters in AWS",
    "Security Risk": "Without encryption, data traveling between nodes may be intercepted, compromising data integrity and confidentiality.",
    "Default Behavior / Limitations": "Performance may be impacted.",
    "Automation": "Can be enforced via AWS Config rule and validated using the `opensearch-node-to-node-encryption-enabled` rule.",
    "References": [
      "https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ntn.html#enabling-ntn"
    ]
  },
  {
    "Title": "Enable Error Logging to CloudWatch Logs for Elasticsearch Domains",
    "Description": "Configure Elasticsearch domains to publish error logs to CloudWatch Logs for effective auditing, access control monitoring, and incident response.",
    "Applicability": "All Elasticsearch domains in AWS",
    "Security Risk": "Without proper logging, it becomes difficult to audit access, troubleshoot issues, and respond to security incidents.",
    "Default Behavior / Limitations": "Only 'error' log types are considered in this context.",
    "Automation": "Can be configured through AWS CLI or Console, monitored via AWS Config rule.",
    "References": [
      "https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createdomain-configure-slow-logs.html#createdomain-configure-slow-logs-console"
    ]
  },
  {
    "Title": "Enable Audit Logging for Elasticsearch Domains",
    "Description": "Track all access and modifications within Elasticsearch domains by sending audit logs to CloudWatch Logs for detailed tracking and investigation of user actions.",
    "Applicability": "All Elasticsearch domains in AWS",
    "Security Risk": "Without audit logs, it's challenging to track and investigate user actions, potentially leaving security breaches undetected.",
    "Default Behavior / Limitations": "Audit logs must be explicitly enabled.",
    "Automation": "Can be enforced through AWS Management Console or API, audited via AWS Config.",
    "References": [
      "https://docs.aws.amazon.com/opensearch-service/latest/developerguide/audit-logs.html#audit-log-enabling"
    ]
  },
  {
    "Title": "Ensure Minimum of Three Data Nodes in Elasticsearch Domains",
    "Description": "Configure Elasticsearch domains with at least three data nodes to ensure high availability and fault tolerance.",
    "Applicability": "Elasticsearch domains requiring high availability",
    "Security Risk": "Having fewer data nodes reduces fault tolerance, increasing the risk of data loss or availability issues during failures.",
    "Default Behavior / Limitations": "Requires manual configuration for additional nodes.",
    "Automation": "Manual validation required; can use AWS CloudFormation templates to enforce.",
    "References": [
      "https://docs.aws.amazon.com/opensearch-service/latest/developerguide/sizing-domains.html"
    ]
  },
  {
    "Title": "Configure at Least Three Dedicated Master Nodes in Elasticsearch Domains",
    "Description": "Ensure Elasticsearch domains are configured with at least three dedicated master nodes to enhance cluster stability and fault tolerance.",
    "Applicability": "All critical Elasticsearch domains",
    "Security Risk": "Without adequate master nodes, cluster instability can lead to data loss or service outages during node or network failures.",
    "Default Behavior / Limitations": "May increase costs; Manual Configuration required.",
    "Automation": "Manually enforceable; monitor configuration via AWS Config.",
    "References": [
      "https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-advanced-options.html"
    ]
  },
  {
    "Title": "Enforce Single Connection Encryption Using Latest TLS Policy",
    "Description": "Ensure Elasticsearch domains use the latest AWS TLS policies to secure communication and protect against man-in-the-middle (MITM) attacks.",
    "Applicability": "All Elasticsearch domains exposed to networks",
    "Security Risk": "Using outdated TLS policies could expose communication to MITM attacks, risking data confidentiality and integrity.",
    "Default Behavior / Limitations": "Ensure compatibility with clients; may impact performance.",
    "Automation": "Can be enforced using AWS Config and validated through `tls-policy-enabled` checks.",
    "References": [
      "https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ntn.html#ntn-tls"
    ]
  },
  {
    "Title": "Ensure Elasticsearch Domains are Tagged Correctly",
    "Description": "Apply appropriate resource tags to Elasticsearch domains to facilitate better management, billing, and resource identification, avoiding the use of PII in tags.",
    "Applicability": "All managed Elasticsearch resources in AWS",
    "Security Risk": "Lack of tagging can lead to unmanaged resources, complicating billing, access control, and inventory management.",
    "Default Behavior / Limitations": "Tags should not contain PII.",
    "Automation": "Can be audited using AWS Config rule `required-tags`. AWS Tag Editor may be used for tag management.",
    "References": [
      "https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-awsresourcetagging.html"
    ]
  }
]
```