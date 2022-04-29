"""Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."""

l = str(input("F ou M? "))

if l == "F" or l == "f":
    print("Feminino")
elif l == "M" or  l == "m":
    print("Masculino")
else:
    print("Sexo inválido")