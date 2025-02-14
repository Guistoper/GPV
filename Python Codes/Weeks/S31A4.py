numeros_pares = [num for num in range(21) if num % 2 == 0]

quadrados = [num ** 2 for num in numeros_pares]

print("Números pares de 0 a 20:", numeros_pares)
print("Quadrado de cada número:", quadrados)
