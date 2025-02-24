# Processed Content from URL: {'REFERENCE': 'https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/vpc-endpoints-in-use.html'}

  * [ Sign In ](https://www.cloudconformity.com/identity/sign-in.html)
  * [ Buy ](https://aws.amazon.com/marketplace/pp/prodview-g232pyu6l55l4?applicationId=AWSMPContessa)
  * [ Free Trial  ](https://cloudone.trendmicro.com/SignUp.screen?)

* * *

[ ![Logo of Trend
Micro](/cloudoneconformity/assets/v2/images/common/logo.svg?1740361707617976185)
](https://trendmicro.com/cloudoneconformity/)

  * Knowledge Base 

    * [ AWS ](/cloudoneconformity/knowledge-base/aws/)
    * [ Azure ](/cloudoneconformity/knowledge-base/azure/)
    * [ GCP ](/cloudoneconformity/knowledge-base/gcp/)
    * [ Conformity ](/cloudoneconformity/knowledge-base/cloudconformity/)
    * [ Alibaba Cloud ](/cloudoneconformity/knowledge-base/alibaba-cloud/)

  * Products 

    * [ Cloud Oneâ¢ - Conformity ](https://www.trendmicro.com/cloudone-conformity)
    * [ All Cloud Oneâ¢ Services ](https://www.trendmicro.com/hybridcloud)

  * [ Help  ](https://cloudone.trendmicro.com/docs/conformity/)
  * 

  * Knowledge Base 

    * [ AWS  ](/cloudoneconformity/knowledge-base/aws/)
    * [ Azure  ](/cloudoneconformity/knowledge-base/azure/)
    * [ GCP  ](/cloudoneconformity/knowledge-base/gcp/)
    * [ Conformity  ](/cloudoneconformity/knowledge-base/cloudconformity/)
    * [ Alibaba Cloud  ](/cloudoneconformity/knowledge-base/alibaba-cloud/)

  * Products 

    * [ Cloud Oneâ¢ - Conformity  ](https://www.trendmicro.com/cloudone-conformity)
    * [ All Cloud Oneâ¢ Services  ](https://www.trendmicro.com/hybridcloud)

  * [ Help  ](https://cloudone.trendmicro.com/docs/conformity/)

  * [ Sign In  ](https://www.cloudconformity.com/identity/sign-in.html)
  * [ Buy  ](https://aws.amazon.com/marketplace/pp/prodview-g232pyu6l55l4?applicationId=AWSMPContessa)
  * [ Free Trial  ](https://cloudone.trendmicro.com/SignUp.screen?)

Use the Conformity Knowledge Base AI to help improve your Cloud Posture [ ð¬
Conformity Knowledge Base AI >
](https://www.trendmicro.com/cloudoneconformity/ai-assistant-kb.html)

  * [Knowledge Base](/knowledge-base/ "Best practice knowledge base homepage")
  * [Amazon Web Services](/cloudoneconformity/knowledge-base/aws/ "Best practice knowledge base for Amazon Web Services")
  * [Amazon Virtual Private Cloud (VPC)](/cloudoneconformity/knowledge-base/aws/VPC/ "Knowledge Base for Amazon Virtual Private Cloud \(VPC\)")
  * VPC Endpoints In Use

# VPC Endpoints In Use

Trend Cloud Oneâ¢ â Conformity is a continuous assurance tool that provides
peace of mind for your cloud infrastructure, delivering over 1000 automated
best practice checks.

[ Start a Free Trial  ](https://cloudone.trendmicro.com/SignUp.screen?) [
Product Feature  ](https://www.trendmicro.com/cloudone-conformity)

Risk Level: Medium (should be achieved)

Rule ID: VPC-016

Ensure that your Amazon Virtual Private Cloud (VPC) endpoints are being used
to allow you to securely connect your VPC to other AWS cloud services without
the need of an Internet Gateway (IGW), NAT device, VPN connection, or an AWS
Direct Connect connection. A VPC endpoint is a virtual device which is
horizontally scaled, redundant and highly available, that provides
communication between EC2 instances within your Virtual Private Cloud (VPC)
and other supported AWS services without introducing availability risks or
bandwidth constraints on your network traffic. The Amazon EC2 instances
available in your VPC do not require public IP addresses and the traffic
between these resources and the supported services does not leave the AWS
cloud network. There are two types of VPC endpoints that you can use based on
the AWS service supported â interface endpoints and gateway endpoints:  

  1. Interface endpoints use Elastic Network Interfaces (ENIs) with private IP addresses that are powered by AWS PrivateLink â a highly available and scalable technology that privately connects your VPC to supported AWS services, services hosted by other AWS accounts (also known as VPC endpoint services), and supported AWS Marketplace partner services. Each ENI acts as the entry point for the traffic intended to a specific service. The following AWS services are supported: 
     * Amazon API Gateway
     * AWS CloudFormation
     * Amazon CloudWatch
     * Amazon CloudWatch Events
     * Amazon CloudWatch Logs
     * AWS CodeBuild
     * AWS Config
     * Amazon EC2 API
     * AWS Elastic Load Balancing API
     * AWS Key Management Service
     * Amazon Kinesis Data Streams
     * Amazon SageMaker Runtime
     * AWS Secrets Manager
     * AWS Security Token Service
     * AWS Service Catalog
     * Amazon SNS
     * AWS Systems Manager
     * Endpoint services hosted by other AWS accounts
     * Supported AWS Marketplace partner services
  2. Gateway endpoints are gateways targeted for specific routes within the VPC route tables and used for traffic intended to supported services. The following AWS cloud services are supported:
     * Amazon DynamoDB
     * Amazon S3

This rule resolution is part of the Conformity [Security & Compliance tool for
AWS](https://www.trendmicro.com/cloud-one-conformity "Conformity product
features for AWS").

![security](/cloudoneconformity/assets/v2/images/icons/security.svg?1740361707617976185)
Security

Amazon VPC endpoints enable you to privately access specific AWS services from
your own Virtual Private Cloud (VPC), without using public IP addresses and
without requiring the traffic data to travel across the Internet.

Note: VPC endpoints are only supported within the same AWS cloud region. You
can't use VPC endpoints to connect an AWS service from one region to a VPC in
a different region.

* * *

### Audit

To determine if your VPC endpoints are being used within your AWS cloud
account, perform the following operations:

#### Using AWS Console

01 Sign in to the AWS Management Console.

02 Navigate to Amazon VPC console at <https://console.aws.amazon.com/vpc/>.

03 Select the Virtual Private Cloud (VPC) that you want to examine from the
**Select a VPC** dropdown menu.

04 In the navigation panel, under **VIRTUAL PRIVATE CLOUD** , choose
**Endpoints**.

05 On the VPC endpoints listing page, check for any Amazon VPC endpoints
available in the current AWS region. If there are no VPC endpoints listed on
this page, instead the following message is displayed: "**You do not have any
Endpoints in this region.** ", there are no VPC endpoints deployed for the
selected Amazon VPC network, within the current AWS region.

06 Repeat steps no. 3 â 5 for other Virtual Private Clouds (VPCs) available
in the current AWS region.

07 Change the AWS cloud region from the navigation bar and repeat the Audit
process for other regions.

#### Using AWS CLI

01 Run **describe-vpcs** command (OSX/Linux/UNIX) to list the ID of each VPC
networks available within the current AWS region:

    
    
    aws ec2 describe-vpcs
      --region us-east-1
      --output table --query 'Vpcs[*].VpcId'
    

02 The command output should return a table with the requested VPC ID(s):

    
    
    ------------------
    |  DescribeVpcs  |
    +----------------+
    |  vpc-abcd1234  |
    |  vpc-1234abcd  |
    +----------------+
    

03 Run **describe-vpc-endpoints** command (OSX/Linux/UNIX) using the ID of the
VPC network that you want to examine as the identifier parameter and custom
query filters to describe the identifiers of the VPC endpoints created for the
selected VPC:

    
    
    aws ec2 describe-vpc-endpoints
      --region us-east-1
      --filters Name=vpc-id,Values=vpc-abcd1234
      --query 'VpcEndpoints[*].VpcEndpointId'
    

04 The command output should return the requested VPC endpoint ID(s):

    
    
    []
    

  
If the **describe-vpc-endpoints** command returns an empty array (i.e.
**[]**), as shown in the output example above, there are no Amazon VPC
endpoints deployed for the selected VPC network, within the selected AWS
region.

05 Repeat steps no. 3 and 4 for other Virtual Private Clouds (VPCs) available
in the selected AWS region.

06 Change the AWS cloud region by updating the **\--region** command parameter
value and repeat the Audit process for other regions.

### Remediation / Resolution

A VPC endpoint enables you to connect with particular AWS cloud services that
are outside your VPC network through a private link. To deploy and configure a
VPC endpoint within your AWS account, perform the following operations:

_Note: As an example, this conformity rule demonstrates how to create an
interface VPC endpoint between a Virtual Private Cloud and the Elastic Load
Balancing (ELB) service within the US East region. An interface endpoint is an
Elastic Network Interface (ENI) that serves as an endpoint for communicating
with a specified AWS service (in this case Amazon ELB). You can specify the
subnet in which to create the endpoint and the security group(s) to associate
with the endpoint network interface._

#### Using AWS CloudFormation

01 CloudFormation template (JSON):

    
    
    {
    	"AWSTemplateFormatVersion": "2010-09-09",
    	"Resources": {
    		"NLB": {
    			"Type": "AWS::ElasticLoadBalancingV2::LoadBalancer",
    			"Properties": {
    				"Name": "cc-network-load-balancer",
    				"Type": "network",
    				"Scheme": "internet-facing",
    				"IpAddressType": "ipv4",
    				"Subnets": [
    					"subnet-01234abcd1234abcd",
    					"subnet-0abcd1234abcd1234"
    				]
    			}
    		},
    		"NLBListener": {
    			"Type": "AWS::ElasticLoadBalancingV2::Listener",
    			"Properties": {
    				"DefaultActions": [
    					{
    						"Type": "redirect",
    						"RedirectConfig": {
    							"Protocol": "HTTPS",
    							"Port": 443,
    							"Host": "#{host}",
    							"Path": "/#{path}",
    							"Query": "#{query}",
    							"StatusCode": "HTTP_301"
    						}
    					}
    				],
    				"LoadBalancerArn": {
    					"Ref": "NLB"
    				},
    				"Port": 80,
    				"Protocol": "HTTP"
    			}
    		}
    	},
    	"VPCEndpoint": {
    		"Type": "AWS::EC2::VPCEndpointService",
    		"Properties": {
    			"NetworkLoadBalancerArns": [
    				{
    					"Ref": "NLB"
    				}
    			]
    		}
    	}
    }
    

02 CloudFormation template (YAML):

    
    
    AWSTemplateFormatVersion: '2010-09-09'
    	Resources:
    	NLB:
    		Type: AWS::ElasticLoadBalancingV2::LoadBalancer
    		Properties:
    		Name: cc-network-load-balancer
    		Type: network
    		Scheme: internet-facing
    		IpAddressType: ipv4
    		Subnets:
    			- subnet-01234abcd1234abcd
    			- subnet-0abcd1234abcd1234
    	NLBListener:
    		Type: AWS::ElasticLoadBalancingV2::Listener
    		Properties:
    		DefaultActions:
    			- Type: redirect
    			RedirectConfig:
    				Protocol: HTTPS
    				Port: 443
    				Host: '#{host}'
    				Path: /#{path}
    				Query: '#{query}'
    				StatusCode: HTTP_301
    		LoadBalancerArn: !Ref 'NLB'
    		Port: 80
    		Protocol: HTTP
    	VPCEndpoint:
    	Type: AWS::EC2::VPCEndpointService
    	Properties:
    		NetworkLoadBalancerArns:
    		- !Ref 'NLB'
    

#### Using Terraform ([AWS
Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs))

01 Terraform configuration file (.tf):

    
    
    terraform {
    	required_providers {
    		aws = {
    			source  = "hashicorp/aws"
    			version = "~> 4.0"
    		}
    	}
    
    	required_version = ">= 0.14.9"
    }
    
    provider "aws" {
    	profile = "default"
    	region  = "us-east-1"
    }
    
    resource "aws_lb" "network-load-balancer" {
    	name               = "cc-network-load-balancer"
    	load_balancer_type = "network"
    	internal           = false
    	ip_address_type    = "ipv4"
    	subnets            = ["subnet-01234abcd1234abcd","subnet-0abcd1234abcd1234"]
    }
    
    resource "aws_lb_listener" "nlb-listener" {
    	load_balancer_arn = aws_lb.network-load-balancer.arn
    	port              = "80"
    	protocol          = "HTTP"
    	default_action {
    		type = "redirect"
    		redirect {
    			port        = "443"
    			protocol    = "HTTPS"
    			status_code = "HTTP_301"
    		}
    	}
    }
    
    resource "aws_vpc_endpoint_service" "vpc-endpoint-service" {
    	network_load_balancer_arns = [aws_lb.network-load-balancer.arn]
    }
    

#### Using AWS Console

01 Sign in to the AWS Management Console.

02 Navigate to Amazon VPC console at <https://console.aws.amazon.com/vpc/>.

03 Select the Virtual Private Cloud (VPC) that you want to access from the
**Select a VPC** dropdown menu.

04 In the navigation panel, under **VIRTUAL PRIVATE CLOUD** , choose
**Endpoints**.

05 Choose **Create Endpoint** to initiate the VPC endpoint setup process.

06 On the **Create Endpoint** setup page, perform the following actions:

  1. For **Service category** , choose **AWS services** to get the list with the AWS cloud services supported in the selected region.
  2. Select the AWS service that the new endpoint will connect to, in this case **com.amazonaws.us-east-1.elasticloadbalancing** , from the **Service Name** list.
  3. For **VPC** , select the ID of the VPC network for which you want to create your new endpoint.
  4. For **Subnets** , select the Availability Zones (AZs) and the associated subnets in which to create your new VPC endpoint network interfaces.
  5. For **Enable DNS name** , choose whether or not to associate a private hosted zone with the VPC network selected at step c.
  6. For **Security group** , click on the **Select security groups** button to list the security groups available in the current AWS region and select one or more security groups for your new endpoint. If you want to set up a new security group, choose **Create a new security group**.
  7. For **Policy*** , choose whether to allow full access or to create a custom policy. A VPC endpoint policy controls access to the associated AWS service(s).
  8. (Optional) Use the **Add Tag** button to apply one or more tag sets to your VPC endpoint.
  9. Choose **Create endpoint** to deploy your new Amazon VPC endpoint within the selected AWS cloud region.

07 If required, repeat step no. 5 and 6 to deploy more interface endpoints
within the selected VPC network.

08 If required, repeat steps no. 3 â 7 for other Virtual Private Clouds
(VPCs) available in the current AWS region.

09 Change the AWS cloud region from the navigation bar and repeat the Audit
process for other regions.

#### Using AWS CLI

01 Run **create-vpc-endpoint** command (OSX/Linux/UNIX) to create a new
interface VPC endpoint. The following command example creates an Amazon VPC
endpoint between a VPC network identified by the ID vpc-abcd1234 and the
Elastic Load Balancing (ELB) service within the US East (N. Virginia) region.
The endpoint is created within a VPC subnet identified by the ID
subnet-12341234, and is associated with a security group identified by the ID
sg-0abcd1234abcd1234:

    
    
    aws ec2 create-vpc-endpoint
      --region us-east-1
      --vpc-id vpc-abcd1234
      --vpc-endpoint-type Interface
      --service-name com.amazonaws.us-east-1.elasticloadbalancing
      --subnet-id subnet-12341234
      --security-group-id sg-0abcd1234abcd1234
    

02 The command output should return the metadata available for your new Amazon
VPC endpoint:

    
    
    {
    	"VpcEndpoint": {
    		"VpcId": "vpc-abcd1234",
    		"NetworkInterfaceIds": [
    			"eni-01234abcd1234abcd"
    		],
    		"SubnetIds": [
    			"subnet-12341234"
    		],
    		"PrivateDnsEnabled": true,
    		"State": "pending",
    		"ServiceName": "com.amazonaws.us-east-1.elasticloadbalancing",
    		"RouteTableIds": [],
    		"Groups": [
    			{
    				"GroupName": "cc-project5-sg",
    				"GroupId": "sg-0abcd1234abcd1234"
    			}
    		],
    		"VpcEndpointId": "vpce-0abcdabcdabcdabcd",
    		"VpcEndpointType": "Interface",
    		"CreationTimestamp": "2018-10-19T15:39:20.942Z",
    		"DnsEntries": [
    			{
    				"HostedZoneId": "AABBCCDDAABBC",
    				"DnsName": "elasticloadbalancing.us-east-1.amazonaws.com"
    			},
    			{
    				"HostedZoneId": "AAAABBBBCCCCD",
    				"DnsName": "vpce-0abcdabcdabcdabcd-12345678.elasticloadbalancing.us-east-1.vpce.amazonaws.com"
    			},
    			{
    				"HostedZoneId": "AAAABBBBCCCCD",
    				"DnsName": "vpce-0abcdabcdabcdabcd-12345678-us-east-1a.elasticloadbalancing.us-east-1.vpce.amazonaws.com"
    			}
    		]
    	}
    }
    

03 If required, repeat step no. 1 and 2 to deploy more interface endpoints
within the selected VPC network.

04 If required, repeat steps no. 1 â 3 for other Virtual Private Clouds
(VPCs) available in the selected AWS region.

05 Change the AWS cloud region by updating the **\--region** command parameter
value and repeat the Remediation process for other regions.

### References

  * AWS Documentation
  * [Introducing AWS PrivateLink for AWS Services](https://aws.amazon.com/about-aws/whats-new/2017/11/introducing-aws-privatelink-for-aws-services/)
  * [What Is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
  * [VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html)
  * [VPC Endpoint Services (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-service.html)
  * [Modify the DNS attributes for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html)

  * AWS Command Line Interface (CLI) Documentation
  * [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html)
  * [describe-vpcs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpcs.html)
  * [describe-vpc-endpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-endpoints.html)
  * [create-vpc-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc-endpoint.html)

Publication date Nov 5, 2018

### Related VPC rules

  * [ VPC Naming Conventions (Security) ](/cloudoneconformity/knowledge-base/aws/VPC/vpc-naming-conventions.html "VPC Naming Conventions")
  * [ VPC Endpoints In Use (Security) ](/cloudoneconformity/knowledge-base/aws/VPC/vpc-endpoints-in-use.html "VPC Endpoints In Use")
  * [ VPC Peering Connections To Accounts Outside AWS Organization (Security) ](/cloudoneconformity/knowledge-base/aws/VPC/vpc-peering-connections-to-accounts-outside-aws-organizations.html "VPC Peering Connections To Accounts Outside AWS Organization")
  * [ Unrestricted Inbound Traffic on Remote Server Administration Ports (Security) ](/cloudoneconformity/knowledge-base/aws/VPC/acl-inbound-access-on-admin-ports.html "Unrestricted Inbound Traffic on Remote Server Administration Ports")

* * *

Whether your cloud exploration is just starting to take shape, youâre mid-
way through a migration or youâre already running complex workloads in the
cloud, Conformity offers full visibility into your overall security and
governance posture across various standards and frameworks.

##  Continuous security & compliance for cloud environments. Grow and scale
your business with confidence

[ Try it for free  ](https://cloudone.trendmicro.com/SignUp.screen?) [ Get
pricing  ](https://resources.trendmicro.com/cloud-one-conformity-pricing.html)

Products

  * [ Conformity ](https://www.trendmicro.com/cloudone-conformity)
  * [ Workload Security ](https://www.trendmicro.com/cloudone-workload)
  * [ Container Security ](https://www.trendmicro.com/cloudone-image)
  * [ File Storage Security ](https://www.trendmicro.com/cloudone-file)
  * [ Application Security ](https://www.trendmicro.com/cloudone-app)
  * [ Network Security ](https://www.trendmicro.com/cloudone-net)

Solutions For

  * [ Cloud Migration ](https://www.trendmicro.com/cloud-migration-security)
  * [ Cloud Operational Excellence ](https://www.trendmicro.com/opexcellence)
  * [ Cloud Native App Development ](https://www.trendmicro.com/nativeappdev)
  * [ Data Center Security ](https://www.trendmicro.com/security-data-center-virtualization)

Help

  * [ Help by Topic ](https://cloudone.trendmicro.com/docs/conformity/)
  * [ Help AI Assistant ](https://www.trendmicro.com/cloudoneconformity/ai-assistant-help.html)
  * [ API Documentation ](https://cloudone.trendmicro.com/docs/conformity/api-reference/)
  * [ Contact Us ](https://resources.trendmicro.com/Hybrid-Cloud-Security-Contact-Us.html)
  * [ Knowledge Base AI Assistant ](https://www.trendmicro.com/cloudoneconformity/ai-assistant-kb.html)

Company

  * [ About Us ](https://www.trendmicro.com/about)
  * [ Careers ](https://www.trendmicro.com/careers)
  * [ Newsroom ](https://www.trendmicro.com/newsroom)

Privacy and Protection

  * [ Terms and Conditions ](https://www.cloudconformity.com/terms-and-conditions.html)
  * [ Privacy Policy ](https://www.trendmicro.com/privacy)
  * [ Report a Security Vulnerability ](https://www.cloudconformity.com/responsible-disclosure.html)

[ ](https://www.facebook.com/TrendMicro/) [ ](https://twitter.com/trendmicro)
[ ](https://www.linkedin.com/company/trend-micro) [
](http://feeds.trendmicro.com/TrendMicroSimplySecurity) [
](https://www.youtube.com/user/TrendMicroInc)

Copyright Â© 2025 Trend Micro Incorporated. All rights reserved. Version
v1.188.9-383-geea80320

