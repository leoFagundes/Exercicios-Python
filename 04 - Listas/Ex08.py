'''Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.'''

alturas =[]
idades = []

for i in range(1, 6):
    print("")
    h = float(input(f"Digite a altura da {i}ª pessoa "))
    idade = int(input(f"Digite a idade da {i}ª pessoa "))
    alturas.append(h)
    idades.append(idade)

alturas.reverse()
idades.reverse()
print(alturas)
print(idades)