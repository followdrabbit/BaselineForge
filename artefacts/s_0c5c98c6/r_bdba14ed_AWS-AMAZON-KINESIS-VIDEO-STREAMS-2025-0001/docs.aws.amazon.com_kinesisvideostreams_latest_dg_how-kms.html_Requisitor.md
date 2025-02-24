```json
[
  {
    "Description": "Server-side encryption must always be enabled on Kinesis Video Streams. If no user-provided key is specified, the AWS managed key is used by default.",
    "Reference": "https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-kms.html, Section: How do I get started with server-side encryption?",
    "Observations": "This is a default configuration and does not require additional configuration unless a user-provided KMS key is needed."
  },
  {
    "Description": "A user-provided KMS key must be assigned at the creation of a Kinesis video stream and cannot be reassigned using the UpdateStream API later.",
    "Reference": "https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-kms.html, Section: How do I get started with server-side encryption?",
    "Observations": "Ensure the correct KMS key is specified during the stream creation if custom KMS keys are utilized."
  },
  {
    "Description": "Kinesis Video Stream producers must have the \"kms:GenerateDataKey\" and \"kinesis-video:PutMedia\" permissions for encrypting data.",
    "Reference": "https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-kms.html, Section: Example producer permissions",
    "Observations": "Verify IAM policies that grant these permissions to avoid stream write failures."
  },
  {
    "Description": "Kinesis Video Stream consumers must have the \"kms:Decrypt\" and \"kinesis-video:GetMedia\" permissions for decrypting data.",
    "Reference": "https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-kms.html, Section: Example consumer permissions",
    "Observations": "Ensure consumers have these permissions to prevent read failures from streams."
  },
  {
    "Description": "API requests for AWS KMS to generate or retrieve encryption keys incur usage costs.",
    "Reference": "https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-kms.html, Section: AWS KMS API usage",
    "Observations": "Plan for AWS KMS API usage costs, which vary with the number of user credentials and traffic."
  },
  {
    "Description": "To use customer managed keys in a different AWS account, permissions must be in place to allow cross-account use of those keys.",
    "Reference": "https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-kms.html, Section: Using a customer managed key",
    "Observations": "Set up cross-account IAM permissions correctly to avoid operational failures."
  }
]
```