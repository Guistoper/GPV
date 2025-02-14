import random

def criar_tabuleiro():
    grid = [[0, 0, 0] for _ in range(3)]
    tesouro_x, tesouro_y = random.randint(0, 2), random.randint(0, 2)
    grid[tesouro_x][tesouro_y] = 1
    return grid

def imprimir_tabuleiro(grid):
    for linha in grid:
        print(' '.join('X' if celula == 1 else '0' for celula in linha))

def jogar():
    grid = criar_tabuleiro()
    tentativas = 0
    while True:
        imprimir_tabuleiro(grid)
        print(tentativas)
        try:
            x = int(input("Escolha uma linha (0-2): "))
            y = int(input("Escolha uma coluna (0-2): "))
            if grid[x][y] == 1:
                print("Parabéns! Você encontrou o tesouro!")
                break
            elif grid[x][y] == 'T':  # Checa se a tentativa já foi feita
                print("Você já tentou aqui. Tente novamente.")
                continue
            else:
                print("Não há tesouro aqui. Tente novamente.")
                grid[x][y] = 'T'  # Marca a tentativa do jogador
            tentativas += 1
        except IndexError:
            print("Entrada inválida. Tente novamente dentro dos limites do tabuleiro.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

    print(f"Você encontrou o tesouro em {tentativas} tentativas!")

jogar()
