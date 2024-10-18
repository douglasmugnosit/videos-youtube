# Modelo de Responsabilidade Compartilhada da AWS Explicado

O modelo de responsabilidade compartilhada da AWS define as responsabilidades da AWS e do cliente em relação à segurança e conformidade. Entender essa divisão é crucial para garantir a proteção de dados e o cumprimento de normas.

## Índice

1. [Responsabilidades no Modelo de Segurança da AWS](#responsabilidades-no-modelo-de-segurança-da-aws)  
2. [Dividindo a Segurança e Conformidade](#dividindo-a-segurança-e-conformidade)  
3. [Exemplos de Responsabilidade no Modelo Compartilhado](#exemplos-de-responsabilidade-no-modelo-compartilhado)  
4. [Referências](#referências)  

---

## Responsabilidades no Modelo de Segurança da AWS

A **AWS** é responsável pela **segurança da nuvem**, cuidando da infraestrutura que inclui hardware, redes e os datacenters. Isso garante que o ambiente subjacente está protegido contra falhas e ameaças físicas.

Já o **cliente** é responsável pela **segurança na nuvem**, ou seja, pela configuração e gestão dos serviços que ele utiliza, como permissões de acesso, criptografia e monitoramento de aplicações.

Essa divisão é fundamental para garantir uma **segurança completa** na nuvem. A AWS cuida da infraestrutura, mas o cliente deve garantir que suas aplicações e dados estejam protegidos corretamente.

![Responsabilidades no Modelo de Segurança da AWS](modelo_de_responsabilidade_compartilhado.png)

**Exemplos**:
- AWS: controle de acesso físico aos datacenters.
- Cliente: configurações de segurança no IAM e permissões de buckets S3.

---

## Dividindo a Segurança e Conformidade

Para **segurança e conformidade**, os clientes da AWS têm responsabilidades sobre vários pontos:

- **Criptografia**: O cliente escolhe como e onde criptografar os dados. A AWS oferece ferramentas como o **AWS Key Management Service (KMS)** para facilitar isso.
- **Gerenciamento de Identidades**: Ferramentas como o **IAM (Identity and Access Management)** são responsabilidade do cliente, para garantir que cada usuário tenha permissões adequadas.

A **segurança é sempre uma prioridade compartilhada**. A AWS fornece as ferramentas, mas a configuração e o monitoramento adequados são de responsabilidade do cliente.


---

## Exemplos de Responsabilidade no Modelo Compartilhado

**Pergunta**: Fiz o deploy de uma aplicação dentro de uma instância EC2, mas a instância caiu. De quem é a responsabilidade?  
**Resposta**: Se o problema for de infraestrutura (hardware, rede), a responsabilidade é da **AWS**. Se for relacionado à configuração ou aplicação, é responsabilidade do **cliente**.

**Pergunta**: Houve um problema físico em um datacenter da AWS. Quem é responsável?  
**Resposta**: A **AWS** é responsável pela segurança física e manutenção dos seus datacenters.

**Pergunta**: Um bucket S3 foi configurado como público e dados vazaram. De quem é a responsabilidade?  
**Resposta**: A configuração do bucket S3 é de responsabilidade do **cliente**, incluindo controle de acessos.

**Pergunta**: Um servidor EC2 foi comprometido por falta de atualização de patches de segurança. Quem é o responsável?  
**Resposta**: A atualização de patches em instâncias EC2 é responsabilidade do **cliente**.

---

## Referências

- [Modelo de Responsabilidade Compartilhada da AWS](https://aws.amazon.com/pt/compliance/shared-responsibility-model/)
