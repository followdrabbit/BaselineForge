# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/global-accelerator/latest/dg/secure-vpc-connections.html'}

[](/pdfs/global-accelerator/latest/dg/global-accelerator-guide.pdf#secure-vpc-
connections "Open PDF")

[Documentation](/index.html)[AWS Global Accelerator](/global-
accelerator/index.html)[Developer Guide](what-is-global-accelerator.html)

# Secure VPC connections in AWS Global Accelerator

When you add a Network Load Balancer, an internal Application Load Balancer,
or an Amazon EC2 instance endpoint in AWS Global Accelerator, you enable
internet traffic to flow directly to and from the endpoint in Virtual Private
Clouds (VPCs) by targeting it in a private subnet. The VPC that contains the
load balancer or EC2 instance must have an [internet
gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)
attached to it, to indicate that the VPC accepts internet traffic. However,
you don't need public IP addresses on the load balancer or EC2 instance. You
also don't need an associated internet gateway route for the subnet.

This is different from the typical internet gateway use case in which both
public IP addresses and internet gateway routes are required for internet
traffic to flow to instances or load balancers in a VPC. Even if the elastic
network interfaces of your targets are present in a public subnet (that is, a
subnet with an internet gateway route), when you use Global Accelerator for
internet traffic, Global Accelerator overrides the typical internet route and
all logical connections that arrive through the Global Accelerator also return
through Global Accelerator rather than through the internet gateway.

###### Note

Using public IP addresses and using a public subnet for your Amazon EC2
instances are not typical, though itâs possible to set up your configuration
with them. Security groups apply to any traffic that arrives to your
instances, including traffic from Global Accelerator and any public or Elastic
IP address that is assigned to your instance ENI. Use private subnets to
ensure that traffic is delivered only by Global Accelerator.

To learn more about working with ENIs, security groups, and Global
Accelerator, see [ Requirements for endpoints with client IP address
preservation](./about-endpoints.sipp-caveats.html).

Keep this information in mind when considering network perimeter issues and
configuring IAM privileges related to internet access management. For more
information about controlling internet access to your VPC, see this [ service
control policy
example](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_vpc.html).

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Troubleshooting

Logging and monitoring

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

