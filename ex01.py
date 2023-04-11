lista = input("Digite uma lista de números separados por espaço: ").split()
numeros_pares = []

for num in lista:
    if int(num) % 2 == 0:
        numeros_pares.append(num)

print("Números pares: ", end="")
for num in numeros_pares:
    print(num, end=" ")