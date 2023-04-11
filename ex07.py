nomes = input("Digite uma lista de nomes separados por espaço: ").split()

nome_mais_longo = max(nomes, key=len)
nome_mais_curto = min(nomes, key=len)

print(f"O nome mais longo é: {nome_mais_longo}")
print(f"O nome mais curto é: {nome_mais_curto}")