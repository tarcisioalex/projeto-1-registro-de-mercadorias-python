from prettytable import PrettyTable

mercTotal = PrettyTable()
mercReposicao = PrettyTable()
mercTotal.field_names = ["Produto","Quantidade mínima","Quantidade máxima", "Quantidade atual", "Valor unitário"]
mercReposicao.field_names = ["Produto","Quantidade mínima","Quantidade máxima", "Quantidade atual", "Valor unitário"]

def mercadoriaTotal(nome, quantMin, quantMax, quantAtual, valorUni):

    mercTotal.add_row([nome, quantMin, quantMax, quantAtual, valorUni])
    return mercTotal

def mercadoriaReposicao(nome, quantMin, quantMax, quantAtual, valorUni):
    mercReposicao.add_row([nome, quantMin, quantMax, quantAtual, valorUni])
    return mercReposicao
