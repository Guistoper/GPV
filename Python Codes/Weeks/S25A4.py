temperatura = [
    [22, 25, 28, 32],
    [20, 23, 26, 30],
    [18, 22, 25, 29]
]

transpor = [list(coluna) for coluna in zip(*temperatura)]
print(transpor)