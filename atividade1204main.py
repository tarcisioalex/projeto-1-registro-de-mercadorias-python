import atividade1204

valorTotal = 0
condicao = "s"

while condicao == "s":

    nome = input("Digite o nome da mercadoria: ")
    quantMin = int(input("Digite a quantidade mínima dessa mercadoria: "))
    while quantMin <= 0:
        quantMin = int(input("A quantidade mínima não pode ser zero ou inferior.\nDigite novamente: "))
    quantMax = int(input("Digite a quantidade máxima dessa mercadoria: "))
    while quantMax <= 0 or quantMax < quantMin:
        quantMax = int(input("A quantidade máxima não pode ser zero ou inferior e nem menor do que a quantidade mínima\nDigite novamente: "))
    quantAtual = int(input("Digite a quantidade atual dessa mercadoria no estoque: "))
    while quantAtual < 0:
        quantAtual = int(input("A quantidade atual não pode ser inferior a zero.\nDigite novamente: "))
    valorUni = float(input("Digite o valor unitário dessa mercadoria: "))
    while valorUni <= 0:
        valorUni = int(input("O valor unitário não pode ser igual ou inferior a zero.\nDigite novamente: "))

    mTotal = atividade1204.mercadoriaTotal(nome, quantMin, quantMax, quantAtual, valorUni)
    if quantAtual < quantMin:
        mReposicao = atividade1204.mercadoriaReposicao(nome, quantMin, quantMax, quantAtual, valorUni)

    valorTotal += quantAtual * valorUni

    condicao = input("Deseja registrar mais produtos? (s/n):")

print("\nTodos os produtos registrados: ")
print(mTotal)
print("\nProdutos que precisam de reposição: ")
print(mReposicao)
print("\nValor total do estoque %0.2f" %(valorTotal))
