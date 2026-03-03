# Data App (Streamlit)

Esta etapa entrega um **Data App desenvolvido em Streamlit** para exploração interativa do catálogo Amazon, utilizando dados derivados da camada Curated, enriquecidos com atributos semânticos via LLM (camada Enriched).

## 🎯 Objetivo

Disponibilizar uma interface analítica interativa que permita exploração granular do catálogo de produtos.

- **Explorar o catálogo por:** Categoria, Price Segment e Popularity Tier
- **Visualizar relações entre:** Preço × Rating
- **Analisar o mix de produtos por** Price Segment e indicador de monetização (Revenue Proxy)
- **Explorar atributos enriquecidos por IA:** Brand Guess e Product Type

O Data App atua como camada complementar ao dashboard executivo, oferecendo exploração analítica mais granular:

- **Dashboard (BI):** visão executiva consolidada
- **Data App (Streamlit):** exploração interativa, filtros dinâmicos, tabelas e gráficos detalhados

> [!NOTE]
> Embora o Data App esteja hospedado externamente (Streamlit Community Cloud), a estrutura de dados segue o modelo arquitetural proposto (RAW → Standardized → Enriched → Curated), demonstrando portabilidade da solução e independência entre camada de dados e camada de visualização.

## 🧾 Entradas e Saídas

### Entrada

- Notebook no Google Colab: [Data APP Streamlit](../notebooks/04_data_app_streamlit.ipynb)
- Dataset em formato Parquet utilizado pelo app: [Amazon Catalog APP](../app/amazon_catalog_app.parquet)
- Arquivo principal da aplicação: [Streamlit Data App](../app/app.py)

**Colunas utilizadas no app:**

- `product_id`, `product_title`, `category_name`
- `price`, `rating`, `units_sold_last_month`, `is_best_seller`
- `price_segment`, `popularity_tier`
- `llm_brand_guess`, `llm_product_type`, `llm_title_clean`

### Saída

#### 📌 Aplicação Streamlit: [Amazon Catalog Intelligence](https://acs-amazon-catalog-app.streamlit.app/)

O notebook no Google Colab gera o arquivo Parquet utilizado pelo Data App.

Esse arquivo é consumido diretamente pelo script `app.py` para carregamento do dataset no momento da inicialização da aplicação.

> [!NOTE]
> O arquivo Parquet foi mantido na pasta `app/` para facilitar a execução local da aplicação.  
> Em ambiente produtivo, recomenda-se leitura a partir de storage ou camada analítica materializada via pipeline.

## 🧱 Estrutura no Repositório

Arquivos criados/organizados nesta etapa:

- `app/app.py` — aplicação Streamlit
- `app/requirements.txt` — dependências do app
- `app/README.md` — instruções de execução local
- `app/.streamlit/config.toml` (se presente) — configuração visual e de tema

## ▶️ Como rodar localmente

Abra o terminal na raiz do repositório e execute:

```bash
cd app
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

## 🧭 Navegação do App

O aplicativo foi estruturado em três abas principais:

- **Executive:**
  - Cards: Products, Best Sellers, Avg Price, Avg Rating
  - Tabela: Top Products (Units Sold Last Month)
  - Scatter: Performance Map (Preço × Rating)
- **Segmentation:**
  - Tabela: Product Mix (Category × Price Segment)
  - Gráfico: Revenue Proxy (indicador direcional)
- **AI Insights:**
  - Ranking por IA (ex: Revenue Proxy por llm_product_type e/ou llm_brand_guess)
  - Foco em identificar padrões e concentração por atributos inferidos via LLM

## 🧠 Papel Estratégico do Data App

O Data App atua como camada de exploração analítica livre, permitindo análises ad-hoc e inspeção granular de produtos individuais, complementando o dashboard executivo.

Enquanto o dashboard responde perguntas estruturadas e consolidadas, o Data App permite investigação interativa, exploração de filtros e descoberta de padrões emergentes no catálogo.

### 📷 Evidências

#### 📌 Executive

![Executive Overview](../assets/prints/09_app_01_executive.jpg)

#### 📌 Segmentation

![Segmentation](../assets/prints/09_app_02_segmentation.jpg)

#### 📌 AI Insights

![AI Insights](../assets/prints/09_app_03_ai_insights.jpg)

## 🔁 Integração com Pipeline

A versão atual utiliza dataset exportado em Parquet para fins de demonstração da PoC.

**A arquitetura proposta prevê:**

- Pipeline automatizado responsável pela materialização e atualização da camada Curated
- Versionamento e atualização incremental dos dados
- Consumo direto da camada analítica pelo Data App
- Conexão segura ou endpoint de dados para leitura em tempo quase real
