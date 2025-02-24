```json
[
  {
    "Title": "Block Public Access to S3 Buckets",
    "Description": "Configure all S3 buckets to block public access at the bucket level to prevent unauthorized data exposure. Ensure AWS Config rules are in place to enforce and monitor this setting.",
    "Applicability": "All Amazon S3 buckets",
    "Security Risk": "Public buckets can lead to data leaks.",
    "Default Behavior / Limitations": "AWS S3 does not block public access by default.",
    "Automation": "Enforce and monitor using AWS Config rules such as `s3-bucket-public-read-prohibited`.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html"
    ]
  },
  {
    "Title": "Enable MFA-Delete on S3 Buckets",
    "Description": "Require Multi-Factor Authentication (MFA) for any delete operation on S3 buckets holding critical data to prevent accidental or malicious deletion.",
    "Applicability": "All S3 buckets with deletion capabilities for critical data",
    "Security Risk": "Without MFA-Delete, unauthorized users could permanently delete critical data.",
    "Default Behavior / Limitations": "MFA-Delete is not enabled by default and requires manual configuration for each bucket.",
    "Automation": "Manual verification required; currently not enforceable through AWS Config or IAM.",
    "References": [
      "https://docs.aws.amazon.com/AmazonS3/latest/userguide/MFADelete.html"
    ]
  },
  {
    "Title": "Configure ELB Listeners to Use Secure Protocols",
    "Description": "Ensure that Elastic Load Balancer (ELB) listeners, including both Application and Network Load Balancers, use TLS or HTTPS protocols for secure data transmission. Configure AWS Config rules to monitor compliance.",
    "Applicability": "All Elastic Load Balancers",
    "Security Risk": "Insecure protocols can lead to data breaches through interception.",
    "Default Behavior / Limitations": "Secure protocols must be manually configured; not enforced by default.",
    "Automation": "AWS Config rules like `elasticloadbalancer-tls-protocols-restricted` can enforce secure protocols.",
    "References": [
      "https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/create-tls-listener.html"
    ]
  },
  {
    "Title": "Enable Access Logging for Load Balancers",
    "Description": "Activate access logging on all Elastic Load Balancers (ALBs and NLBs) to ensure requests are logged for audit and troubleshooting.",
    "Applicability": "All Elastic Load Balancers",
    "Security Risk": "Without logging, it's difficult to track access patterns and identify anomalous activities.",
    "Default Behavior / Limitations": "Logging is disabled by default and needs to be enabled manually.",
    "Automation": "Can be enforced with AWS Config rules and monitored through AWS CloudWatch Logs.",
    "References": [
      "https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html"
    ]
  },
  {
    "Title": "Implement AWS WAF on Internet-Facing ELBs",
    "Description": "Deploy AWS Web Application Firewall (WAF) in front of Application Load Balancers to mitigate common web threats like SQL injection and XSS.",
    "Applicability": "All Internet-facing ELBs",
    "Security Risk": "Without WAF, ALBs are more vulnerable to common web attacks.",
    "Default Behavior / Limitations": "AWS WAF requires manual configuration.",
    "Automation": "Automate using AWS WAF policies and integrate through AWS Firewall Manager.",
    "References": [
      "https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html"
    ]
  },
  {
    "Title": "Restrict Security Groups for ELBs",
    "Description": "Configure security groups for Elastic Load Balancers to only allow necessary IPs and ports, limiting exposure to unauthorized access.",
    "Applicability": "All ELBs",
    "Security Risk": "Inadequately restricted security groups can lead to unauthorized access.",
    "Default Behavior / Limitations": "Security groups must be manually configured.",
    "Automation": "AWS Config can monitor compliance with security group configurations.",
    "References": [
      "https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html"
    ]
  },
  {
    "Title": "Use Latest Security Policies for SSL/TLS on Load Balancers",
    "Description": "Ensure that all Elastic Load Balancers are configured to use the latest predefined security policies for SSL/TLS negotiations to protect against vulnerabilities.",
    "Applicability": "All ELBs using SSL/TLS",
    "Security Risk": "Outdated security policies can expose communications to interception.",
    "Default Behavior / Limitations": "Security policies must be updated manually.",
    "Automation": "Monitor using AWS Config and Security Hub for alerts on outdated policies.",
    "References": [
      "https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html"
    ]
  },
  {
    "Title": "Enforce ALB Listener Authentication with OIDC",
    "Description": "Configure ALB listeners to leverage OpenID Connect (OIDC) for offloading authentication, thereby strengthening application-level user authentication.",
    "Applicability": "ALBs where user authentication is required",
    "Security Risk": "Insufficient authentication may lead to unauthorized access to resources.",
    "Default Behavior / Limitations": "OIDC authentication needs explicit configuration.",
    "Automation": "Configure using AWS CloudFormation for automated rule setup.",
    "References": [
      "https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-authenticate-users.html"
    ]
  },
  {
    "Title": "Ensure Deletion Protection on ELBv2",
    "Description": "Enable Deletion Protection for ELBv2 Load Balancers to prevent accidental or unauthorized deletions.",
    "Applicability": "All ELBv2 Load Balancers",
    "Security Risk": "Without Deletion Protection, critical resources are at risk of accidental destruction.",
    "Default Behavior / Limitations": "Deletion Protection is not enabled by default.",
    "Automation": "AWS Config can enforce this setting.",
    "References": [
      "https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html"
    ]
  },
  {
    "Title": "Use HTTP/2 for Improved Performance on ALBs",
    "Description": "Enable HTTP/2 support on Application Load Balancers for better performance and resource utilization.",
    "Applicability": "All Application Load Balancers",
    "Security Risk": "HTTP/1.x may result in slower interaction due to lack of multiplexing.",
    "Default Behavior / Limitations": "HTTP/2 must be explicitly enabled.",
    "Automation": "Monitor through AWS Config to ensure support is enabled.",
    "References": [
      "https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html"
    ]
  }
]
```