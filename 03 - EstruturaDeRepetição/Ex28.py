'''Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
O usuário deverá informar a quantidade de CDs e o valor para em cada um.'''

print("Você é um colecionador de CDs e queremos saber o valor total investido, vamos lá")

while True:
    qtde_cd = int(input("Qual a quatidade de CDs em sua coleção? "))
    if qtde_cd > 0:
        break
    else:
        print("Informe um valor positivo")
        continue

valorTotal = 0
i = 0
CDs = {}

while i < qtde_cd:
    i += 1
    valor_cd = float(input(f"Qual o valor gasto no Cd {i}? "))
    CDs[f"Cd {i}"] = valor_cd

for valor in CDs.values():
    valorTotal += valor

print("Os Cd's são: ")
for k in list(CDs.items()):
    print(k)

print("O valor total investido em seus {} Cd's foi de R${:,}\nE o valor médio gasto em cada um deles foi de R${:,.2f}\n".format(qtde_cd, valorTotal, valorTotal/qtde_cd))

