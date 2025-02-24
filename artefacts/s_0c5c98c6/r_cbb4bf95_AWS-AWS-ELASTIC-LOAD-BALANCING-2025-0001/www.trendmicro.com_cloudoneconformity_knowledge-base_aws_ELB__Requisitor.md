```json
[
  {
    "Description": "Ensure app-tier ELB listener uses a secure HTTPS or SSL protocol.",
    "Reference": "[App-Tier ELB Listener Security](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/app-tier-elb-https-listener.html)",
    "Observations": "HTTPS/SSL protocols are necessary to secure data in transit."
  },
  {
    "Description": "Ensure app-tier ELBs use the latest predefined security policies.",
    "Reference": "[App-Tier ELB Security Policy](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/app-tier-elb-latest-ssl-security-policies.html)",
    "Observations": "Up-to-date security policies help mitigate vulnerabilities."
  },
  {
    "Description": "Ensure app tier Elastic Load Balancer has application layer health check configured.",
    "Reference": "[App-Tier ELBs Health Check](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/app-tier-elb-health-check.html)",
    "Observations": "Application layer health checks ensure the ELB routes traffic to healthy instances."
  },
  {
    "Description": "Ensure HTTP/HTTPS applications are using Application Load Balancer instead of Classic Load Balancer.",
    "Reference": "[Classic Load Balancer](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-classic.html)",
    "Observations": "Application Load Balancers provide better features for traffic management."
  },
  {
    "Description": "Ensure that the suitable Desync Mitigation mode is configured for Classic Load Balancers.",
    "Reference": "[Configure HTTP Desync Mitigation Mode for Classic Load Balancers](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/enable-configure-desync-mitigation-mode.html)",
    "Observations": "Desync mitigation helps protect against HTTP desynchronization threats."
  },
  {
    "Description": "Ensure ELB access logging is enabled.",
    "Reference": "[ELB Access Log](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-access-log.html)",
    "Observations": "Access logs are crucial for troubleshooting and security audits."
  },
  {
    "Description": "Ensure connection draining is enabled for all load balancers.",
    "Reference": "[ELB Connection Draining Enabled](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-connection-draining-enabled.html)",
    "Observations": "Connection draining ensures in-flight requests are served before deregistering backend instances."
  },
  {
    "Description": "Ensure Cross-Zone Load Balancing is enabled for all load balancers.",
    "Reference": "[ELB Cross-Zone Load Balancing Enabled](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-cross-zone-load-balancing-enabled.html)",
    "Observations": "This ensures request distribution across multiple zones for higher availability."
  },
  {
    "Description": "Ensure ELBs don't use insecure SSL ciphers.",
    "Reference": "[ELB Insecure SSL Ciphers](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-insecure-ssl-ciphers.html)",
    "Observations": "Insecure ciphers can expose data to unauthorized parties."
  },
  {
    "Description": "Ensure ELBs don't use insecure SSL protocols.",
    "Reference": "[ELB Insecure SSL Protocols](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-insecure-ssl-protocols.html)",
    "Observations": "Insecure protocols such as SSLv3 can be vulnerable to attacks."
  },
  {
    "Description": "Ensure even distribution of backend instances registered to an ELB across Availability Zones.",
    "Reference": "[ELB Instances Distribution Across AZs](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/ec2-instances-distribution-across-availability-zones.html)",
    "Observations": "Even distribution maximizes fault tolerance and performance."
  },
  {
    "Description": "Ensure ELB listener uses a secure HTTPS or SSL protocol.",
    "Reference": "[ELB Listener Security](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-listener-security.html)",
    "Observations": "HTTPS/SSL ensures secure communication."
  },
  {
    "Description": "Ensure there is a minimum number of two healthy backend instances associated with each ELB.",
    "Reference": "[ELB Minimum Number Of EC2 Instances](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-minimum-number-of-ec2-instances.html)",
    "Observations": "This is fundamental for high availability and load balancing."
  },
  {
    "Description": "Check ELB security layer for at least one valid security group restricting access only to listener configuration ports.",
    "Reference": "[ELB Security Group](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-security-group.html)",
    "Observations": "Security groups control access to ELBs, reducing exposure to potential attacks."
  },
  {
    "Description": "Ensure ELBs use the latest predefined security policies.",
    "Reference": "[ELB Security Policy](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/elb-security-policy.html)",
    "Observations": "Regular policy updates protect against evolving threats."
  },
  {
    "Description": "Identify idle Elastic Load Balancers and terminate them to optimize AWS costs.",
    "Reference": "[Idle Elastic Load Balancer](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/idle-elastic-load-balancer.html)",
    "Observations": "Saving costs by removing unused resources."
  },
  {
    "Description": "Regularly review Amazon internet-facing ELBs/ALBs for security purposes.",
    "Reference": "[Internet Facing ELBs](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/internet-facing-load-balancers.html)",
    "Observations": "Internet-facing ELBs can be prime targets for attacks."
  },
  {
    "Description": "Identify unused Elastic Load Balancers and delete them to help lower monthly AWS costs.",
    "Reference": "[Unused Elastic Load Balancers](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/unused-elastic-load-balancers.html)",
    "Observations": "Cost optimization by removing unnecessary resources."
  },
  {
    "Description": "Ensure web-tier ELB listener uses a secure HTTPS or SSL protocol.",
    "Reference": "[Web-Tier ELB Listener Security](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/web-tier-elb-https-listener.html)",
    "Observations": "Securing data in transit is critical for web applications."
  },
  {
    "Description": "Ensure web-tier ELBs use the latest predefined security policies.",
    "Reference": "[Web-Tier ELB Security Policy](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/web-tier-elb-latest-ssl-security-policies.html)",
    "Observations": "Using current security policies protects from known vulnerabilities."
  },
  {
    "Description": "Ensure web tier Elastic Load Balancer has application layer health check configured.",
    "Reference": "[Web-Tier ELBs Health Check](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/web-tier-elb-health-check.html)",
    "Observations": "Proper health checks ensure resilient service provision."
  }
]
```