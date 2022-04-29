"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias."""

m2 = float(input("Qual o tamanho em m² da área a ser pintada? "))

litros = m2/6

latas = (litros)/18
galao = (litros)/3.6

striLATAS = str(latas)
inteLATAS = int(latas)

striGALAO = str(galao)
inteGALAO = int(galao)


print("Você irá precisar de {:.2f} litros".format(litros))

print("\nA quantidade exata de latas que deverá usar é: {:.2f} latas de tinta".format(latas))
if latas != inteLATAS:
    inteLATAS += 1
    print("A quantidade de latas de tinta arredondadas a serem usadas é: {} latas de tinta".format(inteLATAS))
print("O preço a se pagar é: {} R$\n".format(inteLATAS*80))

print("\nA quantidade exata de galões que deverá usar é: {:.2f} galões de tinta".format(galao))
if galao != inteGALAO:
    inteGALAO += 1
    print("A quantidade de galões de tinta arredondados a serem usadas é: {} galões de tinta".format(inteGALAO))
print("O preço a se pagar é: {} R$\n".format(inteGALAO*25))

inteLATAS -= 1
inteGALAO -= 1
   
restoLATA = (litros) % 18
restoGALÃO = restoLATA / 3.6
folga = restoGALÃO*10/100

if restoGALÃO > (int(restoGALÃO) + folga):
    print("A quantidade de latas é {} e a de galões é {}".format(inteLATAS, int(restoGALÃO)+1))
    print("O preço a se pagar é {} R$\n".format(inteLATAS*80 + (int(restoGALÃO)+1)*25))
elif restoGALÃO < (int(restoGALÃO) + folga):
    print("A quantidade de latas é {} e a de galões é {}".format(inteLATAS, int(restoGALÃO)))
    print("O preço a se pagar é {} R$\n".format(inteLATAS*80 + (int(restoGALÃO))*25))
