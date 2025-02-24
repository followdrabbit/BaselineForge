# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-iam-setup.html'}

[](/pdfs/AmazonRDS/latest/UserGuide/rds-ug.pdf#rds-proxy-iam-setup "Open PDF")

[Documentation](/index.html)[Amazon RDS](/rds/index.html)[User
Guide](Welcome.html)

PrerequisitesCreating an IAM policy for Secrets Manager access

# Configuring IAM authentication for RDS Proxy

To set up AWS Identity and Access Management (IAM) authentication for RDS
Proxy in Amazon RDS, create and configure an IAM policy that grants the
necessary permissions. RDS Proxy uses AWS Secrets Manager to manage database
credentials securely, which allows applications to authenticate through the
proxy without directly handling credentials.

This topic provides the steps to configure IAM authentication for RDS Proxy,
including creating the required IAM policy and attaching it to an IAM role.

###### Tip

This procedure is only necessary if you want to create your own IAM role.
Otherwise, RDS can automatically create the required role when you set up the
proxy, so you can skip these steps.

## Prerequisites

Before you set up IAM authentication for RDS Proxy, make sure that you have
the following:

  * **AWS Secrets Manager** â At least one stored secret that contains database credentials. For instructions to create secrets, see [Setting up database credentials in AWS Secrets Manager for RDS Proxy](./rds-proxy-secrets-arns.html).

  * **IAM permissions** â An IAM role or user with permissions to create and manage IAM policies, roles, and secrets in AWS Secrets Manager.

## Creating an IAM policy for Secrets Manager access

To allow RDS Proxy to retrieve database credentials from Secrets Manager,
create an IAM role with a policy that grants the necessary permissions.

###### To create a role to access your secrets for use with your proxy

  1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

  2. Create a permissions policy for the role. For general steps, see [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html).

Paste this policy into the JSON editor and make the following changes:

     * Substitute your own account ID.

     * Substitute `us-east-2` with the Region where the proxy will reside.

     * Substitute the secret names with the ones you created. For more information, see [ Specifying KMS keys in IAM policy statements](https://docs.aws.amazon.com/kms/latest/developerguide/cmks-in-iam-policies.html).

     * Substitue the KMS key ID with the one you used to encrypt the Secrets Manager secrets, either the default key or your own key.
    
        {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "secretsmanager:GetSecretValue",
                "Resource": [
                    "arn:aws:secretsmanager:us-east-2:account_id:secret:secret_name_1",
                    "arn:aws:secretsmanager:us-east-2:account_id:secret:secret_name_2"
                ]
            },
            {
                "Effect": "Allow",
                "Action": "kms:Decrypt",
                "Resource": "arn:aws:kms:us-east-2:account_id:key/key_id",
                "Condition": {
                    "StringEquals": {
                        "kms:ViaService": "secretsmanager.us-east-2.amazonaws.com"
                    }
                }
            }
        ]
    }

  3. Create the role and attach the permissions policy to it. For general steps, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html). 

For the **Trusted entity type** , choose **AWS service**. Under **Use case** ,
select **RDS** and choose **RDS - Add Role to Database** for the use case.

  4. For **Permissions policies** , choose the policy that you created.

  5. For **Select trusted entities** , enter the following trust policy for the role:
    
        {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "",
          "Effect": "Allow",
          "Principal": {
            "Service": "rds.amazonaws.com"
          },
          "Action": "sts:AssumeRole"
        }
      ]
    }

To create the role using the AWS CLI, send the following request:

    
    
    aws iam create-role \
      --role-name my_role_name \
      --assume-role-policy-document '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":["rds.amazonaws.com"]},"Action":"sts:AssumeRole"}]}'

Then, attach the policy to the role:

    
    
    aws iam put-role-policy \
      --role-name my_role_name \
      --policy-name secret_reader_policy \
      --policy-document '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": "secretsmanager:GetSecretValue",
                "Resource": [
                    "arn:aws:secretsmanager:us-east-2:account_id:secret:secret_name_1",
                    "arn:aws:secretsmanager:us-east-2:account_id:secret:secret_name_2"
                ]
            },
            {
                "Sid": "VisualEditor1",
                "Effect": "Allow",
                "Action": "kms:Decrypt",
                "Resource": "arn:aws:kms:us-east-2:account_id:key/key_id",
                "Condition": {
                    "StringEquals": {
                        "kms:ViaService": "secretsmanager.us-east-2.amazonaws.com"
                    }
                }
            }
        ]
    }'

With the IAM role and permissions configured, you can now create a proxy and
associate it with this role. This allows the proxy to retrieve database
credentials securely from AWS Secrets Manager and enable IAM authentication
for your applications. For instructions, see [Creating an RDS proxy](./rds-
proxy-creating.html).

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Setting up database credentials in Secrets Manager

Creating an RDS proxy

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

