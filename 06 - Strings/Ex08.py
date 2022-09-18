'''
Palíndromo. 
Um palíndromo é uma sequência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice-versa. 
Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. 
A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. 
Faça um programa que leia uma seqüência de caracteres, mostre-a e diga se é um palíndromo ou não.
'''

string = input("Escreva uma frase: ")

stringP = string[::-1].replace(" ", "")

print(string)
print(stringP)

if string.replace(" ", "") == stringP:
    print(f"\nA frase digitada foi {string}")
    print("É um texto palíndromo\n")
else:
    print(f"\nA frase digitada foi {string}")
    print("Não é um texto palíndromo\n")
