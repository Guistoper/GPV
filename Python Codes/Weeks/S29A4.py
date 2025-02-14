estoque = {}

class Estoque:
    def adicionar(produto, preco):
        if produto.capitalize() not in estoque:
            estoque.update({produto: preco})
            return produto.capitalize(), preco
        else:
            return "Erro #1 - Produto Já Está Na Lista."
    def remover(produto):
        if produto.capitalize() in estoque:
            del estoque[produto]
            return produto.capitalize()
        else:
            return "Erro #2 - Produto Inválido."
    def exibir():
        return estoque

while True:
    print("-" * 50)
    print("INVENTÁRIO DE PRODUTOS")
    print("1 - Exibir o Estoque")
    print("2 - Adicionar ao Estoque")
    print("3 - Remover do Estoque")
    print("4 - Sair")
    selecao = int(input("Selecione uma opção: "))
    match selecao:
        case 1:
            print("ATUALIZAR O ESTOQUE")
            print(f"Estoque: {Estoque.exibir()}")
        case 2:
            print("ADICIONAR AO ESTOQUE")
            produto = input("Selecione o produto que deseja adicionar: ")
            preco = input("Selecione o preço que deseja adicionar: ")
            print(f"Valor Final: {Estoque.adicionar(produto, preco)}")
        case 3:
            print("RETIRAR DO ESTOQUE")
            produto = input("Selecione o produto: ")
            print(f"Valor Final: {Estoque.remover(produto)}")
        case 4:
            print("SAIR")
            break
        case _:
            print("Opção Inválida.")