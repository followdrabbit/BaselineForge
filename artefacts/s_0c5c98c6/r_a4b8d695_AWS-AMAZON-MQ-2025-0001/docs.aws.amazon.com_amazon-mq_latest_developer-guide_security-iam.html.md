# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security-iam.html'}

[](/pdfs/amazon-mq/latest/developer-guide/amazon-mq-dg.pdf#security-iam "Open
PDF")

[Documentation](/index.html)[Amazon MQ](/amazon-mq/index.html)[Developer
Guide](welcome.html)

AudienceAuthenticating with identitiesManaging access using policies

# Identity and access Management for Amazon MQ

AWS Identity and Access Management (IAM) is an AWS service that helps an
administrator securely control access to AWS resources. IAM administrators
control who can be _authenticated_ (signed in) and _authorized_ (have
permissions) to use Amazon MQ resources. IAM is an AWS service that you can
use with no additional charge.

###### Topics

  * Audience
  * Authenticating with identities
  * Managing access using policies
  * [How Amazon MQ works with IAM](./security_iam_service-with-iam.html)
  * [Amazon MQ Identity-based policy examples](./security_iam_id-based-policy-examples.html)
  * [API authentication and authorization for Amazon MQ](./security-api-authentication-authorization.html)
  * [AWS managed policies for Amazon MQ](./security-iam-aws-managed-policies.html)
  * [Using service-linked roles for Amazon MQ](./using-service-linked-roles.html)
  * [Troubleshooting Amazon MQ identity and access](./security_iam_troubleshoot.html)

## Audience

How you use AWS Identity and Access Management (IAM) differs, depending on the
work that you do in Amazon MQ.

**Service user** â If you use the Amazon MQ service to do your job, then
your administrator provides you with the credentials and permissions that you
need. As you use more Amazon MQ features to do your work, you might need
additional permissions. Understanding how access is managed can help you
request the right permissions from your administrator. If you cannot access a
feature in Amazon MQ, see [Troubleshooting Amazon MQ identity and
access](./security_iam_troubleshoot.html).

**Service administrator** â If you're in charge of Amazon MQ resources at
your company, you probably have full access to Amazon MQ. It's your job to
determine which Amazon MQ features and resources your service users should
access. You must then submit requests to your IAM administrator to change the
permissions of your service users. Review the information on this page to
understand the basic concepts of IAM. To learn more about how your company can
use IAM with Amazon MQ, see [How Amazon MQ works with
IAM](./security_iam_service-with-iam.html).

**IAM administrator** â If you're an IAM administrator, you might want to
learn details about how you can write policies to manage access to Amazon MQ.
To view example Amazon MQ identity-based policies that you can use in IAM, see
[Amazon MQ Identity-based policy examples](./security_iam_id-based-policy-
examples.html).

## Authenticating with identities

Authentication is how you sign in to AWS using your identity credentials. You
must be _authenticated_ (signed in to AWS) as the AWS account root user, as an
IAM user, or by assuming an IAM role.

You can sign in to AWS as a federated identity by using credentials provided
through an identity source. AWS IAM Identity Center (IAM Identity Center)
users, your company's single sign-on authentication, and your Google or
Facebook credentials are examples of federated identities. When you sign in as
a federated identity, your administrator previously set up identity federation
using IAM roles. When you access AWS by using federation, you are indirectly
assuming a role.

Depending on the type of user you are, you can sign in to the AWS Management
Console or the AWS access portal. For more information about signing in to
AWS, see [How to sign in to your AWS
account](https://docs.aws.amazon.com/signin/latest/userguide/how-to-sign-
in.html) in the _AWS Sign-In User Guide_.

If you access AWS programmatically, AWS provides a software development kit
(SDK) and a command line interface (CLI) to cryptographically sign your
requests by using your credentials. If you don't use AWS tools, you must sign
requests yourself. For more information about using the recommended method to
sign requests yourself, see [AWS Signature Version 4 for API
requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html)
in the _IAM User Guide_.

Regardless of the authentication method that you use, you might be required to
provide additional security information. For example, AWS recommends that you
use multi-factor authentication (MFA) to increase the security of your
account. To learn more, see [Multi-factor
authentication](https://docs.aws.amazon.com/singlesignon/latest/userguide/enable-
mfa.html) in the _AWS IAM Identity Center User Guide_ and [AWS Multi-factor
authentication in
IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)
in the _IAM User Guide_.

### AWS account root user

When you create an AWS account, you begin with one sign-in identity that has
complete access to all AWS services and resources in the account. This
identity is called the AWS account _root user_ and is accessed by signing in
with the email address and password that you used to create the account. We
strongly recommend that you don't use the root user for your everyday tasks.
Safeguard your root user credentials and use them to perform the tasks that
only the root user can perform. For the complete list of tasks that require
you to sign in as the root user, see [Tasks that require root user
credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-
user.html#root-user-tasks) in the _IAM User Guide_.

### Users and groups

An _[IAM
user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html)_ is an
identity within your AWS account that has specific permissions for a single
person or application. Where possible, we recommend relying on temporary
credentials instead of creating IAM users who have long-term credentials such
as passwords and access keys. However, if you have specific use cases that
require long-term credentials with IAM users, we recommend that you rotate
access keys. For more information, see [Rotate access keys regularly for use
cases that require long-term
credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-
practices.html#rotate-credentials) in the _IAM User Guide_.

An [_IAM
group_](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html) is an
identity that specifies a collection of IAM users. You can't sign in as a
group. You can use groups to specify permissions for multiple users at a time.
Groups make permissions easier to manage for large sets of users. For example,
you could have a group named _IAMAdmins_ and give that group permissions to
administer IAM resources.

Users are different from roles. A user is uniquely associated with one person
or application, but a role is intended to be assumable by anyone who needs it.
Users have permanent long-term credentials, but roles provide temporary
credentials. To learn more, see [Use cases for IAM
users](https://docs.aws.amazon.com/IAM/latest/UserGuide/gs-identities-iam-
users.html) in the _IAM User Guide_.

### IAM roles

An _[IAM
role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)_ is an
identity within your AWS account that has specific permissions. It is similar
to an IAM user, but is not associated with a specific person. To temporarily
assume an IAM role in the AWS Management Console, you can [switch from a user
to an IAM role
(console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-
role-console.html). You can assume a role by calling an AWS CLI or AWS API
operation or by using a custom URL. For more information about methods for
using roles, see [Methods to assume a
role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage-
assume.html) in the _IAM User Guide_.

IAM roles with temporary credentials are useful in the following situations:

  * **Federated user access** â To assign permissions to a federated identity, you create a role and define permissions for the role. When a federated identity authenticates, the identity is associated with the role and is granted the permissions that are defined by the role. For information about roles for federation, see [ Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the _IAM User Guide_. If you use IAM Identity Center, you configure a permission set. To control what your identities can access after they authenticate, IAM Identity Center correlates the permission set to a role in IAM. For information about permissions sets, see [ Permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html) in the _AWS IAM Identity Center User Guide_.

  * **Temporary IAM user permissions** â An IAM user or role can assume an IAM role to temporarily take on different permissions for a specific task.

  * **Cross-account access** â You can use an IAM role to allow someone (a trusted principal) in a different account to access resources in your account. Roles are the primary way to grant cross-account access. However, with some AWS services, you can attach a policy directly to a resource (instead of using a role as a proxy). To learn the difference between roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the _IAM User Guide_.

  * **Cross-service access** â Some AWS services use features in other AWS services. For example, when you make a call in a service, it's common for that service to run applications in Amazon EC2 or store objects in Amazon S3. A service might do this using the calling principal's permissions, using a service role, or using a service-linked role. 

    * **Forward access sessions (FAS)** â When you use an IAM user or role to perform actions in AWS, you are considered a principal. When you use some services, you might perform an action that then initiates another action in a different service. FAS uses the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. FAS requests are only made when a service receives a request that requires interactions with other AWS services or resources to complete. In this case, you must have permissions to perform both actions. For policy details when making FAS requests, see [Forward access sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html). 

    * **Service role** â A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the _IAM User Guide_. 

    * **Service-linked role** â A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles. 

  * **Applications running on Amazon EC2** â You can use an IAM role to manage temporary credentials for applications that are running on an EC2 instance and making AWS CLI or AWS API requests. This is preferable to storing access keys within the EC2 instance. To assign an AWS role to an EC2 instance and make it available to all of its applications, you create an instance profile that is attached to the instance. An instance profile contains the role and enables programs that are running on the EC2 instance to get temporary credentials. For more information, see [Use an IAM role to grant permissions to applications running on Amazon EC2 instances](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html) in the _IAM User Guide_. 

## Managing access using policies

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

### Identity-based policies

Identity-based policies are JSON permissions policy documents that you can
attach to an identity, such as an IAM user, group of users, or role. These
policies control what actions users and roles can perform, on which resources,
and under what conditions. To learn how to create an identity-based policy,
see [Define custom IAM permissions with customer managed
policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html)
in the _IAM User Guide_.

Identity-based policies can be further categorized as _inline policies_ or
_managed policies_. Inline policies are embedded directly into a single user,
group, or role. Managed policies are standalone policies that you can attach
to multiple users, groups, and roles in your AWS account. Managed policies
include AWS managed policies and customer managed policies. To learn how to
choose between a managed policy or an inline policy, see [Choose between
managed policies and inline
policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-
choosing-managed-or-inline.html) in the _IAM User Guide_.

### Resource-based policies

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

### Access Control Lists (ACLs)

Access control lists (ACLs) control which principals (account members, users,
or roles) have permissions to access a resource. ACLs are similar to resource-
based policies, although they do not use the JSON policy document format.

Amazon S3, AWS WAF, and Amazon VPC are examples of services that support ACLs.
To learn more about ACLs, see [Access control list (ACL)
overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-
overview.html) in the _Amazon Simple Storage Service Developer Guide_.

### Other policy types

AWS supports additional, less-common policy types. These policy types can set
the maximum permissions granted to you by the more common policy types.

  * **Permissions boundaries** â A permissions boundary is an advanced feature in which you set the maximum permissions that an identity-based policy can grant to an IAM entity (IAM user or role). You can set a permissions boundary for an entity. The resulting permissions are the intersection of an entity's identity-based policies and its permissions boundaries. Resource-based policies that specify the user or role in the `Principal` field are not limited by the permissions boundary. An explicit deny in any of these policies overrides the allow. For more information about permissions boundaries, see [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in the _IAM User Guide_.

  * **Service control policies (SCPs)** â SCPs are JSON policies that specify the maximum permissions for an organization or organizational unit (OU) in AWS Organizations. AWS Organizations is a service for grouping and centrally managing multiple AWS accounts that your business owns. If you enable all features in an organization, then you can apply service control policies (SCPs) to any or all of your accounts. The SCP limits permissions for entities in member accounts, including each AWS account root user. For more information about Organizations and SCPs, see [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the _AWS Organizations User Guide_.

  * **Resource control policies (RCPs)** â RCPs are JSON policies that you can use to set the maximum available permissions for resources in your accounts without updating the IAM policies attached to each resource that you own. The RCP limits permissions for resources in member accounts and can impact the effective permissions for identities, including the AWS account root user, regardless of whether they belong to your organization. For more information about Organizations and RCPs, including a list of AWS services that support RCPs, see [Resource control policies (RCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) in the _AWS Organizations User Guide_.

  * **Session policies** â Session policies are advanced policies that you pass as a parameter when you programmatically create a temporary session for a role or federated user. The resulting session's permissions are the intersection of the user or role's identity-based policies and the session policies. Permissions can also come from a resource-based policy. An explicit deny in any of these policies overrides the allow. For more information, see [Session policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session) in the _IAM User Guide_. 

### Multiple policy types

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

Data protection

How Amazon MQ works with IAM

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

