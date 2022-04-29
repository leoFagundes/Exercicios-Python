'''Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.'''

listaA = [1, 3, 6, 34, 15, 4, 65, 32, 10, 8]

for i, ints in enumerate(listaA):
    listaA[i] *= listaA[i]

print(f"S = {sum(listaA)}")