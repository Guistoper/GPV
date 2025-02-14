import math

def isPrime(num):
    if(num==1):
        return False
    if(num==2):
        return True
    if(num%2==0):
        return False
    i = 3
    while(i<math.sqrt(num)+1):
        if num%i==0:
            return False
        i += 2
    return True

while True:
    print("-" * 30)
    num = int(input("Digite um número: "))
    if num < 0:
        print("Número negativo.")
        break
    elif num < 1:
        print("Número menor que 1.")
        continue
    elif num >= 2:
        prime = isPrime(num)
        if prime == True:
            print("Número primo.")
            continue
        elif prime == False:
            print("Número não primo.")
            break 