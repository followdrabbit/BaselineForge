### ControlGen Output - Arquivo 1
```json
[
  {
    "Title": "Restrict Access to Replication Servers to Source CIDR Range",
    "Description": "Configure security groups for replication servers to allow inbound traffic only from the specified source servers' CIDR range. This can be achieved by adding ingress rules to the security group associated with the replication servers, specifying the exact CIDR range allowed.",
    "Applicability": "Replication servers within AWS Application Migration Service",
    "Security Risk": "If access is not restricted to specific CIDR ranges, unauthorized users could exploit open network paths to compromise system integrity and data confidentiality.",
    "Default Behavior / Limitations": "AWS security groups do not restrict CIDR ranges by default; customization is needed.",
    "Automation": "Enforceable through AWS Config rule `custom-inbound-sg-rule` to ensure only specific CIDR ranges are allowed.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/security.html"
    ]
  },
  {
    "Title": "Restrict Open Ports Post-Migration",
    "Description": "Configure security groups and Network ACLs for migrated servers to allow only necessary ports. This involves reviewing and setting egress and ingress rules to deny all entries except those explicitly required for application functionality.",
    "Applicability": "Post-migration server environments",
    "Security Risk": "Exposing unnecessary ports can lead to potential vulnerabilities and unauthorized access, risking system availability and data integrity.",
    "Default Behavior / Limitations": "AWS security groups do not restrict ports by default; manual configuration is required.",
    "Automation": "Utilize AWS Config rules such as `restricted-common-port` to ensure compliance with open port policies.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/security.html"
    ]
  },
  {
    "Title": "Automate OS and Software Package Patching",
    "Description": "Utilize AWS Systems Manager Patch Manager to automate the patching of OS and software packages. This ensures that all systems are regularly updated to protect against known vulnerabilities.",
    "Applicability": "All servers managed within AWS Application Migration Service",
    "Security Risk": "Unpatched systems may be vulnerable to exploit and attack, risking data theft or system compromise.",
    "Default Behavior / Limitations": "Patching is not automated by default and requires configuration of AWS Systems Manager.",
    "Automation": "Automated through AWS Systems Manager Patch Manager, which can schedule and apply patches systematically.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/security.html"
    ]
  },
  {
    "Title": "Verify and Enforce Minimal Running Services",
    "Description": "Using AWS Config rules or custom scripts, ensure that only necessary OS/application services are enabled post-migration.",
    "Applicability": "All instances post-migration",
    "Security Risk": "Running unnecessary services increases the attack surface and resource utilization, potentially compromising security and performance.",
    "Default Behavior / Limitations": "AWS does not provide built-in verification of running services, custom implementation required.",
    "Automation": "AWS Config custom rules can assist in auditing running services and enforcing compliance.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/security.html"
    ]
  },
  {
    "Title": "Enable AWS Shield for Anti-DDoS Protection",
    "Description": "Activate AWS Shield, particularly AWS Shield Advanced, to protect replication and migrated servers from DDoS attacks by enabling it within the AWS account for critical resources.",
    "Applicability": "All critical resources within AWS Application Migration Service",
    "Security Risk": "Lack of protection exposes resources to denial of service attacks, impacting availability and service continuity.",
    "Default Behavior / Limitations": "AWS Shield Standard is enabled by default, but AWS Shield Advanced requires manual activation and setup.",
    "Automation": "Manual validation required for AWS Shield Advanced setup. Monitor through AWS Shield dashboard.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/security.html"
    ]
  },
  {
    "Title": "Implement Structured IAM Policies",
    "Description": "Ensure all IAM policies are structured using 'Effect', 'Action', 'Resource', and optionally 'Condition' to define precise permissions and limitations on actions.",
    "Applicability": "All IAM policies in the AWS account",
    "Security Risk": "Improperly structured policies may lead to over-permissive access, risking data breaches and unauthorized actions.",
    "Default Behavior / Limitations": "IAM does not enforce a specific structure beyond syntactical correctness.",
    "Automation": "Manual validation required to ensure policy compliance with defined structure.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/security.html"
    ]
  },
  {
    "Title": "Enable CloudTrail Logging for AWS Application Migration Service",
    "Description": "Configure AWS CloudTrail to log all activities related to the AWS Application Migration Service in all regions to ensure complete auditability and traceability.",
    "Applicability": "All AWS accounts using AWS Application Migration Service",
    "Security Risk": "Without CloudTrail logging, unauthorized activities may go unnoticed, complicating incident response and forensics.",
    "Default Behavior / Limitations": "CloudTrail is not enabled by default for all regions; setup is required.",
    "Automation": "Automated setup through AWS CloudFormation or manual configuration. AWS Config rule `cloudtrail-enabled-and-logging` can monitor compliance.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/security.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 2
```json
[
  {
    "Title": "Explicit IAM Policy for AWS Application Migration Service (AWS MGN)",
    "Description": "Create a specific IAM policy that grants necessary permissions for users to manage AWS Application Migration Service (AWS MGN) resources. Attach this policy to IAM users or groups that require access.",
    "Applicability": "All IAM users who require access to AWS MGN resources",
    "Security Risk": "Without explicit permissions, users cannot manage AWS MGN resources, potentially impacting operations that depend on this service.",
    "Default Behavior / Limitations": "By default, users have no permissions to AWS MGN resources. Permissions must be explicitly granted.",
    "Automation": "Can be managed through IAM by creating custom policies and using AWS Config to ensure policy compliance.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/identity-access-management.html"
    ]
  },
  {
    "Title": "Enforce Federation for AWS Access using Identity Providers",
    "Description": "Configure AWS IAM roles with policies for federated users to access AWS services using temporary credentials through an identity provider. This setup must use AWS Security Token Service (STS) to generate temporary access.",
    "Applicability": "All human users, including those with administrative access requirements",
    "Security Risk": "Permanent credentials pose a risk of unauthorized access if compromised. Federated access reduces this risk by using temporary credentials.",
    "Default Behavior / Limitations": "AWS accounts do not enforce federation by default. Requires integration with identity providers.",
    "Automation": "Implement through AWS IAM by configuring identity providers and roles with suitable trust policies, enforce via AWS Config and Security Hub.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/identity-access-management.html"
    ]
  },
  {
    "Title": "Centralized Access Management with AWS IAM Identity Center",
    "Description": "Use AWS IAM Identity Center to centralize user and group management across AWS accounts and applications. Integrate with external identity providers to synchronize user and group data.",
    "Applicability": "All AWS accounts using multiple applications or needing centralized identity management",
    "Security Risk": "Without centralized management, inconsistencies in access policies may occur, leading to unauthorized access or inefficient user management.",
    "Default Behavior / Limitations": "Requires configuration of AWS IAM Identity Center and integration with external identity providers. Not enabled by default.",
    "Automation": "Use AWS IAM Identity Center setup, manage policies via AWS IAM, and validate synchronization with AWS Config.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/identity-access-management.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 3
```json
[
  {
    "Title": "Create and Attach Necessary IAM Policies",
    "Description": "Ensure that IAM policies are created and appropriately attached to users, roles, or groups to grant necessary permissions for executing actions on AWS resources.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Without properly assigned IAM permissions, users or roles may not have the necessary permissions to perform required operations, leading to operational inefficiencies or potential security risks.",
    "Default Behavior / Limitations": "AWS accounts and roles have no permissions by default; explicit policies need to be defined and attached.",
    "Automation": "Can be automated using AWS IAM and CloudFormation templates to ensure policies are created and managed centrally.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html"
    ]
  },
  {
    "Title": "Implement Identity-based Policies",
    "Description": "Use identity-based policies in JSON format to grant permissions directly to AWS identities such as users, roles, or groups, distinguishing between inline and managed policies for optimal flexibility.",
    "Applicability": "All AWS accounts",
    "Security Risk": "Improperly configured identity-based policies can result in either excessive permissions or lack of necessary access, undermining security principles.",
    "Default Behavior / Limitations": "Policies must be defined; no default permissions are granted.",
    "Automation": "Can be managed through AWS IAM using CloudFormation or the AWS CLI for consistent policy application.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html"
    ]
  },
  {
    "Title": "Deploy Resource-based Policies",
    "Description": "Ensure that resource-based policies are configured and attached to AWS resources to explicitly denote which principals have access, overcoming cross-account access challenges.",
    "Applicability": "All AWS resources supporting resource-based policies",
    "Security Risk": "Lack of resource-based policies can lead to unauthorized access to AWS resources, especially in cross-account scenarios.",
    "Default Behavior / Limitations": "Resource-based policies must be explicitly defined on supported resources for access management.",
    "Automation": "Can be handled using AWS CloudFormation templates or the AWS CLI to define and deploy resource-based policies.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_resource-based.html"
    ]
  },
  {
    "Title": "Define Permissions Boundaries",
    "Description": "Set permissions boundaries to restrict the maximum permissions an identity-based policy can grant, limiting access in a controlled manner.",
    "Applicability": "All identities within AWS accounts",
    "Security Risk": "Without boundaries, there's potential risk of inadvertently granting excessive permissions, which could be exploited by malicious actors.",
    "Default Behavior / Limitations": "Permissions boundaries must be explicitly defined; they do not override existing policies but act as a limiting layer.",
    "Automation": "Use AWS IAM to define and manage permissions boundaries through the Console or AWS CLI.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html"
    ]
  },
  {
    "Title": "Apply Service Control Policies (SCPs)",
    "Description": "Implement SCPs across AWS Organizations to limit the maximum allowable permissions for member accounts or organizational units.",
    "Applicability": "All AWS Organization member accounts",
    "Security Risk": "Without SCPs, organizational units might exceed their intended permissions, leading to potential security vulnerabilities across multiple accounts.",
    "Default Behavior / Limitations": "SCPs must be explicitly configured within AWS Organizations.",
    "Automation": "Manage SCPs using AWS Organizations Console or through AWS CLI for enforcing organization-wide policies.",
    "References": [
      "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html"
    ]
  },
  {
    "Title": "Limit Permissions with Resource Control Policies (RCPs)",
    "Description": "Configure RCPs to restrict permissions across AWS resources, including those outside of organizational boundaries, maintaining stringent access control.",
    "Applicability": "Applicable to cross-account or external resource access",
    "Security Risk": "Lack of RCPs can result in unauthorized cross-account access that might not align with organizational security practices.",
    "Default Behavior / Limitations": "RCPs require explicit definition; they are not innate within AWS two-account communications.",
    "Automation": "Manage RCPs using AWS IAM policies and cross-account resource sharing setups.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-control-access.html"
    ]
  },
  {
    "Title": "Manage Session Policies for Temporary Access",
    "Description": "Utilize session policies to define permissions for temporary sessions during role assumption or federation, ensuring proper intersection with existing policies.",
    "Applicability": "Roles and federated identities using temporary credentials",
    "Security Risk": "Without controls on session policies, temporary access can lead to permission slip-ups either providing excessive access or lacking needed permissions.",
    "Default Behavior / Limitations": "Session policies have to be purposely defined and used.",
    "Automation": "Session policies can be configured and enforced via AWS STS operations when defining temporary credential parameters.",
    "References": [
      "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_policy-summary.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 4
```json
[
  {
    "Title": "Enforce TLS 1.2 or Later with PFS for AWS Application Migration Service",
    "Description": "Configure network settings to ensure connections to AWS Application Migration Service use TLS 1.2 or later with cipher suites that support Perfect Forward Secrecy (PFS) such as DHE or ECDHE.",
    "Applicability": "All network clients accessing AWS Application Migration Service",
    "Security Risk": "Using protocols or cipher suites that do not support PFS can lead to potential breaches where past communications could be decrypted if the server's private key is compromised.",
    "Default Behavior / Limitations": "TLS 1.2 and later supporting PFS is typically supported by modern systems; however, it must be enforced in client configurations.",
    "Automation": "Manual validation required to ensure network policy enforcement as AWS does not control client-side configurations.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/infrastructure-security.html"
    ]
  },
  {
    "Title": "Sign All Requests Using AWS STS or IAM Credentials",
    "Description": "Ensure all requests to AWS Application Migration Service are signed using AWS Security Token Service (STS) or credentials associated with an IAM principal.",
    "Applicability": "All requests to AWS Application Migration Service",
    "Security Risk": "Unsigned requests could lead to unauthorized access, data leaks, or unauthorized modifications.",
    "Default Behavior / Limitations": "AWS services automatically require signed API requests.",
    "Automation": "Enforced by AWS SDKs and AWS CLI, which automatically sign API requests using AWS credentials.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/infrastructure-security.html"
    ]
  },
  {
    "Title": "Automate Access Key Deletion after AWS Replication Agent Installation",
    "Description": "Use IAM permission boundaries and aws:CurrentTime global context key to automate the expiration and deletion of AWS access keys after AWS Replication Agent installation and migration completion.",
    "Applicability": "All AWS Application Migration Service installations",
    "Security Risk": "Residual access keys not deleted could be misused, leading to unauthorized access.",
    "Default Behavior / Limitations": "Keys are deleted from source servers upon disconnection but customer action is required for any remaining keys.",
    "Automation": "Can be enforced using IAM policies with time-based conditions.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/infrastructure-security.html"
    ]
  },
  {
    "Title": "Use Amazon EBS Encryption for Data Security",
    "Description": "Enable Amazon EBS encryption for all EBS volumes used by AWS Application Migration Service to ensure data is protected at rest.",
    "Applicability": "All EBS volumes used by AWS Application Migration Service",
    "Security Risk": "Unencrypted data at rest can be accessed if compromised, leading to information exposure.",
    "Default Behavior / Limitations": "Amazon EBS encryption is not enabled by default.",
    "Automation": "Can be enforced using AWS Config rule `ebs-encrypted-volumes`.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/infrastructure-security.html"
    ]
  },
  {
    "Title": "Minimize Public Internet Exposure for Replication Servers",
    "Description": "Configure security groups and use VPN connections to minimize replication servers' exposure to the public internet, allowing access only from specific IP addresses.",
    "Applicability": "Replication servers in AWS Application Migration Service",
    "Security Risk": "Servers exposed to the public internet are vulnerable to unauthorized access and attacks.",
    "Default Behavior / Limitations": "Default security group settings may allow broader access than intended; proper configuration is essential.",
    "Automation": "Can be enforced using AWS Security Hub and AWS Config to check security group configurations.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/infrastructure-security.html"
    ]
  },
  {
    "Title": "Ensure 'aws-replication' User Has Necessary Permissions",
    "Description": "The 'aws-replication' user on the Linux source server must have permissions to read and write to block devices necessary for AWS Application Migration Service operations.",
    "Applicability": "Linux source servers within AWS Application Migration Service",
    "Security Risk": "Insufficient permissions may disrupt migration operations, leading to data integrity issues.",
    "Default Behavior / Limitations": "AWS creates the 'aws-replication' user but configuring permissions must be performed manually.",
    "Automation": "Manual validation required to set the correct permissions.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/infrastructure-security.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 5
```json
[
  {
    "Title": "Enforce Use of aws:SourceArn and aws:SourceAccount in Resource Policies for AWS Application Migration Service",
    "Description": "Ensure that resource policies for AWS Application Migration Service include both `aws:SourceArn` and `aws:SourceAccount` global condition context keys. These keys should be used to limit permissions and prevent cross-service confused deputy problems by verifying that the `aws:SourceAccount` matches the account ID specified in the `aws:SourceArn`.",
    "Applicability": "AWS Application Migration Service resource policies",
    "Security Risk": "Without proper constraints using `aws:SourceArn` and `aws:SourceAccount`, services may become vulnerable to the confused deputy problem, leading to potential unauthorized access and privilege escalation by malicious actors.",
    "Default Behavior / Limitations": "AWS does not enforce the use of `aws:SourceArn` and `aws:SourceAccount` by default in resource policies.",
    "Automation": "Can be audited using AWS Config rule `custom-resource-policies-audit` to ensure that policies include these conditions.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/cross-service-confused-deputy-prevention.html"
    ]
  },
  {
    "Title": "Restrict aws:SourceArn for AWS Application Migration Service to Specific ARN Structure",
    "Description": "For policies related to AWS Application Migration Service, set the `aws:SourceArn` value to 'arn:aws:mgn:*:123456789012:source-server/*'. This ensures that policies have a specified and expected structure to limit the conditions in place.",
    "Applicability": "AWS Application Migration Service policies",
    "Security Risk": "Incorrect ARN patterns may bypass policy conditions, allowing potential misuse of cross-service permissions and leading to unauthorized access.",
    "Default Behavior / Limitations": "The service does not mandate this specific ARN pattern by default; it needs manual configuration.",
    "Automation": "Can be enforced through custom AWS Config rules that check for the specific ARN pattern in policy conditions.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/cross-service-confused-deputy-prevention.html"
    ]
  },
  {
    "Title": "Implement Full ARN in aws:SourceArn for Confused Deputy Protection",
    "Description": "Configure policies to use `aws:SourceArn` with the complete ARN of the resource when protecting against the confused deputy problem. If the full ARN is unknown, consider using wildcards judiciously for unknown segments.",
    "Applicability": "All AWS services using resource policies susceptible to confused deputy problems",
    "Security Risk": "Incomplete ARN specifications can leave room for exploitation, allowing unauthorized services to access resources by exploiting policy loopholes.",
    "Default Behavior / Limitations": "AWS does not automatically verify ARN completeness in `aws:SourceArn`, requiring manual validation.",
    "Automation": "Audit using AWS Config custom rules designed to enforce the presence of a full ARN in resource policies.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/cross-service-confused-deputy-prevention.html"
    ]
  }
]
```

### ControlGen Output - Arquivo 6
```json
[
  {
    "Title": "Automatic Creation of Service-Linked Role for AWS Application Migration Service",
    "Description": "AWS Application Migration Service automatically creates the service-linked role `AWSServiceRoleForApplicationMigrationService` when configuring the Replication Configuration Template. This role is managed by AWS, eliminating the need for manual role creation.",
    "Applicability": "AWS Application Migration Service users",
    "Security Risk": "Manual role creation could introduce configuration errors, leading to potential security flaws or service outages.",
    "Default Behavior / Limitations": "The service-linked role is automatically created by AWS, and users cannot alter this behavior.",
    "Automation": "This control is enforced automatically by AWS when using the service. Monitoring is not required.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/using-service-linked-roles.html"
    ]
  },
  {
    "Title": "Immutable Name for AWS Service-Linked Role",
    "Description": "The name of the service-linked role `AWSServiceRoleForApplicationMigrationService` cannot be modified after creation, though its description can be edited.",
    "Applicability": "AWS Application Migration Service users",
    "Security Risk": "Changing role names can disrupt service operations and lead to unauthorized access if not tracked correctly.",
    "Default Behavior / Limitations": "AWS enforces this restriction automatically, maintaining role integrity.",
    "Automation": "AWS manages this automatically, and no configuration is needed from the user.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/using-service-linked-roles.html"
    ]
  },
  {
    "Title": "Service-Linked Role Permissions Management",
    "Description": "The `AWSServiceRoleForApplicationMigrationService` includes permissions for services like EC2, IAM, KMS, and Organizations. It assumes trust for `mgn.amazonaws.com` and contains various permissions related to AWS resources.",
    "Applicability": "AWS Application Migration Service users",
    "Security Risk": "Incorrect permissions could allow unauthorized actions on AWS resources, impacting confidentiality, integrity, or availability.",
    "Default Behavior / Limitations": "Permission updates on service-linked roles are managed by AWS.",
    "Automation": "AWS manages role permissions automatically. Users should review IAM policies regularly.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/using-service-linked-roles.html"
    ]
  },
  {
    "Title": "Conditional Deletion of Service-Linked Role",
    "Description": "Before deleting the `AWSServiceRoleForApplicationMigrationService`, all associated AWS resources (waves, applications, source servers, and jobs) must be cleaned up in every AWS region to ensure permissions are not inadvertently removed.",
    "Applicability": "AWS Application Migration Service users",
    "Security Risk": "Premature deletion of the service-linked role can lead to orphaned resources and unintentional data exposure or loss.",
    "Default Behavior / Limitations": "AWS does not automatically handle the cleanup of associated resources before role deletion.",
    "Automation": "Manual validation is required to ensure all resources are removed before role deletion.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/using-service-linked-roles.html"
    ]
  },
  {
    "Title": "Restriction of EC2 Actions Based on Resource Tagging",
    "Description": "The permissions policy for `AWSServiceRoleForApplicationMigrationService` allows actions like `StartInstances`, `StopInstances`, and `TerminateInstances` on EC2, except when the resource tag `AWSApplicationMigrationServiceManaged` is true.",
    "Applicability": "AWS Application Migration Service users",
    "Security Risk": "Allowing unrestricted actions on EC2 instances can lead to unauthorized changes affecting system availability and data integrity.",
    "Default Behavior / Limitations": "Tag-based permissions are enforced automatically within the role's policy.",
    "Automation": "AWS IAM policies inherently support this through policy definitions. Monitoring through AWS Config for compliance is recommended.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/using-service-linked-roles.html"
    ]
  },
  {
    "Title": "Conditional EC2 Resource Creation by Request Tags",
    "Description": "The `AWSServiceRoleForApplicationMigrationService` includes permissions to create EC2 resources such as volumes and security groups, with conditions based on request tags.",
    "Applicability": "AWS Application Migration Service users",
    "Security Risk": "Unrestricted resource creation can lead to misconfigurations or unexpected costs impacting the security and budget of the organization.",
    "Default Behavior / Limitations": "Request tag conditioning is natively supported in IAM and enforced by AWS.",
    "Automation": "AWS IAM policies enable this control inherently. Additional monitoring can be configured using AWS Config.",
    "References": [
      "https://docs.aws.amazon.com/mgn/latest/ug/using-service-linked-roles.html"
    ]
  }
]
```