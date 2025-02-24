# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/mgn/latest/ug/cross-service-confused-deputy-prevention.html'}

[](/pdfs/mgn/latest/ug/user-guide.pdf#cross-service-confused-deputy-prevention
"Open PDF")

[Documentation](/index.html)[Application Migration
Service](/mgn/index.html)[User Guide](what-is-application-migration-
service.html)

# Cross-service confused deputy prevention

The confused deputy problem is a security issue where an entity that doesn't
have permission to perform an action can coerce a more-privileged entity to
perform the action. In AWS, cross-service impersonation can result in the
confused deputy problem. Cross-service impersonation can occur when one
service (the _calling service_) calls another service (the _called service_).
The calling service can be manipulated to use its permissions to act on
another customer's resources in a way it should not otherwise have permission
to access. To prevent this, AWS provides tools that help you protect your data
for all services with service principals that have been given access to
resources in your account.

We recommend using the
[`aws:SourceArn`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-
keys.html#condition-keys-sourcearn) and
[`aws:SourceAccount`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-
keys.html#condition-keys-sourceaccount) global condition context keys in
resource policies to limit the permissions that AWS Application Migration
Service gives another service to the resource. If you use both global
condition context keys, the `aws:SourceAccount` value and the account in the
`aws:SourceArn` value must use the same account ID when used in the same
policy statement.

The value of `aws:SourceArn` must be "arn:aws:mgn:*:123456789012:source-
server/*"

The most effective way to protect against the confused deputy problem is to
use the `aws:SourceArn` global condition context key with the full ARN of the
resource. If you don't know the full ARN of the resource or if you are
specifying multiple resources, use the `aws:SourceArn` global context
condition key with wildcards (`*`) for the unknown portions of the ARN. For
example, `arn:aws:`servicename`::`123456789012`:* ` .

The following example shows how you can use the `aws:SourceArn` and
`aws:SourceAccount` global condition context keys in AWS Application Migration
Service to prevent the confused deputy problem.

    
    
    {
            "Version": "2012-10-17",
            "Statement": {
                    "Sid": "ConfusedDeputyPreventionExamplePolicy",
                    "Effect": "Allow",
                    "Principal": {
                            "Service": "mgn.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole",
                    "Condition": {
                            "StringLike": {
                                    "aws:SourceArn": "arn:aws:mgn:*:123456789012:source-server/*",
                                    "aws:SourceAccount": "123456789012"
                            }
                    }
            }
    }
            

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Compliance validation

Troubleshooting

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

