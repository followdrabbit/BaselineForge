# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-secrets-arns.html'}

[](/pdfs/AmazonRDS/latest/UserGuide/rds-ug.pdf#rds-proxy-secrets-arns "Open
PDF")

[Documentation](/index.html)[Amazon RDS](/rds/index.html)[User
Guide](Welcome.html)

# Setting up database credentials in AWS Secrets Manager for RDS Proxy

For each proxy that you create, you first use the Secrets Manager service to
store sets of user name and password credentials. You create a separate
Secrets Manager secret for each database user account that the proxy connects
to on the RDS DB instance.

In Secrets Manager console, you create these secrets with values for the
`username` and `password` fields. Doing so allows the proxy to connect to the
corresponding database users on a RDS DB instance that you associate with the
proxy. To do this, you can use the setting **Credentials for other database**
, **Credentials for RDS database** , or **Other type of secrets**. Fill in the
appropriate values for the **User name** and **Password** fields, and values
for any other required fields. The proxy ignores other fields such as **Host**
and **Port** if they're present in the secret. Those details are automatically
supplied by the proxy.

You can also choose **Other type of secrets**. In this case, you create the
secret with keys named `username` and `password`.

To connect through the proxy as a specific database user, make sure that the
password associated with a secret matches the database password for that user.
If there's a mismatch, you can update the associated secret in Secrets
Manager. In this case, you can still connect to other accounts where the
secret credentials and the database passwords do match.

###### Note

For RDS for SQL Server, RDS Proxy needs a secret in Secrets Manager that is
case sensitive to application code irrespective of the DB instance collation
settings. For example, if your application can use both usernames "Admin" or
"admin", then configure the proxy with secrets for both "Admin" and "admin".
RDS Proxy does not accommodate username case-insensitivity in the
authentication process between the client and proxy.

For more information about collation in SQL Server, see the [ Microsoft SQL
Server](https://docs.microsoft.com/en-us/sql/relational-
databases/collations/collation-and-unicode-support?view=sql-server-ver16)
documentation.

When you create a proxy through the AWS CLI or RDS API, you specify the Amazon
Resource Names (ARNs) of the corresponding secrets. You do so for all the DB
user accounts that the proxy can access. In the AWS Management Console, you
choose the secrets by their descriptive names.

For instructions about creating secrets in Secrets Manager, see the [Creating
a
secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-
basic-secret.html) page in the Secrets Manager documentation. Use one of the
following techniques:

  * Use [Secrets Manager](https://aws.amazon.com/secrets-manager/) in the console. 

  * To use the CLI to create a Secrets Manager secret for use with RDS Proxy, use a command such as the following. 
    
        aws secretsmanager create-secret
      --name "secret_name"
      --description "secret_description"
      --region region_name
      --secret-string '{"username":"db_user","password":"db_user_password"}'

  * You can also create a custom key to encrypt your Secrets Manager secret. The following command creates an example key.
    
        PREFIX=my_identifier
    aws kms create-key --description "$PREFIX-test-key" --policy '{
      "Id":"$PREFIX-kms-policy",
      "Version":"2012-10-17",
      "Statement":
        [
          {
            "Sid":"Enable IAM User Permissions",
            "Effect":"Allow",
            "Principal":{"AWS":"arn:aws:iam::account_id:root"},
            "Action":"kms:*","Resource":"*"
          },
          {
            "Sid":"Allow access for Key Administrators",
            "Effect":"Allow",
            "Principal":
              {
                "AWS":
                  ["$USER_ARN","arn:aws:iam:account_id::role/Admin"]
              },
            "Action":
              [
                "kms:Create*",
                "kms:Describe*",
                "kms:Enable*",
                "kms:List*",
                "kms:Put*",
                "kms:Update*",
                "kms:Revoke*",
                "kms:Disable*",
                "kms:Get*",
                "kms:Delete*",
                "kms:TagResource",
                "kms:UntagResource",
                "kms:ScheduleKeyDeletion",
                "kms:CancelKeyDeletion"
              ],
            "Resource":"*"
          },
          {
            "Sid":"Allow use of the key",
            "Effect":"Allow",
            "Principal":{"AWS":"$ROLE_ARN"},
            "Action":["kms:Decrypt","kms:DescribeKey"],
            "Resource":"*"
          }
        ]
    }'

For example, the following commands create Secrets Manager secrets for two
database users:

    
    
    aws secretsmanager create-secret \
      --name secret_name_1 --description "db admin user" \
      --secret-string '{"username":"admin","password":"choose_your_own_password"}'
    
    aws secretsmanager create-secret \
      --name secret_name_2 --description "application user" \
      --secret-string '{"username":"app-user","password":"choose_your_own_password"}'

To create these secrets encrypted with your custom AWS KMS key, use the
following commands:

    
    
    aws secretsmanager create-secret \
      --name secret_name_1 --description "db admin user" \
      --secret-string '{"username":"admin","password":"choose_your_own_password"}'
      --kms-key-id arn:aws:kms:us-east-2:account_id:key/key_id
    
    aws secretsmanager create-secret \
      --name secret_name_2 --description "application user" \
      --secret-string '{"username":"app-user","password":"choose_your_own_password"}'
      --kms-key-id arn:aws:kms:us-east-2:account_id:key/key_id

To see the secrets owned by your AWS account, use a command such as the
following.

    
    
    aws secretsmanager list-secrets

When you create a proxy using the CLI, you pass the Amazon Resource Names
(ARNs) of one or more secrets to the `--auth` parameter. The following Linux
example shows how to prepare a report with only the name and ARN of each
secret owned by your AWS account. This example uses the `--output table`
parameter that is available in AWS CLI version 2. If you are using AWS CLI
version 1, use `--output text` instead.

    
    
    aws secretsmanager list-secrets --query '*[].[Name,ARN]' --output table

To verify that you stored the correct credentials and in the right format in a
secret, use a command such as the following. Substitute the short name or the
ARN of the secret for ``your_secret_name``.

    
    
    aws secretsmanager get-secret-value --secret-id your_secret_name

The output should include a line displaying a JSON-encoded value like the
following.

    
    
    "SecretString": "{\"username\":\"your_username\",\"password\":\"your_password\"}",

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Set up a proxy network

Configuring IAM authentication

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

