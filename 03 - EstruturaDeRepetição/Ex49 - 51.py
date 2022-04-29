'''Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série.
'''

print("Diga qual será o N termo da seguinte série: ")
n = int(input("S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m\n"))

s = []

# Mostrar a sequência na tela
m = 1
for i in range(1, n+1, 1):
  s.append(f'{i}/{m}')
  m += 2

print(f"\nS = {' + '.join(s)}")

# Soma
soma = 0
m = 1
for i in range(1, n+1, 1):
  soma += i/m
  m += 2

print(f'Soma = {soma:.2f}')