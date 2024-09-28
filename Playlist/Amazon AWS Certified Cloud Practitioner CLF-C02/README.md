# AWS Certified Cloud Practitioner (CLF-C02) - Principais Tópicos e Serviços

Este guia descreve os principais tópicos do exame AWS Certified Cloud Practitioner (CLF-C02) e os serviços da AWS associados a cada um deles. Ele também destaca os benefícios oferecidos pela AWS em cada domínio.

Este guia é um **COMPILADO** e **NÃO** **CÓPIA** do guia oficial.

README baseado no exam guide de 2024/Q4. [Visite o site oficial da certificação](https://aws.amazon.com/certification/certified-cloud-practitioner/?ch=sec&sec=rmg&d=1) para mais detalhes.

---

## 1. Conceitos de Nuvem

### Benefícios:
- **Escalabilidade**: Permite ajustar recursos de TI conforme necessário, economizando custos e oferecendo flexibilidade.
- **Globalização**: Infraestrutura global com baixa latência e alta disponibilidade, permitindo alcance mundial.
- **Alta Disponibilidade**: Garantida pela arquitetura global da AWS, com suporte a failover automático e auto scaling.

### Serviços Principais:
- **Amazon EC2**: Computação escalável na nuvem.
- **Amazon S3**: Armazenamento de objetos com alta durabilidade.
- **AWS Global Infrastructure**: Regiões, Zonas de Disponibilidade e Locais de Borda para suporte à entrega global.

### Vídeos:
1. [O Que Você Precisa Saber para a Certificação AWS Cloud Practitioner (CLF-C02)](./1.%20Conceitos%20de%20Nuvem/1.%20Benef%C3%ADcios%20da%20Nuvem%20AWS.md)
2. [Guia Completo para Iniciantes na Certificação AWS Cloud Practitioner](./1.%20Conceitos%20de%20Nuvem/2.%20Princ%C3%ADpios%20de%20Design%20na%20Nuvem%20AWS.md)
3. [O que é Cloud Computing? Principais Conceitos da Nuvem AWS](./1.%20Conceitos%20de%20Nuvem/3.%20Estrat%C3%A9gias%20de%20Migra%C3%A7%C3%A3o%20para%20a%20Nuvem.md)
4. [Benefícios da Nuvem AWS: Escalabilidade, Flexibilidade e Economia de Custos](./1.%20Conceitos%20de%20Nuvem/4.%20Aspectos%20Econ%C3%B4micos%20da%20Nuvem.md)

---

## 2. Segurança e Conformidade

### Benefícios:
- **Segurança Reforçada**: Criptografia avançada, segurança multicamada e controle de acesso.
- **Conformidade**: Certificações globais que facilitam a adoção em setores regulamentados (GDPR, HIPAA, etc.).
- **Modelo de Responsabilidade Compartilhada**: A AWS cuida da segurança da infraestrutura, enquanto o cliente é responsável pelos dados e aplicativos.

### Serviços Principais:
- **AWS IAM**: Gerenciamento de identidades e controle de permissões.
- **AWS Shield**: Proteção contra ataques DDoS.
- **AWS Security Hub**: Centralização de conformidade e segurança.
- **AWS Artifact**: Documentos de conformidade.
- **Amazon GuardDuty**: Monitoramento de ameaças.
- **AWS Secrets Manager**: Gerenciamento seguro de credenciais.

### Vídeos:
1. [Modelo de Responsabilidade Compartilhada da AWS Explicado](./2.%20Seguran%C3%A7a%20e%20Conformidade/1.%20Modelo%20de%20Responsabilidade%20Compartilhada.md)
2. [Segurança na Nuvem AWS: Entenda o Modelo de Responsabilidade Compartilhada](./2.%20Seguran%C3%A7a%20e%20Conformidade/2.%20Conceitos%20de%20Governan%C3%A7a%20e%20Seguran%C3%A7a.md)
3. [Principais Conceitos de Segurança e Conformidade na AWS](./2.%20Seguran%C3%A7a%20e%20Conformidade/3.%20Gerenciamento%20de%20Identidade%20e%20Acesso.md)
4. [Como Gerenciar Identidade e Acesso (IAM) na AWS](./2.%20Seguran%C3%A7a%20e%20Conformidade/4.%20Componentes%20e%20Recursos%20de%20Seguran%C3%A7a.md)

---

## 3. Tecnologia e Serviços da Nuvem

### Benefícios:
- **Elasticidade e Eficiência de Custos**: Auto scaling e opções de compra como **Spot Instances** permitem ajustar o uso de recursos e pagar apenas pelo que é utilizado.
- **Automação e Agilidade**: Ferramentas como **AWS Lambda** e **AWS Fargate** oferecem automação sem a necessidade de gerenciamento de infraestrutura.
- **Inovação com IA e Machine Learning**: Serviços como **Amazon SageMaker** e **Amazon Rekognition** facilitam a implementação de soluções inteligentes.

### Serviços Principais:
- **Computação**:
  - **Amazon EC2**: Computação escalável.
  - **AWS Lambda**: Computação sem servidor.
  - **AWS Fargate**: Execução de containers sem gerenciamento de infraestrutura.
- **Banco de Dados**:
  - **Amazon RDS**: Banco de dados relacional gerenciado.
  - **Amazon DynamoDB**: Banco de dados NoSQL.
  - **Amazon Aurora**: Banco de dados relacional otimizado para a nuvem.
- **Armazenamento**:
  - **Amazon S3**: Armazenamento de objetos.
  - **Amazon EFS**: Armazenamento de arquivos.
  - **Amazon EBS**: Armazenamento em bloco.
  - **AWS Backup**: Backup centralizado.
- **Rede**:
  - **Amazon VPC**: Redes virtuais privadas.
  - **Amazon CloudFront**: Rede de distribuição de conteúdo.
  - **Amazon Route 53**: DNS gerenciado.
  - **AWS Direct Connect**: Conexões dedicadas com a AWS.
- **Machine Learning e IA**:
  - **Amazon SageMaker**: Criação e treinamento de modelos de machine learning.
  - **Amazon Rekognition**: Análise de imagens e vídeos.
  - **Amazon Lex**: Chatbots com IA.
  - **Amazon Polly**: Conversão de texto em fala.

### Vídeos:
1. [EC2, Lambda e Fargate: Como Escolher o Serviço de Computação Certo na AWS](./3.%20Tecnologia%20e%20Servi%C3%A7os%20da%20Nuvem/1.%20M%C3%A9todos%20de%20Implanta%C3%A7%C3%A3o%20e%20Opera%C3%A7%C3%A3o.md)
2. [AWS EC2 Explicado: Instâncias Sob Demanda, Spot e Reservadas](./3.%20Tecnologia%20e%20Servi%C3%A7os%20da%20Nuvem/3.%20Servi%C3%A7os%20Computacionais.md)
3. [Tudo Sobre Armazenamento na AWS: S3, EBS, EFS e Mais](./3.%20Tecnologia%20e%20Servi%C3%A7os%20da%20Nuvem/6.%20Servi%C3%A7os%20de%20Armazenamento.md)
4. [Amazon S3 e EBS: Armazenamento Escalável na Nuvem AWS](./3.%20Tecnologia%20e%20Servi%C3%A7os%20da%20Nuvem/6.%20Servi%C3%A7os%20de%20Armazenamento.md)
5. [Introdução ao Amazon VPC: Crie Redes Privadas na AWS](./3.%20Tecnologia%20e%20Servi%C3%A7os%20da%20Nuvem/5.%20Servi%C3%A7os%20de%20Rede.md)
6. [Como Funciona o Amazon CloudFront: Distribuição Global de Conteúdo](./3.%20Tecnologia%20e%20Servi%C3%A7os%20da%20Nuvem/5.%20Servi%C3%A7os%20de%20Rede.md)
7. [Introdução ao Machine Learning na AWS: Amazon SageMaker Explicado](./3.%20Tecnologia%20e%20Servi%C3%A7os%20da%20Nuvem/7.%20Servi%C3%A7os%20de%20IA%20e%20Machine%20Learning.md)
8. [Serviços de IA na AWS: Amazon Rekognition, Lex, Polly e Mais](./3.%20Tecnologia%20e%20Servi%C3%A7os%20da%20Nuvem/7.%20Servi%C3%A7os%20de%20IA%20e%20Machine%20Learning.md)

---

## 4. Cobrança, Preços e Suporte

### Benefícios:
- **Economia de Custos**: Modelos de preços flexíveis como **Instâncias Sob Demanda**, **Spot Instances** e **Savings Plans** permitem otimizar os custos.
- **Previsibilidade e Controle**: Ferramentas como **AWS Cost Explorer** e **AWS Budgets** permitem monitorar e planejar os custos de forma eficiente.
- **Suporte Flexível**: Diferentes níveis de suporte técnico (Básico, Empresarial) garantem que os clientes obtenham a ajuda necessária, desde desenvolvedores até grandes empresas.

### Serviços Principais:
- **Modelos de Preço**:
  - **Instâncias Sob Demanda**: Pague pelo uso real.
  - **Instâncias Reservadas**: Desconto em compromissos de longo prazo.
  - **Spot Instances**: Capacidade ociosa com descontos significativos.
  - **Savings Plans**: Planos de economia ao comprometer uso de longo prazo.
- **Gerenciamento de Custos**:
  - **AWS Cost Explorer**: Análise de custos detalhada.
  - **AWS Budgets**: Definição de limites de orçamento e alertas.
  - **AWS Pricing Calculator**: Estimativa de custos.
- **Suporte**:
  - **AWS Support Plans**: Planos de suporte ajustáveis (Basic, Developer, Business, Enterprise).
  - **AWS Trusted Advisor**: Recomendações para otimização de custos, segurança e performance.
  - **AWS Health Dashboard**: Relatórios de integridade do ambiente e alertas personalizados.

### Vídeos:
1. [Guia Completo sobre Cobrança e Modelos de Preço na AWS](./4.%20Cobran%C3%A7a,%20Pre%C3%A7os%20e%20Suporte/1.%20Guia%20Completo%20sobre%20Cobran%C3%A7a%20e%20Modelos%20de%20Pre%C3%A7o%20na%20AWS.md)
2. [Instâncias Sob Demanda vs Reservadas vs Spot: Qual a Melhor Opção?](./4.%20Cobran%C3%A7a,%20Pre%C3%A7os%20e%20Suporte/2.%20Inst%C3%A2ncias%20Sob%20Demanda%20vs%20Reservadas%20vs%20Spot.md)
3. [Como Usar o AWS Cost Explorer para Monitorar seus Gastos na Nuvem](./4.%20Cobran%C3%A7a,%20Pre%C3%A7os%20e%20Suporte/3.%20Como%20Usar%20o%20AWS%20Cost%20Explorer.md)
4. [AWS Trusted Advisor: Como Otimizar Custos e Melhorar a Segurança na AWS](./4.%20Cobran%C3%A7a,%20Pre%C3%A7os%20e%20Suporte/4.%20AWS%20Trusted%20Advisor.md)

---

## Referências

Esta estrutura é baseada nos domínios e serviços cobertos no exame AWS Certified Cloud Practitioner (CLF-C02) e foi desenhada para ajudar a organizar o estudo e a preparação para a certificação.