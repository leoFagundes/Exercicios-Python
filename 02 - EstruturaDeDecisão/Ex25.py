"""Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente"."""


print("Responda com 's' (sim) ou 'n' (não)\n")


a = str(input("Telefonou para a vítima?"))
if a != 's' and a != 'n':
    print("Resposta inválida.")
    exit()
    
b = str(input("Esteve no local do crime?"))
if b != 's' and b != 'n':
    print("Resposta inválida.")
    exit()

c = str(input("Mora perto da vítima?"))
if c != 's' and c != 'n':
    print("Resposta inválida.")
    exit()

d = str(input("Devia para a vítima?"))
if d != 's' and d != 'n':
    print("Resposta inválida.")
    exit()

e = str(input("Já trabalhou com a vítima?"))
if e != 's' and e != 'n':
    print("Resposta inválida.")
    exit()

susp = 0

if a == 's':
    susp += 1

if b == 's':
    susp += 1

if c == 's':
    susp +=1

if d == 's':
    susp +=1

if e == 's':
    susp +=1

if susp == 2:
    print("Suspeita")
elif susp == 3 or susp == 4:
    print("Cúmplice")
elif susp == 5:
    print("Assassino")
else:
    print("Inocente")