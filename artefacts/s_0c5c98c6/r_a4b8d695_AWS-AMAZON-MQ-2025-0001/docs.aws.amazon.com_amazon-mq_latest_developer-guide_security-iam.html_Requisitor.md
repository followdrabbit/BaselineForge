```json
[
  {
    "Description": "Amazon MQ must log all API requests made to it and the service's operations using CloudTrail.",
    "Reference": "[How Amazon MQ works with IAM](./security_iam_service-with-iam.html) - URL: https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security-iam.html",
    "Observations": "Ensure that AWS CloudTrail is enabled for all regions to capture the logs."
  },
  {
    "Description": "Configure IAM policies to manage access to Amazon MQ resources, ensuring that only authorized users can perform actions on the resources.",
    "Reference": "[Managing access using policies](./security_iam_service-with-iam.html) - URL: https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security-iam.html",
    "Observations": "Use AWS IAM to create and attach policies that are based on specific business needs."
  },
  {
    "Description": "Use IAM roles with temporary credentials for applications running on Amazon EC2 instances to access AWS services securely.",
    "Reference": "[Applications running on Amazon EC2](./security_iam_service-with-iam.html) - URL: https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security-iam.html",
    "Observations": "Create an IAM role and assign it to an EC2 instance via an instance profile."
  },
  {
    "Description": "Rotate IAM user access keys regularly to minimize the risk of them being compromised.",
    "Reference": "[Rotate access keys regularly for use cases that require long-term credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#rotate-credentials) in the _IAM User Guide_",
    "Observations": "This practice helps mitigate security risks associated with leaked or outdated keys."
  },
  {
    "Description": "Enable multi-factor authentication (MFA) for accessing Amazon MQ and other AWS resources.",
    "Reference": "[AWS Multi-factor authentication in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html) in the _IAM User Guide_",
    "Observations": "MFA provides an extra layer of protection on top of usernames and passwords."
  },
  {
    "Description": "Use resource-based policies to define permissions for Amazon S3 or other applicable AWS services utilized by Amazon MQ.",
    "Reference": "[Resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json) in the _IAM User Guide_",
    "Observations": "Ensure that the appropriate policies are applied directly to resources to control access."
  }
]
```