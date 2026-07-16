import pandas as pd
import openpyxl

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

#Para manter a rastreabilidade da venda, adicionamos o "Não identificado" para o valor nulo na tabela
df_vendas["vendedor"] = df_vendas["vendedor"].fillna('Não identificado')


#Conversão para números, o errors="coerse" transforma valores inválidos em NaN, evitando possíveis quebras de código
#Comum para caso sejam recebidas planilhas preenchidas manualmente
df_vendas["valor_venda"] = pd.to_numeric(df_vendas["valor_venda"], errors="coerce")
df_vendas["desconto"] = pd.to_numeric(df_vendas["desconto"], errors="coerce")


#As linhas que estiverem com erros preenchidos com NaN(tratato anteriormente), vão ser substituídas por 0 para manter o funcionamento
#Essa regra de substituição irá depende da regra de negócio da empresa
df_vendas["valor_venda"] = df_vendas["valor_venda"].fillna(0)
df_vendas["desconto"] = df_vendas["desconto"].fillna(0)

#Aplicando regras de negócio:
#Cria um novo DataFrame, filtrando apenas por pedidos concluídos, o .copy() evita problemas de edição em fatias do DataFrame original
df_concluidas = df_vendas[df_vendas["status"] == "Concluido"].copy()


print("\nBase Tratada (Somente pedidos concluídos)")
print(df_concluidas)


#Transformações
#Valor Líquido = valor bruto - desconto
#Métrica que geralmente entra em análises de receita
df_concluidas["valor_liquido"] = df_concluidas["valor_venda"] - df_concluidas["desconto"]

print("-"*90)
print(df_concluidas)

#Aplicando regra de comissão (Geralmente é uma métrica comercial)
df_concluidas["comissao"] = df_concluidas["valor_liquido"] * 0.05

print("-"*90)
print(df_concluidas)

#KPI's (Key Performance Indicator) - Indicador-Chave de Desempenho utilizado na gestão de negócios para medir o progresso e avaliar o sucesso de estratégias.
#KPI 1: receita por vendedor
#Ajuda a acompanhar a performance individual dos vendedores
total_por_vendedor = df_concluidas.groupby("vendedor")["valor_liquido"].sum()
print("-"*90)
print("Receita líquida por vendedor:")
print(total_por_vendedor)

#KPI 2: receita por região
#Ajuda a entender a concentração geográfica das vendas
total_por_regiao = df_concluidas.groupby("regiao")["valor_liquido"].sum()
print("-"*90)
print("Receita líquida por região:")
print(total_por_regiao)

#KPI 3: ticket médio por vendedor
#Mostra o valor médio por pedido, não só o volume total)
ticket_medio_por_vendedor = df_concluidas.groupby("vendedor")["valor_liquido"].mean()
print("-"*90)
print("Ticket médio por vendedor:")
print(ticket_medio_por_vendedor)

#Ranking de vendedores para leitura executiva mais rápida:
ranking_vendedores = (
    df_concluidas.groupby("vendedor")["valor_liquido"]
    .sum()
    .sort_values(ascending=False) #Organiza em ordem decrescente o ranking
    .reset_index(name="receita_líquida") #Adiciona um novo index (índice) para cada vendedor no ranking
)
print("-"*90)
print("Ranking vendedores:")
print(ranking_vendedores)

#Receita filtrada pelo mês
receita_mes = df_concluidas.groupby("mes")["valor_liquido"].sum().reset_index()
print("-"*90)
print("Receita líquida mensal:")
print(receita_mes)

"""df_concluidas.to_csv("vendas_tratadas.csv", index=False)
ranking_vendedores.to_csv("ranking_vendedor.csv", index=False)
receita_mes.to_csv("receita_mensal.csv", index=False)"""

