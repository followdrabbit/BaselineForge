```json
[
  {
    "Title": "Enable Auto Minor Version Upgrade for AWS MQ",
    "Description": "Ensure that all AWS MQ brokers have the auto minor version upgrade feature enabled to automatically receive minor engine upgrades during the maintenance window.",
    "Applicability": "All AWS MQ broker instances",
    "Security Risk": "Without automatic minor version upgrades, brokers may not receive important updates and patches, increasing security vulnerabilities.",
    "Default Behavior / Limitations": "This feature must be enabled manually as it is not enforced by default.",
    "Automation": "Can be enforced via AWS CloudFormation templates or AWS CLI by setting the AutoMinorVersionUpgrade parameter to true.",
    "References": [
      "https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/configure-broker.html"
    ]
  },
  {
    "Title": "Deploy AWS MQ Brokers in Active/Standby Mode",
    "Description": "Configure all AWS MQ brokers in active/standby deployment mode to ensure high availability and failover capabilities.",
    "Applicability": "All AWS MQ broker deployments requiring high availability",
    "Security Risk": "Without active/standby deployment, broker failure could lead to downtime, impacting availability.",
    "Default Behavior / Limitations": "Active/standby configuration must be set during broker creation.",
    "Automation": "Can be implemented through AWS CloudFormation by specifying DeploymentMode as ACTIVE_STANDBY.",
    "References": [
      "https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/active-mq.html"
    ]
  },
  {
    "Title": "Specify Amazon MQ Broker Instance Types",
    "Description": "Ensure that all Amazon MQ broker instances are configured with approved instance types as specified for performance and cost management.",
    "Applicability": "All AWS MQ brokers across AWS accounts",
    "Security Risk": "Using incorrect instance types may lead to performance degradation or higher costs than budgeted.",
    "Default Behavior / Limitations": "The instance type must be specified at the time of broker creation.",
    "Automation": "Check compliance with AWS Config rules for instance type consistency.",
    "References": [
      "https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-instance-types.html"
    ]
  },
  {
    "Title": "Use the Latest Version of Apache ActiveMQ for AWS MQ Brokers",
    "Description": "Ensure that all AWS MQ brokers are updated to the latest version of the Apache ActiveMQ engine to benefit from security patches and new features.",
    "Applicability": "All AWS MQ broker deployments",
    "Security Risk": "Running outdated versions may expose systems to unpatched vulnerabilities.",
    "Default Behavior / Limitations": "Manual upgrade needed if not using automatic minor version updates.",
    "Automation": "Monitor through AWS Config for broker versions, alert on outdated versions.",
    "References": [
      "https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/engine-types.html"
    ]
  },
  {
    "Title": "Enable Log Exports for Amazon MQ Brokers",
    "Description": "Configure Amazon MQ brokers to enable the Log Exports feature to log activities for auditing and monitoring purposes.",
    "Applicability": "All AWS MQ broker instances",
    "Security Risk": "Without logging, it is difficult to audit and monitor broker activities and diagnose issues.",
    "Default Behavior / Limitations": "Logging must be enabled during broker creation.",
    "Automation": "Ensure compliance with AWS CloudFormation and AWS CLI scripts to set theLogs property.",
    "References": [
      "https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/logging.html"
    ]
  },
  {
    "Title": "Configure Network of Brokers for Amazon MQ",
    "Description": "Configure AWS MQ brokers using a network of brokers setup to enhance resilience, fault tolerance, and scalability.",
    "Applicability": "Deployments requiring high availability and scalability",
    "Security Risk": "Without a network of brokers, individual broker failures could impact system availability.",
    "Default Behavior / Limitations": "Network configuration must be manually set and maintained.",
    "Automation": "Configuration through AWS CloudFormation or management console for a network of brokers.",
    "References": [
      "https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-network-of-brokers.html"
    ]
  },
  {
    "Title": "Ensure AWS MQ Brokers Are Not Publicly Accessible",
    "Description": "Ensure that AWS MQ brokers are configured to restrict public access to protect sensitive data and reduce exposure to unauthorized access.",
    "Applicability": "All AWS MQ deployments with sensitive data",
    "Security Risk": "Public accessibility increases the risk of unauthorized access and data breaches.",
    "Default Behavior / Limitations": "Brokers are not public by default unless configured otherwise.",
    "Automation": "Monitor with AWS Config rules and AWS Security Hub to alert if brokers become publicly accessible.",
    "References": [
      "https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-network.html"
    ]
  }
]
```