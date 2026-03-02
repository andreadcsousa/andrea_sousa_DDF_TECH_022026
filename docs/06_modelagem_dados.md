# Modelagem de Dados

## 📐 Abordagem escolhida: Kimball

A modelagem foi estruturada seguindo os princípios de **Ralph Kimball (modelo dimensional)**, organizando o domínio em:

- **Dimensões** → contexto e atributos descritivos
- **Fatos** → métricas e eventos mensuráveis

### 🎯 Justificativa da Escolha

- Foco em análise e BI (Metabase / Dadosfera)
- Clareza na definição de granularidade
- Facilidade de expansão futura (GenAI, similaridade, recomendação)
- Desempenho em consultas analíticas (Star Schema)

## 📌 Princípio de Modelagem

O modelo foi estruturado em formato Star Schema, com fatos centralizados e dimensões desnormalizadas para otimização analítica. O modelo foi dividido em duas visões complementares:

1. **Snapshot por Produto →** análise de performance individual.
2. **Série Temporal Agregada →** análise estratégica por categoria e segmento.

## 🔎 Visão 1 – Catálogo e Performance (Snapshot por Produto)

### 🧩 Dimensões

> 🛍 dim_product

| Campo            | Tipo    |
| ---------------- | ------- |
| product_id (PK)  | text    |
| product_title    | text    |
| category_id (FK) | integer |
| price            | numeric |
| list_price       | numeric |
| price_segment    | text    |
| rating           | numeric |
| review_count     | integer |
| has_rating       | boolean |
| is_best_seller   | boolean |
| image_url        | text    |
| product_url      | text    |

> 📂 dim_category

| Campo            | Tipo    |
| ---------------- | ------- |
| category_id (PK) | integer |
| category_name    | text    |

### 📊 Fatos

> fact_product_snapshot

- Granularidade: **1 linha = 1 produto**
- Chave Primária: **product_id**

| Métrica               |
| --------------------- |
| units_sold_last_month |
| weighted_score        |
| strategic_score       |
| category_rank         |
| is_top_10_category    |

> 💼 Uso Principal

- Top produtos por categoria
- Priorização de catálogo
- Comparação de performance intra-categoria

## 📈 Visão 2 – Série Temporal (Mensal por Categoria + Segmentações)

### 🧩 Dimensões

> 📅 dim_date

- Granularidade: **1 linha = 1 mês**

| Campo        |
| ------------ |
| date_id (PK) |
| month_start  |
| year         |
| month_number |
| month_name   |

> 💲 dim_price_segment

| Campo              |
| ------------------ |
| price_segment (PK) |

> ⭐ dim_popularity_tier

| Campo                |
| -------------------- |
| popularity_tier (PK) |

> 📂 dim_category (reutilizada)

A dimensão de categoria é compartilhada entre os fatos, garantindo consistência analítica entre análises de produto e análises temporais.

### 📊 Fatos

> fact_category_monthly

- Granularidade: **1 linha = 1 mês + 1 categoria + 1 price_segment + 1 popularity_tier**
- Chave Primária composta: **date_id, category_id, price_segment, popularity_tier**

| Métrica      |
| ------------ |
| units_sold   |
| revenue      |
| median_price |
| avg_price    |

> 💼 Uso Principal

- Análise de tendência e sazonalidade
- Comparação entre segmentos (budget vs premium)
- Análise por faixa de popularidade

> [!IMPORTANT]
> **Observação:** Como o dataset não possui data real, a série temporal foi gerada de forma sintética e reprodutível (seed fixa), ancorada em `units_sold_last_month` e sazonalidade típica de e-commerce.

## ➿ Diagrama ERD

- Ferramenta utilizada: **dbdesigner (ERD)**
- Validação do DDL: **DBeaver + DuckDB**

#### 📌 Modelo Kimball

![Modelo Kimball](../assets/diagrams/06_modelagem_00_diagrama_kimball.png)

## 🧾 DDL (SQL)

- Arquivo: **[assets/sql/kimball_ddl.sql](../assets/sql/kimball_ddl.sql)**
- Engine de validação: **DuckDB (via DBeaver)**

### ✅ Validação do Modelo

A validação estrutural assegura que o modelo pode ser implantado em qualquer engine SQL compatível, reforçando a capacidade de substituição arquitetural. O modelo dimensional foi validado executando o DDL no DBeaver utilizando DuckDB como engine local.

**Nesta etapa foi validada:**

- Estrutura das tabelas
- Chaves primárias
- Chaves estrangeiras
- Integridade relacional

#### 📌 DDL no Dbeaver

![Kimball DDL](../assets/prints/06_modelagem_01_kimball_ddl.jpg)

> [!WARNING]
> A carga de dados não foi realizada neste momento, pois o objetivo desta etapa é demonstrar o desenho lógico do Data Warehouse.
