### ControlGen Output - Arquivo 1
```json
[
  {
    "Title": "Enforce Multi-Factor Authentication (MFA) for AWS Accounts",
    "Description": "Ensure that all AWS accounts have multi-factor authentication (MFA) enabled, especially for users with administrative privileges. Implement IAM policies to deny access when MFA is not enabled.",
    "Applicability": "All AWS accounts with IAM users",
    "Security Risk": "Without MFA, accounts are more vulnerable to unauthorized access, potentially leading to data breaches or unauthorized actions within the account.",
    "Default Behavior / Limitations": "AWS IAM does not enforce MFA by default; it must be configured manually.",
    "Automation": "Can be enforced using IAM policies and AWS Config rule `iam-user-mfa-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/data-protection.html"
    ]
  },
  {
    "Title": "Enforce TLS 1.2 or Higher for Communication with AWS Resources",
    "Description": "Configure all AWS resources to use SSL/TLS for communication, requiring TLS 1.2 as a minimum and recommending TLS 1.3 where possible. Ensure that security policies and network settings enforce the use of these protocols.",
    "Applicability": "All services communicating with AWS resources",
    "Security Risk": "Communication using outdated or unsecured protocols can lead to data interception and man-in-the-middle attacks.",
    "Default Behavior / Limitations": "AWS supports TLS 1.2 or higher, but enforcement depends on customer configuration.",
    "Automation": "Can be monitored using AWS Config rule `cloudfront-encryption-protocols-policy` for CloudFront and similar rules for other services.",
    "References": [
      "https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/data-protection.html"
    ]
  },
  {
    "Title": "Enable and Configure AWS CloudTrail for API and User Activity Logging",
    "Description": "Enable AWS CloudTrail in all regions and configure it to log both management and data events for auditing API calls and changes in account settings.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without logging, unauthorized activities might remain undetected, reducing the ability to audit and trace changes.",
    "Default Behavior / Limitations": "AWS CloudTrail is available but not enabled by default; customers must configure it.",
    "Automation": "Can be automated using AWS Config rule `cloud-trail-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/data-protection.html"
    ]
  },
  {
    "Title": "Utilize AWS Encryption Solutions for Data at Rest and in Transit",
    "Description": "Ensure that all data at rest is encrypted using AWS native solutions such as AWS KMS, and data in transit is secured using SSL/TLS protocols.",
    "Applicability": "All AWS resources storing or processing sensitive data",
    "Security Risk": "Unencrypted data could lead to unauthorized access and data breaches.",
    "Default Behavior / Limitations": "AWS provides encryption solutions, but implementation depends on customer configuration.",
    "Automation": "Can be monitored using AWS Config rules like `rds-storage-encrypted` and `s3-bucket-server-side-encryption-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/kms/latest/developerguide/overview.html",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/data-protection.html"
    ]
  },
  {
    "Title": "Prohibit Inclusion of Sensitive Data in Tags or Free-Form Text Fields",
    "Description": "Implement policies and monitoring to ensure sensitive information is not included in resource tags or free-form text fields.",
    "Applicability": "All AWS resources utilizing tagging or metadata fields",
    "Security Risk": "Embedding sensitive data in tags or text fields can lead to unauthorized access through metadata retrieval.",
    "Default Behavior / Limitations": "AWS does not natively enforce content of tags or text fields; requires manual checks.",
    "Automation": "Manual validation required; use AWS Lambda functions or custom AWS Config rules for scanning.",
    "References": [
      "https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/data-protection.html"
    ]
  },
  {
    "Title": "Use FIPS 140-3 Validated Cryptographic Modules",
    "Description": "Ensure compliance with federal standards by using FIPS 140-3 validated cryptographic modules for encryption.",
    "Applicability": "AWS accounts requiring compliance with federal regulations",
    "Security Risk": "Non-compliance with encryption standards can lead to legal and operational risks.",
    "Default Behavior / Limitations": "AWS provides FIPS compliance for certain services; users must select these endpoints.",
    "Automation": "Selection of FIPS-compliant endpoints requires manual configuration; no automated enforcement.",
    "References": [
      "https://aws.amazon.com/compliance/fips/",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/data-protection.html"
    ]
  },
  {
    "Title": "Leverage VPC Endpoints for Private AWS Resource Access",
    "Description": "Configure VPC endpoints to access AWS Service Catalog APIs privately, eliminating the need for internet gateways or VPN connections.",
    "Applicability": "All VPCs interacting with AWS Service Catalog",
    "Security Risk": "Using public internet gateways increases exposure to potential attack vectors.",
    "Default Behavior / Limitations": "VPC endpoints are not configured by default; needs manual setup.",
    "Automation": "Can be automated through AWS CloudFormation or custom scripts.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/data-protection.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 2
```json
[
  {
    "Title": "Grant AWS Service Catalog Administrators Full Access",
    "Description": "IAM roles assigned to AWS Service Catalog administrators must include comprehensive permissions to manage portfolios, products, constraints, and access for end users. This can be achieved by assigning the AWS managed policy 'AWSServiceCatalogAdminFullAccess' to the administrator roles.",
    "Applicability": "All AWS accounts with Service Catalog usage",
    "Security Risk": "Without appropriate permissions, administrators may be unable to manage catalog components effectively, leading to misconfigurations and availability issues.",
    "Default Behavior / Limitations": "IAM does not automatically assign this level of access; it must be explicitly configured.",
    "Automation": "Can be implemented by attaching the 'AWSServiceCatalogAdminFullAccess' managed policy to administrator roles in IAM.",
    "References": [
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/controlling_access.html",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security-iam-awsmanpol.html"
    ]
  },
  {
    "Title": "Grant End Users Access to AWS Service Catalog",
    "Description": "IAM roles for end users should include permissions for accessing the AWS Service Catalog end user console and optionally managing provisioned products, using the managed policy 'AWSServiceCatalogEndUserFullAccess'.",
    "Applicability": "All AWS accounts where end users need Service Catalog access",
    "Security Risk": "Incorrect configurations could lead to unauthorized access or inability to use needed resources, affecting productivity.",
    "Default Behavior / Limitations": "IAM does not define end user roles by default; they must be set up according to organizational needs.",
    "Automation": "Can be implemented by attaching the 'AWSServiceCatalogEndUserFullAccess' managed policy to end user roles in IAM.",
    "References": [
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/controlling_access.html",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security-iam-awsmanpol.html"
    ]
  },
  {
    "Title": "Utilize AWS Managed Policies for Service Catalog IAM Policy Creation",
    "Description": "Administrators should create IAM policies for AWS Service Catalog access control by reviewing AWS managed policies as examples to ensure comprehensive permissions are configured for required roles.",
    "Applicability": "Organizations utilizing AWS Service Catalog",
    "Security Risk": "Poorly configured IAM policies could lead to unauthorized access or limit functionality required by roles, impacting security and efficiency.",
    "Default Behavior / Limitations": "AWS provides managed policies, but custom policies need to be manually tailored based on these examples.",
    "Automation": "Manual validation required for custom policy creation, although baseline policies can be derived from AWS managed policies.",
    "References": [
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security-iam-awsmanpol.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 3
```json
[
  {
    "Title": "Enforce Trust Policy for AWSServiceRoleForServiceCatalogSync",
    "Description": "Ensure the service-linked role `AWSServiceRoleForServiceCatalogSync` has a trust policy allowing the service `sync.servicecatalog.amazonaws.com` to assume the role with specified permissions.",
    "Applicability": "All AWS accounts using AWS Service Catalog",
    "Security Risk": "If the trust policy is not properly configured, unauthorized entities may assume the service-linked role, leading to unauthorized modifications in CodeConnections and ProvisioningArtifact resources.",
    "Default Behavior / Limitations": "The role is created with the correct policies automatically when needed, but relying on manual setup may introduce errors.",
    "Automation": "Monitor using AWS Config to ensure the correct trust policy is applied to the service-linked role.",
    "References": [
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/using-service-linked-roles.html"
    ]
  },
  {
    "Title": "Enforce Trust Policy for AWSServiceRoleForServiceCatalogOrgsDataSync",
    "Description": "Ensure the service-linked role `AWSServiceRoleForServiceCatalogOrgsDataSync` has a trust policy allowing the service `orgsdatasync.servicecatalog.amazonaws.com` to assume the role with specific actions on AWS Organizations resources.",
    "Applicability": "Organizations using AWS Service Catalog with AWS Organizations",
    "Security Risk": "Improper trust policies may lead to unauthorized access to sensitive organization data or misconfiguration of organization accounts.",
    "Default Behavior / Limitations": "The role is generated with correct policies upon creation by AWS services.",
    "Automation": "Verify trust policies using AWS Config in conjunction with AWS Organizations to uphold correct configurations.",
    "References": [
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/using-service-linked-roles.html"
    ]
  },
  {
    "Title": "Automate Creation of Service-Linked Roles in AWS Service Catalog",
    "Description": "Utilize AWS Service Catalog to automatically create service-linked roles such as `AWSServiceRoleForServiceCatalogSync` and `AWSServiceRoleForServiceCatalogOrgsDataSync` when performing actions like establishing CodeConnections or enabling AWS Organizations.",
    "Applicability": "All AWS accounts utilizing AWS Service Catalog for automation features",
    "Security Risk": "Manual creation of roles could lead to misconfigurations, inconsistent deployments, and potential security gaps.",
    "Default Behavior / Limitations": "AWS automatically creates these service-linked roles when required operations are performed.",
    "Automation": "AWS handles this automatically, ensuring the roles are created correctly without manual intervention.",
    "References": [
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/using-service-linked-roles.html"
    ]
  },
  {
    "Title": "Ensure Resources are Removed Before Deleting Service-Linked Roles",
    "Description": "Before deleting any service-linked roles associated with AWS Service Catalog, remove all linked resources to avoid accidental permission loss or service disruptions.",
    "Applicability": "Administrative roles managing AWS Service Catalog",
    "Security Risk": "Failure to remove resources before deletion could disrupt service operations and lead to loss of permissions necessary for critical business functions.",
    "Default Behavior / Limitations": "Deletions are not validated or enforced automatically by AWS.",
    "Automation": "Manual validation required as AWS does not automate resource dependency checks prior to service-linked role deletion.",
    "References": [
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/using-service-linked-roles.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 4
```json
[
  {
    "Title": "Enable CloudTrail Logging for AWS Service Catalog API Calls",
    "Description": "AWS CloudTrail must be configured to capture and log all API calls made to AWS Service Catalog in all available regions. Ensure logs are delivered to a specified and secured Amazon S3 bucket.",
    "Applicability": "All AWS accounts using AWS Service Catalog",
    "Security Risk": "Without logging, unauthorized actions and security incidents could go untracked, increasing the risk of undetected data breaches and configuration changes.",
    "Default Behavior / Limitations": "AWS CloudTrail is not enabled by default for AWS Service Catalog. Users must manually set up CloudTrail and specify the S3 bucket for log storage.",
    "Automation": "Can be enforced using AWS Config with custom rules to ensure CloudTrail is configured to log AWS Service Catalog API calls. Use IAM policies to restrict access to the S3 bucket.",
    "References": [
      "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/logging-and-monitoring.html"
    ]
  },
  {
    "Title": "Configure AWS SNS Notifications for AWS Service Catalog Stack Events",
    "Description": "AWS Service Catalog must be configured to use AWS SNS notifications for stack events, ensuring notifications are correctly set up through notification constraints. Verify that the SNS topic has the appropriate access policy.",
    "Applicability": "All AWS accounts utilizing AWS Service Catalog to manage stacks",
    "Security Risk": "Without proper notification of stack events, critical changes could go unnoticed, potentially leading to unmonitored deployments and unnoticed failures.",
    "Default Behavior / Limitations": "AWS Service Catalog does not automatically configure SNS notifications. Users must configure SNS topics and notification constraints manually.",
    "Automation": "Manual validation required to ensure SNS topics and permissions are configured correctly, as automation depends on the specific architecture and integration of the SNS topics.",
    "References": [
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/notifying-events.html",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/logging-and-monitoring.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 5
```json
[
  {
    "Title": "Enforce TLS 1.2 or 1.3 for AWS Service Catalog Communications",
    "Description": "Configure AWS Service Catalog and all interacting client systems to enforce Transport Layer Security (TLS) version 1.2 or 1.3 for all communications to ensure encryption and secure communication channels.",
    "Applicability": "All AWS accounts using AWS Service Catalog",
    "Security Risk": "Using outdated versions of TLS increases the risk of eavesdropping, man-in-the-middle attacks, and data breaches due to vulnerabilities in older protocols.",
    "Default Behavior / Limitations": "AWS services typically require TLS 1.2 or higher by default, but client systems interfacing with AWS must also be configured to support it.",
    "Automation": "Monitor and enforce using AWS Config rule `tls-v12-enabled` to validate enforcement of TLS 1.2 or 1.3 on connected resources.",
    "References": [
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/infrastructure-security.html",
      "https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-fsbp-controls.html"
    ]
  },
  {
    "Title": "Enforce Use of Cipher Suites with Perfect Forward Secrecy (PFS)",
    "Description": "Ensure that all communication with AWS Service Catalog utilizes cipher suites that support Perfect Forward Secrecy (PFS) such as DHE or ECDHE to enhance session security and protect past sessions from future compromises.",
    "Applicability": "All AWS accounts using AWS Service Catalog",
    "Security Risk": "Without PFS, compromised server keys could lead to the decryption of past sessions, compromising data confidentiality.",
    "Default Behavior / Limitations": "AWS services often prefer or enforce PFS-enabled cipher suites, but client-side configurations must be verified.",
    "Automation": "Manual validation required; verify configurations for compatibility with PFS-enabled cipher suites.",
    "References": [
      "https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-tls-listener.html",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/infrastructure-security.html"
    ]
  },
  {
    "Title": "Sign All Requests to AWS Service Catalog Using IAM Credentials or STS",
    "Description": "Configure all API requests to AWS Service Catalog to be signed using AWS Signature Version 4 with an IAM user's access key ID and secret access key or temporary credentials from AWS Security Token Service (STS).",
    "Applicability": "All AWS accounts using AWS Service Catalog",
    "Security Risk": "Unsigned or improperly signed requests can lead to unauthorized access or man-in-the-middle attacks, threatening the integrity and confidentiality of requests.",
    "Default Behavior / Limitations": "AWS requires requests to be signed, but correct configuration is necessary for enforcement.",
    "Automation": "Verify through AWS CloudTrail to monitor API calls and check for signed requests.",
    "References": [
      "https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/infrastructure-security.html"
    ]
  },
  {
    "Title": "Control AWS Service Catalog Product Availability by Region",
    "Description": "Use the AWS Service Catalog `CopyProduct` API to control in which AWS Regions your portfolios and products are available, ensuring data residency and compliance requirements are met.",
    "Applicability": "All AWS accounts using AWS Service Catalog",
    "Security Risk": "Unrestricted data placement across regions can lead to compliance violations and data sovereignty issues.",
    "Default Behavior / Limitations": "Manual configuration required; AWS does not restrict region replication by default for products.",
    "Automation": "Utilize AWS CloudFormation or AWS Service Catalog APIs for automated deployment and management of products across specific regions.",
    "References": [
      "https://docs.aws.amazon.com/servicecatalog/latest/dg/API_CopyProduct.html",
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/infrastructure-security.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 6
```json
[
  {
    "Title": "Implement Template Constraints for AWS CloudFormation",
    "Description": "Create template constraints within AWS Service Catalog for CloudFormation templates to control parameter values that users can enter when launching resources. These constraints ensure compliance with organizational security policies by enforcing a set of allowable values and limits, such as instance types, AMI IDs, and key pairs.",
    "Applicability": "All products and services deployed via AWS Service Catalog in the organization",
    "Security Risk": "Without template constraints, users may deploy resources that don't comply with security policies, resulting in potential exposure to security vulnerabilities and non-compliance with regulatory requirements.",
    "Default Behavior / Limitations": "AWS CloudFormation templates do not have constraints by default; they must be specified manually in the Service Catalog.",
    "Automation": "Can be enforced by configuring template constraints in AWS Service Catalog portfolios and products.",
    "References": [
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security-best-practices.html"
    ]
  },
  {
    "Title": "Apply Restrictive Constraints for Product Provisioning in AWS Service Catalog",
    "Description": "Define and apply the most restrictive constraints when provisioning or updating a product within AWS Service Catalog. For example, restrict instance types to a predefined list such as 't1.micro' and 'm1.small' to ensure cost-effective and secure deployments.",
    "Applicability": "All products and services provisioned via AWS Service Catalog",
    "Security Risk": "Lack of restrictive constraints can lead to unexpected resource usage, increased costs, and deployment of non-compliant resources that pose security risks.",
    "Default Behavior / Limitations": "Constraints must be defined manually; no default restrictions are applied.",
    "Automation": "Constraint enforcement is managed through AWS Service Catalog configurations.",
    "References": [
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security-best-practices.html"
    ]
  },
  {
    "Title": "Limit User Access to Resources with IAM Policies and Launch Constraints",
    "Description": "Attach a restrictive IAM policy to a launch role and utilize AWS Service Catalog to create launch constraints for roles to limit user access to AWS resources. This establishes role-based access control (RBAC), segmenting access according to user roles and permissions.",
    "Applicability": "All roles used to provision products via AWS Service Catalog",
    "Security Risk": "Failure to limit user access can result in unauthorized access to AWS resources, leading to potential data breaches and unauthorized modifications or deletions.",
    "Default Behavior / Limitations": "IAM policies provide the mechanism to enforce role-based access control but must be appropriately configured.",
    "Automation": "Role-based access controls can be enforced through IAM policies and AWS Service Catalog launch constraints.",
    "References": [
      "https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security-best-practices.html"
    ]
  }
]
```