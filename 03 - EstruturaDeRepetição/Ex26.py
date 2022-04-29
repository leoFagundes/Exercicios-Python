'''Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.'''

eleitores = int(input("Quantos eleitores temos? "))
i = 0
primeiro = 0
segundo = 0
terceiro = 0


while i < eleitores:
    i += 1
    votos = input(f"O eleitor {i} vota no primeiro - (p), segundo - (s) ou no terceiro - (t) candidato? ")
    votos.casefold().strip()
    if votos == 'p':
        primeiro += 1
    elif votos == 's':
        segundo += 1
    elif votos == 't':
        terceiro += 1

texto = f'''
O primeiro candidato teve {primeiro} votos
O segundo cadidato teve {segundo} votos
O terceiro candidato teve {terceiro} votos
'''
print(texto)
