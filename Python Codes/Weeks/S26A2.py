L = int(input("Selecione a linha (0-11): "))
T = input("Selecione a operação (S de Soma | M de Média): ")

soma = 0.0
for i in range(12):
    for _ in range(12):
        numero = float(input(f"Digite um número ({i} Linha, {_}º Número): "))
        if(i == L):
            soma += numero
    
if(T.upper() == 'S'):
    print(f'{soma:.1f}')
else:
    print(f'{soma/12:.1f}')