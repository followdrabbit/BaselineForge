# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL-certificate-rotation.html'}

[](/pdfs/AmazonRDS/latest/AuroraUserGuide/aurora-ug.pdf#UsingWithRDS.SSL-
certificate-rotation "Open PDF")

[Documentation](/index.html)[Amazon RDS](/rds/index.html)[User Guide for
Aurora](CHAP_AuroraOverview.html)

Considerations for rotating certificatesUpdating your CA certificate by
modifying your DB instance Updating your CA certificate by applying
maintenanceServer certificate rotationSample script for importing certificates

# Rotating your SSL/TLS certificate

Amazon RDS Certificate Authority certificates rds-ca-2019 expired in August,
2024. If you use or plan to use Secure Sockets Layer (SSL) or Transport Layer
Security (TLS) with certificate verification to connect to your RDS DB
instances , consider using one of the new CA certificates rds-ca-rsa2048-g1,
rds-ca-rsa4096-g1 or rds-ca-ecc384-g1. If you currently do not use SSL/TLS
with certificate verification, you might still have an expired CA certificate
and must update them to a new CA certificate if you plan to use SSL/TLS with
certificate verification to connect to your RDS databases.

Amazon RDS provides new CA certificates as an AWS security best practice. For
information about the new certificates and the supported AWS Regions, see
[Using SSL/TLS to encrypt a connection to a DB
cluster](./UsingWithRDS.SSL.html).

To update the CA certificate for your database, use the following methods:

  * Updating your CA certificate by modifying your DB instance 

  * Updating your CA certificate by applying maintenance

Before you update your DB instances to use the new CA certificate, make sure
that you update your clients or applications connecting to your RDS databases.

## Considerations for rotating certificates

Consider the following situations before rotating your certificate:

  * Amazon RDS Proxy and Aurora Serverless v1 use certificates from the AWS Certificate Manager (ACM). If you're using RDS Proxy, when you rotate your SSL/TLS certificate, you don't need to update applications that use RDS Proxy connections. For more information, see [Using TLS/SSL with RDS Proxy](./rds-proxy.howitworks.html#rds-proxy-security.tls).

  * If you're using Aurora Serverless v1, downloading Amazon RDS certificates isn't required. For more information, see [Using TLS/SSL with Aurora Serverless v1](./aurora-serverless.html#aurora-serverless.tls).

  * If you're using a Go version 1.15 application with a DB instance that was created or updated to the rds-ca-2019 certificate prior to July 28, 2020, you must update the certificate again. Update the certificate to rds-ca-rsa2048-g1, rds-ca-rsa4096-g1, or rds-ca-ecc384-g1 depending on your engine. 

Use the `modify-db-instance` command , using the new CA certificate
identifier. You can find the CAs that are available for a specific DB engine
and DB engine version using the `describe-db-engine-versions` command.

If you created your database or updated its certificate after July 28, 2020,
no action is required. For more information, see [Go GitHub issue
#39568](https://github.com/golang/go/issues/39568).

## Updating your CA certificate by modifying your DB instance

The following example updates your CA certificate from _rds-ca-2019_ to _rds-
ca-rsa2048-g1_. You can choose a different certificate. For more information,
see [Certificate
authorities](./UsingWithRDS.SSL.html#UsingWithRDS.SSL.RegionCertificateAuthorities).

Update your application trust store to reduce any down time associated with
updating your CA certificate. For more information about restarts associated
with CA certificate rotation, see Automatic server certificate rotation.

###### To update your CA certificate by modifying your DB instance

  1. Download the new SSL/TLS certificate as described in [Using SSL/TLS to encrypt a connection to a DB cluster](./UsingWithRDS.SSL.html).

  2. Update your applications to use the new SSL/TLS certificate.

The methods for updating applications for new SSL/TLS certificates depend on
your specific applications. Work with your application developers to update
the SSL/TLS certificates for your applications.

For information about checking for SSL/TLS connections and updating
applications for each DB engine, see the following topics:

     * [Updating applications to connect to Aurora MySQL DB clusters using new TLS certificates](./ssl-certificate-rotation-aurora-mysql.html)

     * [Updating applications to connect to Aurora PostgreSQL DB clusters using new SSL/TLS certificates](./ssl-certificate-rotation-aurora-postgresql.html)

For a sample script that updates a trust store for a Linux operating system,
see Sample script for importing certificates into your trust store.

###### Note

The certificate bundle contains certificates for both the old and new CA, so
you can upgrade your application safely and maintain connectivity during the
transition period. If you are using the AWS Database Migration Service to
migrate a database to a DB cluster, we recommend using the certificate bundle
to ensure connectivity during the migration.

  3. Modify the DB instance to change the CA from **rds-ca-2019** to **rds-ca-rsa2048-g1**. To check if your database requires a restart to update the CA certificates, use the [describe-db-engine-versions](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-engine-versions.html) command and check the `SupportsCertificateRotationWithoutRestart` flag. 

###### Note

Reboot your Babelfish cluster after modifying to update the CA certificate.

###### Important

If you are experiencing connectivity issues after certificate expiry, use the
apply immediately option by specifying **Apply immediately** in the console or
by specifying the `--apply-immediately` option using the AWS CLI. By default,
this operation is scheduled to run during your next maintenance window.

To set an override for your cluster CA that's different from the default RDS
CA, use the [modify-
certificates](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-
certificates.html) CLI command.

You can use the AWS Management Console or the AWS CLI to change the CA
certificate from **rds-ca-2019** to **rds-ca-rsa2048-g1** for a DB instance .

Console

    

  1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

  2. In the navigation pane, choose **Databases** , and then choose the DB instance that you want to modify. 

  3. Choose **Modify**.

![Modify DB instance](/images/AmazonRDS/latest/AuroraUserGuide/images/ssl-
rotate-cert-modify-aurora.png)

  4. In the **Connectivity** section, choose **rds-ca-rsa2048-g1**.

![Choose CA certificate](/images/AmazonRDS/latest/AuroraUserGuide/images/ssl-
rotate-cert-ca-rsa2048-g1.png)

  5. Choose **Continue** and check the summary of modifications. 

  6. To apply the changes immediately, choose **Apply immediately**.

  7. On the confirmation page, review your changes. If they are correct, choose **Modify DB Instance** to save your changes. 

###### Important

When you schedule this operation, make sure that you have updated your client-
side trust store beforehand.

Or choose **Back** to edit your changes or **Cancel** to cancel your changes.

AWS CLI

    

To use the AWS CLI to change the CA from **rds-ca-2019** to **rds-ca-
rsa2048-g1** for a DB instance , call the [modify-db-
instance](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-
instance.html) or [modify-db-
cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-
cluster.html) command. Specify the DB instance identifier and the `--ca-
certificate-identifier` option.

Use the `--apply-immediately` parameter to apply the update immediately. By
default, this operation is scheduled to run during your next maintenance
window.

###### Important

When you schedule this operation, make sure that you have updated your client-
side trust store beforehand.

The following example modifies `mydbinstance` by setting the CA certificate to
`rds-ca-rsa2048-g1`.

For Linux, macOS, or Unix:

    
    
    aws rds modify-db-instance \
        --db-instance-identifier mydbinstance \
        --ca-certificate-identifier rds-ca-rsa2048-g1 

For Windows:

    
    
    aws rds modify-db-instance ^
        --db-instance-identifier mydbinstance ^
        --ca-certificate-identifier rds-ca-rsa2048-g1

###### Note

If your instance requires reboot, you can use the [modify-db-
instance](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-
instance.html) CLI command and specify the `--no-certificate-rotation-restart`
option.

## Updating your CA certificate by applying maintenance

Perform the following steps to update your CA certificate by applying
maintenance.

Console

    

###### To update your CA certificate by applying maintenance

  1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

  2. In the navigation pane, choose **Certificate update**.

![Certificate rotation navigation pane
option](/images/AmazonRDS/latest/AuroraUserGuide/images/ssl-rotate-cert-
certupdate.png)

The **Databases requiring certificate update** page appears.

![Update CA certificate for
database](/images/AmazonRDS/latest/AuroraUserGuide/images/ssl-rotate-cert-
update-multiple.png)

###### Note

This page only shows the DB instances for the current AWS Region. If you have
databases in more than one AWS Region, check this page in each AWS Region to
see all DB instances with old SSL/TLS certificates.

  3. Choose the DB instance that you want to update.

You can schedule the certificate rotation for your next maintenance window by
choosing **Schedule**. Apply the rotation immediately by choosing **Apply
now**.

###### Important

If you experience connectivity issues after certificate expiry, use the
**Apply now** option.

  4.     1. If you choose **Schedule** , you are prompted to confirm the CA certificate rotation. This prompt also states the scheduled window for your update. 

![Confirm certificate
rotation](/images/AmazonRDS/latest/AuroraUserGuide/images/ssl-rotate-cert-
confirm-schedule.png)

    2. If you choose **Apply now** , you are prompted to confirm the CA certificate rotation.

![Confirm certificate
rotation](/images/AmazonRDS/latest/AuroraUserGuide/images/ssl-rotate-cert-
confirm-now.png)

###### Important

Before scheduling the CA certificate rotation on your database, update any
client applications that use SSL/TLS and the server certificate to connect.
These updates are specific to your DB engine. After you have updated these
client applications, you can confirm the CA certificate rotation.

To continue, choose the check box, and then choose **Confirm**.

  5. Repeat steps 3 and 4 for each DB instance that you want to update.

## Automatic server certificate rotation

If your root CA supports automatic server certificate rotation, RDS
automatically handles the rotation of the DB server certificate. RDS uses the
same root CA for this automatic rotation, so you don't need to download a new
CA bundle. See [Certificate
authorities](./UsingWithRDS.SSL.html#UsingWithRDS.SSL.RegionCertificateAuthorities).

The rotation and validity of your DB server certificate depend on your DB
engine:

  * If your DB engine supports rotation without restart, RDS automatically rotates the DB server certificate without requiring any action from you. RDS attempts to rotate your DB server certificate in your preferred maintenance window at the DB server certificate half life. The new DB server certificate is valid for 12 months.

  * If your DB engine doesn't support rotation without restart, RDS notifies you about a maintenance event at least 6 months before the DB server certificate expires. The new DB server certificate is valid for 36 months.

Use the [ describe-db-engine-
versions](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-
engine-versions.html) command and inspect the
`SupportsCertificateRotationWithoutRestart` flag to identify whether the DB
engine version supports rotating the certificate without restart. For more
information, see [Setting the CA for your
database](./UsingWithRDS.SSL.html#UsingWithRDS.SSL.RegionCertificateAuthorities.Selection).

## Sample script for importing certificates into your trust store

The following are sample shell scripts that import the certificate bundle into
a trust store.

Each sample shell script uses keytool, which is part of the Java Development
Kit (JDK). For information about installing the JDK, see [ JDK Installation
Guide](https://docs.oracle.com/en/java/javase/17/install/overview-jdk-
installation.html).

Linux

    

The following is a sample shell script that imports the certificate bundle
into a trust store on a Linux operating system.

    
    
    mydir=tmp/certs
    if [ ! -e "${mydir}" ]
    then
    mkdir -p "${mydir}"
    fi
    
    truststore=${mydir}/rds-truststore.jks
    storepassword=changeit
    
    curl -sS "https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem" > ${mydir}/global-bundle.pem
    awk 'split_after == 1 {n++;split_after=0} /-----END CERTIFICATE-----/ {split_after=1}{print > "rds-ca-" n+1 ".pem"}' < ${mydir}/global-bundle.pem
    
    for CERT in rds-ca-*; do
      alias=$(openssl x509 -noout -text -in $CERT | perl -ne 'next unless /Subject:/; s/.*(CN=|CN = )//; print')
      echo "Importing $alias"
      keytool -import -file ${CERT} -alias "${alias}" -storepass ${storepassword} -keystore ${truststore} -noprompt
      rm $CERT
    done
    
    rm ${mydir}/global-bundle.pem
    
    echo "Trust store content is: "
    
    keytool -list -v -keystore "$truststore" -storepass ${storepassword} | grep Alias | cut -d " " -f3- | while read alias 
    do
       expiry=`keytool -list -v -keystore "$truststore" -storepass ${storepassword} -alias "${alias}" | grep Valid | perl -ne 'if(/until: (.*?)\n/) { print "$1\n"; }'`
       echo " Certificate ${alias} expires in '$expiry'" 
    done
                    

macOS

    

The following is a sample shell script that imports the certificate bundle
into a trust store on macOS.

    
    
    mydir=tmp/certs
    if [ ! -e "${mydir}" ]
    then
    mkdir -p "${mydir}"
    fi
    
    truststore=${mydir}/rds-truststore.jks
    storepassword=changeit
    
    curl -sS "https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem" > ${mydir}/global-bundle.pem
    split -p "-----BEGIN CERTIFICATE-----" ${mydir}/global-bundle.pem rds-ca-
    
    for CERT in rds-ca-*; do
      alias=$(openssl x509 -noout -text -in $CERT | perl -ne 'next unless /Subject:/; s/.*(CN=|CN = )//; print')
      echo "Importing $alias"
      keytool -import -file ${CERT} -alias "${alias}" -storepass ${storepassword} -keystore ${truststore} -noprompt
      rm $CERT
    done
    
    rm ${mydir}/global-bundle.pem
    
    echo "Trust store content is: "
    
    keytool -list -v -keystore "$truststore" -storepass ${storepassword} | grep Alias | cut -d " " -f3- | while read alias 
    do
       expiry=`keytool -list -v -keystore "$truststore" -storepass ${storepassword} -alias "${alias}" | grep Valid | perl -ne 'if(/until: (.*?)\n/) { print "$1\n"; }'`
       echo " Certificate ${alias} expires in '$expiry'" 
    done
                    

To learn more best practices about using SSL with Amazon RDS, see [ Best
practices for successful SSL connections to Amazon RDS for Oracle
](https://aws.amazon.com/blogs/database/best-practices-for-successful-ssl-
connections-to-amazon-rds-for-oracle/).

![Warning](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled.
Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Using SSL/TLS to encrypt a connection

Internetwork traffic privacy

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of
it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation
better.

