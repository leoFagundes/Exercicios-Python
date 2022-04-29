'''Faça um programa que calcule o mostre a média aritmética de N notas.'''

notas = []
notaFinal = 0

while True:
    n = int(input('Informe uma nota: (para sair digite -1) '))
    if n == -1:
        break
    if n > 10:
        print('Digite uma nota entre 0 e 10')
        continue
    notas.append(n)

for nota in notas:
    notaFinal += nota

print('A média aritmética entre as notas é: {}'.format(notaFinal/len(notas)))
