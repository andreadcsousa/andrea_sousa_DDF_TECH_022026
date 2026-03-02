# Case Técnico – Plataforma de Dados com IA (Dadosfera)

## 📌 Visão Geral

Este repositório apresenta a implementação de uma Plataforma de Dados para otimização de catálogo de produtos em um e-commerce de grande escala, utilizando o dataset Amazon Products Dataset 2023.

O objetivo é demonstrar, ponta a ponta, o ciclo de vida dos dados, desde ingestão até geração de valor com IA e Data Apps.

## 🎯 Problema de Negócio

A empresa possui mais de 1 milhão de produtos cadastrados com:

- Estrutura de catálogo pouco padronizada
- Dificuldade de análise estratégica por categoria
- Baixa capacidade de segmentação inteligente
- Ausência de estrutura adequada para IA e recomendação

A solução proposta centraliza, estrutura e enriquece o catálogo utilizando engenharia de dados e GenAI.

## 🏗 Arquitetura do Projeto

Camadas implementadas:

- **Bronze** → Dados brutos
- **Silver** → Dados tratados, padronizados e enriquecidos
- **Gold** → Tabelas analíticas e série temporal
- **GenAI** → Extração de features via LLM
- **Data App** → Aplicação interativa com Streamlit

## 📂 Estrutura do Repositório

```
app/
assets/
data/
docs/
notebooks/
```

## 📊 Itens do Case

| Item | Descrição            | Status |
| ---- | -------------------- | ------ |
| 0    | Planejamento (PMBOK) | ✅     |
| 1    | Base de Dados        | ✅     |
| 2    | Integrar             | ✅     |
| 3    | Explorar             | ✅     |
| 4    | Data Quality         | ✅     |
| 5    | GenAI / LLM          | ✅     |
| 6    | Modelagem de Dados   | ✅     |
| 7    | Análise / Dashboard  | ⏳     |
| 8    | Pipelines            | ⏳     |
| 9    | Data App             | ⏳     |
| 10   | Apresentação         | ⏳     |

## 🧠 Tecnologias e Ferramentas

### Engenharia de Dados

- Python
- Pandas
- PyArrow
- Parquet

### Inteligência Artificial

- OpenAI API (LLM)
- Feature Engineering via GenAI

### Visualização

- Metabase (via Dadosfera)

### Plataforma de Dados

- Dadosfera SaaS

### Aplicação

- Streamlit

### Ambiente de Desenvolvimento

- Google Colab

### Versionamento e Documentação

- GitHub

## ▶️ Como Reproduzir

1. Baixar o dataset via Kaggle
2. Executar notebook 01 (ETL Silver)
3. Executar notebook 02 (Gold)
4. Executar notebook 03 (LLM)
5. Rodar Streamlit em `app/app.py`

## 🎥 Apresentação

Link do vídeo (Unlisted):
[INSERIR LINK AQUI]

## 🚀 Conclusão

Este case demonstra como podemos atuar como a plataforma central para transformar dados brutos em valor estratégico, reduzindo complexidade arquitetural e acelerando iniciativas de IA.
