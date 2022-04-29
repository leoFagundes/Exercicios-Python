"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês."""

Sph = float(input("Quanto ganha por hora? "))
Hora = float(input("Trabalha quantas horas por mês? "))

Total = Sph*Hora

print("Você ganha um total de {} reais por mês".format(Total))