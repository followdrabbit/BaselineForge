# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/outposts/latest/userguide/using-service-linked-roles.html'}

[](/pdfs/outposts/latest/userguide/outposts-rack.pdf#using-service-linked-
roles "Open PDF")

[Documentation](/index.html)[AWS Outposts](/outposts/index.html)[User Guide
for Outposts racks](what-is-outposts.html)

Permissions for AWS OutpostsCreate a service-linked roleEdit a service-linked
roleDelete a service-linked roleSupported Regions

# Service-linked roles for AWS Outposts

AWS Outposts uses AWS Identity and Access Management (IAM) service-linked
roles. A service-linked role is a type of service role that is linked directly
to AWS Outposts. AWS Outposts defines service-linked roles and includes all
the permissions that it requires to call other AWS services on your behalf.

A service-linked role makes setting up your AWS Outposts more efficient
because you donât have to manually add the necessary permissions. AWS
Outposts defines the permissions of its service-linked roles, and unless
defined otherwise, only AWS Outposts can assume its roles. The defined
permissions include the trust policy and the permissions policy, and that
permissions policy can't be attached to any other IAM entity.

You can delete a service-linked role only after first deleting the related
resources. This protects your AWS Outposts resources because you can't
inadvertently remove permission to access the resources.

## Service-linked role permissions for AWS Outposts

AWS Outposts uses the service-linked role named
**AWSServiceRoleForOutposts_`OutpostID`** â Allows Outposts to access AWS
resources for private connectivity on your behalf. This service-linked role
allows private connectivity configuration, creates network interfaces, and
attaches them to service link endpoint instances.

The AWSServiceRoleForOutposts_`OutpostID` service-linked role trusts the
following services to assume the role:

  * `outposts.amazonaws.com`

The **AWSServiceRoleForOutposts_`OutpostID`** service-linked role includes the
following policies:

  * **AWSOutpostsServiceRolePolicy**

  * **AWSOutpostsPrivateConnectivityPolicy_`OutpostID`**

The **AWSOutpostsServiceRolePolicy** policy is a service-linked role policy to
enable access to AWS resources managed by AWS Outposts.

This policy allows AWS Outposts to complete the following actions on the
specified resources:

  * Action: `ec2:DescribeNetworkInterfaces` on `all AWS resources`

  * Action: `ec2:DescribeSecurityGroups` on `all AWS resources`

  * Action: `ec2:CreateSecurityGroup` on `all AWS resources`

  * Action: `ec2:CreateNetworkInterface` on `all AWS resources`

The **AWSOutpostsPrivateConnectivityPolicy_`OutpostID`** policy allows AWS
Outposts to complete the following actions on the specified resources:

  * Action: `ec2:AuthorizeSecurityGroupIngress` on `all AWS resources that match the following Condition:`
    
        { "StringLike" : { "ec2:ResourceTag/outposts:private-connectivity-resourceId" : "OutpostID" }} and { "StringEquals" : { "ec2:Vpc" : "vpcArn" }}

  * Action: `ec2:AuthorizeSecurityGroupEgress` on `all AWS resources that match the following Condition:`
    
        { "StringLike" : { "ec2:ResourceTag/outposts:private-connectivity-resourceId" : "OutpostID" }} and { "StringEquals" : { "ec2:Vpc" : "vpcArn" }}

  * Action: `ec2:CreateNetworkInterfacePermission` on `all AWS resources that match the following Condition:`
    
        { "StringLike" : { "ec2:ResourceTag/outposts:private-connectivity-resourceId" : "OutpostID" }} and { "StringEquals" : { "ec2:Vpc" : "vpcArn" }}

  * Action: `ec2:CreateTags` on `all AWS resources that match the following Condition:`
    
        { "StringLike" : { "aws:RequestTag/outposts:private-connectivity-resourceId" : "{{OutpostId}}*"}}

You must configure permissions to allow an IAM entity (such as a user, group,
or role) to create, edit, or delete a service-linked role. For more
information, see [Service-linked role
permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-
service-linked-role.html#service-linked-role-permissions) in the _IAM User
Guide_.

## Create a service-linked role for AWS Outposts

You don't need to manually create a service-linked role. When you configure
private connectivity for your Outpost in the AWS Management Console, AWS
Outposts creates the service-linked role for you.

For more information, see [Service link private connectivity
options](./private-connectivity.html).

## Edit a service-linked role for AWS Outposts

AWS Outposts does not allow you to edit the
AWSServiceRoleForOutposts_`OutpostID` service-linked role. After you create a
service-linked role, you can't change the name of the role because various
entities might reference the role. However, you can edit the description of
the role using IAM. For more information, see [Update a service-linked
role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-
service-linked-role.html) in the _IAM User Guide_.

## Delete a service-linked role for AWS Outposts

If you no longer require a feature or service that requires a service-linked
role, we recommend that you delete that role. That way you avoid having an
unused entity that is not actively monitored or maintained. However, you must
clean up the resources for your service-linked role before you can manually
delete it.

If the AWS Outposts service is using the role when you try to delete the
resources, then the deletion might fail. If that happens, wait for a few
minutes and try the operation again.

You must delete your Outpost before you can delete the
AWSServiceRoleForOutposts_`OutpostID` service-linked role.

Before you begin, make sure that your Outpost is not being shared using AWS
Resource Access Manager (AWS RAM). For more information, see [Unsharing a
shared Outpost resource](./sharing-outposts.html#sharing-unshare).

###### To delete AWS Outposts resources used by the
AWSServiceRoleForOutposts_`OutpostID`

Contact AWS Enterprise Support to delete your Outpost.

###### To manually delete the service-linked role using IAM

For more information, see [Delete a service-linked
role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html#id_roles_manage_delete_slr)
in the _IAM User Guide_.

## Supported Regions for AWS Outposts service-linked roles

AWS Outposts supports using service-linked roles in all of the Regions where
the service is available. For more information, see the FAQs for [Outposts
racks](https://aws.amazon.com/outposts/rack/faqs/) and [Outposts
servers](https://aws.amazon.com/outposts/servers/faqs/).

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Policy examples

AWS managed policies

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

