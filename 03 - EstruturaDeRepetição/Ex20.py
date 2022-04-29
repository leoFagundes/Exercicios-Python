'''Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.'''

while True:
    n = int(input("Informe um número para calcular seu fatorial: "))
    if n < 0 or n > 16:
        print("Digite um número inteiro menor do que 16")
        continue
    NumBonito = n
    fat = []
    fatorial = n

    for i in range(1, n+1):
        fat.append(i)
    fat.sort(reverse=True)

    for i in fat:
        n -= 1
        if n != 0:
            fatorial = fatorial*n
        else:
            break

    print("{}! = {}".format(NumBonito, fatorial))

    reiniciar = input("Deseja inserir um novo valor? 's' ou 'n' ")
    if reiniciar == 'n':
        break
    elif reiniciar == 's':
        continue
