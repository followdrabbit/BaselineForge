```json
[
  {
    "Title": "Configure ALB with HTTPS Listeners for ALB Authentication",
    "Description": "Configure Application Load Balancer (ALB) listeners to use 'authenticate-cognito' or 'authenticate-oidc' action types exclusively on HTTPS listeners for secure authentication.",
    "Applicability": "All Application Load Balancers with authentication requirements",
    "Security Risk": "Using non-TLS protocols for authentication can lead to exposure of sensitive information, such as credentials, over an insecure connection.",
    "Default Behavior / Limitations": "AWS ALBs do not enforce HTTPS listeners by default; manual configuration is required.",
    "Automation": "Can be monitored using AWS Config rule `elbv2-load-balancer-tls-https-listeners-only` to ensure listeners are HTTPS.",
    "References": [
      "https://aws.amazon.com/blogs/networking-and-content-delivery/security-best-practices-when-using-alb-authentication/"
    ]
  },
  {
    "Title": "Set ALB OnUnauthenticatedRequest to 'Authenticate'",
    "Description": "Ensure ALB listener rules with authentication actions have the `OnUnauthenticatedRequest` setting configured to 'authenticate' to enforce user authentication before granting content access.",
    "Applicability": "All ALB configurations requiring user login for access control",
    "Security Risk": "Allowing access without authentication risks unauthorized access to sensitive or private content.",
    "Default Behavior / Limitations": "This setting must be explicitly configured for listener rules.",
    "Automation": "Manual validation required for listener rule configurations as this setting is specific to ALB usage scenarios.",
    "References": [
      "https://aws.amazon.com/blogs/networking-and-content-delivery/security-best-practices-when-using-alb-authentication/"
    ]
  },
  {
    "Title": "Restrict ALB Target Security Groups",
    "Description": "Configure security groups for ALB targets to only accept traffic from the ALB's security group, ensuring controlled access solely through the ALB.",
    "Applicability": "All AWS environments using ALB with private backend resources",
    "Security Risk": "Open target access can expose applications to unauthorized traffic and potential attacks.",
    "Default Behavior / Limitations": "Security groups allow broad configuration; manual restrictions are necessary.",
    "Automation": "Can be verified using AWS Config custom rules or Security Hub to ensure compliance.",
    "References": [
      "https://aws.amazon.com/blogs/networking-and-content-delivery/security-best-practices-when-using-alb-authentication/"
    ]
  },
  {
    "Title": "Deploy ALB Targets in Private Subnets",
    "Description": "Deploy Application Load Balancer targets within private subnets without public IPs to prevent direct public internet access.",
    "Applicability": "All AWS accounts using ALB with targets needing restricted internet exposure",
    "Security Risk": "Public accessibility increases the risk of direct attacks on application resources.",
    "Default Behavior / Limitations": "AWS VPC default configuration allows for public subnet deployments; private subnet adjustments are necessary.",
    "Automation": "Can be monitored using AWS Config to ensure that subnets do not have public IP capabilities.",
    "References": [
      "https://aws.amazon.com/blogs/networking-and-content-delivery/security-best-practices-when-using-alb-authentication/"
    ]
  },
  {
    "Title": "Implement Signature Validation for JWTs from ALB",
    "Description": "Verify that JSON Web Tokens (JWTs) signed by Application Load Balancers match the ALB's ARN to ensure they are correctly issued.",
    "Applicability": "Applications using JWTs for authentication with ALB",
    "Security Risk": "Incorrectly verified JWTs can result in unauthorized access if tokens from other sources are accepted.",
    "Default Behavior / Limitations": "Manual verification code must be implemented in application logic.",
    "Automation": "Manual validation required; application code must handle JWT signature checks.",
    "References": [
      "https://aws.amazon.com/blogs/networking-and-content-delivery/security-best-practices-when-using-alb-authentication/"
    ]
  },
  {
    "Title": "Download and Validate JWT Public Key Using AWS Key ID",
    "Description": "Download and verify the JWT's public key from AWS's regional endpoints using the key ID present in the JWT header to ensure token integrity.",
    "Applicability": "All applications relying on JWT validation for secure authentication",
    "Security Risk": "Failure to accurately validate JWTs can allow token forgery and unauthorized access.",
    "Default Behavior / Limitations": "Manual coding is required for downloading and validating the public key.",
    "Automation": "Manual validation required as application logic must include public key download and verification.",
    "References": [
      "https://aws.amazon.com/blogs/networking-and-content-delivery/security-best-practices-when-using-alb-authentication/"
    ]
  },
  {
    "Title": "Verify JWT Expiration Before Use",
    "Description": "Check the expiration field in JWT payloads to ensure tokens are not used after their expiry, preventing outdated authentication.",
    "Applicability": "Applications using JWTs for session management or access control",
    "Security Risk": "Using expired JWTs can compromise security by allowing unauthorized access based on outdated validation.",
    "Default Behavior / Limitations": "Expiration checks must be implemented at the application level.",
    "Automation": "Manual validation required; application must handle expiration checks for JWTs.",
    "References": [
      "https://aws.amazon.com/blogs/networking-and-content-delivery/security-best-practices-when-using-alb-authentication/"
    ]
  }
]
```