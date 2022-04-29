"""Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;"""

print("Veremos as raizes de uma equação do segundo grau, informe a, b e c\n")

a = float(input("Digite o valor de a: "))
if a == 0:
    print("a = 0, não é um valor válido.")
    exit()
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = (b ** 2) - (4*a*c)
print("Delta = {}.".format(delta))


if delta < 0:
    print("A equação não possui raizes reais.")
    exit()

raiz1 = (-b + delta ** (1/2))/(2*a)
raiz2 = (-b - delta ** (1/2))/(2*a)

if delta == 0:
    print("A equação possui apenas uma raiz real, sendo ela: {}".format(raiz1))
    exit()

if delta > 0:
    print("A equação possui duas raizes reais sendo elas: {} e {}".format(raiz1, raiz2))


