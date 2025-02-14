print(30 * " ")
matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]
print(matriz1)
print(matriz2)
print(30 * " ")
soma_matrizes = [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]
for linha in soma_matrizes:
    print(linha)
print(30 * " ")