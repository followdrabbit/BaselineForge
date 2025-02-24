```json
[
  {
    "Title": "Enforce Use of aws:SourceArn and aws:SourceAccount in Resource Policies for AWS Application Migration Service",
    "Description": "Ensure that resource policies for AWS Application Migration Service include both `aws:SourceArn` and `aws:SourceAccount` global condition context keys. These keys should be used to limit permissions and prevent cross-service confused deputy problems by verifying that the `aws:SourceAccount` matches the account ID specified in the `aws:SourceArn`.",
    "Applicability": "AWS Application Migration Service resource policies",
    "Security Risk": "Without proper constraints using `aws:SourceArn` and `aws:SourceAccount`, services may become vulnerable to the confused deputy problem, leading to potential unauthorized access and privilege escalation by malicious actors.",
    "Default Behavior / Limitations": "AWS does not enforce the use of `aws:SourceArn` and `aws:SourceAccount` by default in resource policies.",
    "Automation": "Can be audited using AWS Config rule `custom-resource-policies-audit` to ensure that policies include these conditions.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/cross-service-confused-deputy-prevention.html"
    ]
  },
  {
    "Title": "Restrict aws:SourceArn for AWS Application Migration Service to Specific ARN Structure",
    "Description": "For policies related to AWS Application Migration Service, set the `aws:SourceArn` value to 'arn:aws:mgn:*:123456789012:source-server/*'. This ensures that policies have a specified and expected structure to limit the conditions in place.",
    "Applicability": "AWS Application Migration Service policies",
    "Security Risk": "Incorrect ARN patterns may bypass policy conditions, allowing potential misuse of cross-service permissions and leading to unauthorized access.",
    "Default Behavior / Limitations": "The service does not mandate this specific ARN pattern by default; it needs manual configuration.",
    "Automation": "Can be enforced through custom AWS Config rules that check for the specific ARN pattern in policy conditions.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/cross-service-confused-deputy-prevention.html"
    ]
  },
  {
    "Title": "Implement Full ARN in aws:SourceArn for Confused Deputy Protection",
    "Description": "Configure policies to use `aws:SourceArn` with the complete ARN of the resource when protecting against the confused deputy problem. If the full ARN is unknown, consider using wildcards judiciously for unknown segments.",
    "Applicability": "All AWS services using resource policies susceptible to confused deputy problems",
    "Security Risk": "Incomplete ARN specifications can leave room for exploitation, allowing unauthorized services to access resources by exploiting policy loopholes.",
    "Default Behavior / Limitations": "AWS does not automatically verify ARN completeness in `aws:SourceArn`, requiring manual validation.",
    "Automation": "Audit using AWS Config custom rules designed to enforce the presence of a full ARN in resource policies.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/cross-service-confused-deputy-prevention.html"
    ]
  }
]
```