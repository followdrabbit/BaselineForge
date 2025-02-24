# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/servicecatalog/latest/adminguide/controlling_access.html'}

[](/pdfs/servicecatalog/latest/adminguide/service-catalog-
ag.pdf#controlling_access "Open PDF")

[Documentation](/index.html)[AWS Service
Catalog](/servicecatalog/index.html)[Administrator Guide](introduction.html)

Audience

# Identity and Access Management in AWS Service Catalog

Access to AWS Service Catalog requires credentials. Those credentials must
have permission to access AWS resources, such as a AWS Service Catalog
portfolio or product. AWS Service Catalog integrates with AWS Identity and
Access Management (IAM) to enable you to grant AWS Service Catalog
administrators the permissions they need to create and manage products, and to
grant AWS Service Catalog end users the permissions they need to launch
products and manage provisioned products. These policies are either created
and managed by AWS or individually by administrators and end users. To control
access, you attach these policies to users, groups, and roles that you use
with AWS Service Catalog.

## Audience

The permissions you have _with_ AWS Identity and Access Management (IAM) can
depend on the role you play in AWS Service Catalog.

The permissions you have _through_ AWS Identity and Access Management (IAM)
can also depend on the role you play in AWS Service Catalog.

**Administrator** \- As a AWS Service Catalog administrator, you need full
access to the administrator console and IAM permissions that allow you to
perform tasks such as creating and managing portfolios and products, managing
constraints, and granting access to end users.

**End user** \- Before your end users can use your products, you need to grant
them permissions that give them access to the AWS Service Catalog end user
console. They can also have permissions to launch products and manage
provisioned products.

**IAM administrator** \- If you're an IAM administrator, you might want to
learn details about how you can write policies to manage access to AWS Service
Catalog. To view example AWS Service Catalog identity-based policies that you
can use in IAM, see [AWS managed policies for AWS Service Catalog
AppRegistry](./security-iam-awsmanpol.html).

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Data Protection

Identity-based policy examples for AWS Service Catalog

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

