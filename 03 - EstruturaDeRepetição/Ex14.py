'''Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.'''
lista = []
par = 0
imp = 0

for i in range(1, 11):
    n = int(input('Informe um número: '))
    lista.append(n)

for num in lista:
    if num % 2 == 0:
        par += 1
    else:
        imp += 1

print(f"A quantidade de números pares é {par} e de números ímpares é {imp}")