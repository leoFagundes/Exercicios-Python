"""Faça um Programa para um caixa eletrônico. 
O programa deverá perguntar ao usuário o valor do saque1 e depois informar quantas nota(s) de cada valor serão fornecidas. 
As nota(s) disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de nota(s) existentes na máquina.

Exemplo 1:
Para sacar a quantia de 256 reais, o programa fornece duas nota(s) de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2:
Para sacar a quantia de 399 reais, o programa fornece três nota(s) de 100, uma nota de 50, quatro nota(s) de 10, uma nota de 5 e quatro nota(s) de 1."""

saque = int(input("Informe o valor do saque: "))

saque1 = saque
nota100 = 0
nota50 = 0
nota10 = 0
nota5 = 0
nota1 = 0

if saque1 < 10 or saque1 > 600:
    print("Saque fora do limite de 10 a 600 reais.")
    exit()

nota100 += int(saque1/100)
saque1 -= int(nota100)*100
  
nota50 += int(saque1/50)
saque1 -= int(nota50)*50

nota10 += int(saque1/10)
saque1 -= int(nota10)*10

nota5 += int(saque1/5)
saque1 -= int(nota5)*5

nota1 += int(saque1/1)
saque1 -= int(nota1)*1

#1
if nota100 != 0 and nota50 == 0 and nota10 == 0 and nota5 == 0 and nota1 == 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 100".format(saque, nota100))
if nota100 == 0 and nota50 != 0 and nota10 == 0 and nota5 == 0 and nota1 == 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 50".format(saque, nota50))
if nota100 == 0 and nota50 == 0 and nota10 != 0 and nota5 == 0 and nota1 == 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 10".format(saque, nota10))

#2
if nota100 != 0 and nota50 != 0 and nota10 == 0 and nota5 == 0 and nota1 == 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 100 e {} nota(s) de 50".format(saque, nota100, nota50))
if nota100 != 0 and nota50 == 0 and nota10 != 0 and nota5 == 0 and nota1 == 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 100 e {} nota(s) de 10".format(saque, nota100, nota10))
if nota100 != 0 and nota50 == 0 and nota10 == 0 and nota5 != 0 and nota1 == 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 100 e {} nota(s) de 5".format(saque, nota100, nota5))
if nota100 != 0 and nota50 == 0 and nota10 == 0 and nota5 == 0 and nota1 != 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 100 e {} nota(s) de 1".format(saque, nota100, nota1))

if nota100 == 0 and nota50 != 0 and nota10 != 0 and nota5 == 0 and nota1 == 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 50 e {} nota(s) de 10".format(saque, nota50, nota10))
if nota100 == 0 and nota50 != 0 and nota10 == 0 and nota5 != 0 and nota1 == 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 50 e {} nota(s) de 5".format(saque, nota50, nota5))
if nota100 == 0 and nota50 != 0 and nota10 == 0 and nota5 == 0 and nota1 != 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 50 e {} nota(s) de 1".format(saque, nota50, nota1))

if nota100 == 0 and nota50 == 0 and nota10 != 0 and nota5 != 0 and nota1 == 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 10 e {} nota(s) de 5".format(saque, nota10, nota5))
if nota100 == 0 and nota50 == 0 and nota10 != 0 and nota5 == 0 and nota1 != 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 10 e {} nota(s) de 1".format(saque, nota10, nota1))

#3
if nota100 != 0 and nota50 != 0 and nota10 != 0 and nota5 == 0 and nota1 == 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 100, {} nota(s) de 50, {} nota(s) de 10 e {} nota(s) de 1".format(saque, nota100, nota50, nota10, nota5))
if nota100 != 0 and nota50 != 0 and nota10 == 0 and nota5 != 0 and nota1 == 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 100, {} nota(s) de 50 e {} nota(s) de 5".format(saque, nota100, nota50, nota5))
if nota100 != 0 and nota50 != 0 and nota10 == 0 and nota5 == 0 and nota1 != 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 100, {} nota(s) de 50 e {} nota(s) de 1".format(saque, nota100, nota50, nota1))

if nota100 != 0 and nota50 == 0 and nota10 != 0 and nota5 != 0 and nota1 == 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 100, {} nota(s) de 10 e {} nota(s) de 5".format(saque, nota100, nota10, nota5))
if nota100 != 0 and nota50 == 0 and nota10 != 0 and nota5 == 0 and nota1 != 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 100, {} nota(s) de 10 e {} nota(s) de 1".format(saque, nota100, nota10, nota1))
if nota100 != 0 and nota50 == 0 and nota10 == 0 and nota5 != 0 and nota1 != 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 100, {} nota(s) de 5 e {} nota(s) de 1".format(saque, nota100, nota5, nota1))

if nota100 == 0 and nota50 != 0 and nota10 != 0 and nota5 != 0 and nota1 == 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 50, {} nota(s) de 10 e {} nota(s) de 5".format(saque, nota50, nota10, nota5))
if nota100 == 0 and nota50 != 0 and nota10 != 0 and nota5 == 0 and nota1 != 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 50, {} nota(s) de 10 e {} nota(s) de 1".format(saque, nota50, nota10, nota1))
if nota100 == 0 and nota50 != 0 and nota10 == 0 and nota5 != 0 and nota1 != 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 50, {} nota(s) de 5 e {} nota(s) de 1".format(saque, nota50, nota5, nota1))

if nota100 == 0 and nota50 == 0 and nota10 != 0 and nota5 != 0 and nota1 != 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 10, {} nota(s) de 5 e {} nota(s) de 1".format(saque, nota10, nota5, nota1))

#4
if nota100 != 0 and nota50 != 0 and nota10 != 0 and nota5 != 0 and nota1 == 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 100, {} nota(s) de 50, {} nota(s) de 10 e {} nota(s) de 1".format(saque, nota100, nota50, nota10, nota5))
if nota100 != 0 and nota50 == 0 and nota10 != 0 and nota5 != 0 and nota1 != 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 100, {} nota(s) de 10, {} nota(s) de 5 e {} nota(s) de 1".format(saque, nota100, nota10, nota5, nota1))
if nota100 != 0 and nota50 != 0 and nota10 == 0 and nota5 != 0 and nota1 != 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 100, {} nota(s) de 50, {} nota(s) de 5 e {} nota(s) de 1".format(saque, nota100, nota50, nota5, nota1))
if nota100 != 0 and nota50 != 0 and nota10 != 0 and nota5 == 0 and nota1 != 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 100, {} nota(s) de 50, {} nota(s) de 10 e {} nota(s) de 1".format(saque, nota100, nota50, nota10, nota1))
if nota100 == 0 and nota50 != 0 and nota10 != 0 and nota5 != 0 and nota1 != 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 5, {} nota(s) de 10, {} nota(s) de 5 e {} nota(s) de 1".format(saque, nota50, nota10, nota5, nota1))

#5
if nota100 != 0 and nota50 != 0 and nota10 != 0 and nota5 != 0 and nota1 != 0:
    print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 100, {} nota(s) de 50, {} nota(s) de 10, {} nota(s) de 5 e {} nota(s) de 1".format(saque, nota100, nota50, nota10, nota5, nota1))
