"""Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida."""

data = str(input("Informe uma data no modelo 'dd/mm/aaaa': "))

if data[2] != '/' and data [5] != '/':
    print("Está data é inválida.")
else:
    print(data)
