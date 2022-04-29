"""Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente."""

ma = float(input("Informe a quantidade (em Kg) de maçãs: \n"))
mo = float(input("Informe a quantidade (em Kg) de morangos: \n"))

desconto = 0

if ma <= 5:
    ValorMa = 1.8*ma
elif ma > 5:
    ValorMa = 1.5*ma

if mo <= 5:
    ValorMo = 2.5*mo
elif mo > 5:
    ValorMo = 1.5*mo

if (ma+mo) > 8 or (ValorMa + ValorMo) > 25:
    desconto =  (ValorMa + ValorMo)*10/100

print(f"O valor total a se pagar é {ValorMa + ValorMo - desconto}")