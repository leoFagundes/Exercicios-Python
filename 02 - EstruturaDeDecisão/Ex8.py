"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato."""

p1 = float(input("Preço do produto 1: "))
p2 = float(input("Preço do produto 2: "))
p3 = float(input("Preço do produto 3: "))

barato = 9999999999999999

if p1 < barato:
    barato = p1
if p2 < barato:
    barato = p2
if p3 < barato:
    barato = p3

if p1 == barato:
    print("O produto mais barato é o produto 1 de {} R$". format(p1))
if p2 == barato:
    print("O produto mais barato é o produto 2 de {} R$". format(p2))
if p3 == barato:
    print("O produto mais barato é o produto 3 de {} R$". format(p3))
