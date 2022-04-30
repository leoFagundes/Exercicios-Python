"""Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente"."""

respostas = []

respostas.append(input("Telefonou para a vítima? ").casefold().capitalize())
respostas.append(input("Esteve no local do crime? ").casefold().capitalize())
respostas.append(input("Mora perto da vítima? ").casefold().capitalize())
respostas.append(input("Devia para a vítima? ").casefold().capitalize())
respostas.append(input("Já trabalhou com a vítima? ").casefold().capitalize())

sim = 0
for resposta in respostas:
    if resposta in ['Sim', 'S']:
        sim += 1

print("")
if sim == 2:
    print("Suspeita")
elif sim == 2 or sim == 3:
    print("Cúmplice")
elif sim == 5:
    print("Assassino")
else:
    print("Inocente")

