'''
Data por extenso. 
Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
'''

def validar_data(data):
    if len(data) != 10:
        return 'Data inválida, coloque na ordem DD/MM/AAAA'
    elif '/' not in data[2] and '/' not in data[5]:
        return 'Data inválida, acrescente -> /'
    else:
        return ''

meses = ['janeiro', 'fevereiro', 'março', 'abril,', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
mesesNumeros = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
while True:
    data = str(input("\nDigite uma data no formato DD/MM/AAAA -> "))
    if validar_data(data) == '':
        pass
    else:
        print(validar_data(data))
        
    if 'inválida' in validar_data(data):
        continue
    else:
        data = data.strip()
        diaN = data[0:2]
        mesN = data[3:5] #mes número 01, 02...
        mesE = '' #mes extenso
        anoN = data[6:10]

        if int(diaN) > 31 or int(diaN) < 0:
            print("Dia ou Mês inválidos.")
            continue
        elif int(mesN) > 12 or int(mesN) < 0:
            print("Dia ou Mês inválidos.")
            continue
        else: 
            print(validar_data(data))
            break

for i, mesNumero in enumerate(mesesNumeros):
    if mesNumero == mesN:
        mesE = meses[i].capitalize()
print(f'Você nasceu no dia {diaN} de {mesE} de {anoN}.\n')