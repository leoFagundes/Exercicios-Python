"""Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro

Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro 

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
(codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90."""

litros = float(input("Quantos litros deseja colocar? \n"))
combust = str(input("Qual o tipo de combústivel? A-álcool, G-gasolina\n"))


if combust == 'a' or combust == 'A':
    valor = 1.9
    if  litros <= 20:
        desconto = 3

    elif litros > 20:
        desconto = 5 

    combust = 'Àlcool'

if combust == 'g' or combust == 'G':
    valor = 2.5
    if  litros <= 20:
        desconto = 4

    elif litros > 20:
        desconto = 6

    combust = 'Gasolina'

print(f"O valor a pagar por {litros} litros de {combust} é: {(valor*litros) - (litros*desconto/100)} reais")