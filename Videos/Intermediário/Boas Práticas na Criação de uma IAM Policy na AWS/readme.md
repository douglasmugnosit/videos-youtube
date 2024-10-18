# Boas Práticas na Criação de IAM Policies na AWS

## Introdução
As políticas do AWS Identity and Access Management (IAM) controlam o acesso aos recursos da AWS. Seguir boas práticas na criação de políticas garante a aplicação do **princípio do menor privilégio**, mantendo a segurança e evitando permissões excessivas. Este guia apresenta práticas recomendadas para criar políticas IAM seguras e eficientes.

---

## Boas Práticas e Exemplos

### 1. Princípio do Menor Privilégio

**Descrição**: Conceda apenas as permissões necessárias para realizar uma tarefa. Evite permissões amplas que possam conceder acesso desnecessário a outros recursos.

**Exemplo**:

Em vez de conceder permissões amplas como:

```json
{
  "Effect": "Allow",
  "Action": "s3:*",
  "Resource": "*"
}
```

Conceda permissões mais restritas:

```json
{
  "Effect": "Allow",
  "Action": [
    "s3:GetObject",
    "s3:PutObject"
  ],
  "Resource": "arn:aws:s3:::meu-bucket/*"
}
```

---

### 2. Use Políticas Gerenciadas Sempre que Possível ** SUGESTIVO! 

**Descrição**: Utilize políticas gerenciadas pela AWS ou políticas gerenciadas centralmente para facilitar o gerenciamento e garantir atualizações seguras e contínuas.

**Exemplo**: A AWS fornece várias **mnanaged policies**, como `AmazonS3ReadOnlyAccess` e `ReadOnlyAccess`, que já seguem boas práticas e podem ser utilizadas diretamente.

---

### 3. Restrinja Recursos Específicos

**Descrição**: Evite usar `"Resource": "*"`, que dá acesso a todos os recursos de um serviço. Sempre restrinja os recursos especificando o **ARN** (Amazon Resource Name) do recurso.

**Exemplo**:

Evite:

```json
{
  "Effect": "Allow",
  "Action": "ec2:StartInstances",
  "Resource": "*"
}
```

Prefira algo como:

```json
{
  "Effect": "Allow",
  "Action": "ec2:StartInstances",
  "Resource": "arn:aws:ec2:us-east-1:123456789012:instance/i-0abcd1234ef56789a"
}
```

---

### 4. Use Condições para Controle Granular

**Descrição**: Utilize condições (`Condition`) para restringir permissões com base em **tags**, **endereços IP**, **regiões** ou **MFA**, fornecendo um controle refinado sobre quando e como as ações podem ser executadas.

**Exemplo**:

Permitir a execução de ações apenas se a instância EC2 possuir a tag `Environment=Production`:

```json
{
  "Effect": "Allow",
  "Action": "ec2:StartInstances",
  "Resource": "arn:aws:ec2:us-east-1:123456789012:instance/*",
  "Condition": {
    "StringEquals": {
      "ec2:ResourceTag/Environment": "Production"
    }
  }
}
```

---

### 5. Evite Políticas Inline Extensas

**Descrição**: Políticas inline são associadas diretamente a um único usuário, grupo ou role, tornando o gerenciamento difícil em larga escala. Prefira políticas gerenciadas, que podem ser reutilizadas e atualizadas facilmente.

---

### 6. Utilize o IAM Access Analyzer

**Descrição**: Utilize o **IAM Access Analyzer** para identificar permissões excessivamente permissivas e ajustar políticas com base nas análises geradas.

---

### 7. Verifique Regularmente as Políticas

**Descrição**: Faça revisões periódicas nas suas políticas para garantir que as permissões ainda estejam alinhadas com as necessidades e que não haja permissões excessivas ou desnecessárias.

---

### 8. Políticas com Nomes Claros e Descritivos

**Descrição**: Use nomes descritivos para suas políticas, o que facilita a identificação rápida do objetivo de cada uma.

**Exemplo**: `S3-ReadOnly-Policy`, `EC2-AdminPolicy`, etc.

---

### 9. Teste as Políticas em Ambiente Controlado

**Descrição**: Sempre teste novas políticas em ambientes de desenvolvimento ou sandbox antes de aplicá-las em produção para evitar concessões excessivas de permissões.

---

## Conclusão

Seguir essas boas práticas ajuda a garantir que suas políticas IAM sejam seguras, fáceis de gerenciar e adaptáveis às mudanças na sua organização. A abordagem correta à criação e manutenção de políticas reduz o risco de permissões excessivas e protege melhor os seus recursos na AWS.
