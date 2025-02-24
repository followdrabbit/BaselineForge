# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/infrastructure-security.html'}

[](/pdfs/datapipeline/latest/DeveloperGuide/datapipeline-
dg.pdf#infrastructure-security "Open PDF")

[Documentation](/index.html)[AWS Data Pipeline](/data-
pipeline/index.html)[Developer Guide](what-is-datapipeline.html)

AWS Data Pipeline is no longer available to new customers. Existing customers
of AWS Data Pipeline can continue to use the service as normal. [Learn
more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-
pipeline/)

# Infrastructure Security in AWS Data Pipeline

As a managed service, AWS Data Pipeline is protected by the AWS global network
security procedures that are described in the [Amazon Web Services: Overview
of Security
Processes](https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf)
whitepaper.

You use AWS published API calls to access AWS Data Pipeline through the
network. Clients must support Transport Layer Security (TLS) 1.0 or later. We
recommend TLS 1.2 or later. Clients must also support cipher suites with
perfect forward secrecy (PFS) such as Ephemeral Diffie-Hellman (DHE) or
Elliptic Curve Ephemeral Diffie-Hellman (ECDHE). Most modern systems such as
Java 7 and later support these modes.

Additionally, requests must be signed by using an access key ID and a secret
access key that is associated with an IAM principal. Or you can use the [AWS
Security Token
Service](https://docs.aws.amazon.com/STS/latest/APIReference/Welcome.html)
(AWS STS) to generate temporary security credentials to sign requests.

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Resilience

Configuration and Vulnerability Analysis in AWS Data Pipeline

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

