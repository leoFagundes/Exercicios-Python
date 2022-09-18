'''
Número por extenso. 
Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.
'''

unidades = ['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
dezenas = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
others = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']

n = int(input("Digite um número de 1 à 99: "))
nString = str(n)

if n < 1 or n > 99:
    print("Valor inválido")
    exit()
else:
    if n >= 20:
        for i, dezena in enumerate(dezenas):
            if i == int(nString[0]):
                if int(nString[1]) == 0:
                    print(dezena)
                else:
                    for i, unidade in enumerate(unidades):
                        if i+1 == int(nString[1]):
                            print(f"{dezena} e {unidade}")
    elif n < 10:
        for i, unidade in enumerate(unidades):
            if i+1 == n:
                print(unidade)
    else:
        for i, other in enumerate(others):
            if i == int(nString[1]):
                print(other)




