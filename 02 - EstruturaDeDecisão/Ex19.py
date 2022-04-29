"""Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16"""

n = int(input("Digite um número menor do que 1000: "))

if n >= 1000 or n < 0:
    print("Número inválido.")
    exit()

NumeroStr = str(n)

if n < 10:
    if NumeroStr[0] == '1':
        print("{} = {} unidade".format(n, NumeroStr[0]))
        exit()
    print("{} = {} unidades".format(n, NumeroStr[0]))

if n >= 10 and n < 100:
    if NumeroStr[0] == '1' and NumeroStr[1] == '1':
        print("{} = {} dezena e {} unidade".format(n, NumeroStr[0], NumeroStr[1]))
        exit()

    if NumeroStr[1] == '1':
        print("{} = {} dezenas e {} unidade".format(n, NumeroStr[0], NumeroStr[1]))
        exit()
    if NumeroStr[0] == '1':
        print("{} = {} dezena e {} unidades".format(n, NumeroStr[0], NumeroStr[1]))
        exit()
    print("{} = {} dezenas e {} unidades".format(n, NumeroStr[0], NumeroStr[1]))

if n >= 100:
    if NumeroStr[1]== '1' and NumeroStr[0] =='1' and NumeroStr[2] == '1':
        print("{} = {} centena, {} dezena e {} unidade".format(n, NumeroStr[0], NumeroStr[1], NumeroStr[2]))
        exit()

    if NumeroStr[2] == '1' and NumeroStr[1] == '1' and NumeroStr[0] != '1':
        print("{} = {} centenas, {} dezena e {} unidade".format(n, NumeroStr[0], NumeroStr[1], NumeroStr[2]))
        exit()
    if NumeroStr[0] == '1' and NumeroStr[1] == '1' and NumeroStr[2] != '1':
        print("{} = {} centena, {} dezena e {} unidades".format(n, NumeroStr[0], NumeroStr[1], NumeroStr[2]))
        exit()
    if NumeroStr[0] == '1' and NumeroStr[2] == '1' and NumeroStr[1] != '1':
        print("{} = {} centena, {} dezenas e {} unidade".format(n, NumeroStr[0], NumeroStr[1], NumeroStr[2]))
        exit()

    if NumeroStr[2] == '1':
        print("{} = {} centenas, {} dezenas e {} unidade".format(n, NumeroStr[0], NumeroStr[1], NumeroStr[2]))
        exit()
    if NumeroStr[1] == '1':
        print("{} = {} centenas, {} dezena e {} unidades".format(n, NumeroStr[0], NumeroStr[1], NumeroStr[2]))
        exit()
    if NumeroStr[0] == '1':
        print("{} = {} centena, {} dezenas e {} unidades".format(n, NumeroStr[0], NumeroStr[1], NumeroStr[2]))
        exit()
    print("{} = {} centenas, {} dezenas e {} unidades".format(n, NumeroStr[0], NumeroStr[1], NumeroStr[2]))