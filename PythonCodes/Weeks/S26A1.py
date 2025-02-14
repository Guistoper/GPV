V = int(input("Digite um número (1-50): "))

if V <= 50 and V > 0:
    for i in range(10):
        print(f"N[{i}] = {V}")
        V <<= 1