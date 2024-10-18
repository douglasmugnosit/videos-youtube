# Versionamento de Policy na AWS

## O que é o Versionamento de Policy na AWS?

O **versionamento de policy na AWS** permite que você crie várias versões de uma mesma política de permissões no IAM (Identity and Access Management), mantendo o histórico de alterações. Cada policy na AWS pode ter até **cinco versões ativas** simultaneamente, e você pode escolher qual delas será marcada como a versão ativa. Isso facilita a gestão e auditoria de mudanças em permissões, sem a necessidade de reescrever ou substituir completamente uma política.

### Principais Características:
- **Suporte a múltiplas versões**: Mantém até cinco versões de uma política.
- **Controle de versão ativa**: Escolha a versão que estará ativa enquanto preserva versões anteriores.
- **Histórico de alterações**: Facilita a rastreabilidade de mudanças, permitindo a comparação entre versões.

## Por que usar o Versionamento de Policy?

O versionamento de políticas oferece uma série de vantagens para gerenciar permissões com maior controle e segurança:

### 1. **Facilitar Rollback**:
   - Se uma alteração em uma policy causar problemas de permissões, o versionamento permite **reverter facilmente** para uma versão anterior sem precisar recriar toda a política.
   
### 2. **Auditar Mudanças**:
   - Com o versionamento, é possível **auditar as modificações** feitas em uma política ao longo do tempo. 

### 3. **Testar Alterações**:
   - Permite testar mudanças em uma política em diferentes versões antes de aplicá-las como padrão. Você pode criar uma nova versão para adicionar permissões e testar seu impacto antes de torná-la a versão ativa.

### 4. **Evitar Perda de Configurações**:
   - O versionamento evita a **perda acidental de permissões** ou de configurações importantes ao modificar uma policy, já que versões anteriores continuam disponíveis para consulta ou recuperação.

## Como Usar o Versionamento de Policy na AWS

### Criando uma Nova Versão:
1. Acesse o console do **AWS IAM**.
2. Na seção de políticas, selecione a política que deseja modificar.
3. Crie uma nova versão da política com as alterações desejadas. (Edit)
4. Ative a nova versão, se necessário.

### Revertendo para uma Versão Anterior:
1. Acesse a lista de versões da política.
2. Selecione a versão anterior desejada.
3. Marque essa versão como a "default" para que ela entre em vigor.

## Conclusão

O versionamento de policy na AWS é uma funcionalidade poderosa que permite gerenciar, auditar e restaurar alterações em permissões de forma controlada e segura. É especialmente útil em ambientes dinâmicos, críticos ou regulatórios, onde a rastreabilidade e a capacidade de rollback são essenciais. No entanto, em casos de políticas simples ou que raramente mudam, o uso do versionamento pode ser desnecessário.
