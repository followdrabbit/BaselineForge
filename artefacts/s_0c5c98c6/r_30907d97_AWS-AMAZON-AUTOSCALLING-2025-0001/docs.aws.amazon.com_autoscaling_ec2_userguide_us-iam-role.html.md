# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html'}

[](/pdfs/autoscaling/ec2/userguide/as-dg.pdf#us-iam-role "Open PDF")

[Documentation](/index.html)[Auto Scaling](/autoscaling/index.html)[User
Guide](what-is-amazon-ec2-auto-scaling.html)

PrerequisitesCreate a launch templateSee also

# IAM role for applications that run on Amazon EC2 instances

Applications that run on Amazon EC2 instances need credentials to access other
AWS services. To provide these credentials in a secure way, use an IAM role.
The role supplies temporary permissions that the application can use when it
accesses other AWS resources. The role's permissions determine what the
application is allowed to do.

For instances in an Auto Scaling group, you must create a launch template or
launch configuration and choose an instance profile to associate with the
instances. An instance profile is a container for an IAM role that allows
Amazon EC2 to pass the IAM role to an instance when the instance is launched.
First, create an IAM role that has all of the permissions required to access
the AWS resources. Then, create the instance profile and assign the role to
it.

###### Note

As a best practice, we strongly recommend that you create the role so that it
has the minimum permissions to other AWS services that your application
requires.

###### Contents

  * [Prerequisites](./us-iam-role.html#us-iam-role-prereq)
  * [Create a launch template](./us-iam-role.html#us-iam-role-create-lt)
  * [See also](./us-iam-role.html#iam-role-see-also)

## Prerequisites

Create the IAM role that your application running on Amazon EC2 can assume.
Choose the appropriate permissions so that the application that is
subsequently given the role can make the specific API calls that it needs.

If you use the IAM console instead of the AWS CLI or one of the AWS SDKs, the
console creates an instance profile automatically and gives it the same name
as the role to which it corresponds.

###### To create an IAM role (console)

  1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

  2. In the navigation pane on the left, choose **Roles**.

  3. Choose **Create role**.

  4. For **Select trusted entity** , choose **AWS service**. 

  5. For your use case, choose **EC2** and then choose **Next**. 

  6. If possible, select the policy to use for the permissions policy or choose **Create policy** to open a new browser tab and create a new policy from scratch. For more information, see [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html#access_policies_create-start) in the _IAM User Guide_. After you create the policy, close that tab and return to your original tab. Select the check box next to the permissions policies that you want the service to have.

  7. (Optional) Set a permissions boundary. This is an advanced feature that is available for service roles. For more information, see [Permissions boundaries for IAM entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in the _IAM User Guide_.

  8. Choose **Next**.

  9. On the **Name, review, and create** page, for **Role name** , enter a role name to help you identify the purpose of this role. This name must be unique within your AWS account. Because other AWS resources might reference the role, you can't edit the name of the role after it has been created. 

  10. Review the role, and then choose **Create role**. 

###### IAM permissions

Use an IAM identity-based policy to control access to your new IAM role. The
`iam:PassRole` permission is needed on the IAM identity (user or role) that
creates or updates an Auto Scaling group using a launch template that
specifies an instance profile.

The following example policy grants permissions to pass only IAM roles whose
name begins with ``qateam-``.

    
    
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "iam:PassRole",
                "Resource": "arn:aws:iam::account-id:role/qateam-*",
                "Condition": {
                    "StringEquals": {
                        "iam:PassedToService": [
                            "ec2.amazonaws.com",
                            "ec2.amazonaws.com.cn"
                        ]
                    }
                }
            }
        ]
    }
    

###### Important

For information about how Amazon EC2 Auto Scaling validates permissions for
the `iam:PassRole` action for an Auto Scaling group that uses a launch
template, see [Permissions validation for ec2:RunInstances and
iam:PassRole](./ec2-auto-scaling-launch-template-
permissions.html#runinstances-permissions-validation).

## Create a launch template

When you create the launch template using the AWS Management Console, in the
**Advanced details** section, select the role from **IAM instance profile**.
For more information, see [Create a launch template using advanced
settings](./advanced-settings-for-your-launch-template.html).

When you create the launch template using the [create-launch-
template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-
launch-template.html) command from the AWS CLI, specify the instance profile
name of your IAM role as shown in the following example.

    
    
    aws ec2 create-launch-template --launch-template-name my-lt-with-instance-profile --version-description version1 \
    --launch-template-data '{"ImageId":"ami-04d5cc9b88example","InstanceType":"t2.micro","IamInstanceProfile":{"Name":"my-instance-profile"}}'

## See also

For more information to help you start learning about and using IAM roles for
Amazon EC2, see:

  * [IAM roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) in the _Amazon EC2 User Guide_

  * [Using instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) and [Using an IAM role to grant permissions to applications running on Amazon EC2 instances](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html) in the _IAM User Guide_

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Control Amazon EC2 launch template usage in Auto Scaling groups

Compliance validation

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

