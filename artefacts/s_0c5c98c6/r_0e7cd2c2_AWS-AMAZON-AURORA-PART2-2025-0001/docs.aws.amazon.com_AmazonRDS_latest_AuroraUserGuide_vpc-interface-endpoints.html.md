# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/vpc-interface-endpoints.html'}

[](/pdfs/AmazonRDS/latest/AuroraUserGuide/aurora-ug.pdf#vpc-interface-
endpoints "Open PDF")

[Documentation](/index.html)[Amazon RDS](/rds/index.html)[User Guide for
Aurora](CHAP_AuroraOverview.html)

ConsiderationsAvailabilityCreating an interface VPC endpointCreating a VPC
endpoint policy

# Amazon RDS API and interface VPC endpoints (AWS PrivateLink)

You can establish a private connection between your VPC and Amazon RDS API
endpoints by creating an _interface VPC endpoint_. Interface endpoints are
powered by [AWS PrivateLink](https://aws.amazon.com/privatelink).

AWS PrivateLink enables you to privately access Amazon RDS API operations
without an internet gateway, NAT device, VPN connection, or AWS Direct Connect
connection. DB instances in your VPC don't need public IP addresses to
communicate with Amazon RDS API endpoints to launch, modify, or terminate DB
instances and DB clusters. Your DB instances also don't need public IP
addresses to use any of the available RDS API operations. Traffic between your
VPC and Amazon RDS doesn't leave the Amazon network.

Each interface endpoint is represented by one or more elastic network
interfaces in your subnets. For more information on elastic network
interfaces, see [Elastic network
interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-
eni.html) in the _Amazon EC2 User Guide._

For more information about VPC endpoints, see [Interface VPC endpoints (AWS
PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-
interface.html) in the _Amazon VPC User Guide_. For more information about RDS
API operations, see [Amazon RDS API
Reference](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/).

You don't need an interface VPC endpoint to connect to a DB cluster. For more
information, see [Scenarios for accessing a DB cluster in a
VPC](./USER_VPC.Scenarios.html).

## Considerations for VPC endpoints

Before you set up an interface VPC endpoint for Amazon RDS API endpoints,
ensure that you review [Interface endpoint properties and
limitations](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-
interface.html#vpce-interface-limitations) in the _Amazon VPC User Guide_.

All RDS API operations relevant to managing Amazon Aurora resources are
available from your VPC using AWS PrivateLink.

VPC endpoint policies are supported for RDS API endpoints. By default, full
access to RDS API operations is allowed through the endpoint. For more
information, see [Controlling access to services with VPC
endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-
access.html) in the _Amazon VPC User Guide_.

## Availability

Amazon RDS API currently supports VPC endpoints in the following AWS Regions:

  * US East (Ohio)

  * US East (N. Virginia)

  * US West (N. California)

  * US West (Oregon)

  * Africa (Cape Town)

  * Asia Pacific (Hong Kong)

  * Asia Pacific (Mumbai)

  * Asia Pacific (Osaka)

  * Asia Pacific (Seoul)

  * Asia Pacific (Singapore)

  * Asia Pacific (Sydney)

  * Asia Pacific (Tokyo)

  * Canada (Central)

  * Canada West (Calgary)

  * China (Beijing)

  * China (Ningxia)

  * Europe (Frankfurt)

  * Europe (Zurich)

  * Europe (Ireland)

  * Europe (London)

  * Europe (Paris)

  * Europe (Stockholm)

  * Europe (Milan)

  * Israel (Tel Aviv)

  * Middle East (Bahrain)

  * South America (SÃ£o Paulo)

  * AWS GovCloud (US-East)

  * AWS GovCloud (US-West)

## Creating an interface VPC endpoint for Amazon RDS API

You can create a VPC endpoint for the Amazon RDS API using either the Amazon
VPC console or the AWS Command Line Interface (AWS CLI). For more information,
see [Creating an interface
endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-
interface.html#create-interface-endpoint) in the _Amazon VPC User Guide_.

Create a VPC endpoint for Amazon RDS API using the service name
`com.amazonaws.`region`.rds`.

Excluding AWS Regions in China, if you enable private DNS for the endpoint,
you can make API requests to Amazon RDS with the VPC endpoint using its
default DNS name for the AWS Region, for example `rds.us-
east-1.amazonaws.com`. For the China (Beijing) and China (Ningxia) AWS
Regions, you can make API requests with the VPC endpoint using `rds-api.cn-
north-1.amazonaws.com.cn` and `rds-api.cn-northwest-1.amazonaws.com.cn`,
respectively.

For more information, see [Accessing a service through an interface
endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-
interface.html#access-service-though-endpoint) in the _Amazon VPC User Guide_.

## Creating a VPC endpoint policy for Amazon RDS API

You can attach an endpoint policy to your VPC endpoint that controls access to
Amazon RDS API. The policy specifies the following information:

  * The principal that can perform actions.

  * The actions that can be performed.

  * The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC
endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-
access.html) in the _Amazon VPC User Guide_.

###### Example: VPC endpoint policy for Amazon RDS API actions

The following is an example of an endpoint policy for Amazon RDS API. When
attached to an endpoint, this policy grants access to the listed Amazon RDS
API actions for all principals on all resources.

    
    
    {
       "Statement":[
          {
             "Principal":"*",
             "Effect":"Allow",
             "Action":[
                "rds:CreateDBInstance",
                "rds:ModifyDBInstance",
                "rds:CreateDBSnapshot"
             ],
             "Resource":"*"
          }
       ]
    }

###### Example: VPC endpoint policy that denies all access from a specified
AWS account

The following VPC endpoint policy denies AWS account `123456789012` all access
to resources using the endpoint. The policy allows all actions from other
accounts.

    
    
    {
      "Statement": [
        {
          "Action": "*",
          "Effect": "Allow",
          "Resource": "*",
          "Principal": "*"
        },
        {
          "Action": "*",
          "Effect": "Deny",
          "Resource": "*",
          "Principal": { "AWS": [ "123456789012" ] }
         }
       ]
    }

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Infrastructure security

Security best practices

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

