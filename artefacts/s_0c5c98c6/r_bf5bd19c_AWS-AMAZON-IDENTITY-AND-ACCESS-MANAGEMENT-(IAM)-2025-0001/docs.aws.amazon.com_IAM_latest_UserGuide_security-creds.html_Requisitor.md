```json
[
  {
    "Description": "Multi-factor authentication (MFA) must be enabled on the AWS account root user and all IAM users.",
    "Reference": "[AWS Multi-factor authentication in IAM](./id_credentials_mfa.html) - URL: https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html",
    "Observations": "This adds an additional layer of security for accessing AWS accounts."
  },
  {
    "Description": "Centrally manage and secure the root user credentials of AWS accounts using AWS Organizations.",
    "Reference": "[Centrally manage root access for member accounts](./id_root-user.html#id_root-user-access-management) - URL: https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html",
    "Observations": "This prevents unintended root access at scale and simplifies credential management."
  },
  {
    "Description": "Use IAM policies to securely control access to AWS services and resources.",
    "Reference": "[Policies](./access_policies.html) - URL: https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html",
    "Observations": "Policies determine user actions in the AWS account based on defined conditions."
  },
  {
    "Description": "Temporary security credentials provided by IAM roles and federated users should be used instead of long-term credentials.",
    "Reference": "Temporary credentials section - URL: https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html",
    "Observations": "Avoids embedding long-term credentials and reduces the risk of credential leakage."
  },
  {
    "Description": "An AWS Organizations service control policy (SCP) can be used to limit the permissions of the root user.",
    "Reference": "[Service control policy (SCP)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_type-auth.html) - URL: https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html",
    "Observations": "Direct IAM policies cannot explicitly deny root user access."
  },
  {
    "Description": "Ensure to save sign-in credentials and access keys in a secure location for _Emergency Access_ IAM user.",
    "Reference": "Security considerations section - URL: https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html",
    "Observations": "Necessary for recovery in case of lost access keys or credentials."
  }
]
```
