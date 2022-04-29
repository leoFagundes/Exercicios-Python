"""Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)."""

f = float(input("Temperatura em graus Fahrenheit: "))

C = 5*((f-32)/9)

print("A temperatura de {} graus Fahrenheit em célsius fica: {} graus Celsius".format(f, C))