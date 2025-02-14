filme1 = "O Homem de Toronto"
filme2 = "Missão Impossível"
filme3 = "As Branquelas"
filme4 = "Gente Grande"
filme5 = "Eu Antes de Você"
filme6 = "Marley e Eu"

preferencia = input("Diga a sua preferência de filme (Ação, Comédia, Drama): ")
idade = int(input("Diga a sua idade: "))

match preferencia.lower():
    case "ação": 
        if idade >= 18:
            print(f"O filme recomendado para você é: {filme1}")
        else:
            print(f"O filme recomendado para você é: {filme2}")
    case "comédia":
        if idade >= 18:
            print(f"O filme recomendado para você é: {filme4}")
        else:
            print(f"O filme recomendado para você é: {filme3}")
    case "drama":
        if idade >= 18:
            print(f"O filme recomendado para você é: {filme5}")
        else:
            print(f"O filme recomendado para você é: {filme6}")
    case _:
        print("Gênero de Filme inválido.")