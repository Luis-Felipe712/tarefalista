numeros = input("Digite uma lista de números separados por espaço: ").split()
divisor = int(input("Digite o número pelo qual deseja dividir: "))

divisiveis = [int(num) for num in numeros if int(num) % divisor == 0]

print("Números divisíveis por", divisor, ":", divisiveis)