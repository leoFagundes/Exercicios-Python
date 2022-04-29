'''
Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. 
A sua nota fica sendo a média dos votos restantes. 
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, 
conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. 
Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
'''

notas = []

atleta = input("\nQual o nome do atleta? ")

i = 0
while i < 7:
    i += 1
    nota = float(input(f"Qual é a {i}ª nota? "))
    notas.append(nota)

melhorNota = -1
piorNota = 999
for i in notas:
    if i > melhorNota:
        melhorNota = i
    if i < piorNota:
        piorNota = i

print(f"\nAtleta: {atleta}")
for i in notas:
    print(f"Nota: {i}")

for i in notas:
    if i == melhorNota:
        notas.remove(i)
        break

for i in notas:
    if i == piorNota:
        notas.remove(i)
        break

media = sum(notas)/len(notas)
texto = f'''
Resultado Final:
Atleta: {atleta}
Melhor nota: {melhorNota}
Pior nota: {piorNota}
Média: {media:.2f}
'''
print(texto)



