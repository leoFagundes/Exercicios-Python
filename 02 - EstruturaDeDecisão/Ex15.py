"""Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:

Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;"""

n1 = float(input("Primeiro lado do triângulo: "))
n2 = float(input("Segundo lado do triângulo: "))
n3 = float(input("Terceiro lado do triângulo: "))

if (n1 + n2) > n3 and (n1 + n3) > n2 and (n2 + n3) > n1:
    print("É um triângulo válido.")
    if n1 == n2 == n3:
        print("Seu triângulo é Equilátero.")
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print("Seu triângulo é Isóseceles.")
    elif n1 != n2 != n3:
        print("Seu triângulo é Escaleno")
else:
    print("Triângulo inválido.")