# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-vpc-endpoints.html'}

[](/pdfs/amazonswf/latest/developerguide/swf-dg.pdf#swf-vpc-endpoints "Open
PDF")

[Documentation](/index.html)[Amazon Simple Workflow
Service](/swf/index.html)[Developer Guide](swf-welcome.html)

Creating the EndpointAmazon VPC Endpoint Policies

# Amazon VPC endpoints for Amazon SWF

###### Note

AWS PrivateLink support is currently available in the AWS Top Secret - East,
AWS Secret Region, and China Regions only.

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS
resources, you can establish a connection between your Amazon VPC and Amazon
Simple Workflow Service workflows. You can use this connection with your
Amazon SWF workflows without crossing the public internet.

Amazon VPC lets you launch AWS resources in a custom virtual network. You can
use a VPC to control your network settings, such as the IP address range,
subnets, route tables, and network gateways. For more information about VPCs,
see the [Amazon VPC User
Guide](https://docs.aws.amazon.com/vpc/latest/userguide/).

To connect your Amazon VPC to Amazon SWF you must first define an _interface
VPC endpoint_ , which lets you connect your VPC to other AWS services. The
endpoint provides reliable, scalable connectivity, without requiring an
internet gateway, network address translation (NAT) instance, or VPN
connection. For more information, see [Interface VPC Endpoints (AWS
PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-
interface.html) in the _Amazon VPC User Guide_.

## Creating the Endpoint

You can create an Amazon SWF endpoint in your VPC using the AWS Management
Console, the AWS Command Line Interface (AWS CLI), an AWS SDK, the Amazon SWF
API, or AWS CloudFormation.

For information about creating and configuring an endpoint using the Amazon
VPC console or the AWS CLI, see [Creating an Interface
Endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-
interface.html#create-interface-endpoint) in the _Amazon VPC User Guide._

###### Note

When you create an endpoint, specify Amazon SWF as the service that you want
your VPC to connect to. In the Amazon VPC console, service names vary based on
the AWS Region. For example, in the AWS Top Secret - East Region, the service
name for Amazon SWF is **com.amazonaws.us-iso-east-1.swf**.

For information about creating and configuring an endpoint using AWS
CloudFormation, see the
[AWS::EC2::VPCEndpoint](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-
resource-ec2-vpcendpoint.html) resource in the _AWS CloudFormation User
Guide_.

## Amazon VPC Endpoint Policies

To control connectivity access to Amazon SWF you can attach an AWS Identity
and Access Management (IAM) endpoint policy while creating an Amazon VPC
endpoint. You can create complex IAM rules by attaching multiple endpoint
policies. For more information, see:

  * [Amazon Virtual Private Cloud Endpoint Policies for Amazon SWF](./swf-vpc-iam.html)

  * [Controlling Access to Services with VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html)

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Tag-based Policies

Endpoint Policies

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

