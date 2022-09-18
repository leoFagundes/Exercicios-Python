'''
Nome na vertical em escada invertida. 
Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F
'''

nome = input("Digite seu nome: ")

i = len(nome)
for letra in nome:
    print(nome[0:i])
    i -= 1