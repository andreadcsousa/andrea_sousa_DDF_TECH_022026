# Data App (Streamlit)

Esta etapa entrega um **Data App em Streamlit** para exploração interativa do catálogo Amazon, utilizando a base **Silver enriquecida com features via LLM** (camada Enriched).

## 🎯 Objetivo

O objetivo é disponibilizar uma experiência leve e navegável para:

- **Explorar o catálogo por:** Categoria, Price Segment e Popularity Tier
- **Visualizar relações entre:** Preço x Rating
- **Analisar mix por:** Price Segment e por Revenue Proxy
- **Consumir atributos enriquecidos por IA:** Brand Guess e Product Type

Camada de consumo interativo (Data App) que complementa o dashboard executivo:

- **Data App (Streamlit):** exploração livre, filtros, tabelas e gráficos com granularidade

## 🧾 Entradas e Saídas

### Entrada

- Notebook no Google Colab: [Data APP Streamlit](../notebooks/04_data_app_streamlit.ipynb)
- Dataset parquet do app: [Amazon Catalog APP](../app/amazon_catalog_app.parquet)
- Arquivo da aplicação: [Streamlit Data APP](../app/app.py)
- Conteúdo (colunas esperadas, exemplo):
  - `product_id`, `product_title`, `category_name`
  - `price`, `rating`, `units_sold_last_month`, `is_best_seller`
  - `price_segment`, `popularity_tier`
  - `llm_brand_guess`, `llm_product_type`, `llm_title_clean`

### Saída

#### 📌 Aplicação Streamlit: [Amazon Catalog Intelligence]()

O notebook no Google Colab gera o arquivo parquet. Esse arquivo é utilizado no script do app para executar a aplicação via Streamlit localmente.

> [!NOTE]
> O arquivo parquet foi baixado e mantido na pasta `app/` para facilitar a execução local.  
> Em cenário produtivo, recomenda-se apontar para um storage/URL ou pipeline de publicação.

### 📷 Evidências

#### 📌 Executive Overview

![Executive Overview](../assets/prints/09_app_01_executive.jpg)

#### 📌 Segmentation

![Segmentation](../assets/prints/09_app_02_segmentation.jpg)

#### 📌 I Insights

![AI Insights](../assets/prints/09_app_03_ai_insights.jpg)

## 🧱 Estrutura no repositório

Arquivos criados/organizados nesta etapa:

- `app/app.py` — aplicação Streamlit
- `app/requirements.txt` — dependências do app
- `app/README.md` — instruções rápidas de execução

## ▶️ Como rodar localmente

1. Abra o terminal na raiz do repositório e rode:

```bash
cd app
python -m venv venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
