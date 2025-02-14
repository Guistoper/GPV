estoque = [20, 15, 10, 30, 5]

class Estoque:
    def adicionar_estoque(num1, num2):
        if num1 < len(estoque):
            if num2 > 0:
                estoque[num1] += num2 
                return estoque[num1]  
            else:
                return "Erro #2 - Quantidade de Produtos Inválido."
        else:
            return "Erro #1 - Posição do Estoque Inválida."
    def retirar_estoque(num1, num2):
        if num1 < len(estoque):
            if num2 > 0:
                estoque[num1] -= num2
                if estoque[num1] >= 0:
                    return estoque[num1]
                elif estoque[num1] < 0:
                    estoque[num1] == 0
                    return estoque[num1]
                else:
                    return "Erro #3 - Valor Final do Estoque Inválido."
            else:
                return "Erro #2 - Número de Produtos Inválido."
        else:
            return "Erro #1 - Posição do Estoque Inválida."
    def quantidade(num1):
        if num1 < len(estoque):
            return estoque[num1]
        else:
            return "Erro #1 - Posição do Estoque Inválida."
    def atualizar_estoque():
        return estoque

while True:
    print("-" * 50)
    print("ESTOQUE DE PRODUTOS")
    print("1 - Atualizar o Estoque")
    print("2 - Ver o Produto")
    print("3 - Adicionar ao Estoque")
    print("4 - Retirar do Estoque")
    selecao = int(input("Selecione uma opção: "))
    match selecao:
        case 1:
            print("ATUALIZAR O ESTOQUE")
            print(f"Estoque: {Estoque.atualizar_estoque()}")
        case 2:
            print("VER O PRODUTO")
            num1 = int(input("Selecione o produto: "))
            print(f"Produto: {Estoque.quantidade(num1)}")
        case 3:
            print("ADICIONAR AO ESTOQUE")
            num1 = int(input("Selecione o produto: "))
            num2 = int(input("Selecione a quantidade: "))
            print(f"Valor Final: {Estoque.adicionar_estoque(num1, num2)}")
        case 4:
            print("RETIRAR DO ESTOQUE")
            num1 = int(input("Selecione o produto: "))
            num2 = int(input("Selecione a quantiade: "))
            print(f"Valor Final: {Estoque.retirar_estoque(num1, num2)}")
        case _:
            print("Opção Inválida.")