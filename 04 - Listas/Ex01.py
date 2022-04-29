'''Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.'''

numeros = []

while len(numeros) < 5:
    n = int(input("Digite um número inteiro: "))
    numeros.append(n)

print(numeros)