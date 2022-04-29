'''Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.'''

n = int(input('Digite um número inteiro: '))
NPrimos = []
divisores = []

for i in range(1, n+1):
    if n % i == 0:
        NPrimos.append(i)

if len(NPrimos) == 2:   
    print(f"{n} é um número primo")
else:
    print(f"{n} não é um número primo")
    print(f"E seus divisores são: {NPrimos}")