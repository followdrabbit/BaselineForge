```json
[
  {
    "Title": "Enforce Multi-Factor Authentication (MFA) for Sign-In",
    "Description": "All IAM users and root accounts must have multi-factor authentication enabled to enhance security during the sign-in process.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without MFA, credentials can be easily compromised, leading to unauthorized account access and potential data breaches.",
    "Default Behavior / Limitations": "AWS does not enforce MFA by default for accounts. Manual configuration is required.",
    "Automation": "Can be enforced using AWS IAM policies and monitored using AWS Config rules `iam-user-mfa-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html"
    ]
  },
  {
    "Title": "Centralized Access Management with AWS IAM Identity Center",
    "Description": "Configure AWS IAM Identity Center to centralize user access management and synchronize with the organization's identity provider.",
    "Applicability": "All organizations using AWS IAM Identity Center",
    "Security Risk": "Failure to centralize access can lead to inconsistent permission management and potential security gaps.",
    "Default Behavior / Limitations": "IAM Identity Center setup depends on the integration with external identity providers.",
    "Automation": "Requires manual integration setup but can be monitored via AWS IAM Identity Center logging capabilities.",
    "References": [
      "https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html"
    ]
  },
  {
    "Title": "Regular Access Key Rotation",
    "Description": "Implement policies to rotate IAM user access keys regularly to minimize the risk of credential exposure.",
    "Applicability": "All IAM users with long-term credentials",
    "Security Risk": "Stale access keys increase the risk of unauthorized access if the keys are compromised.",
    "Default Behavior / Limitations": "AWS does not automatically enforce access key rotation.",
    "Automation": "Can be managed with AWS Secrets Manager or AWS Config rule `access-keys-rotated`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey"
    ]
  },
  {
    "Title": "Use IAM Roles for Federated User Access",
    "Description": "Create and configure IAM roles for federated users to allow access using temporary credentials.",
    "Applicability": "Organizations using federated authentications",
    "Security Risk": "Permanent credentials increase exposure compared to temporary credentials which have limited lifespan.",
    "Default Behavior / Limitations": "AWS supports federated authentication but setup and configuration are required.",
    "Automation": "Automate role creation and policies through CloudFormation or Terraform.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html"
    ]
  },
  {
    "Title": "Implement Service-Linked Roles for AWS Services",
    "Description": "Configure service-linked roles to allow AWS services to interact securely with each other.",
    "Applicability": "All AWS services requiring cross-service interaction",
    "Security Risk": "Improperly configured roles could lead to unauthorized access to services.",
    "Default Behavior / Limitations": "AWS services may create service-linked roles automatically when needed.",
    "Automation": "Monitoring via AWS Config and CloudTrail checks on role modifications.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html"
    ]
  },
  {
    "Title": "Set Permissions Boundaries on IAM Entities",
    "Description": "Use permissions boundaries to define the maximum permissions that any identity policy can grant.",
    "Applicability": "All IAM users and roles",
    "Security Risk": "Lack of boundaries can lead to over-provisioning and increase the risk of policy mismanagement.",
    "Default Behavior / Limitations": "Permissions boundaries must be manually defined and applied.",
    "Automation": "Monitor and audit using AWS Config rules and IAM policy validations.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html"
    ]
  },
  {
    "Title": "Apply Service Control Policies (SCPs) for AWS Organizations",
    "Description": "Use SCPs to enforce the maximum permissions that identities can have in an AWS Organization.",
    "Applicability": "All AWS Organizations and corresponding OUs",
    "Security Risk": "Without SCPs, organizations risk unauthorized actions beyond desired security limits.",
    "Default Behavior / Limitations": "SCPs must be manually configured and applied to OUs.",
    "Automation": "Enforced and managed using AWS Organizations and AWS Config.",
    "References": [
      "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html"
    ]
  },
  {
    "Title": "Ensure VPC has Internet Gateway for AWS Global Accelerator",
    "Description": "Attach an internet gateway to any VPC containing a Network Load Balancer, internal Application Load Balancer, or Amazon EC2 instance used as AWS Global Accelerator endpoints, to enable acceptance of internet traffic.",
    "Applicability": "All VPCs containing AWS Global Accelerator endpoints",
    "Security Risk": "Without an internet gateway, AWS Global Accelerator cannot route internet traffic to the intended endpoints, potentially leading to loss of connectivity or service unavailability.",
    "Default Behavior / Limitations": "AWS does not automatically attach an internet gateway to VPCs. This requires manual configuration.",
    "Automation": "Can be enforced using AWS Config rule `vpc-gateway-attached` to ensure an internet gateway is attached to the target VPC.",
    "References": [
      "https://docs.aws.amazon.com/global-accelerator/latest/dg/secure-vpc-connections.html",
      "https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html"
    ]
  },
  {
    "Title": "Use Private Subnets for Amazon EC2 Instances with AWS Global Accelerator",
    "Description": "Configure Amazon EC2 instances within private subnets to ensure that all traffic directed by AWS Global Accelerator is managed efficiently through security groups.",
    "Applicability": "All deployments using AWS Global Accelerator with Amazon EC2 instances",
    "Security Risk": "Publicly accessible instances in public subnets may expose vulnerabilities and increase the attack surface.",
    "Default Behavior / Limitations": "AWS provides the capability to use private subnets, but configuration must be done manually.",
    "Automation": "Manual validation required for subnet configuration. Use AWS Config rules to ensure instances do not have public IPs.",
    "References": [
      "https://docs.aws.amazon.com/global-accelerator/latest/dg/secure-vpc-connections.html",
      "https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html"
    ]
  },
  {
    "Title": "Review IAM Policies for Network Perimeter Configurations",
    "Description": "Review and configure IAM policies to account for permissions affecting internet access and network perimeter security, ensuring compliance with organizational security postures.",
    "Applicability": "IAM roles managing VPC configurations and internet access",
    "Security Risk": "Improper IAM policies may allow unauthorized changes to network configurations, potentially exposing internal resources to the internet.",
    "Default Behavior / Limitations": "IAM permissions related to network configurations are not explicitly managed by default and require detailed policy setup.",
    "Automation": "Manual validation required. Regular IAM policy reviews and audits can be performed using AWS IAM Access Analyzer and AWS Config rules.",
    "References": [
      "https://docs.aws.amazon.com/global-accelerator/latest/dg/secure-vpc-connections.html",
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html"
    ]
  },
  {
    "Title": "Configure CloudWatch Alarms for AWS Global Accelerator Metrics",
    "Description": "Set up Amazon CloudWatch alarms to monitor AWS Global Accelerator metrics such as 'NewFlowCount', 'ProcessedBytesOut', and 'ConsumedLCUs'. Alarms should trigger notifications or automated actions if the defined thresholds are exceeded.",
    "Applicability": "All AWS accounts using AWS Global Accelerator",
    "Security Risk": "Without real-time monitoring of Global Accelerator metrics, potential issues like exceeded capacity or DDoS attempts might go unnoticed, leading to service disruptions.",
    "Default Behavior / Limitations": "Amazon CloudWatch does not automatically configure alarms; they must be set up manually.",
    "Automation": "Can be configured using AWS CloudFormation templates to deploy and manage CloudWatch alarms for specified metrics.",
    "References": [
      "https://docs.aws.amazon.com/global-accelerator/latest/dg/logging-and-monitoring.html",
      "https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html"
    ]
  },
  {
    "Title": "Enable Global Accelerator Flow Logs",
    "Description": "Set up flow logs for AWS Global Accelerator to record detailed traffic data, including source/destination IPs, ports, protocols, and the number of packets and bytes transferred.",
    "Applicability": "All AWS accounts using AWS Global Accelerator",
    "Security Risk": "Without flow logs, it is challenging to conduct thorough security audits and monitor traffic patterns, which might lead to undetected malicious activities.",
    "Default Behavior / Limitations": "Flow logs are not enabled by default and need to be configured manually.",
    "Automation": "Can be integrated with AWS CloudFormation or CLI scripts to automate the setup of Global Accelerator flow logs.",
    "References": [
      "https://docs.aws.amazon.com/global-accelerator/latest/dg/logging-and-monitoring.html",
      "https://docs.aws.amazon.com/global-accelerator/latest/dg/monitoring-global-accelerator.flow-logs.html"
    ]
  },
  {
    "Title": "Enable AWS CloudTrail for Global Accelerator API Activity",
    "Description": "Activate AWS CloudTrail to log all API calls related to AWS Global Accelerator, capturing detailed information about every request made to the service.",
    "Applicability": "All AWS accounts using AWS Global Accelerator",
    "Security Risk": "Without CloudTrail logging, crucial details of API-level activities are not preserved, impairing incident investigations and audit processes.",
    "Default Behavior / Limitations": "CloudTrail logging must be manually enabled for each account and region used.",
    "Automation": "Can be enforced using AWS Config rules to ensure CloudTrail is active and capturing necessary logs.",
    "References": [
      "https://docs.aws.amazon.com/global-accelerator/latest/dg/logging-and-monitoring.html",
      "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html"
    ]
  },
  {
    "Title": "Enforce TLS 1.2 or Higher for AWS Global Accelerator",
    "Description": "Ensure that all communications with AWS Global Accelerator use Transport Layer Security (TLS) version 1.2 or higher.",
    "Applicability": "All clients accessing AWS Global Accelerator",
    "Security Risk": "Using TLS versions below 1.2 exposes communications to vulnerabilities such as POODLE and BEAST attacks, compromising confidentiality and integrity.",
    "Default Behavior / Limitations": "AWS Global Accelerator supports TLS 1.2 and higher by default, however, enforcement must be configured.",
    "Automation": "This can be partially automated using AWS Global Accelerator settings. Continuous monitoring is recommended via AWS Config or AWS CloudTrail logs.",
    "References": [
      "https://docs.aws.amazon.com/global-accelerator/latest/dg/infrastructure-security.html"
    ]
  },
  {
    "Title": "Require Perfect Forward Secrecy (PFS) Cipher Suites for AWS Global Accelerator",
    "Description": "Ensure that AWS Global Accelerator only accepts connections encrypted with cipher suites that support perfect forward secrecy (PFS), such as DHE or ECDHE.",
    "Applicability": "All clients accessing AWS Global Accelerator",
    "Security Risk": "Without PFS, the compromise of a private key can lead to decryption of all past and future sessions even if encrypted.",
    "Default Behavior / Limitations": "Supported depending on client configuration. Ensure client systems support required cipher suites.",
    "Automation": "Monitor and enforce compliance via AWS Config or custom CloudWatch metrics by inspecting SSL/TLS client connections to verify cipher suite usage.",
    "References": [
      "https://docs.aws.amazon.com/global-accelerator/latest/dg/infrastructure-security.html"
    ]
  },
  {
    "Title": "Enforce Signed Requests for AWS Global Accelerator",
    "Description": "All API requests to AWS Global Accelerator must be signed using the caller's IAM principal credentials.",
    "Applicability": "All API requests to AWS Global Accelerator",
    "Security Risk": "Unsigned requests can lead to unauthorized operations, making it difficult to attribute actions to specific users, affecting accountability.",
    "Default Behavior / Limitations": "AWS API requests require signature, but correct implementation must be ensured on client-side.",
    "Automation": "Enforce and monitor using AWS CloudTrail and AWS Config to ensure all requests are signed and track compliance against IAM policies.",
    "References": [
      "https://docs.aws.amazon.com/global-accelerator/latest/dg/infrastructure-security.html",
      "https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html"
    ]
  }
]
```