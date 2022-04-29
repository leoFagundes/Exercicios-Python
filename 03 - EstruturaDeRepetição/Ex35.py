'''Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.'''

n = int(input('Digite um número inteiro: '))

NPrimos = []

for k in range(2, n):
    divisores = []
    for i in range(1, n+1):
        if k % i == 0:
            divisores.append(i)

    if len(divisores) == 2:   
        divisores.sort(reverse=True)
        NPrimos.append(divisores[0])

print(f'Os números primos entre 1 e {n} são: {NPrimos}')