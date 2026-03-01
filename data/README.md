# Data Directory

O dataset completo **Amazon Products Dataset 2023 (1.4M registros)** não é versionado neste repositório devido ao seu tamanho.

## 📥 Como Reproduzir

1. Baixe o dataset no Kaggle:
   https://www.kaggle.com/datasets/asaniczka/amazon-products-dataset-2023-1-4m-products

> [!WARNING]
> Não é necessário baixar de fato o dataset, é possível conectar o Colab direto ao Kaggle.

2. Execute o notebook:
   `01_etl_ingestao_limpeza_silver.ipynb`

3. Em seguida execute:
   - `02_gold_series_temporal_e_metricas.ipynb`
   - `03_llm_feature_extraction.ipynb`

## 📁 Estrutura Esperada (Local)

```text
data/
 ├── raw/        # arquivos originais do kaggle
 ├── sample/     # amostras pequenas versionadas
 └── README.md
```

### 🧪 Samples Versionados

A pasta data/sample/ contém pequenas amostras para:

- Demonstração
- Testes rápidos
- Execução do Data App sem necessidade do dataset completo

> [!IMPORTANT]
> As camadas Silver e Gold são geradas dinamicamente via notebooks e não são versionadas neste repositório.

**Isso garante:**

- Reprodutibilidade
- Controle de tamanho do repositório
- Separação entre código e dados
