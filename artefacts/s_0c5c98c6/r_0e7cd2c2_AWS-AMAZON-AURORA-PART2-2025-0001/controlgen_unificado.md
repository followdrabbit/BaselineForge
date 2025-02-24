### ControlGen Output - Arquivo 1
```json
[
  {
    "Title": "Enforce Multi-Factor Authentication (MFA) for AWS Accounts",
    "Description": "All AWS accounts must have MFA enabled for additional security. Use AWS IAM policies to enforce MFA for console access.",
    "Applicability": "All AWS accounts and IAM users",
    "Security Risk": "Without MFA, accounts are vulnerable to unauthorized access, data breaches, and privilege escalation.",
    "Default Behavior / Limitations": "AWS IAM does not enforce MFA by default and requires manual configuration.",
    "Automation": "Monitor and enforce using AWS Config rule `iam-user-mfa-enabled`. Validate with AWS Security Hub.",
    "References": [
      "https://docs.aws.amazon.com/singlesignon/latest/userguide/enable-mfa.html"
    ]
  },
  {
    "Title": "Regular Rotation of IAM User Access Keys",
    "Description": "Set up an automated schedule for rotating IAM user access keys to reduce exposure risk of compromised keys.",
    "Applicability": "All IAM users with long-term credentials",
    "Security Risk": "Stale or compromised access keys can lead to unauthorized access and potential breaches.",
    "Default Behavior / Limitations": "AWS does not automatically rotate access keys.",
    "Automation": "Automate using AWS IAM Access Analyzer for access key age monitoring. Enforce action with AWS Lambda to rotate keys periodically.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#rotate-credentials"
    ]
  },
  {
    "Title": "Attach IAM Policies to Control Access Permissions",
    "Description": "Ensure IAM policies are effectively attached to identities or resources to grant necessary permissions only.",
    "Applicability": "All IAM identities and resources",
    "Security Risk": "Excessive permissions can lead to misuse or breaches of sensitive data.",
    "Default Behavior / Limitations": "IAM policy attachments must be manually configured.",
    "Automation": "Use AWS Config and AWS IAM Access Analyzer to audit permissions regularly.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json"
    ]
  },
  {
    "Title": "Use IAM Roles for EC2 Instances",
    "Description": "Assign IAM roles to EC2 instances to provide temporary credentials instead of embedding access keys directly in the configuration.",
    "Applicability": "All Amazon EC2 instances",
    "Security Risk": "Hard-coded access keys can be exposed through instance compromise, leading to unauthorized API calls.",
    "Default Behavior / Limitations": "IAM roles must be manually attached via instance profiles.",
    "Automation": "Monitor using AWS Config rule `ec2-instance-profile-attached`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html"
    ]
  },
  {
    "Title": "Centralized Access Management with AWS Identity Center",
    "Description": "Leverage AWS Identity Center for centralized access control to streamline identity management across AWS accounts and applications.",
    "Applicability": "Organizations using multiple AWS accounts",
    "Security Risk": "Decentralized identity management can lead to inconsistency in access permissions and increased security risks.",
    "Default Behavior / Limitations": "Requires setup and maintenance of synchronization configurations manually.",
    "Automation": "Use AWS Single Sign-On (SSO) to automate user access provisioning.",
    "References": [
      "https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html"
    ]
  },
  {
    "Title": "Set Permissions Boundaries for IAM Entities",
    "Description": "Implement permissions boundaries to restrict the maximum permissions that can be granted to IAM users and roles.",
    "Applicability": "IAM roles and users with sensitive permissions",
    "Security Risk": "Overprivileged users or roles may lead to unauthorized access to critical resources.",
    "Default Behavior / Limitations": "Permissions boundaries need to be defined and associated manually.",
    "Automation": "Audit using AWS Config and IAM Access Analyzer to ensure compliance.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html"
    ]
  },
  {
    "Title": "Restrict Use of AWS Root User",
    "Description": "Limit the tasks performed by the AWS root user and avoid its use for regular operations. Monitor root user activity for any anomalous access.",
    "Applicability": "All AWS accounts",
    "Security Risk": "The root user has unrestricted access, making its credentials a critical target for attackers.",
    "Default Behavior / Limitations": "Root user restrictions are not enforced by AWS by default.",
    "Automation": "Track root user actions using AWS CloudTrail and notify via AWS Security Hub for anomalous usage.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks"
    ]
  }
]
```

### ControlGen Output - Arquivo 2
```json
[
  {
    "Title": "Use aws:SourceArn and aws:SourceAccount in Resource Policies",
    "Description": "Implement resource policies for Amazon RDS that use both the `aws:SourceArn` and `aws:SourceAccount` global condition context keys to restrict permissions granted to other AWS services. This practice prevents cross-service impersonation (confused deputy) problems by ensuring that access is properly scoped to specified accounts and resources.",
    "Applicability": "All Amazon RDS resource policies granting permissions to other AWS services",
    "Security Risk": "Without these conditions, a malicious service or actor could exploit service roles to impersonate other AWS services and gain unintended access to RDS resources.",
    "Default Behavior / Limitations": "AWS does not automatically enforce the use of `aws:SourceArn` and `aws:SourceAccount` in resource policies. This configuration requires manual inclusion in policy documents.",
    "Automation": "Manual validation required, but can be monitored using AWS Config rules to check for conditions in resource policies.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/cross-service-confused-deputy-prevention.html"
    ]
  },
  {
    "Title": "Enforce aws:SourceArn and aws:SourceAccount in Absence of Account ID",
    "Description": "In scenarios where the `aws:SourceArn` does not contain an account ID, both `aws:SourceArn` and `aws:SourceAccount` condition keys must be used to define permissions in resource policies, ensuring permissions are accurately scoped.",
    "Applicability": "All Amazon RDS resource policies without explicit account ID in `aws:SourceArn`",
    "Security Risk": "Inaccurate scope of permissions due to missing account ID could result in unauthorized access if only the `aws:SourceArn` condition is used.",
    "Default Behavior / Limitations": "Manual configuration required to ensure policies include both condition keys.",
    "Automation": "Manual validation required; automated check can be conducted using policy validation tools.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/cross-service-confused-deputy-prevention.html"
    ]
  },
  {
    "Title": "Validate aws:SourceArn as Amazon RDS Resource Type",
    "Description": "Ensure that the `aws:SourceArn` used in resource policies correctly corresponds to an Amazon RDS resource type, maintaining specificity and accuracy in access controls.",
    "Applicability": "Amazon RDS resource policies using `aws:SourceArn` condition key",
    "Security Risk": "Using incorrect ARN types could inadvertently grant access to unintended resources, compromising data security.",
    "Default Behavior / Limitations": "Manual validation required to confirm proper ARN types. AWS does not verify ARN types automatically.",
    "Automation": "Manual validation required; utilize AWS IAM policy simulators or automated policy review tools for policy validation.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/cross-service-confused-deputy-prevention.html"
    ]
  },
  {
    "Title": "Use Wildcards in aws:SourceArn for Partial ARN Information",
    "Description": "When the full ARN of the resource in `aws:SourceArn` is not known, use wildcards (`*`) appropriately to specify unknown portions of the ARN. This allows the policy to remain flexible while still applying controls.",
    "Applicability": "Amazon RDS resource policies with incomplete `aws:SourceArn` information",
    "Security Risk": "Incorrect use of wildcards could overly broaden the scope of permissions, allowing unintended access.",
    "Default Behavior / Limitations": "Wildcards must be configured manually; careful consideration is required to avoid over-privilege.",
    "Automation": "Manual setting required; policy simulation tools can be used to test and validate policy effects.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/cross-service-confused-deputy-prevention.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 3
```json
[
  {
    "Title": "Enforce SSL/TLS for IAM Database Authentication",
    "Description": "Configure IAM database authentication to require SSL/TLS for all network traffic to and from the database. This involves enabling SSL/TLS in the database parameter group settings and ensuring that all client connections use SSL/TLS for encryption.",
    "Applicability": "All databases using IAM database authentication",
    "Security Risk": "Without SSL/TLS, data may be transmitted unencrypted across networks, potentially exposing sensitive information to interception.",
    "Default Behavior / Limitations": "SSL/TLS is not enforced by default in RDS configurations and must be explicitly enabled.",
    "Automation": "Can be monitored via AWS Config custom rules to ensure SSL/TLS is enforced. Use IAM policies to ensure all users connect via SSL/TLS.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html"
    ]
  },
  {
    "Title": "Limit New IAM Database Authentication Connections",
    "Description": "Implement connection pooling or use Amazon RDS Proxy to manage and limit new IAM database authentication connections to no more than 200 per second to prevent throttling.",
    "Applicability": "All RDS instances using IAM database authentication",
    "Security Risk": "Exceeding connection limits may lead to throttling, causing availability issues for clients attempting to authenticate with the database.",
    "Default Behavior / Limitations": "RDS Proxy and connection pooling must be explicitly configured to manage connection rates.",
    "Automation": "Can be configured using RDS Proxy settings and monitored with Amazon CloudWatch metrics.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html"
    ]
  },
  {
    "Title": "Optimize Usage of Authentication Tokens for IAM Database Authentication",
    "Description": "Ensure that authentication tokens for IAM database authentication are reused within their 15-minute validity period to optimize the number of token generation requests and improve system efficiency.",
    "Applicability": "All applications utilizing IAM database authentication",
    "Security Risk": "Frequent token generation can lead to unnecessary API load and potential throttling.",
    "Default Behavior / Limitations": "Token reuse optimizations must be implemented in application logic.",
    "Automation": "Manual validation required to ensure applications correctly reuse tokens.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html"
    ]
  },
  {
    "Title": "Ensure Sufficient Memory for IAM DB Authentication",
    "Description": "Configure the database cluster to have at least 300 to 1000 MiB of extra memory to ensure reliable connectivity when using IAM database authentication.",
    "Applicability": "All database clusters utilizing IAM DB authentication",
    "Security Risk": "Insufficient memory can lead to instability in handling IAM authentication requests, affecting availability.",
    "Default Behavior / Limitations": "Instance memory must be manually adjusted based on workload requirements.",
    "Automation": "Manual configuration required to adjust memory settings based on instance type and workload needs.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html"
    ]
  },
  {
    "Title": "Implement Additional Logging for IAM Authentication Activities",
    "Description": "Since CloudWatch and CloudTrail do not natively log IAM authentication activities, implement additional logging mechanisms to monitor and audit IAM database authentication events.",
    "Applicability": "All environments requiring detailed logging of IAM authentication activities",
    "Security Risk": "Lack of logging makes it difficult to audit authentication attempts and investigate anomalies.",
    "Default Behavior / Limitations": "AWS does not provide direct logging of these activities. Custom solutions are required.",
    "Automation": "Manual validation required to ensure additional logging mechanisms are implemented.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html"
    ]
  },
  {
    "Title": "Enforce IAM Role-Based Authentication for Aurora PostgreSQL",
    "Description": "Ensure that Aurora PostgreSQL databases utilize the IAM role `rds_iam` for authentication instead of traditional password-based methods for enhanced security.",
    "Applicability": "All Aurora PostgreSQL instances using IAM database authentication",
    "Security Risk": "Using password-based authentication can expose sensitive credentials and increase the risk of unauthorized access.",
    "Default Behavior / Limitations": "IAM role-based authentication must be configured manually for each database instance.",
    "Automation": "Can be audited using custom AWS Config rules or manual validation to ensure `rds_iam` role usage for authentication.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 4
```json
[
  {
    "Title": "Configure CloudWatch Alarms for Specified Metrics",
    "Description": "Set up Amazon CloudWatch alarms to monitor a single metric over a specified time period and send notifications if a defined threshold is exceeded. Ensure that alarm state change is maintained for a designated number of periods before an action is triggered.",
    "Applicability": "All AWS accounts using Amazon CloudWatch",
    "Security Risk": "Without proper monitoring, potential resource performance issues or anomalies may go undetected, leading to downtime or degraded performance.",
    "Default Behavior / Limitations": "CloudWatch does not automatically configure alarms; manual setup is required.",
    "Automation": "Can be enforced using AWS CloudFormation templates to define alarms and SNS for notifications.",
    "References": [
      "https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html"
    ]
  },
  {
    "Title": "Enable AWS CloudTrail for Logging API Calls to Amazon Aurora",
    "Description": "Activate AWS CloudTrail to capture all API calls made to Amazon Aurora. This includes details such as request sources and user identities.",
    "Applicability": "All AWS accounts with Amazon Aurora",
    "Security Risk": "Without logging, it is difficult to trace unauthorized access or configurations, posing a risk to data security.",
    "Default Behavior / Limitations": "CloudTrail logging must be manually set up; it is not enabled by default.",
    "Automation": "AWS Config rule `cloud-trail-enabled` can be used to ensure CloudTrail is active.",
    "References": [
      "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html"
    ]
  },
  {
    "Title": "Enable Enhanced Monitoring for Amazon Aurora",
    "Description": "Turn on Enhanced Monitoring for Amazon Aurora to collect real-time metrics from the operating system hosting the DB cluster. These metrics can be accessed through Amazon CloudWatch Logs.",
    "Applicability": "All AWS accounts using Amazon Aurora",
    "Security Risk": "Without real-time monitoring data, it may be challenging to diagnose performance issues or unauthorized changes swiftly.",
    "Default Behavior / Limitations": "Enhanced Monitoring requires explicit activation; it is not enabled by default.",
    "Automation": "Can be implemented and managed using AWS CLI or AWS Management Console.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Monitoring.OS.html"
    ]
  },
  {
    "Title": "Utilize Amazon RDS Performance Insights",
    "Description": "Activate Amazon RDS Performance Insights to monitor database performance and visualize database load in Amazon Aurora.",
    "Applicability": "All AWS accounts using Amazon Aurora",
    "Security Risk": "Unmonitored database performance can result in misconfigurations or unidentified performance degradation, affecting service delivery.",
    "Default Behavior / Limitations": "Performance Insights must be enabled per DB instance; it is not enabled by default.",
    "Automation": "Control can be configured via the AWS Management Console or AWS CLI.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html"
    ]
  },
  {
    "Title": "Enable Amazon Aurora Event Notifications",
    "Description": "Configure Amazon Aurora to push event notifications through Amazon SNS for specific database events, enabling prompt awareness and response to operational changes or issues.",
    "Applicability": "All AWS accounts using Amazon Aurora",
    "Security Risk": "Failure to receive timely alerts could delay response to critical database issues, impacting resilience and recovery.",
    "Default Behavior / Limitations": "Event notifications need to be manually configured; they are not enabled by default.",
    "Automation": "Can be automated using AWS CloudFormation templates to set up SNS topics and subscriptions.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.html#Aurora.Overview.Events"
    ]
  },
  {
    "Title": "Leverage AWS Trusted Advisor for Recommendations on Amazon Aurora",
    "Description": "Utilize AWS Trusted Advisor to receive advisories and checks on Amazon Aurora settings, including security group access, backups, and Multi-AZ configurations.",
    "Applicability": "All AWS accounts with active AWS Support Plans",
    "Security Risk": "Neglecting Trusted Advisor checks might lead to unoptimized configurations, posing performance or security risks.",
    "Default Behavior / Limitations": "Requires an AWS account with Business or Enterprise Support.",
    "Automation": "Automated checks and recommendations available through Trusted Advisor console and API.",
    "References": [
      "https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html#trusted-advisor"
    ]
  },
  {
    "Title": "Implement Database Activity Streams for Amazon Aurora",
    "Description": "Enable Database Activity Streams on Amazon Aurora to provide an audit trail and control over DBA access to streams.",
    "Applicability": "All AWS accounts using Amazon Aurora",
    "Security Risk": "Without activity streams, there is an increased risk of unauthorized database transactions going undetected, impacting data integrity and compliance.",
    "Default Behavior / Limitations": "Activity Streams are not enabled by default and require configuration.",
    "Automation": "Can be managed using AWS CLI or SDK to ensure appropriate setup and maintenance.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/DBActivityStreams.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 5
```json
[
  {
    "Title": "Enforce TLS 1.2 or Higher for Amazon RDS",
    "Description": "Ensure that all client connections to Amazon RDS use TLS version 1.2 or higher by configuring the database to reject connections using older protocols.",
    "Applicability": "All Amazon RDS instances",
    "Security Risk": "Older TLS versions have known vulnerabilities that can be exploited, compromising data confidentiality and integrity.",
    "Default Behavior / Limitations": "Amazon RDS supports TLS 1.0, 1.1, 1.2, and in some cases 1.3. Manual configuration is necessary to restrict to 1.2 or higher.",
    "Automation": "Monitor RDS parameter groups to ensure TLS settings are configured using AWS Config rules or AWS Lambda.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html"
    ]
  },
  {
    "Title": "Enforce Perfect Forward Secrecy Cipher Suites for Amazon RDS",
    "Description": "Configure Amazon RDS to accept only cipher suites that offer Perfect Forward Secrecy, such as DHE or ECDHE.",
    "Applicability": "All Amazon RDS instances",
    "Security Risk": "Without Perfect Forward Secrecy, session keys could be compromised if long-term keys are intercepted.",
    "Default Behavior / Limitations": "AWS Managed instances provide support, but explicit configurations may vary by client application settings.",
    "Automation": "Manual validation required to ensure client applications use the required cipher suites.",
    "References": [
      "https://aws.amazon.com/blogs/security/how-to-control-tls-ciphers-in-amazon-rds/"
    ]
  },
  {
    "Title": "Enforce IAM or STS for Amazon RDS Requests",
    "Description": "Ensure all requests to Amazon RDS are signed and authenticated using IAM credentials or AWS STS.",
    "Applicability": "All Amazon RDS API access",
    "Security Risk": "Unsigned requests can lead to unauthorized access and potential data breaches.",
    "Default Behavior / Limitations": "AWS SDKs and CLI enforce signature by default for client-side requests.",
    "Automation": "Can be enforced via IAM policies by auditing API calls using AWS CloudTrail.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html"
    ]
  },
  {
    "Title": "Restrict Amazon RDS Network Access Using Security Groups",
    "Description": "Configure AWS security groups to allow only the minimum necessary inbound and outbound traffic to Amazon RDS instances.",
    "Applicability": "All Amazon RDS instances",
    "Security Risk": "Improperly configured security groups can lead to unauthorized access and potential data breaches.",
    "Default Behavior / Limitations": "By default, all traffic is denied until security group rules are explicitly added.",
    "Automation": "Can be monitored and enforced using AWS Config rules for security group configurations.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html"
    ]
  },
  {
    "Title": "Control Public Accessibility of Amazon RDS Instances",
    "Description": "Ensure that Amazon RDS instances are appropriately configured for public access based on the 'Public accessibility' parameter.",
    "Applicability": "Amazon RDS instances with the public access requirement",
    "Security Risk": "Publicly accessible RDS instances increase the attack surface and risk unauthorized access to the database.",
    "Default Behavior / Limitations": "By default, the public accessibility setting must be manually configured during RDS instance setup.",
    "Automation": "Use AWS Config rules to audit the 'Publicly accessible' settings of RDS instances.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 6
```json
[
  {
    "Title": "Create Interface VPC Endpoint for Amazon RDS API",
    "Description": "Configure an interface VPC endpoint for the Amazon RDS API using the service name `com.amazonaws.region.rds` by leveraging the Amazon VPC console or AWS CLI, and ensure that private DNS is enabled to use the default DNS name for API requests in regions outside AWS China.",
    "Applicability": "All VPCs requiring access to Amazon RDS API without public Internet exposure",
    "Security Risk": "Without a private VPC endpoint, API traffic to Amazon RDS could potentially traverse the public Internet, increasing the risk of data interception and exposure.",
    "Default Behavior / Limitations": "Private DNS is not enabled by default in AWS Regions. Must be manually enabled when creating the endpoint.",
    "Automation": "Can be enforced using AWS CloudFormation scripts or AWS CLI commands to set up the VPC endpoint with appropriate DNS settings.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint"
    ]
  },
  {
    "Title": "Enforce VPC Endpoint Policy for Amazon RDS API",
    "Description": "Implement and customize a VPC endpoint policy for the Amazon RDS API that details which AWS IAM principals can perform specified actions on specific resources via the endpoint.",
    "Applicability": "All environments using VPC endpoints to restrict and control Amazon RDS API access",
    "Security Risk": "Using the default full access policy could allow unauthorized access to Amazon RDS resources, leading to potential data breaches or unauthorized operations.",
    "Default Behavior / Limitations": "VPC endpoints have full access by default. It is necessary to customize the policy to meet access control requirements.",
    "Automation": "Can be automated with AWS CloudFormation or AWS IAM policy templates for fine-grained access control.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html"
    ]
  },
  {
    "Title": "Use AWS PrivateLink for Amazon RDS API Access",
    "Description": "Configure AWS PrivateLink to ensure that access to the Amazon RDS API occurs privately and doesn't require public IP addresses, keeping traffic within the Amazon network.",
    "Applicability": "All VPCs requiring private access to the Amazon RDS API",
    "Security Risk": "Without PrivateLink, data traffic might exit the AWS network, increasing the vulnerability to interception and network-based attacks.",
    "Default Behavior / Limitations": "PrivateLink usage requires setting up interface endpoints and might incur additional costs.",
    "Automation": "Setup can be automated using AWS CloudFormation templates to create and configure necessary VPC endpoints.",
    "References": [
      "https://aws.amazon.com/privatelink",
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html"
    ]
  },
  {
    "Title": "Review Interface Endpoint Properties and Limitations",
    "Description": "Conduct a comprehensive review of interface endpoint properties and limitations before implementing them for RDS API endpoints, including performance constraints and compliance with outlined considerations.",
    "Applicability": "All teams responsible for the configuration and deployment of VPC endpoints",
    "Security Risk": "Ignoring endpoint limitations may lead to sub-optimal configurations that could result in outages or limit service availability.",
    "Default Behavior / Limitations": "Endpoint setup must comply with regional constraints and resource quotas.",
    "Automation": "Manual validation required due to variable project-specific constraints and environment factors.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#vpce-interface-limitations"
    ]
  },
  {
    "Title": "Verify Amazon RDS API Support for VPC Endpoints by Region",
    "Description": "Ensure that VPC endpoint support for the Amazon RDS API is available in the desired AWS region, taking into consideration any special configurations for non-standard regions such as those in AWS China.",
    "Applicability": "All deployments across various AWS Regions",
    "Security Risk": "Misconfigurations due to unsupported regions could lead to connectivity failures and hinder operations.",
    "Default Behavior / Limitations": "Endpoint availability and DNS configurations can vary across regions.",
    "Automation": "Verification requires manual review of AWS regional endpoint documentation.",
    "References": [
      "https://docs.aws.amazon.com/general/latest/gr/rande.html#rds_region"
    ]
  }
]
```

### ControlGen Output - Arquivo 7
```json
[
  {
    "Title": "Enforce Specific IP Range and Port Rules in VPC Security Groups",
    "Description": "Each VPC security group must specify inbound and outbound rules allowing access from a defined IP address range and a specific port or another security group. Configure rules correctly to comply with organizational security policies and limit to 20 rules per security group.",
    "Applicability": "All environments using VPC security groups",
    "Security Risk": "Improperly configured security groups can expose resources to unauthorized access, leading to potential data breaches or compromise.",
    "Default Behavior / Limitations": "AWS does not enforce specific IP ranges or ports by default. Security group rules must be manually configured.",
    "Automation": "AWS Config rule `vpc-sg-open-only-authorized-ports` can enforce restrictions on allowed IP ranges and ports. Use AWS CloudFormation to automate security group rule creation.",
    "References": [
      "https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.html",
      "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group.html"
    ]
  },
  {
    "Title": "Single Port Specification Per IP Range in Security Group Rules",
    "Description": "Ensure each security group rule specifies a single port for each range of IP addresses it allows access to, thereby minimizing unnecessary open ports.",
    "Applicability": "All AWS security groups",
    "Security Risk": "Leaving multiple ports open increases the potential attack surface, enabling potential intrusions.",
    "Default Behavior / Limitations": "AWS allows specifying ranges of ports which could lead to multiple open ports unintentionally.",
    "Automation": "AWS Config custom rule can be created to enforce single port specification. Use AWS CloudFormation `Properties` or custom scripts to manage.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.RDSSecurityGroups.html"
    ]
  },
  {
    "Title": "Automate VPC Security Group Creation Using AWS CloudFormation",
    "Description": "Use AWS CloudFormation to create and manage VPC security groups ensuring that configurations are consistent with best practices and organizational requirements.",
    "Applicability": "All AWS accounts using VPCs",
    "Security Risk": "Manual creation of security groups can lead to misconfigurations and non-standard implementations.",
    "Default Behavior / Limitations": "CloudFormation provides infrastructure as code capabilities but manually created resources need consistent configurations.",
    "Automation": "Fully automated through AWS CloudFormation templates, triggering updates with changesets for managing lifecycle.",
    "References": [
      "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html"
    ]
  },
  {
    "Title": "Track Changes to DB Cluster Security Groups Using Modify-db-cluster",
    "Description": "Utilize the RDS API or AWS CLI to modify DB cluster security groups, ensuring all changes are logged and reviewed by security teams.",
    "Applicability": "All AWS environments using RDS DB clusters",
    "Security Risk": "Untracked modifications could lead to unapproved access configurations and potential security risks.",
    "Default Behavior / Limitations": "Modifications are not automatically logged for review unless CloudTrail is enabled.",
    "Automation": "Enable AWS CloudTrail and AWS Config to monitor changes, using Config Rules to enforce compliance with policies.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.RDSSecurityGroups.html",
      "https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html"
    ]
  },
  {
    "Title": "Secure Non-Publicly Accessible DB Clusters Using VPN or Direct Connect",
    "Description": "Configure an AWS Site-to-Site VPN or AWS Direct Connect for secure communication with DB clusters that are not publicly accessible, ensuring connection methods adhere to security and compliance requirements.",
    "Applicability": "All AWS environments with non-public DB clusters",
    "Security Risk": "Relying solely on the internet for transmission can lead to exposure of sensitive data during transit.",
    "Default Behavior / Limitations": "VPN or Direct Connect must be manually configured for secure private network connections.",
    "Automation": "Can be automated using AWS CloudFormation and AWS Transit Gateway for consistent VPN or Direct Connect configurations.",
    "References": [
      "https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-configurations.html",
      "https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 8
```json
[
  {
    "Title": "Enforce Restricted Use of Master User in AWS RDS",
    "Description": "Ensure that the master user account for any Amazon Aurora DB cluster is not used by applications directly. Applications should use a separate database user with only the necessary privileges to perform their operations.",
    "Applicability": "All Amazon Aurora DB clusters",
    "Security Risk": "Using the master user directly increases the attack surface and potential impact from compromised applications, as it has extensive privileges.",
    "Default Behavior / Limitations": "AWS allows the use of master credentials by default; users must implement security best practices manually.",
    "Automation": "Manual validation required. Currently, AWS offers no automated method to enforce the non-use of the master user by applications. Periodic audits and application reviews are recommended.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.MasterAccounts.html"
    ]
  },
  {
    "Title": "Automate Restoration of Master User Permissions in Amazon Aurora",
    "Description": "If permissions for the master user account are removed, restore them by modifying the DB cluster and updating the master user password. This operation resets the master user's privileges to the default set.",
    "Applicability": "All Amazon Aurora DB clusters",
    "Security Risk": "Without the default permissions, the master user may be unable to perform necessary administrative actions, leading to operational disruptions.",
    "Default Behavior / Limitations": "This is a manual operation. AWS management console or CLI is required to change the master password and reset permissions.",
    "Automation": "Manual process; requires user intervention to modify the DB cluster and set a new password. Potential automation could be implemented using custom AWS Lambda scripts triggered by monitoring.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.MasterAccounts.html"
    ]
  },
  {
    "Title": "Verify System Privileges for Aurora MySQL Master User",
    "Description": "The master user in Aurora MySQL should have specific system privileges, including ALTER, CREATE USER, DELETE, based on engine version, and potentially 'rds_superuser_role' for version 3.",
    "Applicability": "Amazon Aurora MySQL DB clusters",
    "Security Risk": "Incorrect privileges may prevent necessary administrative actions or increase security risks if excessive privileges are granted.",
    "Default Behavior / Limitations": "AWS provides default master user privileges; however, adjustments can be made post-creation.",
    "Automation": "Can be monitored using AWS Config and custom rules to audit existing privileges against a defined baseline.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.MasterAccounts.html"
    ]
  },
  {
    "Title": "Verify System Privileges for Aurora PostgreSQL Master User",
    "Description": "The master user in Aurora PostgreSQL should have specific system privileges such as LOGIN, CREATEDB, CREATEROLE, and the 'RDS_SUPERUSER' role, which provides comprehensive database privileges.",
    "Applicability": "Amazon Aurora PostgreSQL DB clusters",
    "Security Risk": "Lack of necessary privileges may lead to inadequate database administration capabilities or security vulnerabilities if excessive privileges are granted.",
    "Default Behavior / Limitations": "Post-creation privilege modifications are possible. Default privileges are assigned upon DB cluster creation.",
    "Automation": "Can be verified automatically with AWS Config rules tailored to audit the privileges of the master user against predefined standards.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.MasterAccounts.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 9
```json
[
    {
        "Title": "Enforce Usage of AWSServiceRoleForRDS for Amazon RDS",
        "Description": "Ensure the use of the AWSServiceRoleForRDS service-linked role for Amazon RDS to call AWS services on behalf of your DB clusters.",
        "Applicability": "All AWS environments using Amazon RDS",
        "Security Risk": "Without the appropriate service-linked role, RDS may not have the necessary permissions, potentially disrupting service operations.",
        "Default Behavior / Limitations": "The service-linked role is automatically created when a DB cluster is created. Manual intervention is typically not required unless restricted by IAM policies.",
        "Automation": "Manual validation required; AWS IAM automatic creation upon DB cluster instantiation ensures compliance.",
        "References": [
            "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAM.ServiceLinkedRoles.html"
        ]
    },
    {
        "Title": "Validate IAM Permissions for Creating Service-Linked Roles",
        "Description": "Ensure IAM permissions 'iam:CreateServiceLinkedRole' are properly configured to allow the creation of service-linked roles.",
        "Applicability": "Accounts using service-linked roles in Amazon RDS",
        "Security Risk": "Improper configuration could hinder service operations and automatic setup of required service-linked roles.",
        "Default Behavior / Limitations": "Does not configure by default; requires manual policy adjustments.",
        "Automation": "Can be enforced using AWS IAM policy changes and regularly audited using AWS IAM Access Analyzer.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions"
        ]
    },
    {
        "Title": "Restrict Editing of AWSServiceRoleForRDS",
        "Description": "Deny editing permissions for the AWSServiceRoleForRDS service-linked role to maintain system integrity.",
        "Applicability": "All AWS accounts using Amazon RDS",
        "Security Risk": "Allowing edits to critical roles can lead to unauthorized changes and potential security breaches.",
        "Default Behavior / Limitations": "Role name changing is restricted by default, but the description can be modified.",
        "Automation": "Can be enforced using IAM policies to deny edit actions on the service-linked role.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role"
        ]
    },
    {
        "Title": "Verify Deletion of DB Clusters Before Removing AWSServiceRoleForRDS",
        "Description": "Implement checks to ensure all DB clusters are deleted before attempting to delete the AWSServiceRoleForRDS service-linked role.",
        "Applicability": "AWS accounts decommissioning RDS environments",
        "Security Risk": "Deleting the service-linked role while clusters are active could disrupt service operations.",
        "Default Behavior / Limitations": "Manual checks are necessary; no native AWS enforcement for active session detections.",
        "Automation": "Manual validation required; potentially use AWS Lambda functions to automate pre-deletion checks.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role"
        ]
    },
    {
        "Title": "Apply AmazonRDSServiceRolePolicy to Service-Linked Roles",
        "Description": "Attach the AmazonRDSServiceRolePolicy to service-linked roles to ensure necessary permissions are granted.",
        "Applicability": "All AWS accounts utilizing RDS with service-linked roles",
        "Security Risk": "Incorrect permissions could lead to operational failures or inadequate security postures.",
        "Default Behavior / Limitations": "Must be manually reviewed and applied; not automatically configured.",
        "Automation": "Can be monitored using AWS IAM Access Analyzer and enforced through AWS IAM policies.",
        "References": [
            "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonRDSServiceRolePolicy.html"
        ]
    },
    {
        "Title": "Allow rds.amazonaws.com to Assume Service-Linked Roles",
        "Description": "Ensure that only rds.amazonaws.com is allowed to assume service-linked roles such as AWSServiceRoleForRDS, AWSServiceRoleForRDSBeta, and AWSServiceRoleForRDSPreview.",
        "Applicability": "All RDS environments using service-linked roles",
        "Security Risk": "Incorrect trust relationships could lead to unauthorized access or role assumptions.",
        "Default Behavior / Limitations": "Trust relationships need to be manually verified; not inherently enforced.",
        "Automation": "Can be enforced using IAM trust policy configurations and audited via AWS IAM Access Analyzer.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions"
        ]
    }
]
```

### ControlGen Output - Arquivo 10
```json
[
  {
    "Title": "Ensure VPC has Subnets across Multiple Availability Zones",
    "Description": "Deploy the Amazon Aurora DB cluster in a VPC that contains at least two subnets across different Availability Zones to ensure high availability.",
    "Applicability": "All Amazon Aurora DB clusters in AWS",
    "Security Risk": "Without multiple availability zones, a failure in one zone could lead to database inaccessibility, affecting availability and resilience.",
    "Default Behavior / Limitations": "AWS does not enforce this automatically; users must configure subnets correctly.",
    "Automation": "Can be enforced using AWS CloudFormation by specifying 'AvailabilityZones' parameter for VPC. AWS Config can monitor using custom rules for VPC configuration.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.VPC.html"
    ]
  },
  {
    "Title": "Configure DB Subnet Groups with Multiple Availability Zones",
    "Description": "Ensure DB subnet groups contain subnets in at least two Availability Zones within an AWS Region for fault tolerance.",
    "Applicability": "All Amazon Aurora DB subnet groups",
    "Security Risk": "Single availability zone failure could result in loss of database connectivity.",
    "Default Behavior / Limitations": "AWS requires configuration; there is no automatic enforcement of multiple availability zones.",
    "Automation": "Managed via AWS CloudFormation template definitions for subnet groups. AWS Config can report compliance using custom rules.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_VPC.Scenarios.html"
    ]
  },
  {
    "Title": "Enable DNS Hostnames and DNS Resolution in VPC",
    "Description": "For public accessibility, ensure 'DNS hostnames' and 'DNS resolution' are enabled in the VPC.",
    "Applicability": "Amazon Aurora DB clusters requiring public access",
    "Security Risk": "Disabling DNS settings can prevent public endpoint resolution, causing network accessibility issues.",
    "Default Behavior / Limitations": "These settings are not enabled by default for all VPCs and must be configured.",
    "Automation": "Configured via AWS CLI or AWS Management Console. Monitoring via AWS Config custom rules.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html"
    ]
  },
  {
    "Title": "Allocate Adequate CIDR Blocks for Subnets",
    "Description": "Ensure subnets have sufficiently large CIDR blocks to accommodate spare IP addresses needed during maintenance.",
    "Applicability": "All subnets in Amazon Aurora deployments",
    "Security Risk": "Insufficient IP addresses could lead to resource exhaustion, affecting service availability during maintenance.",
    "Default Behavior / Limitations": "AWS does not automatically manage subnet CIDR block sizes.",
    "Automation": "Configured using AWS CloudFormation for initial setup. AWS Config can alert on compliance using custom rules.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Sizing.html"
    ]
  },
  {
    "Title": "Support Dual-Stack Mode in DB Subnet Groups",
    "Description": "DB subnet groups must have an associated IPv6 CIDR block to support dual-stack operations.",
    "Applicability": "Amazon Aurora DB subnet groups configured for dual-stack mode",
    "Security Risk": "Inadequate support for IPv6 can lead to future compatibility and scalability issues.",
    "Default Behavior / Limitations": "AWS does not enforce IPv6 support; it must be configured.",
    "Automation": "Managed through AWS CLI or AWS CloudFormation. AWS Config can verify the presence of IPv6 CIDR blocks.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html"
    ]
  },
  {
    "Title": "Ensure Security Groups Allow IPv4 and IPv6 Traffic",
    "Description": "Security groups must be configured to allow traffic over both IPv4 and IPv6 for dual-stack mode functionality.",
    "Applicability": "All Amazon Aurora DB clusters using dual-stack mode",
    "Security Risk": "Inadequate security group configurations can prevent proper connectivity and expose services to potential threats.",
    "Default Behavior / Limitations": "Security groups default to allowing only IPv4 unless explicitly configured for IPv6.",
    "Automation": "Configured using AWS CLI, AWS Management Console, or AWS CloudFormation, and monitored through AWS Config rules.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html"
    ]
  },
  {
    "Title": "Restrict Dual-Stack Mode DB Clusters to Private Access",
    "Description": "Ensure dual-stack mode DB clusters are private and not publicly accessible to enhance security.",
    "Applicability": "All dual-stack mode Amazon Aurora DB clusters",
    "Security Risk": "Publicly accessible endpoints can lead to increased risk of unauthorized access and exposure.",
    "Default Behavior / Limitations": "By design, dual-stack mode does not enforce private access; configurations are necessary.",
    "Automation": "Managed via AWS Security Group rules and controlled through AWS CloudFormation. Verified using AWS Config and Security Hub findings.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.manual.html"
    ]
  },
  {
    "Title": "Enable Internet Gateway for Publicly Accessible DB Clusters",
    "Description": "Ensure subnets for publicly accessible DB clusters are connected to an Internet Gateway for necessary public connectivity.",
    "Applicability": "Publicly accessible Amazon Aurora DB clusters",
    "Security Risk": "Without an Internet Gateway, publicly declared endpoints may become unreachable, impacting service availability.",
    "Default Behavior / Limitations": "Internet Gateways are not automatically associated with public subnets.",
    "Automation": "Configured via AWS Management Console, AWS CLI, or AWS CloudFormation, and audited via AWS Config.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html"
    ]
  },
  {
    "Title": "Verify DB Instance Class for Dedicated Hosting",
    "Description": "Ensure the DB instance class used is approved for dedicated instances when setting the instance tenancy attribute to dedicated.",
    "Applicability": "Amazon Aurora DB clusters with dedicated instance tenancy",
    "Security Risk": "Using unapproved instance classes with dedicated hosting may cause performance degradation and unsupported configurations.",
    "Default Behavior / Limitations": "AWS does not automatically validate compatibility of instance classes for dedicated tenancy.",
    "Automation": "Manually validated for compatibility; automated checks can be incorporated using AWS Config for specific class verifications.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Dedicated-Hardware.html"
    ]
  }
]
```