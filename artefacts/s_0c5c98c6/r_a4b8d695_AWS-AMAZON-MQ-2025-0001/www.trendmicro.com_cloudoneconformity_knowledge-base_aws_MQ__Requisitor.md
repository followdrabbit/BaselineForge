```json
[
  {
    "Description": "Enable Auto Minor Version Upgrade for AWS MQ to ensure automatic receipt of minor engine upgrades during the maintenance window.",
    "Reference": "Best practice rules for Amazon MQ - [MQ Auto Minor Version Upgrade](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/auto-minor-version-upgrade.html)",
    "Observations": "Verifies if automatic minor version upgrades are configured for MQ brokers."
  },
  {
    "Description": "Use the active/standby deployment mode for AWS MQ brokers to ensure high availability.",
    "Reference": "Best practice rules for Amazon MQ - [MQ Deployment Mode](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/deployment-mode.html)",
    "Observations": "This deployment ensures that there is always an active broker in case of failures."
  },
  {
    "Description": "Ensure all Amazon MQ broker instances are of a specified type as per requirements.",
    "Reference": "Best practice rules for Amazon MQ - [MQ Desired Broker Instance Type](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/desired-instance-type.html)",
    "Observations": "Requires setting broker instance types to align with performance and cost objectives."
  },
  {
    "Description": "Use the latest version of the Apache ActiveMQ engine for your AWS MQ brokers.",
    "Reference": "Best practice rules for Amazon MQ - [MQ Engine Version](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/engine-version.html)",
    "Observations": "Ensures security patches and new features are automatically applied."
  },
  {
    "Description": "Enable the Log Exports feature for your Amazon MQ brokers to ensure activity logging.",
    "Reference": "Best practice rules for Amazon MQ - [MQ Log Exports](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/log-exports.html)",
    "Observations": "Helps in auditing and monitoring broker activities and diagnosing issues."
  },
  {
    "Description": "Configure Amazon MQ brokers using the network of brokers configuration to ensure resilience and scalability.",
    "Reference": "Best practice rules for Amazon MQ - [MQ Network of Brokers](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/network-of-brokers.html)",
    "Observations": "Improves fault tolerance by connecting brokers into a network."
  },
  {
    "Description": "Ensure AWS MQ brokers are not publicly accessible to avoid exposing sensitive data.",
    "Reference": "Best practice rules for Amazon MQ - [Publicly Accessible MQ Brokers](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/publicly-accessible.html)",
    "Observations": "Reduces the risk of unauthorized access by keeping brokers private."
  }
]
```