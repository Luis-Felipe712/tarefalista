numeros = input("Digite uma lista de números separados por espaço: ").split()
numeros = [int(numero) for numero in numeros]

segundo_mais_baixo = sorted(numeros)[1]

print(f"O segundo número mais baixo é {segundo_mais_baixo}")