'''Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.'''

n = int(input('Digite um número inteiro: '))
NPrimos = []

for i in range(1, n+1):
    if n % i == 0:
        NPrimos.append(i)

if len(NPrimos) == 2:   
    print(f"{n} é um número primo")
else:
    print(f"{n} não é um número primo")