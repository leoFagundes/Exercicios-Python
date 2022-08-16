"""Utilize uma lista para resolver o problema a seguir. 
Uma empresa paga seus vendedores com base em comissões.
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. 
Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie na fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados."""

valorBase = 200
vendas = []

k = 0
while True:
    k += 1
    venda = float(input(f"O {k}º vendedor vendeu quanto nessa semana? (-1 para sair) "))
    if venda == -1:
        break
    venda = valorBase + 0.09*venda
    vendas.append(venda)

vendas.sort() #ordenar os valores da lista
print(vendas)

valorInicial = 200
valorFinal = 299

print("\n")
k = 0
while True:
    for x in vendas:
        if x >= valorInicial and x <= valorFinal:
            k += 1
    print(f"{valorInicial} - {valorFinal}: {k} vendedore(s)")

    valorInicial += 100
    valorFinal += 100

    k = 0
    if valorInicial >= 1000:
        for x in vendas:
            if x > valorInicial:
                k += 1
        print(f"1000 em diante: {k} vendedore(s)")
        break