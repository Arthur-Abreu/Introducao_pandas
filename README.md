# 📊 Pipeline de Tratamento e Análise de Vendas com Pandas

Este projeto é um script de teste prático utilizando a biblioteca **Pandas** para simular um fluxo real de engenharia e análise de dados (ETL). O script recebe uma base de dados bruta de vendas, realiza a limpeza e o tratamento dos dados, calcula métricas de negócio (KPIs) e exporta os resultados tratados.

## 🚀 Funcionalidades do Script

O script simula as seguintes etapas de um pipeline de dados:

1. **Limpeza e Tratamento de Dados (Data Cleaning):**
   - Substituição de vendedores nulos por "Não identificado" (garantindo rastreabilidade).
   - Conversão segura de colunas de texto/mistas para números (`valor_venda` e `desconto`).
   - Tratamento de valores inválidos ou vazios (`NaN`), substituindo-os por `0`.
   - Filtragem ativa para analisar apenas vendas com status **"Concluido"**.

2. **Transformação de Dados:**
   - Criação da métrica de **Valor Líquido** (Valor Bruto - Desconto).
   - Cálculo automático de **Comissão** comercial (5% sobre o valor líquido).

3. **Cálculo de KPIs (Métricas de Negócio):**
   - Receita líquida total por vendedor.
   - Receita líquida total por região geográfica (Sul e Sudeste).
   - Ticket médio por vendedor.
   - Ranking de performance de vendedores em ordem decrescente.
   - Faturamento líquido mensal.

4. **Exportação de Resultados:**
   - O script gera automaticamente 3 arquivos de saída para consumo de outras equipes ou ferramentas de BI (como Power BI ou Tableau):
     - `vendas_tratadas.csv`
     - `ranking_vendedor.csv`
     - `receita_mensal.csv`

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Pandas** (Tratamento e análise dos dados)
- **Openpyxl** (Suporte para manipulação de arquivos Excel)

---

## 💻 Como Executar o Projeto

### Prerrequisitos

Antes de rodar o script, você precisa ter o Python instalado e as bibliotecas do projeto. Você pode instalá-las rodando o comando abaixo no seu terminal:

```bash
pip install pandas openpyxl
