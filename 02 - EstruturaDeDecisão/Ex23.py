"""Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento."""

n = float(input("Um número: "))

if int(n) == n:
    print("Esse número é inteiro.")
else:
    print("Esse número é decimal.")