### ControlGen Output - Arquivo 1
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

### ControlGen Output - Arquivo 2
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

### ControlGen Output - Arquivo 3
```json
[
  {
    "Title": "Enforce HTTPS/SSL Protocol Use for App-Tier ELB Listeners",
    "Description": "Configure the Elastic Load Balancer (ELB) listener in the application tier to use HTTPS/SSL protocol to ensure secure data transmission. Update the ELB listener to utilize secure protocols only.",
    "Applicability": "All Application Tier ELBs",
    "Security Risk": "Using insecure protocols can lead to data breaches through man-in-the-middle attacks or eavesdropping.",
    "Default Behavior / Limitations": "ELB supports various protocols by default. HTTPS/SSL needs to be configured explicitly.",
    "Automation": "Can be enforced using AWS Config custom rule to ensure only HTTPS/SSL listeners are active.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/app-tier-elb-https-listener.html"
    ]
  },
  {
    "Title": "Enforce Use of Latest Security Policies for App-Tier ELBs",
    "Description": "Configure app-tier Elastic Load Balancers to use the latest predefined security policies. Regularly review and update ELB security policies to the latest versions provided by AWS.",
    "Applicability": "All Application Tier ELBs",
    "Security Risk": "Outdated security policies expose systems to vulnerabilities that have been addressed in newer policies.",
    "Default Behavior / Limitations": "Security policies are not automatically updated.",
    "Automation": "Use AWS Config and Security Hub to detect outdated security policies and alert for manual updates.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/app-tier-elb-latest-ssl-security-policies.html"
    ]
  },
  {
    "Title": "Configure Application Layer Health Checks for App-Tier ELBs",
    "Description": "Ensure application layer health check is configured on app-tier ELBs for effective monitoring of backend instance health. Update ELB health checks to include application endpoints.",
    "Applicability": "All Application Tier ELBs",
    "Security Risk": "Without application-level health checks, ELBs may route traffic to unhealthy instances, affecting application availability.",
    "Default Behavior / Limitations": "Health checks need to be manually configured per listener.",
    "Automation": "Manual configuration required; monitoring can be done using CloudWatch to alert on unhealthy instances.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/app-tier-elb-health-check.html"
    ]
  },
  {
    "Title": "Use Application Load Balancer for HTTP/HTTPS Traffic",
    "Description": "Replace Classic Load Balancers with Application Load Balancers (ALB) for web applications handling HTTP/HTTPS traffic to take advantage of advanced traffic management features.",
    "Applicability": "All environments using Classic Load Balancers for HTTP/HTTPS",
    "Security Risk": "Classic Load Balancers lack modern features and security enhancements compared to ALBs.",
    "Default Behavior / Limitations": "Classic Load Balancers do not support ALB-specific features.",
    "Automation": "AWS Config can be used to detect Classic Load Balancers running HTTP/HTTPS and notify for manual upgrade to ALBs.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-classic.html"
    ]
  },
  {
    "Title": "Configure Desync Mitigation Mode for Classic Load Balancers",
    "Description": "Ensure the suitable Desync Mitigation mode is enabled for Classic Load Balancers to protect against HTTP desynchronization threats. Configure through the AWS Management Console or using AWS CLI.",
    "Applicability": "Classic Load Balancers with HTTP/HTTPS listeners",
    "Security Risk": "Desync attacks can lead to applications handling malicious requests that could affect application integrity.",
    "Default Behavior / Limitations": "Classic Load Balancers do not have desync mitigation enabled by default.",
    "Automation": "AWS Config custom rules can be developed to check Desync Mitigation Mode settings.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/enable-configure-desync-mitigation-mode.html"
    ]
  },
  {
    "Title": "Enable ELB Access Logging",
    "Description": "Enable access logging on Elastic Load Balancers to record all requests sent to the load balancer for monitoring and troubleshooting purposes.",
    "Applicability": "All Elastic Load Balancers",
    "Security Risk": "Without access logs, it is challenging to perform effective security audits and resolve operational issues.",
    "Default Behavior / Limitations": "ELB does not have access logging enabled by default.",
    "Automation": "AWS Config rule `eip-attached` can be used to verify if ELB access logging is enabled.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-access-log.html"
    ]
  },
  {
    "Title": "Ensure Connection Draining is Enabled on Load Balancers",
    "Description": "Enable connection draining on all load balancers to allow in-flight requests to complete before deregistering backend instances.",
    "Applicability": "All Elastic Load Balancers",
    "Security Risk": "Disabling connection draining can result in dropped connections during scaling events, impacting user experience.",
    "Default Behavior / Limitations": "Connection draining is not enabled by default and must be configured per load balancer.",
    "Automation": "AWS Config rule `connection-draining-enabled` can audit whether connection draining is enabled.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-connection-draining-enabled.html"
    ]
  },
  {
    "Title": "Enable Cross-Zone Load Balancing",
    "Description": "Ensure Cross-Zone Load Balancing is enabled for all load balancers to evenly distribute incoming requests across multiple Availability Zones.",
    "Applicability": "All Elastic Load Balancers",
    "Security Risk": "Without cross-zone load balancing, resources can be unevenly utilized, leading to potential performance degradation.",
    "Default Behavior / Limitations": "Cross-zone load balancing is not enabled by default on all ELBs.",
    "Automation": "AWS Config can be used to detect and report on ELBs without cross-zone load balancing enabled.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-cross-zone-load-balancing-enabled.html"
    ]
  },
  {
    "Title": "Prohibit the Use of Insecure SSL Ciphers",
    "Description": "Ensure Elastic Load Balancers are configured to disallow the use of insecure SSL ciphers to protect connections from compromise.",
    "Applicability": "All Elastic Load Balancers using SSL",
    "Security Risk": "The use of weak SSL ciphers can expose data in transit to attacks.",
    "Default Behavior / Limitations": "Elliptic Curve ciphers are not enabled by default and must be configured.",
    "Automation": "AWS Config rules can be used to detect the use of insecure ciphers.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-insecure-ssl-ciphers.html"
    ]
  },
  {
    "Title": "Prohibit the Use of Insecure SSL Protocols",
    "Description": "Ensure Elastic Load Balancers are set to disallow insecure SSL protocols like SSLv3 to prevent vulnerabilities like POODLE attacks.",
    "Applicability": "All Elastic Load Balancers using SSL",
    "Security Risk": "Older SSL protocols are susceptible to various cryptographic attacks.",
    "Default Behavior / Limitations": "The use of newer protocols needs manual configuration.",
    "Automation": "AWS Config rules can detect ELBs configured with insecure SSL protocols.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-insecure-ssl-protocols.html"
    ]
  },
  {
    "Title": "Ensure Even Distribution of ELB Instances Across Availability Zones",
    "Description": "Configure Elastic Load Balancers to distribute backend instances evenly across Availability Zones to ensure high availability and fault tolerance.",
    "Applicability": "All Elastic Load Balancers",
    "Security Risk": "Uneven distribution can lead to a single point of failure and degrade performance.",
    "Default Behavior / Limitations": "Manual configuration is needed to ensure even instance distribution.",
    "Automation": "AWS Config custom rules can be used to detect and alert if instances are not evenly distributed.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/ec2-instances-distribution-across-availability-zones.html"
    ]
  },
  {
    "Title": "Maintain Minimum Backend Instances for ELBs",
    "Description": "Configure Elastic Load Balancers to have at least two healthy backend instances to ensure redundancy and high availability.",
    "Applicability": "All Elastic Load Balancers",
    "Security Risk": "Having fewer than two instances can lead to service disruptions if one becomes unhealthy.",
    "Default Behavior / Limitations": "Manual configuration required as AWS does not enforce a minimum number of backend instances.",
    "Automation": "AWS Health and CloudWatch can monitor instance health and alert when the minimum is not maintained.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-minimum-number-of-ec2-instances.html"
    ]
  },
  {
    "Title": "Restrict ELB Access Using Security Groups",
    "Description": "Ensure that Elastic Load Balancers are associated with at least one security group that restricts access only to specified listener ports for enhanced security.",
    "Applicability": "All Elastic Load Balancers",
    "Security Risk": "Unrestricted access increases the risk of malicious attacks on the load balancer.",
    "Default Behavior / Limitations": "Security groups must be configured manually for each ELB.",
    "Automation": "AWS Security Hub can assess and report on security group configurations for ELBs.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-security-group.html"
    ]
  },
  {
    "Title": "Identify and Terminate Idle Elastic Load Balancers",
    "Description": "Regularly review Elastic Load Balancers to identify those that are idle and terminate them to optimize AWS costs.",
    "Applicability": "All AWS Accounts",
    "Security Risk": "Idle resources incur unnecessary costs without providing any functionality.",
    "Default Behavior / Limitations": "Idle ELBs are not identified by default.",
    "Automation": "CloudWatch metrics can be used to determine ELBs with zero traffic and alert for cost optimization.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/idle-elastic-load-balancer.html"
    ]
  },
  {
    "Title": "Regularly Review Internet-Facing ELBs for Security",
    "Description": "Conduct routine reviews of internet-facing Elastic Load Balancers for security purposes to ensure they are configured according to the latest security best practices.",
    "Applicability": "All Internet-Facing Elastic Load Balancers",
    "Security Risk": "Misconfigured internet-facing ELBs are vulnerable to attacks from external entities.",
    "Default Behavior / Limitations": "No automated scanning for security alignment is provided by default AWS services.",
    "Automation": "Use AWS Security Hub to evaluate security configurations based on AWS best practices.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/internet-facing-load-balancers.html"
    ]
  },
  {
    "Title": "Identify and Remove Unused Elastic Load Balancers",
    "Description": "Detect and remove unused Elastic Load Balancers to lower monthly AWS costs by eliminating unnecessary resources.",
    "Applicability": "All AWS Accounts",
    "Security Risk": "Unnecessary costs associated with unused ELBs that do not add value or security.",
    "Default Behavior / Limitations": "Unused ELBs are not automatically removed.",
    "Automation": "AWS Trusted Advisor or CloudWatch metrics can be used to identify unused ELBs and alert accordingly.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/unused-elastic-load-balancers.html"
    ]
  },
  {
    "Title": "Enforce Secure Protocols for Web-Tier ELB Listeners",
    "Description": "Configure web-tier ELB listeners to enforce secure HTTPS/SSL protocols, protecting data in transit between clients and the web servers.",
    "Applicability": "All Web-Tier ELBs",
    "Security Risk": "Use of insecure protocols can allow interception and compromise of data in transit.",
    "Default Behavior / Limitations": "HTTPS/SSL must be explicitly configured; it is not enforced by default.",
    "Automation": "AWS Config rule `elbv2-esni-enabled` can verify HTTPS/SSL configuration for web-tier ELBs.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/web-tier-elb-https-listener.html"
    ]
  },
  {
    "Title": "Enforce Up-to-Date Security Policies for Web-Tier ELBs",
    "Description": "Ensure web-tier Elastic Load Balancers use the most recent predefined security policies to mitigate exposure to vulnerabilities.",
    "Applicability": "All Web-Tier ELBs",
    "Security Risk": "Outdated security policies risk exposing applications to known and patched vulnerabilities.",
    "Default Behavior / Limitations": "Regular manual updates are required.",
    "Automation": "AWS Config and Security Hub can monitor for outdated security policies and alert accordingly.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/web-tier-elb-latest-ssl-security-policies.html"
    ]
  },
  {
    "Title": "Configure Application Layer Health Checks for Web-Tier ELBs",
    "Description": "Set up application layer health checks for web-tier ELBs to ensure traffic is directed only to healthy backend instances.",
    "Applicability": "All Web-Tier ELBs",
    "Security Risk": "Without appropriate health checks, load balancers may route traffic to unhealthy instances, affecting service availability.",
    "Default Behavior / Limitations": "Health checks are configurable per target group.",
    "Automation": "Use AWS CloudWatch to monitor health check status and alert on failures.",
    "References": [
      "https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/web-tier-elb-health-check.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 4
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