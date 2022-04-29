"""Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números."""

numeros = []
numerosSTR = []

while len(numeros) < 5:
    numeros.append(int(input("Digite um númmero inteiro: ")))

multiplicacao = 1
soma = sum(numeros)

for i in numeros:
    multiplicacao *= i

for i in numeros:
    numerosSTR.append(str(i))

print(f"\n{' + '.join(numerosSTR)} = {soma}")
print(f"{' x '.join(numerosSTR)} = {multiplicacao}")