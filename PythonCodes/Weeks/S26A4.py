temperaturas = [
    [18, 19, 20, 21, 22, 23, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3],
    [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44],
]

dias_acima_20 = []
transpor = [list(coluna) for coluna in zip(*temperaturas)]
for dia, temperaturas_dia in enumerate(transpor, start=1):
    media = sum(temperaturas_dia) / len(temperaturas_dia)
    print(media)
    if media > 20:
        dias_acima_20.append(dia)

print(f"Dias com temperatura média superior a 20°C: {dias_acima_20}")