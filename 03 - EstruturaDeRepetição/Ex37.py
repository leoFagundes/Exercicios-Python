'''Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, 
a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, 
sua altura e seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, 
além da média das alturas e dos pesos dos clientes'''


codigos = []
nomes = []
alturas = []
pesos = []

print("")

while True:
    codigo = int(input("Código do cliente: (digite '0' para sair) "))
    if codigo == 0:
        break
    codigos.append(codigo)

    nome = input("Nome do cliente: ")
    nomes.append(nome)

    altura = float(input(f"Altura do {nome}: "))
    alturas.append(altura)

    peso = float(input(f"Peso do {nome}: "))
    pesos.append(peso)

    print("")
    
alto = 0
baixo = 99*99

for i in alturas:
    if i > alto:
        alto = i
    if i < baixo:
        baixo = i

indiceAlto = 0
indiceBaixo = 0
for i, altura in enumerate(alturas):
    if altura == alto:
        indiceAlto = i
    if altura == baixo:
        indiceBaixo = i

gordo = 0
magro = 99*99

for i in pesos:
    if i > gordo:
        gordo = i
    if i < magro:
        magro = i

indiceGordo = 0
indiceMagro = 0
for i, peso in enumerate(pesos):
    if peso == gordo:
        indiceGordo = i
    if peso == magro:
        indiceGordo = i

mediaAlt = sum(alturas)/len(alturas)
mediaPeso = sum(pesos)/len(pesos)


print(nomes)
print(alturas)
print(pesos)

print(f"\nO cliente mais alto foi o {nomes[indiceAlto]} com {alto} metros de altura e pesando {pesos[indiceAlto]}kg")
print(f"O cliente mais baixo foi o {nomes[indiceBaixo]} com {baixo} metros de altura e pesando {pesos[indiceBaixo]}kg")

print(f"O cliente mais gordo foi o {nomes[indiceGordo]} com {alturas[indiceGordo]} metros de altura e pesando {gordo}kg")
print(f"O cliente mais magro foi o {nomes[indiceMagro]} com {alturas[indiceMagro]} metros de altura e pesando {magro}kg")

print(f"\nA média das alturas foi de {mediaAlt:.2f} metros")
print(f"A média dos pesos foi de {mediaPeso:.2f}kg")
