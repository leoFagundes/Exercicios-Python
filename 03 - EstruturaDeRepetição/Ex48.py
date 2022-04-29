'''Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321'''

while True:
    n = int(input("Digite um número inteiro positivo: "))
    if n < 0:
        print("Digite um número positivo.") 
        continue
    else:
        break

numeros = []

for i in str(n):
    numeros.append(i)

numeros.reverse()
print(f'O número {n} invertido fica {"".join(numeros)}')