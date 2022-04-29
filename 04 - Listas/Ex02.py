'''Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.'''

numeros = []

while len(numeros) < 10:
    n = int(input("Digite um número inteiro: "))
    numeros.append(n)

numeros.reverse()

print(numeros)