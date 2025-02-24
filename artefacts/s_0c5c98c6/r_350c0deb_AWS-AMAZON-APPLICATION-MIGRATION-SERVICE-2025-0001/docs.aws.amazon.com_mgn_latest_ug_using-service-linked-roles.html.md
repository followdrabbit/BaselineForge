# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/mgn/latest/ug/using-service-linked-roles.html'}

[](/pdfs/mgn/latest/ug/user-guide.pdf#using-service-linked-roles "Open PDF")

[Documentation](/index.html)[Application Migration
Service](/mgn/index.html)[User Guide](what-is-application-migration-
service.html)

Service-linked role permissions for AWS Application Migration ServiceCreating
a service-linked role for AWS Application Migration ServiceEditing a service-
linked role for AWS Application Migration ServiceDeleting a service-linked
role for AWS Application Migration ServiceSupported Regions for AWS MGN
service-linked roles

# Using service-linked roles for AWS Application Migration Service

AWS Application Migration Service uses AWS Identity and Access Management
(IAM)[ service-linked
roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-
concepts.html#iam-term-service-linked-role). A service-linked role is a unique
type of IAM role that is linked directly to AWS Application Migration Service.
Service-linked roles are predefined by AWS Application Migration Service and
include all the permissions that the service requires to call other AWS
services on your behalf.

A service-linked role makes setting up AWS Application Migration Service
easier because you donât have to manually add the necessary permissions. AWS
Application Migration Service defines the permissions of its service-linked
roles, and unless defined otherwise, only AWS Application Migration Service
can assume its roles. The defined permissions include the trust policy and the
permissions policy, and that permissions policy cannot be attached to any
other IAM entity.

You can delete a service-linked role only after first deleting their related
resources. This protects your AWS Application Migration Service resources
because you can't inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see
[AWS Services That Work with IAM
](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-
that-work-with-iam.html) and look for the services that have **Yes** in the
**Service-Linked Role** column. Choose a **Yes** with a link to view the
service-linked role documentation for that service.

## Service-linked role permissions for AWS Application Migration Service

AWS Application Migration Service uses the service-linked role named
**AWSServiceRoleForApplicationMigrationService**. This is a managed IAM policy
with scoped permissions that AWS Application Migration Service needs to run in
your account.

The AWSServiceRoleForApplicationMigrationService service-linked role trusts
the following services to assume the role:

  * `mgn.amazonaws.com`

The role permissions policy allows AWS Application Migration Service to
complete the following actions on the specified resources.

    
    
    {
            "Version": "2012-10-17",
            "Statement": [
                    {
                            "Effect": "Allow",
                            "Action": "mgn:ListTagsForResource",
                            "Resource": "*"
                    },
                    {
                            "Effect": "Allow",
                            "Action": "kms:ListRetirableGrants",
                            "Resource": "*"
                    },
                    {
                            "Effect": "Allow",
                            "Action": [
                                    "mgh:AssociateCreatedArtifact",
                                    "mgh:CreateProgressUpdateStream",
                                    "mgh:DisassociateCreatedArtifact",
                                    "mgh:GetHomeRegion",
                                    "mgh:ImportMigrationTask",
                                    "mgh:NotifyMigrationTaskState",
                                    "mgh:PutResourceAttributes"
                            ],
                            "Resource": "*"
                    },
                    {
                            "Effect": "Allow",
                            "Action": [
                                    "ec2:DescribeAccountAttributes",
                                    "ec2:DescribeAvailabilityZones",
                                    "ec2:DescribeImages",
                                    "ec2:DescribeInstances",
                                    "ec2:DescribeInstanceTypes",
                                    "ec2:DescribeInstanceAttribute",
                                    "ec2:DescribeInstanceStatus",
                                    "ec2:DescribeLaunchTemplateVersions",
                                    "ec2:DescribeLaunchTemplates",
                                    "ec2:DescribeSecurityGroups",
                                    "ec2:DescribeSnapshots",
                                    "ec2:DescribeSubnets",
                                    "ec2:DescribeVolumes",
                                    "ec2:GetEbsDefaultKmsKeyId",
                                    "ec2:GetEbsEncryptionByDefault"
                            ],
                            "Resource": "*"
                    },
                    {
                            "Effect": "Allow",
                            "Action": [
                                    "organizations:DescribeAccount"
                            ],
                            "Resource": "arn:aws:organizations::*:account/*"
                    },
                    {
                            "Effect": "Allow",
                            "Action": [
                                    "organizations:DescribeOrganization",
                                    "organizations:ListAWSServiceAccessForOrganization",
                                    "organizations:ListDelegatedAdministrators",
                                    "organizations:ListAccounts"
                            ],
                            "Resource": "*"
                    },
                    {
                            "Effect": "Allow",
                            "Action": [
                                    "ec2:RegisterImage",
                                    "ec2:DeregisterImage"
                            ],
                            "Resource": "*"
                    },
                    {
                            "Effect": "Allow",
                            "Action": [
                                    "ec2:DeleteSnapshot"
                            ],
                            "Resource": "arn:aws:ec2:*:*:snapshot/*",
                            "Condition": {
                                    "Null": {
                                            "aws:ResourceTag/AWSApplicationMigrationServiceManaged": "false"
                                    }
                            }
                    },
                    {
                            "Effect": "Allow",
                            "Action": [
                                    "ec2:CreateLaunchTemplateVersion",
                                    "ec2:ModifyLaunchTemplate",
                                    "ec2:DeleteLaunchTemplate",
                                    "ec2:DeleteLaunchTemplateVersions"
                            ],
                            "Resource": "arn:aws:ec2:*:*:launch-template/*",
                            "Condition": {
                                    "Null": {
                                            "aws:ResourceTag/AWSApplicationMigrationServiceManaged": "false"
                                    }
                            }
                    },
                    {
                            "Effect": "Allow",
                            "Action": [
                                    "ec2:DeleteVolume"
                            ],
                            "Resource": "arn:aws:ec2:*:*:volume/*",
                            "Condition": {
                                    "Null": {
                                            "aws:ResourceTag/AWSApplicationMigrationServiceManaged": "false"
                                    }
                            }
                    },
                    {
                            "Effect": "Allow",
                            "Action": [
                                    "ec2:StartInstances",
                                    "ec2:StopInstances",
                                    "ec2:TerminateInstances",
                                    "ec2:ModifyInstanceAttribute",
                                    "ec2:GetConsoleOutput",
                                    "ec2:GetConsoleScreenshot"
                            ],
                            "Resource": "arn:aws:ec2:*:*:instance/*",
                            "Condition": {
                                    "Null": {
                                            "aws:ResourceTag/AWSApplicationMigrationServiceManaged": "false"
                                    }
                            }
                    },
                    {
                            "Effect": "Allow",
                            "Action": [
                                    "ec2:RevokeSecurityGroupEgress",
                                    "ec2:AuthorizeSecurityGroupIngress",
                                    "ec2:AuthorizeSecurityGroupEgress"
                            ],
                            "Resource": "arn:aws:ec2:*:*:security-group/*",
                            "Condition": {
                                    "Null": {
                                            "aws:ResourceTag/AWSApplicationMigrationServiceManaged": "false"
                                    }
                            }
                    },
                    {
                            "Effect": "Allow",
                            "Action": [
                                    "ec2:CreateVolume"
                            ],
                            "Resource": "arn:aws:ec2:*:*:volume/*",
                            "Condition": {
                                    "Null": {
                                            "aws:RequestTag/AWSApplicationMigrationServiceManaged": "false"
                                    }
                            }
                    },
                    {
                            "Effect": "Allow",
                            "Action": [
                                    "ec2:CreateSecurityGroup"
                            ],
                            "Resource": "arn:aws:ec2:*:*:security-group/*",
                            "Condition": {
                                    "Null": {
                                            "aws:RequestTag/AWSApplicationMigrationServiceManaged": "false"
                                    }
                            }
                    },
                    {
                            "Effect": "Allow",
                            "Action": [
                                    "ec2:CreateSecurityGroup"
                            ],
                            "Resource": "arn:aws:ec2:*:*:vpc/*"
                    },
                    {
                            "Effect": "Allow",
                            "Action": [
                                    "ec2:CreateLaunchTemplate"
                            ],
                            "Resource": "arn:aws:ec2:*:*:launch-template/*",
                            "Condition": {
                                    "Null": {
                                            "aws:RequestTag/AWSApplicationMigrationServiceManaged": "false"
                                    }
                            }
                    },
                    {
                            "Effect": "Allow",
                            "Action": [
                                    "ec2:CreateSnapshot"
                            ],
                            "Resource": "arn:aws:ec2:*:*:volume/*",
                            "Condition": {
                                    "Null": {
                                            "ec2:ResourceTag/AWSApplicationMigrationServiceManaged": "false"
                                    }
                            }
                    },
                    {
                            "Effect": "Allow",
                            "Action": [
                                    "ec2:CreateSnapshot"
                            ],
                            "Resource": "arn:aws:ec2:*:*:snapshot/*",
                            "Condition": {
                                    "Null": {
                                            "aws:RequestTag/AWSApplicationMigrationServiceManaged": "false"
                                    }
                            }
                    },
                    {
                            "Effect": "Allow",
                            "Action": [
                                    "ec2:DetachVolume",
                                    "ec2:AttachVolume"
                            ],
                            "Resource": "arn:aws:ec2:*:*:instance/*",
                            "Condition": {
                                    "Null": {
                                            "ec2:ResourceTag/AWSApplicationMigrationServiceManaged": "false"
                                    }
                            }
                    },
                    {
                            "Effect": "Allow",
                            "Action": [
                                    "ec2:AttachVolume"
                            ],
                            "Resource": "arn:aws:ec2:*:*:volume/*",
                            "Condition": {
                                    "Null": {
                                            "ec2:ResourceTag/AWSApplicationMigrationServiceManaged": "false"
                                    }
                            }
                    },
                    {
                            "Effect": "Allow",
                            "Action": [
                                    "ec2:DetachVolume"
                            ],
                            "Resource": "arn:aws:ec2:*:*:volume/*"
                    },
                    {
                            "Effect": "Allow",
                            "Action": [
                                    "ec2:RunInstances"
                            ],
                            "Resource": "arn:aws:ec2:*:*:instance/*",
                            "Condition": {
                                    "Null": {
                                            "aws:RequestTag/AWSApplicationMigrationServiceManaged": "false"
                                    }
                            }
                    },
                    {
                            "Effect": "Allow",
                            "Action": [
                                    "ec2:RunInstances"
                            ],
                            "Resource": [
                                    "arn:aws:ec2:*:*:security-group/*",
                                    "arn:aws:ec2:*:*:volume/*",
                                    "arn:aws:ec2:*:*:subnet/*",
                                    "arn:aws:ec2:*:*:image/*",
                                    "arn:aws:ec2:*:*:network-interface/*",
                                    "arn:aws:ec2:*:*:launch-template/*"
                            ]
                    },
                    {
                            "Effect": "Allow",
                            "Action": "iam:PassRole",
                            "Resource": [
                                    "arn:aws:iam::*:role/service-role/AWSApplicationMigrationReplicationServerRole",
                                    "arn:aws:iam::*:role/service-role/AWSApplicationMigrationConversionServerRole"
                            ],
                            "Condition": {
                                    "StringEquals": {
                                            "iam:PassedToService": "ec2.amazonaws.com"
                                    }
                            }
                    },
                    {
                            "Effect": "Allow",
                            "Action": "ec2:CreateTags",
                            "Resource": [
                                    "arn:aws:ec2:*:*:launch-template/*",
                                    "arn:aws:ec2:*:*:security-group/*",
                                    "arn:aws:ec2:*:*:volume/*",
                                    "arn:aws:ec2:*:*:snapshot/*",
                                    "arn:aws:ec2:*:*:instance/*"
                            ],
                            "Condition": {
                                    "StringEquals": {
                                            "ec2:CreateAction": [
                                                    "CreateLaunchTemplate",
                                                    "CreateSecurityGroup",
                                                    "CreateVolume",
                                                    "CreateSnapshot",
                                                    "RunInstances"
                                            ]
                                    }
                            }
                    },
                    {
                            "Effect": "Allow",
                            "Action": [
                                    "ec2:CreateTags",
                                    "ec2:ModifyVolume"
                            ],
                            "Resource": [
                                    "arn:aws:ec2:*:*:volume/*"
                            ],
                            "Condition": {
                                    "Null": {
                                            "ec2:ResourceTag/AWSApplicationMigrationServiceManaged": "false"
                                    }
                            }
                    }
            ]
    }
                    

You must configure permissions to allow an IAM entity (such as a user, group,
or role) to create, edit, or delete a service-linked role. For more
information, see [Service-Linked Role Permissions
](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-
roles.html#service-linked-role-permissions) in the _IAM User Guide_.

## Creating a service-linked role for AWS Application Migration Service

You don't need to manually create a service-linked role. When you configure
the Replication Configuration Template for AWS Application Migration Service,
a service-linked role is automatically created. MGN automatically creates the
IAM service-linked role, which you can see in the IAM console. You don't need
to manually create or configure this role.

If you delete this service-linked role, and then need to create it again, you
can use the same process to recreate the role in your account. When you create
the first new replication configuration template in MGN, it creates the
service-linked role for you again.

In the AWS CLI or the AWS API, create a service-linked role with the AWS
Application Migration Service name. For more information, see [Creating a
Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-
service-linked-roles.html#create-service-linked-role) in the _IAM User Guide_.
If you delete this service-linked role, you can use this same process to
create the role again.

## Editing a service-linked role for AWS Application Migration Service

AWS Application Migration Service does not allow you to edit the
AWSServiceRoleForApplicationMigrationService service-linked role. After you
create a service-linked role, you cannot change the name of the role because
various entities might reference the role. However, you can edit the
description of the role using IAM. For more information, see [Editing a
Service-Linked Role ](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-
service-linked-roles.html#edit-service-linked-role) in the _IAM User Guide_.

## Deleting a service-linked role for AWS Application Migration Service

If you no longer need to use a feature or service that requires a service-
linked role, we recommend that you delete that role. That way you donât have
an unused entity that is not actively monitored or maintained. However, you
must clean up the resources for your service-linked role before you can
manually delete it.

###### Note

If AWS Application Migration Service is using the role when you try to delete
the resources, the deletion might fail. If that happens, wait for a few
minutes and try the operation again.

**To clean up AWS Application Migration Service resources used by
AWSServiceRoleforApplicationMigrationService**

  1. Identify and delete any waves and applications in all AWS Regions

    1. identify any waves:
        
                aws mgn list-waves

    2. Delete any waves:
        
                aws mgn delete-wave --wave-id {WaveID}

    3. Identify any application:
        
                aws mgn list-applications

    4. Delete any application:
        
                aws mgn delete-application --application-id {ApplicationID}

  2. Identify and delete any source servers in all AWS Regions

    1. Identify any active source servers:
        
                aws mgn describe-source-servers --filters isArchived=False --query "items[*].sourceServerID"

    2. Disconnect any archived source server:
        
                aws mgn disconnect-from-service --source-server-id {SourceServerID}

    3. Archive any disconnected source servers: 
        
                aws mgn mark-as-archived --source-server-id {SourceServerID}

    4. Delete any archived source server:
        
                aws mgn delete-source-server --source-server-id {SourceServerID}

  3. Identify and delete any AWS MGN jobs in all AWS Regions

    1. Identify any AWS MGN jobs
        
                aws mgn describe-jobs

    2. Delete any AWS MGN jobs:
        
                aws mgn delete-job --job-id {MGNJobId}

  4. Identify and delete any AWS MGN replication templates

    1. Identify any AWS MGN replication template:
        
                aws mgn describe-replication-configuration-templates

    2. Remove any AWS MGN replication templates:
        
                aws mgn delete-replication-configuration-template --replication-configuration-template-id {rct-TemplateID}

Resources can be cleaned up without stopping any service provided by AWS
Application Migration Service. Cleaning up AWS Application Migration Service
resources will cause AWS Application Migration Service to stop working. For
more information, see [Cleaning up a Service-Linked Role
](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-
roles.html#delete-service-linked-role) in the _IAM User Guide_.

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the
AWSServiceRoleForApplicationMigrationService service-linked role. For more
information, see [Deleting a Service-Linked Role
](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-
roles.html#delete-service-linked-role) in the _IAM User Guide_.

## Supported Regions for AWS MGN service-linked roles

AWS Application Migration Service supports using service-linked roles in all
of the [AWS Regions where the service is available](./what-is-application-
migration-service.html#supported-regions).

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Restrict permission to act on a source server associated with given AWS
vCenter client

Resilience

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

