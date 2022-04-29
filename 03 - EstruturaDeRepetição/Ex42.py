'''Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: 
[0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.'''

numeros = []

intervalor_0_25 = []
intervalo_26_50 = []
intervalo_51_75 = []
intervalor_76_100 = []


while True:
    n = int(input("Digite um número: (digite um número negativo para sair)\n"))
    if n < 0:
        break
    numeros.append(n)

for i in numeros:
    if i > 0 and i <= 25:
        intervalor_0_25.append(i)
    if i > 25 and i <= 50:
        intervalo_26_50.append(i)
    if i > 50 and i <= 75:
        intervalo_51_75.append(i)
    if i > 75 and i <= 100:
        intervalor_76_100.append(i)

print(f"Existem {len(intervalor_0_25)} números no intervalo [0-25]")
print(f"Existem {len(intervalo_26_50)} números no intervalo [26-50]")
print(f"Existem {len(intervalo_51_75)} números no intervalo [51-75]")
print(f"Existem {len(intervalor_76_100)} números no intervalo [76-100]")