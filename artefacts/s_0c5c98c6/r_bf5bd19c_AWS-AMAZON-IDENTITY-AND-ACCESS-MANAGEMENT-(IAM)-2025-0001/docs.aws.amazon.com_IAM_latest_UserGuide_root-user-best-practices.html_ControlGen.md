```json
[
  {
    "Title": "Enforce Multi-Factor Authentication (MFA) for Root User Sign-In",
    "Description": "Ensure that multi-factor authentication (MFA) is enabled for the root user of your AWS account. This is a critical security measure to protect your account from unauthorized access.",
    "Applicability": "Root user of all AWS accounts",
    "Security Risk": "Without MFA, the root account is vulnerable to unauthorized access if credentials are compromised, posing significant security risks.",
    "Default Behavior / Limitations": "AWS does not enforce MFA for root users by default. It must be manually configured.",
    "Automation": "Manual validation required to ensure MFA is enabled for root user. AWS Config rule `root-account-mfa-enabled` can help evaluate compliance.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html#root-user-mfa"
    ]
  },
  {
    "Title": "Prohibit Creation of Access Keys for Root User",
    "Description": "Do not create AWS access keys for the root user. Access should be managed through IAM users with more specific permissions.",
    "Applicability": "Root user of all AWS accounts",
    "Security Risk": "Access keys for the root user increase the risk of credential leakage and unauthorized access, leading to potential misuse of account privileges.",
    "Default Behavior / Limitations": "AWS allows creation of access keys for root users, but it is strongly discouraged.",
    "Automation": "Manual validation required to ensure root user does not have access keys. Regularly audit IAM credentials.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html#root-user-no-access-keys"
    ]
  },
  {
    "Title": "Require Strong and Unique Passwords for Root User",
    "Description": "Ensure that the root user password complies with AWS's recommended complexity requirements, including a mix of uppercase and lowercase letters, numbers, and symbols.",
    "Applicability": "Root user of all AWS accounts",
    "Security Risk": "Weak passwords increase the likelihood of unauthorized access to critical account functions.",
    "Default Behavior / Limitations": "AWS allows configuration of password policies for IAM users but does not enforce specific password complexity for root users.",
    "Automation": "Manual enforcement required to manage the root user's password complexity. Regular checks are advisable.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html#root-user-password"
    ]
  },
  {
    "Title": "Monitor and Notify on Root User Activity",
    "Description": "Configure Amazon EventBridge to monitor root user activities and CloudWatch to send notifications using SNS when root user activities are detected.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Root user activity without monitoring could lead to undetected unauthorized changes in the account.",
    "Default Behavior / Limitations": "AWS provides tools for monitoring but requires configuration to effectively track and notify root user actions.",
    "Automation": "Can be automated with Amazon EventBridge rules and CloudWatch alarms integrated with SNS to alert administrators.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html#root-user-monitoring"
    ]
  },
  {
    "Title": "Evaluate Root User MFA Compliance with AWS Config",
    "Description": "Utilize AWS Config rules to assess and ensure that MFA is enabled for root user credentials.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Lack of MFA on root accounts can lead to unauthorized access if credentials are compromised.",
    "Default Behavior / Limitations": "AWS provides AWS Config rules to evaluate compliance but does not automatically enforce MFA.",
    "Automation": "Can be automated using AWS Config rule `root-account-mfa-enabled` to continuously evaluate MFA compliance.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html#root-user-mfa-evaluation"
    ]
  },
  {
    "Title": "Restrict Root User Actions with Service Control Policies (SCP)",
    "Description": "Apply SCPs in AWS Organizations to restrict unnecessary root user actions and prevent unauthorized activities in member accounts.",
    "Applicability": "AWS Organizations",
    "Security Risk": "Excessive permissions for root users can lead to unauthorized changes across the organization's accounts.",
    "Default Behavior / Limitations": "SCPs provide a mechanism to limit permissions but require proper configuration.",
    "Automation": "Effective use of SCPs can automatically enforce restrictions on root activities across all member accounts.",
    "References": [
      "https://docs.aws.amazon.com/organizations/latest/userguide/best-practices_member-acct.html#bp_member-acct_use-scp"
    ]
  },
  {
    "Title": "Centralize Management of Root Credentials",
    "Description": "Securely manage and centralize root credentials within AWS Organizations, eliminating individual root access for member accounts and ensuring security measures like MFA are in place.",
    "Applicability": "AWS Organizations",
    "Security Risk": "Dispersed root credentials increase the threat surface and vulnerability to unauthorized account control.",
    "Default Behavior / Limitations": "AWS advises centralization but organizations must implement this by designing their management structure.",
    "Automation": "Manual implementation is necessary to centralize credential management and enforce security policies for root users.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html#secure-org-account"
    ]
  }
]
```