'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120'''

n = int(input("Informe um número para calcular seu fatorial: "))
NumBonito = n
fat = []
fatorial = n

for i in range(1, n+1):
    fat.append(i)
fat.sort(reverse=True)

for i in fat:
    print(i)
    n -= 1
    if n != 0:
        fatorial = fatorial*n
    else:
        break


print("{}! = {}".format(NumBonito, fatorial))