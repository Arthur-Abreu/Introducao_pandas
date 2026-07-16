import os
import pandas as pd
import duckdb

# ==========================================
# 1. Extração e Tratamento (Bronze -> Silver)
# ==========================================
dados_vendas = {
    "id_pedido": ["001", "002", "003", "004", "005", "006", "007", "008"],
    "vendedor": ["Ana", "Ana", "Bruno", "Bruno", "Carlos", "Carlos", None, "Ana"],
    "regiao": ["Sul", "Sul", "Sudeste", "Sudeste", "Sul", "Sul", "Sudeste", "Sul"],
    "valor_venda": ["1000", "1500", "2000", None, "1800", "900", "1200", "1300"],
    "desconto": [100, 0, 150, 200, None, 50, 0, 130],
    "status": ["Concluido", "Concluido", "Concluido", "Cancelado", "Concluido", "Concluido", "Cancelado", "Concluido"],
    "mes": ["Jan", "Fev", "Jan", "Fev", "Jan", "Fev", "Fev", "Mar"],
}

df_vendas = pd.DataFrame(dados_vendas)

# Limpeza e tipagem dos dados
df_vendas["vendedor"] = df_vendas["vendedor"].fillna("Não identificado")
df_vendas["valor_venda"] = pd.to_numeric(df_vendas["valor_venda"], errors="coerce").fillna(0)
df_vendas["desconto"] = pd.to_numeric(df_vendas["desconto"], errors="coerce").fillna(0)

# Filtragem e Regras de Negócio
df_concluidas = df_vendas[df_vendas["status"] == "Concluido"].copy()
df_concluidas["valor_liquido"] = df_concluidas["valor_venda"] - df_concluidas["desconto"]
df_concluidas["comissao"] = df_concluidas["valor_liquido"] * 0.05

# ==========================================
# 2. Agrupamentos e Criação de KPIs
# ==========================================
# KPI 1: Ranking de Vendedores por Receita Líquida
ranking_vendedores = (
    df_concluidas.groupby("vendedor")["valor_liquido"]
    .sum()
    .sort_values(ascending=False)
    .reset_index(name="receita_liquida")
)

# KPI 2: Receita por Região
receita_regiao = (
    df_concluidas.groupby("regiao")["valor_liquido"]
    .sum()
    .reset_index(name="receita_liquida")
)

# KPI 3: Receita Mensal
receita_mes = (
    df_concluidas.groupby("mes")["valor_liquido"]
    .sum()
    .reset_index(name="receita_liquida")
)

# ==========================================
# 3. Carga e Exportação (Silver -> Gold)
# ==========================================
# Garantir que a pasta local 'data' exista
if not os.path.exists('data'):
    os.makedirs('data')

# A: Exportação em formato Parquet para disponibilização via DuckDB
con = duckdb.connect(database=":memory:")
con.register("df_concluidas", df_concluidas)
con.execute("COPY df_concluidas TO 'data/gold_vendas_tratadas.parquet' (FORMAT PARQUET)")
con.close()

# B: Exportação em Excel Multi-abas (para Relatório Executivo)
# Aqui usamos o openpyxl por debaixo dos panos
caminho_excel = "data/relatorio_comercial_kpis.xlsx"
with pd.ExcelWriter(caminho_excel, engine="openpyxl") as writer:
    df_concluidas.to_excel(writer, sheet_name="Vendas_Tratadas", index=False)
    ranking_vendedores.to_excel(writer, sheet_name="Ranking_Vendedores", index=False)
    receita_regiao.to_excel(writer, sheet_name="Receita_por_Regiao", index=False)
    receita_mes.to_excel(writer, sheet_name="Receita_Mensal", index=False)

print(f"✅ Pipeline executada com sucesso!")
print(f"👉 Parquet gerado em: 'data/gold_vendas_tratadas.parquet'")
print(f"👉 Relatório em Excel gerado em: '{caminho_excel}'")