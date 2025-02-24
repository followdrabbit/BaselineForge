```json
[
  {
    "Title": "Ensure AWS Outpost ARN is Reflected in EC2 Instance Metadata",
    "Description": "Verify that the ARN of the AWS Outpost rack is recorded in the metadata of EC2 instances. This ensures accurate tracking and management of Outpost resources.",
    "Applicability": "All EC2 instances running on AWS Outposts",
    "Security Risk": "Failure to associate the correct ARN could lead to mismanagement and errors in security policy application for Outpost resources.",
    "Default Behavior / Limitations": "The ARN is supposed to automatically appear in the instance metadata once the AWS account is added.",
    "Automation": "Manual validation required to ensure Deep Security Manager reflects the correct ARN in resource metadata.",
    "References": [
      "https://help.deepsecurity.trendmicro.com/20_0/on-premise/aws-outposts.html"
    ]
  },
  {
    "Title": "Automate Security Agent Installation on Amazon EC2 and WorkSpaces",
    "Description": "Deploy security agents automatically on Amazon EC2 instances and WorkSpaces to ensure consistent and traceable security coverage using Deep Security.",
    "Applicability": "All Amazon EC2 instances and WorkSpaces within the AWS environment managed by Deep Security",
    "Security Risk": "Without automated installation, the potential exists for inconsistent security posture and increased vulnerability to threats.",
    "Default Behavior / Limitations": "Requires custom automation scripts or integration with deployment tools.",
    "Automation": "Can be automated using AWS Systems Manager for EC2 instances and a combination of scripts and deployment tools for WorkSpaces.",
    "References": [
      "https://help.deepsecurity.trendmicro.com/20_0/on-premise/aws-outposts.html"
    ]
  },
  {
    "Title": "Automate Activation of Security Agent Post-Installation",
    "Description": "Configure scripts or automation tools to activate the Deep Security agent immediately after it is installed on each node.",
    "Applicability": "All nodes with the Deep Security agent installed",
    "Security Risk": "Unactivated agents cannot enforce security controls, exposing systems to potential threats.",
    "Default Behavior / Limitations": "Activation typically requires manual intervention unless automated during deployment.",
    "Automation": "Can be automated with scripts or configuration management tools such as Ansible or AWS Systems Manager.",
    "References": [
      "https://help.deepsecurity.trendmicro.com/20_0/on-premise/aws-outposts.html"
    ]
  },
  {
    "Title": "Automate Creation and Management of Deep Security Policies",
    "Description": "Utilize API capabilities to automate the creation and ongoing management of security policies for resources managed by Deep Security.",
    "Applicability": "All resources managed through Deep Security",
    "Security Risk": "Manual policy management can lead to inconsistent security enforcement and potential vulnerabilities.",
    "Default Behavior / Limitations": "Deep Security supports API integration for policy management.",
    "Automation": "Can be automated using Deep Security APIs integrated with CI/CD pipelines.",
    "References": [
      "https://help.deepsecurity.trendmicro.com/20_0/on-premise/aws-outposts.html"
    ]
  },
  {
    "Title": "Configure High Availability for Deep Security Manager",
    "Description": "Set up Deep Security Manager instances across multiple nodes to ensure high availability using load balancing and fault tolerance configurations.",
    "Applicability": "All Deep Security Manager installations",
    "Security Risk": "Single points of failure in the security management system can result in downtime and reduced security coverage during outages.",
    "Default Behavior / Limitations": "High availability requires manual setup and configuration.",
    "Automation": "Can be automated using AWS Elastic Load Balancing and Auto Scaling for node management.",
    "References": [
      "https://help.deepsecurity.trendmicro.com/20_0/on-premise/aws-outposts.html"
    ]
  }
]
```