# Índice Geral do Case

Este documento centraliza todos os links, evidências e ativos exigidos para avaliação do Case Técnico.

### 🔎 Status Geral do Projeto:

✔ Planejamento  
✔ Engenharia  
✔ Modelagem  
⏳ GenAI  
⏳ Dashboard  
⏳ Pipeline  
⏳ Data App  
⏳ Apresentação

## 1️⃣ Planejamento (PMBOK)

- **Documento:** [Planejamento do Projeto (PMBOK)](../docs/01_planejamento_pmbok.md)
- **Ferramenta de Gestão Utilizada:** Azure DevOps (Agile/Kanban)
- **Evidências:**
  - Estruturação em Epics, Features e Tasks
  - Prints incluídos no documento

## 2️⃣ Base de Dados

- **Documento:** [Base de Dados](../docs/02_base_de_dados.md)
- **Link Dataset:** [Amazon Products Dataset 2023](https://www.kaggle.com/datasets/asaniczka/amazon-products-dataset-2023-1-4m-products)

## 3️⃣ Integrar e Explorar

- **Documento:** [Integrar e Explorar](../docs/03_integrar_explorar.md)
- **Notebooks:**
  - [ETL de ingestão e limpeza](../notebooks/01_etl_ingestao_limpeza_silver.ipynb)
  - [Gold série temporal e métricas](../notebooks/02_gold_series_temporal_e_metricas.ipynb)
- **Link da Dadosfera:** [app.dadosfera.ai](https://app.dadosfera.ai/pt-BR/)
- **Saídas geradas:**
  - amazon_products_bronze
  - amazon_products_silver
  - gold_products_curated
  - gold_category_metrics
  - gold_category_segment_tier_monthly
  - gold_top_products
- **Evidências:**
  - Print do dataset carregado
  - Evidência de ingestão
  - Dicionário de dados
  - Print do catálogo

## 4️⃣ Data Quality

- **Documento:** [Data Quality](../docs/04_data_quality.md)
- **Evidências:**
  - Análise de nulos
  - Validação de schema
  - Prints

## 5️⃣ GenAI / LLM

- **Documento:** [Processar GenAI LLM](../docs/05_processar_genai_llm.md)
- **Notebook:** [Processar GenAI LLM features](../notebooks/03_processar_genai_llm_features.ipynb)
- **Modelo utilizado:** OpenAI (GPT-4o-mini / GPT-4.1-mini)
- **Evidências:**
  - Prints das features geradas
  - Persistência Gold Enriched

## 6️⃣ Modelagem de Dados

- **Documento:** [Modelagem de Dados](../docs/06_modelagem_dados.md)
- **Notebook:** [Gold série temporal e métricas](../notebooks/02_gold_series_temporal_e_metricas.ipynb)
- **Diagrama ERD:**
  - Gerado via dbdesigner
  - Validado no DuckDB (DBeaver)
- **DDL:** [Kimball DDL SQL](../assets/sql/kimball_ddl.sql)

## 7️⃣ Dashboard

- **Documento:** [Analisar Dashboard](../docs/07_analisar_dashboard.md)
- **Coleção:** <Nome Sobrenome - Mes_Ano>
- **SQL utilizada:** [Dashboard Queries SQL](../assets/sql/dashboard_queries.sql)
- **Evidências:**
  - 5 visualizações distintas
  - Evidência de coleção criada

## 8️⃣ Pipeline

- **Documento:** [Pipelines](../docs/08_pipelines.md)
- **Ativos cadastrados na Dadosfera:**
  - Produtos
  - Categorias
- **Evidências:**
  - Print do pipeline
  - Evidência de execução

## 9️⃣ Data App

- **Documento:** [Data APP](../docs/09_data_app.md)
- **Notebook:** [Data APP Streamlit](../notebooks/04_data_app_streamlit.ipynb)
- **Link Streamlit:** [Inserir link]()
- **Evidências:** [](../assets/prints/)

## 🔟 Apresentação

- **Documento:** [Apresentação](../docs/10_apresentacao.md)
- **Vídeo (YouTube - Unlisted):** [Inserir link]()
