# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/servicecatalog/latest/adminguide/infrastructure-security.html'}

[](/pdfs/servicecatalog/latest/adminguide/service-catalog-
ag.pdf#infrastructure-security "Open PDF")

[Documentation](/index.html)[AWS Service
Catalog](/servicecatalog/index.html)[Administrator Guide](introduction.html)

# Infrastructure Security in AWS Service Catalog

As a managed service, AWS Service Catalog is protected by AWS global network
security. For information about AWS security services and how AWS protects
infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To
design your AWS environment using the best practices for infrastructure
security, see [Infrastructure
Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-
pillar/infrastructure-protection.html) in _Security Pillar AWS
WellâArchitected Framework_.

You use AWS published API calls to access AWS Service Catalog through the
network. Clients must support the following:

  * Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.

  * Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

Additionally, requests must be signed by using an access key ID and a secret
access key that is associated with an IAM principal. Or you can use the [AWS
Security Token
Service](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html)
(AWS STS) to generate temporary security credentials to sign requests.

With AWS Service Catalog, you can control the Regions in which data is stored.
Portfolios and products are only available in the Regions in which you have
made them available. You can use the `CopyProduct` API to copy a product to
another Region.

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Resilience

Security Best Practices

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

