```json
[
  {
    "Description": "Create a VPC endpoint with an attached endpoint policy in JSON format that uses IAM policy language. The policy must include a Principal element.",
    "Reference": "Section: ConsideraÃ§Ãµes - VPC Endpoints Access Documentation - URL: https://docs.aws.amazon.com/pt_br/vpc/latest/privatelink/vpc-endpoints-access.html",
    "Observations": "The policy must not exceed 20,480 characters, including whitespace."
  },
  {
    "Description": "Ensure that default endpoint policy grants full access to the endpoint.",
    "Reference": "Section: PolÃ­tica de endpoint padrÃ£o - VPC Endpoints Access Documentation - URL: https://docs.aws.amazon.com/pt_br/vpc/latest/privatelink/vpc-endpoints-access.html",
    "Observations": "Default policies apply when no custom policies are attached."
  },
  {
    "Description": "When creating a VPC endpoint for a non-AWS service, allow full access to the endpoint by default.",
    "Reference": "Section: ConsideraÃ§Ãµes - VPC Endpoints Access Documentation - URL: https://docs.aws.amazon.com/pt_br/vpc/latest/privatelink/vpc-endpoints-access.html",
    "Observations": "Custom policies should be added if restrictions are needed on the service."
  },
  {
    "Description": "Do not use wildcard (*) or numeric condition operators with global context keys referencing system-generated identifiers.",
    "Reference": "Section: ConsideraÃ§Ãµes - VPC Endpoints Access Documentation - URL: https://docs.aws.amazon.com/pt_br/vpc/latest/privatelink/vpc-endpoints-access.html",
    "Observations": "Ensure compliance with this restriction in JSON policies."
  },
  {
    "Description": "When using a string condition operator, include at least six consecutive characters before or after each wildcard character.",
    "Reference": "Section: ConsideraÃ§Ãµes - VPC Endpoints Access Documentation - URL: https://docs.aws.amazon.com/pt_br/vpc/latest/privatelink/vpc-endpoints-access.html",
    "Observations": "Review policies to ensure they meet this criterion for string conditions."
  },
  {
    "Description": "In endpoints of gateway, set Principal to * and use aws:PrincipalArn key for specific principals.",
    "Reference": "Section: Entidades principais de endpoints de gateway - VPC Endpoints Access Documentation - URL: https://docs.aws.amazon.com/pt_br/vpc/latest/privatelink/vpc-endpoints-access.html",
    "Observations": "This limits the access granted to specific users."
  },
  {
    "Description": "Use modify-vpc-endpoint to update endpoint policies from AWS CLI.",
    "Reference": "Section: Atualizar uma polÃ­tica VPC de endpoint - VPC Endpoints Access Documentation - URL: https://docs.aws.amazon.com/pt_br/vpc/latest/privatelink/vpc-endpoints-access.html",
    "Observations": "Changes to policies may take some minutes to apply."
  },
  {
    "Description": "In gateway endpoints, specifying the main entity as account_id grants access only to the root user of the AWS account.",
    "Reference": "Section: Entidades principais de endpoints de gateway - VPC Endpoints Access Documentation - URL: https://docs.aws.amazon.com/pt_br/vpc/latest/privatelink/vpc-endpoints-access.html",
    "Observations": "Ensure this configuration if restricting access to the root account is desired."
  }
]
```