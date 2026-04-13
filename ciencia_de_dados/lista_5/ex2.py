import pandas as pd

relatorio_anual = pd.DataFrame({
    "Mês": ["Jan", "Fev", "Mar", "Abr"],
    "Receita": [15000, 18000, 17500, 20000],
    "Despesas": [12000, 13000, 14000, 15000]
})

with pd.ExcelWriter("relatorio.xlsx", engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
    relatorio_anual.to_excel(writer, sheet_name="Resultados", index=False)
 
df_dados_brutos = pd.read_excel("relatorio.xlsx", sheet_name="Dados Brutos")

print("DataFrame salvo em relatorio.xlsx (aba 'Resultados').")
print("Aba 'Dados Brutos':")
print(df_dados_brutos)