"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo."""

i1 = int(input("Digite um número itneiro: "))
i2 = int(input("Digite um número itneiro: "))
r1 = float(input("Digite um número real: "))

print("O dobro do primeiro com a metade do segundo é {}".format((i1*2)*(i2/2)))
print("A soma do triplo do primeiro com o terceiro é: {}".format(i1*3 + r1))
print("O terceiro elevado ao cubo é: {}".format(r1*r1*r1))