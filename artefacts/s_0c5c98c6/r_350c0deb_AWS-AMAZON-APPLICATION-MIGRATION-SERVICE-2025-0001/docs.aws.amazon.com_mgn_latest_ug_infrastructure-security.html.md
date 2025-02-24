# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/mgn/latest/ug/infrastructure-security.html'}

[](/pdfs/mgn/latest/ug/user-guide.pdf#infrastructure-security "Open PDF")

[Documentation](/index.html)[Application Migration
Service](/mgn/index.html)[User Guide](what-is-application-migration-
service.html)

# Infrastructure security in AWS Application Migration Service

As a managed service, AWS Application Migration Service is protected by the
AWS global network security procedures that are described in the [Amazon Web
Services: Overview of Security Processes
](https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf)
whitepaper.

You use AWS published API calls to access AWS Application Migration Service
through the network. Clients must support Transport Layer Security (TLS) 1.2
or later. Clients must also support cipher suites with perfect forward secrecy
(PFS) such as Ephemeral Diffie-Hellman (DHE) or Elliptic Curve Ephemeral
Diffie-Hellman (ECDHE). Most modern systems such as Java 7 and later support
these modes.

All parties involved in the communication authenticate each other using TLS,
IAM policies and tokens. The communication between the Agents and the
replication server are based on TLS 1.2 only with the highest standard of
cipher suite (PFS, ECDHE. Requests between the agent and AWS Application
Migration Service as well as between the replication server and Application
Migration Service are signed using an access key ID and a secret access key
that is associated with an IAM principal).

All requests must be signed using the [AWS Security Token
Service](https://docs.aws.amazon.com/STS/latest/APIReference/Welcome.html)
(AWS STS), which allows you to generate temporary security credentials to sign
requests. Alternatively, use credentials that associated with an IAM
principal.

AWS Application Migration Service customers must ensure that they manually
delete their access keys after installing the AWS Replication Agent and
successful migration. AWS does not delete these keys automatically. AWS
Application Migration Service does delete the keys from source servers after
they are disconnected from the service. If you want your keys to automatically
stop working at a certain date after you have finished using them so that you
do not have to worry about manually deleting them, you can do so though the
[IAM permissions
boundary](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)
and the [aws:CurrentTime global context
key](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-
keys.html#condition-keys-currenttime).

AWS Application Migration Service customers should use [Amazon EBS
encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html).

AWS Application Migration Service customers should secure their replication
servers by reducing their exposure to the public internet. This can be done
through:

  1. Using security groups to only allow permitted IP addresses to connect to the replication servers. [Learn more about Security Groups. ](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

  2. Using a VPN to connect to the replication servers, such as the AWS site-to-site VPN. [Learn more about the AWS Site-to-site VPN. ](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)

AWS Application Migration Service creates and uses the "aws-replication" user
within the Linux Source server. The AWS Application Migration Service
replication server and AWS Replication Agent run under this user. Although
this is not a root user, this user needs to be part of the disk group that
grants this user full read and write permissions to block devices.

###### Note

AWS Application Migration Service only uses these permissions to read from
block devices.

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Resilience

Compliance validation

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

