# 📊 Dashboard de Performance Comercial & Pipeline de ETL Moderna 🦆

Um projeto de análise de dados ponta a ponta (End-to-End) que une uma pipeline de ETL de alta performance em Python a um **Dashboard interativo e moderno no Power BI**.

O projeto realiza a ingestão de dados transacionais brutos de vendas, aplica regras de negócio e limpeza de dados (Arquitetura Medallion), calcula Indicadores-Chave de Desempenho (KPIs) e exporta arquivos otimizados para consumo de negócios e integração de BI.

---

## 🎨 Dashboard no Power BI

Abaixo está uma prévia do painel analítico interativo desenvolvido para monitorar os resultados comerciais:

> 💡 **Dica:** Adicione um print do seu dashboard escuro aqui! 
> Basta salvar a imagem dentro do seu repositório (ex: em uma pasta chamada `imagens/`) e apontar o link abaixo:
> `![Dashboard de Performance Comercial](imagens/dashboard_screenshot.png)`

### Principais Indicadores do Painel:
*   **Receita Líquida Total (Faturamento - Descontos):** R$ 8,07 Mil
*   **Ticket Médio por Venda:** R$ 1,35 Mil
*   **Total de Comissões Distribuídas (5%):** R$ 403,50
*   **Performance Mensal e Regional:** Filtros dinâmicos por Vendedor (Ana, Bruno, Carlos) e por Região (Sul, Sudeste).

---

## 📂 Estrutura do Repositório e dos Códigos

O código foi estruturado de forma organizada para separar o ambiente de validação inicial da pipeline final de produção:

```text
├── data/
│   ├── gold_vendas_tratadas.parquet    # Arquivo colunar otimizado para o Power BI
│   └── relatorio_comercial_kpis.xlsx   # Relatório Excel multi-abas para a diretoria
├── src/
│   ├── teste_pandas.py                 # Script de testes e prototipação de KPIs
│   └── main.py                         # Pipeline de ETL de produção (Exportação via DuckDB)
├── .gitignore
├── README.md
└── requirements.txt
