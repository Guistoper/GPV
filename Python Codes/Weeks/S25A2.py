assentos = [["O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O"]]


class Assento:
    def assentos_disponiveis():
        for linha in assentos:
            print(linha)
    def reservar_assento(num1, num2):
        if assentos[num2][num1] != "X":
            assentos[num2][num1] = "X"
            print(Assento.assentos_disponiveis())
        elif assentos[num2][num1] == "X":
            print("Este assento já está marcado.")
        else:
            print("Erro #1 - Assento Não Encontrado.")
    def cancelar_reserva(num2, num1):
        if assentos[num2][num1] == "X":
            assentos[num2][num1] = "O"
            print(Assento.assentos_disponiveis())
        else:
            print("Erro #2 - Assento Não Marcado.")

while True:
    print("-" * 50)
    print("ASSENTOS DISPONÍVEIS")
    print("1 - Ver Assentos")
    print("2 - Reservar Assento")
    print("3 - Cancelar Reserva")
    selecao = int(input("Selecione uma opção: "))
    match selecao:
        case 1:
            Assento.assentos_disponiveis()
        case 2:
            print("RESERVAR ASSENTO")
            Assento.assentos_disponiveis()
            num1 = int(input("Selecione a coluna: "))
            num2 = int(input("Selecione a linha: "))
            Assento.reservar_assento(num1, num2)
        case 3:
            print("CANCELAR RESERVA")
            Assento.assentos_disponiveis()
            num1 = int(input("Selecione a coluna: "))
            num2 = int(input("Selecione a linha: "))
            Assento.cancelar_reserva(num1, num2)
        case _:
            print("Opção Inválida.")