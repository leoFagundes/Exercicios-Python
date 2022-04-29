'''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.'''

PopA = 80000
PopB = 200000
ano = 0

while PopA < PopB:
    PopA += PopA*0.3
    PopB += PopB * 0.15
    ano += 1

print(f"A populção A demorou {ano} anos para ultrapassar a população B")
print("População A: {:,.2f}".format(PopA))
print("População B: {:,.2f}".format(PopB))
