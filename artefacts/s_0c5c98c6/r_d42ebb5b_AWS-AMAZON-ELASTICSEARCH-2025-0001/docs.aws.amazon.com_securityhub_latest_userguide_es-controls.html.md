# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/securityhub/latest/userguide/es-controls.html'}

[](/pdfs/securityhub/latest/userguide/securityhub.pdf#es-controls "Open PDF")

[Documentation](/index.html)[AWS Security Hub](/securityhub/index.html)[User
Guide](what-is-securityhub.html)

[ES.1] Elasticsearch domains should have encryption at-rest enabled[ES.2]
Elasticsearch domains should not be publicly accessible[ES.3] Elasticsearch
domains should encrypt data sent between nodes[ES.4] Elasticsearch domain
error logging to CloudWatch Logs should be enabled[ES.5] Elasticsearch domains
should have audit logging enabled[ES.6] Elasticsearch domains should have at
least three data nodes[ES.7] Elasticsearch domains should be configured with
at least three dedicated master nodes[ES.8] Connections to Elasticsearch
domains should be encrypted using the latest TLS security policy[ES.9]
Elasticsearch domains should be tagged

# Security Hub for Elasticsearch

These AWS Security Hub controls evaluate the Elasticsearch service and
resources.

These controls may not be available in all AWS Regions. For more information,
see [Availability of controls by Region](./securityhub-
regions.html#securityhub-regions-control-support).

## [ES.1] Elasticsearch domains should have encryption at-rest enabled

**Related requirements:** PCI DSS v3.2.1/3.4, NIST.800-53.r5 CA-9(1),
NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28,
NIST.800-53.r5 SC-28(1), NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SI-7(6)

**Category:** Protect > Data Protection > Encryption of data-at-rest

**Severity:** Medium

**Resource type:** `AWS::Elasticsearch::Domain`

**AWS Config rule:** [`elasticsearch-encrypted-at-
rest`](https://docs.aws.amazon.com/config/latest/developerguide/elasticsearch-
encrypted-at-rest.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether Elasticsearch domains have encryption at rest
configuration enabled. The check fails if encryption at rest is not enabled.

For an added layer of security for your sensitive data in OpenSearch, you
should configure your OpenSearch to be encrypted at rest. Elasticsearch
domains offer encryption of data at rest. The feature uses AWS KMS to store
and manage your encryption keys. To perform the encryption, it uses the
Advanced Encryption Standard algorithm with 256-bit keys (AES-256).

To learn more about OpenSearch encryption at rest, see [Encryption of data at
rest for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-
service/latest/developerguide/encryption-at-rest.html) in the _Amazon
OpenSearch Service Developer Guide_.

Certain instance types, such as `t.small` and `t.medium`, don't support
encryption of data at rest. For details, see [Supported instance
types](https://docs.aws.amazon.com/opensearch-
service/latest/developerguide/supported-instance-types.html) in the _Amazon
OpenSearch Service Developer Guide_.

### Remediation

To enable encryption at rest for new and existing Elasticsearch domains, see
[Enabling encryption of data at rest](https://docs.aws.amazon.com/opensearch-
service/latest/developerguide/encryption-at-rest.html#enabling-ear) in the
_Amazon OpenSearch Service Developer Guide_.

## [ES.2] Elasticsearch domains should not be publicly accessible

**Related requirements:** PCI DSS v3.2.1/1.2.1,PCI DSS v3.2.1/1.3.1,PCI DSS
v3.2.1/1.3.2,PCI DSS v3.2.1/1.3.4,PCI DSS v3.2.1/1.3.6, NIST.800-53.r5 AC-21,
NIST.800-53.r5 AC-3, NIST.800-53.r5 AC-3(7), NIST.800-53.r5 AC-4,
NIST.800-53.r5 AC-4(21), NIST.800-53.r5 AC-6, NIST.800-53.r5 SC-7,
NIST.800-53.r5 SC-7(11), NIST.800-53.r5 SC-7(16), NIST.800-53.r5 SC-7(20),
NIST.800-53.r5 SC-7(21), NIST.800-53.r5 SC-7(3), NIST.800-53.r5 SC-7(4),
NIST.800-53.r5 SC-7(9), PCI DSS v4.0.1/1.4.4

**Category:** Protect > Secure network configuration > Resources within VPC

**Severity:** Critical

**Resource type:** `AWS::Elasticsearch::Domain`

**AWS Config rule:** [`elasticsearch-in-vpc-
only`](https://docs.aws.amazon.com/config/latest/developerguide/elasticsearch-
in-vpc-only.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether Elasticsearch domains are in a VPC. It does not
evaluate the VPC subnet routing configuration to determine public access. You
should ensure that Elasticsearch domains are not attached to public subnets.
See [Resource-based policies](https://docs.aws.amazon.com/opensearch-
service/latest/developerguide/ac.html#ac-types-resource) in the _Amazon
OpenSearch Service Developer Guide_. You should also ensure that your VPC is
configured according to the recommended best practices. See [Security best
practices for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-
security-best-practices.html) in the _Amazon VPC User Guide_.

Elasticsearch domains deployed within a VPC can communicate with VPC resources
over the private AWS network, without the need to traverse the public
internet. This configuration increases the security posture by limiting access
to the data in transit. VPCs provide a number of network controls to secure
access to Elasticsearch domains, including network ACL and security groups.
Security Hub recommends that you migrate public Elasticsearch domains to VPCs
to take advantage of these controls.

### Remediation

If you create a domain with a public endpoint, you cannot later place it
within a VPC. Instead, you must create a new domain and migrate your data. The
reverse is also true. If you create a domain within a VPC, it cannot have a
public endpoint. Instead, you must either [create another
domain](https://docs.aws.amazon.com/opensearch-
service/latest/developerguide/createupdatedomains.html) or disable this
control.

See [Launching your Amazon OpenSearch Service domains within a
VPC](https://docs.aws.amazon.com/opensearch-
service/latest/developerguide/vpc.html) in the _Amazon OpenSearch Service
Developer Guide_.

## [ES.3] Elasticsearch domains should encrypt data sent between nodes

**Related requirements:** NIST.800-53.r5 AC-4, NIST.800-53.r5 SC-13,
NIST.800-53.r5 SC-23, NIST.800-53.r5 SC-23(3), NIST.800-53.r5 SC-7(4),
NIST.800-53.r5 SC-8, NIST.800-53.r5 SC-8(1), NIST.800-53.r5 SC-8(2), PCI DSS
v4.0.1/4.2.1

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:** `AWS::Elasticsearch::Domain`

**AWS Config rule:** [`elasticsearch-node-to-node-encryption-
check`](https://docs.aws.amazon.com/config/latest/developerguide/elasticsearch-
node-to-node-encryption-check.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Elasticsearch domain has node-to-node
encryption enabled. The control fails if the Elasticsearch domain doesn't have
node-to-node encryption enabled. The control also produces failed findings if
an Elasticsearch version doesn't support node-to-node encryption checks.

HTTPS (TLS) can be used to help prevent potential attackers from eavesdropping
on or manipulating network traffic using person-in-the-middle or similar
attacks. Only encrypted connections over HTTPS (TLS) should be allowed.
Enabling node-to-node encryption for Elasticsearch domains ensures that intra-
cluster communications are encrypted in transit.

There can be a performance penalty associated with this configuration. You
should be aware of and test the performance trade-off before enabling this
option.

### Remediation

For information about enabling node-to-node encryption on new and existing
domains, see [Enabling node-to-node
encryption](https://docs.aws.amazon.com/opensearch-
service/latest/developerguide/ntn.html#enabling-ntn) in the _Amazon OpenSearch
Service Developer Guide_.

## [ES.4] Elasticsearch domain error logging to CloudWatch Logs should be
enabled

**Related requirements:** NIST.800-53.r5 AC-2(4), NIST.800-53.r5 AC-4(26),
NIST.800-53.r5 AC-6(9), NIST.800-53.r5 AU-10, NIST.800-53.r5 AU-12,
NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3, NIST.800-53.r5 AU-6(3),
NIST.800-53.r5 AU-6(4), NIST.800-53.r5 CA-7, NIST.800-53.r5 SC-7(9),
NIST.800-53.r5 SI-3(8), NIST.800-53.r5 SI-4(20), NIST.800-53.r5 SI-7(8)

**Category:** Identify - Logging

**Severity:** Medium

**Resource type:** `AWS::Elasticsearch::Domain`

**AWS Config rule:** [`elasticsearch-logs-to-
cloudwatch`](https://docs.aws.amazon.com/config/latest/developerguide/elasticsearch-
logs-to-cloudwatch.html)

**Schedule type:** Change triggered

**Parameters:**

  * `logtype = 'error'` (not customizable)

This control checks whether Elasticsearch domains are configured to send error
logs to CloudWatch Logs.

You should enable error logs for Elasticsearch domains and send those logs to
CloudWatch Logs for retention and response. Domain error logs can assist with
security and access audits, and can help to diagnose availability issues.

### Remediation

For information on how to enable log publishing, see [Enabling log publishing
(console)](https://docs.aws.amazon.com/opensearch-
service/latest/developerguide/createdomain-configure-slow-
logs.html#createdomain-configure-slow-logs-console) in the _Amazon OpenSearch
Service Developer Guide_.

## [ES.5] Elasticsearch domains should have audit logging enabled

**Related requirements:** NIST.800-53.r5 AC-2(4), NIST.800-53.r5 AC-4(26),
NIST.800-53.r5 AC-6(9), NIST.800-53.r5 AU-10, NIST.800-53.r5 AU-12,
NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3, NIST.800-53.r5 AU-6(3),
NIST.800-53.r5 AU-6(4), NIST.800-53.r5 CA-7, NIST.800-53.r5 SC-7(9),
NIST.800-53.r5 SI-3(8), NIST.800-53.r5 SI-4(20), NIST.800-53.r5 SI-7(8), PCI
DSS v4.0.1/10.4.2

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:** `AWS::Elasticsearch::Domain`

**AWS Config rule:** `elasticsearch-audit-logging-enabled` (custom Security
Hub rule)

**Schedule type:** Change triggered

**Parameters:**

  * `cloudWatchLogsLogGroupArnList` (not customizable). Security Hub does not populate this parameter. Comma-separated list of CloudWatch Logs log groups that should be configured for audit logs.

This rule is `NON_COMPLIANT` if the CloudWatch Logs log group of the
Elasticsearch domain is not specified in this parameter list.

This control checks whether Elasticsearch domains have audit logging enabled.
This control fails if an Elasticsearch domain does not have audit logging
enabled.

Audit logs are highly customizable. They allow you to track user activity on
your Elasticsearch clusters, including authentication successes and failures,
requests to OpenSearch, index changes, and incoming search queries.

### Remediation

For detailed instructions on enabling audit logs, see [Enabling audit
logs](https://docs.aws.amazon.com/opensearch-
service/latest/developerguide/audit-logs.html#audit-log-enabling) in the
_Amazon OpenSearch Service Developer Guide_.

## [ES.6] Elasticsearch domains should have at least three data nodes

**Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-6(2),
NIST.800-53.r5 SC-36, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-13(5)

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:** `AWS::Elasticsearch::Domain`

**AWS Config rule:** `elasticsearch-data-node-fault-tolerance` (custom
Security Hub rule)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether Elasticsearch domains are configured with at least
three data nodes and `zoneAwarenessEnabled` is `true`.

An Elasticsearch domain requires at least three data nodes for high
availability and fault-tolerance. Deploying an Elasticsearch domain with at
least three data nodes ensures cluster operations if a node fails.

### Remediation

###### To modify the number of data nodes in an Elasticsearch domain

  1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/).

  2. Under **Domains** , choose the name of the domain you want to edit.

  3. Choose **Edit domain**.

  4. Under **Data nodes** , set **Number of nodes** to a number greater than or equal to `3`.

For three Availability Zone deployments, set to a multiple of three to ensure
equal distribution across Availability Zones.

  5. Choose **Submit**.

## [ES.7] Elasticsearch domains should be configured with at least three
dedicated master nodes

**Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-6(2),
NIST.800-53.r5 SC-36, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-13(5)

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:** `AWS::Elasticsearch::Domain`

**AWS Configrule:** `elasticsearch-primary-node-fault-tolerance` (custom
Security Hub rule)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether Elasticsearch domains are configured with at least
three dedicated primary nodes. This control fails if the domain does not use
dedicated primary nodes. This control passes if Elasticsearch domains have
five dedicated primary nodes. However, using more than three primary nodes
might be unnecessary to mitigate the availability risk, and will result in
additional cost.

An Elasticsearch domain requires at least three dedicated primary nodes for
high availability and fault-tolerance. Dedicated primary node resources can be
strained during data node blue/green deployments because there are additional
nodes to manage. Deploying an Elasticsearch domain with at least three
dedicated primary nodes ensures sufficient primary node resource capacity and
cluster operations if a node fails.

### Remediation

###### To modify the number of dedicated primary nodes in an OpenSearch domain

  1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/).

  2. Under **Domains** , choose the name of the domain you want to edit.

  3. Choose **Edit domain**.

  4. Under **Dedicated master nodes** , set **Instance type** to the desired instance type.

  5. Set **Number of master nodes** equal to three or greater.

  6. Choose **Submit**.

## [ES.8] Connections to Elasticsearch domains should be encrypted using the
latest TLS security policy

**Related requirements:** NIST.800-53.r5 AC-17(2), NIST.800-53.r5 AC-4,
NIST.800-53.r5 IA-5(1), NIST.800-53.r5 SC-12(3), NIST.800-53.r5 SC-13,
NIST.800-53.r5 SC-23, NIST.800-53.r5 SC-23(3), NIST.800-53.r5 SC-7(4),
NIST.800-53.r5 SC-8, NIST.800-53.r5 SC-8(1), NIST.800-53.r5 SC-8(2),
NIST.800-53.r5 SI-7(6), PCI DSS v4.0.1/4.2.1

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:** `AWS::Elasticsearch::Domain`

**AWS Config rule:** `elasticsearch-https-required` (custom Security Hub rule)

**Schedule type:** Change triggered

**Parameters:** None

This controls checks whether an Elasticsearch domain endpoint is configured to
use the latest TLS security policy. The control fails if the Elasticsearch
domain endpoint isn't configured to use the latest supported policy or if
HTTPs isn't enabled. The current latest supported TLS security policy is
`Policy-Min-TLS-1-2-PFS-2023-10`.

HTTPS (TLS) can be used to help prevent potential attackers from using person-
in-the-middle or similar attacks to eavesdrop on or manipulate network
traffic. Only encrypted connections over HTTPS (TLS) should be allowed.
Encrypting data in transit can affect performance. You should test your
application with this feature to understand the performance profile and the
impact of TLS. TLS 1.2 provides several security enhancements over previous
versions of TLS.

### Remediation

To enable TLS encryption, use the
[UpdateDomainConfig](https://docs.aws.amazon.com/opensearch-
service/latest/APIReference/API_UpdateDomainConfig.html) API operation to
configure the [DomainEndpointOptions](https://docs.aws.amazon.com/opensearch-
service/latest/APIReference/API_DomainEndpointOptions.html) object. This sets
the `TLSSecurityPolicy`.

## [ES.9] Elasticsearch domains should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::Elasticsearch::Domain`

**AWS Config rule:** `tagged-elasticsearch-domain` (custom Security Hub rule)

**Schedule type:** Change triggered

**Parameters:**

Parameter | Description | Type | Allowed custom values | Security Hub default value  
---|---|---|---|---  
`requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive.  | StringList  | List of tags that meet [AWS requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html#tag-conventions) |  `No default value`  
  
This control checks whether an Elasticsearch domain has tags with the specific
keys defined in the parameter `requiredTagKeys`. The control fails if the
domain doesnât have any tag keys or if it doesnât have all the keys
specified in the parameter `requiredTagKeys`. If the parameter
`requiredTagKeys` isn't provided, the control only checks for the existence of
a tag key and fails if the domain isn't tagged with any key. System tags,
which are automatically applied and begin with `aws:`, are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key
and an optional value. You can create tags to categorize resources by purpose,
owner, environment, or other criteria. Tags can help you identify, organize,
search for, and filter resources. Tagging also helps you track accountable
resource owners for actions and notifications. When you use tagging, you can
implement attribute-based access control (ABAC) as an authorization strategy,
which defines permissions based on tags. You can attach tags to IAM entities
(users or roles) and to AWS resources. You can create a single ABAC policy or
a separate set of policies for your IAM principals. You can design these ABAC
policies to allow operations when the principal's tag matches the resource
tag. For more information, see [What is ABAC for
AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-
based-access-control.html) in the _IAM User Guide_.

###### Note

Donât add personally identifiable information (PII) or other confidential or
sensitive information in tags. Tags are accessible to many AWS services,
including AWS Billing. For more tagging best practices, see [Tagging your AWS
resources](https://docs.aws.amazon.com/tag-
editor/latest/userguide/tagging.html#tag-best-practices) in the _AWS General
Reference_.

### Remediation

To add tags to an Elasticsearch domain, see [Working with
tags](https://docs.aws.amazon.com/opensearch-
service/latest/developerguide/managedomains-
awsresourcetagging.html#managedomains-awsresourcetagging-console) in the
_Amazon OpenSearch Service Developer Guide_.

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Elastic Load Balancing controls

Amazon EMR controls

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

