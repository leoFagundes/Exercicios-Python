'''Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. 
Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.'''

#Vou mudar mudar "número do aluno" para o nome dele

nomes = []
alturas = []

i = 0
while i < 10:
    i += 1

    nome = input(f"\nQual o nome do aluno{i}? ")
    nomes.append(nome)
    altura = float(input(f"Qual a altura do {nome}? "))
    alturas.append(altura)

alto = 0
indiceAlto = 0

baixo = 99999
indiceBaixo = 0
for indice, k in enumerate(alturas):
    if k > alto:
        alto = k
        indiceAlto = indice
    if k < baixo:
        baixo = k
        indiceBaixo = indice

print(f"\nO aluno mais alto foi o {nomes[indiceAlto]}, medindo {alto}\nO aluno mais baixo foi o {nomes[indiceBaixo]} medindo {baixo}")
