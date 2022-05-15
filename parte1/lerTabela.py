import pandas as pd

tabela = pd.read_excel(r"C:\Users\lecos\Downloads\Vendas - Dez.xlsx")
print(tabela)
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()
