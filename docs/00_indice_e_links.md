# Índice Geral do Case

Este documento centraliza todos os links, evidências e ativos exigidos para avaliação do Case Técnico.

### 🔎 Status Geral do Projeto:

✔ Planejamento  
✔ Engenharia  
✔ Modelagem  
✔ GenAI  
✔ Dashboard  
⏳ Pipeline  
⏳ Data App  
⏳ Apresentação

## 1️⃣ Planejamento (PMBOK)

- **Documento:** [Planejamento do Projeto (PMBOK)](../docs/01_planejamento_pmbok.md)
- **Ferramenta de Gestão Utilizada:** Azure DevOps (Agile/Kanban)
- **Evidências:**
  - Estruturação em epics, features e tasks

## 2️⃣ Base de Dados

- **Documento:** [Base de Dados](../docs/02_base_de_dados.md)
- **Link Dataset:** [Amazon Products Dataset 2023](https://www.kaggle.com/datasets/asaniczka/amazon-products-dataset-2023-1-4m-products)
- **Evidências:**
  - Leitura, head e info do dataset

## 3️⃣ Integrar e Explorar

- **Documento:** [Integrar e Explorar](../docs/03_integrar_explorar.md)
- **Link da Dadosfera:** [app.dadosfera.ai](https://app.dadosfera.ai/pt-BR/)
- **Notebooks:**
  - [ETL de ingestão e limpeza](../notebooks/01_etl_ingestao_limpeza_silver.ipynb)
  - [Gold série temporal e métricas](../notebooks/02_gold_series_temporal_e_metricas.ipynb)
- **Evidências:**
  - Upload no catálogo da Dadosfera
  - Descrição dos ativos
  - Análise exploratória
  - Estrutura final da silver

## 4️⃣ Data Quality

- **Documento:** [Data Quality](../docs/04_data_quality.md)
- **Evidências:**
  - Análise de nulos
  - Distribuição de preços e rating

## 5️⃣ GenAI / LLM

- **Documento:** [Processar com GenAI (LLM Feature Extraction)](../docs/05_processar_genai_llm.md)
- **Notebook:** [Processar GenAI LLM features](../notebooks/03_processar_genai_llm_features.ipynb)
- **Modelo utilizado:** OpenAI (GPT-5.2 Plus)
- **Evidências:**
  - Shape do Sample
  - Prompt Definition
  - Enriched Dataframe Preview
  - Parquet Saved Confirmation
  - Execution Progress Bar e Summary
  - Cost Estimation Output

## 6️⃣ Modelagem de Dados

- **Documento:** [Modelagem de Dados](../docs/06_modelagem_dados.md)
- **Notebook:** [Gold série temporal e métricas](../notebooks/02_gold_series_temporal_e_metricas.ipynb)
- **Evidências:**
  - Diagrama ERD
  - Kimball DDL

## 7️⃣ Dashboard

- **Documento:** [Analisar Dashboard](../docs/07_analisar_dashboard.md)
- **Dashboard:** [Amazon Catalog Intelligence & Strategic Analytics](../dashboard/amazon_catalog_intelligence.pbix)
- **Evidências:**
  - Páginas: Executive Overview, Segmentation, AI Insights
  - Relacionamentos e Modelos de Pasta de Exibição
  - Métrica para texto dinâmico

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
- **Evidências:**

## 🔟 Apresentação

- **Documento:** [Apresentação](../docs/10_apresentacao.md)
- **Vídeo (YouTube - Unlisted):** [Inserir link]()
