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

## 🔹 01. Planejamento (PMBOK)

📄 Documento:  
[01_planejamento_pmbok.md](../docs/01_planejamento_pmbok.md)

📋 Ferramenta de Gestão Utilizada:

- Azure DevOps (Agile/Kanban)

🖼 Evidências:

- Estruturação em Epics, Features e Tasks
- Prints incluídos no documento

## 🔹 02. Base de Dados

📄 Documento:  
[02_base_de_dados.md](../docs/02_base_de_dados.md)

🌐 Link Dataset:  
[Amazon Products Dataset 2023 (1.4M Products)](https://www.kaggle.com/datasets/asaniczka/amazon-products-dataset-2023-1-4m-products)

## 🔹 03. Integrar e Explorar

📄 Documento:  
[03_integrar_explorar.md](../docs/03_integrar_explorar.md)

📓 Notebooks:  
[01_etl_ingestao_limpeza_silver.ipynb](../notebooks/01_etl_ingestao_limpeza_silver.ipynb)  
[02_gold_series_temporal_e_metricas.ipynb](../notebooks/02_gold_series_temporal_e_metricas.ipynb)

📑 Saídas geradas:

- amazon_products_bronze
- amazon_products_silver
- gold_products_curated
- gold_category_metrics
- gold_category_segment_tier_monthly
- gold_top_products

🖼 Evidências:

- Print do dataset carregado
- Evidência de ingestão
- Dicionário de dados
- Print do catálogo

## 🔹 04. Data Quality

📄 Documento:  
[04_data_quality.md](../docs/04_data_quality.md)

🖼 Evidências:

- Análise de nulos
- Validação de schema
- Prints

## 🔹 05. GenAI / LLM

📄 Documento:  
[05_processar_genai_llm.md](../docs/05_processar_genai_llm.md)

📋 Modelo utilizado:

- OpenAI (GPT-4o-mini / GPT-4.1-mini)

📓 Notebook:  
[05_processar_genai_llm_features.ipynb](../notebooks/03_processar_genai_llm_features.ipynb)

🖼 Evidências:

- Prints das features geradas
- Persistência Gold Enriched

## 🔹 06. Modelagem de Dados

📄 Documento:  
[06_modelagem_dados.md](../docs/06_modelagem_dados.md)

📓 Notebook:  
[02_gold_series_temporal_e_metricas.ipynb](../notebooks/02_gold_series_temporal_e_metricas.ipynb)

🗺 Diagrama ERD:

- Gerado via dbdesigner
- Validado no DuckDB (DBeaver)

📂 DDL:  
[assets/sql/kimball_ddl.sql](../assets/sql/kimball_ddl.sql)

## 🔹 07. Dashboard

📄 Documento:  
[07_analisar_dashboard.md](../docs/07_analisar_dashboard.md)

📊 Coleção:  
<Nome Sobrenome - Mes_Ano>

📄 SQL utilizada:  
[assets/sql/dashboard_queries.sql](../assets/sql/dashboard_queries.sql)

🖼 Evidências:

- 5 visualizações distintas
- Evidência de coleção criada

## 🔹 08. Pipeline

📄 Documento:  
[08_pipelines.md](../docs/08_pipelines.md)

⚙ Ativo cadastrado na Dadosfera

🖼 Evidências:

- Print do pipeline
- Evidência de execução

## 🔹 09. Data App

📄 Documento:  
[09_data_app.md](../docs/09_data_app.md)

🌐 Link Streamlit:  
[Inserir link]

📓 Notebook:  
[04_data_app_streamlit.ipynb](../notebooks/04_data_app_streamlit.ipynb)

🖼 Evidências:  
[](../assets/prints/)

## 🔹 10. Apresentação

📄 Documento:  
[10_apresentacao.md](../docs/10_apresentacao.md)

🎥 Vídeo (YouTube - Unlisted):  
[Inserir link]()

## 🔹 11. Arquitetura e Substituição

> [!WARNING]
> Descrição da proposta de substituição arquitetural utilizando Dadosfera como plataforma central.

📄 Documento:  
[11_arquitetura_substituicao.md](../docs/11_arquitetura_substituicao.md)
