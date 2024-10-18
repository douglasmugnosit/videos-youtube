# Entenda a Composição de uma AWS IAM Policy de vez por todas

## O que é uma IAM Policy?

Uma **IAM Policy** (Política IAM) na AWS é um documento em formato JSON que define permissões para conceder **(ALLOW)** ou negar**(DENY)** o acesso a recursos . Essas políticas são fundamentais para controlar quem pode fazer o quê dentro da infraestrutura da AWS.

### Tipos de IAM Policies

1. **Políticas Gerenciadas pela AWS // AWS managed**:
   - Pré-construídas pela AWS e atualizadas automaticamente para seguir boas práticas de segurança.
   - Exemplo: `AmazonS3ReadOnlyAccess` (permissões de leitura no S3).
   - AWS managed e AWS managed - job Function

2. **Políticas Gerenciadas pelo Cliente**:
   - Criadas e gerenciadas pelos administradores da conta AWS, permitindo personalização total.
   - Exemplo: Políticas específicas para a sua organização.

3. **Políticas Inline**:
   - Criadas e atribuídas diretamente a um **usuário**, **grupo** ou **role**, e não podem ser reutilizadas em outro contexto.

## Estrutura de uma IAM Policy


```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::meu-bucket/*"
    }
  ]
}
```

Uma **IAM Policy** tem uma estrutura simples, mas é altamente flexível. A política é composta pelos seguintes blocos principais:

- **Version**: Define a versão da linguagem da política (Atual mecanismo de politica da AWS). Atualmente. Valores : `["2012-10-17"]`.
  
- **Statement**: O bloco mais importante da política, onde as permissões são realmente definidas. Dentro do **Statement**, temos os seguintes elementos:
  
  - **Effect**: Define se a política vai **Allow** (permitir) ou **Deny** (negar) o acesso.
  - **Action**: Define quais ações são permitidas ou negadas. Exemplo: `s3:PutObject`, `ec2:StartInstances`, `<SERVICE>:<API/ACTION>`
  - **Resource**: Define quais recursos específicos estão sendo afetados pela política. Exemplo: ARN de um bucket S3 ou de uma instância EC2. Exemplo: `arn:aws:s3:::meu-bucket/*`, `arn:aws:ec2:us-east-1:123456789012:instance/i-0abcd1234ef56789a`
  - **Condition (opcional)** : Define condições específicas que devem ser atendidas para que a política seja aplicada.

- **Condition** (opcional): Define condições específicas que devem ser atendidas para que a política seja aplicada. 

#### Exemplos de Condições (Conditions Key):

- **aws:ResourceTag/<TagKey>**:
  - **Descrição**: Define que a ação só será permitida se o recurso tiver uma tag específica com um valor correspondente.
  - **Uso Comum**: Restringir ações em recursos (como EC2, S3) com base em suas tags. Por exemplo, permitir que uma ação seja realizada apenas se a instância EC2 tiver a tag `Environment=Production`.

- **aws:SourceIp**:
  - **Descrição**: Especifica que a ação só será permitida se a requisição vier de um endereço IP ou bloco de IPs específico.
  - **Uso Comum**: Restringir o acesso a recursos da AWS a partir de redes específicas, como IPs de um escritório corporativo ou uma faixa de IPs de uma VPN.

- **aws:SourceArn**:
  - **Descrição**: Condiciona a permissão à origem de um ARN específico, como o ARN de um recurso, serviço ou função que está chamando a ação.
  - **Uso Comum**: Usado para limitar ações com base em qual recurso ou serviço AWS está fazendo a requisição. Por exemplo, permitir que um Lambda assuma uma role somente se ele tiver um ARN específico.

- **aws:MultiFactorAuthPresent**:
  - **Descrição**: Verifica se a autenticação multifator (MFA) está ativada no momento da execução da ação.
  - **Uso Comum**: Restringir o acesso a ações sensíveis (como deletar instâncias EC2 ou buckets S3) exigindo que o usuário esteja autenticado com MFA.

- **aws:RequestedRegion**:
  - **Descrição**: Especifica que a ação só será permitida se a solicitação for feita em uma região da AWS específica.
  - **Uso Comum**: Restringir a execução de ações apenas para determinadas regiões AWS, como `us-east-1` ou `sa-east-1`.

- **s3:prefix**:
  - **Descrição**: Define um prefixo em um bucket S3 para restringir o acesso a certos diretórios ou arquivos.
  - **Uso Comum**: Controlar o acesso a partes específicas de um bucket S3, permitindo, por exemplo, o acesso apenas a arquivos dentro de `logs/`.

- **aws:CurrentTime**:
  - **Descrição**: Restringe a execução de uma ação com base no horário atual.
  - **Uso Comum**: Limitar o acesso a recursos apenas durante um intervalo de tempo específico, como horário comercial (9h às 18h).

   [VEJA TODAS CONDITIONS AQUI](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html)


```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ec2:StartInstances",
      "Resource": "arn:aws:ec2:*:*:instance/*",
      "Condition": {
        "StringEquals": {
          "ec2:ResourceTag/Environment": "Production"
        }
      }
    }
  ]
}
```

### Exemplos de Operadores de Condição:

- **DateLessThan**: Ação permitida se a data/hora for anterior a um valor.
- **DateGreaterThan**: Ação permitida se a data/hora for posterior a um valor.
- **StringEquals**: Ação permitida se o valor da string for igual ao esperado.
- **StringNotEquals**: Ação permitida se o valor da string for diferente do esperado.
- **IpAddress**: Ação permitida se a requisição vier de um endereço IP ou bloco específico.
- **Bool**: Ação permitida se o valor booleano for verdadeiro ou falso.
- **NumericLessThan**: Ação permitida se o valor numérico for menor que o esperado.
- **NumericGreaterThan**: Ação permitida se o valor numérico for maior que o esperado.
- **ArnEquals**: Ação permitida se o ARN for igual ao especificado.


 **DENY tem precedência sobre ALLOW, sendo na mesma ou em outra Policy assinada no mesmo acesso(Ex. Role com 3 policies)**