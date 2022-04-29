"""Faça um Programa que leia três números e mostre o maior e o menor deles."""

n1 = float(input("Número 1: "))
n2= float(input("Número 2: "))
n3 = float(input("Número 3: "))

Maior = -99999999999999999999
Menor = 999999999999999999999

if n1 > Maior:
    Maior = n1
if n2 > Maior:
    Maior = n2
if n3 > Maior:
    Maior = n3

if n1 < Menor:
    Menor = n1
if n2 < Menor:
    Menor = n2
if n3 < Menor:
    Menor = n3

print("O maior número é: {}".format(Maior))
print("O menor número é: {}".format(Menor))