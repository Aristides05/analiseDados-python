import produtosUnidade as pu
import vendasProdutos as vp
import vendasUnidade as vu  
    
print("Escolha o que deseja consultar: \n")

print("1 - Vendas por unidade")
print("2 - Vendas totais de cada produto")
print("3 - Vendas totais de produtos por unidade de loja \n")

option = int(input("Digite a opção desejada: "))

match option: 
    case 1: 
        vu.vendasUnidade()
    case 2: 
        vp.vendasProdutos()
    case 3: 
        pu.produtosUnidade()
    case _: 
        print("Digite uma opção válida")