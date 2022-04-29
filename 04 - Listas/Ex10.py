'''Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, 
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.'''

lista1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
lista2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

lista3 = []

for i in range(0, 10):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(lista3)