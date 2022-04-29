"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do \nsalário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do \nSalário Bruto, mas não é descontado 
(é a empresa que deposita). O \nSalário Líquido corresponde ao \nSalário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
\nSalário Bruto até 900 (inclusive) - isento
\nSalário Bruto até 1500 (inclusive) - desconto de 5%
\nSalário Bruto até 2500 (inclusive) - desconto de 10%
\nSalário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

        \nSalário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        \nSalário Liquido                 : R$  935,00"""

s = float(input("Qual seu salário por hora? "))
h = float(input("Quantas horas são trabalhadas por mês? "))

if s*h <= 900:
    print("\nSalário Bruto: {}".format(s*h))
    print("(-) IR (0%): isento")
    print("(-) INSS ( 10%): {}".format(s*h*10/100))
    print("FGTS (11%): {}".format(s*h*11/100))
    print("Total de descontos: {}".format(s*h*10/100))
    print("Salário Líquido: {}".format(s*h - (s*h*10/100)))

elif s*h > 900 and s*h <= 1500:
    print("\nSalário Bruto: {}".format(s*h))
    print("(-) IR (5%): {}".format(s*h*5/100))
    print("(-) INSS ( 10%): {}".format(s*h*10/100))
    print("FGTS (11%): {}".format(s*h*11/100))
    print("Total de descontos: {}".format(s*h*5/100 + s*h*10/100))
    print("Salário Líquido: {}".format(s*h - (s*h*5/100 + s*h*10/100)))

elif s*h > 1500 and s*h <= 2500:
    print("\nSalário Bruto: {}".format(s*h))
    print("(-) IR (10%): {}".format(s*h*10/100))
    print("(-) INSS ( 10%): {}".format(s*h*10/100))
    print("FGTS (11%): {}".format(s*h*11/100))
    print("Total de descontos: {}".format(s*h*10/100 + s*h*10/100))
    print("Salário Líquido: {}".format(s*h - (s*h*10/100 + s*h*10/100)))

elif s*h > 2500 :
    print("\nSalário Bruto: {}".format(s*h))
    print("(-) IR (20%): {}".format(s*h*20/100))
    print("(-) INSS ( 10%): {}".format(s*h*10/100))
    print("FGTS (11%): {}".format(s*h*11/100))
    print("Total de descontos: {}".format(s*h*20/100 + s*h*10/100))
    print("Salário Líquido: {}".format(s*h - (s*h*20/100 + s*h*10/100)))