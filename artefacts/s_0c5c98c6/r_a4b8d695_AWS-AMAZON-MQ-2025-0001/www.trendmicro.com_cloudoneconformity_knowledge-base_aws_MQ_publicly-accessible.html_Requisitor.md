```json
[
    {
        "Description": "Ensure that Amazon MQ brokers in your AWS account are not publicly accessible from the Internet.",
        "Reference": "Publicly Accessible MQ Brokers Section - Rule ID: MQ-002 - URL: https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/publicly-accessible.html",
        "Observations": "Publicly accessible MQ brokers increase security risks such as XSS and clickjacking attacks by allowing every machine on the Internet to reach them."
    },
    {
        "Description": "Use AWS CLI to automate the audit of Amazon MQ brokers' public accessibility using 'describe-broker' to check if 'PubliclyAccessible' is true.",
        "Reference": "Audit Section - Using AWS CLI - URL: https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/publicly-accessible.html",
        "Observations": "Automatically determine which MQ brokers are publicly accessible using AWS CLI commands."
    },
    {
        "Description": "Configure Amazon MQ broker creation with 'PubliclyAccessible' set to 'false' using AWS CloudFormation.",
        "Reference": "Remediation Section - AWS CloudFormation Templates - URL: https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/publicly-accessible.html",
        "Observations": "The CloudFormation template can be used to automate the process of ensuring brokers are not publicly accessible."
    },
    {
        "Description": "Define Terraform configuration with 'publicly_accessible = false' for Amazon MQ broker creation.",
        "Reference": "Remediation Section - Using Terraform - URL: https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/publicly-accessible.html",
        "Observations": "Use Terraform to ensure that the created MQ brokers are not publicly accessible."
    },
    {
        "Description": "Automate the Amazon MQ broker re-creation process to enable only private VPC access using AWS CLI with '--no-publicly-accessible'.",
        "Reference": "Remediation Section - Using AWS CLI - URL: https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/publicly-accessible.html",
        "Observations": "Use AWS CLI to ensure the new MQ broker configuration restricts public access."
    }
]
```
