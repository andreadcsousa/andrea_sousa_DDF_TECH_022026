# Case Técnico – Plataforma de Dados com IA (Dadosfera)

## 📌 Visão Geral

Este repositório apresenta uma Prova de Conceito (PoC) para implementação de uma Plataforma de Dados utilizando a Dadosfera SaaS, aplicada a um cenário realista de e-commerce com mais de 1,5 milhão de registros (Amazon Products Dataset 2023).

O objetivo é demonstrar como a Dadosfera pode atuar como camada central de integração, processamento, modelagem, IA e consumo analítico, reduzindo complexidade arquitetural e acelerando a geração de valor.

## 🎯 Problema de Negócio

A empresa possui mais de 1 milhão de produtos cadastrados com:

- Estrutura de catálogo pouco padronizada
- Dificuldade de análise estratégica por categoria
- Baixa capacidade de segmentação inteligente
- Ausência de estrutura adequada para IA e recomendação

Impacto estimado:

- Perda de oportunidades de venda por baixa recomendação inteligente
- Dificuldade em identificar categorias estratégicas
- Alto custo operacional para análises ad-hoc

A solução proposta centraliza, estrutura e enriquece o catálogo utilizando engenharia de dados e GenAI.

## 🗃️ Arquitetura do Projeto

Camadas implementadas (equivalente ao modelo de Data Lake da Dadosfera):

- **RAW (Bronze)** → Dados brutos importados via módulo de Coleta
- **STANDARDIZED (Silver)** → Dados tratados e padronizados via pipelines
- **CURATED (Gold)** → Modelagem analítica (Data Warehouse - Kimball)
- **GenAI Layer** → Extração de features estruturadas via LLM
- **Consumption Layer** → Dashboards (Metabase) e Data App (Streamlit)

## 📂 Estrutura do Repositório

```
app/ → Data App Streamlit
assets/ → Diagramas e imagens do case
dashboard/ → Queries SQL e prints do Metabase
data/ → Dados processados (amostras)
docs/ → Documentação complementar (PMBOK, modelagem, etc.)
notebooks/ → ETL, LLM e análises exploratórias
```

## 📊 Itens do Case e Documentação

A documentação completa de cada etapa do case está disponível na pasta `docs/`, organizada conforme o template oficial da Dadosfera:

| Item | Descrição            | Status      | Documentação                          |
| ---- | -------------------- | ----------- | ------------------------------------- |
| 1    | Planejamento (PMBOK) | Concluído   | [Ver](docs/01_planejamento_pmbok.md)  |
| 2    | Base de Dados        | Concluído   | [Ver](docs/02_base_de_dados.md)       |
| 3    | Integrar e Explorar  | Parcial     | [Ver](docs/03_integrar_explorar.md)   |
| 4    | Data Quality         | Documentado | [Ver](docs/04_data_quality.md)        |
| 5    | GenAI / LLM          | Concluído   | [Ver](docs/05_processar_genai_llm.md) |
| 6    | Modelagem de Dados   | Concluído   | [Ver](docs/06_modelagem_dados.md)     |
| 7    | Análise / Dashboard  | Pendente    | [Ver](docs/07_analisar_dashboard.md)  |
| 8    | Pipelines            | Pendente    | [Ver](docs/08_pipelines.md)           |
| 9    | Data App             | Concluído   | [Ver](docs/09_data_app.md)            |
| 10   | Apresentação         | Pendente    | [Ver](docs/10_apresentacao.md)        |

## 🧠 Tecnologias e Ferramentas

### 🗄️ Banco de Dados

- **PostgreSQL (Cloud):** Base transacional pública utilizada como origem operacional do e-commerce.
- Utilizado para simular ambiente transacional real e permitir integração via módulo de Coleta da Dadosfera.

### 🏗️ Engenharia de Dados

- **Python (Google Colab):** Processamento e transformação dos dados.
- **Pandas / PyArrow:** Manipulação e persistência em formato analítico.
- **Parquet:** Armazenamento otimizado para análises.
- **Estruturação em camadas:** RAW → STANDARDIZED → CURATED.

### 🧱 Modelagem de Dados

- **Modelagem Dimensional (Kimball):** Construção de Data Warehouse com visão analítica orientada a negócio.
- Separação em tabelas fato e dimensões para suportar análises por categoria e série temporal.

### 🤖 Inteligência Artificial

- **OpenAI API (LLM):** Extração de features estruturadas a partir de descrições textuais.
- Enriquecimento semântico do catálogo para segmentação e futuras aplicações de recomendação.

### 📊 Visualização e Consumo Analítico

- **Metabase (via Dadosfera):** Dashboards internos na plataforma.
- **Power BI:** Análises complementares externas e comparação arquitetural.

### 🌐 Plataforma de Dados

- **Dadosfera SaaS:** Camada central de integração, catalogação, pipelines e governança.

### 📱 Data App

- **Streamlit:** Aplicação interativa para exploração do catálogo enriquecido (CURATED + GenAI Features).

### 💻 Ambiente de Desenvolvimento

- Google Colab
- Visual Studio Code

### 📦 Versionamento e Documentação

- GitHub

## ▶️ Como Reproduzir

### Pré-requisitos

- Python 3.10+
- Variável de ambiente OPENAI_API_KEY configurada
- Dataset com ~1.5M registros

### Passos

1. Baixar o dataset via Kaggle
2. Executar notebook 01 (ETL Silver)
3. Executar notebook 02 (Gold)
4. Executar notebook 03 (LLM)
5. Rodar Streamlit em `app/app.py`

## 🎥 Apresentação

O vídeo apresenta:

- Problema de negócio
- Arquitetura proposta
- Demonstração da plataforma
- Viabilidade de substituição da arquitetura atual

Link do vídeo (Unlisted): [Apresentação do Case]()

## 🚀 Conclusão

A solução proposta demonstra como a Dadosfera pode substituir arquiteturas fragmentadas, centralizando integração, processamento, governança e IA em uma única plataforma, reduzindo custo operacional e tempo até geração de valor.
