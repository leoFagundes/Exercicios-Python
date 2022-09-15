'''
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
'''

def numeros(n):
    x = 0
    while x < n:
        x += 1
        for i in range(1, x+1):
            print(f' {i} ', end='')
        print('\n')

n = int(input("Digite um número: "))
numeros(n)