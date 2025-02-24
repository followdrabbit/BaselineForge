```json
[
  {
    "Title": "Enforce IAM Policy Naming Convention for Amazon SimpleDB",
    "Description": "IAM policies granting access to Amazon SimpleDB must specify actions with the prefix 'sdb:'. Ensure all actions like 'sdb:GetAttributes', 'sdb:Select', or 'sdb:*' are correctly defined within IAM policies.",
    "Applicability": "All IAM policies related to Amazon SimpleDB",
    "Security Risk": "Improper permissions due to incorrect action prefixes might lead to unauthorized access to SimpleDB resources.",
    "Default Behavior / Limitations": "IAM does not enforce action prefixes by default. They must be explicitly defined.",
    "Automation": "AWS Config custom rules or AWS IAM Access Analyzer can audit adherence to the naming convention.",
    "References": [
      "https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/UsingIAMWithSDB.html"
    ]
  },
  {
    "Title": "Specify Correct Amazon SimpleDB Domain ARNs Including Region",
    "Description": "Ensure Amazon SimpleDB domains are specified using the ARN format `arn:aws:sdb:<region>:<account_ID>:domain/<domain_name>`, ensuring the <region> parameter is included.",
    "Applicability": "All IAM policies and resource-based policies utilizing SimpleDB domains",
    "Security Risk": "Incorrect ARN formats can lead to misconfigured access and potential security breaches.",
    "Default Behavior / Limitations": "IAM policy validation does not automatically enforce correct ARN formats.",
    "Automation": "AWS Config custom rules can monitor the correctness of ARNs, particularly focusing on region specification.",
    "References": [
      "https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/UsingIAMWithSDB.html"
    ]
  },
  {
    "Title": "Apply Least Privilege Principle for SimpleDB Read Actions",
    "Description": "Policies granting read access to Amazon SimpleDB should specify actions such as `sdb:GetAttributes` and `sdb:Select` to adhere to the principle of least privilege.",
    "Applicability": "All IAM and resource-based policies granting read access to Amazon SimpleDB",
    "Security Risk": "Excessive permissions can lead to unauthorized data access and information exposure.",
    "Default Behavior / Limitations": "Broad permissions are allowed by default unless specific permissions are defined.",
    "Automation": "AWS IAM Access Analyzer can audit policies to ensure they respect least privilege principles.",
    "References": [
      "https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/UsingIAMWithSDB.html"
    ]
  },
  {
    "Title": "Utilize Deny Statements for Restricting Unwanted SimpleDB Actions",
    "Description": "Include `Deny` statements in IAM policies to explicitly prevent unwanted actions, especially when using broad permissions.",
    "Applicability": "All IAM policies with conditional broad permissions for Amazon SimpleDB",
    "Security Risk": "Policies without explicit deny conditions may become overly permissive, resulting in data manipulation or exposure.",
    "Default Behavior / Limitations": "IAM allows all actions not explicitly denied, so careful deny conditions must be defined.",
    "Automation": "AWS IAM Access Analyzer evaluates policy effectiveness in applying least privilege principles.",
    "References": [
      "https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/UsingIAMWithSDB.html"
    ]
  },
  {
    "Title": "Enforce Use of Temporary Security Credentials for Amazon SimpleDB Access",
    "Description": "Configure IAM roles to provide temporary security credentials for accessing Amazon SimpleDB, replacing AWSAccessKeyId with these credentials and including a valid SecurityToken parameter.",
    "Applicability": "All users accessing Amazon SimpleDB",
    "Security Risk": "Using permanent access keys increases risk of unauthorized access if compromised, leading to data exposure.",
    "Default Behavior / Limitations": "Temporary credentials need to be explicitly configured, AWS IAM does not enforce this automatically.",
    "Automation": "Automate through IAM roles configured with AWS STS and monitor access via AWS CloudTrail logs.",
    "References": [
      "https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/UsingTemporarySecurityCredentials_SDB.html",
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html"
    ]
  },
  {
    "Title": "Ensure HMAC-SHA256 Signing Method for SimpleDB Requests Using Temporary Credentials",
    "Description": "Verify that all requests to Amazon SimpleDB using temporary security credentials are signed with the HMAC-SHA256 method, setting the SignatureMethod field to HmacSHA256.",
    "Applicability": "All API requests to Amazon SimpleDB using temporary security credentials",
    "Security Risk": "Insecure signing methods can allow unauthorized request modification, leading to replay attacks or data integrity issues.",
    "Default Behavior / Limitations": "AWS SDKs default to HMAC-SHA256, but custom implementations must enforce this explicitly.",
    "Automation": "Automate verification using tools inspecting API request headers and events analyzed via AWS CloudTrail.",
    "References": [
      "https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/UsingTemporarySecurityCredentials_SDB.html",
      "https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html"
    ]
  }
]
```