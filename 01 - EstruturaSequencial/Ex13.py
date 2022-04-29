"""Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7"""


h = float(input("Sua altura: "))
a = True
while a == True:
    Genero = str(input("Você é Homem ou Mulher? "))
    Genero = Genero.capitalize()
    if (Genero == "Homem") or (Genero == "H"):
        print("Seu peso ideal é: {:.2f}".format((72.7*h) - 58))
        a = False
    elif (Genero == "Mulher") or (Genero == "M"):
        print("Seu peso ideal é: {:.2f}".format((62.1*h) - 44.7))
        a = False
