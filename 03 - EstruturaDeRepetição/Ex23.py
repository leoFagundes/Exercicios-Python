'''Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.'''


n = int(input('Digite um número inteiro: '))

NPrimos = []
divisoes = 0

for k in range(2, n):
    divisores = []
    for i in range(1, n+1):
        if k % i == 0:
            divisoes += 1
            divisores.append(i)

    if len(divisores) == 2:   
        divisores.sort(reverse=True)
        NPrimos.append(divisores[0])

print(f'Os números primos entre 1 e {n} são: {NPrimos}')
print(f'Divisões feitas: {divisoes}')