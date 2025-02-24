```json
[
  {
    "Description": "Ensure each app-tier Auto Scaling Group (ASG) has an associated Elastic Load Balancer (ELB) to maintain availability and distribute application load.",
    "Reference": "AWS AutoScaling Best Practices - [App-Tier Auto Scaling Group associated ELB](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/app-tier-autoscaling-group-associated-load-balancer.html)",
    "Observations": ""
  },
  {
    "Description": "Ensure Amazon Auto Scaling Groups utilize cooldown periods.",
    "Reference": "AWS AutoScaling Best Practices - [Auto Scaling Group Cooldown Period](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/cooldown-period.html)",
    "Observations": ""
  },
  {
    "Description": "Enable ELB health check if Elastic Load Balancing is used, and EC2 health check if not, for Auto Scaling groups.",
    "Reference": "AWS AutoScaling Best Practices - [Auto Scaling Group Health Check](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/auto-scaling-group-health-check.html)",
    "Observations": ""
  },
  {
    "Description": "Enable notifications for ASGs to receive scaling operations information.",
    "Reference": "AWS AutoScaling Best Practices - [Auto Scaling Group Notifications](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/auto-scaling-group-notifications.html)",
    "Observations": ""
  },
  {
    "Description": "Ensure Auto Scaling Groups have active Elastic Load Balancers.",
    "Reference": "AWS AutoScaling Best Practices - [Auto Scaling Group Referencing Missing ELB](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/auto-scaling-group-referencing-missing-elb.html)",
    "Observations": ""
  },
  {
    "Description": "Install AWS CloudWatch Logs agent within Auto Scaling Group for app tier.",
    "Reference": "AWS AutoScaling Best Practices - [CloudWatch Logs Agent for App-Tier Auto Scaling Group In Use](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/app-tier-autoscaling-group-cloudwatch-logs-agent.html)",
    "Observations": ""
  },
  {
    "Description": "Install AWS CloudWatch Logs agent within Auto Scaling Group for web tier.",
    "Reference": "AWS AutoScaling Best Practices - [CloudWatch Logs Agent for Web-Tier Auto Scaling Group In Use](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/web-tier-autoscaling-group-cloudwatch-logs-agent.html)",
    "Observations": ""
  },
  {
    "Description": "Configure metadata response hop limit for EC2 instances within Auto Scaling Group.",
    "Reference": "AWS AutoScaling Best Practices - [Configure Metadata Response Hop Limit](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/auto-scaling-group-imds-ttl.html)",
    "Observations": ""
  },
  {
    "Description": "Use multiple instance types across multiple Availability Zones for Auto Scaling Groups.",
    "Reference": "AWS AutoScaling Best Practices - [Configure Multiple Instance Types Across Multiple AZs](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/asg-multiple-instance-type-az.html)",
    "Observations": ""
  },
  {
    "Description": "Disable public IP association in Auto Scaling Group launch templates.",
    "Reference": "AWS AutoScaling Best Practices - [Disable Public IP Association in ASG Launch Templates](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/disable-associate-public-ip-address.html)",
    "Observations": ""
  },
  {
    "Description": "Identify and remove empty AWS Auto Scaling Groups.",
    "Reference": "AWS AutoScaling Best Practices - [Empty Auto Scaling Group](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/empty-auto-scaling-group.html)",
    "Observations": ""
  },
  {
    "Description": "Use app-tier IAM roles for ASG launch configurations.",
    "Reference": "AWS AutoScaling Best Practices - [IAM Roles for App-Tier ASG Launch Configurations](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/app-tier-autoscaling-group-launch-configuration-iam-role.html)",
    "Observations": ""
  },
  {
    "Description": "Use web-tier IAM roles for ASG launch configurations.",
    "Reference": "AWS AutoScaling Best Practices - [IAM Roles for Web-Tier ASG Launch Configurations](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/web-tier-autoscaling-group-launch-configuration-iam-role.html)",
    "Observations": ""
  },
  {
    "Description": "Ensure AWS Launch Configurations utilize active Amazon Machine Images.",
    "Reference": "AWS AutoScaling Best Practices - [Launch Configuration Referencing Missing AMI](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/launch-configuration-referencing-missing-ami.html)",
    "Observations": ""
  },
  {
    "Description": "Ensure AWS Launch Configurations utilize active Security Groups.",
    "Reference": "AWS AutoScaling Best Practices - [Launch Configuration Referencing Missing Security Groups](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/launch-configuration-referencing-missing-security-group.html)",
    "Observations": ""
  },
  {
    "Description": "Utilize multiple Availability Zones in AWS Auto Scaling Groups.",
    "Reference": "AWS AutoScaling Best Practices - [Multi-AZ Auto Scaling Groups](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/multiple-availability-zones.html)",
    "Observations": ""
  },
  {
    "Description": "Ensure AWS Availability Zones for ASGs and their ELBs are the same.",
    "Reference": "AWS AutoScaling Best Practices - [Same Availability Zones In ASG And ELB](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/same-availability-zones-in-asg-and-elb.html)",
    "Observations": ""
  },
  {
    "Description": "Ensure no Amazon Auto Scaling Groups have suspended processes.",
    "Reference": "AWS AutoScaling Best Practices - [Suspended Auto Scaling Groups](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/suspended-auto-scaling-groups.html)",
    "Observations": ""
  },
  {
    "Description": "Identify and remove unused AWS Auto Scaling Launch Configuration templates.",
    "Reference": "AWS AutoScaling Best Practices - [Unused Launch Configuration](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/unused-launch-configuration.html)",
    "Observations": ""
  },
  {
    "Description": "Use approved Amazon Machine Images for app-tier ASG launch configurations.",
    "Reference": "AWS AutoScaling Best Practices - [Use Approved AMIs for App-Tier ASG Launch Configurations](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/app-tier-autoscaling-launch-configuration-approved-amazon-machine-image.html)",
    "Observations": ""
  },
  {
    "Description": "Use approved Amazon Machine Images for web-tier ASG launch configurations.",
    "Reference": "AWS AutoScaling Best Practices - [Use Approved AMIs for Web-Tier ASG Launch Configurations](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/web-tier-autoscaling-launch-configuration-approved-amazon-machine-image.html)",
    "Observations": ""
  },
  {
    "Description": "Ensure Auto Scaling Groups utilize launch templates.",
    "Reference": "AWS AutoScaling Best Practices - [Use Launch Templates for Auto Scaling Groups](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/asg-launch-template.html)",
    "Observations": ""
  },
  {
    "Description": "Ensure each web-tier Auto Scaling Group has an associated Elastic Load Balancer to maintain availability and distribute application load.",
    "Reference": "AWS AutoScaling Best Practices - [Web-Tier Auto Scaling Group associated ELB](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/web-tier-autoscaling-group-associated-load-balancer.html)",
    "Observations": ""
  }
]
```