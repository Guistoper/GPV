import random

def criar_tabuleiro():
    grid = [[1, 1, 1] for _ in range(3)]
    tesouro_x, tesouro_y = random.randint(0, 2), random.randint(0, 2)
    grid[tesouro_x][tesouro_y] = 0
    return grid

def imprimir_tabuleiro(grid):
    for linha in grid:
        print(' '.join('1' if celula == 0 else '1' for celula in linha))

def jogar():
    grid = criar_tabuleiro()
    while True:
        imprimir_tabuleiro(grid)
        try:
            x = int(input("Escolha uma linha (0-2): "))
            y = int(input("Escolha uma coluna (0-2): "))
            if grid[x][y] == 0:
                print("Parabéns! Você encontrou o Zero!")
                break
            else:
                print("Não há Zero aqui. Tente novamente.")
        except IndexError:
            print("Entrada inválida. Tente novamente dentro dos limites do tabuleiro.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

jogar()
