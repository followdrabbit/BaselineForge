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
    "Title": "Utilize Multiple AZs for ASGs",
    "Description": "Configure Auto Scaling Groups to deploy instances across multiple Availability Zones to maximize resilience and availability.",
    "Applicability": "All AWS accounts using ASGs",
    "Security Risk": "Single AZ deployments can be compromised by AZ-specific failures, affecting application availability.",
    "Default Behavior / Limitations": "This requires specific configuration in the ASG settings.",
    "Automation": "Can be setup using AWS CloudFormation templates or configured through AWS Management Console.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/multiple-availability-zones.html"
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
    "Title": "Remove Suspended Processes in ASGs",
    "Description": "Ensure that no suspended processes are present in Auto Scaling Groups, as this may affect their ability to scale and maintain desired configurations.",
    "Applicability": "All AWS accounts using ASGs",
    "Security Risk": "Suspended processes can lead to inconsistent instance scaling and mismanagement of resources.",
    "Default Behavior / Limitations": "Suspended processes need manual management.",
    "Automation": "Can be monitored using AWS CloudWatch Alarms and actioned through notification/automation scripts.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/suspended-auto-scaling-groups.html"
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
  }
]
```