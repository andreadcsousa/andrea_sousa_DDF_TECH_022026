# Amazon Catalog Intelligence — Plataforma de Dados com IA

## 📌 Resumo Executivo

Este projeto demonstra a construção de uma **plataforma analítica de dados para e-commerce**, integrando engenharia de dados, enriquecimento semântico via IA e visualização analítica.

A solução consolida um fluxo completo de dados:

`Ingestão → Qualidade → Enriquecimento com LLM → Modelagem → Dashboards → Data App → Pipeline automatizado.`

O resultado é uma arquitetura capaz de transformar um catálogo de produtos em **inteligência analítica acionável**.

## 🎯 Problema de Negócio

Empresas de e-commerce frequentemente possuem grandes catálogos de produtos distribuídos em múltiplos sistemas.

**Esse cenário dificulta:**

- análise de performance de produtos
- identificação de categorias estratégicas
- segmentação inteligente do catálogo
- utilização de inteligência artificial sobre dados não estruturados

O desafio consiste em centralizar esses dados em uma plataforma analítica e aplicar enriquecimento com IA para gerar novos insights estratégicos.

## 🧱 Arquitetura de Dados

| Camada       | Função                                |
| ------------ | ------------------------------------- |
| RAW          | Dados brutos ingeridos                |
| STANDARDIZED | Limpeza e padronização                |
| ENRICHED     | Atributos semânticos extraídos via IA |
| CURATED      | Modelagem analítica dimensional       |
| CONSUMO      | Dashboards e Data App                 |

## 🔄 Fluxo da Plataforma de Dados

O ciclo de dados implementado no projeto segue as etapas:

1️⃣ **Ingestão**  
Dados brutos do catálogo são integrados na plataforma.

2️⃣ **Padronização (Standardized)**  
Tratamento, tipagem e criação de atributos derivados.

3️⃣ **Enriquecimento com IA (Enriched)**  
Extração de marca, tipo de produto e atributos via LLM.

4️⃣ **Modelagem Analítica (Curated)**  
Estrutura dimensional para consultas analíticas.

5️⃣ **Visualização Analítica**  
Dashboards em Metabase e Power BI.

6️⃣ **Exploração Interativa**  
Data App em Streamlit para análise granular.

7️⃣ **Automação**  
Pipeline orquestra o fluxo completo de dados.

## 📟 Tecnologias Utilizadas

### Plataforma de Dados

- Dadosfera SaaS

### Engenharia de Dados

- Python
- Pandas
- DuckDB

### Armazenamento

- PostgreSQL
- Parquet

### Inteligência Artificial

- OpenAI API (LLM)

### Visualização

- Metabase
- Power BI

### Aplicação Analítica

- Streamlit

## 🗂️ Estrutura da Documentação

| Documento              | Descrição                |
| ---------------------- | ------------------------ |
| 01_planejamento_pmbok  | Planejamento do projeto  |
| 02_base_de_dados       | Descrição do dataset     |
| 03_integrar_explorar   | Ingestão e catalogação   |
| 04_data_quality        | Estratégia de qualidade  |
| 05_processar_genai_llm | Enriquecimento via IA    |
| 06_modelagem_dados     | Modelo dimensional       |
| 07_analisar_dashboard  | Dashboards analíticos    |
| 08_pipelines           | Automação e orquestração |
| 09_data_app            | Aplicação interativa     |

## 🌐 Acessos

- [Dashboard Dadosfera](http://metabase-treinamentos.dadosfera.ai/public/dashboard/395efcb8-bcda-45bf-8c7e-c4c26b53f866)

- [Dashboard Power BI](https://app.powerbi.com/view?r=eyJrIjoiNjhmNDg5MWMtMGU0Yi00ZjI5LTg5MTMtNTRiNTM5Y2RkOTAzIiwidCI6ImEzZTU3Zjc1LTU5YTktNDFkOS05ZGIwLTA0YmM0ODg2YWY3NyJ9&pageName=5f22c10194a1a41d956c)

- [Data App Streamlit](https://acs-amazon-catalog-app.streamlit.app/)

## 📊 Resultados do Projeto

**A solução implementada permite:**

- Centralização do catálogo em uma plataforma analítica
- Extração de atributos semânticos via IA
- Modelagem dimensional para análise estratégica
- Dashboards executivos para tomada de decisão
- Exploração interativa de dados via Data App
- Automação do fluxo de dados por pipeline

O projeto demonstra como uma plataforma de dados moderna pode transformar dados operacionais em **insights estratégicos acionáveis**.
