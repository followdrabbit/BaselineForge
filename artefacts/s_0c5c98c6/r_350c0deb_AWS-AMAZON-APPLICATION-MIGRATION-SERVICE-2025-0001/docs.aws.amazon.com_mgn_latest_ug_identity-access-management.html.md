# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/mgn/latest/ug/identity-access-management.html'}

[](/pdfs/mgn/latest/ug/user-guide.pdf#identity-access-management "Open PDF")

[Documentation](/index.html)[Application Migration
Service](/mgn/index.html)[User Guide](what-is-application-migration-
service.html)

Federated identity

# Identity and access management for AWS Application Migration Service

AWS Identity and Access Management (IAM) is an AWS service that helps an
administrator securely control access to AWS resources. IAM administrators
control who can be authenticated (signed in) and authorized (have permissions)
to use AWS resources. IAM enables you to create users and groups under your
AWS account. You control the permissions that users have to perform tasks
using AWS resources. You can use IAM for no additional charge.

By default, users created via the IAM service don't have permissions for AWS
Application Migration Service (AWS MGN) resources and operations. To allow
these users to manage AWS Application Migration Service resources, you must
create an IAM policy that explicitly grants them permissions, and attach the
policy to the users or groups that require those permissions.

When you attach a policy to a user or group of users, it allows or denies the
users permission to perform the specified tasks on the specified resources.
For more information, see [Policies and
Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
in the _IAM User Guide_ guide.

## Federated identity

As a best practice, require human users, including users that require
administrator access, to use federation with an identity provider to access
AWS services by using temporary credentials.

A _federated identity_ is a user from your enterprise user directory, a web
identity provider, the AWS Directory Service, the Identity Center directory,
or any user that accesses AWS services by using credentials provided through
an identity source. When federated identities access AWS accounts, they assume
roles, and the roles provide temporary credentials.

For centralized access management, we recommend that you use AWS IAM Identity
Center. You can create users and groups in IAM Identity Center, or you can
connect and synchronize to a set of users and groups in your own identity
source for use across all your AWS accounts and applications. For information
about IAM Identity Center, see [What is IAM Identity
Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-
is.html) in the _AWS IAM Identity Center User Guide_.

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Security

Authenticating with identities

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

