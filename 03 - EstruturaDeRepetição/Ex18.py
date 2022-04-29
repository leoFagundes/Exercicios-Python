'''Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.'''

numeros = []

while True:
    n = int(input("Digite um número: (digite -1 para encerrar)\n"))
    if n == -1:
        break
    numeros.append(n)

maior = -999*999
menor = 999*999
soma = 0

for i in numeros:
    if i > maior:
        maior = i
    if i < menor:
        menor = i
    soma = soma + i

print(f"Os valores são: {numeros}")
print(f"O maior valor é: {maior}\nO menor valor é: {menor}\nA soma dos valores é: {soma}")