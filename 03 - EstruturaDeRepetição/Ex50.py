'''Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.'''

print("Diga qual será o N termo da seguinte série: ")
n = int(input("H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N\n"))

h = []

# Mostrar a sequência na tela
for i in range(1, n+1, 1):
    h.append(f"1/{i}")

print(f'H = {" + ".join(h)}')

# Soma
soma = 0

for i in range(1, n+1, 1):
    soma += 1/i

print(f"H = {soma:.2f}")