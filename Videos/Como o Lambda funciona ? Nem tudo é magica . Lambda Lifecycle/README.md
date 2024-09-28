# Como o Lambda Funciona? Nem tudo é mágica – Lambda Lifecycle

### AWS Lambda
AWS Lambda é um serviço de **computação serverless** da AWS. Ele permite que você execute código sem precisar provisionar ou gerenciar servidores, pagando apenas pelo tempo de execução do código. 

### Lifecycle

![Communication](image-1.png)
<br><p>
![Lifecycle](image.png)
https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html


### Fases

0. Lambda Service
    1. Lambda service chama seu serviço em uma execution environment (isolamento)
    2. A execution environment gerencia os recursos para rodar a função
    3. Env é criado com recurso de compute definido, Permissions, credentials, env variables...


1. INIT (TIMEOUT 10 Seconds - Retry)
    1. EXTENSION INIT
    2. RUNTIME INIT
    3. FUNCTION INIT

2. INVOKE
    1. INVOKE

3. SHUTDOWN
    1. RUNTIME SHUTDOWN
    2. EXTENSION SHUTDOWN


#### INVOKE

#### SHUTDOWN

#### INVOKE

#### SHUTDOWN










### O que é AWS Lambda?

AWS Lambda é um serviço de **computação serverless** da AWS. Ele permite que você execute código sem precisar provisionar ou gerenciar servidores, pagando apenas pelo tempo de execução do código. Mas, por trás da simplicidade aparente, há um ciclo de vida claro e lógico.

### Lambda Lifecycle

O ciclo de vida do Lambda passa por várias fases, desde o evento que o aciona até a sua finalização.

#### 1. **Invoke - O Evento que Dispara a Função**
Tudo começa com um evento que dispara a função. Esse evento pode ser:
- Uma requisição HTTP via **API Gateway**
- Uma mensagem de **SNS**
- Um evento de upload no **S3**
- Um cron job via **CloudWatch**

Esse evento é passado como input para a função Lambda.

**Exemplo**: Uma requisição de login via API pode disparar uma função Lambda para processar a autenticação.

#### 2. **Inicialização do Ambiente (Init Phase)**

Antes de rodar o código, o Lambda precisa **inicializar o ambiente de execução**, o que inclui:
- Provisionar o ambiente.
- Carregar bibliotecas e executar o código de inicialização.

Aqui ocorrem duas situações:

- **Cold Start**: Quando a função não foi executada recentemente, o ambiente precisa ser inicializado do zero, o que gera uma pequena latência na primeira execução.
  
  **Exemplo**: Se a função Lambda ficou inativa por um tempo, o próximo request pode demorar um pouco mais devido ao cold start.
  
- **Warm Start**: Se a função já foi executada recentemente, o ambiente permanece em standby, o que acelera a execução.

**Exemplo**: A função Lambda já foi chamada antes e o ambiente já está pronto, então a execução é mais rápida.

#### 3. **Execução da Função (Execution Phase)**

Após a inicialização, o código da função Lambda é executado com o input do evento.

- Você paga apenas pelo **tempo de execução** da função, que é medido em milissegundos.
- Existem limites como:
  - **Tempo máximo de execução**: 15 minutos.
  - **Memória alocada**: 128 MB a 10 GB.

**Exemplo**: Uma função que consulta um banco de dados e retorna uma resposta seria executada aqui.

#### 4. **Encerramento e Reaproveitamento (Termination & Reuse Phase)**

Após a execução, o Lambda pode manter o ambiente ativo para **reaproveitamento** em futuras execuções. Isso é o que ocorre no **warm start**.

- **Terminação**: Se o ambiente não for reutilizado por um tempo, ele pode ser encerrado.
- **Persistência**: Variáveis no escopo global da função podem ser reutilizadas entre invocações.

**Exemplo**: Se você inicializa uma conexão com o banco de dados no escopo global, ela pode ser reutilizada nas próximas execuções, evitando o tempo de reconexão.

### Boas Práticas para Lambda

- **Minimizar Cold Starts**:
  - Mantenha suas funções pequenas e leves.
  - Escolha linguagens com inicialização rápida, como **Node.js** e **Python**.

- **Aproveitar a Persistência do Ambiente**:
  - Inicialize objetos de conexão fora do handler principal, para reutilizar o ambiente entre execuções.

- **Gerenciamento de Dependências**:
  - Inclua apenas as bibliotecas necessárias para reduzir o tempo de inicialização.

- **Monitoramento e Logs**:
  - Use **CloudWatch** para monitorar tempos de inicialização e execução, além de verificar erros.

### Conclusão

Embora o AWS Lambda pareça mágica, existe um ciclo de vida claro que influencia diretamente o desempenho e o custo das funções. Ao entender e otimizar cada fase, você pode garantir que suas funções Lambda rodem da maneira mais eficiente possível. Se curtiu o conteúdo, deixe o like e inscreva-se para mais dicas sobre AWS!
