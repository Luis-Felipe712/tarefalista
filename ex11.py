numeros = input("Digite uma lista de números separados por espaço: ").split()
soma_impares = 0

for numero in numeros:
    if int(numero) % 2 == 1:
        soma_impares += int(numero)

print("A soma dos números ímpares na lista é:", soma_impares)
