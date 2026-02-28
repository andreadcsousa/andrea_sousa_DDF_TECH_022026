# Planejamento do Projeto (PMBOK)

## 🎯 Objetivo do Projeto

Construir uma Plataforma de Dados para centralizar, estruturar e enriquecer um catálogo de e-commerce com mais de 1 milhão de produtos, permitindo análises estratégicas e uso de IA para geração de valor.

---

# 📌 Escopo do Projeto

Inclui:

- Ingestão de dados (>1M registros)
- Tratamento e padronização (Silver)
- Modelagem analítica (Gold)
- Geração de série temporal
- Extração de features via LLM
- Criação de Dashboard analítico
- Criação de Data App com Streamlit
- Pipeline automatizado
- Apresentação executiva

Não inclui:

- Deploy produtivo em ambiente corporativo real
- Integração com ERP/CRM externo
- Monitoramento contínuo em produção

---

# 🗂 Estrutura Analítica do Projeto (WBS)

1. Planejamento
2. Ingestão e Integração
3. Tratamento e Padronização
4. Modelagem de Dados
5. Enriquecimento com IA
6. Análise e Visualização
7. Desenvolvimento de Data App
8. Pipeline e Catalogação
9. Apresentação Executiva

---

# 📌 Metodologia de Gestão

O projeto foi estruturado utilizando abordagem Kanban, com organização em Epics e Tasks no Jira.

Colunas utilizadas:

- Backlog
- To Do
- In Progress
- Review
- Done

A organização por Epics permitiu controle incremental da entrega e mitigação de riscos dentro do prazo de 4 dias.

---

# ⚠️ Análise de Riscos

| Risco                | Impacto             | Mitigação                               |
| -------------------- | ------------------- | --------------------------------------- |
| Alto volume de dados | Lentidão            | Uso de tipos otimizados (float32/int32) |
| Custo de API LLM     | Financeiro          | Uso de amostra estratificada            |
| Dataset sem data     | Limitação analítica | Geração de série temporal sintética     |
| Prazo curto (4 dias) | Pressão             | Planejamento incremental                |

---

# 💰 Estimativa de Custos (Simulação)

- Infraestrutura Dadosfera: SaaS
- Processamento LLM: custo controlado por amostra
- Streamlit Cloud: gratuito
- Ambiente Colab: gratuito

Estimativa: Baixo custo inicial comparado à arquitetura distribuída tradicional.

---

# 🔗 Interdependências

- Gold depende da Silver
- LLM depende da Silver
- Dashboard depende da Gold
- Data App depende da Gold e LLM
- Apresentação depende de todos os itens anteriores

---

# 🎯 Pontos Críticos

- Garantir consistência do schema
- Controlar volume da amostra para LLM
- Manter rastreabilidade das transformações
- Documentação clara e reprodutível

---

# 📊 Justificativa Estratégica

O planejamento foi estruturado para demonstrar como a Dadosfera pode reduzir complexidade arquitetural, centralizando ingestão, processamento, modelagem, IA e visualização em uma única plataforma.
