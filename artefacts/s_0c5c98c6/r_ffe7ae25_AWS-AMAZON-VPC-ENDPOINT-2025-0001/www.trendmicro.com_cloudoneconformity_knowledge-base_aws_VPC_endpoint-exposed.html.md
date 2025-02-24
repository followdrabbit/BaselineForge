# Processed Content from URL: {'REFERENCE': 'https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/endpoint-exposed.html'}

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
  * VPC Endpoint Exposed

# VPC Endpoint Exposed

Trend Cloud Oneâ¢ â Conformity is a continuous assurance tool that provides
peace of mind for your cloud infrastructure, delivering over 1000 automated
best practice checks.

[ Start a Free Trial  ](https://cloudone.trendmicro.com/SignUp.screen?) [
Product Feature  ](https://www.trendmicro.com/cloudone-conformity)

Risk Level: Medium (should be achieved)

Rule ID: VPC-005

Identify fully accessible Amazon VPC endpoints and update their access policy
in order to stop any unsigned requests initiated for the supported AWS cloud
services and resources.

This rule can help you with the following compliance standards:

  * PCI 
  * GDPR 
  * APRA 
  * MAS 
  * NIST4 

For further details on compliance standards supported by Conformity, see
[here](https://cloudone.trendmicro.com/docs/conformity/compliance-and-
conformity/ "Compliance And Conformity").

This rule can help you work with the [AWS Well-Architected
Framework](https://www.trendmicro.com/cloud-architecture "What is the Well-
Architected Framework").

This rule resolution is part of the Conformity [Security & Compliance tool for
AWS](https://www.trendmicro.com/cloud-one-conformity "Conformity product
features for AWS").

![security](/cloudoneconformity/assets/v2/images/icons/security.svg?1740361707617976185)
Security

When the "Principal" element value is set to "*" within the VPC endpoint
access policy, the endpoint allows full access (i.e. allow access by any user
or service within the VPC using credentials from any AWS accounts to any
resources in this AWS service). Allowing access in this manner is considered a
bad practice and can lead to data exposure, data loss and/or unexpected
charges on your AWS bill.

* * *

### Audit

To determine if your Amazon VPC endpoints are exposed to everyone, perform the
following operations:

#### Using AWS Console

01 Sign in to the AWS Management Console.

02 Navigate to Amazon VPC console at <https://console.aws.amazon.com/vpc/>.

03 In the navigation panel, under **VIRTUAL PRIVATE CLOUD** , choose
**Endpoints**.

04 Select the Amazon VPC endpoint that you want to examine.

05 Select the **Policy** tab from the console bottom panel and choose **Edit
Policy**.

06 On the **Edit Policy** page, within the **Policy** section, verify the set
of permissions configured for the selected VPC endpoint. If the **Policy** is
set to **Full Access** , the selected Amazon VPC endpoint is exposed to
everyone. Also, if the **Policy** is set to **Custom** but the **"Principal"**
element value is set to **"*"** or **{ "AWS": "*" }** , and the custom policy
is not using any **"Condition"** clauses to filter the access, the selected
Amazon VPC endpoint is fully exposed.

07 Repeat steps no. 4 â 6 for other Amazon VPC endpoint available within the
current AWS region.

08 Change the AWS cloud region from the navigation bar and repeat the Audit
process for other regions.

#### Using AWS CLI

01 Run **describe-vpc-endpoints** command (OSX/Linux/UNIX) with custom query
filters to list the ID of each VPC endpoint deployed in the selected AWS
region:

    
    
    aws ec2 describe-vpc-endpoints
      --region us-east-1
      --output table
      --query 'VpcEndpoints[*].VpcEndpointId'
    

02 The command output should return the requested VPC endpoint ID(s):

    
    
    ----------------------------
    |   DescribeVpcEndpoints   |
    +--------------------------+
    |  vpce-0abcd1234abcd1234  |
    |  vpce-01234abcd1234abcd  |
    +--------------------------+
    

03 Run **describe-vpc-endpoints** command (OSX/Linux/UNIX) using the ID of the
VPC endpoint that you want to examine as the identifier parameter and custom
query filters to describe the access policy defined for the selected endpoint:

    
    
    aws ec2 describe-vpc-endpoints
      --region us-east-1
      --vpc-endpoint-ids vpce-0abcd1234abcd1234
      --query 'VpcEndpoints[*].PolicyDocument'
    

04 The command output should return the VPC endpoint policy document in JSON
format:

    
    
    {
      "Statement": [
          {
              "Action": "*",
              "Effect": "Allow",
              "Resource": "arn:aws:s3:::cc-internal-bucket/*",
              "Principal": "*"
          }
      ]
    }
    

  
If the **"Principal"** element value is set to **"*"** or **{ "AWS": "*" }** ,
and the custom policy is not using any **"Condition"** clauses to filter the
access, the selected Amazon VPC endpoint is fully accessible.

05 Repeat steps no. 3 and 4 for other Amazon VPC endpoint available in the
selected AWS region.

06 Change the AWS cloud region by updating the **\--region** command parameter
value and repeat the Audit process for other regions.

### Remediation / Resolution

To restrict access for your exposed Amazon VPC endpoints, perform the
following operations:

#### Using AWS CloudFormation

01 CloudFormation template (JSON):

    
    
    {
      "AWSTemplateFormatVersion": "2010-09-09",
      "Description": "Restrict Access via Access Control Policy (Allow Access from Trusted Entities Only)",
      "Resources": {
        "AWSVPCNetwork": {
          "Type": "AWS::EC2::VPC",
          "Properties": {
            "CidrBlock": "10.0.0.0/16",
            "EnableDnsHostnames": true,
            "EnableDnsSupport": true,
            "InstanceTenancy": "default"
          }
        },
        "S3GatewayEndpoint": {
          "Type": "AWS::EC2::VPCEndpoint",
          "Properties": {
            "VpcId": {
              "Ref": "AWSVPCNetwork"
            },
            "ServiceName": {
              "Fn::Sub": "com.amazonaws.${AWS::Region}.s3"
            },
            "VpcEndpointType": "Gateway",
            "PolicyDocument": {
              "Version": "2012-10-17",
              "Statement": [
                {
                  "Effect": "Allow",
                  "Principal": {
                    "AWS": [
                      "arn:aws:iam::123456789012:user/cc-s3-manager"
                    ]
                  },
                  "Action": "*",
                  "Resource": [
                    "arn:aws:s3:::cc-internal-bucket/*"
                  ]
                }
              ]
            }
          }
        }
      }
    }
    

02 CloudFormation template (YAML):

    
    
    AWSTemplateFormatVersion: '2010-09-09'
    Description: Restrict Access via Access Control Policy (Allow Access from Trusted
      Entities Only)
    Resources:
      AWSVPCNetwork:
        Type: AWS::EC2::VPC
        Properties:
          CidrBlock: 10.0.0.0/16
          EnableDnsHostnames: true
          EnableDnsSupport: true
          InstanceTenancy: default
      S3GatewayEndpoint:
        Type: AWS::EC2::VPCEndpoint
        Properties:
          VpcId: !Ref 'AWSVPCNetwork'
          ServiceName: !Sub 'com.amazonaws.${AWS::Region}.s3'
          VpcEndpointType: Gateway
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Principal:
                  AWS:
                    - arn:aws:iam::123456789012:user/cc-s3-manager
                Action: '*'
                Resource:
                  - arn:aws:s3:::cc-internal-bucket/*
    

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
      region  = "us-east-1"
    }
    
    resource "aws_vpc" "aws-vpc-network" {
      cidr_block = "10.0.0.0/16"
      enable_dns_hostnames = true
      enable_dns_support = true
      instance_tenancy = "default"
    }
    
    resource "aws_vpc_endpoint" "s3-gateway-endpoint" {
    
      vpc_id = aws_vpc.aws-vpc-network.id
      service_name = "com.amazonaws.us-east-1.s3"
      vpc_endpoint_type = "Gateway"
    
      # Restrict Access via Access Control Policy (Allow Access from Trusted Entities Only)
      policy = jsonencode({
        "Version" : "2012-10-17",
        "Statement": [
          {
            "Effect": "Allow",
            "Principal": {
              "AWS": [
                "arn:aws:iam::123456789012:user/cc-s3-manager"
              ]
            },
            "Action": "*",
            "Resource": [
              "arn:aws:s3:::cc-internal-bucket/*"
            ]
          }
        ]
      })
    
    }
    

#### Using AWS Console

01 Sign in to the AWS Management Console.

02 Navigate to Amazon VPC console at <https://console.aws.amazon.com/vpc/>.

03 In the navigation panel, under **VIRTUAL PRIVATE CLOUD** , choose
**Endpoints**.

04 Select the Amazon VPC endpoint that you want to reconfigure.

05 Select the **Policy** tab from the console bottom panel and choose **Edit
Policy**.

06 On the **Edit Policy** page, in the **Policy** section, select **Custom**
and update the VPC endpoint policy by performing one of the following actions:

  1. Replace the "Everyone" grantee (i.e. **'*'** or **{ "AWS": "*" }**) from the **"Principal"** element value with an AWS account ID (e.g. 123456789012), an AWS account ARN (e.g. arn:aws:iam::123456789012:root), or an IAM user ARN (e.g. arn:aws:iam::123456789012:user/cc-vpce-manager). Choose **Save** to apply the policy changes.
  2. Add a **"Condition"** clause to the policy statement to filter the endpoint access to specific, trusted entities. Choose **Save** to apply the changes. 

07 Repeat steps no. 4 â 6 to update the access policy for other VPC
endpoints available within the current AWS region.

08 Change the AWS cloud region from the console navigation bar and repeat the
Remediation process for other regions.

#### Using AWS CLI

01 Edit your VPC endpoint access policy and restrict access to specific,
trusted entities only. Save the updated policy document to a JSON file named
**cc-vpce-access-policy.json**. The following example describes a policy
document that grants access to an IAM user identified by the ARN
arn:aws:iam::123456789012:user/cc-vpce-manager to perform any actions on the
services supported by the selected VPC endpoint:

    
    
    {
      "Id": "VPCEndpointAccessPolicy",
      "Version": "2012-10-17",
      "Statement": [
        {
          "Action": "*",
          "Effect": "Allow",
          "Resource": "arn:aws:s3:::cc-internal-bucket/*",
          "Principal": {
            "AWS": [
              "arn:aws:iam::123456789012:user/cc-s3-manager"
            ]
          }
        }
      ]
    }
    

02 Run **modify-vpc-endpoint** command (OSX/Linux/UNIX) using the ID of the
VPC endpoint that you want to reconfigure as the identifier parameter, to
replace the existing endpoint policy with the one defined at the previous
step, i.e. **cc-vpce-access-policy.json** :

    
    
    aws ec2 modify-vpc-endpoint
      --region us-east-1
      --vpc-endpoint-id vpce-0abcd1234abcd1234
      --policy-document file://cc-vpce-access-policy.json
    

03 The command output should return **true** if the command request succeeds,
otherwise it should return an error:

    
    
    {
        "Return": true
    }
    

04 Repeat steps no. 1 â 3 to update the access policy for other VPC
endpoints available in the selected AWS region.

05 Change the AWS cloud region by updating the **\--region** command parameter
value and repeat the Remediation process for other AWS regions.

### References

  * AWS Documentation
  * [Amazon VPC FAQs](https://aws.amazon.com/vpc/faqs/)
  * [AWS PrivateLink concepts](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-endpoints.html)
  * [Identity and access management for Amazon VPC](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_IAM.html)
  * [AWS Policy Generator](https://awspolicygen.s3.amazonaws.com/policygen.html)

  * AWS Blog
  * [New â VPC Endpoint for Amazon S3](https://aws.amazon.com/blogs/aws/new-vpc-endpoint-for-amazon-s3/)

  * AWS Command Line Interface (CLI) Documentation
  * [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html)
  * [describe-vpc-endpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-endpoints.html)
  * [modify-vpc-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpc-endpoint.html)

  * CloudFormation Documentation
  * [AWS::EC2::VPCEndpoint](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html)

  * Terraform Documentation
  * [AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)

Publication date Jan 7, 2017

### Related VPC rules

  * [ Unrestricted Inbound Traffic on Remote Server Administration Ports (Security) ](/cloudoneconformity/knowledge-base/aws/VPC/acl-inbound-access-on-admin-ports.html "Unrestricted Inbound Traffic on Remote Server Administration Ports")
  * [ VPC Endpoint Cross Account Access (Security) ](/cloudoneconformity/knowledge-base/aws/VPC/endpoint-cross-account-access.html "VPC Endpoint Cross Account Access")
  * [ Unrestricted Network ACL Outbound Traffic (Security) ](/cloudoneconformity/knowledge-base/aws/VPC/network-acl-outbound-traffic-all-ports.html "Unrestricted Network ACL Outbound Traffic")
  * [ Ineffective Network ACL DENY Rules (Security) ](/cloudoneconformity/knowledge-base/aws/VPC/network-acl-deny-rules.html "Ineffective Network ACL DENY Rules")

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

