```json
[
  {
    "Description": "Use the `aws:SourceArn` and `aws:SourceAccount` global condition context keys in resource policies to limit permissions for AWS Application Migration Service, preventing cross-service confused deputy problems.",
    "Reference": "Section 'Cross-service confused deputy prevention' - URL: https://docs.aws.amazon.com/mgn/latest/ug/cross-service-confused-deputy-prevention.html",
    "Observations": "Ensure that `aws:SourceAccount` matches the account ID in `aws:SourceArn` when both keys are used in the same policy statement."
  },
  {
    "Description": "The value of `aws:SourceArn` must be 'arn:aws:mgn:*:123456789012:source-server/*' to correctly implement policy conditions for AWS Application Migration Service.",
    "Reference": "Section 'Cross-service confused deputy prevention' - URL: https://docs.aws.amazon.com/mgn/latest/ug/cross-service-confused-deputy-prevention.html",
    "Observations": "This specific example restricts the ARN structure for the policy condition."
  },
  {
    "Description": "Use the `aws:SourceArn` global condition context key with the full ARN of the resource to protect against the confused deputy problem.",
    "Reference": "Section 'Cross-service confused deputy prevention' - URL: https://docs.aws.amazon.com/mgn/latest/ug/cross-service-confused-deputy-prevention.html",
    "Observations": "If the full ARN is not known, use wildcards for the unknown portions."
  }
]
```