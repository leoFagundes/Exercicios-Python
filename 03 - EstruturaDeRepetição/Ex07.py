'''Faça um programa que leia 5 números e informe o maior número.'''

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

list = []
list.extend((n1, n2, n3, n4, n5))

maior = -99999*999999

for i, item in enumerate(list):
    if list[i] > maior:
        maior = item
print(f'O maior número foi o: {maior}')