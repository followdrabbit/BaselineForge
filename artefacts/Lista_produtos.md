
# Melhoras no script

- Ser capaz de processar outros formatos como Yaml (Falha ao processar URL: aws-config-conformance-packs/Security-Best-Practices-for-AutoScaling.yaml)
- Adicionar lógica de fracionar a unificação dos documentos (2 por vez até restar apenas um documento unificado)
- Ajustar os prompts dizendo que enviarei a informação sobre o serviço AWS em questão, para que eles então foquem apenas na proteção destes serviços


# Lista de produtos para criar baselines

## Amazon Application Migration Service

### Fonte
- https://docs.aws.amazon.com/mgn/latest/ug/security.html
- https://docs.aws.amazon.com/mgn/latest/ug/identity-access-management.html
- https://docs.aws.amazon.com/mgn/latest/ug/security_iam_access-manage.html
- https://docs.aws.amazon.com/mgn/latest/ug/infrastructure-security.html
- https://docs.aws.amazon.com/mgn/latest/ug/cross-service-confused-deputy-prevention.html
- https://docs.aws.amazon.com/mgn/latest/ug/using-service-linked-roles.html


## Amazon AutoScalling

### Fonte
- aws-config-conformance-packs/Security-Best-Practices-for-AutoScaling.yaml
- https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/AutoScaling/
- https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-data-protection.html
- https://docs.aws.amazon.com/autoscaling/ec2/userguide/cross-service-confused-deputy-prevention.html
- https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-launch-template-permissions.html
- https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html
- https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-vpc-endpoints.html


## Amazon Lightsail

### Fonte
- https://docs.aws.amazon.com/lightsail/latest/userguide/security_iam_service-with-iam.html
- https://docs.aws.amazon.com/lightsail/latest/userguide/security_iam.html
- https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-using-service-linked-roles.html
- https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-update-management.html


## Amazon Outposts

### Fonte
- https://docs.aws.amazon.com/outposts/latest/userguide/data-protection.html
- https://docs.aws.amazon.com/outposts/latest/userguide/security_iam_service-with-iam.html
- https://docs.aws.amazon.com/outposts/latest/userguide/using-service-linked-roles.html
- https://docs.aws.amazon.com/outposts/latest/userguide/infrastructure-security.html
- https://docs.aws.amazon.com/outposts/latest/userguide/internet-access.html
- https://sysdig.com/blog/secure-and-monitor-aws-outposts-hybrid-clouds/
- https://help.deepsecurity.trendmicro.com/20_0/on-premise/aws-outposts.html


## Amazon Simple Workflow Service (SWF)

### Fonte
- https://docs.aws.amazon.com/amazonswf/latest/developerguide/data-protection.html
- https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-vpc-endpoints.html
- https://docs.aws.amazon.com/amazonswf/latest/developerguide/ct-logging.html
- https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html
- https://docs.aws.amazon.com/amazonswf/latest/developerguide/infrastructure-security.html


## Amazon Identity and Access Management (IAM)

### Fonte
- https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html
- https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html
- https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html
- https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds-programmatic-access.html
- https://docs.aws.amazon.com/IAM/latest/UserGuide/security-audit-guide.html
- https://docs.aws.amazon.com/IAM/latest/UserGuide/data-protection.html
- https://docs.aws.amazon.com/IAM/latest/UserGuide/security-logging-and-monitoring.html
- https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html
-  https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-track-privileged-tasks.html


## Amazon Aurora

### Fonte

#### Parte 1

- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_BestPractices.Security.html
- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.html
- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/database-authentication.html
- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html
- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/DataDurability.html
- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html
- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.Keys.html
- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html
- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL-certificate-rotation.html
- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/inter-network-traffic-privacy.html


#### Parte 2

- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAM.html
- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/cross-service-confused-deputy-prevention.html
- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html
- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.LoggingAndMonitoring.html
- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/infrastructure-security.html
- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/vpc-interface-endpoints.html
- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.RDSSecurityGroups.html
- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.MasterAccounts.html
- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAM.ServiceLinkedRoles.html
- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html
 

## Amazon Elasticsearch

Foi descontinuado e tem pouca documentação oficial, o serviço deve ser migrado para o aws OpenSearch (https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html)
De qualquer forma é possível definir algumas regras com base nesta doc: https://docs.aws.amazon.com/securityhub/latest/userguide/es-controls.html


## Amazon RDS Proxy

### Fonte
- https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html
- https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-planning.html
- https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.howitworks.html
- https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-secrets-arns.html
- https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-iam-setup.html
- https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-connections.html
- https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-pinning.html


## Amazon SimpleDB

### Fonte
- https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/UsingIAMWithSDB.html
- https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/UsingTemporarySecurityCredentials_SDB.html


## Amazon TimeStream

### Fonte
- https://docs.aws.amazon.com/timestream/latest/developerguide/data-protection.html
- https://docs.aws.amazon.com/timestream/latest/developerguide/EncryptionAtRest.html
- https://docs.aws.amazon.com/timestream/latest/developerguide/security-bp.html
- https://docs.aws.amazon.com/timestream/latest/developerguide/EncryptionInTransit.html
- https://docs.aws.amazon.com/timestream/latest/developerguide/KeyManagement.html
- https://docs.aws.amazon.com/timestream/latest/developerguide/monitoring.html
- https://docs.aws.amazon.com/timestream/latest/developerguide/logging-using-cloudtrail.html
- https://docs.aws.amazon.com/timestream/latest/developerguide/ConfigAndVulnerability.html
- https://docs.aws.amazon.com/timestream/latest/developerguide/VPCEndpoints.html
- https://docs.aws.amazon.com/timestream/latest/developerguide/best-practices-security-preventative.html


## Amazon Cloud WAN

### Fonte
- https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-security.html


## Amazon Direct Connect

### Fonte
- https://docs.aws.amazon.com/directconnect/latest/UserGuide/data-protection.html
- https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-at-rest.html
- https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-in-transit.html
- https://docs.aws.amazon.com/directconnect/latest/UserGuide/dc-incident-response.html
- https://docs.aws.amazon.com/directconnect/latest/UserGuide/infrastructure-security.html


## AWS Elastic Load Balancing

Contém:

- Amazon Application Load balancer
- Amazon Network Load Balancer
- Amazon Gateway Load Balancer sob o nome AWS Elastic Load Balancing


### Fonte

- https://aws.amazon.com/pt/blogs/networking-and-content-delivery/security-best-practices-when-using-alb-authentication/
- https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELBv2/
- https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ELB/
- https://sysdig.com/learn-cloud-native/aws-elastic-load-balancing-security/


## Amazon Global Accelerator

### Fonte
- https://docs.aws.amazon.com/global-accelerator/latest/dg/security-iam.html
- https://docs.aws.amazon.com/global-accelerator/latest/dg/secure-vpc-connections.html
- https://docs.aws.amazon.com/global-accelerator/latest/dg/logging-and-monitoring.html
- https://docs.aws.amazon.com/global-accelerator/latest/dg/infrastructure-security.html


## Amazon Registrar

Serviço não Encontrado


## Amazon ServiceCatalog

### Fonte
- https://docs.aws.amazon.com/servicecatalog/latest/adminguide/data-protection.html
- https://docs.aws.amazon.com/servicecatalog/latest/adminguide/controlling_access.html
- https://docs.aws.amazon.com/servicecatalog/latest/adminguide/using-service-linked-roles.html
- https://docs.aws.amazon.com/servicecatalog/latest/adminguide/logging-and-monitoring.html
- https://docs.aws.amazon.com/servicecatalog/latest/adminguide/infrastructure-security.html
- https://docs.aws.amazon.com/servicecatalog/latest/adminguide/security-best-practices.html


## Amazon VPC

### Fonte
- https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html
- https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/
- https://docs.aws.amazon.com/vpc/latest/userguide/data-protection.html
- https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html
- https://docs.aws.amazon.com/vpc/latest/userguide/security-iam.html
- https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html


## Amazon VPC EndPoint

### Fonte
- https://docs.aws.amazon.com/pt_br/vpc/latest/privatelink/vpc-endpoints-access.html
- https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/vpc-endpoints-in-use.html
- https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/VPC/endpoint-exposed.html
- https://aws.amazon.com/pt/blogs/architecture/reduce-cost-and-increase-security-with-amazon-vpc-endpoints/


## Amazon MQ

### Fonte
- https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/
- https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/data-protection.html
- https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security-iam.html
- https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/infrastructure-security.html
- https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/using-amazon-mq-securely.html
- https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/publicly-accessible.html


### Amazon Kinesis Video Streams

### Fonte
- https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/security-best-practices.html
- https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-kms.html
- https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-iam.html
- https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-iot.html


## Amazon CloudSearch

### Fonte
- https://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-access.html
- https://aws.amazon.com/pt/blogs/security/amazon-cloudsearch-now-with-more-granular-access-control-for-domains/


## Amazon Data Pipeline

### Fonte
- https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/data-protection.html
- https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html
- https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-cloudtrail-logging.html
- https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/infrastructure-security.html


