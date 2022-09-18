'''
Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx 
e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.
'''

cpf = input("Digite um CPF no formato xxx.xxx.xxx-xx: ")

if len(cpf) == 14:
    if cpf[3] == '.':
        if cpf[7] == '.':
            if cpf[11] == '-':
                print("CPF está correto") 
            else:
                print("CPF sem o caractere '-'")   
        else:
            print("CPF sem o caractere '.'")    
    else:
        print("CPF sem o caractere '.'")
else:
    print("CPF inválido, coloque no formato xxx.xxx.xxx-xx")
        