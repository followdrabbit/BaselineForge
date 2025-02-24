```json
[
  {
    "Description": "Ensure that the suitable Desync Mitigation mode is configured for your Application Load Balancers.",
    "Reference": "[Configure HTTP Desync Mitigation Mode for Application Load Balancers](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/configure-desync-mitigation-mode.html)",
    "Observations": "Allows automated checking to ensure the correct desync mitigation mode is set."
  },
  {
    "Description": "Ensure that Amazon Gateway Load Balancers are using Multi-AZ configurations.",
    "Reference": "[Configure Multiple Availability Zones for Gateway Load Balancers](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/enable-multi-az.html)",
    "Observations": "Multi-AZ configurations improve fault tolerance."
  },
  {
    "Description": "Ensure that Drop Invalid Header Fields feature is enabled for your Application Load Balancers.",
    "Reference": "[Drop Invalid Header Fields for Application Load Balancers](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/drop-invalid-header-fields-enabled.html)",
    "Observations": "Helps maintain standard headers integrity."
  },
  {
    "Description": "Ensure ELBv2 ALBs are using a secure protocol.",
    "Reference": "[ELBv2 ALB Listener Security](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/listener-security.html)",
    "Observations": "Secure protocols like TLS are recommended."
  },
  {
    "Description": "Ensure ELBv2 load balancers have secure and valid security groups.",
    "Reference": "[ELBv2 ALB Security Group](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/security-group.html)",
    "Observations": "Security groups should limit access based on necessity."
  },
  {
    "Description": "Ensure that Amazon ALBs are using the latest predefined security policy for their SSL negotiation configuration.",
    "Reference": "[ELBv2 ALB Security Policy](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/security-policy.html)",
    "Observations": "Predefined policies help protect against SSL/TLS vulnerabilities."
  },
  {
    "Description": "Ensure that Amazon ALBs have the Access Logging feature enabled.",
    "Reference": "[ELBv2 Access Log](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/access-log.html)",
    "Observations": "Logs are crucial for auditing and troubleshooting."
  },
  {
    "Description": "Ensure ELBv2 Load Balancers have Deletion Protection feature enabled.",
    "Reference": "[ELBv2 Elastic Load Balancing Deletion Protection](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/deletion-protection.html)",
    "Observations": "Prevents accidental deletion of load balancers."
  },
  {
    "Description": "Ensure there is a minimum number of two healthy target instances associated with each AWS ELBv2 load balancer.",
    "Reference": "[ELBv2 Minimum Number of EC2 Target Instances](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/minimum-number-of-ec2-instances.html)",
    "Observations": "Ensures load balancing and high availability."
  },
  {
    "Description": "Ensure that your AWS Network Load Balancer listeners are using a secure protocol such as TLS.",
    "Reference": "[ELBv2 NLB Listener Security](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/network-load-balancer-listener-security.html)",
    "Observations": "TLS ensures encrypted communication."
  },
  {
    "Description": "Use Amazon WAF to protect Application Load Balancers from common web exploits.",
    "Reference": "[Enable Amazon WAF Integration for Application Load Balancers](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/alb-integrated-with-waf.html)",
    "Observations": "WAFs are effective in guarding against common web attacks."
  },
  {
    "Description": "Ensure fault tolerance for your Amazon Gateway Load Balancers by enabling Cross-Zone Load Balancing.",
    "Reference": "[Enable Cross-Zone Load Balancing](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/enable-cross-zone-load-balancing.html)",
    "Observations": "Cross-zone load balancing ensures better distribution and failover."
  },
  {
    "Description": "Ensure that Deletion Protection is enabled for Amazon Gateway Load Balancers.",
    "Reference": "[Enable Deletion Protection](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/enable-gwlb-deletion-protection.html)",
    "Observations": "Deletion protection prevents unwanted removal."
  },
  {
    "Description": "Ensure that your Application Load Balancers have a rule that redirects HTTP traffic to HTTPS.",
    "Reference": "[Enable HTTP to HTTPS Redirect for Application Load Balancers](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/http-to-https-redirect.html)",
    "Observations": "HTTP to HTTPS redirection helps ensure encrypted user sessions."
  },
  {
    "Description": "Ensure that Least Outstanding Requests (LOR) algorithm is enabled for your AWS Application Load Balancers (ALBs).",
    "Reference": "[Enable Least Outstanding Requests Algorithm](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/enable-alb-least-outstanding-requests.html)",
    "Observations": "LOR can improve load distribution."
  },
  {
    "Description": "Ensure that HTTP/2 support is enabled for Amazon Application Load Balancers (ALBs).",
    "Reference": "[Enable Support for HTTP/2](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/enable-http2-support.html)",
    "Observations": "HTTP/2 support can improve performance and efficiency."
  },
  {
    "Description": "Ensure that support for gRPC protocol is enabled for Application Load Balancers (ALBs).",
    "Reference": "[Enable Support for gRPC Protocol](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/enable-grpc-support.html)",
    "Observations": "gRPC support is essential for certain modern applications."
  },
  {
    "Description": "Ensure that your AWS Network Load Balancers are using TLS ALPN policies.",
    "Reference": "[Enable TLS ALPN Policy for Network Load Balancers](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/enable-tlsalpn-policy.html)",
    "Observations": "TLS ALPN policies allow better protocol negotiation."
  },
  {
    "Description": "Ensure Amazon internet-facing ELBv2 Load Balancers are regularly reviewed for security purposes.",
    "Reference": "[Internet Facing ELBv2 Load Balancers](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/internet-facing-load-balancers.html)",
    "Observations": "Security reviews can identify potential vulnerabilities."
  },
  {
    "Description": "Ensure Amazon Network Load Balancers (NLBs) are using the latest recommended predefined security policy for TLS negotiation configuration.",
    "Reference": "[Network Load Balancer Security Policy](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/network-load-balancer-security-policy.html)",
    "Observations": "Using up-to-date security policies improves security."
  },
  {
    "Description": "Identify unused ELBv2 Elastic Load Balancers, and delete them to help lower the cost of your monthly AWS bill.",
    "Reference": "[Unused ELBv2 Load Balancers](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/unused-load-balancers.html)",
    "Observations": "Identifying and removing unused resources can reduce costs."
  }
]
```