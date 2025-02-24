# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-vpc-endpoints.html'}

[](/pdfs/autoscaling/ec2/userguide/as-dg.pdf#ec2-auto-scaling-vpc-endpoints
"Open PDF")

[Documentation](/index.html)[Auto Scaling](/autoscaling/index.html)[User
Guide](what-is-amazon-ec2-auto-scaling.html)

Create an interface VPC endpointCreate a VPC endpoint policy

# Amazon EC2 Auto Scaling and interface VPC endpoints

You can improve the security posture of your VPC by configuring Amazon EC2
Auto Scaling to use an interface VPC endpoint. Interface endpoints are powered
by AWS PrivateLink, a technology that enables you to privately access Amazon
EC2 Auto Scaling APIs by restricting all network traffic between your VPC and
Amazon EC2 Auto Scaling to the AWS network. With interface endpoints, you also
don't need an internet gateway, a NAT device, or a virtual private gateway.

You are not required to configure AWS PrivateLink, but it's recommended. For
more information about AWS PrivateLink and VPC endpoints, see [What is AWS
PrivateLink?](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-
privatelink.html) in the _AWS PrivateLink Guide_.

###### Topics

  * Create an interface VPC endpoint
  * Create a VPC endpoint policy 

## Create an interface VPC endpoint

Create an endpoint for Amazon EC2 Auto Scaling using the following service
name:

    
    
    com.amazonaws.region.autoscaling

For more information, see [Access an AWS service using an interface VPC
endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-
endpoint.html) in the _AWS PrivateLink Guide_.

You do not need to change any Amazon EC2 Auto Scaling settings. Amazon EC2
Auto Scaling calls other AWS services using either service endpoints or
private interface VPC endpoints, whichever are in use.

## Create a VPC endpoint policy

You can attach a policy to your VPC endpoint to control access to the Amazon
EC2 Auto Scaling API. The policy specifies:

  * The principal that can perform actions.

  * The actions that can be performed.

  * The resource on which the actions can be performed.

The following example shows a VPC endpoint policy that denies everyone
permission to delete a scaling policy through the endpoint. The example policy
also grants everyone permission to perform all other actions.

    
    
    {
       "Statement": [
            {
                "Action": "*",
                "Effect": "Allow",
                "Resource": "*",
                "Principal": "*"
            },
            {
                "Action": "autoscaling:DeleteScalingPolicy",
                "Effect": "Deny",
                "Resource": "*",
                "Principal": "*"
            }
        ]
    }

For more information, see [Control access to VPC endpoints using endpoint
policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-
access.html) in the _AWS PrivateLink Guide_.

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Compliance validation

Working with AWS SDKs

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

