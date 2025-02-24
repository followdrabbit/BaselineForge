# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-using-service-linked-roles.html'}

[](/pdfs/lightsail/latest/userguide/lightsail-ug.pdf#amazon-lightsail-using-
service-linked-roles "Open PDF")

[Documentation](/index.html)[Amazon Lightsail](/lightsail/index.html)[User
Guide](what-is-amazon-lightsail.html)

Service-Linked Role Permissions for Amazon LightsailCreating a Service-Linked
Role for Amazon LightsailEditing a Service-Linked Role for Amazon
LightsailDeleting a Service-Linked Role for Amazon LightsailSupported Regions
for Amazon Lightsail Service-Linked Roles

# Use service-linked roles for Amazon Lightsail

Amazon Lightsail uses AWS Identity and Access Management (IAM)[ service-linked
roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-
concepts.html#iam-term-service-linked-role). A service-linked role is a unique
type of IAM role that is linked directly to Amazon Lightsail. Service-linked
roles are predefined by Amazon Lightsail and include all the permissions that
Lightsail requires to call other AWS services on your behalf.

A service-linked role makes setting up Amazon Lightsail easier because you
donât have to manually add the necessary permissions. Amazon Lightsail
defines the permissions of its service-linked roles, and unless defined
otherwise, only Amazon Lightsail can assume its roles. The defined permissions
include the trust policy and the permissions policy, which cannot be attached
to any other IAM entity.

You can delete a service-linked role only after first deleting their related
resources. This protects your Amazon Lightsail resources because you can't
inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see
[AWS Services That Work with
IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-
that-work-with-iam.html) and look for the services that have **Yes** in the
**Service-Linked Role** column. Choose a **Yes** with a link to view the
service-linked role documentation for that service.

## Service-Linked Role Permissions for Amazon Lightsail

Amazon Lightsail uses the service-linked role named
**AWSServiceRoleForLightsail** â Role to export Lightsail instance and block
storage disk snapshots to Amazon Elastic Compute Cloud (Amazon EC2), and to
get the current account-level Block Public Access configuration from Amazon
Simple Storage Service (Amazon S3).

The AWSServiceRoleForLightsail service-linked role trusts the following
services to assume the role:

  * `lightsail.amazonaws.com`

The role permissions policy allows Amazon Lightsail to complete the following
actions on the specified resources:

  * Action: `ec2:CopySnapshot` on all AWS resources.

  * Action: `ec2:DescribeSnapshots` on all AWS resources.

  * Action: `ec2:CopyImage` on all AWS resources.

  * Action: `ec2:DescribeImages` on all AWS resources.

  * Action: `cloudformation:DescribeStacks` on all AWS AWS CloudFormation stacks.

  * Action: `s3:GetAccountPublicAccessBlock` on all AWS resources.

### Service-Linked Role Permissions

You must configure permissions to allow an IAM entity (such as a user, group,
or role) to create or edit the description of a service-linked role.

**To allow an IAM entity to create a specific service-linked role**

Add the following policy to the IAM entity that needs to create the service-
linked role.

    
    
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "iam:CreateServiceLinkedRole",
                "Resource": "arn:aws:iam::*:role/aws-service-role/lightsail.amazonaws.com/AWSServiceRoleForLightsail*",
                "Condition": {"StringLike": {"iam:AWSServiceName": "lightsail.amazonaws.com"}}
            },
            {
                "Effect": "Allow",
                "Action": "iam:PutRolePolicy",
                "Resource": "arn:aws:iam::*:role/aws-service-role/lightsail.amazonaws.com/AWSServiceRoleForLightsail*"
            }
        ]
    }
        

**To allow an IAM entity to create any service-linked role**

Add the following statement to the permissions policy for the IAM entity that
needs to create a service-linked role, or any service role that includes the
needed policies. This policy attaches a policy to the role.

    
    
    {
        "Effect": "Allow",
        "Action": "iam:CreateServiceLinkedRole",
        "Resource": "arn:aws:iam::*:role/aws-service-role/*"
    }
        

**To allow an IAM entity to edit the description of any service roles**

Add the following statement to the permissions policy for the IAM entity that
needs to edit the description of a service-linked role, or any service role.

    
    
    {
        "Effect": "Allow",
        "Action": "iam:UpdateRoleDescription",
        "Resource": "arn:aws:iam::*:role/aws-service-role/*"
    }
        

**To allow an IAM entity to delete a specific service-linked role**

Add the following statement to the permissions policy for the IAM entity that
needs to delete the service-linked role.

    
    
    {
        "Effect": "Allow",
        "Action": [
            "iam:DeleteServiceLinkedRole",
            "iam:GetServiceLinkedRoleDeletionStatus"
        ],
        "Resource": "arn:aws:iam::*:role/aws-service-role/lightsail.amazonaws.com/AWSServiceRoleForLightsail*"
    }
        

**To allow an IAM entity to delete any service role**

Add the following statement to the permissions policy for the IAM entity that
needs to delete a service-linked role, or any service-role.

    
    
    {
        "Effect": "Allow",
        "Action": [
            "iam:DeleteServiceLinkedRole",
            "iam:GetServiceLinkedRoleDeletionStatus"
        ],
        "Resource": "arn:aws:iam::*:role/aws-service-role/*"
    }
        

Alternatively, you can use an AWS managed policy to provide full access to the
service.

## Creating a Service-Linked Role for Amazon Lightsail

You don't need to manually create a service-linked role. When you export your
Lightsail instance or block storage disk snapshot to Amazon EC2, or create or
update a Lightsail bucket in the AWS AWS Management Console, the AWS CLI, or
the AWS API, Amazon Lightsail creates the service-linked role for you.

If you delete this service-linked role and need to create it again, you can
use the same process to recreate the role in your account. When you export
your Lightsail instance or block storage disk snapshot to Amazon EC2, or
create or update a Lightsail bucket, Amazon Lightsail creates the service-
linked role for you again.

###### Important

You must configure IAM permissions to allow Amazon Lightsail to create the
service-linked role. To do this, complete the steps that are in the following
_Service-Linked Role Permissions_ section.

## Editing a Service-Linked Role for Amazon Lightsail

Amazon Lightsail does not allow you to edit the AWSServiceRoleForLightsail
service-linked role. After you create a service-linked role, you cannot change
the name of the role because various entities might reference the role.
However, you can edit the description of the role using IAM. For more
information, see [Editing a Service-Linked
Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-
roles.html#edit-service-linked-role) in the _IAM User Guide_.

## Deleting a Service-Linked Role for Amazon Lightsail

If you no longer need to use a feature or service that requires a service-
linked role, we recommend that you delete that role. That way you donât have
an unused entity that is not actively monitored or maintained. However, you
must confirm that there are no Amazon Lightsail instance or disk snapshots in
a pending copy state before you can delete the AWSServiceRoleForLightsail
service-linked role. For more information, see [Export snapshots to Amazon
EC2](./amazon-lightsail-exporting-snapshots-to-amazon-ec2.html).

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the
AWSServiceRoleForLightsail service-linked role. For more information, see
[Deleting a Service-Linked
Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-
roles.html#delete-service-linked-role) in the _IAM User Guide_.

## Supported Regions for Amazon Lightsail Service-Linked Roles

Amazon Lightsail supports using service-linked roles in all of the regions
where the service is available. For more information about the regions that
Lightsail is available in, see [Amazon Lightsail
Regions](https://docs.aws.amazon.com/general/latest/gr/rande.html#lightsail_region).

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Resource-level permissions policy examples

Manage buckets with IAM

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

