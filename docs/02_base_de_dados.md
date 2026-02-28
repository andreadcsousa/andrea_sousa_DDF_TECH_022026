# Base de Dados

## Dataset Selecionado

Amazon Products Dataset 2023
Total de registros: 1.426.337 produtos
Domínio: E-commerce

## Justificativa da Escolha

O dataset foi selecionado por:

- Escala adequada (> 100.000 registros)
- Representação realista de um grande catálogo de e-commerce
- Presença de variáveis relevantes para análise estratégica:
  - Preço
  - Avaliações (rating)
  - Volume de vendas
  - Categoria
  - Indicador de Best Seller
- Campo textual (product_title) adequado para enriquecimento via LLM

## Estrutura dos Dados

Principais colunas:

- product_id
- product_title
- category_id
- category_name
- price
- list_price
- rating
- review_count
- units_sold_last_month
- is_best_seller

## Potencial Analítico

O dataset permite:

- Análise estrutural de catálogo
- Segmentação por faixa de preço
- Análise de performance por categoria
- Geração de série temporal sintética
- Enriquecimento de atributos via GenAI

## Conexão com o Problema de Negócio

A base permite simular um cenário real de e-commerce com mais de 1 milhão de produtos, onde:

- A padronização do catálogo é crítica
- A análise por categoria impacta estratégia comercial
- O enriquecimento via IA habilita recomendação e segmentação inteligente
