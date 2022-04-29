'''Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
1, 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. 
Para finalizar o conjunto de votos tem-se o valor zero.'''

candidatos = '''
Os candidatos são:
1 - Leonardo
2 - Jose
3 - João
4 - Julia
nulo - Voto nulo
br - Voto em branco
'''
print(candidatos)

votos = []

while True:
    print("")
    voto = input("Em qual candidato deseja votar? [0] para encerrar os votos ")
    if voto == '0':
        break
    elif voto != '1' and voto != '2' and voto != '3' and voto != '4' and voto != 'nulo' and voto != 'br':
        print("Voto inválido.")
        continue
    votos.append(voto)

candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0

nulos = 0
emBranco = 0

for i in votos:
    if i == '1':
        candidato1 += 1
    elif i == '2':
        candidato2 += 1
    elif i == '3':
        candidato3 += 1
    elif i == '4':
        candidato4 += 1
    elif i == 'nulo':
        nulos += 1
    elif i == 'br':
        emBranco += 1

TextoFinal = f'''
O total de votos foi de {len(votos)},
Os candidatos tiveram os seguintes votos:
- Leonardo teve {candidato1} votos
- Jose teve {candidato2} votos
- João teve {candidato3} votos
- Julia teve {candidato4} votos

Tiveram {nulos} votos nulos, que significa {nulos/len(votos):.1%} do total de votos.
Tiveram {emBranco} votos em branco, que significa {emBranco/len(votos):.1%} do total de votos.
'''

print(TextoFinal)