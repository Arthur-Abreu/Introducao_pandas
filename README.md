
1. main.py (Pipeline de Dados Otimizado para Produção)
Uma evolução do script inicial, focada em automação, performance e entrega corporativa de alta maturidade:

Persistência Analítica (Parquet): Utiliza o DuckDB para exportar de forma ultraveloz a base tratada da camada Silver em formato Parquet (data/gold_vendas_tratadas.parquet). O formato colunar garante máxima compactação, velocidade de leitura para o BI e preservação nativa dos tipos de dados.

Carga Centralizada em Excel (Multi-abas): Utiliza o motor do openpyxl para consolidar todas as tabelas e KPIs gerados em um único relatório executivo (data/relatorio_comercial_kpis.xlsx), distribuídos de maneira elegante em abas dedicadas:

📑 Vendas_Tratadas (Base detalhada e limpa)

🏆 Ranking_Vendedores (Visão de performance)

📍 Receita_por_Regiao (Geolocalização das vendas)

📅 Receita_Mensal (Sazonalidade e evolução)

💻 Estrutura de Código: Script a Script
O projeto é modularizado em dois scripts principais que mostram a evolução desde a análise exploratória até o pipeline estruturado em produção:

2. teste_pandas.py (Análise Exploratória e Exploração de KPIs)
Focado no tratamento inicial dos dados utilizando Pandas. É o script ideal para homologação rápida de regras de negócio.

Limpeza de Nulos: Identificação de vendedores ausentes (atribuindo "Não identificado" para rastreabilidade) e preenchimento de valores monetários nulos com 0.

Segurança de Tipagem: Conversão segura usando pd.to_numeric(..., errors="coerce") para evitar quebras se houver caracteres inválidos ou texto em colunas numéricas (cenário comum em planilhas manuais).

Definição de Métricas Comerciais:

Valor Líquido = Valor Venda - Desconto

Comissão = Valor Líquido * 5%

Exportação Inicial: Gera arquivos CSVs isolados para auditoria rápida (vendas_tratadas.csv, ranking_vendedor.csv, receita_mensal.csv).

📈 Integração e Relatório no Power BI
Dashboard de Performance Comercial (dashboard.png)

Dashboard de Performance Comercial

<img width="1315" height="736" alt="image" src="https://github.com/user-attachments/assets/c45d27e5-4501-4e85-adb4-94e45d63bc6f" />

O resultado final do pipeline é exposto em um painel executivo moderno e interativo, projetado para apoiar a tomada de decisão rápida e estratégica da liderança comercial.

![Dashboard de Performance Comercial](dashboard.png)

### 🔍 Principais Indicadores e Insights Gerados

O painel consome os dados tratados da camada **Gold** e oferece análises em tempo real:

* **Métricas Principais (KPIs):**
  * **Receita Líquida (R$ 8,07 Mil):** O faturamento real acumulado das vendas concluídas, já descontando todas as concessões.
  * **Ticket Médio (R$ 1,35 Mil):** O valor médio por pedido concluído, indicando a força de vendas do time por transação.
  * **Total de Comissões (R$ 403,50):** O montante dinâmico calculado com base na regra de negócio de 5% sobre o valor líquido.
* **Desempenho por Vendedor (Ranking):**
  * **Ana** lidera com folga o ranking individual de faturamento (R$ 3,6 Mil), seguida por **Carlos** (R$ 2,7 Mil) e **Bruno** (R$ 1,9 Mil).
* **Distribuição Geográfica (Receita por Região):**
  * Identificação de forte concentração de receita na região **Sul** (77,08% do total, representando R$ 6,22 Mil), em contraste com o **Sudeste** que representa 22,92% (R$ 1,85 Mil).
* **Análise de Sazonalidade (Evolução Mensal):**
  * O gráfico de linhas expõe uma tendência clara de queda consecutiva no faturamento de Janeiro para Março, sinalizando a necessidade imediata de novas campanhas ou incentivos de vendas.
* **Filtros Interativos:**
  * Segmentadores dinâmicos no topo permitem filtrar instantaneamente todos os visuais por vendedor selecionado, permitindo análises individuais personalizadas.

---

### ⚙️ Diferencial Técnico: Integração Nativa com Parquet

Ao contrário da abordagem tradicional de conectar o Power BI a arquivos planos como Excel ou CSV, este projeto utiliza o arquivo **`gold_vendas_tratadas.parquet`** como fonte única de verdade:

1. **Eficiência Analítica (Compactação Colunar):** O Power BI lê arquivos Parquet com velocidade extrema. Em grandes volumes de dados (milhões de registros), o tempo de atualização e o consumo de memória do dashboard são drasticamente reduzidos.
2. **Imutabilidade de Tipos (Schema):** Evita o problema clássico de o Power Query alterar formatos de dados incorretamente durante a carga. Como o Parquet guarda a tipagem nativa do Pandas, os dados entram estruturados sem necessidade de novos tratamentos no BI.
3. **Padrão Moderno de Data Lakehouse:** O modelo implementado reflete fielmente arquiteturas utilizadas em grandes empresas que conectam ferramentas de visualização diretamente a repositórios de dados na nuvem (AWS S3, Azure ADLS, Google Cloud Storage).


