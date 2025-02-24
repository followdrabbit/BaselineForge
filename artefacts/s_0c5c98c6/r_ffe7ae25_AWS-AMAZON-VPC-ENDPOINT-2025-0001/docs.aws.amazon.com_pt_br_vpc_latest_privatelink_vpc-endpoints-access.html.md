# Processed Content from URL: {'REFERENCE': 'https://docs.aws.amazon.com/pt_br/vpc/latest/privatelink/vpc-endpoints-access.html'}

[](aws-privatelink.pdf#vpc-endpoints-access "Abrir em PDF")

[DocumentaÃ§Ã£o](/index.html)[Amazon VPC](/vpc/index.html)[AWS
PrivateLink](what-is-privatelink.html)

ConsideraÃ§ÃµesPolÃ­tica de endpoint padrÃ£oPolÃ­ticas para endpoints de
interfaceEntidades principais de endpoints de gatewayAtualizar uma polÃ­tica
VPC de endpoint

As traduÃ§Ãµes sÃ£o geradas por traduÃ§Ã£o automÃ¡tica. Em caso de conflito
entre o conteÃºdo da traduÃ§Ã£o e da versÃ£o original em inglÃªs, a versÃ£o em
inglÃªs prevalecerÃ¡.

# Controle o acesso aos VPC endpoints usando polÃ­ticas de endpoint

Uma polÃ­tica de endpoint Ã© uma polÃ­tica baseada em recursos que vocÃª anexa
a um VPC endpoint para controlar quais AWS entidades principais podem usar o
endpoint para acessar um. AWS service (ServiÃ§o da AWS)

Uma polÃ­tica de endpoint nÃ£o substitui polÃ­ticas baseadas em identidade nem
polÃ­ticas baseadas em recursos. Por exemplo, se vocÃª estiver usando um
endpoint de interface para se conectar ao Amazon S3, vocÃª tambÃ©m pode usar
as polÃ­ticas de bucket do Amazon S3 para controlar o acesso a buckets de
endpoints especÃ­ficos ou especÃ­ficos. VPCs

###### ConteÃºdo

  * ConsideraÃ§Ãµes
  * PolÃ­tica de endpoint padrÃ£o
  * PolÃ­ticas para endpoints de interface
  * Entidades principais de endpoints de gateway
  * Atualizar uma polÃ­tica VPC de endpoint

## ConsideraÃ§Ãµes

  * Uma polÃ­tica de endpoint Ã© um documento JSON de polÃ­tica que usa a linguagem da IAM polÃ­tica. A polÃ­tica deve conter um elemento [Principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html). O tamanho de uma polÃ­tica de endpoint nÃ£o pode exceder 20.480 caracteres, incluindo espaÃ§os em branco.

  * Ao criar uma interface ou um endpoint de gateway para um AWS service (ServiÃ§o da AWS), vocÃª pode anexar uma Ãºnica polÃ­tica de endpoint ao endpoint. VocÃª pode atualizar a polÃ­tica de endpoint a qualquer momento. Se vocÃª nÃ£o anexar uma polÃ­tica de endpoint, anexaremos aÂ polÃ­tica de endpoint padrÃ£o.

  * Nem todas ServiÃ§os da AWS oferecem suporte a polÃ­ticas de endpoint. Se um AWS service (ServiÃ§o da AWS) nÃ£o oferecer suporte Ã s polÃ­ticas de endpoint, permitimos acesso total a qualquer endpoint do serviÃ§o. Para obter mais informaÃ§Ãµes, consulte [Visualizar suporte a politicas de endpoint](./aws-services-privatelink-support.html#vpce-endpoint-policy-support).

  * Quando vocÃª cria um VPC endpoint para um serviÃ§o de endpoint diferente de um AWS service (ServiÃ§o da AWS), permitimos acesso total ao endpoint.

  * NÃ£o Ã© permitido usar caracteres curinga (* ou?) ou [operadores de condiÃ§Ãµes numÃ©ricas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html#Conditions_Numeric) com chaves de contexto globais que fazem referÃªncia a identificadores gerados pelo sistema (por exemplo, `aws:PrincipalAccount` ou `aws:SourceVpc`).

  * Ao usar um [operador de condiÃ§Ã£o de cadeia de caracteres](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html#Conditions_String), vocÃª deve usar pelo menos seis caracteres consecutivos antes ou depois de cada caractere curinga.

  * Quando vocÃª especifica um ARN em um elemento de recurso ou condiÃ§Ã£o, a parte da conta ARN pode incluir um ID de conta ou um caractere curinga, mas nÃ£o ambos.

## PolÃ­tica de endpoint padrÃ£o

A polÃ­tica de endpoint padrÃ£o concede acesso total ao endpoint.

    
    
    {
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": "*",
                "Action": "*",
                "Resource": "*"
            }
        ]
    }

## PolÃ­ticas para endpoints de interface

Por exemplo, polÃ­ticas de endpoint para ServiÃ§os da AWS, consulte[ServiÃ§os
da AWS que se integram com AWS PrivateLink](./aws-services-privatelink-
support.html). A primeira coluna da tabela contÃ©m links para a AWS
PrivateLink documentaÃ§Ã£o de cada uma AWS service (ServiÃ§o da AWS). Se um
AWS service (ServiÃ§o da AWS) oferece suporte a polÃ­ticas de endpoint, sua
documentaÃ§Ã£o inclui exemplos de polÃ­ticas de endpoint.

## Entidades principais de endpoints de gateway

Com endpoints de gateway, o elemento `Principal` deve ser definido como `*`.
Para especificar uma entidade principal, use a chave de condiÃ§Ã£o
`aws:PrincipalArn`.

    
    
    "Condition": {
        "StringEquals": {
            "aws:PrincipalArn": "arn:aws:iam::123456789012:user/endpointuser"
        }
    }

Se vocÃª especificar a entidade principal no formato abaixo, o acesso serÃ¡
concedido somente ao UsuÃ¡rio raiz da conta da AWS , e nÃ£o a todos os
usuÃ¡rios e perfis da conta.

    
    
    "AWS": "account_id"

Veja abaixo alguns exemplos de polÃ­ticas do endpoint para endpoints de
gateway:

  * [Endpoints para o Amazon S3](./vpc-endpoints-s3.html#edit-vpc-endpoint-policy-s3)

  * [Endpoints para o DynamoDB](./vpc-endpoints-ddb.html#iam-policies-ddb)

## Atualizar uma polÃ­tica VPC de endpoint

Use o seguinte procedimento para atualizar uma polÃ­tica de endpoint para umÂ
AWS service (ServiÃ§o da AWS). Depois que vocÃª atualizar uma polÃ­tica de
endpoint, poderÃ¡ levar alguns minutos para que as alteraÃ§Ãµes sejam
aplicadas.

###### Para atualizar uma polÃ­tica de endpoint usando o console

  1. Abra o VPC console da Amazon em [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

  2. No painel de navegaÃ§Ã£o, escolha **Endpoints**.

  3. Selecione o VPC endpoint.

  4. Escolha **Actions** (AÃ§Ãµes), **Manage policy** (Gerenciar polÃ­tica).

  5. Escolha **Full Access** (Acesso total) para permitir acesso total ao serviÃ§o ou escolha **Custom** (Personalizado) e anexe uma polÃ­tica personalizada.

  6. Escolha **Salvar**.

###### Para atualizar uma polÃ­tica de endpoint usando a linha de comando

  * [modify-vpc-endpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpc-endpoint.html) (AWS CLI)

  * [Edit-EC2VpcEndpoint](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2VpcEndpoint.html)(Ferramentas para Windows PowerShell)

![AtenÃ§Ã£o](https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png)
**O Javascript estÃ¡ desativado ou nÃ£o estÃ¡ disponÃ­vel no seu navegador.**

Para usar a documentaÃ§Ã£o da AWS, o Javascript deve estar ativado. Consulte
as pÃ¡ginas de Ajuda do navegador para obter instruÃ§Ãµes.

[ConvenÃ§Ãµes do documento](/general/latest/gr/docconventions.html)

Exemplos de polÃ­ticas baseadas em identidade

AWS polÃ­ticas gerenciadas

Essa pÃ¡gina foi Ãºtil? - Sim

Obrigado por nos informar que estamos fazendo um bom trabalho!

Se tiver tempo, conte-nos sobre o que vocÃª gostou para que possamos melhorar
ainda mais.

Essa pÃ¡gina foi Ãºtil? - NÃ£o

Obrigado por nos informar que precisamos melhorar a pÃ¡gina. Lamentamos ter
decepcionado vocÃª.

Se tiver tempo, conte-nos como podemos melhorar a documentaÃ§Ã£o.

