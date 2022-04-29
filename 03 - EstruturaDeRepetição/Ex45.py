'''Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, 
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota 
(atribuir 1 ponto por resposta certa). 
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. 

Após todos os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.
'''

'''
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

gabaritoFinal = []
questao = 0
while questao < 11:
    questao += 1
    gabarito = input("Digite a resposta da {questao}ª questão: ")
    gabarito = gabarito.capitalize()
    if gabarito != 'A' and gabarito != 'B' and gabarito != 'C' and gabarito != 'D' and gabarito != 'E':
            print("Resposta inválida, digite novamente.")
            continue
    gabaritoFinal.append(gabarito)
'''
gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
alunos = []
#lista_respostas = []
pontos = []

while True:
    #respostas = []
    ponto = 0
    questao = 1
    aluno = input("\nQual o nome do aluno? ")
    aluno = aluno.capitalize()
    alunos.append(aluno)
    while questao < 11:
        resposta = input(f"Qual a resposta da {questao}ª questão? ")
        resposta = resposta.capitalize()
        if resposta != 'A' and resposta != 'B' and resposta != 'C' and resposta != 'D' and resposta != 'E':
            print("Resposta inválida, digite novamente.")
            continue
        #respostas.append(resposta)
        if resposta == gabarito[questao-1]:
            ponto += 1
        questao += 1

    #lista_respostas.append(respostas)
    pontos.append(ponto)

    while True:
        outro_aluno = input("\nOutro aluno vai utilizar o sistema? ")
        outro_aluno.casefold().strip()
        if outro_aluno != 'sim' and outro_aluno != 's' and  outro_aluno != 'nao' and outro_aluno != 'não' and outro_aluno != 'n':
            print("Resposta inválida, digite novamente.")
            continue
        else:
            break

    if outro_aluno == 'sim' or outro_aluno == 's':
        continue
    elif outro_aluno == 'nao' or outro_aluno == 'não' or outro_aluno == 'n':
        break

maiorPonto = -1
indiceMaior = 0

menorPonto = 11
indiceMenor = 0

for indice, i in enumerate(pontos):
    if i > maiorPonto:
        maiorPonto = i
        indiceMaior = indice
    if i < menorPonto:
        menorPonto = i
        indiceMenor = indice

print(f"{len(alunos)} alunos utilizaram o sistema")
print(f"O aluno que teve a maior quantidade de acertos foi {alunos[indiceMaior]} com {maiorPonto} acertos")
print(f"O aluno que teve a menor quantidade de acertos foi {alunos[indiceMenor]} com {menorPonto} acertos")
print(f"A média de notas dos alunos que utilizaram o sistema foi de {sum(pontos)/len(pontos)}")