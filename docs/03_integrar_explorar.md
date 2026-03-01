# Integrar e Explorar

Este documento descreve as etapas de ingestão, padronização e exploração inicial do dataset de e-commerce.

## 🔌 Integração (Ingestão)

### 📥 Fonte de Dados

- Dataset: Amazon Products Dataset 2023
- Origem: Kaggle
- Formato: CSV

### 🛠 Ambiente Utilizado

- Google Colab
- Python (pandas, pyarrow)
- Armazenamento em Parquet

## 🗂 Estrutura Inicial

Após ingestão, o dataset apresentou:

- 1.426.337 registros
- 11 colunas principais
- Tipos mistos (object, float64, int64)

### 🖼 Evidências

#### 📌 Head do dataset

![Head do dataset](../assets/prints/base_dataset_head.jpg)

#### 📌 Informações do dataset

![Estrutura do dataset (.info())](../assets/prints/base_dataset_info.jpg)

## 🧹 Tratamento e Padronização (Silver)

Foram realizadas as seguintes transformações:

### 🔤 Padronização de Nomes

- asin → product_id
- title → product_title
- reviews → review_count
- boughtInLastMonth → units_sold_last_month

### 🧮 Otimização de Tipos

- float64 → float32
- int64 → int32
- object → string
- Criação de colunas booleanas

### 📊 Criação de Novas Variáveis

- price_segment
- has_rating
- weighted_score
- popularity_tier

### 📦 Organização em Camadas

- Bronze → dados brutos
- Silver → dados limpos e tipados
- Persistência em Parquet particionado

### 🔁 Garantia de Reprocessamento

Antes da persistência, o diretório Parquet é removido para evitar duplicidade de dados (overwrite controlado).

Essa estratégia garante idempotência no pipeline e permite reprocessamento seguro do dataset.

## 🔎 Exploração Inicial

Foram realizadas análises exploratórias para entender distribuição e qualidade dos dados:

- 📈 Distribuição de preços
- ⭐ Distribuição de ratings
- 📦 Produtos sem preço
- ⭐ Produtos com rating zero
- 🏷 Distribuição por categoria

Essas análises subsidiaram decisões de:

- Segmentação de preço
- Estratégia de ranking
- Estratégia de amostragem para LLM

## 📤 Saída da Camada Silver

DataFrame final:

- 1.379.629 registros válidos
- 17 colunas estruturadas
- Tipagem otimizada
- Sem nulos críticos

### 🖼 Evidências

#### 📌 Head do dataset

![Head do dataset](../assets/prints/final_dataset_head.jpg)

#### 📌 Informações do dataset

![Estrutura do dataset (.info())](../assets/prints/final_dataset_info.jpg)
