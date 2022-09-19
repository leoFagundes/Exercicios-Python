'''
Valida e corrige número de telefone. Faça um programa que leia um número de telefone, 
e corrija o número no caso deste conter somente 8 dígitos, acrescentando o '9' na frente. 
O usuário pode informar o número com ou sem o traço separador.

Valida e corrige número de telefone
Telefone: 9461-0133
Telefone possui 8 dígitos. Vou acrescentar o digito nove na frente.
Telefone corrigido sem formatação: 994610133
Telefone corrigido com formatação: 99461-0133
'''

tel = input("Digite um número de telefone: ")
tel = tel.strip()
try:
    tel = tel.replace("-", "")
except ValueError:
    pass

lista_telefone = []

if len(tel) == 9:
    for i, n in enumerate(tel):
        if i == 5:
            lista_telefone.append('-')
        lista_telefone.append(n)
    print(f"\nTelefone: {tel}")
    print(f"Telefone com formatação: {''.join(lista_telefone)}")
elif len(tel) == 8:
    for i, n in enumerate(tel):
        if i == 0:
            lista_telefone.append('9')
        if i == 4:
            lista_telefone.append('-')
        lista_telefone.append(n)
    print(f"\nTelefone: {tel}")
    print("Telefone possui 8 dígitos. Vou acresentar o digito nove na frente.")
    print(f"Telefone com formatação: {''.join(lista_telefone)}")
else: 
    print("Número inválido.")