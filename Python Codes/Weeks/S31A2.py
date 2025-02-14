numeros = []

while True:
    som = int(input("Digite um número: "))
    if som == 0:
        break
    else:
        numeros.append(som)

print(sum(numeros) / len(numeros))