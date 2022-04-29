'''Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.'''

n1 = int(input("Informe um número: "))
n2 = int(input("Informe outro número: "))

pot = n1

for i in range(1, n2):
    pot = pot * n1
print(f"{n1} elevado a {n2} = {pot}")
