import pandas as pd
from IPython.display import display

def vendasUnidade():
    tabela = pd.read_excel("Vendas.xlsx")
    faturamentoUnidade = tabela[["ID Loja", "Quantidade", "Valor Final"]].groupby("ID Loja").sum()
    display(faturamentoUnidade)