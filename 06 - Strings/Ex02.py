'''
Nome ao contrário em maiúsculas. 
Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. 
Dica: lembre-se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
'''

listaNome = []

nome = input("Digite seu nome: ")

for letra in nome:
    listaNome.append(letra)

nomeContrario = ''.join(listaNome[::-1])
nomeContrario = nomeContrario.upper()

print(nomeContrario)
