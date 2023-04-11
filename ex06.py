lista_str = input("Digite a lista de números separados por espaço: ")
lista = [int(num) for num in lista_str.split()]
lista.sort(reverse=True)

print("Lista ordenada em ordem decrescente:", lista)
