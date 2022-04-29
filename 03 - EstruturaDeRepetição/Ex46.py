'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, 
o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada 
(retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados.
O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m'''

atletas = []
saltosAtletas = []

ordinais = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']

while True:
    ordinal = 1
    saltos = []
    atleta = input("\nQual o nome do atleta? ")
    if atleta == '':
        break
    atletas.append(atleta)

    while ordinal < 6:
        salto = float(input(f"Resultado do {ordinal}º salto: "))
        saltos.append(salto)
        ordinal += 1
    saltosAtletas.append(saltos)

for indice, nome in enumerate(atletas):
    print(f"\nAtleta: {nome}\n")

    melhorSalto = 0
    piorSalto = 9999999
    for indice2, i in enumerate(saltosAtletas[indice]):
        print(f'{ordinais[indice2]} Salto: {i} m')
        if i > melhorSalto:
            melhorSalto = i
        if i < piorSalto:
            piorSalto = i
    print(f"\nMelhor Salto: {melhorSalto} m")
    print(f"Pior salto: {piorSalto} m ")

    for i in saltosAtletas[indice]:
        if i == melhorSalto:
            saltosAtletas[indice].remove(i)
        if i == piorSalto:
            saltosAtletas[indice].remove(i)

    mediaSaltos = sum(saltosAtletas[indice])/3
    print(f"Média dos demais saltos: {mediaSaltos:.1f} m\n")

    print(f"Resultado Final:\n{nome}: {mediaSaltos:.1f}")
    print("-"*35)
