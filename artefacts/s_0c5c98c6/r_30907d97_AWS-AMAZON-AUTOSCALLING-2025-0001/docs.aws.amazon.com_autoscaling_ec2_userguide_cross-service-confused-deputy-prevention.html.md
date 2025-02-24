# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/autoscaling/ec2/userguide/cross-service-confused-deputy-prevention.html'}

[](/pdfs/autoscaling/ec2/userguide/as-dg.pdf#cross-service-confused-deputy-
prevention "Open PDF")

[Documentation](/index.html)[Auto Scaling](/autoscaling/index.html)[User
Guide](what-is-amazon-ec2-auto-scaling.html)

Example: Using aws:SourceArn and aws:SourceAccount condition keysAdditional
information

# Cross-service confused deputy prevention

The confused deputy problem is a security issue where an entity that doesn't
have permission to perform an action can coerce a more-privileged entity to
perform the action.

In AWS, cross-service impersonation can result in the confused deputy problem.
Cross-service impersonation can occur when one service (the _calling service_)
calls another service (the _called service_). The calling service can be
manipulated to use its permissions to act on another customer's resources in a
way it should not otherwise have permission to access.

To prevent this, AWS provides tools that help you protect your data for all
services with service principals that have been given access to resources in
your account. We recommend using the
[`aws:SourceArn`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-
keys.html#condition-keys-sourcearn) and
[`aws:SourceAccount`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-
keys.html#condition-keys-sourceaccount) global condition context keys in trust
policies for Amazon EC2 Auto Scaling service roles. These keys limit the
permissions that Amazon EC2 Auto Scaling gives another service to the
resource.

The values for the `SourceArn` and `SourceAccount` fields are set when Amazon
EC2 Auto Scaling uses AWS Security Token Service (AWS STS) to assume a role on
your behalf.

To use the `aws:SourceArn` or `aws:SourceAccount` global condition keys, set
the value to the Amazon Resource Name (ARN) or account of the resource that
Amazon EC2 Auto Scaling stores. Whenever possible, use `aws:SourceArn`, which
is more specific. Set the value to the ARN or an ARN pattern with wildcards
(`*`) for the unknown portions of the ARN. If you don't know the ARN of the
resource, use `aws:SourceAccount` instead.

The following example shows how you can use the `aws:SourceArn` and
`aws:SourceAccount` global condition context keys in Amazon EC2 Auto Scaling
to prevent the confused deputy problem.

## Example: Using `aws:SourceArn` and `aws:SourceAccount` condition keys

A role that a service assumes to perform actions on your behalf is called a
[service role](./control-access-using-iam.html#security_iam_service-with-iam-
roles-service). In cases where you want to create lifecycle hooks that send
notifications to anywhere other than Amazon EventBridge, you must create a
service role to allow Amazon EC2 Auto Scaling to send notifications to an
Amazon SNS topic or Amazon SQS queue on your behalf. If you want only one Auto
Scaling group to be associated with the cross-service access, you can specify
the trust policy of the service role as follows.

This example trust policy uses condition statements to limit the `AssumeRole`
capability on the service role to only the actions that affect the specified
Auto Scaling group in the specified account. The `aws:SourceArn` and
`aws:SourceAccount` conditions are evaluated independently. Any request to use
the service role must satisfy both conditions.

Before using this policy, replace the Region, account ID, UUID, and group name
with valid values from your account.

    
    
    {
      "Version": "2012-10-17",
      "Statement": {
        "Sid": "ConfusedDeputyPreventionExamplePolicy",
        "Effect": "Allow",
        "Principal": {
          "Service": "autoscaling.amazonaws.com"
        },
        "Action": "sts:AssumeRole",
        "Condition": {
          "ArnLike": {
            "aws:SourceArn": "arn:aws:autoscaling:region:account_id:autoScalingGroup:uuid:autoScalingGroupName/my-asg"
          },
          "StringEquals": {
            "aws:SourceAccount": "account_id"
          }
        }
      }
    }

In the preceding example:

  * The `Principal` element specifies the service principal of the service (`autoscaling.amazonaws.com`).

  * The `Action` element specifies the `sts:AssumeRole` action.

  * The `Condition` element specifies the `aws:SourceArn` and `aws:SourceAccount` global condition keys. The source's ARN includes the account ID, so it is not necessary to use `aws:SourceAccount` with `aws:SourceArn`.

## Additional information

For more information, see [AWS global condition context
keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-
keys.html), [The confused deputy
problem](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-
deputy.html), and [Update a role trust
policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-role-
trust-policy.html) in the _IAM User Guide_.

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Identity-based policy examples

Control Amazon EC2 launch template usage in Auto Scaling groups

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

