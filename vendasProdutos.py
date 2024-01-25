import pandas as pd
from IPython.display import display

def vendasProdutos():
    tabela = pd.read_excel("Vendas.xlsx")
    vendasProdutos = tabela[["Produto", "Quantidade", "Valor Final"]].groupby("Produto"). sum()
    display(vendasProdutos)