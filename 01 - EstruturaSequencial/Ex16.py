"""Faça um programa para uma loja de tinteas. O programa deverá pedir o tamanho em metros quadrados da área a ser pinteada. 
Considere que a cobertura da tintea é de 1 litro para cada 3 metros quadrados e que a tintea é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tintea a serem compradas e o preço total."""

m2 = float(input("Qual o tamanho em m² da área a ser pintada? "))

latas = (m2/3)/18

striLATAS = str(latas)
inteLATAS = int(latas)


print("\nA quantidade exata de latas que deverá usar é: {:.2f} latas de tinta".format(latas))
if latas != inteLATAS:
    inteLATAS += 1
    print("A quantidade de latas de tinta arredondadas a serem usadas é: {} latas de tinta".format(inteLATAS))
print("O preço a se pagar é: {} R$\n".format(inteLATAS*80))

