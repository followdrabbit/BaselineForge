```json
[
  {
    "Description": "Use the `aws:SourceArn` and `aws:SourceAccount` global condition context keys in resource policies to limit permissions that Amazon RDS gives to another service.",
    "Reference": "Section on 'Preventing cross-service confused deputy problems' in the documentation (Markdown) - URL: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/cross-service-confused-deputy-prevention.html",
    "Observations": "This is a preventive measure to avoid cross-service impersonation issues."
  },
  {
    "Description": "Use both `aws:SourceArn` and `aws:SourceAccount` when the `aws:SourceArn` value lacks the account ID.",
    "Reference": "Section on 'Preventing cross-service confused deputy problems' in the documentation (Markdown) - URL: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/cross-service-confused-deputy-prevention.html",
    "Observations": "Ensures that permissions are accurately scoped in the absence of account ID in `aws:SourceArn`."
  },
  {
    "Description": "Ensure `aws:SourceArn` is an ARN for an Amazon RDS resource type.",
    "Reference": "Section on 'Preventing cross-service confused deputy problems' in the documentation (Markdown) - URL: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/cross-service-confused-deputy-prevention.html",
    "Observations": "Validates that the ARN used is specific to Amazon RDS, which is critical for precise access controls."
  },
  {
    "Description": "Use `aws:SourceArn` with wildcards (`*`) for unknown portions of the ARN if the full ARN of the resource is not known.",
    "Reference": "Section on 'Preventing cross-service confused deputy problems' in the documentation (Markdown) - URL: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/cross-service-confused-deputy-prevention.html",
    "Observations": "Useful for scenarios where only partial ARN information is available."
  }
]
```