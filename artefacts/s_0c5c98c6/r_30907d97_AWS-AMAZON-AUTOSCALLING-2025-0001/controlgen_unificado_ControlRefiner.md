```json
[
  {
    "Title": "Ensure ASG Association with ELB",
    "Description": "Each app-tier and web-tier Auto Scaling Group (ASG) must have an associated Elastic Load Balancer (ELB) to maintain high availability and balance application load across multiple instances. Verify that ELBs are attached to ASGs through AWS Management Console or AWS CLI.",
    "Applicability": "All AWS accounts utilizing Auto Scaling Groups for app-tier and web-tier",
    "Security Risk": "Without an ELB, ASG might not be able to balance incoming application traffic, leading to potential downtime and unbalanced load distribution.",
    "Default Behavior / Limitations": "AWS does not enforce this association by default.",
    "Automation": "Can be monitored using AWS Config rule `elasticloadbalancer-instances-health`. Manual verification required.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/app-tier-autoscaling-group-associated-load-balancer.html",
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/web-tier-autoscaling-group-associated-load-balancer.html"
    ]
  },
  {
    "Title": "Utilize Cooldown Periods for ASGs",
    "Description": "Auto Scaling Groups must be configured to use cooldown periods to prevent over-scaling. Set a cooldown period (typically 300s) in the ASG settings to allow time for newly launched instances to stabilize.",
    "Applicability": "All AWS accounts with Auto Scaling Groups",
    "Security Risk": "Without a cooldown period, rapid scaling actions may occur, leading to resource wastage and increased costs.",
    "Default Behavior / Limitations": "ASGs can be configured with a default cooldown period, but this may require adjustment depending on workload.",
    "Automation": "Can be enforced using AWS Management Console or CLI to specify cooldown period parameters for ASGs.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/cooldown-period.html"
    ]
  },
  {
    "Title": "Enable Health Checks for ASGs",
    "Description": "Ensure ASGs have health checks enabled: ELB health check if using Elastic Load Balancing, otherwise EC2 health check. Configure health check type and grace period appropriately in the ASG settings.",
    "Applicability": "All AWS accounts with ASGs",
    "Security Risk": "Without health checks, ASGs may not replace unhealthy instances, impacting availability and performance.",
    "Default Behavior / Limitations": "By default, EC2 health checks may be enabled but need manual setup for ELB health checks.",
    "Automation": "Can be monitored with AWS Config using a custom rule that verifies health check configuration.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/auto-scaling-group-health-check.html"
    ]
  },
  {
    "Title": "Configure ASG Notifications",
    "Description": "Enable notifications for Auto Scaling Groups to receive information about scaling operations. Configure Amazon SNS to send alerts to designated email or endpoint.",
    "Applicability": "All AWS accounts using ASGs",
    "Security Risk": "Without notifications, scaling events might go unnoticed, hindering incident response and capacity management.",
    "Default Behavior / Limitations": "Notifications are not enabled by default and require manual setup.",
    "Automation": "Can be configured using AWS Management Console, AWS CLI, or CloudFormation to automate notification setup.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/auto-scaling-group-notifications.html"
    ]
  },
  {
    "Title": "Install CloudWatch Logs Agent for ASGs",
    "Description": "Install the CloudWatch Logs agent on EC2 instances within the app-tier and web-tier ASGs to enable centralized logging and monitoring.",
    "Applicability": "All AWS accounts utilizing Auto Scaling Groups for app-tier and web-tier",
    "Security Risk": "Without logs, operational issues and security incidents may go undetected.",
    "Default Behavior / Limitations": "CloudWatch Logs agent installation must be manually configured on EC2 instances.",
    "Automation": "Can be automated with user-data scripts in launch configurations or EC2 Image Builder.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/app-tier-autoscaling-group-cloudwatch-logs-agent.html",
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/web-tier-autoscaling-group-cloudwatch-logs-agent.html"
    ]
  },
  {
    "Title": "Configure Metadata Response Hop Limit for EC2 Instances",
    "Description": "Set the metadata response hop limit for EC2 instances in Auto Scaling Groups to a value that prevents unauthorized metadata access. Default recommended hop limit is 1.",
    "Applicability": "All AWS accounts utilizing Auto Scaling Groups",
    "Security Risk": "Incorrect hop limits might expose EC2 instance metadata to unauthorized access, leading to potential data exposure.",
    "Default Behavior / Limitations": "The metadata hop limit configuration requires manual setup and is not enforced by default.",
    "Automation": "Can be automated using AWS launch templates with the `InstanceMetadataOptions` configuration.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/auto-scaling-group-imds-ttl.html"
    ]
  },
  {
    "Title": "Utilize Multiple Instance Types and AZs in ASGs",
    "Description": "Configure Auto Scaling Groups to use multiple instance types across multiple Availability Zones for increased fault tolerance and capacity optimization.",
    "Applicability": "All AWS accounts utilizing Auto Scaling Groups",
    "Security Risk": "Relying on a single instance type or Availability Zone may result in capacity shortages or regional failures affecting application availability.",
    "Default Behavior / Limitations": "This setup requires custom configuration per ASG.",
    "Automation": "Can be automated via AWS Auto Scaling launch templates and spot instance fleets.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/asg-multiple-instance-type-az.html"
    ]
  },
  {
    "Title": "Disable Public IP Assignment in ASG Launch Templates",
    "Description": "Ensure that public IP assignment is disabled in the launch templates for Auto Scaling Groups to enhance security by limiting exposure to the public internet.",
    "Applicability": "All AWS accounts using ASGs",
    "Security Risk": "Public IPs increase exposure to potential attacks unless necessary for public-facing services.",
    "Default Behavior / Limitations": "Public IP assignment must be manually disabled in the ASG launch templates.",
    "Automation": "Can be enforced through AWS Config rules or IAM policies that disallow public IP associations.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/disable-associate-public-ip-address.html"
    ]
  },
  {
    "Title": "Ensure Start of ASG with ELB in Same AZs",
    "Description": "Ensure that Auto Scaling Groups and their associated Elastic Load Balancers are configured to operate in the same Availability Zones for optimal load balancing and availability.",
    "Applicability": "All AWS accounts using ASGs with ELBs",
    "Security Risk": "Mismatch in AZs between ASGs and ELBs can result in traffic distribution issues, affecting application availability.",
    "Default Behavior / Limitations": "Requires manual configuration during ASG and ELB setup.",
    "Automation": "No direct automation; requires manual verification and alignment. Can be automated using infrastructure as code tools like AWS CloudFormation.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/same-availability-zones-in-asg-and-elb.html"
    ]
  },
  {
    "Title": "Identify and Remove Empty ASGs",
    "Description": "Detect and remove AWS Auto Scaling Groups which are not currently operating any instances to maintain cloud hygiene and reduce unnecessary costs.",
    "Applicability": "All AWS accounts with ASGs",
    "Security Risk": "Empty ASGs can indicate misconfiguration or under-utilized resources leading to cloud sprawl.",
    "Default Behavior / Limitations": "AWS does not automatically delete empty ASGs; this requires review.",
    "Automation": "Can be detected using AWS Config with custom rules; deletion requires manual confirmation or automated via scripts.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/empty-auto-scaling-group.html"
    ]
  },
  {
    "Title": "Use Approved AMIs for ASG Launch Configurations",
    "Description": "Ensure that app-tier and web-tier ASG launch configurations use only pre-approved and security-validated Amazon Machine Images (AMIs) to ensure compliance with security best practices.",
    "Applicability": "All AWS accounts using ASGs for app-tier and web-tier",
    "Security Risk": "Using unapproved AMIs may introduce vulnerabilities or non-compliant software into production environments.",
    "Default Behavior / Limitations": "AMIs must be manually reviewed and selected.",
    "Automation": "Can be enforced by tagging approved AMIs and using IAM policies to restrict AMIs usage in launch configurations.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/app-tier-autoscaling-launch-configuration-approved-amazon-machine-image.html",
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/web-tier-autoscaling-launch-configuration-approved-amazon-machine-image.html"
    ]
  },
  {
    "Title": "Ensure Launch Configurations Use Active Security Groups",
    "Description": "Ensure that all launch configurations are using security groups that are active and comply with organizational security policies.",
    "Applicability": "All AWS accounts using ASG launch configurations",
    "Security Risk": "Using outdated or incorrect security groups may expose resources to unnecessary risks.",
    "Default Behavior / Limitations": "AWS does not automatically validate the activity status of security groups.",
    "Automation": "Can be automated using AWS Config rules and AWS Security Hub for monitoring.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/launch-configuration-referencing-missing-security-group.html"
    ]
  },
  {
    "Title": "Ensure Launch Templates for ASGs",
    "Description": "Ensure that ASGs are using launch templates instead of launch configurations to leverage features like versioning and new instance parameters.",
    "Applicability": "All AWS accounts using ASGs",
    "Security Risk": "Without launch templates, it is difficult to manage configurations efficiently and reproducibly, which may lead to configuration drift.",
    "Default Behavior / Limitations": "AWS allows usage of either launch configurations or launch templates, but templates are recommended.",
    "Automation": "Automated through AWS Config rules and AWS CloudFormation setup.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/asg-launch-template.html"
    ]
  },
  {
    "Title": "Identify and Remove Unused Launch Configurations",
    "Description": "Identify and decommission unused and outdated launch configurations to streamline resource usage and eliminate unnecessary infrastructure.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Unused configurations can lead to confusion and potential misconfigurations during ASG operations.",
    "Default Behavior / Limitations": "AWS does not automatically clean up unused launch configurations.",
    "Automation": "Can be detected with AWS Config rules; removal may need manual override or scripting.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/unused-launch-configuration.html"
    ]
  },
  {
    "Title": "Enable Multi-Factor Authentication (MFA) for AWS Accounts",
    "Description": "Ensure that multi-factor authentication (MFA) is enabled on the root account and for all IAM users with console access to strengthen access security.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without MFA, unauthorized access through compromised credentials can lead to data breaches and unauthorized changes to AWS resources.",
    "Default Behavior / Limitations": "AWS does not enforce MFA by default. It requires manual activation.",
    "Automation": "MFA can be enforced by using AWS IAM policies and AWS Config rule `iam-user-mfa-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html",
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-data-protection.html"
    ]
  },
  {
    "Title": "Require TLS 1.2 or Higher for AWS Resource Communication",
    "Description": "Ensure all communication with AWS resources uses TLS 1.2 or higher to maintain data security during transit.",
    "Applicability": "All communication endpoints",
    "Security Risk": "Using older TLS versions can expose data to interception and attacks due to known vulnerabilities.",
    "Default Behavior / Limitations": "AWS services typically support TLS 1.2 by default, but verification is advisable.",
    "Automation": "Verification can be automated using AWS Config custom rules to check for allowed SSL/TLS protocols.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-data-protection.html"
    ]
  },
  {
    "Title": "Enable AWS CloudTrail for API and User Activity Logging",
    "Description": "Configure AWS CloudTrail to capture API calls and user activity across all regions for auditing and compliance.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without logging, malicious or accidental changes could go undetected, impeding incident response.",
    "Default Behavior / Limitations": "AWS CloudTrail is not enabled by default for all accounts or regions.",
    "Automation": "Can be enabled using AWS CLI or Console. Compliance can be checked with AWS Config rule `cloud-trail-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html"
    ]
  },
  {
    "Title": "Encrypt Amazon EBS Volumes Using AWS KMS Keys",
    "Description": "Use AWS KMS keys to encrypt Amazon EBS volumes to protect data at rest.",
    "Applicability": "All Amazon EBS volumes",
    "Security Risk": "Unencrypted EBS volumes may expose sensitive data if accessed by unauthorized users.",
    "Default Behavior / Limitations": "AWS supports encryption, but it is not enabled by default.",
    "Automation": "Can be enforced using AWS Config rule `ebs-volumes-encrypted`.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-data-protection.html"
    ]
  },
  {
    "Title": "Utilize Launch Templates for EBS Encryption with Customer Managed Keys",
    "Description": "Use a launch template to specify a customer managed KMS key for encrypting Amazon EBS volumes.",
    "Applicability": "All EC2 Launch Templates",
    "Security Risk": "Failing to specify a customer managed key can lead to less control over encryption key policies.",
    "Default Behavior / Limitations": "Launch configurations do not support customer managed keys.",
    "Automation": "Can be specified in EC2 Launch Templates via AWS Console or CLI.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-data-protection.html"
    ]
  },
  {
    "Title": "Enforce Encryption by Default for New EBS Volumes and Snapshots",
    "Description": "Enable encryption by default for new EBS volumes and snapshots to ensure data protection automatically upon creation.",
    "Applicability": "All EBS volumes and snapshots",
    "Security Risk": "Without automatic encryption, data may be inadvertently stored unencrypted.",
    "Default Behavior / Limitations": "AWS allows configuring regions to encrypt volumes by default.",
    "Automation": "Can be monitored using AWS Config rule `encrypted-volumes`.",
    "References": [
      "https://docs.aws.amazon.com/ebs/latest/userguide/encryption-by-default.html"
    ]
  },
  {
    "Title": "Avoid Sensitive Information in Tags and Free-Form Fields",
    "Description": "Prevent placing sensitive data like customer emails in tags or free-form text fields to avoid data leakage through logs or API responses.",
    "Applicability": "All AWS resources utilizing tags",
    "Security Risk": "Sensitive information may be unintentionally exposed to unauthorized access.",
    "Default Behavior / Limitations": "This requires manual adherence as AWS does not restrict tag content.",
    "Automation": "Manual validation required; tools like tag policies can help enforce tagging conventions.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-data-protection.html"
    ]
  },
  {
    "Title": "Use FIPS 140-3 Validated Cryptographic Modules",
    "Description": "Access AWS services through CLI or APIs using FIPS endpoints to ensure cryptographic module compliance with FIPS 140-3.",
    "Applicability": "All AWS CLI and API users requiring compliance",
    "Security Risk": "Non-compliance with FIPS standards can result in using weaker cryptographic protections, potentially leading to data compromise.",
    "Default Behavior / Limitations": "FIPS endpoints need to be explicitly specified by users.",
    "Automation": "Manual configuration required; guide users to configure their AWS CLI and SDKs to use FIPS endpoints.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-data-protection.html"
    ]
  },
  {
    "Title": "Restrict EC2 Instance Launch to Specific Tagged Templates",
    "Description": "IAM policy must restrict the `ec2:RunInstances` action to only those launch templates with the tag `purpose=testing`. Configure a resource-based policy to enforce this constraint.",
    "Applicability": "All AWS accounts managing EC2 instances through launch templates",
    "Security Risk": "If not enforced, EC2 instances can be launched using unintended or insecure configurations, leading to misconfigurations and potential security gaps.",
    "Default Behavior / Limitations": "By default, AWS allows launching instances with any template. Tag-based access must be explicitly configured.",
    "Automation": "Can be enforced via IAM policies using condition keys such as `aws:RequestTag/purpose` and `aws:TagKeys`.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-launch-template-permissions.html"
    ]
  },
  {
    "Title": "Enforce Launch Template and Version Specification for Auto Scaling",
    "Description": "IAM policies must require a launch template and its version number to be specified when creating or updating Auto Scaling groups. This prevents omitting version numbers, which can cause failures.",
    "Applicability": "All AWS accounts using Auto Scaling groups",
    "Security Risk": "Without specifying a launch template and version, there is a risk of using unintended configurations, potentially leading to errors and vulnerabilities.",
    "Default Behavior / Limitations": "AWS does not enforce this by default; users must specify this requirement in IAM policies.",
    "Automation": "Can be enforced using service control policies (SCPs) or IAM policies with condition keys to verify that both template and version are specified.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-launch-template-permissions.html"
    ]
  },
  {
    "Title": "Require IMDSv2 for EC2 Instance Launches",
    "Description": "Deny `ec2:RunInstances` permissions unless the instance is configured with `ec2:MetadataHttpTokens:required` to ensure the use of Instance Metadata Service Version 2 (IMDSv2).",
    "Applicability": "All AWS accounts launching EC2 instances",
    "Security Risk": "Using IMDSv1 exposes instances to potential metadata theft; IMDSv2 provides improved security via required token usage.",
    "Default Behavior / Limitations": "AWS allows instances to run with IMDSv1 unless manually restricted.",
    "Automation": "Can be enforced using IAM policies and condition keys to require the `ec2:MetadataHttpTokens:required` configuration.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-launch-template-permissions.html"
    ]
  },
  {
    "Title": "Allow Tagging of EC2 Instances and Volumes at Creation",
    "Description": "Provide users with the `ec2:CreateTags` permission to add tags to instances and volumes at the time of their creation.",
    "Applicability": "All AWS accounts using EC2 instances and volumes",
    "Security Risk": "Without proper tagging capabilities, it becomes challenging to manage and identify resources, potentially leading to compliance and management issues.",
    "Default Behavior / Limitations": "AWS IAM does not automatically allow users to create tags; permissions must be deliberately set.",
    "Automation": "Configurable via IAM policies by granting `ec2:CreateTags` permission.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-launch-template-permissions.html"
    ]
  },
  {
    "Title": "Grant Permissions for Describing Launch Templates",
    "Description": "Ensure users have `ec2:DescribeLaunchTemplates` and `ec2:DescribeLaunchTemplateVersions` permissions to utilize launch templates in the Auto Scaling wizard.",
    "Applicability": "All AWS accounts employing Auto Scaling groups",
    "Security Risk": "Without necessary permissions, users cannot access or use launch template features, impacting operational efficiency.",
    "Default Behavior / Limitations": "AWS requires explicit permissions for these actions; it is not granted by default.",
    "Automation": "Managed through IAM policies granting describe permissions.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-launch-template-permissions.html"
    ]
  },
  {
    "Title": "Validate Permissions Using Dry Run for Launch Templates",
    "Description": "IAM policies must ensure validation of permissions for `ec2:RunInstances` and `iam:PassRole` through a dry run of the specified launch template version.",
    "Applicability": "All AWS accounts running EC2 instances via IAM-managed launch templates",
    "Security Risk": "Without a dry run, permission misconfigurations may go unnoticed, leading to unauthorized actions or failed operations.",
    "Default Behavior / Limitations": "Dry run is not enabled by default; it must be specified during permission setup.",
    "Automation": "Can be enforced using IAM policy conditions to check permissions during a dry run.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-launch-template-permissions.html"
    ]
  },
  {
    "Title": "Restrict Access to Specific Launch Template Versions",
    "Description": "Use the `autoscaling:LaunchTemplateVersionSpecified` condition key to restrict access to only $Latest or $Default launch template versions.",
    "Applicability": "All AWS environments managing EC2 instances with launch templates",
    "Security Risk": "Access to unintended launch template versions can introduce outdated configurations, leading to potential vulnerabilities or operational failures.",
    "Default Behavior / Limitations": "AWS defaults do not restrict launch template versioning; explicit restrictions must be configured.",
    "Automation": "Enforced via IAM or SCP conditions by specifying the key `autoscaling:LaunchTemplateVersionSpecified`.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-launch-template-permissions.html"
    ]
  },
  {
    "Title": "Use IAM Role for EC2 Instances to Access AWS Services",
    "Description": "Ensure all Amazon EC2 instances use an IAM role that supplies temporary permissions for accessing AWS resources by configuring them through an attached instance profile.",
    "Applicability": "All EC2 instances",
    "Security Risk": "Without IAM roles, applications might require permanent credentials, increasing the risk of credential leakage and unauthorized access.",
    "Default Behavior / Limitations": "EC2 instances can run without an attached IAM role if not explicitly configured.",
    "Automation": "Enforce by creating and associating instance profiles via AWS CloudFormation templates or AWS CLI scripts.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html"
    ]
  },
  {
    "Title": "Associate Instance Profile with Auto Scaling Groups",
    "Description": "Ensure all EC2 instances in Auto Scaling groups are associated with an appropriate IAM instance profile using a launch template or launch configuration.",
    "Applicability": "EC2 instances in Auto Scaling groups",
    "Security Risk": "Without an instance profile, instances cannot assume the required IAM role, hindering their ability to securely access AWS services.",
    "Default Behavior / Limitations": "Requires manual configuration of instance profiles within launch templates or configurations.",
    "Automation": "Automate through AWS CloudFormation or by scripting AWS CLI commands to include IAM instance profiles in launch configurations.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html"
    ]
  },
  {
    "Title": "Deploy Least Privilege Principle for IAM Roles",
    "Description": "IAM roles must be constructed with permissions that are limited to the minimal functions required for the application or service to operate.",
    "Applicability": "All IAM roles",
    "Security Risk": "Excessive permissions can be exploited if credentials are compromised, leading to data exposure or resource manipulation.",
    "Default Behavior / Limitations": "AWS IAM does not mandate minimal permission constraints by default.",
    "Automation": "Use AWS IAM Access Analyzer to review and suggest least privilege policies that can be applied automatically.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html",
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html"
    ]
  },
  {
    "Title": "Ensure 'iam:PassRole' Permission in Identity-Based Policies",
    "Description": "Include the 'iam:PassRole' permission in IAM policies for roles that need to create or update Auto Scaling groups associated with an instance profile.",
    "Applicability": "IAM roles for users managing Auto Scaling groups",
    "Security Risk": "Without the 'iam:PassRole' permission, users might be unable to create resources with the intended access roles, potentially disrupting necessary integrations.",
    "Default Behavior / Limitations": "This permission must be explicitly granted in IAM policies.",
    "Automation": "Utilize IAM policy management tools or templates to include 'iam:PassRole' in relevant policies.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html"
    ]
  },
  {
    "Title": "Restrict 'iam:PassRole' to Specific Patterns",
    "Description": "Restrict which IAM roles can be passed via 'iam:PassRole' by setting a policy condition that only allows role names matching a specified pattern, e.g., 'qateam-*'.",
    "Applicability": "All IAM roles used in 'iam:PassRole'",
    "Security Risk": "Without restrictions, unauthorized roles could be assigned, leading to excessive permissions and potential security breaches.",
    "Default Behavior / Limitations": "IAM policies can allow unrestricted role passes without explicit name pattern restrictions.",
    "Automation": "Implement identity-based policies with conditions that utilize the 'iam:PassedToService' and 'StringLike' operators.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html"
    ]
  },
  {
    "Title": "Specify IAM Instance Profile in Launch Templates",
    "Description": "When creating launch templates, ensure the 'IamInstanceProfile' attribute specifies an IAM instance profile to be associated with the launched EC2 instances.",
    "Applicability": "Any environment using EC2 launch templates",
    "Security Risk": "Omission of an IAM instance profile might prevent instances from assuming required roles, affecting service functionality and security.",
    "Default Behavior / Limitations": "The 'IamInstanceProfile' attribute must be specified manually in launch templates.",
    "Automation": "Automate launch templates by using AWS CloudFormation or AWS CLI to include the necessary 'IamInstanceProfile'.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html"
    ]
  },
  {
    "Title": "Configure Amazon EC2 Auto Scaling with Interface VPC Endpoints",
    "Description": "Ensure that Amazon EC2 Auto Scaling instances use an interface VPC endpoint to restrict network traffic to the AWS network. This avoids using an internet gateway, NAT device, or virtual private gateway.",
    "Applicability": "All AWS environments using EC2 Auto Scaling",
    "Security Risk": "Without an interface VPC endpoint, EC2 Auto Scaling traffic may traverse the public internet, increasing the risk of eavesdropping and unauthorized access.",
    "Default Behavior / Limitations": "Using an interface VPC endpoint is not configured by default; it requires manual setup.",
    "Automation": "Can be enforced using AWS Config rule `vpc-endpoint-required`.",
    "References": [
      "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-vpc-endpoints.html"
    ]
  },
  {
    "Title": "Create Interface VPC Endpoint for Amazon EC2 Auto Scaling",
    "Description": "Create an interface VPC endpoint for Amazon EC2 Auto Scaling using the service name com.amazonaws.region.autoscaling to ensure private connectivity via AWS PrivateLink.",
    "Applicability": "All AWS environments using EC2 Auto Scaling",
    "Security Risk": "Without a dedicated VPC endpoint, communication with EC2 Auto Scaling may be exposed to insecure channels.",
    "Default Behavior / Limitations": "Manual creation of the VPC endpoint is required, it is not automatically provisioned.",
    "Automation": "Can be monitored using AWS Config custom rule or AWS CloudFormation template for endpoint configuration.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html"
    ]
  },
  {
    "Title": "Attach VPC Endpoint Policy to Control EC2 Auto Scaling API Access",
    "Description": "Attach a policy to the VPC endpoint to control access to the Amazon EC2 Auto Scaling API. The policy should specify the principal, allowed actions, and resources, including denying the deletion of scaling policies while allowing other actions.",
    "Applicability": "All AWS environments using EC2 Auto Scaling with VPC endpoint",
    "Security Risk": "Without restricting API access, unauthorized users may perform destructive actions on Auto Scaling resources.",
    "Default Behavior / Limitations": "There is no default policy; endpoint policies must be created and configured.",
    "Automation": "Can be enforced using AWS IAM policies in combination with AWS Config or AWS CloudFormation.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html"
    ]
  }
]
```