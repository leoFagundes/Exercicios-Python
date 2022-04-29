'''Faça um programa que calcule o número médio de alunos por turma. 
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.'''

turmas = {}
QuantidadeAlunos = 0
letra = 64
i = 0

while True:
    qtdeturmas = int(input("Qual a quantidade de turmas? "))
    if qtdeturmas > 26:
        print('Digite uma quantidade entre 1 e 26')
    else:
        break

while i < qtdeturmas:
    letra += 1
    i += 1
    alunos = int(input(f"Qual a quantidade de alunos para a turma {chr(letra)}? "))
    if alunos > 40 or alunos < 0:
        print("A turma só pode ter 40 alunos")
        letra -= 1
        continue
    turmas[f'Turma {chr(letra)}'] = alunos

for valor in turmas.values():
    QuantidadeAlunos += valor

print("\nAs turmas foram: ")
for k in list(turmas.items()):
    print(k)

print("A média de alunos por turma é de {:.1f} alunos".format(QuantidadeAlunos/qtdeturmas))