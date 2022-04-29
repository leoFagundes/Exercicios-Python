"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido."""

perH = float(input("Quanto ganha por hora: "))
Horas = float(input("Quantas horas por mês: "))
SB = perH*Horas
IR = SB*11/100
INSS = SB*8/100
Sindicato = SB*5/100

print("+ Salário Bruto: {} R$".format(SB))
print("- IR (11%): {} R$".format(IR))
print("- INSS (8%): {} R$".format(INSS))
print("- Sindicato (5%): {} R$".format(Sindicato))
print("= Salário Líquido: {} R$".format(SB-IR-INSS-Sindicato))

