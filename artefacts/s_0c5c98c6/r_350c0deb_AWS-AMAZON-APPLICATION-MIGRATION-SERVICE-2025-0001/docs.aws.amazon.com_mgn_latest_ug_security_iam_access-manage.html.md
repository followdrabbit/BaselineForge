# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/mgn/latest/ug/security_iam_access-manage.html'}

[](/pdfs/mgn/latest/ug/user-guide.pdf#security_iam_access-manage "Open PDF")

[Documentation](/index.html)[Application Migration
Service](/mgn/index.html)[User Guide](what-is-application-migration-
service.html)

Identity-based policies Resource-based policies Access control lists
(ACLs)Other policy typesMultiple policy types

# Managing access using policies

You control access in AWS by creating policies and attaching them to AWS
identities or resources. A policy is an object in AWS that, when associated
with an identity or resource, defines their permissions. AWS evaluates these
policies when a principal (user, root user, or role session) makes a request.
Permissions in the policies determine whether the request is allowed or
denied. Most policies are stored in AWS as JSON documents. For more
information about the structure and contents of JSON policy documents, see
[Overview of JSON
policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-
json) in the _IAM User Guide_.

Administrators can use AWS JSON policies to specify who has access to what.
That is, which **principal** can perform **actions** on what **resources** ,
and under what **conditions**.

By default, users and roles have no permissions. To grant users permission to
perform actions on the resources that they need, an IAM administrator can
create IAM policies. The administrator can then add the IAM policies to roles,
and users can assume the roles.

IAM policies define permissions for an action regardless of the method that
you use to perform the operation. For example, suppose that you have a policy
that allows the `iam:GetRole` action. A user with that policy can get role
information from the AWS Management Console, the AWS CLI, or the AWS API.

## Identity-based policies

Identity-based policies are JSON permissions policy documents that you can
attach to an identity, such as a user, role, or group. These policies control
what actions that identity can perform, on which resources, and under what
conditions. To learn how to create an identity-based policy, see [Define
custom IAM permissions with customer managed policies
](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html)
in the IAM User Guide.

Identity-based policies can be further categorized as inline policies or
managed policies. Inline policies are embedded directly into a single user,
group, or role. Managed policies are standalone policies that you can attach
to multiple users, groups, and roles in your AWS account. Managed policies
include AWS managed policies and customer managed policies. To learn how to
choose between a managed policy or an inline policy, see[Managed policies and
inline policies
](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-
inline.html#choosing-managed-or-inline) in the IAM User Guide.

## Resource-based policies

Resource-based policies are JSON policy documents that you attach to a
resource. Examples of resource-based policies are IAM _role trust policies_
and Amazon S3 _bucket policies_. In services that support resource-based
policies, service administrators can use them to control access to a specific
resource. For the resource where the policy is attached, the policy defines
what actions a specified principal can perform on that resource and under what
conditions. You must [specify a
principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html)
in a resource-based policy. Principals can include accounts, users, roles,
federated users, or AWS services.

Resource-based policies are inline policies that are located in that service.
You can't use AWS managed policies from IAM in a resource-based policy.

## Access control lists (ACLs)

Access control lists (ACLs) control which principals (account members, users,
or roles) have permissions to access a resource. ACLs are similar to resource-
based policies, although they do not use the JSON policy document format.

Amazon S3, AWS WAF, and Amazon VPC are examples of services that support ACLs.
To learn more about ACLs, see [Access control list (ACL)
overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-
overview.html) in the _Amazon Simple Storage Service Developer Guide_.

## Other policy types

AWS supports additional, less-common policy types. These policy types can set
the maximum permissions granted to you by the more common policy types.

  * **Permissions boundaries** â A permissions boundary is an advanced feature in which you set the maximum permissions that an identity-based policy can grant to an IAM entity (IAM user or role). You can set a permissions boundary for an entity. The resulting permissions are the intersection of an entity's identity-based policies and its permissions boundaries. Resource-based policies that specify the user or role in the `Principal` field are not limited by the permissions boundary. An explicit deny in any of these policies overrides the allow. For more information about permissions boundaries, see [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in the _IAM User Guide_.

  * **Service control policies (SCPs)** â SCPs are JSON policies that specify the maximum permissions for an organization or organizational unit (OU) in AWS Organizations. AWS Organizations is a service for grouping and centrally managing multiple AWS accounts that your business owns. If you enable all features in an organization, then you can apply service control policies (SCPs) to any or all of your accounts. The SCP limits permissions for entities in member accounts, including each AWS account root user. For more information about Organizations and SCPs, see [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the _AWS Organizations User Guide_.

  * **Resource control policies (RCPs)** â RCPs are JSON policies that you can use to set the maximum available permissions for resources in your accounts without updating the IAM policies attached to each resource that you own. The RCP limits permissions for resources in member accounts and can impact the effective permissions for identities, including the AWS account root user, regardless of whether they belong to your organization. For more information about Organizations and RCPs, including a list of AWS services that support RCPs, see [Resource control policies (RCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) in the _AWS Organizations User Guide_.

  * **Session policies** â Session policies are advanced policies that you pass as a parameter when you programmatically create a temporary session for a role or federated user. The resulting session's permissions are the intersection of the user or role's identity-based policies and the session policies. Permissions can also come from a resource-based policy. An explicit deny in any of these policies overrides the allow. For more information, see [Session policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session) in the _IAM User Guide_. 

## Multiple policy types

When multiple types of policies apply to a request, the resulting permissions
are more complicated to understand. To learn how AWS determines whether to
allow a request when multiple policy types are involved, see [Policy
evaluation
logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-
logic.html) in the _IAM User Guide_.

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

AWSApplicationMigrationServiceEc2InstancePolicy

Using identity-based policies

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

