'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
O resultado do atleta será determinado pela média dos cinco valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, 
os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. 
A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
'''

atletas = []
saltos = []

while True:
    if len(atletas) == 0:
        atleta = input("\nQual o nome do atleta? (p/sair: enter) ")
    else:
        atleta = input("\nQual o nome do próximo atleta? (p/sair: enter) ")

    if atleta == '':
        break
    else:
        atletas.append(atleta)
        salto = []
        for i in range(1, 6):
            salto.append(float(input(f"Distância do {i}º salto do atleta {atleta}: ")))
        saltos.append(salto)

for i, atleta in enumerate(atletas):
    print(f'''
    Atleta: {atleta}
 
    Primeiro Salto: {saltos[i][0]} m
    Segundo Salto: {saltos[i][1]} m
    Terceiro Salto: {saltos[i][2]} m
    Quarto Salto: {saltos[i][3]} m
    Quinto Salto: {saltos[i][4]} m

    Resultado final:
    Atleta: {atleta}
    Saltos: {saltos[i][0]} - {saltos[i][1]} - {saltos[i][2]} - {saltos[i][3]} - {saltos[i][4]}
    Média dos saltos: {sum(saltos[i])/len(saltos[i])} m
    ''')