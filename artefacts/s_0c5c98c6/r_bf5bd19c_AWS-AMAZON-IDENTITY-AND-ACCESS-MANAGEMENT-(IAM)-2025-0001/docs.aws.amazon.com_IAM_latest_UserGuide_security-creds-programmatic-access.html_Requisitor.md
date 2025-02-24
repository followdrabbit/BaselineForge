```json
[
  {
    "Description": "Use short-term access keys when possible instead of long-term AWS access keys.",
    "Reference": "Section 'Alternatives to long-term access keys' in the documentation - URL: https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds-programmatic-access.html",
    "Observations": "Temporary credentials have a limited lifetime and are more secure."
  },
  {
    "Description": "Don't embed long-term access keys and secret access keys in your application code or in a code repository.",
    "Reference": "Section 'Alternatives to long-term access keys' - URL: https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds-programmatic-access.html",
    "Observations": "Use AWS Secrets Manager or another secrets management solution to store secrets."
  },
  {
    "Description": "Use IAM roles to generate temporary security credentials whenever possible.",
    "Reference": "Section 'Alternatives to long-term access keys' - URL: https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds-programmatic-access.html",
    "Observations": "Temporary security credentials are generated dynamically and are not stored with the user."
  },
  {
    "Description": "Use AWS CloudShell or AWS CLI Version 2 with IAM Identity Center for short-term access key management.",
    "Reference": "Section 'Alternatives to long-term access keys' - URL: https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds-programmatic-access.html",
    "Observations": "CloudShell provides a browser-based shell, and CLI V2 integrates with IAM Identity Center for authentication."
  },
  {
    "Description": "Don't create long-term access keys for human users needing access to AWS services.",
    "Reference": "Section 'Alternatives to long-term access keys' - URL: https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds-programmatic-access.html",
    "Observations": "Use IAM Identity Center to generate temporary credentials and manage access through permission sets."
  },
  {
    "Description": "Don't store long-term access keys within an AWS compute service. Use IAM roles instead.",
    "Reference": "Section 'Alternatives to long-term access keys' - URL: https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds-programmatic-access.html",
    "Observations": "Assign an IAM role to compute resources for automatic temporary credential assignment."
  }
]
```