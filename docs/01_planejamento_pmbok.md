# Planejamento do Projeto (PMBOK)

## 🎯 Objetivo

Estruturar o planejamento completo do projeto de implementação de uma Plataforma de Dados para uma empresa de e-commerce, utilizando a Dadosfera SaaS como solução central.

Este planejamento segue as boas práticas do PMBOK e serve como base organizacional para a execução do case técnico, garantindo alinhamento entre escopo, riscos, entregáveis e geração de valor ao negócio.

## 📋 Artefato de Planejamento

O projeto foi gerenciado através de um Kanban Board estruturado em macrofases, detalhando entregáveis, dependências e pontos críticos.

O planejamento foi elaborado antes da execução técnica do case, servindo como guia para organização das etapas de engenharia, análise e entrega final.

## 📌 Escopo

O escopo foi definido considerando a construção de uma Prova de Conceito (PoC), com foco em demonstrar viabilidade técnica, arquitetura de dados e geração de valor ao negócio.

### Inclui

- Ingestão de dados de e-commerce (>1M registros)
- Tratamento, padronização e organização em camadas (RAW → Standardized → Curated)
- Modelagem analítica dimensional (Data Warehouse - abordagem Kimball)
- Geração de análises de série temporal para suporte à tomada de decisão
- Extração estruturada de features a partir de dados desestruturados via LLM
- Criação de Dashboard analítico com múltiplas visualizações
- Desenvolvimento de Data App interativo com Streamlit
- Construção de Pipeline automatizado para processamento e atualização dos dados
- Apresentação executiva demonstrando a viabilidade da Dadosfera como Plataforma de Dados

### Não inclui

- Implantação produtiva em ambiente corporativo real
- Integração direta com sistemas transacionais externos (ERP/CRM)
- Monitoramento contínuo e governança operacional em ambiente produtivo

## 📂 Estrutura Analítica

1. Planejamento e Definição de Escopo
2. Ingestão e Integração (RAW Zone)
3. Tratamento, Padronização e Data Quality (Standardized Zone)
4. Modelagem Analítica (Curated - Data Warehouse Dimensional)
5. Enriquecimento com IA (Feature Engineering via LLM)
6. Análise e Visualização (Dashboard Analítico)
7. Desenvolvimento de Data App (Streamlit)
8. Pipeline de Processamento e Catalogação
9. Apresentação Executiva (Prova de Conceito)

## 🔁 Alinhamento ao Ciclo de Vida da Dadosfera

O planejamento foi estruturado seguindo as fases:

- **Integrar:** Ingestão (RAW)
- **Processar:** Tratamento, padronização e validação de qualidade (Standardized)
- **Explorar:** Catalogação, organização em camadas e análise exploratória dos dados
- **Analisar:** Dashboards e consultas SQL
- **ML/AI:** Extração de features estruturadas e enriquecimento semântico via LLM
- **Data Apps:** Aplicação interativa em Streamlit para exploração e geração de insights

## 📌 Metodologia de Gestão

O projeto foi estruturado utilizando abordagem Agile (Kanban), com organização em Epics, Features e Tasks no Azure DevOps.

Os Épicos foram definidos utilizando a metodologia **5W (What, Why, Who, When, Where)**, garantindo clareza de escopo, responsabilidade e contexto técnico desde a concepção de cada macroentrega.

**Colunas utilizadas:** `New | Active | Resolved | Closed`

> [!NOTE]
> A organização por Epics permitiu controle incremental da entrega, rastreabilidade das decisões técnicas e mitigação de riscos dentro do prazo estabelecido (5 dias corridos).

## 📅 Cronograma

| Dia | Entregas                | Fase PMBOK               |
| --- | ----------------------- | ------------------------ |
| 1   | Ingestão + Standardized | Execução                 |
| 2   | Curated + Modelagem     | Execução                 |
| 3   | LLM + Dashboard         | Execução                 |
| 4   | Data App + Consolidação | Execução e Monitoramento |
| 5   | Apresentação Executiva  | Encerramento e Entrega   |

## ⚠️ Análise de Riscos

A análise de riscos foi conduzida considerando aspectos técnicos, estratégicos, operacionais e financeiros do projeto.

| Risco                                | Tipo        | Impacto                                                          | Probabilidade | Mitigação                                                             |
| ------------------------------------ | ----------- | ---------------------------------------------------------------- | ------------- | --------------------------------------------------------------------- |
| Alto volume de dados                 | Técnico     | Degradação de performance durante processamento inicial          | Alta          | Uso de tipos otimizados (float32/int32) e particionamento             |
| Dataset sem data real                | Técnico     | Limitação analítica temporal                                     | Alta          | Geração de série temporal sintética reprodutível                      |
| Custo da API LLM                     | Financeiro  | Aumento de custo inesperado                                      | Média         | Processamento em batch, controle de tokens e amostragem estratificada |
| Prazo curto (5 dias corridos)        | Cronograma  | Entrega incompleta                                               | Média         | Planejamento incremental e priorização de entregas essenciais         |
| Complexidade excessiva da solução    | Estratégico | Dificuldade de explicação                                        | Baixa         | Foco em arquitetura clara e modular                                   |
| Dependência de ferramentas externas  | Operacional | Bloqueio técnico                                                 | Baixa         | Uso de alternativas locais (DuckDB, Colab)                            |
| Desalinhamento com critérios do case | Estratégico | Penalização na avaliação                                         | Baixa         | Revisão contínua do enunciado e checklist de requisitos               |
| Endpoint PostgreSQL público          | Técnico     | Indisponibilidade temporária                                     | Baixa         | Uso de provedor estável e backup local                                |
| Falha na ingestão (volume alto)      | Técnico     | Interrupção do fluxo de integração e atraso nas etapas seguintes | Médio         | Uso de amostragem controlada (200k) para contingência                 |
| Instabilidade na conexão PostgreSQL  | Operacional | Impossibilidade temporária de acesso aos dados                   | Alto          | Reconexão automática e fallback local (DuckDB)                        |
| Inconsistência nos dados RAW         | Técnico     | Comprometimento da qualidade analítica e da modelagem            | Médio         | Validação com Great Expectations antes da modelagem                   |

## 🔗 Interdependências do Projeto

A estrutura de dependências foi planejada para garantir evolução incremental e minimizar retrabalho, respeitando a hierarquia técnica das camadas de dados.

O fluxo de dependências segue a lógica das camadas analíticas e do ciclo de vida de dados:

### 🧱 Camadas de Engenharia

- **Standardized → Curated:** A camada Curated depende da padronização, tipagem e validação realizadas na Standardized.
- **Standardized → LLM:** O enriquecimento via LLM utiliza dados estruturados e consistentes provenientes da Standardized.

### 📊 Camadas Analíticas

- **Curated → Dashboard:** O dashboard consome exclusivamente métricas consolidadas da camada Curated.
- **Curated + LLM → Data App:** O Data App integra métricas analíticas (Curated) e atributos enriquecidos (LLM).

### 🎥 Entrega Final

- **Todos os componentes → Apresentação Executiva:** A apresentação depende da consolidação de todas as etapas anteriores, garantindo narrativa coerente e evidências reprodutíveis.

## 💰 Estimativa de Custos

- Plataforma de Dados (Dadosfera SaaS): licenciamento simplificado e centralização de serviços
- Banco relacional PostgreSQL (Cloud - Free Tier para PoC)
- Processamento LLM: custo variável por volume de tokens (controle por batch e amostragem)
- Hospedagem de Data App (Streamlit Cloud - Free Tier)
- Ambiente de desenvolvimento (Google Colab - gratuito)

> [!IMPORTANT]
> Estimativa de baixo custo operacional para PoC, com escalabilidade sob demanda e redução de overhead infraestrutural.

## 📊 Indicadores de Sucesso

O projeto será considerado bem-sucedido se:

- Dados estruturados em camadas RAW, Standardized e Curated
- Modelo dimensional implementado e validado com criação bem-sucedida das tabelas fact e dimension
- Dashboard contendo no mínimo 5 visualizações distintas
- LLM gerando atributos estruturados persistidos e integrados à camada analítica
- Pipeline definido e registrado na plataforma, permitindo execução automatizada
- Data App funcional publicado

## 🎯 Pontos Críticos

Os pontos críticos representam fatores que podem comprometer qualidade, clareza arquitetural ou avaliação técnica do case. Estes pontos foram monitorados ao longo do projeto como critérios de controle de qualidade.

### 🧱 Consistência do Schema

A integridade entre RAW, Standardized e Curated deve ser mantida, garantindo:

- Tipagem consistente
- Ausência de colunas ambíguas ou duplicadas
- Integridade de chaves primárias e estrangeiras no modelo dimensional

### 🤖 Controle de Custo e Volume da LLM

O enriquecimento via LLM deve:

- Utilizar amostragem estratificada controlada
- Minimizar chamadas desnecessárias com processamento em batch
- Produzir atributos estruturados persistidos e reutilizáveis na camada analítica

### 🔍 Rastreabilidade das Transformações

Todas as transformações devem ser:

- Reprodutíveis via notebooks versionados
- Documentadas no GitHub com instruções claras de execução
- Organizadas por camadas (RAW / Standardized / Curated / Enriched)

### 📚 Clareza e Reprodutibilidade

O projeto deve permitir que um avaliador:

- Execute os notebooks sem ajustes manuais
- Compreenda a arquitetura através do índice e da documentação
- Navegue facilmente entre documentos, evidências e ativos publicados

## 📊 Justificativa Estratégica

O planejamento foi estruturado para evidenciar a redução de complexidade arquitetural por meio da centralização de ingestão, processamento, modelagem, enriquecimento com IA e visualização em uma única plataforma integrada.

A proposta demonstra viabilidade técnica e eficiência operacional frente a arquiteturas tradicionais baseadas em múltiplos serviços distribuídos (ETL dedicado, Data Warehouse separado, ferramenta de BI isolada e camada de ML desacoplada), reduzindo overhead de integração, custo de manutenção e tempo de entrega de valor.

## 📷 Evidência de Gestão no Azure DevOps

Abaixo estão evidências da organização e execução do projeto:

#### 📌 Épicos Criados

![Épicos no Azure DevOps](../assets/prints/01_devops_02_epics_overview.jpg)

#### 📌 Hierarquia (Epic → Features → Tasks)

![Hierarquia do Épico Engenharia](../assets/prints/01_devops_03_epic_hierarchy_engineering.jpg)

#### 📌 Estrutura do Épico com 5W

![Épico estruturado com 5W](../assets/prints/01_devops_01_epic_5w_definition.jpg)
