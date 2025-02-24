# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html'}

[](/pdfs/datapipeline/latest/DeveloperGuide/datapipeline-dg.pdf#dp-control-
access "Open PDF")

[Documentation](/index.html)[AWS Data Pipeline](/data-
pipeline/index.html)[Developer Guide](what-is-datapipeline.html)

AWS Data Pipeline is no longer available to new customers. Existing customers
of AWS Data Pipeline can continue to use the service as normal. [Learn
more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-
pipeline/)

# Identity and Access Management for AWS Data Pipeline

Your security credentials identify you to services in AWS and grant you
permissions to use AWS resources, such as your pipelines. You can use features
of AWS Data Pipeline and AWS Identity and Access Management (IAM) to allow AWS
Data Pipeline and other users to access your AWS Data Pipeline resources
without sharing your security credentials.

Organizations can share access to pipelines so that the individuals in that
organization can develop and maintain them collaboratively. However, for
example, it might be necessary to do the following:

  * Control which users can access specific pipelines

  * Protect a production pipeline from being edited by mistake

  * Allow an auditor to have read-only access to pipelines, but prevent them from making changes

AWS Data Pipeline is integrated with AWS Identity and Access Management (IAM),
which offers a wide range of features:

  * Create users and groups in your AWS account.

  * Easily share your AWS resources between the users in your AWS account.

  * Assign unique security credentials to each user.

  * Control each user's access to services and resources.

  * Get a single bill for all users in your AWS account.

By using IAM with AWS Data Pipeline, you can control whether users in your
organization can perform a task using specific API actions and whether they
can use specific AWS resources. You can use IAM policies based on pipeline
tags and worker groups to share your pipelines with other users and control
the level of access they have.

###### Contents

  * [IAM Policies for AWS Data Pipeline](./dp-iam-resourcebased-access.html)
  * [Example Policies for AWS Data Pipeline](./dp-example-tag-policies.html)
  * [IAM Roles for AWS Data Pipeline](./dp-iam-roles.html)

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Data Protection

IAM Policies for AWS Data Pipeline

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

