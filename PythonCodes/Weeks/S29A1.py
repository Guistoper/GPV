def comprar(roupa, quantidade):
    if roupa.lower() == "casual":
        valor = casual * quantidade
        if quantidade <= 5:
            return valor
        elif quantidade >= 6 and quantidade <= 10:
            desconto = valor * .1
            total = valor - desconto
            return total
        elif quantidade > 10:
            desconto = valor * .2
            total = valor - desconto
            return total
    elif roupa.lower() == "formal":
        valor = formal * quantidade
        if quantidade <= 5:
            return valor
        elif quantidade >= 6 and quantidade <= 10:
            desconto = valor * .1
            total = valor - desconto
            return total
        elif quantidade > 10:
            desconto = valor * .2
            total = valor - desconto
            return total
    else:
        return ValueError

casual = 70
formal = 110

print(f"Roupa Casual: {casual} Reais \nRoupa Formal: {formal} Reais")
roupa = input("Escolha o tipo de roupa que deseja comprar: ")
quantidade = int(input("Digite a quantidade que deseja comprar: "))
if comprar(roupa, quantidade) != ValueError:
    print(f"O valor total é {comprar(roupa, quantidade)} Reais por {quantidade} Roupa {roupa.capitalize()}")
else:
    print("Escolha uma roupa válida ou digite um valor válido.")