import duckdb
import pandas as pd
import os

# 1. Recebimento dos dados, primeiros tratamentos (Camada Bronze -> Silver)
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
df_vendas["vendedor"] = df_vendas["vendedor"].fillna("Não identificado")
df_vendas["valor_venda"] = pd.to_numeric(df_vendas["valor_venda"], errors="coerce")
df_vendas["desconto"] = pd.to_numeric(df_vendas["desconto"], errors="coerce")
df_vendas["valor_venda"] = df_vendas["valor_venda"].fillna(0)
df_vendas["desconto"] = df_vendas["desconto"].fillna(0)

df_concluidas = df_vendas[df_vendas["status"] == "Concluido"].copy()
df_concluidas["valor_liquido"] = (df_concluidas["valor_venda"] - df_concluidas["desconto"])
df_concluidas["comissao"] = df_concluidas["valor_liquido"] * 0.05

# 2. DuckDB entra em ação para otimizar e disponibilizar os dados em Parquet (Camada Gold)
# Criamos uma conexão em memória temporária apenas para processar
con = duckdb.connect(database=":memory:")

# Registramos o DataFrame do pandas no contexto do DuckDB
con.register("df_concluidas", df_concluidas)

#Cria a pasta data no diretório, caso ela não exista
if not os.path.exists('data'):
    os.makedirs('data')

# Exportamos diretamente para arquivos PARQUET de forma extremamente rápida
con.execute(
    "COPY df_concluidas TO 'data/gold_vendas_tratadas.parquet' (FORMAT PARQUET)"
)

con.close()
print("Dados transformados e salvos no formato analítico Parquet!")