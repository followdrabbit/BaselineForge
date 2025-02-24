```json
[
  {
    "Description": "Configure listener rules with _authenticate-cognito_ or _authenticate-oidc_ action types exclusively on HTTPS listeners for ALB (Application Load Balancer) authentication.",
    "Reference": "Security best practices when using ALB authentication - ALB authentication configuration section - URL: https://aws.amazon.com/blogs/networking-and-content-delivery/security-best-practices-when-using-alb-authentication/",
    "Observations": "Non-TLS HTTP workloads are not supported for authentication."
  },
  {
    "Description": "Set the _OnUnauthenticatedRequest_ option in ALB listener rules to 'authenticate' to ensure users must be authenticated before accessing content.",
    "Reference": "Security best practices when using ALB authentication - ALB authentication configuration section - URL: https://aws.amazon.com/blogs/networking-and-content-delivery/security-best-practices-when-using-alb-authentication/",
    "Observations": "This is suitable for applications requiring user login to access content."
  },
  {
    "Description": "Restrict ALB target security groups to accept traffic only from the ALB's security group.",
    "Reference": "Security best practices when using ALB authentication - Implementing best practices to secure your target application section - URL: https://aws.amazon.com/blogs/networking-and-content-delivery/security-best-practices-when-using-alb-authentication/",
    "Observations": "Prevents unauthorized access and ensures that only the ALB can communicate with targets."
  },
  {
    "Description": "Deploy ALB targets in private subnets without public or Elastic IPs to prevent direct public internet access.",
    "Reference": "Security best practices when using ALB authentication - Implementing best practices to secure your target application section - URL: https://aws.amazon.com/blogs/networking-and-content-delivery/security-best-practices-when-using-alb-authentication/",
    "Observations": "Enhances security by making the ALB the sole access point to targets."
  },
  {
    "Description": "Implement signature validation for JWTs from ALB by verifying the signer field against the ALB's ARN.",
    "Reference": "Security best practices when using ALB authentication - Implementing JWT validation section - URL: https://aws.amazon.com/blogs/networking-and-content-delivery/security-best-practices-when-using-alb-authentication/",
    "Observations": "Ensures JWTs are issued by the correct ALB."
  },
  {
    "Description": "Download and validate the JWT public key from the AWS regional endpoint specified by the key ID in the JWT header.",
    "Reference": "Security best practices when using ALB authentication - JWT validation steps section - URL: https://aws.amazon.com/blogs/networking-and-content-delivery/security-best-practices-when-using-alb-authentication/",
    "Observations": "Validates that the JWT has not been tampered with."
  },
  {
    "Description": "Check JWT payload's expiration to ensure it has not expired before processing the authentication information.",
    "Reference": "Security best practices when using ALB authentication - JWT validation steps section - URL: https://aws.amazon.com/blogs/networking-and-content-delivery/security-best-practices-when-using-alb-authentication/",
    "Observations": "Prevents using outdated JWTs."
  }
]
```
