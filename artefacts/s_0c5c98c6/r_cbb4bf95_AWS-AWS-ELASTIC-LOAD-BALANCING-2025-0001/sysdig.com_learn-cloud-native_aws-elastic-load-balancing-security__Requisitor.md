```json
[
  {
    "Description": "Configure ELB listeners to support and require encrypted communication using TLS or HTTPS.",
    "Reference": "Best Practices for ELB Security - https://sysdig.com/learn-cloud-native/aws-elastic-load-balancing-security/",
    "Observations": "Ensure to enforce encryption to secure data in transit between clients and the load balancer."
  },
  {
    "Description": "Apply security groups to limit inbound traffic to ELBs and further restrict access to the target groups.",
    "Reference": "Using Security Groups to Secure Your ELB and Applications - https://sysdig.com/learn-cloud-native/aws-elastic-load-balancing-security/",
    "Observations": "Security groups should be configured to restrict access to known IP ranges and necessary ports only."
  },
  {
    "Description": "Ensure that the target groups of your ELB restrict incoming requests to those originating from the ELB.",
    "Reference": "Using Security Groups to Secure Your ELB and Applications - https://sysdig.com/learn-cloud-native/aws-elastic-load-balancing-security/",
    "Observations": "This helps guarantee that all requests are processed through the load balancer, enhancing security."
  },
  {
    "Description": "Leverage Web Application Firewall (AWS WAF) to restrict incoming requests based on IP, geolocation, and other criteria.",
    "Reference": "Best Practices for ELB Security - https://sysdig.com/learn-cloud-native/aws-elastic-load-balancing-security/",
    "Observations": "AWS WAF can be used to create additional security rules to protect the ELB from specific types of internet threats."
  },
  {
    "Description": "Enable authentication on ALB listeners using an OpenID Connect (OIDC) Identity Provider, like Amazon Cognito, to offload application-level authentication.",
    "Reference": "Application Load Balancers (ALB) - https://sysdig.com/learn-cloud-native/aws-elastic-load-balancing-security/",
    "Observations": "This ALB feature supports OpenID Connect to improve user authentication at the load balancer level."
  },
  {
    "Description": "Utilize the principle of least privilege by managing IAM access controls effectively and enforcing MFA on all accounts.",
    "Reference": "Best Practices for ELB Security - https://sysdig.com/learn-cloud-native/aws-elastic-load-balancing-security/",
    "Observations": "Tightly manage account access to prevent unauthorized actions within AWS accounts."
  },
  {
    "Description": "For internal ELBs within a VPC, avoid configuring public IP addresses unless necessary for external access.",
    "Reference": "Best Practices for ELB Security - https://sysdig.com/learn-cloud-native/aws-elastic-load-balancing-security/",
    "Observations": "Reduce the exposed attack surface by restricting public access to ELBs."
  }
]
```