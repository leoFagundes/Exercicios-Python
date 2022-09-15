'''
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. 
Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. 
Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. 
Registre a informação A.M./P.M. como um valor "A" para A.M. e "P" para P.M. 
Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. 
Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
'''

def conversao(horas, minutos):
    turno = ''
    if horas >= 12:
        horas += 12
        horas -= 24
        turno = 'P.M.'
    elif horas < 12:
        turno = 'A.M.'
    return (horas, minutos, turno)

def saida():
    global horas, minutos
    novaHora, novoMinuto, turno = conversao(horas, minutos)
    print(f"Agora são {novaHora}:{novoMinuto} {turno}")

while True:
    horas = int(input("Horas: "))
    if horas > 24:
        print("Valor inválido.")
        continue
    minutos = int(input("Minutos: "))
    if minutos > 60:
        print("Valor inválido.")
        continue
    saida()
    print("")

    