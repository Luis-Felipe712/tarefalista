numeros = input("Digite uma lista de números separados por espaço: ").split()

numeros = [float(numero) for numero in numeros]

media = sum(numeros) / len(numeros)

print(f"A média dos números é: {media}")