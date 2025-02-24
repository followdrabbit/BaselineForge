# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security-best-practices.html'}

[](/pdfs/servicecatalog/latest/adminguide/service-catalog-ag.pdf#security-
best-practices "Open PDF")

[Documentation](/index.html)[AWS Service
Catalog](/servicecatalog/index.html)[Administrator Guide](introduction.html)

# Security Best Practices for AWS Service Catalog

AWS Service Catalog provides a number of security features to consider as you
develop and implement your own security policies. The following best practices
are general guidelines and donât represent a complete security solution.
Because these best practices might not be appropriate or sufficient for your
environment, treat them as helpful considerations rather than prescriptions.

You can define rules that limit the parameter values that a user enters when
launching a product. These rules are called template constraints because they
constrain how the AWS CloudFormation template for the product is deployed. You
use a simple editor to create template constraints, and you apply them to
individual products.

AWS Service Catalog applies constraints when provisioning a new product or
updating a product that is already in use. It always applies the most
restrictive constraint among all constraints applied to the portfolio and the
product. For example, consider a scenario where the product allows all Amazon
EC2 instances to be launched and the portfolio has two constraints: one that
allows all non-GPU type EC2 instances to be launched and one that allows only
t1.micro and m1.small EC2 instances to be launched. For this example, AWS
Service Catalog applies the second, more restrictive constraint (t1.micro and
m1.small).

You can limit the access end users have to AWS resources when you attach an
IAM policy to a launch role. You then use AWS Service Catalog to create a
launch constraint to use the role when launching the product.

To learn more about managed policies for AWS Service Catalog, see [AWS Managed
Policies for AWS Service Catalog.](./security-iam-awsmanpol.html)

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Infrastructure Security

Managing Catalogs

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

