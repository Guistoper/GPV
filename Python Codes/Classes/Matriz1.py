print(30 * " ")
matrizA = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for linha in matrizA:
    print(linha)
print(30 * " ")
matrizA[0][0] = 12
matrizA[1][2] = 16
for linha in matrizA:
    print(linha)
print(30 * " ")