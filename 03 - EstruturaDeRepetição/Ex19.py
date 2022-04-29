'''Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.'''

numeros = []

while True:
    n = int(input("Digite um número entre 0 e 1000: (digite -1 para encerrar)\n"))
    if n == -1:
        break
    if n < 0 or n > 1000:
        print("Valor inválido, digite novamente.")
        continue
    numeros.append(n)

maior = -999*999
menor = 999*999
soma = 0

for i in numeros:
    if i > maior:
        maior = i
    if i < menor:
        menor = i
    soma = soma + i

print(f"Os valores são: {numeros}")
print(f"O maior valor é: {maior}\nO menor valor é: {menor}\nA soma dos valores é: {soma}")