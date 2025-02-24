# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/UsingTemporarySecurityCredentials_SDB.html'}

[](/pdfs/AmazonSimpleDB/latest/DeveloperGuide/sdb-
dg.pdf#UsingTemporarySecurityCredentials_SDB "Open PDF")

[Documentation](/index.html)[Amazon SimpleDB](/simpledb/index.html)[Developer
Guide](Welcome.html)

# Using Temporary Security Credentials

In addition to creating users with their own security credentials, IAM also
enables you to grant temporary security credentials to any user to allow the
user to access your AWS services and resources. You can manage users for your
system who do not have AWS accounts; these users are called federated users.
Additionally, "users" can also be applications that you create to access your
AWS resources.

You can use these temporary security credentials to make requests to Amazon
SimpleDB. Replace your usual `AWSAccessKeyId` parameter with the one provided
by IAM, add the IAM `SecurityToken` as a new parameter, and sign the request
with the `SecretKeyId` provided by IAM. If you send requests using expired
credentials Amazon SimpleDB denies the request.

For more information about IAM support for temporary security credentials, go
to [Granting Temporary Access to Your AWS
Resources](http://docs.aws.amazon.com/IAM/latest/UserGuide/TokenBasedAuth.html)
in _Using IAM_.

###### Example Using Temporary Security Credentials to Authenticate an Amazon
SimpleDB Request

The following example demonstrates the wire protocol for using temporary
security credentials to authenticate an Amazon SimpleDB request over HTTPS.

    
    
    https://sdb.amazonaws.com/
    ?Action=GetAttributes
    &AWSAccessKeyId=Access Key ID provided by AWS Security Token Service 
    &DomainName=MyDomain
    &ItemName=JumboFez
    &SignatureVersion=2
    &SignatureMethod=HmacSHA256
    &Timestamp=2010-01-25T15%3A03%3A07-07%3A00
    &Version=2009-04-15
    &Signature=Signature calculated using the SecretKeyId provided by AWS Security Token Service
    &SecurityToken=Security Token Value		

###### Note

provides support for temporary security credentials and session tokens in the
AWS SDKs so you can implement temporary security credentials or session tokens
with a specific programming language. Each SDK has its own instructions for
implementing this feature. For a current list of AWS SDKs that support this
feature, see [Ways to Access the AWS Security Token
Service](http://docs.aws.amazon.com/IAM/latest/UserGuide/AccessingSTS.html).
Non-AWS products and services should have their own documentation about
supporting temporary credentials and session tokens, if available.

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Managing Users of Amazon SimpleDB

HMAC-SHA Signature

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

