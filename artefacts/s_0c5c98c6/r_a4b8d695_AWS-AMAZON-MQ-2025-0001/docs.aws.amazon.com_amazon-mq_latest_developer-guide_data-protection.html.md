# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/data-protection.html'}

[](/pdfs/amazon-mq/latest/developer-guide/amazon-mq-dg.pdf#data-protection
"Open PDF")

[Documentation](/index.html)[Amazon MQ](/amazon-mq/index.html)[Developer
Guide](welcome.html)

EncryptionEncryption at restEncryption in transit

# Data protection in Amazon MQ

The AWS [shared responsibility
model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies
to data protection in Amazon MQ. As described in this model, AWS is
responsible for protecting the global infrastructure that runs all of the AWS
Cloud. You are responsible for maintaining control over your content that is
hosted on this infrastructure. You are also responsible for the security
configuration and management tasks for the AWS services that you use. For more
information about data privacy, see the [Data Privacy
FAQ](https://aws.amazon.com/compliance/data-privacy-faq/). For information
about data protection in Europe, see the [AWS Shared Responsibility Model and
GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-
model-and-gdpr/) blog post on the _AWS Security Blog_.

For data protection purposes, we recommend that you protect AWS account
credentials and set up individual users with AWS IAM Identity Center or AWS
Identity and Access Management (IAM). That way, each user is given only the
permissions necessary to fulfill their job duties. We also recommend that you
secure your data in the following ways:

  * Use multi-factor authentication (MFA) with each account.

  * Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.

  * Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html) in the _AWS CloudTrail User Guide_.

  * Use AWS encryption solutions, along with all default security controls within AWS services.

  * Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.

  * If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive
information, such as your customers' email addresses, into tags or free-form
text fields such as a **Name** field. This includes when you work with Amazon
MQ or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any
data that you enter into tags or free-form text fields used for names may be
used for billing or diagnostic logs. If you provide a URL to an external
server, we strongly recommend that you do not include credentials information
in the URL to validate your request to that server.

For both Amazon MQ for ActiveMQ and Amazon MQ for RabbitMQ brokers, do not use
any personally identifiable information (PII) or other confidential or
sensitive information for broker names or usernames when creating resources
via the broker web console, or the Amazon MQ API. Broker names and usernames
are accessible to other AWS services, including CloudWatch Logs. Broker
usernames are not intended to be used for private or sensitive data.

## Encryption

User data stored in Amazon MQ is encrypted at rest. Amazon MQ encryption at
rest provides enhanced security by encrypting your data using encryption keys
stored in the AWS Key Management Service (KMS). This service helps reduce the
operational burden and complexity involved in protecting sensitive data. With
encryption at rest, you can build security-sensitive applications that meet
encryption compliance and regulatory requirements.

All connections between Amazon MQ brokers use Transport layer Security (TLS)
to provide encryption in transit.

Amazon MQ encrypts messages at rest and in transit using encryption keys that
it manages and stores securely. For more information, see the _[AWS Encryption
SDK Developer Guide](https://docs.aws.amazon.com/encryption-
sdk/latest/developer-guide/)_.

## Encryption at rest

Amazon MQ integrates with AWS Key Management Service (KMS) to offer
transparent server-side encryption. Amazon MQ always encrypts your data at
rest.

When you create an Amazon MQ for ActiveMQ broker or an Amazon MQ for RabbitMQ
broker, you can specify the AWS KMS key that you want Amazon MQ to use to
encrypt your data at rest. If you do not specify a KMS key, Amazon MQ creates
an AWS owned KMS key for you and uses it on your behalf. Amazon MQ currently
supports symmetric KMS keys. For more information about KMS keys, see [AWS KMS
keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys).

When creating a broker, you can configure what Amazon MQ uses for your
encryption key by selecting one of the following.

  * **Amazon MQ owned KMS key (default)** â The key is owned and managed by Amazon MQ and is not in your account.

  * **AWS managed KMS key** â The AWS managed KMS key (`aws/mq`) is a KMS key in your account that is created, managed, and used on your behalf by Amazon MQ.

  * **Select existing customer managed KMS key** â Customer managed KMS keys are created and managed by you in AWS Key Management Service (KMS).

###### Important

  * Revoking a grant cannot be undone. Instead, we suggest deleting the broker if you need to revoke access rights.

  * For **Amazon MQ for ActiveMQ** brokers that use Amazon Elastic File System (EFS) to store message data, if you revoke the grant that gives Amazon EFS permission to use the KMS keys in your account, it will not take place immediately. 

  * For **Amazon MQ for RabbitMQ** and **Amazon MQ for ActiveMQ** brokers that use EBS to store message data, if you disable, schedule for deletion, or revoke the grant that gives Amazon EBS permission to use the KMS keys in your account, Amazon MQ cannot maintain your broker, and it may change to a degraded state. 

  * If you have deactivated the key or scheduled the key to be deleted, you can reactivate the key or cancel key deletion and keep your broker maintained.

  * Deactivating a key or revoking a grant will not take place immediately.

When creating a [single instance broker](https://docs.aws.amazon.com/amazon-
mq/latest/developer-guide/rabbitmq-broker-architecture.html) with a KMS key
for RabbitMQ, you will see two `CreateGrant` events logged in AWS CloudTrail.
The first event is Amazon MQ creating a grant for the KMS key. The second
event is EBS creating a grant for EBS to use.

mq_grant

    
    
    
    {
        "eventVersion": "1.08",
        "userIdentity": {
            "type": "AssumedRole",
            "principalId": "AKIAIOSFODNN7EXAMPLE",
            "arn": "arn:aws:iam::111122223333:user/AmazonMqConsole",
            "accountId": "111122223333",
            "accessKeyId": "AKIAI44QH8DHBEXAMPLE",
            "sessionContext": {
                "sessionIssuer": {
                    "type": "Role",
                    "principalId": "AKIAIOSFODNN7EXAMPLE",
                    "arn": "arn:aws:iam::111122223333:user/AmazonMqConsole",
                    "accountId": "111122223333",
                    "userName": "AmazonMqConsole"
                },
                "webIdFederationData": {},
                "attributes": {
                    "creationDate": "2023-02-23T18:59:10Z",
                    "mfaAuthenticated": "false"
                }
            },
            "invokedBy": "mq.amazonaws.com"
        },
        "eventTime": "2018-06-28T22:23:46Z",
        "eventSource": "amazonmq.amazonaws.com",
        "eventName": "CreateGrant",
        "awsRegion": "us-west-2",
        "sourceIPAddress": "203.0.113.0",
        "userAgent": "PostmanRuntime/7.1.5",
        "requestParameters": {
            "granteePrincipal": "mq.amazonaws.com",
            "keyId": "arn:aws:kms:us-east-1:316438333700:key/bdbe42ae-f825-4e78-a8a1-828d411c4be2",
            "retiringPrincipal": "mq.amazonaws.com",
            "operations": [
                "CreateGrant",
                "Decrypt",
                "GenerateDataKeyWithoutPlaintext",
                "ReEncryptFrom",
                "ReEncryptTo",
                "DescribeKey"
            ]
        },
        "responseElements": {
            "grantId": "0ab0ac0d0b000f00ea00cc0a0e00fc00bce000c000f0000000c0bc0a0000aaafSAMPLE",
            "keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
            
        "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
        "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
        "readOnly": false,
        "resources": [
            {
               "accountId": "111122223333",
                "type": "AWS::KMS::Key",
                "ARN": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
            }
        ],
        "eventType": "AwsApiCall",
        "managementEvent": true,
        "recipientAccountId": "111122223333",
        "eventCategory": "Management",
        "sessionCredentialFromConsole": "true"
    }
                        

EBS grant creation

    

You will see one event for EBS grant creation.

    
    
                                        {
        "eventVersion": "1.08",
        "userIdentity": {
            "type": "AWSService",
            "invokedBy": "mq.amazonaws.com"
        },
        "eventTime": "2023-02-23T19:09:40Z",
        "eventSource": "kms.amazonaws.com",
        "eventName": "CreateGrant",
        "awsRegion": "us-east-1",
        "sourceIPAddress": "mq.amazonaws.com",
        "userAgent": "ExampleDesktop/1.0 (V1; OS)",
        "requestParameters": {
            "granteePrincipal": "mq.amazonaws.com",
            "keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
            "constraints": {
                "encryptionContextSubset": {
                    "aws:ebs:id": "vol-0b670f00f7d5417c0"
                }
            },
            "operations": [
                "Decrypt"
            ],
            "retiringPrincipal": "ec2.us-east-1.amazonaws.com"
        },
        "responseElements": {
            "grantId": "0ab0ac0d0b000f00ea00cc0a0e00fc00bce000c000f0000000c0bc0a0000aaafSAMPLE",
            "keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
        },
        "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
        "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
        "readOnly": false,
        "resources": [
            {
                "accountId": "111122223333",
                "type": "AWS::KMS::Key",
                "ARN": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
            }
        ],
        "eventType": "AwsApiCall",
        "managementEvent": true,
        "recipientAccountId": "111122223333",
        "sharedEventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
        "eventCategory": "Management"
    }
                                    

When creating a [cluster deployment](https://docs.aws.amazon.com/amazon-
mq/latest/developer-guide/rabbitmq-broker-architecture.html) with a KMS key
for RabbitMQ, you will see five `CreateGrant` events logged in AWS CloudTrail.
The first two events are grant creations for Amazon MQ. The next three events
are grants created by EBS for EBS to use.

mq_grant

    
    
    
    {
        "eventVersion": "1.08",
        "userIdentity": {
            "type": "AssumedRole",
            "principalId": "AKIAIOSFODNN7EXAMPLE",
            "arn": "arn:aws:iam::111122223333:user/AmazonMqConsole",
            "accountId": "111122223333",
            "accessKeyId": "AKIAI44QH8DHBEXAMPLE",
            "sessionContext": {
                "sessionIssuer": {
                    "type": "Role",
                    "principalId": "AKIAIOSFODNN7EXAMPLE",
                    "arn": "arn:aws:iam::111122223333:user/AmazonMqConsole",
                    "accountId": "111122223333",
                    "userName": "AmazonMqConsole"
                },
                "webIdFederationData": {},
                "attributes": {
                    "creationDate": "2023-02-23T18:59:10Z",
                    "mfaAuthenticated": "false"
                }
            },
            "invokedBy": "mq.amazonaws.com"
        },
        "eventTime": "2018-06-28T22:23:46Z",
        "eventSource": "amazonmq.amazonaws.com",
        "eventName": "CreateGrant",
        "awsRegion": "us-west-2",
        "sourceIPAddress": "203.0.113.0",
        "userAgent": "PostmanRuntime/7.1.5",
        "requestParameters": {
            "granteePrincipal": "mq.amazonaws.com",
            "keyId": "arn:aws:kms:us-east-1:316438333700:key/bdbe42ae-f825-4e78-a8a1-828d411c4be2",
            "retiringPrincipal": "mq.amazonaws.com",
            "operations": [
                "CreateGrant",
                "Encrypt",
                "Decrypt",
                "ReEncryptFrom",
                "ReEncryptTo",
                "GenerateDataKey",
                "GenerateDataKeyWithoutPlaintext",
                "DescribeKey"
            ]
        },
        "responseElements": {
            "grantId": "0ab0ac0d0b000f00ea00cc0a0e00fc00bce000c000f0000000c0bc0a0000aaafSAMPLE",
            "keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
            
        "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
        "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
        "readOnly": false,
        "resources": [
            {
               "accountId": "111122223333",
                "type": "AWS::KMS::Key",
                "ARN": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
            }
        ],
        "eventType": "AwsApiCall",
        "managementEvent": true,
        "recipientAccountId": "111122223333",
        "eventCategory": "Management",
        "sessionCredentialFromConsole": "true"
    }
                        

mq_rabbit_grant

    
    
    
    {
        "eventVersion": "1.08",
        "userIdentity": {
            "type": "AssumedRole",
            "principalId": "AKIAIOSFODNN7EXAMPLE",
            "arn": "arn:aws:iam::111122223333:user/AmazonMqConsole",
            "accountId": "111122223333",
            "accessKeyId": "AKIAI44QH8DHBEXAMPLE",
            "sessionContext": {
                "sessionIssuer": {
                    "type": "Role",
                    "principalId": "AKIAIOSFODNN7EXAMPLE",
                    "arn": "arn:aws:iam::111122223333:user/AmazonMqConsole",
                    "accountId": "111122223333",
                    "userName": "AmazonMqConsole"
                },
                "webIdFederationData": {},
                "attributes": {
                    "creationDate": "2023-02-23T18:59:10Z",
                    "mfaAuthenticated": "false"
                }
            },
            "invokedBy": "mq.amazonaws.com"
        },
        "eventTime": "2018-06-28T22:23:46Z",
        "eventSource": "amazonmq.amazonaws.com",
        "eventName": "CreateGrant",
        "awsRegion": "us-west-2",
        "sourceIPAddress": "203.0.113.0",
        "userAgent": "PostmanRuntime/7.1.5",
        "requestParameters": {
            "granteePrincipal": "mq.amazonaws.com",
            "retiringPrincipal": "mq.amazonaws.com",
            "operations": [
                "DescribeKey"
            ],
            "keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
        },
        "responseElements": {
            "grantId": "0ab0ac0d0b000f00ea00cc0a0e00fc00bce000c000f0000000c0bc0a0000aaafSAMPLE",
            "keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
            
        "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
        "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
        "readOnly": false,
        "resources": [
            {
               "accountId": "111122223333",
                "type": "AWS::KMS::Key",
                "ARN": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
            }
        ],
        "eventType": "AwsApiCall",
        "managementEvent": true,
        "recipientAccountId": "111122223333",
        "eventCategory": "Management",
        "sessionCredentialFromConsole": "true"
    }
                        

EBS grant creation

    

You will see three events for EBS grant creation.

    
    
                                          {
        "eventVersion": "1.08",
        "userIdentity": {
            "type": "AWSService",
            "invokedBy": "mq.amazonaws.com"
        },
        "eventTime": "2023-02-23T19:09:40Z",
        "eventSource": "kms.amazonaws.com",
        "eventName": "CreateGrant",
        "awsRegion": "us-east-1",
        "sourceIPAddress": "mq.amazonaws.com",
        "userAgent": "ExampleDesktop/1.0 (V1; OS)",
        "requestParameters": {
            "granteePrincipal": "mq.amazonaws.com",
            "keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
            "constraints": {
                "encryptionContextSubset": {
                    "aws:ebs:id": "vol-0b670f00f7d5417c0"
                }
            },
            "operations": [
                "Decrypt"
            ],
            "retiringPrincipal": "ec2.us-east-1.amazonaws.com"
        },
        "responseElements": {
            "grantId": "0ab0ac0d0b000f00ea00cc0a0e00fc00bce000c000f0000000c0bc0a0000aaafSAMPLE",
            "keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE",
        },
        "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
        "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
        "readOnly": false,
        "resources": [
            {
                "accountId": "111122223333",
                "type": "AWS::KMS::Key",
                "ARN": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
            }
        ],
        "eventType": "AwsApiCall",
        "managementEvent": true,
        "recipientAccountId": "111122223333",
        "sharedEventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
        "eventCategory": "Management"
    }
                                    

For more information about KMS keys, see [AWS KMS
keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys)
in the _AWS Key Management Service Developer Guide_.

## Encryption in transit

**Amazon MQ for ActiveMQ** : Amazon MQ for ActiveMQ requires strong Transport
Layer Security (TLS) and encrypts data in transit between the brokers of your
Amazon MQ deployment. All data that passes between Amazon MQ brokers is
encrypted using strong Transport Layer Security (TLS). This is true for all
available protocols.

**Amazon MQ for RabbitMQ** : Amazon MQ for RabbitMQ requires strong Transport
Layer Security (TLS) encryption for all client connections. RabbitMQ cluster
replication traffic only transits your brokerâs VPC and all network traffic
between AWS data centers is transparently encrypted at the physical layer.
Amazon MQ for RabbitMQ clustered brokers currently do not support [Inter-node
encryption](https://www.rabbitmq.com/clustering-ssl.html) for cluster
replication. To learn more about data-in-transit, see [Encrypting Data-at-Rest
and -in-Transit](https://docs.aws.amazon.com/whitepapers/latest/logical-
separation/encrypting-data-at-rest-and--in-transit.html).

### Amazon MQ for ActiveMQ protocols

You can access your ActiveMQ brokers using the following protocols with TLS
enabled:

  * [AMQP](http://activemq.apache.org/amqp.html)

  * [MQTT](http://activemq.apache.org/mqtt.html)

  * MQTT over [WebSocket](http://activemq.apache.org/websockets.html)

  * [OpenWire](http://activemq.apache.org/openwire.html)

  * [STOMP](http://activemq.apache.org/stomp.html)

  * STOMP over WebSocket

ActiveMQ on Amazon MQ supports the following cipher suites:

  * TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384

  * TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384

  * TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA

  * TLS_DHE_RSA_WITH_AES_256_GCM_SHA384

  * TLS_DHE_RSA_WITH_AES_256_CBC_SHA256

  * TLS_DHE_RSA_WITH_AES_256_CBC_SHA

  * TLS_RSA_WITH_AES_256_GCM_SHA384

  * TLS_RSA_WITH_AES_256_CBC_SHA256

  * TLS_RSA_WITH_AES_256_CBC_SHA

  * TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256

  * TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256

  * TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA

  * TLS_DHE_RSA_WITH_AES_128_GCM_SHA256

  * TLS_DHE_RSA_WITH_AES_128_CBC_SHA256

  * TLS_DHE_RSA_WITH_AES_128_CBC_SHA

  * TLS_RSA_WITH_AES_128_GCM_SHA256

  * TLS_RSA_WITH_AES_128_CBC_SHA256

  * TLS_RSA_WITH_AES_128_CBC_SHA

### Amazon MQ for RabbitMQ protocols

You can access your RabbitMQ brokers using the following protocols with TLS
enabled:

  * [AMQP (0-9-1)](https://www.rabbitmq.com/specification.html)

RabbitMQ on Amazon MQ supports the following cipher suites:

  * TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384

  * TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Security

Identity and access management

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

