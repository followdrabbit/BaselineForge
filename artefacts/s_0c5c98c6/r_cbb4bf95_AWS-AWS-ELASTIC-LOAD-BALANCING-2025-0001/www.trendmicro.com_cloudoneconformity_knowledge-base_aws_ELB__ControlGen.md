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