```json
[
  {
    "Title": "Enforce TLS/HTTPS for ELB Listeners",
    "Description": "Configure Elastic Load Balancing (ELB) listeners to only support and require TLS or HTTPS protocols to ensure encrypted data transmission between clients and the load balancer.",
    "Applicability": "All AWS accounts using ELB",
    "Security Risk": "Without encrypted communication, data is susceptible to interception and unauthorized access, compromising confidentiality.",
    "Default Behavior / Limitations": "ELB listeners require manual configuration to enforce TLS/HTTPS.",
    "Automation": "Can be enforced using AWS Config rule `elasticloadbalancer-tls-protocols-restricted`.",
    "References": [
      "https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/create-tls-listener.html"
    ]
  },
  {
    "Title": "Apply Restrictive Security Groups to ELBs",
    "Description": "Configure security groups for Elastic Load Balancers (ELBs) to restrict inbound traffic to necessary IP ranges and ports, limiting exposure to unauthorized access.",
    "Applicability": "All AWS accounts utilizing ELBs",
    "Security Risk": "Open inbound traffic increases the risk of unauthorized access and potential exposure to attacks.",
    "Default Behavior / Limitations": "Security groups need manual setup to implement restrictions.",
    "Automation": "Can be monitored and partially enforced using AWS Config rules related to security group rules.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html"
    ]
  },
  {
    "Title": "Restrict Incoming Requests to Target Groups via ELB",
    "Description": "Ensure that target groups for your ELB only accept incoming requests from the ELB's IP address, using security group rules to enforce this restriction.",
    "Applicability": "All AWS accounts using ELB with target groups",
    "Security Risk": "Allowing requests from arbitrary sources can bypass load balancer security, increasing the risk of unauthorized access.",
    "Default Behavior / Limitations": "Requires manual configuration of security group rules.",
    "Automation": "Manual validation required. No direct AWS Config rule; implement via security group best practices.",
    "References": [
      "https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html"
    ]
  },
  {
    "Title": "Implement AWS WAF for Enhanced ELB Security",
    "Description": "Leverage AWS Web Application Firewall (WAF) to apply custom rules for IP, geolocation, and specific threat mitigation, enhancing overall security for the ELB.",
    "Applicability": "All AWS accounts using ELB",
    "Security Risk": "Without WAF, ELBs are more vulnerable to web-based attacks and other malicious activities.",
    "Default Behavior / Limitations": "AWS WAF must be configured manually for each application.",
    "Automation": "Can be configured via AWS WAF APIs and CloudFormation for rule automation.",
    "References": [
      "https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html"
    ]
  },
  {
    "Title": "Enable OIDC-based Authentication on ALB Listeners",
    "Description": "Configure Application Load Balancer (ALB) listeners to offload authentication to an OpenID Connect (OIDC) Identity Provider, such as Amazon Cognito, providing application-level user authentication.",
    "Applicability": "AWS accounts using ALB where user authentication is required",
    "Security Risk": "Lack of authentication could allow unauthenticated users to access application resources, leading to data breaches.",
    "Default Behavior / Limitations": "OIDC needs to be configured explicitly on ALB.",
    "Automation": "Can be automated using AWS CloudFormation for ALB listener rules.",
    "References": [
      "https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-authenticate-users.html"
    ]
  },
  {
    "Title": "Implement IAM Least Privilege and Enforce MFA",
    "Description": "Manage Identity and Access Management (IAM) access controls to ensure compliance with the principle of least privilege and enforce Multi-Factor Authentication (MFA) on all accounts.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Improper access controls could lead to unauthorized actions within AWS accounts, increasing risk exposure.",
    "Default Behavior / Limitations": "IAM access and MFA policies require manual setup.",
    "Automation": "Can be enforced using IAM policies and AWS Config rules like `iam-user-mfa-enabled`.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"
    ]
  },
  {
    "Title": "Restrict Public IP on Internal ELBs within a VPC",
    "Description": "Ensure internal Elastic Load Balancers (ELBs) within a Virtual Private Cloud (VPC) do not use public IP addresses unless necessary, to minimize exposure to external threats.",
    "Applicability": "All AWS accounts using internal ELBs",
    "Security Risk": "Assigning public IPs to internal ELBs unnecessarily increases the attack surface of internal resources.",
    "Default Behavior / Limitations": "VPC configurations allow for both public and private IP assignments.",
    "Automation": "Manual validation required; ensure network configurations and subnet settings adhere to this guideline.",
    "References": [
      "https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction-to-elb.html"
    ]
  }
]
```