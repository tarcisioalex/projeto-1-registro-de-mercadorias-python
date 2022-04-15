from prettytable import PrettyTable

x = PrettyTable()
y = PrettyTable()
x.field_names = ["Produto","Quantidade mínima","Quantidade máxima", "Quantidade atual", "Valor unitário"]
y.field_names = ["Produto","Quantidade mínima","Quantidade máxima", "Quantidade atual", "Valor unitário"]

def mercadoriaTotal(nome, quantMin, quantMax, quantAtual, valorUni):

    x.add_row([nome, quantMin, quantMax, quantAtual, valorUni])
    return x

def mercadoriaReposicao(nome, quantMin, quantMax, quantAtual, valorUni):
    y.add_row([nome, quantMin, quantMax, quantAtual, valorUni])
    return y
