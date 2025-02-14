import numpy as np

def maior(vendas, n):
    vendas.sort()
    return vendas[n-1]

vendas = np.array([120, 130, 140, 150, 160, 170, 160, 150, 140, 130, 120, 110])
n = len(vendas)
soma = vendas.sum()
media = soma / len(vendas)
maximo = maior(vendas, n)

print(f"Total de Vendas Anual: {soma}")
print(f"Média de Vendas Mensal: {media}")
print(f"Mês com Maior Vendas: {maximo}")