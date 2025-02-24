### ControlGen Output - Arquivo 1
```json
[
  {
    "Title": "Enforce IAM Policy Naming Convention for Amazon SimpleDB",
    "Description": "IAM policies granting access to Amazon SimpleDB must specify actions with the prefix 'sdb:'. For instance, use 'sdb:GetAttributes', 'sdb:Select', or 'sdb:*' for all actions to define permissions correctly.",
    "Applicability": "All IAM policies related to Amazon SimpleDB",
    "Security Risk": "Failure to use correct action prefixes might result in improper permissions, which can lead to unauthorized access to SimpleDB resources.",
    "Default Behavior / Limitations": "IAM does not automatically enforce action prefixes. They must be explicitly defined in IAM policies.",
    "Automation": "Can be audited using AWS Config custom rules or AWS IAM Access Analyzer to ensure adherence to the naming convention.",
    "References": [
      "https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/UsingIAMWithSDB.html"
    ]
  },
  {
    "Title": "Specify Amazon SimpleDB Domain ARNs with Region",
    "Description": "Amazon SimpleDB domains must be specified using the ARN format `arn:aws:sdb:<region>:<account_ID>:domain/<domain_name>`, ensuring the <region> parameter is not left blank.",
    "Applicability": "All IAM policies and resource-based policies utilizing SimpleDB domains",
    "Security Risk": "Incorrect ARN specification can lead to security breaches or misconfigured access, as resources may not be accurately targeted.",
    "Default Behavior / Limitations": "IAM policy validation will not enforce correct ARN formats unless explicitly checked.",
    "Automation": "Monitoring can be implemented using AWS Config custom rules to validate the correctness of ARNs, focusing on region specification.",
    "References": [
      "https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/UsingIAMWithSDB.html"
    ]
  },
  {
    "Title": "Use Wildcard Characters in SimpleDB Domain ARNs",
    "Description": "Policies may use the `*` wildcard for multiple characters and `?` for single characters in Amazon SimpleDB domain names within ARNs, ensuring flexibility while adhering to naming conventions.",
    "Applicability": "All resource-based IAM policies for Amazon SimpleDB",
    "Security Risk": "Improper use of wildcards may lead to overbroad access or denial of access where intended, compromising security or functionality.",
    "Default Behavior / Limitations": "IAM policy language supports wildcards but requires careful implementation to avoid unintended matches.",
    "Automation": "Manual validation required to ensure wildcard usage aligns with resource naming conventions and security requirements.",
    "References": [
      "https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/UsingIAMWithSDB.html"
    ]
  },
  {
    "Title": "Apply Least Privilege Principle for SimpleDB Read Actions",
    "Description": "Policies granting read access to Amazon SimpleDB should specifically allow actions like `sdb:GetAttributes` and `sdb:Select` rather than broad permissions, ensuring adherence to the principle of least privilege.",
    "Applicability": "All IAM and resource-based policies granting read access to Amazon SimpleDB",
    "Security Risk": "Granting excessive permissions can lead to unauthorized data access, thus exposing sensitive information.",
    "Default Behavior / Limitations": "IAM policies allow broad permissions but specific permissions must be defined by policy creators.",
    "Automation": "Audited using AWS IAM Access Analyzer for policies respecting least privilege principles.",
    "References": [
      "https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/UsingIAMWithSDB.html"
    ]
  },
  {
    "Title": "Utilize Deny Statements for Restricting Unwanted SimpleDB Actions",
    "Description": "IAM policies should include `Deny` statements to explicitly prevent unwanted actions, specifying precise actions that are allowed, especially when broad permissions are in use.",
    "Applicability": "All IAM policies with conditional broad permissions for Amazon SimpleDB",
    "Security Risk": "Without explicit deny conditions, policies can become too permissive, resulting in unauthorized data manipulation or exposure.",
    "Default Behavior / Limitations": "IAM allows all actions not explicitly denied; care must be taken to define proper deny conditions.",
    "Automation": "Can be enforced via AWS IAM Access Analyzer for evaluating policy effectiveness in applying least privilege principles.",
    "References": [
      "https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/UsingIAMWithSDB.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 2
```json
[
  {
    "Title": "Enforce Use of Temporary Security Credentials for Amazon SimpleDB Access",
    "Description": "Configure IAM roles to provide temporary security credentials for accessing Amazon SimpleDB. Ensure that all request signatures replace AWSAccessKeyId with these temporary credentials and include a valid SecurityToken parameter.",
    "Applicability": "All users accessing Amazon SimpleDB",
    "Security Risk": "Failure to use temporary credentials could lead to unauthorized access if permanent access keys are compromised, increasing the risk of data exposure and credential misuse.",
    "Default Behavior / Limitations": "Temporary security credentials must be generated through AWS STS and configured explicitly for SimpleDB access. AWS IAM does not enforce this automatically.",
    "Automation": "This control can be automated using IAM roles configured with AWS STS and monitoring access patterns via AWS CloudTrail logs.",
    "References": [
      "https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/UsingTemporarySecurityCredentials_SDB.html",
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html"
    ]
  },
  {
    "Title": "Ensure HMAC-SHA256 Signing Method for SimpleDB Requests Using Temporary Credentials",
    "Description": "Verify that all requests to Amazon SimpleDB, when using temporary security credentials, are signed using the HMAC-SHA256 method. The SignatureMethod field in these requests must be set to HmacSHA256.",
    "Applicability": "All API requests to Amazon SimpleDB using temporary security credentials",
    "Security Risk": "Using an insecure or unsupported signing method could allow unauthorized modification of requests, leading to potential replay attacks or data integrity issues.",
    "Default Behavior / Limitations": "AWS SDKs and tools typically use HMAC-SHA256 by default. However, custom implementations must be configured to enforce this explicitly.",
    "Automation": "Automate verification using tools that inspect API request headers and verify the SignatureMethod field. AWS CloudTrail can be configured to capture events, which can then be analyzed.",
    "References": [
      "https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/UsingTemporarySecurityCredentials_SDB.html",
      "https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html"
    ]
  }
]
```