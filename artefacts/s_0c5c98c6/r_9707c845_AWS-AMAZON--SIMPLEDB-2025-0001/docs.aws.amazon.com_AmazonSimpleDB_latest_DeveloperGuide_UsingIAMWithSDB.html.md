# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/UsingIAMWithSDB.html'}

[](/pdfs/AmazonSimpleDB/latest/DeveloperGuide/sdb-dg.pdf#UsingIAMWithSDB "Open
PDF")

[Documentation](/index.html)[Amazon SimpleDB](/simpledb/index.html)[Developer
Guide](Welcome.html)

Amazon Resource Names (ARNs) for Amazon SimpleDBAmazon SimpleDB ActionsAmazon
SimpleDB KeysExample Policies for Amazon SimpleDB

# Managing Users of Amazon SimpleDB

###### Topics

  * Amazon Resource Names (ARNs) for Amazon SimpleDB
  * Amazon SimpleDB Actions
  * Amazon SimpleDB Keys
  * Example Policies for Amazon SimpleDB

Amazon SimpleDB does not offer its own resource-based permissions system.
However, the service now integrates with IAM (AWS Identity and Access
Management) so that you can give other Users in your AWS Account access to
Amazon SimpleDB domains within the AWS Account. For example, Joe can create an
Amazon SimpleDB domain, and then write an IAM policy specifying which Users in
his AWS Account can access that domain. Joe can't give another AWS Account (or
Users in another AWS Account) access to his AWS Account's SimpleDB domains.

###### Important

Aside from the integration with IAM, Amazon SimpleDB hasn't changed. Its API
is not affected by the introduction of IAM, and includes no new actions
related to Users and access control.

For examples of policies that cover Amazon SimpleDB actions and resources, see
Example Policies for Amazon SimpleDB.

## Amazon Resource Names (ARNs) for Amazon SimpleDB

For Amazon SimpleDB, domains are the only resource type you can specify in a
policy. The ARN format for domains follows this format:

    
    
    arn:aws:sdb:<region>:<account_ID>:domain/<domain_name>

The _< region>_ is required and can be any of the individual Regions Amazon
SimpleDB supports (e.g., us-east-1), or * to represent all Regions. The _<
region>_ must not be blank.

###### Example

Following is an ARN for a domain named Domain1 in the us-east-1 region,
belonging to AWS Account 111122223333.

    
    
    arn:aws:sdb:us-east-1:111122223333:domain/Domain1

###### Example

Following is an ARN for a domain named Domain1 in all Regions that Amazon
SimpleDB supports.

    
    
    arn:aws:sdb:*:111122223333:domain/Domain1

You can use * and ? wildcards in the domain name. The * represents zero or
multiple characters, and ? represents one character. For example, the
following could refer to all the domains prefixed with `don_`.

    
    
    arn:aws:sdb:*:111122223333:domain/don_*

For more information about ARNs, see
[ARNs](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html#Identifiers_ARNs).

## Amazon SimpleDB Actions

In an IAM policy, you can specify any and all actions that Amazon SimpleDB
offers. You must prefix each action name with the lowercase string `sdb:`. For
example: `sdb:GetAttributes`, `sdb:Select`, `sdb:*` (for all Amazon SimpleDB
actions). For a list of the actions, see
[Operations](./SDB_API_Operations.html).

## Amazon SimpleDB Keys

Amazon SimpleDB implements the following policy keys, but no product-specific
ones. For more information about policy keys, see
[Condition](http://docs.aws.amazon.com/IAM/latest/UserGuide/AccessPolicyLanguage_ElementDescriptions.html#Condition).

For a list of condition keys supported by each AWS service, see [Actions,
resources, and condition keys for AWS
services](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_actions-
resources-contextkeys.html) in the _IAM User Guide_. For a list of condition
keys that can be used in multiple AWS services, see [ global condition context
keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-
keys.html) in the _IAM User Guide_.

## Example Policies for Amazon SimpleDB

This section shows several simple policies for controlling User access to
Amazon SimpleDB domains.

###### Note

In the future, Amazon SimpleDB might add new actions that should logically be
included in one of the following policies, based on the policyâs stated
goals.

###### Example 1: Allow a group to use any Amazon SimpleDB actions on specific
domains

In this example, we create a policy that lets the group use any of the AWS
Account's domains that start with the literal string `test`.

    
    
    {
       "Version": "2012-10-17",
       "Statement":[{
          "Effect":"Allow",
          "Action":"sdb:*",
          "Resource":"arn:aws:sdb:*:111122223333:domain/test*"
          }
       ]
    }

###### Example 2: Allow a group to read data from the AWS Account's domains

In this example, we create a policy that lets the group use the
`GetAttributes` and `Select` actions with any of the AWS Account's domains.

    
    
    {
       "Version": "2012-10-17",
       "Statement":[{
          "Effect":"Allow",
          "Action":["sdb:GetAttributes","sdb:Select"],
          "Resource":"*"
          }
       ]
    }

###### Example 3: Allow a group to list domains and get their metadata

In this example, we create a policy that lets the group use the `ListDomains`
and `DomainMetadata` actions with any of the AWS Account's domains.

    
    
    {
       "Version": "2012-10-17",
       "Statement":[{
          "Effect":"Allow",
          "Action":["sdb:ListDomains",â"sdb:DomainMetadata"],
          "Resource":"*"
          }
       ]
    }

###### Example 4: Allow a partner to only read data from a particular domain

There's no way to share a domain with a different AWS Account, so the partner
must work with your domain as a User within your own AWS Account.

In this example, we create a user for the partner, and create a policy for the
user that gives access to the `GetAttributes` and `Select` actions only on the
domain named _mySDBDomain_.

(Instead of attaching the policy to the User, you could create a group for the
partner, put the User in the group, and assign the policy to the group.)

You might also want to prevent the partner from doing anything else with
mySDBDomain, so we add a statement that denies permission to any Amazon
SimpleDB actions besides `GetAttributes` and `Select`. This is only necessary
if there's also a broad policy that gives the AWS Account's Users wide access
to Amazon SimpleDB and all the AWS Account's domains.

    
    
    {
       "Version": "2012-10-17",
       "Statement":[{
             "Effect":"Allow",
             "Action":["sdb:GetAttributes","sdb:Select"],
             "Resource":"arn:aws:sdb:*:111122223333:domain/mySDBDomain"
          },
          {
             "Effect":"Deny",
             "Action":["sdb:GetAttributes","sdb:Select"],
             "Resource":"*"
          }
       ]
    }

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Creating an AWS Account

Using Temporary Security Credentials

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

