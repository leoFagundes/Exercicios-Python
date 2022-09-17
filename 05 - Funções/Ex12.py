'''
Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. 
Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. 
Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
'''
from random import shuffle

def embaralhar_palavra(palavra, char = 'm'):
    '''
    Uma função para embaralhar uma palavra de forma aleatória
    default -> char = 'm' para voltar a palavra minúscula
               char = 'M' para voltar a palavra maiúscula
    '''
    listaLetras = []
    for letra in palavra:
        listaLetras.append(letra)
    shuffle(listaLetras)

    palavra_embaralhada = ''.join(listaLetras)
    if char == 'm':
        palavra_embaralhada = palavra_embaralhada.casefold()
    elif char == 'M':
        palavra_embaralhada = palavra_embaralhada.upper()
    return palavra_embaralhada

palavra = input("Digite uma palavra: ")

print(F"{palavra} -> {embaralhar_palavra(palavra)}")