# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-iam.html'}

[](/pdfs/kinesisvideostreams/latest/dg/kinesisvideo-dg.pdf#how-iam "Open PDF")

[Documentation](/index.html)[Amazon Kinesis Video
Streams](/kinesis/index.html)[Developer Guide](what-is-kinesis-video.html)

Policy syntaxActions for Kinesis Video StreamsAmazon Resource Names (ARNs) for
Kinesis Video StreamsGranting other IAM accounts access to a Kinesis video
streamExample Policies

# Controlling access to Kinesis Video Streams resources using IAM

You can use AWS Identity and Access Management (IAM) with Amazon Kinesis Video
Streams, to control whether users in your organization can perform a task
using specific Kinesis Video Streams API operations and whether they can use
specific AWS resources.

For more information about IAM, see the following:

  * [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/)

  * [Getting started](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started.html)

  * [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/)

###### Contents

  * Policy syntax
  * Actions for Kinesis Video Streams
  * Amazon Resource Names (ARNs) for Kinesis Video Streams
  * Granting other IAM accounts access to a Kinesis video stream
  * Example policies for Kinesis Video Streams

## Policy syntax

An IAM policy is a JSON document that consists of one or more statements. Each
statement is structured as follows:

    
    
    {
      "Statement":[{
        "Effect":"effect",
        "Action":"action",
        "Resource":"arn",
        "Condition":{
          "condition":{
            "key":"value"
            }
          }
        }
      ]
    }

There are various elements that make up a statement:

  * **Effect** â The _effect_ can be `Allow` or `Deny`. By default, users don't have permission to use resources and API actions, so all requests are denied. An explicit allow overrides the default. An explicit deny overrides any allows.

  * **Action** â The _action_ is the specific API action for which you are granting or denying permission.

  * **Resource** â The resource that's affected by the action. To specify a resource in the statement, you must use its Amazon Resource Name (ARN).

  * **Condition** â Conditions are optional. They can be used to control when your policy is in effect.

As you create and manage IAM policies, we recommend that you use the [IAM
Policy
Generator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-
generator) and the [IAM Policy
Simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-
policies.html).

## Actions for Kinesis Video Streams

In an IAM policy statement, you can specify any API action from any service
that supports IAM. For Kinesis Video Streams, use the following prefix with
the name of the API action: `kinesisvideo:`. For example:
`kinesisvideo:CreateStream`, `kinesisvideo:ListStreams`, and
`kinesisvideo:DescribeStream`.

To specify multiple actions in a single statement, separate them with commas
as follows:

    
    
    "Action": ["kinesisvideo:_action1_ ", "kinesisvideo:_action2_ "]

You can also specify multiple actions using wildcards. For example, you can
specify all actions whose name begins with the word "Get" as follows:

    
    
    "Action": "kinesisvideo:Get*"

To specify all Kinesis Video Streams operations, use the asterisk (*) wildcard
as follows:

    
    
    "Action": "kinesisvideo:*"

For the complete list of Kinesis Video Streams API actions, see the [_Kinesis
Video Streams API
reference_](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_Reference.html).

## Amazon Resource Names (ARNs) for Kinesis Video Streams

Each IAM policy statement applies to the resources that you specify using
their ARNs.

Use the following ARN resource format for Kinesis Video Streams:

    
    
    arn:aws:kinesisvideo:region:account-id:stream/stream-name/code

For example:

    
    
    "Resource": arn:aws:kinesisvideo:*:111122223333:stream/my-stream/0123456789012

You can get the ARN of a stream using
[DescribeStream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeStream.html).

## Granting other IAM accounts access to a Kinesis video stream

You might need to grant permission to other IAM accounts to perform operations
on streams in Kinesis Video Streams. The following overview describes the
general steps to grant access to video streams across accounts:

  1. Get the 12-digit account ID of the account that you want to grant permissions to perform operations on the stream resource created in your account. 

**Example:** In the following steps, we'll use 111111111111 as the account ID
for the account that you want to grant permission to, and 999999999999 as the
ID for your Kinesis Video Streams

  2. Create an IAM managed policy in the account that owns the stream (999999999999) that allows the level of access that you want to grant. 

**Sample policy:**

    
        {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "kinesisvideo:GetDataEndpoint",
                    "kinesisvideo:DescribeStream",
                    "kinesisvideo:PutMedia"
                ],
                "Resource": "arn:aws:kinesisvideo:us-west-2:999999999999:stream/custom-stream-name/1613732218179"
            }
        ]
    }

For other example policies for Kinesis Video Streams resources, see Example
Policies in the next section.

  3. Create a role in the account that owns the stream (999999999999), and specify the account that you want to grant permissions for (111111111111). This will add a trusted entity to the role. 

**Sample trusted policy:**

    
        {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "AWS": "arn:aws:iam::111111111111:root"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }

Attach the policy that you created in the previous step to this role.

You've now created a role in account 999999999999 which has the permission to
operations like `DescribeStream`, `GetDataEndpoint`, and `PutMedia` on a
stream resource ARN in the managed policy. This new role also trusts the other
account, 111111111111, to assume this role.

###### Important

Make note of the role ARN, you'll need it in the next step.

  4. Create a managed policy in the other account, 111111111111, that allows the `AssumeRole` action on the role that you created in account 999999999999 in the previous step. You'll need to mention the role ARN from the previous step. 

**Sample policy:**

    
        {
        "Version": "2012-10-17",
        "Statement": {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Resource": "arn:aws:iam::999999999999:role/CustomRoleName"
        }
    }

  5. Attach the policy created in the previous step to an IAM entity, like a role or a user in account 111111111111. This user now has the permission to assume role `CustomRoleName` in account 999999999999. 

This user's crendentials call AWS STS `AssumeRole` API to get the session
credentials, which are subsequently used to call Kinesis Video Streams APIs on
the stream created in account 999999999999.

    
        aws sts assume-role --role-arn "arn:aws:iam::999999999999:role/CustomRoleName" --role-session-name "kvs-cross-account-assume-role"
    {
        "Credentials": {
            "AccessKeyId": "",
            "SecretAccessKey": "",
            "SessionToken": "",
            "Expiration": ""
        },
        "AssumedRoleUser": {
            "AssumedRoleId": "",
            "Arn": ""
        }
    }

  6. Set the access key, secret key, and session credentials based on the previous set in the environment.
    
        set AWS_ACCESS_KEY_ID=
    set AWS_SECRET_ACCESS_KEY=
    set AWS_SESSION_TOKEN=

  7. Run Kinesis Video Streams APIs to describe and get the data endpoint for the stream in account 999999999999.
    
        aws kinesisvideo describe-stream --stream-arn "arn:aws:kinesisvideo:us-west-2:999999999999:stream/custom-stream-name/1613732218179"
    {
        "StreamInfo": {
            "StreamName": "custom-stream-name",
            "StreamARN": "arn:aws:kinesisvideo:us-west-2:999999999999:stream/custom-stream-name/1613732218179",
            "KmsKeyId": "arn:aws:kms:us-west-2:999999999999:alias/aws/kinesisvideo",
            "Version": "abcd",
            "Status": "ACTIVE",
            "CreationTime": "2018-02-19T10:56:58.179000+00:00",
            "DataRetentionInHours": 24
        }
    }
    
    aws kinesisvideo get-data-endpoint --stream-arn "arn:aws:kinesisvideo:us-west-2:999999999999:stream/custom-stream-name/1613732218179" --api-name "PUT_MEDIA"
    {
        "DataEndpoint": "https://s-b12345.kinesisvideo.us-west-2.amazonaws.com"
    }

For generic step-by-step instructions on granting cross-account access, see
[Delegate Access Across AWS accounts Using IAM
Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-
account-with-roles.html).

## Example policies for Kinesis Video Streams

The following example policies demonstrate how you can control user access to
your Kinesis Video Streams

###### Example 1: Allow users to get data from any Kinesis video stream

This policy allows a user or group to perform the `DescribeStream`,
`GetDataEndpoint`, `GetMedia`, `ListStreams`, and `ListTagsForStream`
operations on any Kinesis video stream. This policy is appropriate for users
who can get data from any video stream.

    
    
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "kinesisvideo:Describe*",
                    "kinesisvideo:Get*",
                    "kinesisvideo:List*"
                ],
                "Resource": "*"
            }
        ]
    }
    

###### Example 2: Allow a user to create a Kinesis video stream and write data
to it

This policy allows a user or group to perform the `CreateStream` and
`PutMedia` operations. This policy is appropriate for a security camera that
can create a video stream and send data to it.

    
    
    {
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "kinesisvideo:CreateStream",
                    "kinesisvideo:PutMedia"            
                ],
                "Resource": "*"
            }
        ]
    }
    

###### Example 3: Allow a user full access to all Kinesis Video Streams
resources

This policy allows a user or group to perform any Kinesis Video Streams
operation on any resource. This policy is appropriate for administrators.

    
    
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "kinesisvideo:*",
                "Resource": "*"
            }
        ]
    }
    

###### Example 4: Allow a user to write data to a specific Kinesis video
stream

This policy allows a user or group to write data to a specific video stream.
This policy is appropriate for a device that can send data to a single stream.

    
    
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "kinesisvideo:PutMedia",
                "Resource": "arn:aws:kinesisvideo:us-west-2:123456789012:stream/your_stream/0123456789012"
            }
        ]
    }
    

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Data Protection

Controlling access to Kinesis Video Streams resources using AWS IoT

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

