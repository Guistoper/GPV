tesouro = [[0, 0, 0], 
           [1, 0, 0], 
           [0, 0, 0]]

tabuleiro = [[0, 0, 0], 
           [0, 0, 0], 
           [0, 0, 0]]

while True:
    print("-" * 30)
    for row in tabuleiro:
        print(row)
    a = int(input("Escolha uma linha do tabuleiro para escavar (0-2): "))
    b = int(input("Escolha uma coluna do tabuleiro para escavar (0-2): "))
    if tesouro[a][b] == 0:
        tabuleiro[a][b] = "X"
        tesouro[a][b] = "X"
        continue
    elif tesouro[a][b] == 1:
        print("Você achou o tesouro!")
        for row in tesouro:
            print(row)
        break