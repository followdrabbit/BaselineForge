# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/amazonswf/latest/developerguide/infrastructure-security.html'}

[](/pdfs/amazonswf/latest/developerguide/swf-dg.pdf#infrastructure-security
"Open PDF")

[Documentation](/index.html)[Amazon Simple Workflow
Service](/swf/index.html)[Developer Guide](swf-welcome.html)

# Infrastructure Security in Amazon Simple Workflow Service

As a managed service, Amazon Simple Workflow Service is protected by the AWS
global network security procedures that are described in the [Amazon Web
Services: Overview of Security
Processes](https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf)
whitepaper.

You use AWS published API calls to access Amazon SWF through the network.
Clients must support Transport Layer Security (TLS) 1.0 or later. We recommend
TLS 1.2 or later. Clients must also support cipher suites with perfect forward
secrecy (PFS) such as Ephemeral Diffie-Hellman (DHE) or Elliptic Curve
Ephemeral Diffie-Hellman (ECDHE). Most modern systems such as Java 7 and later
support these modes.

Additionally, requests must be signed by using an access key ID and a secret
access key that is associated with an IAM principal. Or you can use the [AWS
Security Token
Service](https://docs.aws.amazon.com/STS/latest/APIReference/Welcome.html)
(AWS STS) to generate temporary security credentials to sign requests.

You can call these API operations from any network location, but Amazon SWF
does support resource-based access policies, which can include restrictions
based on the source IP address. You can also use Amazon SWF policies to
control access from specific Amazon Virtual Private Cloud (Amazon VPC)
endpoints or specific VPCs. Effectively, this isolates network access to a
given Amazon SWF resource from only the specific VPC within the AWS network.

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Resilience

Configuration and Vulnerability Analysis

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

