# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-launch-template-permissions.html'}

[](/pdfs/autoscaling/ec2/userguide/as-dg.pdf#ec2-auto-scaling-launch-template-
permissions "Open PDF")

[Documentation](/index.html)[Auto Scaling](/autoscaling/index.html)[User
Guide](what-is-amazon-ec2-auto-scaling.html)

Require launch templates that have a specific tagRequire a launch template and
a version numberRequire the use of instance metadata service version 2
(IMDSv2)Restrict access to Amazon EC2 resourcesPermissions required to tag
instances and volumesAdditional launch template permissionsPermissions
validation for ec2:RunInstances and iam:PassRoleRelated resources

# Control Amazon EC2 launch template usage in Auto Scaling groups

Amazon EC2 Auto Scaling supports using Amazon EC2 launch templates with your
Auto Scaling groups. We recommend that you allow users to create Auto Scaling
groups from launch templates, because doing so allows them to use the latest
features of Amazon EC2 Auto Scaling and Amazon EC2. For example, users must
specify a launch template to use a [mixed instances
policy](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_MixedInstancesPolicy.html).

You can use the `AmazonEC2FullAccess` policy to give users complete access to
work with Amazon EC2 Auto Scaling resources, launch templates, and other EC2
resources in their account. Or, you can create your own custom IAM policies to
give users fine-grained permissions to work with launch templates, as
described in this topic.

**A sample policy that you can tailor for your own use**

The following shows an example of a basic permissions policy that you can
tailor for your own use. The policy grants permissions to create, update, and
delete all Auto Scaling groups, but only if the group uses the tag
``purpose=testing``. It then gives permission for all `Describe` actions.
Because `Describe` actions do not support resource-level permissions, you must
specify them in a separate statement without conditions.

IAM identities (users or roles) with this policy have permission to create or
update an Auto Scaling group using a launch template because they're also
given permission to use the `ec2:RunInstances` action.

    
    
    {
        "Version": "2012-10-17",
        "Statement": [
              {
                "Effect": "Allow",
                "Action": [
                    "autoscaling:CreateAutoScalingGroup",
                    "autoscaling:UpdateAutoScalingGroup",
                    "autoscaling:DeleteAutoScalingGroup"
                ],
                "Resource": "*",
                "Condition": {
                    "StringEquals": { "autoscaling:ResourceTag/purpose": "testing" }
                }
             },
             {
                "Effect": "Allow",
                "Action": [
                    "autoscaling:Describe*",
                    "ec2:RunInstances"
                ],
                "Resource": "*"
            }
        ]
    }

Users who create or update Auto Scaling groups might need some related
permissions, such as:

  * **ec2:CreateTags** â To add tags to the instances and volumes on creation, the user must have the `ec2:CreateTags` permission in an IAM policy. For more information, see Permissions required to tag instances and volumes.

  * **iam:PassRole** â To launch EC2 instances from a launch template that contains an instance profile (a container for an IAM role), the user must also have the `iam:PassRole` permission in an IAM policy. For more information and an example IAM policy, see [IAM role for applications that run on Amazon EC2 instances](./us-iam-role.html). 

  * **ssm:GetParameters** â To launch EC2 instances from a launch template that uses an AWS Systems Manager parameter, the user must also have the `ssm:GetParameters` permission in an IAM policy. For more information, see [Use AWS Systems Manager parameters instead of AMI IDs in launch templates](./using-systems-manager-parameters.html). 

These permissions for actions to be completed when launching instances are
checked when the user interacts with an Auto Scaling group. For more
information, see Permissions validation for ec2:RunInstances and iam:PassRole.

The following examples show policy statements that you could use to control
the access that IAM users have to using launch templates.

###### Topics

  * Require launch templates that have a specific tag
  * Require a launch template and a version number
  * Require the use of instance metadata service version 2 (IMDSv2)
  * Restrict access to Amazon EC2 resources
  * Permissions required to tag instances and volumes
  * Additional launch template permissions
  * Permissions validation for ec2:RunInstances and iam:PassRole
  * Related resources

## Require launch templates that have a specific tag

When granting `ec2:RunInstances` permissions, you can specify that users can
only use launch templates with specific tags or specific IDs to limit
permissions when launching instances with a launch template. You can also
control the AMI and other resources that anyone using launch templates can
reference and use when launching instances by specifying additional resource-
level permissions for the `RunInstances` call.

The following example restricts permissions for the `ec2:RunInstances` action
to launch templates that are located in the specified Region and that have the
tag ``purpose=testing``. It also gives users access to the resources specified
in a launch template: AMIs, instance types, volumes, key pairs, network
interfaces, and security groups.

    
    
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "ec2:RunInstances",
                "Resource": "arn:aws:ec2:region:account-id:launch-template/*",
                "Condition": {
                    "StringEquals": { "aws:ResourceTag/purpose": "testing" }
                }
            },
            {
                "Effect": "Allow",
                "Action": "ec2:RunInstances",
                "Resource": [
                    "arn:aws:ec2:region::image/ami-*",
                    "arn:aws:ec2:region:account-id:instance/*",
                    "arn:aws:ec2:region:account-id:subnet/*",
                    "arn:aws:ec2:region:account-id:volume/*",
                    "arn:aws:ec2:region:account-id:key-pair/*",
                    "arn:aws:ec2:region:account-id:network-interface/*",
                    "arn:aws:ec2:region:account-id:security-group/*"
                ]
            }
        ]
    }

For more information about using tag-based policies with launch templates, see
[Control access to launch templates with IAM
permissions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/permissions-
for-launch-templates.html) in the _Amazon EC2 User Guide_.

## Require a launch template and a version number

You can also use IAM permissions to enforce that a launch template and the
version number of the launch template must be specified when creating or
updating Auto Scaling groups.

The following example allows users to create and update Auto Scaling groups
only if a launch template and the version number of the launch template are
specified. If users with this policy omit the version number to specify either
the `$Latest` or `$Default` launch template version, or attempt to use a
launch configuration instead, the action fails.

    
    
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "autoscaling:CreateAutoScalingGroup",
                    "autoscaling:UpdateAutoScalingGroup"
                ],
                "Resource": "*",
                "Condition": {
                    "Bool": { "autoscaling:LaunchTemplateVersionSpecified": "true" }
                }
            },
            {
                "Effect": "Deny",
                "Action": [
                    "autoscaling:CreateAutoScalingGroup",
                    "autoscaling:UpdateAutoScalingGroup"
                ],
                "Resource": "*",
                "Condition": {
                    "Null": { "autoscaling:LaunchConfigurationName": "false" }
                }
            }
        ]
    }

## Require the use of instance metadata service version 2 (IMDSv2)

For extra security, you can set your users' permissions to require the use of
a launch template that requires IMDSv2. For more information, see [Configuring
the instance metadata
service](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-
instance-metadata-service.html) in the _Amazon EC2 User Guide_.

The following example specifies that users can't call the `ec2:RunInstances`
action unless the instance is also opted in to require the use of IMDSv2
(indicated by `"ec2:MetadataHttpTokens":"required"`).

    
    
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "RequireImdsV2",
                "Effect": "Deny",
                "Action": "ec2:RunInstances",
                "Resource": "arn:aws:ec2:*:*:instance/*",
                "Condition": {
                    "StringNotEquals": { "ec2:MetadataHttpTokens": "required" }
                }
            }
        ]
    }

###### Tip

To force replacement Auto Scaling instances to launch that use a new launch
template or a new version of a launch template with the instance metadata
options configured, you can start an instance refresh. For more information,
see [Update Auto Scaling instances](./update-auto-scaling-group.html#update-
auto-scaling-instances).

## Restrict access to Amazon EC2 resources

The following examples show how to use resource-level permissions and tagged
resources to restrict access to Amazon EC2 resources.

###### Example 1: Restrict Amazon EC2 instance launches to specific resources
and instance types

The following example controls the configuration of the instances that a user
can launch by restricting access to Amazon EC2 resources. To specify resource-
level permissions for resources specified in a launch template, you must
include the resources in the `RunInstances` action statement.

    
    
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "ec2:RunInstances",
                "Resource": [
                    "arn:aws:ec2:region:account-id:launch-template/*",
                    "arn:aws:ec2:region::image/ami-04d5cc9b88example",
                    "arn:aws:ec2:region:account-id:subnet/subnet-1a2b3c4d",
                    "arn:aws:ec2:region:account-id:volume/*",
                    "arn:aws:ec2:region:account-id:key-pair/*",
                    "arn:aws:ec2:region:account-id:network-interface/*",
                    "arn:aws:ec2:region:account-id:security-group/sg-903004f88example"
                ]
            },
            {
                "Effect": "Allow",
                "Action": "ec2:RunInstances",
                "Resource": "arn:aws:ec2:region:account-id:instance/*",
                "Condition": {
                    "StringEquals": { "ec2:InstanceType": ["t2.micro", "t2.small"] }
                }
            }
        ]
    }

In this example, there are two statements:

  * The first statement requires that users launch instances into a specific subnet (``subnet-1a2b3c4d``), using a specific security group (``sg-903004f88example``), and using a specific AMI (``ami-04d5cc9b88example``). It also gives users access to the resources specified in a launch template: network interfaces, key pairs, and volumes. 

  * The second statement allows users to launch instances using only the ``t2.micro`` and ``t2.small`` instance types, which you might do to control costs.

However, note that there is not currently an effective way to completely
prevent users who have permission to launch instances with a launch template
from launching other instance types. This is because an instance type
specified in a launch template can be overridden to use instance types that
are defined using attribute-based instance type selection.

For a full list of the resource-level permissions that you can use to control
the configuration of the instances that a user can launch, see [Actions,
resources, and condition keys for Amazon
EC2](https://docs.aws.amazon.com/service-
authorization/latest/reference/list_amazonec2.html) in the _Service
Authorization Reference_.

###### Example 2: Require tags and restrict resource access for Amazon EC2
instance launches

The following example policy shows how you can use conditions in your
identity-based policy to control access to Amazon EC2 resources based on tags.

    
    
    {
        "Version": "2012-10-17",
        "Statement": [
             {
               "Sid": "InstanceTags",
               "Effect": "Allow",
               "Action": [
                    "ec2:RunInstances"
                ],
                "Resource": [
                    "arn:aws:ec2:us-east-1:555555555555:instance/*"
                ],
                "Condition": {
                    "StringEquals": {
                        "aws:RequestTag/owner": "dev"
                    }
                }    
            },       
            {
                "Sid": "InstanceBoundaries"
                "Effect": "Allow",
                "Action": [
                    "ec2:RunInstances"
                ],
                "Resource": [
                    "arn:aws:ec2:us-east-1::image/*",
                    "arn:aws:ec2:us-east-1:555555555555:subnet/*",
                    "arn:aws:ec2:us-east-1:555555555555:network-interface/*"
                ],  
            },
            {
                "Sid": "InstanceResourceTags",
                "Effect": "Allow",
                "Action": [
                    "ec2:RunInstances"
                ],    
                "Resource": [
                    "arn:aws:ec2:us-east-1:555555555555:key-pair/*",
                    "arn:aws:ec2:us-east-1:555555555555:security-group/*",
                    "arn:aws:ec2:us-east-1:555555555555:launch-template/*"
                    "arn:aws:ec2:us-east-1:555555555555:volume/*"   
                ],
                "Condition": {
                    "StringEquals": {
                        "aws:ResourceTag/purpose": "testing"
                    }
                }
            }  
        ]
    }

In this example, there are three statements:

  * The first statement allows users to launch instances in the specified Region only if a tag with `owner=dev` is used in the request. 

  * The second statement gives users access to the AMI, subnet, and network interface in the specified Region. 

  * The third statement allows users to launch instances in the specified Region with an existing key pair, security group, launch template, and volume that have the tag `purpose=testing`.

For more information, see [Controlling access to AWS resources using
tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) in
the _IAM User Guide_.

## Permissions required to tag instances and volumes

The following example allows users to tag instances and volumes on creation.
This policy is needed if there are tags specified in the launch template. For
more information, see [Grant permission to tag resources during
creation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/supported-iam-
actions-tagging.html) in the _Amazon EC2 User Guide_.

    
    
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "ec2:CreateTags",
                "Resource": "arn:aws:ec2:region:account-id:*/*",
                "Condition": {
                    "StringEquals": { "ec2:CreateAction": "RunInstances" }
                }
            }
        ]
    }

## Additional launch template permissions

You must give your console users permissions for the
`ec2:DescribeLaunchTemplates` and `ec2:DescribeLaunchTemplateVersions`
actions. Without these permissions, launch template data cannot load in the
Auto Scaling group wizard, and users cannot step through the wizard to launch
instances using a launch template. You can specify these additional actions in
the `Action` element of an IAM policy statement.

## Permissions validation for `ec2:RunInstances` and `iam:PassRole`

Users can specify which version of a launch template their Auto Scaling group
uses. Depending on their permissions, this can be a specific numbered version,
or the `$Latest` or `$Default` version of the launch template. If it's the
latter, take special care. This may override permissions for
`ec2:RunInstances` and `iam:PassRole` that you intended to restrict.

This section explains the scenario of using the latest or default version of
the launch template with an Auto Scaling group.

When a user calls the `CreateAutoScalingGroup`, `UpdateAutoScalingGroup`, or
`StartInstanceRefresh` APIs, Amazon EC2 Auto Scaling checks their permissions
against the version of the launch template that is the latest or default
version at that time before proceeding with the request. This validates
permissions for actions to be completed when launching instances, such as the
`ec2:RunInstances` and `iam:PassRole` actions. To accomplish this, we issue an
Amazon EC2
[RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html)
dry run call to validate whether the user has the required permissions for the
action, without actually making the request. When a response is returned, it
is read by Amazon EC2 Auto Scaling. If the user's permissions do not allow a
given action, Amazon EC2 Auto Scaling fails the request and returns an error
to the user containing information about the missing permission.

After the initial verification and request are complete, whenever instances
launch, Amazon EC2 Auto Scaling launches them with the latest or default
version, even if it has changed, using the permissions of its [service-linked
role](./autoscaling-service-linked-role.html#service-linked-role-permissions).
This means that a user who is using the launch template could potentially
update it to pass an IAM role to an instance even if they don't have the
`iam:PassRole` permission.

Use the `autoscaling:LaunchTemplateVersionSpecified` condition key if you want
to limit who has access to configuring groups to use the `$Latest` or
`$Default` version. This ensures that the Auto Scaling group only accepts a
specific numbered version when a user calls the `CreateAutoScalingGroup` and
`UpdateAutoScalingGroup` APIs. For an example that shows how to add this
condition key to an IAM policy, see Require a launch template and a version
number.

For Auto Scaling groups that are configured to use the `$Latest` or `$Default`
launch template version, consider limiting who can create and manage versions
of the launch template, including the `ec2:ModifyLaunchTemplate` action that
allows a user to specify the default launch template version. For more
information, see [Control versioning
permissions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/permissions-
for-launch-templates.html#permissions-for-launch-template-versions) in the
_Amazon EC2 User Guide_.

## Related resources

To learn more about permissions to view, create, and delete launch templates
and launch template versions, see [Control access to launch templates with IAM
permissions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/permissions-
for-launch-templates.html) in the _Amazon EC2 User Guide_.

For more information about the resource-level permissions that you can use to
control access to the `RunInstances` call, see [Actions, resources, and
condition keys for Amazon EC2](https://docs.aws.amazon.com/service-
authorization/latest/reference/list_amazonec2.html) in the _Service
Authorization Reference_.

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Cross-service confused deputy prevention

IAM role for applications that run on Amazon EC2 instances

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

