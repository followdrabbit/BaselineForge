# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html'}

[](/pdfs/vpc/latest/userguide/vpc-ug.pdf#security-vpc-bpa "Open PDF")

[Documentation](/index.html)[Amazon VPC](/vpc/index.html)[User Guide](what-is-
amazon-vpc.html)

# Block public access to VPCs and subnets

VPC Block Public Access (BPA) is a centralized security feature that enables
you to authoritatively prevent public internet access to VPC resources across
an entire AWS account, ensuring compliance with security requirements while
providing flexibility for specific exceptions and audit capabilities.

The VPC BPA feature has the following modes:

  * **Bidirectional** : All traffic to and from internet gateways and egress-only internet gateways in this Region (except for excluded VPCs and subnets) is blocked.

  * **Ingress-only** : All internet traffic to the VPCs in this Region (except for VPCs or subnets which are excluded) is blocked. Only traffic to and from NAT gateways and egress-only internet gateways is allowed because these gateways only allow outbound connections to be established.

You can also create "exclusions" for this feature for traffic you don't want
to block. An exclusion is a mode that can be applied to a single VPC or subnet
that exempts it from the account's BPA mode and will allow bidirectional or
egress-only access.

Exclusions can have either of the following modes:

  * **Bidirectional** : All internet traffic to and from the excluded VPCs and subnets is allowed.

  * **Egress-only** : Outbound internet traffic from the excluded VPCs and subnets is allowed. Inbound internet traffic to the excluded VPCs and subnets is blocked. This only applies when BPA is set to Bidirectional.

###### Contents

  * [BPA basics](./security-vpc-bpa-basics.html)
  * [Assess impact of BPA and monitor BPA](./security-vpc-bpa-assess-impact-main.html)
  * [Advanced example](./security-vpc-bpa-example.html)

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Compliance validation

BPA basics

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

