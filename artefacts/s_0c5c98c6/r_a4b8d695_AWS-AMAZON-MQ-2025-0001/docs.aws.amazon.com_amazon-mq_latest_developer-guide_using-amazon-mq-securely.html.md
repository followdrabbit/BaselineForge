# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/using-amazon-mq-securely.html'}

[](/pdfs/amazon-mq/latest/developer-guide/amazon-mq-dg.pdf#using-amazon-mq-
securely "Open PDF")

[Documentation](/index.html)[Amazon MQ](/amazon-mq/index.html)[Developer
Guide](welcome.html)

Prefer brokers without public accessibilityAlways configure an authorization
mapBlock Unnecessary Protocols

# Security best practices for Amazon MQ

The following design patterns can improve the security of your Amazon MQ
broker.

###### Topics

  * Prefer brokers without public accessibility
  * Always configure an authorization map
  * Block unnecessary protocols with VPC security groups

For more information about how Amazon MQ encrypts your data, as well as a list
of supported protocols, see [Data Protection](./data-protection.html).

## Prefer brokers without public accessibility

Brokers created without public accessibility can't be accessed from outside of
your
[VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Introduction.html).
This greatly reduces your broker's susceptibility to Distributed Denial of
Service (DDoS) attacks from the public internet. For more information, see
[Accessing the Amazon MQ broker web console without public
accessibility](./accessing-web-console-of-broker-without-public-
accessibility.html) in this guide and [How to Help Prepare for DDoS Attacks by
Reducing Your Attack Surface](https://aws.amazon.com/blogs/security/how-to-
help-prepare-for-ddos-attacks-by-reducing-your-attack-surface/) on the AWS
Security Blog.

## Always configure an authorization map

Because ActiveMQ has no authorization map configured by default, any
authenticated user can perform any action on the broker. Thus, it is a best
practice to restrict permissions _by group_. For more information, see
`[authorizationEntry](./child-element-details.html#authorizationEntry)`.

###### Important

If you specify an authorization map which doesn't include the `activemq-
webconsole` group, you can't use the ActiveMQ Web Console because the group
isn't authorized to send messages to, or receive messages from, the Amazon MQ
broker.

## Block unnecessary protocols with VPC security groups

To improve security, you should restrict the connections of unnecessary
protocols and ports by properly configuring your Amazon VPC Security Group.
For instance, to restrict access to most protocols while allowing access to
OpenWire and the web console, you could allow access to only 61617 and 8162.
This limits your exposure by blocking protocols you are not using, while
allowing OpenWire and the web console to function normally.

Allow only the protocol ports that you are using.

  * AMQP: 5671

  * MQTT: 8883

  * OpenWire: 61617

  * STOMP: 61614

  * WebSocket: 61619

For more information see:

  * [ Configure additional Amazon MQ broker settings](./configure-advanced-broker-settings-console.html)

  * [Security Groups for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

  * [Default Security Group for Your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#DefaultSecurityGroup)

  * [Working with Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#WorkingWithSecurityGroups)

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Infrastructure security

Logging and monitoring

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

