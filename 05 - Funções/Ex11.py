'''
Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. 
Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
'''

def validar_data(data):
    if len(data) != 10:
        return 'Data inválida, coloque na ordem DD/MM/AAAA'
    elif '/' not in data[2] and '/' not in data[5]:
        return 'Data inválida, acrescente -> /'
    else:
        return ''

def data_mesExtesnso():
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
    return f'{diaN}/{mesE}/{anoN}\n'

print(data_mesExtesnso())






    