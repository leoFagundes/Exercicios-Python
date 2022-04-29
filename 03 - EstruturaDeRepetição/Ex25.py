'''Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; 
e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.'''

idades = []
idadeFinal = 0

while True:
    i = int(input('Informe uma nota: (para sair digite -1) '))
    if i == -1:
        break
    if i < -1 or i > 120:
        print('Digite uma idade valida')
        continue
    idades.append(i)

for idade in idades:
    idadeFinal += idade

idadeTurma = idadeFinal / len(idades)

if idadeTurma >= 0 and idadeTurma <= 25:
    print("A turma é jovem")
if idadeTurma > 25 and idadeTurma <= 60:
    print("A turma é adulta")
if idadeTurma > 60:
    print("A turma é idosa")