"""Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal."""

n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))

print("\nQual operação deseja realizar: \n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão")
operacao = input()

if operacao == '1' or operacao == 'Soma' or operacao == 'soma':
    soma = n1+n2
    print(f"A soma de {n1} + {n2} = {soma}")
    if (soma)%2 == 0:
        print(f"{soma} é um número par.")
    else:
        print(f"{soma} é um número ímpar.")
    
    if soma < 0:
        print(f"{soma} é um número negativo.")
    else:
        print(f"{soma} é um número positivo.")

    if int(soma) == soma:
        print(f"{soma} é um número inteiro.")
    else:
        print(f"{soma} é um número decimal.")

elif operacao == '2' or operacao == 'Subtração' or operacao == 'subtração':
    subt = n1-n2
    print(f"A subtração de {n1} - {n2} = {subt}")
    if (subt)%2 == 0:
        print(f"{subt} é um número par.")
    else:
        print(f"{subt} é um número ímpar.")
    
    if subt < 0:
        print(f"{subt} é um número negativo.")
    else:
        print(f"{subt} é um número positivo.")

    if int(subt) == subt:
        print(f"{subt} é um número inteiro.")
    else:
        print(f"{subt} é um número decimal.")

elif operacao == '3' or operacao == 'Multiplicação' or operacao == 'multiplicação':
    mult = n1*n2
    print(f"A multiplicação de {n1} x {n2} = {mult}")
    if (mult)%2 == 0:
        print(f"{mult} é um número par.")
    else:
        print(f"{mult} é um número ímpar.")
    
    if mult < 0:
        print(f"{mult} é um número negativo.")
    else:
        print(f"{mult} é um número positivo.")

    if int(mult) == mult:
        print(f"{mult} é um número inteiro.")
    else:
        print(f"{mult} é um número decimal.")

elif operacao == '4' or operacao == 'Divisão' or operacao == 'divisão':
    div = n1/n2
    print(f"A divisão de {n1} / {n2} = {div}")
    if (div)%2 == 0:
        print(f"{div} é um número par.")
    else:
        print(f"{div} é um número ímpar.")
    
    if div < 0:
        print(f"{div} é um número negativo.")
    else:
        print(f"{div} é um número positivo.")

    if int(div) == div:
        print(f"{div} é um número inteiro.")
    else:
        print(f"{div} é um número decimal.")
