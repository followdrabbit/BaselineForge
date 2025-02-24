```json
[
  {
    "Title": "Configure Desync Mitigation Mode for Application Load Balancers",
    "Description": "Ensure that Application Load Balancers are configured with the appropriate desync mitigation mode to protect against HTTP desync attacks. This can be set using the AWS Management Console or AWS CLI.",
    "Applicability": "All Application Load Balancers",
    "Security Risk": "Without proper desync mitigation, ALBs may be vulnerable to HTTP desync attacks, which can compromise data security.",
    "Default Behavior / Limitations": "AWS does not apply desync mitigation mode by default. This needs to be configured manually.",
    "Automation": "Can be audited using AWS Config with custom rules or AWS Security Hub insights.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/configure-desync-mitigation-mode.html"
    ]
  },
  {
    "Title": "Enable Multi-AZ Configurations for Gateway Load Balancers",
    "Description": "Ensure Gateway Load Balancers are deployed in multiple Availability Zones to enhance fault tolerance.",
    "Applicability": "All Gateway Load Balancers",
    "Security Risk": "Single-AZ deployments increase the risk of service disruption in the event of AZ failure.",
    "Default Behavior / Limitations": "Multi-AZ is not enabled by default. Users must configure it when creating or updating a load balancer.",
    "Automation": "Can be enforced and monitored using AWS Config or AWS CloudFormation templates.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/enable-multi-az.html"
    ]
  },
  {
    "Title": "Enable Drop Invalid Header Fields for Application Load Balancers",
    "Description": "Configure Application Load Balancers to drop any requests with invalid header fields to maintain the integrity of request data.",
    "Applicability": "All Application Load Balancers",
    "Security Risk": "Invalid headers can be exploited for poor data integrity and could lead to security vulnerabilities.",
    "Default Behavior / Limitations": "Dropping invalid headers is not enabled by default. It must be configured via AWS Management Console or CLI.",
    "Automation": "Configuration can be monitored using AWS Config.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/drop-invalid-header-fields-enabled.html"
    ]
  },
  {
    "Title": "Use Secure Protocols for ELBv2 ALBs",
    "Description": "Ensure that Application Load Balancer listeners use secure protocols like TLS to guarantee encrypted data transfer.",
    "Applicability": "All Application Load Balancers",
    "Security Risk": "Insecure protocols increase the risk of data being exposed or intercepted during transmission.",
    "Default Behavior / Limitations": "Listeners need to be configured for secure protocols; this is not guaranteed by default.",
    "Automation": "Can be enforced using AWS Config rule `alb-tls-listeners-only`.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/listener-security.html"
    ]
  },
  {
    "Title": "Secure and Valid Security Groups for ELBv2 Load Balancers",
    "Description": "Ensure ELBv2 ALBs have security groups that restrict access to necessary IPs and ports only.",
    "Applicability": "All ELBv2 Load Balancers",
    "Security Risk": "Inadequate security group settings can allow unauthorized access to the load balancer and associated resources.",
    "Default Behavior / Limitations": "Users must manually configure security groups.",
    "Automation": "Security groups can be monitored and audited with AWS Config and Security Hub.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/security-group.html"
    ]
  },
  {
    "Title": "Adopt Latest Security Policies for SSL/TLS on ALBs",
    "Description": "Ensure that Amazon ALBs use the latest predefined security policy for SSL/TLS negotiations to protect against vulnerabilities.",
    "Applicability": "All Application Load Balancers using SSL/TLS",
    "Security Risk": "Outdated security policies may leave communications vulnerable to interception.",
    "Default Behavior / Limitations": "Continuous monitoring and updates are required as new policies are released.",
    "Automation": "Can be tracked using AWS Config with custom rules.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/security-policy.html"
    ]
  },
  {
    "Title": "Enable Access Logging for Amazon ALBs",
    "Description": "Access logging must be enabled on Amazon ALBs to ensure HTTP/S requests and responses are correctly logged for auditing purposes.",
    "Applicability": "All Application Load Balancers",
    "Security Risk": "Without access logging, it is difficult to monitor access patterns and troubleshoot issues.",
    "Default Behavior / Limitations": "Access logging is disabled by default. Needs manual enabling.",
    "Automation": "Can be enforced using AWS Config rules and monitored through AWS CloudWatch.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/access-log.html"
    ]
  },
  {
    "Title": "Enable Deletion Protection for ELBv2 Load Balancers",
    "Description": "Ensure that Deletion Protection is enabled to prevent unauthorized or accidental deletions of ELBv2 load balancers.",
    "Applicability": "All ELBv2 Load Balancers",
    "Security Risk": "Without deletion protection, there is a risk of accidental or malicious removal of critical resources.",
    "Default Behavior / Limitations": "Deletion protection must be manually enabled during or after creation.",
    "Automation": "Can be enforced and monitored through AWS Config.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/deletion-protection.html"
    ]
  },
  {
    "Title": "Maintain Minimum Number of Healthy Targets in ELBv2 Load Balancers",
    "Description": "Ensure that each ELBv2 Load Balancer has at least two healthy target instances to guarantee redundancy and availability.",
    "Applicability": "All ELBv2 Load Balancers",
    "Security Risk": "Insufficient healthy targets can lead to service degradation or outages.",
    "Default Behavior / Limitations": "The configuration of target instances is user-managed and must be monitored.",
    "Automation": "Can be monitored using AWS CloudWatch for health checks.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/minimum-number-of-ec2-instances.html"
    ]
  },
  {
    "Title": "Enforce Secure Protocols for Network Load Balancer Listeners",
    "Description": "Ensure that listeners on AWS Network Load Balancers use secure protocols, such as TLS, for all data communications.",
    "Applicability": "All Network Load Balancers",
    "Security Risk": "Without secure protocols, data could be transmitted unencrypted and be intercepted.",
    "Default Behavior / Limitations": "The listener protocol must be explicitly configured by the user.",
    "Automation": "Can be checked using AWS Config rules.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/network-load-balancer-listener-security.html"
    ]
  },
  {
    "Title": "Protect Application Load Balancers with Amazon WAF",
    "Description": "Deploy Amazon WAF in front of Application Load Balancers to shield against common web application vulnerabilities.",
    "Applicability": "All Application Load Balancers exposed to the internet",
    "Security Risk": "Without a Web Application Firewall, ALBs are prone to common web exploits such as SQL injection and XSS.",
    "Default Behavior / Limitations": "Amazon WAF must be configured and managed by the user.",
    "Automation": "Can be configured using AWS WAF rules and integrated through AWS Firewall Manager.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/alb-integrated-with-waf.html"
    ]
  },
  {
    "Title": "Enable Cross-Zone Load Balancing for Gateway Load Balancers",
    "Description": "Ensure cross-zone load balancing is activated to enhance fault tolerance and load distribution for Gateway Load Balancers.",
    "Applicability": "All Gateway Load Balancers",
    "Security Risk": "Without cross-zone load balancing, imbalanced traffic distribution may occur, leading to possible overloads.",
    "Default Behavior / Limitations": "Cross-zone balancing is not enabled by default and requires manual configuration.",
    "Automation": "Configurations can be managed via AWS CLI or CloudFormation.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/enable-cross-zone-load-balancing.html"
    ]
  },
  {
    "Title": "Enable Deletion Protection for Amazon Gateway Load Balancers",
    "Description": "Activate Deletion Protection on Gateway Load Balancers to avert unauthorized deletion.",
    "Applicability": "All Gateway Load Balancers",
    "Security Risk": "The absence of deletion protection increases the risk of accidental deletion.",
    "Default Behavior / Limitations": "Deletion protection needs to be manually activated.",
    "Automation": "Can be configured and monitored using AWS Config policies.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/enable-gwlb-deletion-protection.html"
    ]
  },
  {
    "Title": "Redirect HTTP Traffic to HTTPS on Application Load Balancers",
    "Description": "Ensure Application Load Balancers have a rule to redirect all HTTP traffic to HTTPS to maintain secure user sessions.",
    "Applicability": "All Application Load Balancers serving HTTP traffic",
    "Security Risk": "Without HTTPS redirection, user sessions may be vulnerable to session hijacking.",
    "Default Behavior / Limitations": "HTTP to HTTPS redirection needs to be explicitly configured.",
    "Automation": "AWS Config can be used to validate the presence of an HTTPS redirect rule.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/http-to-https-redirect.html"
    ]
  },
  {
    "Title": "Enable Least Outstanding Requests (LOR) Algorithm for ALBs",
    "Description": "Ensure that ALBs use the Least Outstanding Requests (LOR) algorithm for efficient load distribution.",
    "Applicability": "All Application Load Balancers",
    "Security Risk": "Without appropriate load balancing algorithms, load distribution may become inefficient, leading to poor performance.",
    "Default Behavior / Limitations": "LOR must be selected when configuring the ALB.",
    "Automation": "AWS CloudFormation templates can be used to enforce LOR.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/enable-alb-least-outstanding-requests.html"
    ]
  },
  {
    "Title": "Enable HTTP/2 Support on Application Load Balancers",
    "Description": "Enable HTTP/2 support to improve performance and resource utilization for Application Load Balancers.",
    "Applicability": "All Application Load Balancers",
    "Security Risk": "Without HTTP/2, you may experience slower communication speeds and reduced efficiency.",
    "Default Behavior / Limitations": "HTTP/2 support needs to be activated during configuration.",
    "Automation": "Monitored through AWS Config for correct configuration.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/enable-http2-support.html"
    ]
  },
  {
    "Title": "Enable gRPC Protocol Support for Application Load Balancers",
    "Description": "Ensure that gRPC protocol support is enabled for ALBs where applicable to benefit from improved communication efficiency in modern applications.",
    "Applicability": "All Application Load Balancers using gRPC",
    "Security Risk": "Without gRPC support, applications may face interoperability and performance issues.",
    "Default Behavior / Limitations": "gRPC must be configured explicitly by the user.",
    "Automation": "Can be verified and managed using AWS Config.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/enable-grpc-support.html"
    ]
  },
  {
    "Title": "Implement TLS ALPN Policies on Network Load Balancers",
    "Description": "Ensure Network Load Balancers use TLS ALPN policies to better negotiate application-layer protocols.",
    "Applicability": "All Network Load Balancers",
    "Security Risk": "Without ALPN policies, there may be inefficiencies in protocol negotiation.",
    "Default Behavior / Limitations": "ALPN policies must be configured by the user.",
    "Automation": "Configuration changes can be tracked using AWS Config.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/enable-tlsalpn-policy.html"
    ]
  },
  {
    "Title": "Regular Review of Amazon Internet-Facing ELBv2 Load Balancers",
    "Description": "Ensure regular reviews and audits of internet-facing ELBv2 load balancers to identify and mitigate security vulnerabilities.",
    "Applicability": "All Internet-Facing ELBv2 Load Balancers",
    "Security Risk": "Lack of regular reviews can lead to undetected vulnerabilities and misconfigurations.",
    "Default Behavior / Limitations": "Manual process requiring periodic reviews.",
    "Automation": "Manual validation required; however, AWS Config and Security Hub can assist in identifying some misconfigurations.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/internet-facing-load-balancers.html"
    ]
  },
  {
    "Title": "Utilize Latest Security Policies for NLB TLS Negotiation",
    "Description": "Ensure Network Load Balancers are using the latest AWS recommended security policies for TLS negotiation to mitigate potential vulnerabilities.",
    "Applicability": "All Network Load Balancers",
    "Security Risk": "Outdated security policies can expose the service to known vulnerabilities.",
    "Default Behavior / Limitations": "Security policies must be updated actively by the user.",
    "Automation": "Compliance can be tracked with AWS Config.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/network-load-balancer-security-policy.html"
    ]
  },
  {
    "Title": "Identify and Remove Unused ELBv2 Load Balancers",
    "Description": "Regularly identify unused ELBv2 load balancers and delete them to optimize costs and reduce the attack surface.",
    "Applicability": "All ELBv2 Load Balancers",
    "Security Risk": "Unused resources add to costs and can be a target for unauthorized actions if not monitored.",
    "Default Behavior / Limitations": "Regular audits required; no automation for unused resource detection by default.",
    "Automation": "AWS Cost Explorer and manual reviews; some functionality may be supported via AWS Config.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/unused-load-balancers.html"
    ]
  }
]
```