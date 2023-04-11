palavras = input("Digite uma lista de palavras separadas por espaço: ")

lista_palavras = palavras.split()

palavras_impares = []

for palavra in lista_palavras:
    if len(palavra) % 2 == 1:
        palavras_impares.append(palavra)

print("Palavras com número ímpar de letras:", palavras_impares)