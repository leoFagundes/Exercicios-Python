"""Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0."""

notasAlunos = []
acimaMedia = 0

for i in range(1, 11):
    notas = []
    print("")
    for i2 in range(1, 5):
        notas.append(float(input(f"Digite a {i2}ª nota do {i}º aluno:")))
    notasAlunos.append(notas)

for aluno in notasAlunos:
    if sum(aluno)/len(aluno) >= 7:
        acimaMedia += 1

print(f"\n{acimaMedia} alunos ficaram acima da média (7.0)")