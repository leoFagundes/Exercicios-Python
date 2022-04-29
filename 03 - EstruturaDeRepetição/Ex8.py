'''Faça um programa que leia 5 números e informe a soma e a média dos números.'''

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

list = []
list.extend((n1, n2, n3, n4, n5))
soma = 0
for i in list:
    soma += i

media = soma / len(list)
print(f'A soma é {soma} e a média é {media}')