'''
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. 
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, 
que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. 
Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação.
Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. 
O cálculo do valor a ser pago é feito da seguinte forma. 
Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
'''

def valorPagamento(valor, atraso):
    if atraso == 0:
        return valor
    else:
        valor += valor*3/100
        valor += valor*(atraso*0.1/100)
        return valor

prestacoes = []

while True: 
    listaProvisoria = []
    valor = float(input("\nValor a ser pago: (0 -> Sair) "))
    if valor == 0:
        break
    atraso = int(input("Atraso em dias: "))

    listaProvisoria.append(valor)
    listaProvisoria.append(atraso)
    prestacoes.append(listaProvisoria)

total = 0
print(f"\n{'Índice':^10}{'valor':^10}{'atraso':^10}{'Valor a ser Pago':^20}")
for i, prestacao in enumerate(prestacoes):
    valor = valorPagamento(prestacao[0], prestacao[1])
    print(f"{i+1:^10}{prestacao[0]:^10}{prestacao[1]:^10}{valor:^20}")
    total += valor
print('---------------------------------------------------')
print(f"{len(prestacoes):^10}{'':^10}{'':^10}{total:^20}")
    

