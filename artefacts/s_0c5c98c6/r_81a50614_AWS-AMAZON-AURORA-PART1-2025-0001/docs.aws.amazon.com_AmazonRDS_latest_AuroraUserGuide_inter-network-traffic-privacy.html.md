# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/inter-network-traffic-privacy.html'}

[](/pdfs/AmazonRDS/latest/AuroraUserGuide/aurora-ug.pdf#inter-network-traffic-
privacy "Open PDF")

[Documentation](/index.html)[Amazon RDS](/rds/index.html)[User Guide for
Aurora](CHAP_AuroraOverview.html)

Traffic between service and on-premises clients and applications

# Internetwork traffic privacy

Connections are protected both between Amazon Aurora and on-premises
applications and between Amazon Aurora and other AWS resources within the same
AWS Region.

## Traffic between service and on-premises clients and applications

You have two connectivity options between your private network and AWS:

  * An AWS Site-to-Site VPN connection. For more information, see [What is AWS Site-to-Site VPN?](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)

  * An AWS Direct Connect connection. For more information, see [What is AWS Direct Connect?](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)

You get access to Amazon Aurora through the network by using AWS-published API
operations. Clients must support the following:

  * Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.

  * Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

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

Rotating your SSL/TLS certificate

Identity and access management

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

