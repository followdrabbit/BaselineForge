```json
[
  {
    "Title": "Use aws:SourceArn and aws:SourceAccount in Resource Policies",
    "Description": "Implement resource policies for Amazon RDS that use both the `aws:SourceArn` and `aws:SourceAccount` global condition context keys to restrict permissions granted to other AWS services. This practice prevents cross-service impersonation (confused deputy) problems by ensuring that access is properly scoped to specified accounts and resources.",
    "Applicability": "All Amazon RDS resource policies granting permissions to other AWS services",
    "Security Risk": "Without these conditions, a malicious service or actor could exploit service roles to impersonate other AWS services and gain unintended access to RDS resources.",
    "Default Behavior / Limitations": "AWS does not automatically enforce the use of `aws:SourceArn` and `aws:SourceAccount` in resource policies. This configuration requires manual inclusion in policy documents.",
    "Automation": "Manual validation required, but can be monitored using AWS Config rules to check for conditions in resource policies.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/cross-service-confused-deputy-prevention.html"
    ]
  },
  {
    "Title": "Enforce aws:SourceArn and aws:SourceAccount in Absence of Account ID",
    "Description": "In scenarios where the `aws:SourceArn` does not contain an account ID, both `aws:SourceArn` and `aws:SourceAccount` condition keys must be used to define permissions in resource policies, ensuring permissions are accurately scoped.",
    "Applicability": "All Amazon RDS resource policies without explicit account ID in `aws:SourceArn`",
    "Security Risk": "Inaccurate scope of permissions due to missing account ID could result in unauthorized access if only the `aws:SourceArn` condition is used.",
    "Default Behavior / Limitations": "Manual configuration required to ensure policies include both condition keys.",
    "Automation": "Manual validation required; automated check can be conducted using policy validation tools.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/cross-service-confused-deputy-prevention.html"
    ]
  },
  {
    "Title": "Validate aws:SourceArn as Amazon RDS Resource Type",
    "Description": "Ensure that the `aws:SourceArn` used in resource policies correctly corresponds to an Amazon RDS resource type, maintaining specificity and accuracy in access controls.",
    "Applicability": "Amazon RDS resource policies using `aws:SourceArn` condition key",
    "Security Risk": "Using incorrect ARN types could inadvertently grant access to unintended resources, compromising data security.",
    "Default Behavior / Limitations": "Manual validation required to confirm proper ARN types. AWS does not verify ARN types automatically.",
    "Automation": "Manual validation required; utilize AWS IAM policy simulators or automated policy review tools for policy validation.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/cross-service-confused-deputy-prevention.html"
    ]
  },
  {
    "Title": "Use Wildcards in aws:SourceArn for Partial ARN Information",
    "Description": "When the full ARN of the resource in `aws:SourceArn` is not known, use wildcards (`*`) appropriately to specify unknown portions of the ARN. This allows the policy to remain flexible while still applying controls.",
    "Applicability": "Amazon RDS resource policies with incomplete `aws:SourceArn` information",
    "Security Risk": "Incorrect use of wildcards could overly broaden the scope of permissions, allowing unintended access.",
    "Default Behavior / Limitations": "Wildcards must be configured manually; careful consideration is required to avoid over-privilege.",
    "Automation": "Manual setting required; policy simulation tools can be used to test and validate policy effects.",
    "References": [
      "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/cross-service-confused-deputy-prevention.html"
    ]
  }
]
```