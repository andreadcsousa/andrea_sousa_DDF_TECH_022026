# Integrar e Explorar

Este documento descreve as etapas de ingestão, padronização e exploração inicial do dataset de e-commerce.

## 🔌 Integração na Plataforma Dadosfera

Os arquivos originais foram carregados utilizando o módulo **Coletar** da Dadosfera, conforme solicitado no case.

- Upload dos arquivos originais
- Criação automática de ativos no **Catálogo**
- Organização inicial na zona **RAW**

### 🖼 Evidência:

#### 📌 Uploads no catálogo da Dadosfera

![Uploads de arquivos raw](../assets/prints/raw_ecommerce_amazon_uploads.jpg)

> [!WARNING]
> A plataforma aceita arquivos com limite de até **250MB** por upload.
>
> O arquivo CSV principal de produtos ultrapassava esse tamanho.  
> Para viabilizar o carregamento, foi realizada a conversão do arquivo para formato **Parquet**, utilizando a ferramenta:
> https://observablehq.com/@observablehq/csv-to-parquet
>
> A conversão reduziu significativamente o tamanho do arquivo, permitindo o upload no catálogo sem perda de estrutura.

> [!TIP]
> A escolha pelo formato Parquet também está alinhada com boas práticas de Data Lake, por ser colunar, comprimido e mais eficiente para processamento analítico.

### 🏷️ Catalogação e Governança

Após o carregamento, foram aplicadas boas práticas de governança:

- Descrição do ativo preenchida
- Tags aplicadas (ecommerce, raw, amazon, case-dadosfera)
- Owner definido
- Dicionário de Dados documentado

### 🖼 Evidência:

- Print da tela de edição do ativo
- Print da descrição de uma coluna

## 📥 Ingestão Técnica (Colab)

- Fonte Kaggle
- Ambiente
- Leitura CSV
- Estrutura Inicial (.info + head)

### 🔎 Exploração Inicial

- Distribuição de preços
- Distribuição de ratings
- Produtos sem preço
- Produtos rating zero
- Decisões tomadas

### 🧹 Tratamento e Padronização (Silver)

- Padronização de nomes
- Otimização de tipos
- Novas variáveis
- Organização em camadas

### 🔁 Garantia de Reprocessamento

- Overwrite controlado
- Idempotência

## 🗂 Estrutura Inicial

Após ingestão, o dataset apresentou:

- 1.426.337 registros
- 11 colunas principais
- Tipos mistos (object, float64, int64)

### 🖼 Evidências

#### 📌 Estrutura inicial (RAW)

![Head do dataset](../assets/prints/base_dataset_head.jpg)

![Estrutura do dataset (.info())](../assets/prints/base_dataset_info.jpg)

## 📤 Saída da Camada Silver

DataFrame final:

- 1.379.629 registros
- 17 colunas
- Tipagem otimizada

### 🖼 Evidências

#### 📌 Estrutura final (Silver)

![Head do dataset](../assets/prints/final_dataset_head.jpg)

![Estrutura do dataset (.info())](../assets/prints/final_dataset_info.jpg)
