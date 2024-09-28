# Como Fazer Modelagem de Dados no AWS DynamoDB

### O que é o DynamoDB?

- DynamoDB é um banco de dados NoSQL da AWS
- altamente escalável e gerenciado
- Projetado para lidar com grandes volumes de dados e alta taxa de requisições. 

### Importância da Modelagem de Dados

- A modelagem de dados no DynamoDB é essencial :
  - Eficiencia
  - Escalabilidade
  - Custo baixo
  - Um design inadequado pode resultar em alto consumo de recursos e baixa performance.

### Conceitos-Chave para Modelagem de Dados no DynamoDB

#### Partition Key

- **Partition Key (Chave de partição)**: Define a partição onde os dados serão armazenados. A escolha correta da chave-partição é fundamental para garantir a distribuição uniforme dos dados.
  
  **Exemplo**: Em um sistema de gerenciamento de pedidos de uma loja online, a **chave-partição** pode ser o **ID do Cliente**. Assim, todos os pedidos de um cliente específico são armazenados na mesma partição.

#### Sort Key

- **Sort Key (Chave de Ordenação)**: Quando usada, a sort key organiza os itens dentro da partição definida pela chave-partição. Ela ajuda a realizar buscas mais detalhadas dentro de uma partição.

  **Exemplo**: Usando o mesmo cenário de uma loja online, a **sort key** pode ser a **data do pedido**, permitindo ordenar e acessar facilmente todos os pedidos de um cliente por data.

#### Exemplo
| ID do Cliente | Data e Hora do Pedido | Item            | Quantidade | Preço |
|---------------|-----------------------|-----------------|------------|-------|
| 12345         | 2024-01-15 10:35:00   | Laptop           | 1          | 2000  |
| 12345         | 2024-02-02 14:20:00   | Smartphone       | 1          | 900   |
| 67890         | 2024-01-22 09:50:00   | Monitor          | 2          | 500   |
| 67890         | 2024-02-05 16:10:00   | Teclado          | 1          | 50    |


### O que é Hot Partition?

- Partição que recebe uma carga desproporcional de acessos ou dados
- Ocorre quando as chaves-partição são mal distribuídas
- Concentra muitas requisições em uma única partição.


| ID do Produto | Data e Hora do Pedido | ID do Cliente | Quantidade | Preço |
|---------------|-----------------------|---------------|------------|-------|
| PROD-001      | 2024-01-15 10:35:00   | 12345         | 1          | 2000  |
| PROD-001      | 2024-02-02 14:20:00   | 12346         | 1          | 900   |
| PROD-001      | 2024-02-02 14:25:00   | 12347         | 2          | 1800  |
| PROD-001      | 2024-02-02 14:30:00   | 12348         | 1          | 900   |


### Como Evitar Hot Partition?

Adicionar um Prefixo Aleatório, Hash, região, ou algo a mais que possa fazer o "sharding" da partição. (Melhor cardinalidade) 

| Partition Key  | Data e Hora do Pedido | ID do Cliente | Quantidade | Preço |
|----------------|-----------------------|---------------|------------|-------|
| A-PROD-001     | 2024-01-15 10:35:00   | 12345         | 1          | 2000  |
| B-PROD-001     | 2024-02-02 14:20:00   | 12346         | 1          | 900   |
| C-PROD-001     | 2024-02-02 14:25:00   | 12347         | 2          | 1800  |
| A-PROD-001     | 2024-02-02 14:30:00   | 12348         | 1          | 900   |

**Só se faz sentido. Qual limite ?**
By default, every partition in a DynamoDB table is designed to deliver a maximum capacity of 3,000 read units per second and 1,000 write units per second. (https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html)