def desempenho(pontos, presentes):
    if pontos >= 80 and presentes >= 90:
        return "Excelente"
    elif pontos > 49 and presentes >= 75:
        return "Bom"
    elif pontos < 50:
        return "Ruim"
    else:
        return "Regular"

pontos = int(input("Digite a sua porcentagem de pontuação: "))
presentes = int(input("Digite a sua porcentagem de presença: "))
print(desempenho(pontos, presentes))

