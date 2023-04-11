nomes = input("Digite uma lista de nomes separados por espaço: ").split()
nome_busca = input("Digite o nome a ser buscado: ")

if nome_busca in nomes:
    print("O nome está na lista")
else:
    print("O nome não está na lista")