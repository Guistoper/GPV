print(30 * " ")
matrizA = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
for linha in matrizA:
    print(linha)
print(30 * " ")
matrizA[0][0] = 0
matrizA[1][1] = 0
matrizA[2][2] = 0
matrizA[3][3] = 0
for linha in matrizA:
    print(linha)
print(30 * " ")