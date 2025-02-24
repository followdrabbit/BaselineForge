# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-in-transit.html'}

[](/pdfs/directconnect/latest/UserGuide/dc-ug.pdf#encryption-in-transit "Open
PDF")

[Documentation](/index.html)[AWS Direct
Connect](/directconnect/index.html)[User Guide](Welcome.html)

# Encryption in AWS Direct Connect

AWS Direct Connect does not encrypt your traffic that is in transit by
default. To encrypt the data in transit that traverses AWS Direct Connect, you
must use the transit encryption options for that service. To learn about EC2
instance traffic encryption, see [Encryption in
Transit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-
protection.html#encryption-transit) in the Amazon EC2 User Guide.

With AWS Direct Connect and AWS Site-to-Site VPN, you can combine one or more
AWS Direct Connect dedicated network connections with the Amazon VPC VPN. This
combination provides an IPsec-encrypted private connection that also reduces
network costs, increases bandwidth throughput, and provides a more consistent
network experience than internet-based VPN connections. For more information,
see [Amazon VPC-to-Amazon VPC Connectivity
Options](https://aws.amazon.com/answers/networking/aws-single-data-center-ha-
network-connectivity/).

MAC Security (MACsec) is an IEEE standard that provides data confidentiality,
data integrity, and data origin authenticity. You can use AWS Direct Connect
connections that support MACsec to encrypt your data from your corporate data
center to the AWS Direct Connect location. For more information, see [MAC
Security in AWS Direct Connect](./MACsec.html).

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Internetwork traffic privacy

Identity and Access Management

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

