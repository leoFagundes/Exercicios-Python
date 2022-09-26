'''
Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, 
colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

8  3  4 
1  5  9
6  7  2

Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. 
Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. 
Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.
'''
from random import choice

def quadrado_magico():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    combinacoes = []
    #essa repetição serve para pegar todas as combinações possíveis em que a soma é 15 e os números não se repetem, ao final ele coloca na lista de combinações
    for numero in numeros:
        for numero2 in numeros:
            for numero3 in numeros:
                if numero + numero2 + numero3 == 15:
                    if numero != numero2 != numero3:
                        combinacoes.append([numero, numero2, numero3])
    #esse while serve para pegar 3 listas aleatorias da lista de combinações e testar pra ver se todas as colunas/linhas/diagionais delas são iguais a 15
    while True:
        combinacoes1 = choice(combinacoes)
        combinacoes2 = choice(combinacoes)
        combinacoes3 = choice(combinacoes)
        if combinacoes1[0] + combinacoes2[0] + combinacoes3[0] == 15:
            if combinacoes1[1] + combinacoes2[1] + combinacoes3[1] == 15:
                if combinacoes1[2] + combinacoes2[2] + combinacoes3[2] == 15:
                    if combinacoes1[0] + combinacoes2[1] + combinacoes3[2] == 15:
                        if combinacoes1[2] + combinacoes2[1] + combinacoes3[0] == 15:
                            #verifica se os números são todos diferentes
                            todasCombinacoes = [combinacoes1[0], combinacoes1[1], combinacoes1[2], combinacoes2[0], combinacoes2[1], combinacoes2[2], combinacoes3[0], combinacoes3[1], combinacoes3[2]]
                            setterCombinacoes = set(todasCombinacoes)
                            if len(list(setterCombinacoes)) == 9:   
                                return (combinacoes1, combinacoes2, combinacoes3)


x, y, z = quadrado_magico()
print(f"{x}\n{y}\n{z}")