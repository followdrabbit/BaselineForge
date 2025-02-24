# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.RDSSecurityGroups.html'}

[](/pdfs/AmazonRDS/latest/AuroraUserGuide/aurora-
ug.pdf#Overview.RDSSecurityGroups "Open PDF")

[Documentation](/index.html)[Amazon RDS](/rds/index.html)[User Guide for
Aurora](CHAP_AuroraOverview.html)

Overview of VPC security groupsSecurity group scenarioCreating a VPC security
groupAssociating with a DB cluster

# Controlling access with security groups

VPC security groups control the access that traffic has in and out of a DB
cluster. By default, network access is turned off for a DB cluster. You can
specify rules in a security group that allow access from an IP address range,
port, or security group. After ingress rules are configured, the same rules
apply to all DB clusters that are associated with that security group. You can
specify up to 20 rules in a security group.

## Overview of VPC security groups

Each VPC security group rule makes it possible for a specific source to access
a DB cluster in a VPC that is associated with that VPC security group. The
source can be a range of addresses (for example, 203.0.113.0/24), or another
VPC security group. By specifying a VPC security group as the source, you
allow incoming traffic from all instances (typically application servers) that
use the source VPC security group. VPC security groups can have rules that
govern both inbound and outbound traffic. However, the outbound traffic rules
typically don't apply to DB clusters. Outbound traffic rules apply only if the
DB cluster acts as a client. You must use the [Amazon EC2
API](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Welcome.html) or
the **Security Group** option on the VPC console to create VPC security
groups.

When you create rules for your VPC security group that allow access to the
clusters in your VPC, you must specify a port for each range of addresses that
the rule allows access for. For example, if you want to turn on Secure Shell
(SSH) access for instances in the VPC, create a rule allowing access to TCP
port 22 for the specified range of addresses.

You can configure multiple VPC security groups that allow access to different
ports for different instances in your VPC. For example, you can create a VPC
security group that allows access to TCP port 80 for web servers in your VPC.
You can then create another VPC security group that allows access to TCP port
3306 for Aurora MySQL DB instances in your VPC.

###### Note

In an Aurora DB cluster, the VPC security group associated with the DB cluster
is also associated with all of the DB instances in the DB cluster. If you
change the VPC security group for the DB cluster or for a DB instance, the
change is applied automatically to all of the DB instances in the DB cluster.

For more information on VPC security groups, see [Security
groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)
in the _Amazon Virtual Private Cloud User Guide_.

###### Note

If your DB cluster is in a VPC but isn't publicly accessible, you can also use
an AWS Site-to-Site VPN connection or an AWS Direct Connect connection to
access it from a private network. For more information, see [Internetwork
traffic privacy](./inter-network-traffic-privacy.html).

## Security group scenario

A common use of a DB cluster in a VPC is to share data with an application
server running in an Amazon EC2 instance in the same VPC, which is accessed by
a client application outside the VPC. For this scenario, you use the RDS and
VPC pages on the AWS Management Console or the RDS and EC2 API operations to
create the necessary instances and security groups:

  1. Create a VPC security group (for example, `sg-0123ec2example`) and define inbound rules that use the IP addresses of the client application as the source. This security group allows your client application to connect to EC2 instances in a VPC that uses this security group.

  2. Create an EC2 instance for the application and add the EC2 instance to the VPC security group (`sg-0123ec2example`) that you created in the previous step.

  3. Create a second VPC security group (for example, `sg-6789rdsexample`) and create a new rule by specifying the VPC security group that you created in step 1 (`sg-0123ec2example`) as the source.

  4. Create a new DB cluster and add the DB cluster to the VPC security group (`sg-6789rdsexample`) that you created in the previous step. When you create the DB cluster, use the same port number as the one specified for the VPC security group (`sg-6789rdsexample`) rule that you created in step 3.

The following diagram shows this scenario.

![DB cluster and EC2 instance in a
VPC](/images/AmazonRDS/latest/AuroraUserGuide/images/con-VPC-sec-grp-
aurora.png)

For detailed instructions about configuring a VPC for this scenario, see
[Tutorial: Create a VPC for use with a DB cluster (IPv4
only)](./CHAP_Tutorials.WebServerDB.CreateVPC.html). For more information
about using a VPC, see [Amazon VPC and Amazon Aurora](./USER_VPC.html).

## Creating a VPC security group

You can create a VPC security group for a DB instance by using the VPC
console. For information about creating a security group, see [Provide access
to the DB cluster in the VPC by creating a security
group](./CHAP_SettingUp_Aurora.html#CHAP_SettingUp_Aurora.SecurityGroup) and
[Security
groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)
in the _Amazon Virtual Private Cloud User Guide_.

## Associating a security group with a DB cluster

You can associate a security group with a DB cluster by using **Modify
cluster** on the RDS console, the `ModifyDBCluster` Amazon RDS API, or the
`modify-db-cluster` AWS CLI command.

The following CLI example associates a specific VPC group and removes DB
security groups from the DB cluster

    
    
    aws rds modify-db-cluster --db-cluster-identifier dbName --vpc-security-group-ids sg-ID

For information about modifying a DB cluster, see [Modifying an Amazon Aurora
DB cluster](./Aurora.Modifying.html).

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Security best practices

Master user account privileges

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

