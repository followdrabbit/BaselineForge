# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/servicecatalog/latest/adminguide/using-service-linked-roles.html'}

[](/pdfs/servicecatalog/latest/adminguide/service-catalog-ag.pdf#using-
service-linked-roles "Open PDF")

[Documentation](/index.html)[AWS Service
Catalog](/servicecatalog/index.html)[Administrator Guide](introduction.html)

Service-linked role permissions for
AWSServiceRoleForServiceCatalogSyncService-linked role permissions for
AWSServiceRoleForServiceCatalogOrgsDataSyncEditing a service-linked role for
AWS Service CatalogDeleting a service-linked role for AWS Service
CatalogSupported regions for AWS Service Catalog service-linked roles

# Using service-linked roles for AWS Service Catalog

AWS Service Catalog uses AWS Identity and Access Management (IAM)[ service-
linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-
and-concepts.html#iam-term-service-linked-role). A service-linked role is a
unique type of IAM role that is linked directly to AWS Service Catalog.
Service-linked roles are predefined by AWS Service Catalog and include all the
permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up AWS Service Catalog easier because you
donât have to manually add the necessary permissions. AWS Service Catalog
defines the permissions of its service-linked roles, and unless defined
otherwise, only AWS Service Catalog can assume its roles. The defined
permissions include the trust policy and the permissions policy, and that
permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related
resources. This protects your AWS Service Catalog resources because you can't
inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see
[AWS Services That Work with
IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-
that-work-with-iam.html) and look for the services that have **Yes** in the
**Service-linked roles** column. Choose a **Yes** with a link to view the
service-linked role documentation for that service.

## Service-linked role permissions for `AWSServiceRoleForServiceCatalogSync`

AWS Service Catalog can use the service-linked role named
**`AWSServiceRoleForServiceCatalogSync`** â This service-linked role is
required for AWS Service Catalog to use CodeConnections and to create, update,
and describe AWS Service Catalog Provisioning Artifacts for a product.

The `AWSServiceRoleForServiceCatalogSync` service-linked role trusts the
following services to assume the role:

  * `sync.servicecatalog.amazonaws.com`

The role permissions policy named **AWSServiceCatalogSyncServiceRolePolicy**
allows AWS Service Catalog to complete the following actions on the specified
resources:

  * Action: `Connection` on `CodeConnections`

  * Action: `Create, Update, and Describe` on `ProvisioningArtifact` for a AWS Service Catalog product

You must configure permissions to allow an IAM entity (such as a user, group,
or role) to create, edit, or delete a service-linked role. For more
information, see [Service-linked role
permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-
linked-roles.html#service-linked-role-permissions) in the _IAM User Guide_.

### Creating the `AWSServiceRoleForServiceCatalogSync` service-linked role

You do not need to manually create the ``AWSServiceRoleForServiceCatalogSync``
service-linked role. AWS Service Catalog creates the service-linked role for
you automatically when you establish CodeConnections in the AWS Management
Console, the AWS CLI, or the AWS API.

###### Important

This service-linked role can appear in your account if you completed an action
in another service that uses the features supported by this role. Also, if you
were using the AWS Service Catalog service before November 18, 2022, when it
began supporting service-linked roles, then AWS Service Catalog created the
`AWSServiceRoleForServiceCatalogSync` role in your account. To learn more, see
[A new role appeared in my IAM
account](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_roles.html#troubleshoot_roles_new-
role-appeared).

If you delete this service-linked role, and then need to create it again, you
can use the same process to recreate the role in your account. When you
establish CodeConnections, AWS Service Catalog creates the service-linked role
for you again.

You can also use the IAM console to create a service-linked role with the
**synced AWS Service Catalog Products** use case. In the AWS CLI or the AWS
API, create a service-linked role with the `sync.servicecatalog.amazonaws.com`
service name. For more information, see [Creating a service-linked
role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-
roles.html#create-service-linked-role) in the _IAM User Guide_. If you delete
this service-linked role, you can use this same process to create the role
again.

## Service-linked role permissions for
`AWSServiceRoleForServiceCatalogOrgsDataSync`

AWS Service Catalog can use the service-linked role named
**`AWSServiceRoleForServiceCatalogOrgsDataSync`** â This service-linked role
is required for AWS Service Catalog organizations to stay in sync with AWS
Organizations.

The `AWSServiceRoleForServiceCatalogOrgsDataSync` service-linked role trusts
the following services to assume the role:

  * `orgsdatasync.servicecatalog.amazonaws.com`

The `AWSServiceRoleForServiceCatalogOrgsDataSync` service-linked role requires
that you use the following trust policy in addition to the
`AWSServiceCatalogOrgsDataSyncServiceRolePolicy` [managed policy](./security-
iam-awsmanpol.html#security-iam-awsmanpol-
AWSServiceCatalogOrgsDataSyncServiceRolePolicy):

    
    
    { 
      "Version": "2012-10-17", 
      "Statement": [ 
        { 
          "Effect": "Allow", 
          "Principal": { 
            "Service": "orgsdatasync.servicecatalog.amazonaws.com" 
          }, 
          "Action": "sts:AssumeRole" 
        } 
      ] 
    }
          

The role permissions policy named
**AWSServiceCatalogOrgsDataSyncServiceRolePolicy** allows AWS Service Catalog
to complete the following actions on the specified resources:

  * Action: `DescribeAccount`, `DescribeOrganization`, and `ListAWSServiceAccessForOrganization` on `Organizations accounts`

  * Action: `ListAccounts`, `ListChildren`, and `ListParent` on `Organizations accounts`

You must configure permissions to allow an IAM entity (such as a user, group,
or role) to create, edit, or delete a service-linked role. For more
information, see [Service-linked role
permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-
linked-roles.html#service-linked-role-permissions) in the _IAM User Guide_.

### Creating the `AWSServiceRoleForServiceCatalogOrgsDataSync` service-linked
role

You do not need to manually create the
``AWSServiceRoleForServiceCatalogOrgsDataSync``service-linked role. AWS
Service Catalog considers your action of enabling [Sharing with AWS
Organizations](./catalogs_portfolios_sharing_how-to-share.html#portfolio-
sharing-organizations) or [Sharing a
Portfolio](./catalogs_portfolios_sharing_how-to-share.html) as permission for
AWS Service Catalog to create a SLR in the background on your behalf.

AWS Service Catalog creates the service-linked role for you automatically when
you request `EnableAWSOrganizationsAccess` or `CreatePortfolioShare` in the
AWS Management Console, the AWS CLI, or the AWS API.

###### Important

This service-linked role can appear in your account if you completed an action
in another service that uses the features supported by this role. To learn
more, see [A new role appeared in my IAM
account](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_roles.html#troubleshoot_roles_new-
role-appeared).

If you delete this service-linked role, and then need to create it again, you
can use the same process to recreate the role in your account. When you
request `EnableAWSOrganizationsAccess` or `CreatePortfolioShare`, AWS Service
Catalog creates the service-linked role for you again.

## Editing a service-linked role for AWS Service Catalog

AWS Service Catalog does not allow you to edit the
`AWSServiceRoleForServiceCatalogSync` or
`AWSServiceRoleForServiceCatalogOrgsDataSync` service-linked roles. After you
create a service-linked role, you cannot change the name of the role because
various entities might reference the role. However, you can edit the
description of the role using IAM. For more information, see [Editing a
service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-
service-linked-roles.html#edit-service-linked-role) in the _IAM User Guide_.

## Deleting a service-linked role for AWS Service Catalog

You can use the IAM console, the AWS CLI, or the AWS API to manually delete
the `AWSServiceRoleForServiceCatalogSync` or
`AWSServiceRoleForServiceCatalogOrgsDataSync` SLR. To do this, you must first
manually remove all resources that are using the service-linked role (for
example, any AWS Service Catalog products that are synced to an external
repository), and then the service-linked role can be manually deleted.

## Supported regions for AWS Service Catalog service-linked roles

AWS Service Catalog supports using service-linked roles in all of the regions
where the service is available. For more information, see [AWS regions and
endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html).

Region name | Region identity | Support in AWS Service Catalog  
---|---|---  
US East (N. Virginia) | us-east-1 | Yes  
US East (Ohio) | us-east-2 | Yes  
US West (N. California) | us-west-1 | Yes  
US West (Oregon) | us-west-2 | Yes  
Africa (Cape Town) | af-south-1 | Yes  
Asia Pacific (Hong Kong) | ap-east-1 | Yes  
Asia Pacific (Jakarta) | ap-southeast-3 | Yes  
Asia Pacific (Mumbai) | ap-south-1 | Yes  
Asia Pacific (Osaka) | ap-northeast-3 | Yes  
Asia Pacific (Seoul) | ap-northeast-2 | Yes  
Asia Pacific (Singapore) | ap-southeast-1 | Yes  
Asia Pacific (Sydney) | ap-southeast-2 | Yes  
Asia Pacific (Tokyo) | ap-northeast-1 | Yes  
Canada (Central) | ca-central-1 | Yes  
Europe (Frankfurt) | eu-central-1 | Yes  
Europe (Ireland) | eu-west-1 | Yes  
Europe (London) | eu-west-2 | Yes  
Europe (Milan) | eu-south-1 | Yes  
Europe (Paris) | eu-west-3 | Yes  
Europe (Stockholm) | eu-north-1 | Yes  
Middle East (Bahrain) | me-south-1 | Yes  
South America (SÃ£o Paulo) | sa-east-1 | Yes  
AWS GovCloud (US-East) | us-gov-east-1 | No  
AWS GovCloud (US-West) | us-gov-west-1 | No  
  
![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

AWS managed policies

Troubleshooting AWS Service Catalog identity and access

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

