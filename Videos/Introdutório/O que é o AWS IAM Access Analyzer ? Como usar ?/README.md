# AWS IAM Access Analyzer

## O que é o IAM Access Analyzer?

O **IAM Access Analyzer** é uma ferramenta fornecida pela AWS que permite monitorar e analisar permissões de acesso aos seus recursos. Ele ajuda a identificar **permissões excessivamente amplas** que podem expor seus recursos a usuários ou serviços não autorizados. O Access Analyzer faz isso verificando as políticas de acesso e gerando alertas sempre que um recurso estiver acessível fora da sua conta AWS, garantindo uma análise de segurança contínua.

### Tipos

<div style="background-color: #FFF9C4; color: black; padding: 10px; border-radius: 5px; border: 1px solid #FBC02D;">

<strong>**External Access Analysis**</strong> : Detecta recursos que permitem acesso a usuários ou contas fora da sua AWS, gerando alertas para revisão de permissões. 
<p> <strong>Exemplo 1 . </strong> Um bucket S3 está configurado como "público", permitindo que qualquer pessoa na internet acesse seus arquivos. O Access Analyzer detecta isso e gera um alerta, avisando que o bucket está acessível fora da sua conta AWS.
<p> <strong>Exemplo 2 . </strong> Uma função Lambda está configurada para ser invocada por uma API pública sem autenticação. O Access Analyzer detecta que a função pode ser chamada por qualquer pessoa na internet, gerando um alerta para que você revise e ajuste a política de acesso, garantindo que apenas usuários autorizados possam invocá-la.
<p> <strong>Exemplo 3 . </strong>  Uma instância do Amazon RDS está configurada para permitir conexões de IPs fora da VPC, o que pode expor seu banco de dados a acessos externos não autorizados. O IAM Access Analyzer detecta essa configuração e emite um alerta, recomendando que você restrinja o acesso apenas a IPs confiáveis ou dentro da VPC.
</div>
<br>

<div style="background-color: #FFF9C4; color: black; padding: 10px; border-radius: 5px; border: 1px solid #FBC02D;">
<strong>Unused Access Analysis</strong> : Identifica permissões concedidas, mas não utilizadas, permitindo removê-las para seguir o princípio de menor privilégio. 
<p> <strong>Exemplo 1 . </strong> Uma função Lambda tem permissões para acessar um banco de dados RDS, mas nunca usa essa permissão. O Access Analyzer identifica que essa permissão não é necessária e recomenda sua remoção para aumentar a segurança.
</div>



### Principais Funcionalidades:
- **Detecção de acessos públicos e entre contas**: Identifica quando um recurso pode ser acessado por entidades fora da sua conta ou organização.
- **Análise automática de políticas**: Verifica suas políticas de acesso em serviços como S3, IAM, Lambda, e outros, para identificar permissões excessivamente permissivas.
- **Sugestões para correções**: Fornece recomendações baseadas nas melhores práticas de segurança, permitindo ajustar políticas de forma precisa.
- **Alertas de eventos de acesso**: Gera notificações sobre descobertas que podem comprometer a segurança dos recursos.


## Exemplos de Casos de Uso:
- **Auditorias de segurança**: Identificar rapidamente quais recursos da sua conta são acessíveis publicamente.
- **Segurança proativa**: Receber alertas sempre que permissões indesejadas forem detectadas em suas políticas.
- **Ajuste de permissões**: Garantir que suas políticas de IAM estejam aderentes ao princípio de menor privilégio.

## Quando usar o IAM Access Analyzer

1. **External Access Analysis**:
   - **Quando usar**: Utilize essa análise sempre que você quiser garantir que seus recursos (como buckets S3, funções Lambda, RDS, etc.) não estejam expostos a usuários não permitidos ou contas externas. Isso é especialmente importante quando você:<p>
     - Está configurando novos recursos com políticas de acesso.
     - Está auditando a segurança dos seus recursos para identificar acessos indesejados ou permissões excessivas.
     - Deseja verificar se algum recurso foi compartilhado publicamente ou com outras contas AWS por erro.
     - Está preparando uma auditoria de segurança ou conformidade e precisa garantir que apenas as partes corretas tenham acesso aos seus recursos.

2. **Unused Access Analysis**:
   - **Quando usar**: Utilize essa análise quando você quiser otimizar suas permissões de acesso, removendo permissões que não são mais necessárias. É ideal para:<p>
     - **Auditorias periódicas**: Revisar permissões e políticas que podem ter sido concedidas anteriormente, mas que não estão mais sendo usadas.
     - **Reforçar o princípio de menor privilégio**: Identificar e remover permissões que não estão sendo usadas para minimizar os riscos de segurança.
     - **Limpar permissões antigas**: Quando uma função, serviço ou usuário teve permissões atribuídas no passado, mas essas permissões não são mais necessárias.
     - **Após mudanças organizacionais ou de projeto**: Para garantir que as permissões de acesso de recursos antigos ou de projetos descontinuados sejam removidas ou ajustadas conforme necessário.


## Conclusão

O IAM Access Analyzer é uma poderosa ferramenta para ajudar a garantir a segurança dos seus recursos na AWS. Ele permite a análise e ajustes contínuos das permissões de acesso, garantindo que somente as entidades certas tenham acesso aos recursos. Usá-lo regularmente ajuda a manter uma postura de segurança robusta e em conformidade com as melhores práticas.
