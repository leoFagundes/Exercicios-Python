'''Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.'''

def digitos(n):
    n = str(n)
    return (len(n))

n = int(input('Digite um número inteiro: '))

print(f"O número {n:,} tem {digitos(n)} digitos")

