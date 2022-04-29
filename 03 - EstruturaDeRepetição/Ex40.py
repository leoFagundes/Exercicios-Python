'''Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:

Nome da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:

Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.'''

cidades = []
veiculos_passeio = []
acidentes_com_vitimas = []

i = 0
while i < 5:
    i += 1
    print("")
    cidade = input(f"Nome da cidade{i}: ")
    cidades.append(cidade)

    veiculo_passeio = int(input(f"Número de veículos de passeio na cidade {cidade}: "))
    veiculos_passeio.append(veiculo_passeio)

    acidente_com_vitima = int(input(f"Número de acidentes com vítimas na cidade {cidade}: "))
    acidentes_com_vitimas.append(acidente_com_vitima)

maior_acidentes = 0
indiceMaiorAcidentes = 0

menor_acidentes = 9999999*9
indiceMenorAcidentes = 0
for indice, k in enumerate(acidentes_com_vitimas):
    if  k > maior_acidentes:
        maior_acidentes = k
        indiceMaiorAcidentes = indice
    if k < menor_acidentes:
        menor_acidentes = k
        indiceMenorAcidentes = indice

print(f"O maior número de acidentes de transitos é {maior_acidentes} e pertence a cidade {cidades[indiceMaiorAcidentes]}")
print(f"O menor número de acidentes de transitos é {menor_acidentes} e pertence a cidade {cidades[indiceMenorAcidentes]}")

mediaVeiculosTotal = sum(veiculos_passeio)/len(veiculos_passeio)
print(f"A média de veículos nas 5 cidades é de {mediaVeiculosTotal:.2f}")

qtdeAcidente = 0
MediaAcidente = 0
for indice, x in enumerate(veiculos_passeio):
    if x < 2000:
        MediaAcidente += acidentes_com_vitimas[indice]
        qtdeAcidente += 1

print(f"A média de acidentes nas cidades com menos de 2000 veículos é {MediaAcidente/qtdeAcidente:.2f} acidentes")


