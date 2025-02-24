# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/outposts/latest/userguide/infrastructure-security.html'}

[](/pdfs/outposts/latest/userguide/outposts-rack.pdf#infrastructure-security
"Open PDF")

[Documentation](/index.html)[AWS Outposts](/outposts/index.html)[User Guide
for Outposts racks](what-is-outposts.html)

Tamper monitoring

# Infrastructure security in AWS Outposts

As a managed service, AWS Outposts is protected by AWS global network
security. For information about AWS security services and how AWS protects
infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To
design your AWS environment using the best practices for infrastructure
security, see [Infrastructure
Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-
pillar/infrastructure-protection.html) in _Security Pillar AWS
WellâArchitected Framework_.

You use AWS published API calls to access AWS Outposts through the network.
Clients must support the following:

  * Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.

  * Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

Additionally, requests must be signed by using an access key ID and a secret
access key that is associated with an IAM principal. Or you can use the [AWS
Security Token
Service](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html)
(AWS STS) to generate temporary security credentials to sign requests.

For more information about the infrastructure security provided for the EC2
instances and EBS volumes running on your Outpost, see [Infrastructure
Security in Amazon
EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/infrastructure-
security.html).

VPC Flow Logs function the same way as they do in an AWS Region. This means
that they can be published to CloudWatch Logs, Amazon S3, or to Amazon
GuardDuty for analysis. Data needs to be sent back to the Region for
publication to these services, so it is not visible from CloudWatch or other
services when the Outpost is in a disconnected state.

## Tamper monitoring on AWS Outposts equipment

Ensure that no one modifies, alters, reverse engineers, or tampers with the
AWS Outposts equipment. AWS Outposts equipment may be equipped with tamper
monitoring to ensure compliance with the [AWS Service
Terms](https://aws.amazon.com/service-terms/).

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

AWS managed policies

Resilience

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

