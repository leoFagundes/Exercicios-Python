'''O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, 
e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.'''

temperaturas = []

print("\nPara sair digite 'sair'")
while True:
    temp = input("Informe uma temperatura: ")
    if temp == 'sair':
        break
    try:
        temperaturas.append(float(temp))
    except:
        print("Essa temperatura está digitada incorretamente")
        continue

maiorT = -999999
menorT = 999999

for i in temperaturas:
    if i > maiorT:
        maiorT = i
    if i < menorT:
        menorT = i

print(f"A maior temperatura é {maiorT} graus, a menor é {menorT} graus.\nA média das temperaturas é {sum(temperaturas)/len(temperaturas):.2f} graus.")
