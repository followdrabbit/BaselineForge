# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/infrastructure-security.html'}

[](/pdfs/AmazonRDS/latest/AuroraUserGuide/aurora-ug.pdf#infrastructure-
security "Open PDF")

[Documentation](/index.html)[Amazon RDS](/rds/index.html)[User Guide for
Aurora](CHAP_AuroraOverview.html)

Security groupsPublic accessibility

# Infrastructure security in Amazon Aurora

As a managed service, Amazon Relational Database Service is protected by AWS
global network security. For information about AWS security services and how
AWS protects infrastructure, see [AWS Cloud
Security](https://aws.amazon.com/security/). To design your AWS environment
using the best practices for infrastructure security, see [Infrastructure
Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-
pillar/infrastructure-protection.html) in _Security Pillar AWS
WellâArchitected Framework_.

You use AWS published API calls to access Amazon RDS through the network.
Clients must support the following:

  * Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.

  * Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

Additionally, requests must be signed by using an access key ID and a secret
access key that is associated with an IAM principal. Or you can use the [AWS
Security Token
Service](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html)
(AWS STS) to generate temporary security credentials to sign requests.

In addition, Aurora offers features to help support infrastructure security.

## Security groups

Security groups control the access that traffic has in and out of a DB
cluster. By default, network access is turned off to a DB cluster. You can
specify rules in a security group that allow access from an IP address range,
port, or security group. After ingress rules are configured, the same rules
apply to all DB clusters that are associated with that security group.

For more information, see [Controlling access with security
groups](./Overview.RDSSecurityGroups.html).

## Public accessibility

When you launch a DB instance inside a virtual private cloud (VPC) based on
the Amazon VPC service, you can turn on or off public accessibility for that
DB instance. To designate whether the DB instance that you create has a DNS
name that resolves to a public IP address, you use the _Public accessibility_
parameter. By using this parameter, you can designate whether there is public
access to the DB instance. You can modify a DB instance to turn on or off
public accessibility by modifying the _Public accessibility_ parameter.

For more information, see [Hiding a DB cluster in a VPC from the
internet](./USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.Hiding).

###### Note

If your DB instance is in a VPC but isn't publicly accessible, you can also
use an AWS Site-to-Site VPN connection or an AWS Direct Connect connection to
access it from a private network. For more information, see [Internetwork
traffic privacy](./inter-network-traffic-privacy.html).

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Resilience

VPC endpoints (AWS PrivateLink)

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

