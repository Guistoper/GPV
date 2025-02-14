entrada = 20
prato_principal = 50
sobremesa = 15

def desconto(valor):
    if valor > 100:
        desconto = valor * .1
        total = valor - desconto
        return total
    else:
        total = valor
        return total

print("Entrada: R$20 \nPrato Principal = R$50 \nSobremesa = R$15")

prato = input("Diga qual prato deseja: ")
quantidade = int(input("Diga a quantidade que deseja: "))

if prato.lower() == "entrada":
    valor = quantidade * entrada
    print(f"Você pediu {quantidade} {prato.capitalize()}, totalizando R${desconto(valor)}.")
elif prato.lower() == "prato principal":
    valor = quantidade * prato_principal
    print(f"Você pediu {quantidade} {prato.capitalize()}, totalizando R${desconto(valor)}.")
elif prato.lower() == "sobremesa":
    valor = quantidade * sobremesa
    print(f"Você pediu {quantidade} {prato.capitalize()}, totalizando R${desconto(valor)}.")
else:
    print("Prato inválido.")