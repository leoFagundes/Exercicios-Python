'''Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas   |  % de Juros sobre o valor inicial da dívida
1                             0%
3                             10%
6                             15%
9                             20%
12                            25%
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67'''


divida = float(input("Qual o valor da dívida? "))
juros = 0
print(f"|{'Valor da Dívida':^23} | {'Valor dos Juros':^20} | {'Qtde de Parcelas':^19} | {'Valor da Parcela':^22} |")
print('-'*96)
for i in [1, 3, 6, 9, 12]:
    print(f"|R$ {divida + divida*juros/100:^20} | {divida*juros/100:^20} |{i:^20} | R${(divida + divida*juros/100) / i:^20.2f} |")
    if i == 1:
        juros += 10
    elif i != 1:
        juros += 5
