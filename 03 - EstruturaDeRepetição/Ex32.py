'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120'''

print("Informe um número inteiro para calcularmos o seu fatorial,")
n = int(input("número: "))

fatorialINT = []
fatorialSTR = []
fatResultado = 1

for i in range (1, n+1):
    fatResultado = fatResultado*i
    fatorialINT.append(i)

fatorialINT.sort(reverse=True)

#Transformando os valores da lista em string para poder usar o método join
for i in fatorialINT:
    fatorialSTR.append(str(i))

print(f"{n}! = {' . '.join(fatorialSTR)} = {fatResultado:,}")
