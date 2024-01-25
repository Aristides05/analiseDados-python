import pandas as pd
from IPython.display import display

def produtosUnidade(): 
    tabela = pd.read_excel("Vendas.xlsx")
    produtosUnidade = tabela[["ID Loja", "Produto", "Quantidade", "Valor Final"]].groupby(["ID Loja", "Produto"]).sum()
    display(produtosUnidade)