'''Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.'''

idades = []
alturas = []

n = 1
while n < 30+1:
    print("")
    idades.append(int(input(f"Digite a idade do {n}º aluno. ")))
    alturas.append(float(input(f"Digite a altura do {n}º aluno. ")))
    n += 1

alturasMenos13Anos = []
for indice, i in enumerate(idades):
    if i <= 13:
        alturasMenos13Anos.append(alturas[indice])

mediaAlturaMenos13Anos = sum(alturasMenos13Anos)/len(alturasMenos13Anos)
pequenininho = 0

for indice, i in enumerate(idades):
    if i > 13:
        if alturas[indice] < mediaAlturaMenos13Anos:
            pequenininho += 1

print(f"{pequenininho} aluno(s) com mais de 13 anos tem altura inferior à média de altura dos alunos com menos de 13 anos")