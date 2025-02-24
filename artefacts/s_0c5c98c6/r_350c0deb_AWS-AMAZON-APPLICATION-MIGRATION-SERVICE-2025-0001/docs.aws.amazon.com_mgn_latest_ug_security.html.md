# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/mgn/latest/ug/security.html'}

[](/pdfs/mgn/latest/ug/user-guide.pdf#security "Open PDF")

[Documentation](/index.html)[Application Migration
Service](/mgn/index.html)[User Guide](what-is-application-migration-
service.html)

OverviewPolicy structure

# Security in AWS Application Migration Service

###### Topics

  * Overview
  * [Identity and access management for AWS Application Migration Service](./identity-access-management.html)
  * [Managing access using policies](./security_iam_access-manage.html)
  * [Using service-linked roles for AWS Application Migration Service](./using-service-linked-roles.html)
  * Policy structure
  * [Resilience in AWS Application Migration Service](./disaster-recovery-resiliency.html)
  * [Infrastructure security in AWS Application Migration Service](./infrastructure-security.html)
  * [Compliance validation for AWS Application Migration Service](./compliance-validation.html)
  * [Cross-service confused deputy prevention ](./cross-service-confused-deputy-prevention.html)

## Overview

Cloud security at AWS is the highest priority. As an AWS customer, you benefit
from a data center and network architecture that is built to meet the
requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared
responsibility model ](https://aws.amazon.com/compliance/shared-
responsibility-model/) describes this as security of the cloud and security in
the cloud:

  * **Security of the cloud** â AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/) . To learn about the compliance programs that apply to AWS Application Migration Service (AWS MGN), see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/). . 

  * **Security in the cloud** â Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your companyâs requirements, and applicable laws and regulations 

This documentation helps you understand how to apply the shared responsibility
model when using AWS Application Migration Service. It shows you how to
configure AWS Application Migration Service to meet your security and
compliance objectives. You also learn how to use other AWS services that help
you to monitor and secure your AWS Application Migration Service resources.

The customer is responsible for making sure that no misconfigurations are
present during and after the migration process, including:

  1. Access to replication servers should be allowed only from source servers CIDR range by applying proper security groups rules on replication servers. 

  2. After the migration, the customer should make sure that only allowed ports are exposed to the public internet. 

  3. Hardening of OS packages and other software deployed in the servers is completely under the customerâs responsibility and we recommend the following: 

    1. Packages should be up to date and free of known vulnerabilities.

    2. Only necessary OS/application services should be up and running.

  4. Enabling the Anti-DDOS protection (AWS Shield) in the customer's AWS Account to eliminate the risk of denial of service attacks on the replication servers as well as the migrated servers. 

## Policy structure

An IAM policy is a JSON document that consists of one or more statements. Each
statement is structured as follows.

    
    
    {
            "Statement": [
                    {
                            "Effect": "effect",
                            "Action": "action",
                            "Resource": "arn",
                            "Condition": {
                                    "condition": {
                                            "key":"value"
                                    }
                            }
                    }
            ]
    }
                

There are various elements that make up a statement:

  * **Effect:** The effect can be `Allow` or `Deny`. By default, IAM users don't have permission to use resources and API actions, so all requests are denied. An explicit allow overrides the default. An explicit deny overrides any allows. 

  * **Action** : The action is the specific AWS Application Migration Service API action for which you are granting or denying permission. 

  * **Resource** : The resource that's affected by the action. For AWS Application Migration Service, you must specify "*" as the resource. 

  * **Condition** : Conditions are optional. They can be used to control when your policy is in effect. 

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Logging AWS Application Migration Service with AWS CloudTrail

Identity and access management

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

