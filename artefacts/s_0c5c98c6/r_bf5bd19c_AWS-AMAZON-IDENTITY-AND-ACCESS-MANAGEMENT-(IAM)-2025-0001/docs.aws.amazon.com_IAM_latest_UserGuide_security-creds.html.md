# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html'}

[](/pdfs/IAM/latest/UserGuide/iam-ug.pdf#security-creds "Open PDF")

[Documentation](/index.html)[AWS Identity and Access
Management](/iam/index.html)[User Guide](introduction.html)

Security considerations

# AWS security credentials

When you interact with AWS, you specify your AWS _security credentials_ to
verify who you are and whether you have permission to access the resources
that you are requesting. AWS uses the security credentials to authenticate and
authorize your requests.

For example, if you want to download a protected file from an Amazon Simple
Storage Service (Amazon S3) bucket, your credentials must allow that access.
If your credentials don't show you are authorized to download the file, AWS
denies your request. However, your AWS security credentials aren't required
for you to download a file in an Amazon S3 bucket that is publicly shared.

There are different types of users in AWS, each with their own security
credentials:

  * **Account owner (root user)** â The user who created the AWS account and has full access.

  * **AWS IAM Identity Center users** â Users managed in AWS IAM Identity Center.

  * **Federated users** â Users from external identity providers who are granted temporary access to AWS through federation. For more information about federated identities, see [Identity providers and federation](./id_roles_providers.html).

  * **IAM users** â Individual users created within the AWS Identity and Access Management (IAM) service.

Users have either long-term or temporary security credentials. Root user, IAM
user, and access keys have long-term security credentials that do not expire.
To protect long-term credentials have processes in place to [manage access
keys](./id_credentials_access-keys.html), [change
passwords](./id_credentials_passwords.html), and [enable
MFA](./id_credentials_mfa.html).

To simplify managing root user credentials across member accounts in AWS
Organizations, you can centrally secure the root user credentials of your AWS
accounts managed using AWS Organizations. [Centrally manage root access for
member accounts](./id_root-user.html#id_root-user-access-management) lets you
centrally remove and prevent long-term root user credential recovery,
preventing unintended root access at scale.

IAM roles, users in AWS IAM Identity Center, and federated users have
temporary security credentials. Temporary security credentials expire after a
defined period of time or when the user ends their session. Temporary
credentials work almost identically to long-term credentials, with the
following differences:

  * Temporary security credentials are _short-term_ , as the name implies. They can be configured to last for anywhere from a few minutes to several hours. After the credentials expire, AWS no longer recognizes them or allows any kind of access from API requests made with them.

  * Temporary security credentials are not stored with the user but are generated dynamically and provided to the user when requested. When (or even before) the temporary security credentials expire, the user can request new credentials, as long as the user requesting them still has permissions to do so.

As a result, temporary credentials have the following advantages over long-
term credentials:

  * You do not have to distribute or embed long-term AWS security credentials with an application.

  * You can provide access to your AWS resources to users without having to define an AWS identity for them. Temporary credentials are the basis for [roles and identity federation](./id_roles.html).

  * The temporary security credentials have a limited lifetime, so you do not have to update them or explicitly revoke them when they're no longer needed. After temporary security credentials expire, they cannot be reused. You can specify how long the credentials are valid, up to a maximum limit. 

## Security considerations

We recommend that you consider the following information when determining the
security provisions for your AWS account:

  * When you create an AWS account, we create the account root user. The credentials of the root user (account owner) allow full access to all resources in the account. The first task you perform with the root user is to grant another user administrative permissions to your AWS account so that you minimize the usage of the root user. 

  * Multi-factor authentication (MFA) provides an extra level of security for users who can access your AWS account. For additional security, we recommend that you require MFA on the AWS account root user credentials and all IAM users. For more information, see [AWS Multi-factor authentication in IAM](./id_credentials_mfa.html).

  * AWS requires different types of security credentials, depending on how you access AWS and what type of AWS user you are. For example, you use sign-in credentials for the AWS Management Console while you use access keys to make programmatic calls to AWS. For help determining your user type and sign-in page, see [What is AWS Sign-In](https://docs.aws.amazon.com/signin/latest/userguide/what-is-sign-in.html) in the _AWS Sign-In User Guide_.

  * You can't use IAM policies to deny the root user access to resources explicitly. You can only use an AWS Organizations [service control policy (SCP)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_type-auth.html) to limit the permissions of the root user. 

  * If you forget or lose your root user password, you must have access to the email address associated with your account in order to reset it.

  * If you lose your root user access keys, you must be able to sign in to your account as the root user to create new ones.

  * Do not use the root user for your everyday tasks. Use it to perform the tasks that only the root user can perform. For the complete list of tasks that require you to sign in as the root user, see [Tasks that require root user credentials](./id_root-user.html#root-user-tasks).

  * Security credentials are account-specific. If you have access to multiple AWS accounts, you have separate credentials for each account.

  * [Policies](./access_policies.html) determine what actions a user, role, or member of a user group can perform, on which AWS resources, and under what conditions. Using policies you can securely control access to AWS services and resources in your AWS account. If you must modify or revoke permissions in response to a security event, you delete or modify the policies instead of making changes directly to the identity.

  * Be sure to save the sign-in credentials for your _Emergency Access_ IAM user and any access keys you created for programmatic access in a secure location. If you lose your access keys, you must sign in to your account to create new ones.

  * We strongly recommend that you use temporary credentials provided by IAM roles and federated users instead of the long-term credentials provided by IAM users and access keys.

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Security

Programmatic access

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

