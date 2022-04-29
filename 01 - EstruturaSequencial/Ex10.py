"""Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit."""

c = float(input("Temperatura em graus Celsius: "))

f = (c*9/5) + 32

print("{} graus Celsius são {} graus Fahrenheit".format(c, f))