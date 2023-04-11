lista = input("Digite uma lista de números separados por espaço: ").split()
lista = [int(num) for num in lista] 
lista_ordenada = sorted(lista, reverse=True) 
segundo_maior = lista_ordenada[1] 
print("O segundo número mais alto é:", segundo_maior)
