# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html'}

[](/pdfs/vpc/latest/userguide/vpc-ug.pdf#vpc-security-best-practices "Open
PDF")

[Documentation](/index.html)[Amazon VPC](/vpc/index.html)[User Guide](what-is-
amazon-vpc.html)

# Security best practices for your VPC

The following best practices are general guidelines and donât represent a
complete security solution. Because these best practices might not be
appropriate or sufficient for your environment, treat them as helpful
considerations rather than prescriptions.

  * When you add subnets to your VPC to host your application, create them in multiple Availability Zones. An Availability Zone is one or more discrete data centers with redundant power, networking, and connectivity in an AWS Region. Using multiple Availability Zones makes your production applications highly available, fault tolerant, and scalable.

  * Use security groups to control traffic to EC2 instances in your subnets. For more information, see [Security groups](./vpc-security-groups.html).

  * Use network ACLs to control inbound and outbound traffic at the subnet level. For more information, see [Control subnet traffic with network access control lists](./vpc-network-acls.html).

  * Manage access to AWS resources in your VPC using AWS Identity and Access Management (IAM) identity federation, users, and roles. For more information, see [Identity and access management for Amazon VPC](./security-iam.html).

  * Use VPC Flow Logs to monitor the IP traffic going to and from a VPC, subnet, or network interface. For more information, see [VPC Flow Logs](./flow-logs.html).

  * Use Network Access Analyzer to identify unintended network access to resources in our VPCs. For more information, see the [Network Access Analyzer Guide](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/).

  * Use AWS Network Firewall to monitor and protect your VPC by filtering inbound and outbound traffic. For more information, see the [AWS Network Firewall Guide](https://docs.aws.amazon.com/network-firewall/latest/developerguide/).

  * Use Amazon GuardDuty to detect potential threats to your accounts, containers, workloads, and data within your AWS environment. The foundational threat detection includes monitoring the VPC flow logs associated with your Amazon EC2 instances. For more information, see [VPC Flow Logs](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_data-sources.html#guardduty_vpc) in the _Amazon GuardDuty User Guide_.

For answers to frequently asked questions related to VPC security, see
_Security and Filtering_ in the [Amazon VPC
FAQs](https://aws.amazon.com/vpc/faqs/).

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Advanced example

Use with other services

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

