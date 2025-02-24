# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/directconnect/latest/UserGuide/infrastructure-security.html'}

[](/pdfs/directconnect/latest/UserGuide/dc-ug.pdf#infrastructure-security
"Open PDF")

[Documentation](/index.html)[AWS Direct
Connect](/directconnect/index.html)[User Guide](Welcome.html)

Border Gateway Protocol

# Infrastructure security in AWS Direct Connect

As a managed service, AWS Direct Connect is protected by the AWS global
network security procedures. You use AWS published API calls to access AWS
Direct Connect through the network. Clients must support Transport Layer
Security (TLS) 1.2 or later. We recommend TLS 1.3. Clients must also support
cipher suites with perfect forward secrecy (PFS) such as Ephemeral Diffie-
Hellman (DHE) or Elliptic Curve Ephemeral Diffie-Hellman (ECDHE). Most modern
systems such as Java 7 and later support these modes.

Additionally, requests must be signed by using an access key ID and a secret
access key that is associated with an IAM principal. Or you can use the [AWS
Security Token
Service](https://docs.aws.amazon.com/STS/latest/APIReference/Welcome.html)
(AWS STS) to generate temporary security credentials to sign requests.

You can call these API operations from any network location, but AWS Direct
Connect supports resource-based access policies, which can include
restrictions based on the source IP address. You can also use AWS Direct
Connect policies to control access from specific Amazon Virtual Private Cloud
(Amazon VPC) endpoints or specific VPCs. Effectively, this isolates network
access to a given AWS Direct Connect resource from only the specific VPC
within the AWS network. For example, see [Identity-based policy examples for
Direct Connect](./security_iam_id-based-policy-examples.html).

## Border Gateway Protocol (BGP) security

The internet relies in large part on BGP for routing information between
network systems. BGP routing can some times be susceptible to malicious
attacks, or BGP hijacking. To understand how AWS works to more securely
safeguard your network from BGP hijacking, see [How AWS is helping to secure
internet routing](https://aws.amazon.com/blogs/networking-and-content-
delivery/how-aws-is-helping-to-secure-internet-routing).

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Resilience in Direct Connect

Use the AWS CLI

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

