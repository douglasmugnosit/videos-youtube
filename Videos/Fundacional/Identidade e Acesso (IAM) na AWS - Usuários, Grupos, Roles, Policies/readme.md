# AWS IAM: Usuários, Grupos, Roles, Policies e Identity Providers

## O que é AWS IAM ?
O **AWS Identity and Access Management (IAM)** permite gerenciar o acesso aos serviços e recursos da AWS com segurança. Com o IAM, você pode criar e gerenciar **ACESSOS DE USUÁRIOS E OBJETOS (ARN - Amazon Resource Name)** na AWS, controlar suas permissões e configurar políticas de segurança.

**AWS IAM é um recurso de escopo GLOBAL**

## Recursos
1. **Usuários (Users)**
   - Definição: Representam pessoas ou aplicativos que precisam interagir com a AWS.
   - Pontos principais:
     - Cada usuário tem um **nome** e **credenciais** (chave de acesso e senha).
     - Usuários podem ser associados a **políticas** para controlar suas permissões.
     - Use **MFA (Autenticação Multifator)** para melhorar a segurança de usuários individuais.
   
2. **Grupos (Groups)**
   - Definição: São coleções de usuários que herdam permissões comuns.
   - Pontos principais:
     - Simplificam o gerenciamento de permissões aplicando uma política única a um conjunto de usuários.
     - Exemplo: Grupo “Administradores” com permissões administrativas ou grupo “Desenvolvedores” com permissões limitadas.
     - Um usuário pode pertencer a vários grupos, e suas permissões são uma combinação de todas as políticas aplicadas aos grupos.

3. **Roles (Funções)**
   - Definição: Roles permitem que uma entidade (usuário, serviço ou conta AWS) assuma permissões temporárias.
   - Pontos principais:
     - Não requer credenciais de login. Em vez disso, são assumidas com permissões específicas.
     - Muito usadas para permitir que recursos da AWS, como EC2 ou Lambda, interajam com outros serviços da AWS.
     - **Role Cross-Account**: permite que usuários de uma conta AWS acessem recursos em outra conta.

4. **Policies (Políticas)**
   - Definição: São documentos JSON que definem permissões para acessar recursos da AWS.
   - Pontos principais:
     - **Políticas Gerenciadas pela AWS**: Criadas e mantidas pela AWS.
     - **Políticas Personalizadas**: Criadas por você, com controle completo sobre permissões.
     - Uma política pode ser anexada a usuários, grupos ou roles.
     - Políticas baseadas em **identidade** (quem pode fazer o quê) e **recursos** (quem pode acessar quais recursos).

5. **Identity Providers (Provedores de Identidade - IdPs)**
   - Definição: Um **Identity Provider (IdP)** é um serviço que gerencia a identidade de usuários e permite o acesso a recursos da AWS sem a necessidade de criar uma conta IAM separada.
   - Pontos principais:
     - **Tipos de Identity Providers**:
       - **SAML 2.0**: Integração com provedores de identidade corporativos, como Active Directory ou Okta, para logins corporativos seguros.
       - **OpenID Connect (OIDC)**: Suporta autenticação com plataformas como Google, Amazon e Facebook.
       - **Cognito**: AWS Cognito permite autenticação para aplicativos móveis e web com integração a provedores sociais (Google, Facebook, etc.) ou identidades corporativas.
     - **Assumindo Roles com Identity Providers**: Usuários autenticados via IdP podem assumir roles da AWS com permissões específicas, baseadas em políticas configuradas.
