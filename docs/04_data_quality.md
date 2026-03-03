# Data Quality

Este documento apresenta a estratégia de qualidade de dados aplicada após a ingestão na camada RAW e antes da modelagem na camada CURATED, garantindo governança e confiabilidade analítica.

## 🎯 Objetivo da Análise de Qualidade

Garantir que o dataset esteja consistente, íntegro e adequado para:

- Modelagem dimensional (Kimball)
- Construção de métricas analíticas
- Enriquecimento via LLM

## 🧪 Estratégia de Validação Automatizada

A validação de qualidade foi estruturada utilizando abordagem compatível com frameworks como Great Expectations ou Soda-Core, permitindo definição formal de regras e validações reprodutíveis.

**As verificações incluíram:**

- Expectativas de domínio (rating entre 0 e 5)
- Expectativas de integridade (product_id único)
- Expectativas de completude (campos críticos não nulos)
- Expectativas de consistência referencial (category_id válido)

## 📊 Análise de Completude (Nulos)

Nenhuma coluna crítica apresentou percentual de nulos superior ao limiar aceitável de 5%.

### 🔍 Verificação de valores ausentes

Foi executada análise de nulos por coluna:

- product_title → percentual residual muito baixo
- price → valores zero identificados
- rating → presença de valores zero
- demais colunas → sem nulos relevantes

### 📷 Evidência

#### 📌 Análise de Nulos

![Análise de nulos](../assets/prints/04_data_quality_01_null_analysis.jpg)

## 📈 Análise de Distribuição

Outliers extremos foram identificados, porém mantidos para preservar integridade do domínio original.

### 💰 Preço

- Preço mínimo: $0.00
- Preço máximo: ~$19.731
- Forte concentração em faixa < $100

### ⭐ Rating

- Alta concentração entre 4.0 e 5.0
- 131.023 produtos com rating zero

### 📷 Evidências

#### 📌 Distribuição de Preços

![Distribuição de Preços](../assets/prints/03_gold_01_price_distribution.jpg)

#### 📌 Distribuição de Ratings

![Distribuição de Ratings](../assets/prints/03_gold_02_rating_distribution.jpg)

### 🔎 Validação de Domínio

- rating dentro do intervalo esperado (0 a 5)
- price ≥ 0

## 🧮 Padronização e Otimização de Tipagem (STANDARDIZED)

**Foram aplicadas otimizações:**

- float64 → float32
- int64 → int32
- object → string
- criação de colunas booleanas

**Objetivo:**

- Redução de uso de memória
- Melhor performance em processamento

## 🏷️ Análise de Integridade

- product_id validado como chave única (sem duplicidade)
- category_id consistente com tabela de categorias (merge validado)
- Nenhum registro duplicado após tratamento

## 📋 Regras de Qualidade Definidas

| Regra                  | Tipo        | Critério                                |
| ---------------------- | ----------- | --------------------------------------- |
| product_id único       | Integridade | Sem duplicidade                         |
| rating entre 0 e 5     | Domínio     | Valores fora do intervalo são inválidos |
| price >= 0             | Domínio     | Valores negativos inválidos             |
| category_id válido     | Referencial | Deve existir na tabela Categories       |
| product_title não nulo | Completude  | Campo obrigatório                       |

## ⚠️ Pontos de Atenção

- Produtos com preço zero podem representar:
  - Produtos descontinuados
  - Erro de origem
- Rating zero pode indicar ausência de avaliações
- Dataset não possui data real

## ✅ Conclusão da Qualidade

Após as verificações realizadas, o dataset apresenta:

- Consistência estrutural
- Integridade referencial
- Tipagem otimizada para performance
- Adequação para modelagem dimensional
- Estrutura apropriada para enriquecimento via LLM

O dataset está apto para evolução para camada CURATED e aplicação de pipelines automatizados de validação contínua.

> [!NOTE]
> Os riscos identificados foram documentados e considerados nas decisões arquiteturais subsequentes.

## 🔁 Reprodutibilidade

Todas as verificações foram executadas via notebook [ETL de Ingestão e Limpeza](../notebooks/01_etl_ingestao_limpeza_silver.ipynb), permitindo reprocessamento e auditoria completa.
