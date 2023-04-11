lista = input("Digite uma lista de números separados por espaço: ").split()
numeros = [int(x) for x in lista]

minimo = min(numeros)
maximo = max(numeros)

print("O número mínimo da lista é:", minimo)
print("O número máximo da lista é:", maximo)