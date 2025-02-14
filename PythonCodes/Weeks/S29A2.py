notas = []
alunos = int(input("Digite a quantidade de alunos: "))
for aluno in range(0, alunos):
    nota = int(input(f"Digite a nota do Aluno Número {aluno}: "))
    if nota > 0 and nota <= 10:
        notas.append(nota)
    else:
        print("Nota inválida.")
        break
print(f"A média de notas da sala é: {sum(notas) / len(notas)}")