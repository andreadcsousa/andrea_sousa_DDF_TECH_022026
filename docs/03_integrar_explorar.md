# Integrar e Explorar

Este documento descreve as etapas de integração na plataforma, governança, ingestão técnica, exploração inicial dos dados e preparação da camada Standardized para posterior modelagem analítica.

## 🔌 Integração na Plataforma de Dados (Zona RAW)

Os arquivos originais foram carregados utilizando o módulo **Coletar**, conforme solicitado no case técnico. Foram realizadas as seguintes ações:

- Upload dos arquivos originais (Produtos e Categorias)
- Criação automática de ativos no **Catálogo**
- Padronização dos nomes técnicos dos ativos
- Classificação na zona **RAW** do Data Lake
- Validação do volume de registros após ingestão

### 📂 Ativos Criados

- `RAW_ECOMMERCE_AMAZON_PRODUCTS`
- `RAW_ECOMMERCE_AMAZON_CATEGORIES`

### 📸 Evidências:

#### 📌 Upload no catálogo

![Uploads de arquivos raw](../assets/prints/03_dadosfera_03_raw_upload_confirmation.jpg)

> [!WARNING]
> A plataforma aceita arquivos com limite de até **250MB** por upload.
>
> O arquivo CSV principal de produtos ultrapassava esse tamanho.
> Para viabilizar o carregamento, foi realizada a conversão para formato **Parquet**, utilizando ferramenta específica de conversão.
>
> A conversão reduziu significativamente o tamanho do arquivo, permitindo o upload sem perda estrutural e com maior eficiência de armazenamento e leitura.

> [!TIP]
> O uso de Parquet está alinhado com boas práticas de Data Lake, por ser um formato colunar, comprimido e otimizado para processamento analítico.

## 🏷️ Catalogação e Governança

Após o carregamento, foram aplicadas boas práticas de governança de dados:

- Descrição detalhada do ativo preenchida no catálogo
- Aplicação de tags (ecommerce, raw, catalog, case-tecnico)
- Definição de owner responsável pelo ativo
- Classificação na zona RAW do Data Lake
- Documentação do **Dicionário de Dados** com padronização técnica dos nomes das colunas

### 📘 Dicionário de Dados – Products (RAW_ECOMMERCE_AMAZON_PRODUCTS)

| Coluna                 | Descrição                                                |
| ---------------------- | -------------------------------------------------------- |
| ASIN                   | Identificador único do produto na Amazon (chave natural) |
| TITLE                  | Nome do produto                                          |
| IMGURL                 | URL da imagem principal                                  |
| PRODUCTURL             | URL da página do produto                                 |
| STARS                  | Avaliação média do produto (0 a 5)                       |
| REVIEWS                | Quantidade total de avaliações                           |
| PRICE                  | Preço atual em USD                                       |
| LISTPRICE              | Preço original antes de desconto                         |
| CATEGORY_ID            | Identificador da categoria (chave estrangeira)           |
| ISBESTSELLER           | Indicador booleano de best seller                        |
| BOUGHTINLASTMONTH      | Volume estimado de vendas no último mês                  |
| \_PROCESSING_TIMESTAMP | Timestamp interno gerado automaticamente na ingestão     |

### 📘 Dicionário de Dados – Categories (RAW_ECOMMERCE_AMAZON_CATEGORIES)

| Coluna                 | Descrição                                            |
| ---------------------- | ---------------------------------------------------- |
| ID                     | Identificador único da categoria (chave primária)    |
| CATEGORY_NAME          | Nome textual da categoria                            |
| \_PROCESSING_TIMESTAMP | Timestamp interno gerado automaticamente na ingestão |

### 📸 Evidências:

#### 📌 Descrição dos ativos no catálogo

![Catalogação dos produtos](../assets/prints/03_dadosfera_02_raw_products_catalog.jpg)

![Catalogação das categorias](../assets/prints/03_dadosfera_01_raw_categories_catalog.jpg)

## 🗂️ Organização em Camadas (Modelo Arquitetural)

Os dados foram organizados seguindo o padrão arquitetural de camadas analíticas:

- **RAW** → Dados brutos carregados diretamente da fonte (Kaggle), sem transformações estruturais.
- **Standardized** → Dados tratados, padronizados, tipados e preparados para modelagem analítica.
- **Curated** → Dados modelados dimensionalmente e preparados para consumo analítico (dashboards e Data App).

## 📥 Ingestão Técnica (Colab)

### 📌 Fonte de Dados

- Dataset: Amazon Products Dataset 2023
- Origem: Kaggle (dataset público)
- Formato original: CSV
- Volume: 1.426.337 registros

### 🛠️ Ambiente Utilizado

- Google Colab
- Python (pandas, pyarrow)
- Conversão e persistência em formato Parquet
- Otimização de tipagem (float32 / int32)

> [!NOTE]
> O processamento inicial foi realizado em ambiente controlado (Colab) para validação técnica, otimização de tipagem e verificação de integridade dos dados. A orquestração definitiva e materialização via pipeline são descritas na etapa de pipelines do projeto.

## 🔎 Exploração Técnica dos Dados (EDA)

Foram realizadas análises exploratórias para compreensão da qualidade, distribuição e comportamento das variáveis:

- Distribuição de preços (price e list_price)
- Distribuição de avaliações (rating)
- Identificação de produtos sem preço válido
- Identificação de produtos com rating igual a zero
- Análise de cardinalidade por categoria
- Avaliação de consistência entre preço atual e preço de lista

Essas análises subsidiaram decisões de:

- Definição de faixas de segmentação de preço
- Estratégia de ranking e priorização de produtos
- Construção de métricas derivadas (popularidade e desconto percentual)
- Estratégia controlada de amostragem para processamento via LLM
- Tratamento de valores nulos e inconsistências na camada Standardized

### 📸 Evidências:

#### 📌 Gráfico de distribuição de preços

![Distribuição de Preços](../assets/prints/03_gold_01_price_distribution.jpg)

#### 📌 Gráfico de distribuição de ratings

![Distribuição de Ratings](../assets/prints/03_gold_02_rating_distribution.jpg)

## 🧹 Tratamento e Padronização (Camada Standardized)

### 🔤 Padronização de Nomes

- asin → product_id
- title → product_title
- imgUrl → image_url
- productURL → product_url
- reviews → review_count
- boughtInLastMonth → units_sold_last_month
- isBestSeller → is_best_seller
- listPrice → list_price

### 🧮 Otimização de Tipos

- float64 → float32
- int64 → int32
- object → string
- Conversão explícita de flags para boolean
- Identificação preliminar de valores nulos e inconsistentes

### 📊 Criação de Novas Variáveis

- discount_percentage (derivado de price e list_price)
- price_segment
- has_rating
- weighted_score (rating ponderado por review_count)
- popularity_tier

## 🔁 Garantia de Reprocessamento

Antes da persistência, o diretório Parquet é removido para evitar duplicidade de dados. Essa estratégia garante:

- Overwrite controlado
- Idempotência do processamento
- Reprocessamento seguro sem acúmulo de versões inconsistentes

## 📤 Saída da Camada Standardized

DataFrame final estruturado para posterior materialização na camada Standardized:

- 1.379.629 registros válidos
- 17 colunas estruturadas
- Tipagem otimizada (float32 / int32 / string / boolean)
- Ausência de nulos críticos nas colunas analíticas

### 📸 Evidências:

#### 📌 Estrutura final (.info)

![Estrutura do dataset (.info())](../assets/prints/03_gold_04_final_dataset_info.jpg)

#### 📌 Head do DataFrame Standardized

![Head do dataset](../assets/prints/03_gold_03_final_dataset_head.jpg)

## 🔄 Próxima Etapa: Microtransformação e Pipeline

A camada Standardized representa a primeira camada analítica confiável do projeto, servindo como base para as etapas subsequentes de qualidade, enriquecimento semântico, modelagem dimensional e consumo analítico. Ela servirá como base para as etapas seguintes do projeto, incluindo enriquecimento semântico via LLM, modelagem dimensional na camada Curated e materialização das transformações por meio de pipelines automatizados.

- Versionamento das transformações
- Execução incremental
- Governança centralizada
- Evolução estruturada para a camada Curated
