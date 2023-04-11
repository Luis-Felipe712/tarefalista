numeros = input("Digite uma lista de números separados por espaço: ")
lista_numeros = numeros.split()
lista_numeros = [int(num) for num in lista_numeros]
lista_ordenada = sorted(lista_numeros)
print("Lista ordenada em ordem crescente:", lista_ordenada)
