'''
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.
'''

frase = input("Digite uma frase: ")

print(f"""
Frase: '{frase}'
Espaços em brancos: {frase.count(' ')}
Vogais a: {frase.count('a')}
       e: {frase.count('e') + frase.count('é')}
       i: {frase.count('i')}
       o: {frase.count('o')}
       u: {frase.count('u')}
""")