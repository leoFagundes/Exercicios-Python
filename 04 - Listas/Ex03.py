'''Faça um Programa que leia 4 notas, mostre as notas e a média na tela.'''

notas = []

while len(notas) < 4:
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

media = sum(notas)/len(notas)
print(f"A média é: {media:.2f}")