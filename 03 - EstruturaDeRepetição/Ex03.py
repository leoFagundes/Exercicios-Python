"""Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';"""

while True:
    nome = input("Diga o seu nome: ")
    if len(nome) > 3:
        break
    else:
        print("Digite novamente\n") 

while True:
    idade = int(input("Diga a sua idade: "))
    if idade >= 0 and idade <= 150:
        break
    else:
        print("Digite novamente\n") 

while True:
    salario = float(input("Diga o seu salário: "))
    if salario > 0:
        break
    else:
        print("Digite novamente\n") 

while True:
    sexo = input("Diga o seu sexo: ")
    if sexo.lower() == 'f' or sexo.lower() == 'm':
        break
    else:
        print("Digite novamente\n") 

while True:
    estado_civil = input("Diga o seu estado civil: ")
    if estado_civil.lower() == 's' or estado_civil.lower() == 'c' or estado_civil.lower() == 'v' or estado_civil.lower() == 'd':
        break
    else:
        print("Digite novamente\n") 
