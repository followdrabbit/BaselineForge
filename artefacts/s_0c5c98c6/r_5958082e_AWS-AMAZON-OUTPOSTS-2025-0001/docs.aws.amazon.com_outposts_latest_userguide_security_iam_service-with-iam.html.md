# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/outposts/latest/userguide/security_iam_service-with-iam.html'}

[](/pdfs/outposts/latest/userguide/outposts-rack.pdf#security_iam_service-
with-iam "Open PDF")

[Documentation](/index.html)[AWS Outposts](/outposts/index.html)[User Guide
for Outposts racks](what-is-outposts.html)

Identity-based policiesPolicy actionsPolicy resourcesPolicy condition
keysABACTemporary credentialsPrincipal permissionsService-linked roles

# How AWS Outposts works with IAM

Before you use IAM to manage access to AWS Outposts, learn what IAM features
are available to use with AWS Outposts.

IAM feature | AWS Outposts support  
---|---  
Identity-based policies |  Yes  
Resource-based policies |  No   
Policy actions |  Yes  
Policy resources |  Yes  
Policy condition keys (service-specific) |  Yes  
ACLs |  No   
ABAC (tags in policies) |  Yes  
Temporary credentials |  Yes  
Principal permissions |  Yes  
Service roles |  No   
Service-linked roles |  Yes  
  
## Identity-based policies for AWS Outposts

**Supports identity-based policies:** Yes

Identity-based policies are JSON permissions policy documents that you can
attach to an identity, such as an IAM user, group of users, or role. These
policies control what actions users and roles can perform, on which resources,
and under what conditions. To learn how to create an identity-based policy,
see [Define custom IAM permissions with customer managed
policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html)
in the _IAM User Guide_.

With IAM identity-based policies, you can specify allowed or denied actions
and resources as well as the conditions under which actions are allowed or
denied. You can't specify the principal in an identity-based policy because it
applies to the user or role to which it is attached. To learn about all of the
elements that you can use in a JSON policy, see [IAM JSON policy elements
reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html)
in the _IAM User Guide_.

###  Identity-based policy examples for AWS Outposts

To view examples of AWS Outposts identity-based policies, see [AWS Outposts
policy examples](./security_iam_id-based-policy-examples.html).

## Policy actions for AWS Outposts

**Supports policy actions:** Yes

Administrators can use AWS JSON policies to specify who has access to what.
That is, which **principal** can perform **actions** on what **resources** ,
and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use
to allow or deny access in a policy. Policy actions usually have the same name
as the associated AWS API operation. There are some exceptions, such as
_permission-only actions_ that don't have a matching API operation. There are
also some operations that require multiple actions in a policy. These
additional actions are called _dependent actions_.

Include actions in a policy to grant permissions to perform the associated
operation.

To see a list of AWS Outposts actions, see [Actions defined by AWS
Outposts](https://docs.aws.amazon.com/service-
authorization/latest/reference/list_awsoutposts.html#awsoutposts-actions-as-
permissions) in the _Service Authorization Reference_.

Policy actions in AWS Outposts use the following prefix before the action:

    
    
    outposts

To specify multiple actions in a single statement, separate them with commas.

    
    
    "Action": [
        "outposts:action1",
        "outposts:action2"
    ]

You can specify multiple actions using wildcards (*). For example, to specify
all actions that begin with the word `List`, include the following action:

    
    
    "Action": "outposts:List*"

## Policy resources for AWS Outposts

**Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what.
That is, which **principal** can perform **actions** on what **resources** ,
and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which
the action applies. Statements must include either a `Resource` or a
`NotResource` element. As a best practice, specify a resource using its
[Amazon Resource Name
(ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html).
You can do this for actions that support a specific resource type, known as
_resource-level permissions_.

For actions that don't support resource-level permissions, such as listing
operations, use a wildcard (*) to indicate that the statement applies to all
resources.

    
    
    "Resource": "*"

Some AWS Outposts API actions support multiple resources. To specify multiple
resources in a single statement, separate the ARNs with commas.

    
    
    "Resource": [
        "resource1",
        "resource2"
    ]

To see a list of AWS Outposts resource types and their ARNs, see [Resource
types defined by AWS Outposts](https://docs.aws.amazon.com/service-
authorization/latest/reference/list_awsoutposts.html#awsoutposts-resources-
for-iam-policies) in the _Service Authorization Reference_. To learn with
which actions you can specify the ARN of each resource, see [Actions defined
by AWS Outposts](https://docs.aws.amazon.com/service-
authorization/latest/reference/list_awsoutposts.html#awsoutposts-actions-as-
permissions).

## Policy condition keys for AWS Outposts

**Supports service-specific policy condition keys:** Yes

Administrators can use AWS JSON policies to specify who has access to what.
That is, which **principal** can perform **actions** on what **resources** ,
and under what **conditions**.

The `Condition` element (or `Condition` _block_) lets you specify conditions
in which a statement is in effect. The `Condition` element is optional. You
can create conditional expressions that use [condition
operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html),
such as equals or less than, to match the condition in the policy with values
in the request.

If you specify multiple `Condition` elements in a statement, or multiple keys
in a single `Condition` element, AWS evaluates them using a logical `AND`
operation. If you specify multiple values for a single condition key, AWS
evaluates the condition using a logical `OR` operation. All of the conditions
must be met before the statement's permissions are granted.

You can also use placeholder variables when you specify conditions. For
example, you can grant an IAM user permission to access a resource only if it
is tagged with their IAM user name. For more information, see [IAM policy
elements: variables and
tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html)
in the _IAM User Guide_.

AWS supports global condition keys and service-specific condition keys. To see
all AWS global condition keys, see [AWS global condition context
keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-
keys.html) in the _IAM User Guide_.

To see a list of AWS Outposts condition keys, see [Condition keys for AWS
Outposts](https://docs.aws.amazon.com/service-
authorization/latest/reference/list_awsoutposts.html#awsoutposts-policy-keys)
in the _Service Authorization Reference_. To learn with which actions and
resources you can use a condition key, see [Actions defined by AWS
Outposts](https://docs.aws.amazon.com/service-
authorization/latest/reference/list_awsoutposts.html#awsoutposts-actions-as-
permissions).

To view examples of AWS Outposts identity-based policies, see [AWS Outposts
policy examples](./security_iam_id-based-policy-examples.html).

## ABAC with AWS Outposts

**Supports ABAC (tags in policies):** Yes

Attribute-based access control (ABAC) is an authorization strategy that
defines permissions based on attributes. In AWS, these attributes are called
_tags_. You can attach tags to IAM entities (users or roles) and to many AWS
resources. Tagging entities and resources is the first step of ABAC. Then you
design ABAC policies to allow operations when the principal's tag matches the
tag on the resource that they are trying to access.

ABAC is helpful in environments that are growing rapidly and helps with
situations where policy management becomes cumbersome.

To control access based on tags, you provide tag information in the [condition
element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html)
of a policy using the `aws:ResourceTag/`key-name``, `aws:RequestTag/`key-
name``, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then
the value is **Yes** for the service. If a service supports all three
condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC
authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-
based-access-control.html) in the _IAM User Guide_. To view a tutorial with
steps for setting up ABAC, see [Use attribute-based access control
(ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-
based-access-control.html) in the _IAM User Guide_.

## Using temporary credentials with AWS Outposts

**Supports temporary credentials:** Yes

Some AWS services don't work when you sign in using temporary credentials. For
additional information, including which AWS services work with temporary
credentials, see [AWS services that work with
IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-
that-work-with-iam.html) in the _IAM User Guide_.

You are using temporary credentials if you sign in to the AWS Management
Console using any method except a user name and password. For example, when
you access AWS using your company's single sign-on (SSO) link, that process
automatically creates temporary credentials. You also automatically create
temporary credentials when you sign in to the console as a user and then
switch roles. For more information about switching roles, see [Switch from a
user to an IAM role
(console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-
role-console.html) in the _IAM User Guide_.

You can manually create temporary credentials using the AWS CLI or AWS API.
You can then use those temporary credentials to access AWS. AWS recommends
that you dynamically generate temporary credentials instead of using long-term
access keys. For more information, see [Temporary security credentials in
IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html).

## Cross-service principal permissions for AWS Outposts

**Supports forward access sessions (FAS):** Yes

When you use an IAM user or role to perform actions in AWS, you are considered
a principal. When you use some services, you might perform an action that then
initiates another action in a different service. FAS uses the permissions of
the principal calling an AWS service, combined with the requesting AWS service
to make requests to downstream services. FAS requests are only made when a
service receives a request that requires interactions with other AWS services
or resources to complete. In this case, you must have permissions to perform
both actions. For policy details when making FAS requests, see [Forward access
sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html).

## Service-linked roles for AWS Outposts

**Supports service-linked roles:** Yes

A service-linked role is a type of service role that is linked to an AWS
service. The service can assume the role to perform an action on your behalf.
Service-linked roles appear in your AWS account and are owned by the service.
An IAM administrator can view, but not edit the permissions for service-linked
roles.

For details about creating or managing AWS Outposts service-linked roles, see
[Service-linked roles for AWS Outposts](./using-service-linked-roles.html).

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Identity and access management

Policy examples

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

