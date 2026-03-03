# Índice Geral do Case

Este documento centraliza os links, evidências e ativos utilizados na construção do case técnico, funcionando como guia de navegação para avaliação da solução proposta.

## 🧭 Como Navegar no Case

Este repositório foi estruturado para apresentar de forma progressiva a construção de uma plataforma analítica de dados.

A leitura recomendada segue a ordem abaixo:

1. **Planejamento** — definição do escopo e estratégia do projeto
2. **Base de Dados** — entendimento do dataset utilizado
3. **Integração e Exploração** — ingestão e organização na plataforma
4. **Qualidade de Dados** — validações e consistência estrutural
5. **Enriquecimento com IA** — extração de atributos semânticos via LLM
6. **Modelagem de Dados** — construção do modelo dimensional analítico
7. **Dashboards** — visualização analítica e insights estratégicos
8. **Pipeline** — automação do fluxo de dados
9. **Data App** — exploração interativa do catálogo
10. **Apresentação** — visão executiva do projeto

### 🔎 Status Geral do Projeto:

✔️ Planejamento  
✔️ Engenharia de Dados  
✔️ Qualidade de Dados  
✔️ Modelagem Dimensional  
✔️ Enriquecimento com GenAI  
✔️ Dashboards Analíticos  
✔️ Pipeline de Dados  
✔️ Data App  
✔️ Documentação de Apresentação

## 🧱 Arquitetura do Projeto

O fluxo de dados implementado segue a arquitetura:

`RAW → Standardized → Enriched → Curated → Camada de Consumo`

Esse fluxo conecta engenharia de dados, enriquecimento com IA e aplicações analíticas.

## 🔗 Repositório do Projeto

[GitHub - Amazon Catalog Intelligence](https://github.com/andreadcsousa/andrea_sousa_DDF_TECH_022026)

## 🌐 Acessos Principais

- **Dashboard Dadosfera (Metabase)**  
  http://metabase-treinamentos.dadosfera.ai/public/dashboard/395efcb8-bcda-45bf-8c7e-c4c26b53f866

- **Dashboard Power BI**  
  https://app.powerbi.com/view?r=eyJrIjoiNjhmNDg5MWMtMGU0Yi00ZjI5LTg5MTMtNTRiNTM5Y2RkOTAzIiwidCI6ImEzZTU3Zjc1LTU5YTktNDFkOS05ZGIwLTA0YmM0ODg2YWY3NyJ9&pageName=5f22c10194a1a41d956c

- **Data App (Streamlit)**  
  https://acs-amazon-catalog-app.streamlit.app/

## 1️⃣ Planejamento (PMBOK)

- **Documento:** [Planejamento do Projeto (PMBOK)](../docs/01_planejamento_pmbok.md)
- **Ferramenta de Gestão Utilizada:** Azure DevOps (Agile/Kanban)
- **Evidências:**
  - Estruturação em epics, features e tasks

## 2️⃣ Base de Dados

- **Documento:** [Base de Dados](../docs/02_base_de_dados.md)
- **Link Dataset:** [Amazon Products Dataset 2023](https://www.kaggle.com/datasets/asaniczka/amazon-products-dataset-2023-1-4m-products)
- **Evidências:**
  - Leitura, head e info do dataset base

## 3️⃣ Integrar e Explorar

- **Documento:** [Integrar e Explorar](../docs/03_integrar_explorar.md)
- **Link da Dadosfera:** [app.dadosfera.ai](https://app.dadosfera.ai/pt-BR/)
- **Notebooks:**
  - [ETL de ingestão e limpeza](../notebooks/01_etl_ingestao_limpeza.ipynb)
  - [Gold série temporal e métricas](../notebooks/02_series_temporal_e_metricas.ipynb)
- **Evidências:**
  - Upload no catálogo da Dadosfera
  - Descrição dos ativos
  - Análise exploratória
  - Estrutura final da camada Standardized

## 4️⃣ Data Quality

- **Documento:** [Data Quality](../docs/04_data_quality.md)
- **Evidências:**
  - Análise de nulos
  - Distribuição de preços e rating

## 5️⃣ GenAI / LLM

- **Documento:** [Processar com GenAI (LLM Feature Extraction)](../docs/05_processar_genai_llm.md)
- **Notebook:** [Processar GenAI LLM features](../notebooks/03_processar_genai_llm_features.ipynb)
- **Modelo utilizado:** OpenAI (gpt-4o-mini)
- **Evidências:**
  - Shape do Sample
  - Prompt Definition
  - Enriched Dataframe Preview
  - Parquet Saved Confirmation
  - Execution Progress Bar e Summary
  - Cost Estimation Output

## 6️⃣ Modelagem de Dados

- **Documento:** [Modelagem de Dados](../docs/06_modelagem_dados.md)
- **Notebook:** [Gold série temporal e métricas](../notebooks/02_series_temporal_e_metricas.ipynb)
- **Evidências:**
  - Diagrama ERD
  - Kimball DDL

## 7️⃣ Dashboards Analíticos

- **Documento:** [Analisar Dashboard](../docs/07_analisar_dashboard.md)
- **Dashboard:** [Amazon Catalog Intelligence & Strategic Analytics](../dashboard/amazon_catalog_intelligence.pbix)
- **Evidências:**
  - Páginas: Executive Overview, Segmentation, AI Insights
  - Relacionamentos e Modelos de Pasta de Exibição
  - Métrica para texto dinâmico
  - Dashboard publicado no Power BI Online e dashboard analítico construído na plataforma Dadosfera (Metabase)

## 8️⃣ Pipeline

- **Documento:** [Pipelines](../docs/08_pipelines.md)
- **Ativos utilizados no pipeline:**
  - Produtos
  - Categorias
  - Tabelas analíticas da camada Curated
- **Evidências:**
  - Print do pipeline
  - Evidência de execução

## 9️⃣ Data App

- **Documento:** [Data APP](../docs/09_data_app.md)
- **Notebook:** [Data APP Streamlit](../notebooks/04_data_app_streamlit.ipynb)
- **Link Streamlit:** [Amazon Catalog Intelligence](https://acs-amazon-catalog-app.streamlit.app/)
- **Evidências:**
  - Páginas da aplicação
  - Aplicação Streamlit para exploração interativa do catálogo

## 🔟 Apresentação

- **Documento:** [Apresentação](../docs/10_apresentacao.md)
- **Vídeo de apresentação (YouTube - Unlisted):** [Inserir link da gravação]()
