### ControlGen Output - Arquivo 1
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

### ControlGen Output - Arquivo 2
```json
[
  {
    "Title": "Enforce Multi-Factor Authentication (MFA) on AWS Accounts",
    "Description": "Configure AWS IAM policies to mandate MFA for all user logins across AWS accounts. Use AWS IAM Identity Center (SSO) or IAM policies with AWS Config rules, such as 'iam-user-mfa-enabled', to ensure MFA is enabled.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without MFA, accounts are vulnerable to unauthorized access if credentials are compromised.",
    "Default Behavior / Limitations": "AWS IAM does not enforce MFA by default; it must be configured by the user.",
    "Automation": "Can be enforced using AWS IAM policies and monitored via AWS Config with 'iam-user-mfa-enabled'.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html"
    ]
  },
  {
    "Title": "Enforce TLS 1.2 or Higher for Communications",
    "Description": "Configure Amazon MQ services to require TLS 1.2 or higher for all communications. Ensure that all AWS services interacting with Amazon MQ enforce SSL/TLS to protect data in transit.",
    "Applicability": "All services communicating with Amazon MQ",
    "Security Risk": "Unencrypted communications can lead to data interception and unauthorized data access.",
    "Default Behavior / Limitations": "TLS 1.2 is required; TLS 1.3 is recommended but may require additional configuration.",
    "Automation": "AWS Config can be used to verify TLS configurations for compliance with security standards.",
    "References": [
      "https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/data-protection.html"
    ]
  },
  {
    "Title": "Set Up Comprehensive AWS CloudTrail Logging",
    "Description": "Activate AWS CloudTrail in all regions and configure it to log all API actions, including management and data events. Ensure CloudTrail logs are delivered to an S3 bucket with access logging enabled.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without detailed logging, it is difficult to detect unauthorized activities or troubleshoot service issues.",
    "Default Behavior / Limitations": "CloudTrail is not enabled by default; it must be set up by the user.",
    "Automation": "Can be monitored using AWS Config rule 'cloud-trail-enabled'.",
    "References": [
      "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html"
    ]
  },
  {
    "Title": "Utilize AWS Encryption and Default Security Controls",
    "Description": "Ensure all data within AWS services is encrypted using AWS Key Management Service (KMS) and that AWS's default security controls are enabled.",
    "Applicability": "All AWS services utilizing sensitive data",
    "Security Risk": "Failure to encrypt data might result in unauthorized data exposure.",
    "Default Behavior / Limitations": "AWS provides various encryption solutions, but not all are enabled by default.",
    "Automation": "Monitor through AWS Config rules like 'kms-key-active'.",
    "References": [
      "https://docs.aws.amazon.com/kms/latest/developerguide/overview.html"
    ]
  },
  {
    "Title": "Implement Secure Naming Conventions for Amazon MQ",
    "Description": "Establish naming standards for Amazon MQ brokers and usernames that exclude the use of Personally Identifiable Information (PII) or sensitive information.",
    "Applicability": "Amazon MQ brokers and users",
    "Security Risk": "Using PII or sensitive data in names increases risk of accidental exposure.",
    "Default Behavior / Limitations": "This requires adherence to internal guidelines as AWS does not enforce naming conventions.",
    "Automation": "Manual validation required; consider using automation scripts to scan configuration for compliance.",
    "References": [
      "https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/data-protection.html"
    ]
  },
  {
    "Title": "Encrypt Amazon MQ Data at Rest Using KMS",
    "Description": "Configure Amazon MQ to use AWS Key Management Service (KMS) keys for encrypting all data at rest.",
    "Applicability": "All Amazon MQ instances",
    "Security Risk": "Unencrypted data at rest can be vulnerable to unauthorized access.",
    "Default Behavior / Limitations": "Data encryption at rest must be explicitly configured to use KMS.",
    "Automation": "Use AWS Config to ensure compliance with encryption standards.",
    "References": [
      "https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/data-protection.html"
    ]
  },
  {
    "Title": "Ensure Strong TLS for All Amazon MQ for ActiveMQ Traffic",
    "Description": "Mandate that all data in transit to and from Amazon MQ for ActiveMQ is encrypted using strong TLS configurations.",
    "Applicability": "All Amazon MQ for ActiveMQ client connections",
    "Security Risk": "Without encryption, data in transit is vulnerable to interception.",
    "Default Behavior / Limitations": "TLS enforcement must be configured.",
    "Automation": "Monitor compliance using AWS Config rules for TLS settings.",
    "References": [
      "https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/data-protection.html"
    ]
  },
  {
    "Title": "Mandate TLS for Amazon MQ for RabbitMQ Client Connections",
    "Description": "Ensure that all client connections to Amazon MQ for RabbitMQ are secured using TLS encryption.",
    "Applicability": "All Amazon MQ for RabbitMQ client connections",
    "Security Risk": "Data in transit without TLS is susceptible to unauthorized access and tampering.",
    "Default Behavior / Limitations": "TLS must be manually enabled and configured.",
    "Automation": "AWS Config can be used to audit TLS configurations.",
    "References": [
      "https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/data-protection.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 3
```json
[
  {
    "Title": "Enable CloudTrail Logging for Amazon MQ API Requests",
    "Description": "AWS CloudTrail must be enabled in all regions to log all API requests and operations made on Amazon MQ. Configure CloudTrail to record these activities across all regions for comprehensive logging.",
    "Applicability": "All AWS accounts using Amazon MQ",
    "Security Risk": "Without CloudTrail logging, unauthorized or unintended actions on Amazon MQ resources may go undetected, leading to potential security breaches.",
    "Default Behavior / Limitations": "CloudTrail does not log by default for all regions; it requires manual configuration.",
    "Automation": "Can be enforced using AWS Config rule `cloud-trail-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security-iam.html",
      "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html"
    ]
  },
  {
    "Title": "Implement Access Control via IAM Policies for Amazon MQ",
    "Description": "Define and attach IAM policies to restrict access to Amazon MQ resources based on business needs. Only users with explicit permission should perform actions on these resources.",
    "Applicability": "All AWS accounts using Amazon MQ",
    "Security Risk": "Improper access control can lead to unauthorized access and potential data breaches.",
    "Default Behavior / Limitations": "IAM does not automatically create policies; administrators must define and manage them.",
    "Automation": "Setup and management can be audited using AWS IAM Access Analyzer.",
    "References": [
      "https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security-iam.html",
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html"
    ]
  },
  {
    "Title": "Use IAM Roles for EC2 Instances Accessing AWS Services",
    "Description": "Assign IAM roles via instance profiles to applications running on Amazon EC2 instances. This allows temporary, secure credentials for accessing AWS services.",
    "Applicability": "All AWS accounts utilizing EC2 instances to access AWS services",
    "Security Risk": "Using long-term credentials can lead to security vulnerabilities if they are exposed or compromised.",
    "Default Behavior / Limitations": "Requires manual configuration of IAM roles and instance profiles.",
    "Automation": "Monitoring can be integrated using AWS Config rule `ec2-instance-profile-attached`.",
    "References": [
      "https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security-iam.html",
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html"
    ]
  },
  {
    "Title": "Regularly Rotate IAM User Access Keys",
    "Description": "Implement a policy for rotating IAM access keys at regular intervals to minimize security risks from compromised keys.",
    "Applicability": "All AWS accounts with users using access keys",
    "Security Risk": "Static credentials increase risks if they are leaked or exposed, leading to unauthorized access.",
    "Default Behavior / Limitations": "AWS does not rotate access keys automatically; this requires a manual or automated process.",
    "Automation": "Set up AWS Lambda with CloudWatch scheduled events for access key audits.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#rotate-credentials",
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html"
    ]
  },
  {
    "Title": "Enforce Multi-Factor Authentication (MFA) for AWS Resources",
    "Description": "Require multi-factor authentication (MFA) for accessing Amazon MQ and other AWS resources to add an extra layer of security.",
    "Applicability": "All AWS accounts accessing critical resources",
    "Security Risk": "Without MFA, compromised credentials could lead to unauthorized access and potential data exfiltration.",
    "Default Behavior / Limitations": "AWS IAM does not enforce MFA by default; administrators must enable it.",
    "Automation": "Can be enforced using IAM policies and AWS Config rule `iam-user-mfa-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html"
    ]
  },
  {
    "Title": "Apply Resource-Based Policies for Service Permissions",
    "Description": "Define resource-based policies for services like Amazon S3 to directly control permissions applied to the resources used by Amazon MQ.",
    "Applicability": "All AWS accounts using Amazon MQ with other services like S3",
    "Security Risk": "Without specific resource-based policies, excessive permissions might inadvertently be granted, leading to potential security vulnerabilities.",
    "Default Behavior / Limitations": "Resource-based policies must be manually defined and applied.",
    "Automation": "Review and verification can be monitored using AWS IAM Access Analyzer.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json",
      "https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-policy-language-overview.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 4
```json
[
  {
    "Title": "Enforce TLS 1.2 or Higher for Amazon MQ Client Connections",
    "Description": "Configure Amazon MQ to enforce TLS 1.2 or higher for all client connections to ensure secure communications. While TLS 1.3 is recommended for enhanced security, TLS 1.2 is the minimum acceptable level.",
    "Applicability": "All Amazon MQ client connections",
    "Security Risk": "Without enforcing TLS 1.2 or higher, data transmitted between clients and Amazon MQ can be susceptible to eavesdropping or man-in-the-middle attacks.",
    "Default Behavior / Limitations": "TLS 1.2 is the minimum version accepted by Amazon MQ as part of the AWS default security configuration.",
    "Automation": "Manual verification is required to ensure that TLS settings are configured appropriately in Amazon MQ as AWS does not provide an automated way to enforce a specific TLS version beyond the default settings.",
    "References": [
      "https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/infrastructure-security.html"
    ]
  },
  {
    "Title": "Support Cipher Suites with Perfect Forward Secrecy in Amazon MQ",
    "Description": "Configure Amazon MQ to use and prefer cipher suites that support Perfect Forward Secrecy (PFS), such as DHE or ECDHE, to maintain the confidentiality of communications even if the server's private key is compromised.",
    "Applicability": "All Amazon MQ client connections",
    "Security Risk": "Without PFS, intercepted data can be decrypted retroactively if the server's private key is compromised, jeopardizing the confidentiality of communications.",
    "Default Behavior / Limitations": "Selection of cipher suites is configured through the client and server settings. Ensure the environment uses Java 7 or later for compatibility.",
    "Automation": "Manual configuration on the client and server sides is required to ensure the use of cipher suites supporting PFS. AWS Config cannot enforce this setting.",
    "References": [
      "https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/infrastructure-security.html"
    ]
  },
  {
    "Title": "Sign Amazon MQ Requests with AWS Credentials",
    "Description": "All requests to Amazon MQ must be signed using either an IAM principal's access key ID and secret access key or through AWS STS-generated temporary security credentials to ensure authentication and integrity.",
    "Applicability": "All requests to Amazon MQ",
    "Security Risk": "Not signing requests can lead to unauthorized requests being made or request tampering, compromising the integrity and security of the messages.",
    "Default Behavior / Limitations": "Requests can be signed using AWS Signature Version 4; however, it's the responsibility of the client application to properly implement signing.",
    "Automation": "AWS Config can be used to monitor IAM policies and credentials usage but cannot enforce signing directly.",
    "References": [
      "https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/infrastructure-security.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 5
```json
[
  {
    "Title": "Disable Public Accessibility for Amazon MQ Brokers",
    "Description": "Ensure that Amazon MQ brokers are configured without public accessibility to prevent exposure to the public internet, minimizing the risk of Distributed Denial of Service (DDoS) attacks.",
    "Applicability": "All Amazon MQ brokers",
    "Security Risk": "Publicly accessible brokers are susceptible to DDoS attacks and unauthorized access, compromising the availability and security of the message queues.",
    "Default Behavior / Limitations": "By default, brokers can be configured with public accessibility; this must be proactively disabled.",
    "Automation": "Can be audited using AWS Config with a custom rule to check if any brokers are publicly accessible.",
    "References": [
      "https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/using-amazon-mq-securely.html"
    ]
  },
  {
    "Title": "Implement Authorization Maps for Amazon MQ",
    "Description": "Configure authorization maps for all Amazon MQ brokers to manage permissions by group. Ensure that sensitive groups such as 'activemq-webconsole' are properly configured if access to the ActiveMQ Web Console is needed.",
    "Applicability": "All Amazon MQ brokers",
    "Security Risk": "Without proper authorization maps, brokers might allow unauthorized users to perform restricted actions, leading to a loss of data integrity and confidentiality.",
    "Default Behavior / Limitations": "No authorization is configured by default; explicit configuration is required.",
    "Automation": "Manual validation is required to ensure proper authorization map configurations as AWS Config does not natively support this verification.",
    "References": [
      "https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/using-amazon-mq-securely.html"
    ]
  },
  {
    "Title": "Configure VPC Security Groups to Restrict Network Access to Amazon MQ",
    "Description": "VPC Security Groups must be configured to block unnecessary protocols and ports, only allowing access to those actively used by the brokers, thereby minimizing potential attack vectors.",
    "Applicability": "All Amazon MQ instances within a VPC",
    "Security Risk": "Leaving unnecessary ports open can expose the broker to unauthorized access, leading to potential data breaches or interruption in service.",
    "Default Behavior / Limitations": "Default VPC Security Groups need to be modified to restrict port access.",
    "Automation": "Can be enforced using AWS Config rules to ensure that security groups only allow traffic on defined necessary ports.",
    "References": [
      "https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/using-amazon-mq-securely.html"
    ]
  },
  {
    "Title": "Restrict Amazon MQ Broker Access to Specific Ports",
    "Description": "Allow network traffic only on required ports such as AMQP (5671), MQTT (8883), OpenWire (61617), STOMP (61614), and WebSocket (61619) by configuring VPC Security Groups, ensuring that other ports remain closed.",
    "Applicability": "All Amazon MQ brokers",
    "Security Risk": "Open ports increase the attack surface for unauthorized access and exploitation, risking data exposure and service availability.",
    "Default Behavior / Limitations": "Security Groups must be explicitly configured for each broker.",
    "Automation": "AWS Config can automate audits of Security Group rules to ensure compliance with the specified port restrictions.",
    "References": [
      "https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/using-amazon-mq-securely.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 6
```json
[
  {
    "Title": "Restrict Public Accessibility of Amazon MQ Brokers",
    "Description": "Configure Amazon MQ brokers to prevent public access by setting 'PubliclyAccessible' to 'false'. Ensure all MQ brokers are launched within private subnets of a VPC and are only accessible within that network.",
    "Applicability": "All AWS accounts using Amazon MQ",
    "Security Risk": "Publicly accessible MQ brokers are exposed to the internet, increasing the risk of unauthorized access, XSS, and clickjacking attacks, compromising confidentiality and integrity.",
    "Default Behavior / Limitations": "By default, MQ brokers can be made publicly accessible. This must be explicitly configured to 'false'.",
    "Automation": "This can be monitored using AWS Config. Create AWS Config custom rule to check if MQ brokers are set with 'PubliclyAccessible' as 'false'. Automate using AWS CloudFormation or Terraform to set 'PubliclyAccessible' to 'false' by default.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/publicly-accessible.html",
      "https://aws.amazon.com/mq/",
      "https://docs.aws.amazon.com/cli/latest/reference/mq/describe-broker.html"
    ]
  },
  {
    "Title": "Audit Amazon MQ Brokers for Public Access Using AWS CLI",
    "Description": "Utilize the AWS CLI command 'describe-broker' to programmatically audit Amazon MQ brokers and verify that 'PubliclyAccessible' is set to 'false'.",
    "Applicability": "All AWS accounts using Amazon MQ",
    "Security Risk": "Failure to regularly audit can result in unnoticed public exposure of MQ brokers, leading to potential security incidents.",
    "Default Behavior / Limitations": "AWS CLI must be available, and sufficient permissions are required to run the 'describe-broker' command.",
    "Automation": "Schedule AWS CLI commands using AWS Lambda or AWS Systems Manager to routinely check 'PubliclyAccessible' status.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/publicly-accessible.html"
    ]
  },
  {
    "Title": "Enforce Private Access Configuration for Amazon MQ Brokers Using AWS CloudFormation",
    "Description": "Deploy Amazon MQ brokers using AWS CloudFormation templates, ensuring that the creation parameter 'PubliclyAccessible' is set to 'false' to restrict public internet access.",
    "Applicability": "All AWS accounts deploying Amazon MQ brokers via AWS CloudFormation",
    "Security Risk": "Misconfiguration during broker creation can inadvertently enable public access, posing a significant risk.",
    "Default Behavior / Limitations": "CloudFormation must be used for MQ broker provisioning to enforce this configuration.",
    "Automation": "Use AWS CloudFormation stacks with templates that set 'PubliclyAccessible' to 'false'. Monitor changes using AWS Config or CloudTrail.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/publicly-accessible.html"
    ]
  },
  {
    "Title": "Use Terraform to Prevent Public Access to Amazon MQ Brokers",
    "Description": "Implement Terraform configurations with 'publicly_accessible = false' for Amazon MQ broker resources to ensure they are not publicly accessible.",
    "Applicability": "All AWS environments deploying MQ brokers via Terraform",
    "Security Risk": "Allowing public access to MQ brokers can lead to unauthorized data access and integrity issues.",
    "Default Behavior / Limitations": "Terraform must be used for infrastructure as code implementations regarding MQ broker configurations.",
    "Automation": "Terraform plans can be reviewed and applied through CI/CD pipelines, ensuring 'publicly_accessible' is set to 'false'.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/publicly-accessible.html"
    ]
  },
  {
    "Title": "Automate Amazon MQ Broker Creation to Enable Private VPC Access",
    "Description": "Script the creation or re-creation of Amazon MQ brokers using AWS CLI with the '--no-publicly-accessible' flag to ensure that brokers are only accessible within a private VPC.",
    "Applicability": "All AWS accounts requiring scripted MQ broker deployments",
    "Security Risk": "Non-private configurations can result in MQ brokers being accessed publicly, leading to security vulnerabilities.",
    "Default Behavior / Limitations": "AWS CLI scripts must be correctly configured and executed with proper permissions.",
    "Automation": "Automate using AWS Batch, Lambda, or Systems Manager to execute creation scripts with '--no-publicly-accessible'.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/publicly-accessible.html"
    ]
  }
]
```