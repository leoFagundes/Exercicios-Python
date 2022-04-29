"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores."""

numeros = []
pares = []
impares = []

while len(numeros) < 20:
    n = int(input("Digite um número inteiro: "))
    numeros.append(n)
    
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    
print(f"\nTodos os números: {numeros}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}\n")

