numeros = input("Digite uma lista de números separados por espaço: ").split()

for numero in numeros:
    if int(numero) < 5:
        print(numero)