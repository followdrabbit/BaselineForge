```json
[
  {
    "Title": "Ensure Server-Side Encryption for Kinesis Video Streams",
    "Description": "Ensure server-side encryption (SSE) is enabled for all Kinesis Video Streams using the AWS managed KMS key by default unless a specific customer-managed key is provided during stream creation.",
    "Applicability": "All Kinesis Video Streams",
    "Security Risk": "Without server-side encryption, sensitive video data could be exposed, compromising confidentiality and compliance with data protection regulations.",
    "Default Behavior / Limitations": "AWS Kinesis Video Streams automatically uses an AWS managed key for encryption if no user-provided key is given.",
    "Automation": "Can be monitored using AWS Config rule `kinesis-video-server-side-encryption-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-kms.html#how-get-started"
    ]
  },
  {
    "Title": "Assign Custom KMS Key at Kinesis Video Stream Creation",
    "Description": "Assign a user-provided KMS key when creating a Kinesis video stream and ensure it cannot be changed later using the UpdateStream API.",
    "Applicability": "Kinesis Video Streams utilizing customer-managed KMS keys",
    "Security Risk": "Failure to assign the correct KMS key at creation can lead to encryption issues and inability to change keys post-creation, affecting data confidentiality.",
    "Default Behavior / Limitations": "KMS key assignment at stream creation is enforced. No changes allowed post-creation.",
    "Automation": "Manual validation required at the time of stream creation.",
    "References": [
      "https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-kms.html#how-get-started"
    ]
  },
  {
    "Title": "Verify IAM Permissions for Kinesis Video Stream Producers",
    "Description": "Ensure that Kinesis Video Stream producers have `kms:GenerateDataKey` and `kinesis-video:PutMedia` permissions for encrypting and streaming data to the video stream.",
    "Applicability": "IAM roles/users acting as Kinesis Video Stream producers",
    "Security Risk": "Lack of necessary IAM permissions can result in the inability to write stream data, causing data loss or stream interruptions.",
    "Default Behavior / Limitations": "IAM permissions must be explicitly set and verified.",
    "Automation": "Can be audited using IAM Access Analyzer.",
    "References": [
      "https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-kms.html#example-permissions-producer"
    ]
  },
  {
    "Title": "Verify IAM Permissions for Kinesis Video Stream Consumers",
    "Description": "Ensure that Kinesis Video Stream consumers have `kms:Decrypt` and `kinesis-video:GetMedia` permissions for decrypting and retrieving data from the video stream.",
    "Applicability": "IAM roles/users acting as Kinesis Video Stream consumers",
    "Security Risk": "Lack of necessary IAM permissions can result in failed data retrieval from streams, impacting application functionality and data access.",
    "Default Behavior / Limitations": "IAM permissions must be explicitly set and verified.",
    "Automation": "Can be audited using IAM Access Analyzer.",
    "References": [
      "https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-kms.html#example-permissions-consumer"
    ]
  },
  {
    "Title": "Monitor AWS KMS API Usage Costs for Kinesis Video Streams",
    "Description": "Monitor and plan for AWS KMS API usage costs associated with key generation and retrieval for encrypting Kinesis Video Streams. This ensures budgeting for the costs incurred by API requests.",
    "Applicability": "All accounts using AWS KMS for Kinesis Video Streams",
    "Security Risk": "Unanticipated costs can impact budgets, leading to uncontrolled spending and financial inefficiency.",
    "Default Behavior / Limitations": "AWS charges are based on usage and must be monitored through AWS Billing and Cost Management.",
    "Automation": "Can be monitored using AWS CloudWatch for budgeting alerts.",
    "References": [
      "https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-kms.html#using-key"
    ]
  },
  {
    "Title": "Set Up Cross-Account Permissions for Customer Managed Keys",
    "Description": "Ensure proper IAM permissions are set up for cross-account use of customer-managed KMS keys when Kinesis Video Streams reside in different AWS accounts.",
    "Applicability": "Organizations using cross-account KMS keys",
    "Security Risk": "Incorrect permissions can lead to operational failures and inability to encrypt or decrypt stream data, impacting data accessibility and security.",
    "Default Behavior / Limitations": "IAM permissions must be configured manually for cross-account use.",
    "Automation": "Manual validation required for IAM policy configuration.",
    "References": [
      "https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-kms.html#using-key"
    ]
  }
]
```