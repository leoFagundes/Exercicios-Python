"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento."""

s = float(input("Digite o salário: "))

if s > 0 and s <= 280:
    print("O salário antes do reajuste: {} R$".format(s))
    print("O percentual de aumento aplicado foi de 20%: {} R$".format(s*20/100))
    print("O novo salário, após aumento: {} R$".format(s + s*20/100))
elif s > 280 and s < 700:
    print("O salário antes do reajuste: {} R$".format(s))
    print("O percentual de aumento aplicado foi de 15%: {} R$".format(s*15/100))
    print("O novo salário, após aumento: {} R$".format(s + s*15/100))
elif s > 700 and s < 1500:
    print("O salário antes do reajuste: {} R$".format(s))
    print("O percentual de aumento aplicado foi de 10%: {} R$".format(s*10/100))
    print("O novo salário, após aumento: {} R$".format(s + s*10/100))
elif s >= 1500:
    print("O salário antes do reajuste: {} R$".format(s))
    print("O percentual de aumento aplicado foi de 5%: {} R$".format(s*5/100))
    print("O novo salário, após aumento: {} R$".format(s + s*5/100))
else:
    print("Salário inválido")
