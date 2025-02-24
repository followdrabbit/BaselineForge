# Processed Content from URL: {'REFERENCE': 'https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/publicly-accessible.html'}

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
  * [Amazon MQ](/cloudoneconformity/knowledge-base/aws/MQ/ "Knowledge Base for Amazon MQ")
  * Publicly Accessible MQ Brokers

# Publicly Accessible MQ Brokers

Trend Cloud Oneâ¢ â Conformity is a continuous assurance tool that provides
peace of mind for your cloud infrastructure, delivering over 1000 automated
best practice checks.

[ Start a Free Trial  ](https://cloudone.trendmicro.com/SignUp.screen?) [
Product Feature  ](https://www.trendmicro.com/cloudone-conformity)

Risk Level: Medium (should be achieved)

Rule ID: MQ-002

Ensure that the Amazon MQ brokers provisioned in your AWS account are not
publicly accessible from the Internet in order to avoid exposing sensitive
data and minimize security risks. The level of access to your MQ brokers
depends on their use cases, however, for most use cases Trend Cloud Oneâ¢ â
Conformity recommends that the MQ brokers should be privately accessible only
from within your AWS Virtual Private Cloud (VPC).

This rule can help you with the following compliance standards:

  * PCI 
  * HIPAA 
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

Public Amazon MQ brokers can be accessed directly, outside of a Virtual
Private Cloud (VPC), therefore every machine on the Internet can reach your
brokers through their public endpoints and this can increase the opportunity
for malicious activity such as cross-site scripting (XSS) and clickjacking
attacks.

* * *

### Audit

To determine if your Amazon MQ brokers are publicly accessible, perform the
following actions:

#### Using AWS Console

01 Sign in to the AWS Management Console.

02 Navigate to Amazon MQ console at <https://console.aws.amazon.com/amazon-
mq/>.

03 In the main navigation panel, under **Amazon MQ** , click **Brokers**.

04 Click on the name (link) of the MQ broker that you want to examine.

05 In the **Details** section, check the **Public accessibility** attribute
value listed under **Security and network** to determine the accessibility
mode configured for the selected MQ broker. If the attribute value is set to
**Yes** , the selected Amazon MQ broker is publicly accessible and exposed to
security risks.

06 Repeat steps no. 4 and 5 for each Amazon MQ broker available within the
current AWS region.

07 Change the AWS cloud region from the navigation bar and repeat the Audit
process for other AWS regions.

#### Using AWS CLI

01 Run **list-brokers** command (OSX/Linux/UNIX) with custom query filters to
list the ID of each Amazon MQ brokers available in the selected AWS region:

    
    
    aws mq list-brokers
      --region us-east-1
      --query 'BrokerSummaries[*].BrokerId'
    

02 The command output should return the requested MQ broker IDs:

    
    
    [
    	"b-aaaabbbb-cccc-dddd-eeee-aaaabbbbcccc",
    	"b-bbbbcccc-dddd-eeee-ffff-bbbbccccdddd"
    ]
    

03 Run **describe-broker** command (OSX/Linux/UNIX) using the ID of the Amazon
MQ broker that you want to examine as the identifier parameter, to describe
the accessibility status available for the selected MQ broker:

    
    
    aws mq describe-broker
      --region us-east-1
      --broker-id b-aaaabbbb-cccc-dddd-eeee-aaaabbbbcccc
      --query 'PubliclyAccessible'
    

04 The command output should return the requested accessibility status
(**true** for publicly accessible, **false** for privately accessible):

    
    
    true
    

  
If the **describe-broker** command output returns **true** , as shown in the
example above, the selected Amazon MQ broker is publicly accessible to the
Internet and exposed to security risks.

05 Repeat steps no. 3 and 4 for each Amazon MQ broker available in the
selected AWS region.

06 Change the AWS cloud region by updating the **\--region** command parameter
value and repeat the Audit process for other AWS regions.

### Remediation / Resolution

To disable public accessibility for your existing Amazon MQ brokers, you must
re-create your brokers with a different configuration so that the brokers
endpoints can be reachable only within your VPC. To relaunch your MQ brokers,
perform the following actions:

#### Using AWS CloudFormation

01 CloudFormation template (JSON):

    
    
    {
    	"AWSTemplateFormatVersion": "2010-09-09",
    	"Description": "Disable Public Access for MQ Brokers",
    	"Resources": {
    		"MQBroker": {
    			"Type": "AWS::AmazonMQ::Broker",
    			"Properties": {
    				"BrokerName": "cc-internal-broker",
    				"DeploymentMode": "SINGLE_INSTANCE",
    				"EngineType": "ActiveMQ",
    				"EngineVersion": "5.15.0",
    				"HostInstanceType": "mq.m5.large",
    				"AutoMinorVersionUpgrade": "true",
    				"Users": [
    					{
    						"Password": "brokeruser",
    						"Username": "brokerpassword"
    					}
    				],
    				"PubliclyAccessible": "false"
    			}
    		}
    	}
    }
    

02 CloudFormation template (YAML):

    
    
    AWSTemplateFormatVersion: '2010-09-09'
    	Description: Disable Public Access for MQ Brokers
    	Resources:
    	MQBroker:
    		Type: AWS::AmazonMQ::Broker
    		Properties:
    		BrokerName: cc-internal-broker
    		DeploymentMode: SINGLE_INSTANCE
    		EngineType: ActiveMQ
    		EngineVersion: 5.15.0
    		HostInstanceType: mq.m5.large
    		AutoMinorVersionUpgrade: 'true'
    		Users:
    			- Password: brokeruser
    			Username: brokerpassword
    		PubliclyAccessible: 'false'
    

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
    
    resource "aws_mq_broker" "mq-broker" {
    	broker_name                = "cc-internal-broker"
    	deployment_mode            = "SINGLE_INSTANCE"
    	engine_type                = "ActiveMQ"
    	engine_version             = "5.15.0"
    	host_instance_type         = "mq.m5.large"
    	auto_minor_version_upgrade = true
    
    	user {
    		username = "brokeruser"
    		password = "brokerpassword"
    	}
    
    	publicly_accessible = false
    
    }
    

#### Using AWS Console

01 Sign in to the AWS Management Console.

02 Navigate to Amazon MQ console at <https://console.aws.amazon.com/amazon-
mq/>.

03 In the main navigation panel, under **Amazon MQ** , click **Brokers**.

04 Click on the name (link) of the MQ broker that you want to re-create.

05 On the selected MQ broker page, collect the broker configuration
information such as **Broker instance type** , **Broker engine** , **Broker
engine version** , **Configuration name and revision, Security and network**
information, and **Maintenance** information, as well as the user and tagging
information available in the **Users** and **Tags** sections.

06 Navigate back to the **Brokers** listing page and choose **Create brokers**
to initiate the setup process.

07 For **Step 1 Select broker engine** , choose **Apache ActiveMQ** for the
broker engine type. Choose **Next** to continue the setup process.

08 For **Step 2 Select deployment and storage type** , select the deployment
mode and storage type for the new Amazon MQ broker. Choose **Next** to
continue the broker setup.

09 For **Step 3 Configure settings** , provide a unique name for the new
broker, and configure the required settings for your new MQ broker using the
configuration, tagging, and user information collected at step no. 5. To
restrict public access to your new Amazon MQ broker and make it accessible
only within your VPC, choose **Additional settings** , and select **Private
access** under **Access type** , in the **Network and security** section.
Choose **Next** to continue.

10 For **Step 4 Review and create** , review the broker configuration
information and choose **Create broker** to launch your new Amazon MQ broker.

11 After the new MQ broker is created, you can replace the broker endpoint(s)
within your application.

12 If required, repeat steps no. 4 â 11 to disable public accessibility for
each Amazon MQ broker available within the current AWS region.

13 Change the AWS cloud region from the navigation bar and repeat the
Remediation process for other AWS regions.

#### Using AWS CLI

01 Run **describe-broker** command (OSX/Linux/UNIX) using the ID of the Amazon
MQ broker that you want to relaunch as the identifier parameter, to describe
the configuration information for the specified MQ broker:

    
    
    aws mq describe-broker
      --region us-east-1
      --broker-id b-aaaabbbb-cccc-dddd-eeee-aaaabbbbcccc
    

02 The command output should return the configuration information available
for the selected MQ broker:

    
    
    {
    	"MaintenanceWindowStartTime": {
    		"DayOfWeek": "MONDAY",
    		"TimeZone": "UTC",
    		"TimeOfDay": "01:00"
    	},
    	"PubliclyAccessible": true,
    	"EngineVersion": "5.15.0",
    	"EngineType": "ActiveMQ",
    
    
    	...
    
    	"HostInstanceType": "mq.m5.large",
    	"SubnetIds": [
    		"subnet-0abcd1234abcd1234",
    		"subnet-01234abcd1234abcd"
    	],
    	"BrokerArn": "arn:aws:mq:us-east-1:123456789012:broker:cc-production-broker:b-aaaabbbb-cccc-dddd-eeee-aaaabbbbcccc",
    	"BrokerId": "b-aaaabbbb-cccc-dddd-eeee-aaaabbbbcccc",
    	"BrokerName": "cc-production-broker",
    	"SecurityGroups": [
    		"sg-01234abcd1234abcd"
    	]
    }
    

03 Run **create-broker** command (OSX/Linux/UNIX) using the configuration
information returned at the previous step to relaunch the selected Amazon MQ
broker and make it accessible only within the your VPC network by adding the
**\--no-publicly-accessible** parameter to the command request:

    
    
    aws mq create-broker
      --region us-east-1
      --broker-name cc-internal-production-broker
      --configuration Id="c-aaaabbbb-cccc-dddd-eeee-aaaabbbbcccc",Revision=1
      --deployment-mode SINGLE_INSTANCE
      --engine-type ACTIVEMQ
      --engine-version 5.15.0
      --host-instance-type mq.m5.large
      --security-groups "sg-01234abcd1234abcd"
      --subnet-ids "subnet-0abcd1234abcd1234"
      --users ConsoleAccess=true,Username="brokeruser",Password="brokerpasswd"
      --auto-minor-version-upgrade
      --no-publicly-accessible
    

04 The command output should return the new Amazon MQ broker identifiers
(broker ARN and ID):

    
    
    {
    	"BrokerArn": "arn:aws:mq:us-east-1:123456789012:broker:cc-ha-production-broker:b-bbbbcccc-dddd-eeee-ffff-bbbbccccdddd",
    	"BrokerId": "b-bbbbcccc-dddd-eeee-ffff-bbbbccccdddd"
    }
    

05 After the new MQ broker is created, you can replace the broker endpoint(s)
within your application.

06 If required, repeat steps no. 1 â 5 to disable public accessibility for
each Amazon MQ broker available in the selected AWS region.

07 Change the AWS region by updating the **\--region** command parameter value
and repeat steps no. 1 â 6 to perform the Remediation process for other
regions.

### References

  * AWS Documentation
  * [Amazon MQ](https://aws.amazon.com/amazon-mq/)
  * [Amazon MQ Basic Elements](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-basic-elements.html)
  * [Getting Started with Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-getting-started.html)
  * [Tutorial: Creating and Configuring an Amazon MQ Broker](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-creating-configuring-broker.html)
  * [Tutorial: Deleting an Amazon MQ Broker](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-deleting-broker.html)

  * AWS Command Line Interface (CLI) Documentation
  * [list-brokers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/list-brokers.html)
  * [describe-broker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/describe-broker.html)
  * [create-broker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/create-broker.html)

Publication date Dec 22, 2017

### Related MQ rules

  * [ Publicly Accessible MQ Brokers (Security) ](/cloudoneconformity/knowledge-base/aws/MQ/publicly-accessible.html "Publicly Accessible MQ Brokers")
  * [ MQ Auto Minor Version Upgrade (Security) ](/cloudoneconformity/knowledge-base/aws/MQ/auto-minor-version-upgrade.html "MQ Auto Minor Version Upgrade")
  * [ MQ Log Exports (Security, reliability, performance-efficiency, operational-excellence) ](/cloudoneconformity/knowledge-base/aws/MQ/log-exports.html "MQ Log Exports")
  * [ MQ Desired Broker Instance Type (Sustainability, security) ](/cloudoneconformity/knowledge-base/aws/MQ/desired-instance-type.html "MQ Desired Broker Instance Type")

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

