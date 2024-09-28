# Retentativas (Retries)

### Sistemas Distribuídos: Coisas falham o tempo todo

- Servidores, Redes, Load Balancers (LBs), software, sistemas operacionais (OS) e erros humanos
- Falha transiente / temporária
- Precisamos arquitetar e desenhar nossas soluções para lidar com essas falhas

### Onde implemento Retries ?
- Service Mesh (Ex. Istio, Envoy...)
- Código (libs ou chamadas)

### Boas Práticas de Retentátivas

#### Retry
- Retry é egoísta, só pensa no cliente mesmo. 
- Independentemente do impacto no destino.
- Quando ocorre uma falha no meio (falha transiente - temporária), está ok. Mas quando é algo no destino, complica mais ainda.

#### Backoff / Exponential Backoff
- Ao invés de retentar imediatamente e agressivamente, o cliente espera algum tempo entre as tentativas, e esse tempo aumenta exponencialmente após cada tentativa.

#### Jitter
- Adicionar um jitter random entre as retentativas, o tempo de espera aumenta. Pode inclusive ser uma estratégia de backoff com jitter!

#### Timeout e número de retentativas
- Sempre configure um timeout para qualquer chamada remota. Um retry pode aumentar o load; imagine várias pessoas fazendo um retry sem nenhum critério de espera.
