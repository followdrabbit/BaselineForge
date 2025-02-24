```json
[
    {
        "Title": "Enable Multi-Factor Authentication (MFA) for AWS Accounts",
        "Description": "Enforce multi-factor authentication (MFA) for all AWS account access to enhance security, focusing on AWS Management Console and API access. Use AWS IAM policies to mandate MFA enrollment for all users and roles.",
        "Applicability": "All AWS accounts",
        "Security Risk": "Without MFA, compromised credentials can allow unauthorized access to AWS resources, leading to data breaches.",
        "Default Behavior / Limitations": "AWS IAM does not enforce MFA by default; requires manual configuration.",
        "Automation": "Can be enforced using AWS IAM policies and AWS Config rule `iam-user-mfa-enabled`.",
        "References": [
            "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html"
        ]
    },
    {
        "Title": "Enforce TLS 1.2 or Later for Secure Communications",
        "Description": "Configure AWS services to require TLS 1.2 or later for all communications, ensuring data is encrypted in transit. Apply configuration settings in services such as ELB and CloudFront to enforce a minimum TLS version.",
        "Applicability": "All AWS services supporting TLS configuration",
        "Security Risk": "Outdated encryption protocols can lead to data interception and unauthorized access.",
        "Default Behavior / Limitations": "TLS 1.2 is not enforced by default for all services and must be explicitly set.",
        "Automation": "Use AWS Config rules such as `elbv2-desired-tls-policy` to ensure TLS policies compliance.",
        "References": [
            "https://aws.amazon.com/blogs/security/how-to-ensure-that-ssl-tls-traffic-is-encrypted/",
            "https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-fsbp-controls.html"
        ]
    },
    {
        "Title": "Enable and Configure AWS CloudTrail for Logging",
        "Description": "Ensure AWS CloudTrail is enabled in all regions to log API calls and user activities, delivering logs to an Amazon S3 bucket for retention and analysis.",
        "Applicability": "All AWS accounts",
        "Security Risk": "Without logging, unauthorized activities may go undetected, leading to potential data breaches and compliance issues.",
        "Default Behavior / Limitations": "AWS does not enable CloudTrail by default; it requires user configuration.",
        "Automation": "Enforce using AWS Config rule `cloud-trail-enabled` and monitor via AWS Security Hub.",
        "References": [
            "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html"
        ]
    },
    {
        "Title": "Implement Encryption for AWS Services",
        "Description": "Ensure the use of AWS managed encryption solutions to protect data at rest and in transit across all services.",
        "Applicability": "All AWS services",
        "Security Risk": "Unencrypted data is vulnerable to unauthorized access and potential data breaches.",
        "Default Behavior / Limitations": "Not all AWS services are encrypted by default; requires manual configuration.",
        "Automation": "Enforce and monitor using AWS Config and AWS Security Hub.",
        "References": [
            "https://docs.aws.amazon.com/general/latest/gr/aws-sec-standards.html"
        ]
    },
    {
        "Title": "Utilize FIPS 140-2 Validated Endpoints",
        "Description": "Configure AWS CLI and API to utilize FIPS endpoints where necessary to comply with federal standards.",
        "Applicability": "Environments requiring FIPS compliance",
        "Security Risk": "Non-compliance can result in weak cryptographic security and regulatory violations.",
        "Default Behavior / Limitations": "FIPS endpoints must be manually configured.",
        "Automation": "Manual validation is required to ensure endpoints are correctly configured.",
        "References": [
            "https://docs.aws.amazon.com/cli/latest/userguide/cli-fips.html"
        ]
    },
    {
        "Title": "Avoid Storing Sensitive Information in Tags or Comments",
        "Description": "Implement checks to prevent storing sensitive information in AWS resource tags or free-form text fields.",
        "Applicability": "All AWS resources",
        "Security Risk": "Sensitive data in unstructured fields may be exposed or leaked.",
        "Default Behavior / Limitations": "AWS does not automatically scan tags for sensitive data.",
        "Automation": "Use AWS Lambda and AWS Config rules to scan and notify of policy violations.",
        "References": [
            "https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"
        ]
    },
    {
        "Title": "Enforce Use of Instance Metadata Service Version 2 (IMDSv2)",
        "Description": "Configure Amazon EC2 instances and EMR clusters to enforce the use of IMDSv2 to enhance security against SSRF attacks.",
        "Applicability": "Amazon EC2 and EMR instances",
        "Security Risk": "IMDSv1 is vulnerable to SSRF attacks.",
        "Default Behavior / Limitations": "IMDSv1 is allowed by default; explicit configuration for IMDSv2 is required.",
        "Automation": "Enforce using AWS Config rules and IAM Instance Profiles.",
        "References": [
            "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html"
        ]
    },
    {
        "Title": "Restrict Data Pipeline Access with IAM Policies",
        "Description": "Create and manage IAM policies to restrict access to AWS Data Pipeline based on roles, permissions, and attributes.",
        "Applicability": "All AWS accounts using AWS Data Pipeline",
        "Security Risk": "Uncontrolled access can lead to data breaches and unauthorized data manipulation.",
        "Default Behavior / Limitations": "IAM requires explicit policy definition and attachment.",
        "Automation": "Monitor compliance using AWS Config with custom IAM policy rules.",
        "References": [
            "https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html"
        ]
    },
    {
        "Title": "Log API Requests and Identity in CloudTrail",
        "Description": "Ensure that CloudTrail logs all AWS API request activity with detailed event information and identity data for all operations.",
        "Applicability": "All AWS accounts",
        "Security Risk": "Lack of detailed logs can hinder forensic investigations and accountability.",
        "Default Behavior / Limitations": "CloudTrail logs include necessary details by default where applicable.",
        "Automation": "Manual validation required to ensure completeness of captured log details.",
        "References": [
            "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html"
        ]
    },
    {
        "Title": "Ensure AWS API Requests are Signed",
        "Description": "Require all AWS API requests to be signed with valid IAM credentials, using STS for temporary credentials to reduce the use of long-term credentials.",
        "Applicability": "All AWS API requests",
        "Security Risk": "Unsigned requests could lead to unauthorized access to AWS resources.",
        "Default Behavior / Limitations": "AWS SDKs and CLI require signed requests by default, but misuse prevention is necessary.",
        "Automation": "Enforce using AWS IAM policies ensuring APIs are not accessible with unsigned requests.",
        "References": [
            "https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html"
        ]
    }
]
```