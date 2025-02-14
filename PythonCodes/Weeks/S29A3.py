lista = []

class Compras:
    def adicionar(produto):
        if produto.capitalize() not in lista:
            lista.append(produto.capitalize()) 
            return produto.capitalize()
        else:
            return "Erro #1 - Produto Já Está Na Lista."
    def remover(produto):
        if produto.capitalize() in lista:
            lista.remove(produto.capitalize())
            return produto.capitalize()
        else:
            return "Erro #2 - Produto Não Está Na Lista."
    def exibir():
        return lista

while True:
    print("-" * 50)
    print("LISTA DE COMPRAS")
    print("1 - Exibir a Lista")
    print("2 - Adicionar a Lista")
    print("3 - Remover da Lista")
    selecao = int(input("Selecione uma opção: "))
    match selecao:
        case 1:
            print("EXIBIR A LISTA")
            print(f"Lista: {Compras.exibir()}")
        case 2:
            print("ADICIONAR A LISTA")
            produto = input("Selecione o produto que deseja adicionar: ")
            print(f"Produto Adicionado: {Compras.adicionar(produto)}")
        case 3:
            print("REMOVER DA LISTA")
            produto = input("Selecione o produto que deseja remover: ")
            print(f"Produto Removido: {Compras.remover(produto)}")
        case _:
            print("Opção Inválida.")