"""Altere o programa anterior, intercalando 3 vetores de 10 elementos cada."""
lista1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
lista2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
lista3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

lista4 = []

for i in range(0, 10):
    lista4.append(lista1[i])
    lista4.append(lista2[i])
    lista4.append(lista3[i])

print(lista4)