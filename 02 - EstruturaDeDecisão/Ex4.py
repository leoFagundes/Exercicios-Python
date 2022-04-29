"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante."""

l = str(input("Digite uma letra: "))

if l == "a" or l == "e" or l == "i" or l == "o" or l == "u":
    print("A letra é volgal.")
else:
    print("A letra é consoante.")