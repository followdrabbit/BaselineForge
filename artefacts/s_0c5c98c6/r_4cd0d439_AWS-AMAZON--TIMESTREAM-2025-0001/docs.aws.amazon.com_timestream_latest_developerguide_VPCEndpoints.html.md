# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/timestream/latest/developerguide/VPCEndpoints.html'}

[](/pdfs/timestream/latest/developerguide/timestream.pdf#VPCEndpoints "Open
PDF")

[Documentation](/index.html)[Amazon
Timestream](/timestream/index.html)[Developer Guide](what-is-timestream.html)

# VPC endpoints (AWS PrivateLink)

You can establish a private connection between your VPC and Amazon Timestream
for LiveAnalytics by creating an _interface VPC endpoint_. Interface endpoints
are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink), a
technology that enables you to privately access Timestream for LiveAnalytics
APIs without an internet gateway, NAT device, VPN connection, or AWS Direct
Connect connection. Instances in your VPC don't need public IP addresses to
communicate with Timestream for LiveAnalytics APIs. Traffic between your VPC
and Timestream for LiveAnalytics does not leave the Amazon network.

Each interface endpoint is represented by one or more [Elastic Network
Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-
eni.html) in your subnets. For more information on Interface VPC endpoints,
see [Interface VPC endpoints (AWS
PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-
interface.html) in the _Amazon VPC User Guide_.

To get started with Timestream for LiveAnalytics and VPC endpoints, we've
provided information on specific considerations for Timestream for
LiveAnalytics with VPC endpoints, creating an interface VPC endpoint for
Timestream for LiveAnalytics, creating a VPC endpoint policy for Timestream
for LiveAnalytics, and using the Timestream client (for either the Write or
Query SDK) with VPC endpoints..

###### Topics

  * [How VPC endpoints work with Timestream](./VPCEndpoints.vpc-endpoint-considerations.html)
  * [Creating an interface VPC endpoint for Timestream for LiveAnalytics](./VPCEndpoints.vpc-endpoint-create.html)
  * [Creating a VPC endpoint policy for Timestream for LiveAnalytics](./VPCEndpoints.vpc-endpoint-policy.html)

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Incident response

How VPC endpoints work with Timestream

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

